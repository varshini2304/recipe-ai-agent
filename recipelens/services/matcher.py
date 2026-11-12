"""Task 2: explainable pantry-to-recipe matching.

Design in one paragraph: the matcher is a pure function of (pantry, constraints, preferences).
Hard constraints are applied in SQL *before* ranking and re-checked in Python afterwards, so a
violating recipe can never appear in the main results. Ranking is a three-term weighted score
(pantry coverage, completeness, step bonus) whose weights live in ``config/scoring.yaml``. If
nothing is eligible the report says so and lists *separate*, clearly labelled
``violating_alternatives``. No LLM is involved anywhere in this module.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path

import yaml

from recipelens.data.ingredients import parse_ingredient
from recipelens.services.ingredient_families import IngredientFamilies
from recipelens.services.taxonomy import IngredientTaxonomy
from recipelens.store.models import Filter, IngredientLine, RecipeRecord
from recipelens.store.repository import RecipeRepository

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "config"

_UNICODE_FRACTIONS = {
    "½": 0.5, "⅓": 1 / 3, "⅔": 2 / 3, "¼": 0.25, "¾": 0.75,
    "⅛": 0.125, "⅜": 0.375, "⅝": 0.625, "⅞": 0.875,
}  # fmt: skip


# --------------------------------------------------------------------------- input models


@dataclass(frozen=True, slots=True)
class PantryItem:
    """One ingredient the user has. ``qty``/``unit`` are optional (e.g. 2, 'cups')."""

    name: str
    qty: float | None = None
    unit: str | None = None


@dataclass(frozen=True, slots=True)
class Constraints:
    """Hard constraints. Never relaxed silently.

    ``exclude_ingredients`` are matched conservatively (family variants plus any canonical or raw
    line containing the word), because over-excluding is the safe direction for an allergy.
    ``excluded_groups`` are taxonomy groups (dairy, eggs, peanuts, ...); an *uncertain* taxonomy
    hit counts as a possible violation and is kept out of the main ranking.
    """

    exclude_ingredients: tuple[str, ...] = ()
    excluded_groups: tuple[str, ...] = ()
    max_steps: int | None = None
    step_metric: str = "step_count"
    exclude_low_confidence: bool = True  # only applies when max_steps is set

    def with_excluded(self, *terms: str) -> Constraints:
        """Follow-up helper: 'exclude eggs too' is just a new Constraints object."""
        merged = tuple(dict.fromkeys((*self.exclude_ingredients, *terms)))
        return replace(self, exclude_ingredients=merged)

    def with_excluded_groups(self, *groups: str) -> Constraints:
        merged = tuple(dict.fromkeys((*self.excluded_groups, *groups)))
        return replace(self, excluded_groups=merged)


@dataclass(frozen=True, slots=True)
class Preferences:
    """Soft preferences: they re-weight the score, they never filter."""

    prefer_fewer_missing: bool = False
    prefer_fewer_steps: bool = False
    assume_staples: bool | None = None  # None -> config/staples.yaml default


# -------------------------------------------------------------------------- output models


@dataclass(frozen=True, slots=True)
class PantryResolution:
    input_name: str
    canonical: str
    match_mode: str  # "family" (reviewed family rule) or "exact" (canonical equality)
    variant_count: int
    found_in_dataset: bool


@dataclass(frozen=True, slots=True)
class MatchedItem:
    pantry_name: str
    canonical: str
    recipe_lines: tuple[str, ...]
    quantity_check: str  # not_requested | sufficient | insufficient | not_verified
    quantity_note: str


@dataclass(frozen=True, slots=True)
class Violation:
    kind: str  # excluded_ingredient | taxonomy_group | possible_taxonomy_group | max_steps | ...
    detail: str
    lines: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class RecipeMatch:
    recipe_id: str
    title: str
    rank: int
    score: float
    score_breakdown: dict[str, float]
    matched: tuple[MatchedItem, ...]
    missing: tuple[str, ...]  # recipe lines the user must still obtain (non-staple, non-optional)
    assumed_staples: tuple[str, ...]
    optional_not_counted: tuple[str, ...]
    unused_pantry: tuple[str, ...]
    step_count: int
    step_metric: str
    instructions_low_confidence: bool
    ingredient_count: int
    quantity_check: str
    why: str
    ingredient_lines: tuple[str, ...]  # original ingredient lines, untouched
    instructions_raw: str | None  # original instructions, untouched
    violations: tuple[Violation, ...] = ()  # always empty for eligible results


@dataclass(frozen=True, slots=True)
class MatchReport:
    status: str  # "ok" | "no_eligible_match"
    results: tuple[RecipeMatch, ...]
    violating_alternatives: tuple[RecipeMatch, ...]
    pantry: tuple[PantryResolution, ...]
    constraints: dict
    preferences: dict
    effective_weights: dict[str, float]
    candidates_total: int
    candidates_scored: int
    truncated: bool
    low_confidence_excluded: int
    secondary_exclusions: int
    notes: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict:
        return asdict(self)


# ----------------------------------------------------------------------------- helpers


def parse_quantity(text: str | None) -> float | None:
    """Parse '2', '1/2', '1 1/2', '1½', '0.5'. Anything else (ranges, words) -> None."""
    if text is None or not text.strip():
        return None
    cleaned = text.strip()
    for glyph, value in _UNICODE_FRACTIONS.items():
        cleaned = cleaned.replace(glyph, f" {value} ")
    total = 0.0
    for token in cleaned.split():
        try:
            if "/" in token:
                top, bottom = token.split("/", maxsplit=1)
                total += float(top) / float(bottom)
            else:
                total += float(token)
        except (ValueError, ZeroDivisionError):
            return None
    return total


@dataclass(frozen=True, slots=True)
class _Resolved:
    item: PantryItem
    canonical: str
    unit: str | None
    variants: frozenset[str]
    mode: str


@dataclass(frozen=True, slots=True)
class _TermRule:
    term: str
    canonicals: frozenset[str]
    regex: re.Pattern[str]


@dataclass(frozen=True, slots=True)
class _Exclusions:
    terms: tuple[_TermRule, ...]
    group_canonicals: dict[str, frozenset[str]]

    def blocked_canonicals(self) -> tuple[str, ...]:
        blocked: set[str] = set()
        for rule in self.terms:
            blocked |= rule.canonicals
        for values in self.group_canonicals.values():
            blocked |= values
        return tuple(sorted(blocked))


# ------------------------------------------------------------------------------ matcher


class Matcher:
    def __init__(
        self,
        repository: RecipeRepository,
        taxonomy: IngredientTaxonomy | None = None,
        families: IngredientFamilies | None = None,
        *,
        config_dir: Path = CONFIG,
    ) -> None:
        self.repository = repository
        self.taxonomy = taxonomy or IngredientTaxonomy(repository=repository)
        self.families = families or IngredientFamilies(repository)
        load = lambda name: yaml.safe_load((config_dir / name).read_text(encoding="utf-8")) or {}
        self.scoring = load("scoring.yaml")
        staples = load("staples.yaml")
        self.staple_patterns = tuple(re.compile(p, re.IGNORECASE) for p in staples["patterns"])
        self.assume_staples_default = bool(staples.get("assume_staples_default", True))
        self.optional_patterns = tuple(
            re.compile(p, re.IGNORECASE) for p in self.scoring.get("optional_patterns", [])
        )
        self.quantities = load("quantities.yaml")
        self.unit_aliases = {
            str(k).casefold(): str(v).casefold() for k, v in load("units.yaml")["units"].items()
        }
        self._known_canonicals: frozenset[str] | None = None
        # Scrape noise (e.g. a trailing 'ADVERTISEMENT') is hidden in displayed lines only;
        # ingredient_lines keeps the original text untouched.
        self.noise_patterns = tuple(
            re.compile(p) for p in load("cleaning.yaml").get("noise_patterns", [])
        )

    # ------------------------------------------------------------------ public API

    def match(
        self,
        pantry: list[PantryItem] | tuple[PantryItem, ...],
        constraints: Constraints = Constraints(),  # noqa: B008
        preferences: Preferences = Preferences(),  # noqa: B008
        top_k: int | None = None,
    ) -> MatchReport:
        """Rank existing recipes against a pantry. Pure: same inputs -> same report."""
        if not pantry:
            raise ValueError("pantry must contain at least one ingredient")
        top_k = int(self.scoring.get("default_top_k", 5)) if top_k is None else top_k
        if top_k < 1:
            raise ValueError("top_k must be >= 1")
        if constraints.step_metric not in {"step_count", "sentence_count"}:
            raise ValueError("step_metric must be 'step_count' or 'sentence_count'")
        for group in constraints.excluded_groups:
            if group not in self.taxonomy.group_names():
                raise KeyError(
                    f"Unknown taxonomy group {group!r}; known: {', '.join(self.taxonomy.group_names())}"
                )

        resolved = self._resolve_pantry(pantry)
        rules = self._exclusions(constraints)
        assume_staples = (
            self.assume_staples_default
            if preferences.assume_staples is None
            else preferences.assume_staples
        )
        weights = self._weights(preferences)
        notes: list[str] = []
        for r in resolved:
            if not r.variants & self._known():
                notes.append(
                    f"'{r.item.name}' (canonical '{r.canonical}') does not appear as an ingredient "
                    "in any recipe; check the spelling or try a more common name."
                )

        # 1) hard constraints in SQL, then a Python re-check (defence in depth)
        step_limited = constraints.max_steps is not None
        recipe_filter = Filter(
            max_steps=constraints.max_steps,
            step_metric=constraints.step_metric,  # type: ignore[arg-type]
            exclude_low_confidence=step_limited and constraints.exclude_low_confidence,
        )
        groups = tuple(tuple(sorted(r.variants)) for r in resolved)
        cap = int(self.scoring["candidate_cap"])
        ids, total = self.repository.top_overlap_ids(
            groups,
            recipe_filter,
            excluded_canonical=rules.blocked_canonicals(),
            require_instructions=step_limited,
            min_overlap=int(self.scoring.get("min_matched_pantry_items", 1)),
            limit=cap,
        )
        scored, secondary = self._score_candidates(
            [rid for rid, _ in ids], resolved, constraints, rules, weights, assume_staples
        )
        eligible = [m for m in scored if not m[0].violations]
        # A candidate that passed SQL but failed the Python re-check is dropped, never shown as eligible.
        eligible_sorted = self._rank(eligible)[:top_k]
        results = tuple(replace(m, rank=i) for i, (m, _) in enumerate(eligible_sorted, 1))

        low_conf = 0
        if step_limited and constraints.exclude_low_confidence:
            low_conf = self.repository.count_low_confidence(
                Filter(
                    include_ingredients=tuple(r.canonical for r in resolved),
                    include_mode="any",
                    max_steps=constraints.max_steps,
                    step_metric=constraints.step_metric,  # type: ignore[arg-type]
                ),
                excluded_canonical=rules.blocked_canonicals(),
                include_variants=groups,
                require_ingredients=True,
                require_instructions=True,
            )
            notes.append(
                f"{low_conf} otherwise-eligible recipe(s) were excluded from the step-limited "
                "ranking because their instructions are low-confidence (very short or no "
                "action words), so their step count cannot be trusted."
            )

        # 2) nothing eligible -> say so, and separately offer clearly-marked violators
        alternatives: tuple[RecipeMatch, ...] = ()
        status = "ok"
        if not results:
            status = "no_eligible_match"
            notes.append(
                "No recipe satisfies every hard constraint. The constraints were NOT relaxed; "
                "any recipes listed under violating_alternatives break at least one of them."
            )
            alt_ids, _alt_total = self.repository.top_overlap_ids(
                groups,
                Filter(),
                min_overlap=int(self.scoring.get("min_matched_pantry_items", 1)),
                limit=int(self.scoring["alternatives"]["candidate_cap"]),
            )
            alt_scored, _ = self._score_candidates(
                [rid for rid, _ in alt_ids], resolved, constraints, rules, weights, assume_staples
            )
            violators = [m for m in alt_scored if m[0].violations]
            ordered = sorted(
                violators,
                key=lambda m: (
                    len({v.kind for v in m[0].violations}),
                    -m[1],
                    len(m[0].missing),
                    m[0].step_count,
                    m[0].recipe_id,
                ),
            )[: int(self.scoring["alternatives"]["max_results"])]
            alternatives = tuple(replace(m, rank=i) for i, (m, _) in enumerate(ordered, 1))
            if not alternatives:
                notes.append("No recipe in the dataset uses any of the listed ingredients.")

        if constraints.exclude_ingredients:
            notes.append(
                "Excluded ingredients are matched conservatively (reviewed family variants plus "
                "any ingredient line containing the word), so recipes are over-excluded rather "
                "than risk a violation. This is text matching, not medical advice."
            )
        if step_limited:
            notes.append(
                f"Step limit uses {constraints.step_metric} (newline-separated blocks; a single "
                "block is split into sentences). Recipes without instructions are excluded."
            )
        if total > cap:
            notes.append(
                f"{total} recipes use at least one of your ingredients; the {cap} with the most "
                "matches (then fewest ingredients) were scored."
            )
        if any(r.item.qty is not None for r in resolved):
            notes.append(
                "Quantities are compared as written in the recipe (servings are not scaled) and "
                "only when units are convertible; otherwise the match is by name and quantity "
                "sufficiency is reported as not verified."
            )
        if assume_staples:
            notes.append("Staples (salt, pepper, water, cooking oil) are assumed on hand and listed per recipe.")

        return MatchReport(
            status=status,
            results=results,
            violating_alternatives=alternatives,
            pantry=tuple(
                PantryResolution(
                    r.item.name, r.canonical, r.mode, len(r.variants), bool(r.variants & self._known())
                )
                for r in resolved
            ),
            constraints=asdict(constraints),
            preferences={**asdict(preferences), "assume_staples": assume_staples},
            effective_weights={k: round(v, 4) for k, v in weights.items()},
            candidates_total=total,
            candidates_scored=len(scored),
            truncated=total > cap,
            low_confidence_excluded=low_conf,
            secondary_exclusions=secondary,
            notes=tuple(notes),
        )

    # ---------------------------------------------------------------- resolution

    def _known(self) -> frozenset[str]:
        if self._known_canonicals is None:
            self._known_canonicals = frozenset(
                c for c, _ in self.repository.canonical_counts(limit=None)
            )
        return self._known_canonicals

    def _display(self, raw: str) -> str:
        text = raw
        for pattern in self.noise_patterns:
            text = pattern.sub("", text)
        return text.strip()

    def _normalize_unit(self, unit: str | None) -> str | None:
        if unit is None or not unit.strip():
            return None
        key = unit.strip().rstrip(".").casefold()
        return self.unit_aliases.get(key, key)

    def _resolve_pantry(self, pantry: list[PantryItem] | tuple[PantryItem, ...]) -> list[_Resolved]:
        resolved: dict[str, _Resolved] = {}
        for item in pantry:
            if not item.name.strip():
                continue
            canonical = parse_ingredient(item.name).canonical
            if canonical in resolved:
                continue  # the same ingredient listed twice counts once
            variants = self.families.variants(canonical)
            family = len(variants) != 1 or variants[0] != canonical
            resolved[canonical] = _Resolved(
                item=item,
                canonical=canonical,
                unit=self._normalize_unit(item.unit),
                variants=frozenset(variants),
                mode="family" if family else "exact",
            )
        if not resolved:
            raise ValueError("pantry must contain at least one non-empty ingredient name")
        return list(resolved.values())

    def _exclusions(self, constraints: Constraints) -> _Exclusions:
        known = self.repository.canonical_counts(limit=None)
        rules = []
        for term in dict.fromkeys(t.strip().casefold() for t in constraints.exclude_ingredients):
            if not term:
                continue
            canonical = parse_ingredient(term).canonical
            forms = sorted({re.escape(term), re.escape(canonical)}, key=len, reverse=True)
            regex = re.compile(rf"\b(?:{'|'.join(forms)})(?:e?s)?\b", re.IGNORECASE)
            canonicals = set(self.families.variants(canonical))
            canonicals.update(c for c, _ in known if regex.search(c))
            rules.append(_TermRule(term, frozenset(canonicals), regex))
        group_sets = {
            g: frozenset(self.taxonomy.canonical_ids_for_group(g, include_uncertain=True))
            for g in constraints.excluded_groups
        }
        return _Exclusions(tuple(rules), group_sets)

    # ------------------------------------------------------------------- scoring

    def _weights(self, preferences: Preferences) -> dict[str, float]:
        weights = {k: float(v) for k, v in self.scoring["weights"].items()}
        multipliers = self.scoring.get("preference_multipliers", {})
        for flag in ("prefer_fewer_missing", "prefer_fewer_steps"):
            if getattr(preferences, flag):
                for key, factor in multipliers.get(flag, {}).items():
                    weights[key] *= float(factor)
        total = sum(weights.values())
        return {k: v / total for k, v in weights.items()}

    def _score_candidates(
        self,
        recipe_ids: list[str],
        resolved: list[_Resolved],
        constraints: Constraints,
        rules: _Exclusions,
        weights: dict[str, float],
        assume_staples: bool,
    ) -> tuple[list[tuple[RecipeMatch, float]], int]:
        records = self.repository.recipes_for_ids(recipe_ids)
        lines_by_id = self.repository.ingredient_lines_for(recipe_ids)
        scored: list[tuple[RecipeMatch, float]] = []
        secondary = 0
        for recipe_id in recipe_ids:
            record = records.get(recipe_id)
            if record is None or not record.title:
                continue
            lines = lines_by_id.get(recipe_id, ())
            violations = self._violations(record, lines, constraints, rules)
            match, raw_score = self._score_one(
                record, lines, resolved, weights, assume_staples, constraints.step_metric
            )
            if violations:
                match = replace(match, violations=tuple(violations))
                secondary += 1
            scored.append((match, raw_score))
        return scored, secondary

    def _score_one(
        self,
        record: RecipeRecord,
        lines: tuple[IngredientLine, ...],
        resolved: list[_Resolved],
        weights: dict[str, float],
        assume_staples: bool,
        metric: str = "step_count",
    ) -> tuple[RecipeMatch, float]:
        matched_lines: dict[int, list[IngredientLine]] = {}
        missing, staples, optional = [], [], []
        for line in lines:
            hits = [i for i, r in enumerate(resolved) if line.canonical in r.variants]
            if hits:
                for i in hits:
                    matched_lines.setdefault(i, []).append(line)
            elif assume_staples and any(p.search(line.canonical) for p in self.staple_patterns):
                staples.append(self._display(line.raw))
            elif any(p.search(line.raw) for p in self.optional_patterns):
                optional.append(self._display(line.raw))
            else:
                missing.append(self._display(line.raw))

        matched_items, credit, unused = [], 0.0, []
        for i, r in enumerate(resolved):
            hit_lines = matched_lines.get(i)
            if not hit_lines:
                unused.append(r.item.name)
                continue
            check, note = self._quantity_check(r, hit_lines)
            credit += float(self.scoring["insufficient_quantity_credit"]) if check == "insufficient" else 1.0
            matched_items.append(
                MatchedItem(
                    r.item.name,
                    r.canonical,
                    tuple(self._display(x.raw) for x in hit_lines),
                    check,
                    note,
                )
            )

        matched_line_count = len({x.position for hit in matched_lines.values() for x in hit})
        required = matched_line_count + len(missing)
        coverage = credit / len(resolved)
        completeness = 1.0 - (len(missing) / required) if required else 1.0
        steps = getattr(record, metric) if record.has_instructions else None
        cap = float(self.scoring["step_cap"])
        step_bonus = max(0.0, 1.0 - steps / cap) if steps is not None else 0.0
        parts = {"coverage": coverage, "completeness": completeness, "steps": step_bonus}
        score = sum(weights[k] * parts[k] for k in parts)

        qty_checks = [m.quantity_check for m in matched_items if m.quantity_check != "not_requested"]
        if not qty_checks:
            recipe_qty = "no_quantities_given"
        elif "insufficient" in qty_checks:
            recipe_qty = "insufficient"
        elif all(c == "sufficient" for c in qty_checks):
            recipe_qty = "sufficient"
        elif all(c == "not_verified" for c in qty_checks):
            recipe_qty = "not_verified"
        else:
            recipe_qty = "partially_verified"

        names = ", ".join(m.pantry_name for m in matched_items) or "none"
        extra = f" ({', '.join(missing[:4])}{', …' if len(missing) > 4 else ''})" if missing else ""
        why = (
            f"Uses {len(matched_items)}/{len(resolved)} of your ingredients ({names}); needs "
            f"{len(missing)} more non-staple ingredient(s){extra}; "
            f"{steps if steps is not None else 'no'} instruction {metric.replace('_count', '')}(s). "
            f"Score {score:.3f} = {weights['coverage']:.2f}×{coverage:.2f} coverage + "
            f"{weights['completeness']:.2f}×{completeness:.2f} completeness + "
            f"{weights['steps']:.2f}×{step_bonus:.2f} step bonus."
        )
        match = RecipeMatch(
            recipe_id=record.recipe_id,
            title=record.title or "",
            rank=0,
            score=round(score, 6),
            score_breakdown={
                "coverage": round(coverage, 6),
                "completeness": round(completeness, 6),
                "step_bonus": round(step_bonus, 6),
                "weighted_coverage": round(weights["coverage"] * coverage, 6),
                "weighted_completeness": round(weights["completeness"] * completeness, 6),
                "weighted_steps": round(weights["steps"] * step_bonus, 6),
            },
            matched=tuple(matched_items),
            missing=tuple(missing),
            assumed_staples=tuple(staples),
            optional_not_counted=tuple(optional),
            unused_pantry=tuple(unused),
            step_count=getattr(record, metric),
            step_metric=metric,
            instructions_low_confidence=record.instructions_low_confidence,
            ingredient_count=record.ingredient_count,
            quantity_check=recipe_qty,
            why=why,
            ingredient_lines=tuple(x.raw for x in lines),
            instructions_raw=record.instructions_raw,
        )
        return match, round(score, 6)

    @staticmethod
    def _rank(
        scored: list[tuple[RecipeMatch, float]],
    ) -> list[tuple[RecipeMatch, float]]:
        """Deterministic order: score desc, fewer missing, fewer steps, recipe_id."""
        return sorted(
            scored,
            key=lambda m: (-m[1], len(m[0].missing), m[0].step_count, m[0].recipe_id),
        )

    # ---------------------------------------------------------------- quantities

    def _convert(self, amount: float, from_unit: str | None, to_unit: str | None) -> float | None:
        if from_unit == to_unit:
            return amount
        for factors in self.quantities["families"].values():
            if from_unit in factors and to_unit in factors:
                return amount * float(factors[from_unit]) / float(factors[to_unit])
        return None

    def _quantity_check(self, r: _Resolved, lines: list[IngredientLine]) -> tuple[str, str]:
        if r.item.qty is None:
            return "not_requested", ""
        needed = 0.0
        for line in lines:
            amount = parse_quantity(line.qty)
            if amount is None:
                return "not_verified", f"recipe line '{line.raw}' has no usable quantity"
            converted = self._convert(amount, self._normalize_unit(line.unit), r.unit)
            if converted is None:
                return (
                    "not_verified",
                    (
                        f"cannot compare recipe unit '{line.unit or 'count'}' with your unit "
                        f"'{r.unit or 'count'}' for '{line.raw}'"
                    ),
                )
            needed += converted
        unit_label = r.unit or "(count)"
        tolerance = float(self.quantities.get("tolerance", 1e-4))
        if r.item.qty + tolerance >= needed:
            return "sufficient", f"have {r.item.qty:g} {unit_label}, recipe needs {needed:g}"
        return (
            "insufficient",
            f"have {r.item.qty:g} {unit_label}, recipe needs {needed:g} (short by {needed - r.item.qty:g})",
        )

    # --------------------------------------------------------------- constraints

    def _violations(
        self,
        record: RecipeRecord,
        lines: tuple[IngredientLine, ...],
        constraints: Constraints,
        rules: _Exclusions,
    ) -> list[Violation]:
        found: list[Violation] = []
        for rule in rules.terms:
            hit = [x.raw for x in lines if x.canonical in rule.canonicals or rule.regex.search(x.raw)]
            if hit:
                found.append(Violation("excluded_ingredient", f"contains excluded '{rule.term}'", tuple(hit)))
        for group in constraints.excluded_groups:
            sure, maybe = [], []
            for x in lines:
                status = self.taxonomy.classify(x.canonical, group).status
                if status == "match":
                    sure.append(x.raw)
                elif status == "uncertain":
                    maybe.append(x.raw)
            if sure:
                found.append(Violation("taxonomy_group", f"contains {group}", tuple(sure)))
            elif maybe:
                found.append(
                    Violation("possible_taxonomy_group", f"possibly contains {group}", tuple(maybe))
                )
        if constraints.max_steps is not None:
            value = record.step_count if constraints.step_metric == "step_count" else record.sentence_count
            if not record.has_instructions:
                found.append(Violation("no_instructions", "no instructions, so the step limit cannot be verified"))
            elif value > constraints.max_steps:
                found.append(
                    Violation("max_steps", f"{constraints.step_metric}={value} exceeds limit {constraints.max_steps}")
                )
            elif constraints.exclude_low_confidence and record.instructions_low_confidence:
                found.append(
                    Violation(
                        "low_confidence_instructions",
                        "instructions are too short/unclear to trust the step count",
                    )
                )
        return found
