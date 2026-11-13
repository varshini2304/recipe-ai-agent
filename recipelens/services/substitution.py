"""Mine cautious ingredient substitution evidence from same-dish recipe peers.

All peer retrieval, frequency calculations, filtering, and text edits are deterministic. Culinary
role notes come from config/roles.yaml and are explicitly reported as unverified predictions.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml

from recipelens.services.ingredient_families import IngredientFamilies
from recipelens.services.matcher import Constraints
from recipelens.services.search import HybridSearch
from recipelens.services.taxonomy import IngredientTaxonomy
from recipelens.store.models import DEFAULT_FILTER, IngredientLine, RecipeRecord
from recipelens.store.repository import RecipeRepository

ROOT = Path(__file__).resolve().parents[2]
SUBSTITUTION_CONFIG = ROOT / "config" / "substitution.yaml"
ROLES_CONFIG = ROOT / "config" / "roles.yaml"
STORE_CONFIG = ROOT / "config" / "store.yaml"


@dataclass(frozen=True, slots=True)
class PeerRecipe:
    recipe_id: str
    title: str
    rank: int
    retrieval_score: float
    title_overlap: int
    ingredient_lines: tuple[IngredientLine, ...]


@dataclass(frozen=True, slots=True)
class PeerSearchReport:
    target_recipe_id: str
    query: str
    retrieval_mode: str
    peers: tuple[PeerRecipe, ...]

    @property
    def n_peers(self) -> int:
        return len(self.peers)


@dataclass(frozen=True, slots=True)
class CandidateEvidence:
    canonical: str
    with_count: int
    without_count: int
    with_rate: float
    without_rate: float
    frequency_difference: float
    lift: float
    evidence_score: float
    evidence_grade: str
    with_recipe_ids: tuple[str, ...]
    support_recipe_ids: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class SubstitutionReport:
    target_recipe_id: str
    target_title: str
    remove: str
    remove_group: str | None
    removed_lines: tuple[str, ...]
    n_peers: int
    with_x_count: int
    without_x_count: int
    retrieval_mode: str
    indirect: bool
    direct_peer_count: int
    peer_recipe_ids: tuple[str, ...]
    candidates: tuple[CandidateEvidence, ...]
    conflicting_signals: tuple[CandidateEvidence, ...]
    evidence_grade: str
    thresholds: dict[str, int | float]
    restrictions: dict[str, object]
    rejected_for_final_restrictions: tuple[str, ...]
    formula: str
    notes: tuple[str, ...]

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class IngredientChange:
    original_line: str
    replacement: str | None
    evidence_grade: str


@dataclass(frozen=True, slots=True)
class SubstitutionPlan:
    report: SubstitutionReport
    original_ingredients: tuple[str, ...]
    updated_ingredients: tuple[str, ...]
    changes: tuple[IngredientChange, ...]
    original_instructions: str
    revised_instructions: str
    predicted_effects: tuple[str, ...]
    uncertainty: tuple[str, ...]
    disclaimer: str

    def to_dict(self) -> dict:
        return asdict(self)


def grade_evidence(
    *,
    n_with: int,
    n_without: int,
    with_count: int,
    without_count: int,
    thresholds: dict,
    alpha: float,
) -> tuple[str, float, float, float, float]:
    """Grade a candidate from peer support, smoothed frequencies, difference, and lift."""
    with_rate = (with_count + alpha) / (n_with + 2 * alpha) if n_with else 0.0
    without_rate = (without_count + alpha) / (n_without + 2 * alpha) if n_without else 0.0
    difference = without_rate - with_rate
    lift = without_rate / with_rate if with_rate else 0.0
    strong = thresholds["evidence_grades"]["strong"]
    weak = thresholds["evidence_grades"]["weak"]
    conflict = thresholds["evidence_grades"]["conflicting"]
    if n_with < int(thresholds.get("minimum_peer_support", 0)) or n_without < int(
        thresholds.get("minimum_peer_support", 0)
    ):
        grade = "none"
    elif (
        n_with >= conflict["min_peer_support_each"]
        and n_without >= conflict["min_peer_support_each"]
        and difference <= -float(conflict["min_frequency_difference"])
    ):
        grade = "conflicting"
    elif (
        n_with >= strong["min_peer_support_each"]
        and n_without >= strong["min_peer_support_each"]
        and without_count >= strong["min_candidate_support"]
        and difference >= strong["min_frequency_difference"]
        and lift >= strong["min_lift"]
    ):
        grade = "strong"
    elif (
        n_with >= weak["min_peer_support_each"]
        and n_without >= weak["min_peer_support_each"]
        and without_count >= weak["min_candidate_support"]
        and difference >= weak["min_frequency_difference"]
        and lift >= weak["min_lift"]
    ):
        grade = "weak"
    else:
        grade = "none"
    return grade, with_rate, without_rate, difference, lift


class SubstitutionService:
    """Retrieve comparable recipes, mine candidate ingredients, and build a cautious plan."""

    def __init__(
        self,
        repository: RecipeRepository,
        taxonomy: IngredientTaxonomy | None = None,
        hybrid_search: HybridSearch | None = None,
        *,
        config_path: Path = SUBSTITUTION_CONFIG,
        roles_path: Path = ROLES_CONFIG,
        store_config_path: Path = STORE_CONFIG,
    ) -> None:
        self.repository = repository
        self.taxonomy = taxonomy or IngredientTaxonomy(repository=repository)
        self.families = IngredientFamilies(repository)
        self.hybrid_search = hybrid_search
        self.config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        self.roles = yaml.safe_load(roles_path.read_text(encoding="utf-8")) or {}
        self.store_config = yaml.safe_load(store_config_path.read_text(encoding="utf-8")) or {}
        self._query_excludes = tuple(
            re.compile(pattern, re.IGNORECASE)
            for pattern in self.config.get("peer_query_exclude_patterns", [])
        )
        self._remove_patterns = {
            name.casefold(): (
                tuple(re.compile(p, re.IGNORECASE) for p in rule.get("match_patterns", [])),
                tuple(re.compile(p, re.IGNORECASE) for p in rule.get("exclude_patterns", [])),
            )
            for name, rule in self.config.get("remove_ingredient_patterns", {}).items()
        }

    def _remove_group(self, remove: str) -> str | None:
        term = remove.strip().casefold()
        group = self.config.get("remove_group_aliases", {}).get(term, term)
        return group if group in self.taxonomy.group_names() else None

    def _matches_removed(self, line: IngredientLine, remove: str, group: str | None) -> bool:
        if group:
            return self.taxonomy.classify(line.canonical, group).status in {"match", "uncertain"}
        key = remove.casefold().strip()
        patterns = self._remove_patterns.get(key) or self._remove_patterns.get(
            self.config.get("remove_group_aliases", {}).get(key, ""),
        )
        if patterns:
            includes, excludes = patterns
            value = line.canonical
            return not any(p.search(value) for p in excludes) and any(
                p.search(value) for p in includes
            )
        token = re.compile(rf"(?<!\w){re.escape(key)}s?(?!\w)", re.IGNORECASE)
        return bool(token.search(line.canonical))

    @staticmethod
    def _title_tokens(title: str) -> set[str]:
        return set(re.findall(r"[a-z0-9]+", title.casefold()))

    def _peer_query(
        self,
        recipe: RecipeRecord,
        lines: tuple[IngredientLine, ...],
        remove: str | None = None,
    ) -> str:
        selected = []
        for line in lines:
            canonical = line.canonical.strip()
            if remove and self._matches_removed(line, remove, self._remove_group(remove)):
                continue
            if not canonical or any(pattern.search(canonical) for pattern in self._query_excludes):
                continue
            if canonical.casefold() not in {item.casefold() for item in selected}:
                selected.append(canonical)
            if len(selected) >= int(self.config["peer_query_ingredient_limit"]):
                break
        return " ".join(part for part in (recipe.title or "", *selected) if part)

    def find_peer_recipes(self, recipe_id: str, remove: str | None = None) -> PeerSearchReport:
        """Find same-dish peers; use vectors only when metadata says the index is complete."""
        target = self.repository.get_recipe(recipe_id)
        if target is None:
            raise KeyError(f"Recipe {recipe_id!r} was not found")
        target_lines = self.repository.ingredient_lines_for((recipe_id,))[recipe_id]
        query = self._peer_query(target, target_lines, remove)
        wanted = int(self.config["peer_pool_size"]) + 1
        indexed, full = (0, 0)
        if self.hybrid_search is not None:
            indexed, full = self.hybrid_search.index_coverage
        use_vector = self.hybrid_search is not None and full > 0 and indexed >= full
        if use_vector:
            found = self.hybrid_search.search(query, top_k=wanted)
            ids = [item.recipe_id for item in found if item.recipe_id != recipe_id]
            rows = [
                (item.recipe_id, item.title, item.score)
                for item in found
                if item.recipe_id != recipe_id
            ]
            backend = str(self.store_config.get("vector_backend", "numpy")).upper()
            retrieval_mode = f"FTS5 + full {backend} vector index (hybrid reciprocal-rank fusion)"
        else:
            found = self.repository.fts_search(
                query,
                DEFAULT_FILTER,
                wanted,
                title_weight=float(self.store_config["fts_title_weight"]),
                ingredient_weight=float(self.store_config["fts_ingredients_weight"]),
            )
            rows = [
                (item.recipe_id, item.title, 1.0 / (int(self.store_config["rrf_k"]) + rank))
                for rank, item in enumerate(found, 1)
                if item.recipe_id != recipe_id
            ]
            ids = [row[0] for row in rows]
            retrieval_mode = "FTS5 only (vector index incomplete or unavailable)"
        line_map = self.repository.ingredient_lines_for(ids)
        target_tokens = self._title_tokens(target.title or "")
        peers = []
        for rank, (peer_id, title, score) in enumerate(rows, 1):
            overlap = len(target_tokens & self._title_tokens(title))
            peers.append(PeerRecipe(peer_id, title, rank, float(score), overlap, line_map[peer_id]))
        return PeerSearchReport(recipe_id, query, retrieval_mode, tuple(peers))

    def _candidate_allowed(
        self,
        canonical: str,
        restrictions: Constraints,
        remove: str,
        remove_group: str | None,
        already_present: set[str],
    ) -> bool:
        if canonical in already_present:
            return False
        if self._matches_removed(
            IngredientLine("", 0, canonical, canonical, None, None, canonical, None),
            remove,
            remove_group,
        ):
            return False
        excluded_groups = set(restrictions.excluded_groups)
        if remove_group:
            excluded_groups.add(remove_group)
        for group in excluded_groups:
            if self.taxonomy.classify(canonical, group).status in {"match", "uncertain"}:
                return False
        for term in restrictions.exclude_ingredients:
            variants = set(self.families.variants(term))
            if canonical in variants or re.search(
                rf"(?<!\w){re.escape(term)}s?(?!\w)", canonical, re.IGNORECASE
            ):
                return False
        return True

    def _final_restriction_violations(
        self,
        lines: tuple[IngredientLine, ...],
        removed: tuple[IngredientLine, ...],
        replacement: str,
        restrictions: Constraints,
        remove: str,
        remove_group: str | None,
    ) -> tuple[str, ...]:
        removed_positions = {line.position for line in removed}
        remaining = [line.canonical for line in lines if line.position not in removed_positions]
        if replacement:
            remaining.append(replacement)
        violations: list[str] = []
        groups = set(restrictions.excluded_groups)
        if remove_group:
            groups.add(remove_group)
        for group in sorted(groups):
            hits = [
                name
                for name in remaining
                if self.taxonomy.classify(name, group).status in {"match", "uncertain"}
            ]
            if hits:
                violations.append(f"{group}: {', '.join(hits)}")
        for term in restrictions.exclude_ingredients:
            hits = [
                name
                for name in remaining
                if re.search(rf"(?<!\w){re.escape(term)}s?(?!\w)", name, re.IGNORECASE)
            ]
            if hits:
                violations.append(f"{term}: {', '.join(hits)}")
        if not remove_group and any(
            self._matches_removed(
                IngredientLine("", 0, name, name, None, None, name, None), remove, None
            )
            for name in remaining
        ):
            violations.append(f"removed ingredient remains: {remove}")
        return tuple(violations)

    def mine_substitutes(
        self,
        recipe_id: str,
        remove: str,
        restrictions: Constraints | None = None,
    ) -> SubstitutionReport:
        """Compare ingredient frequencies in peer recipes with and without the removed item."""
        restrictions = restrictions or Constraints()
        target = self.repository.get_recipe(recipe_id)
        if target is None:
            raise KeyError(f"Recipe {recipe_id!r} was not found")
        lines = self.repository.ingredient_lines_for((recipe_id,))[recipe_id]
        remove_group = self._remove_group(remove)
        removed = tuple(line for line in lines if self._matches_removed(line, remove, remove_group))
        removed_positions = {line.position for line in removed}
        already_present = {
            line.canonical for line in lines if line.position not in removed_positions
        }
        peers = self.find_peer_recipes(recipe_id, remove)
        with_peers = [
            peer
            for peer in peers.peers
            if any(
                self._matches_removed(line, remove, remove_group) for line in peer.ingredient_lines
            )
        ]
        with_ids = {peer.recipe_id for peer in with_peers}
        without_peers = [peer for peer in peers.peers if peer.recipe_id not in with_ids]
        with_count, without_count = len(with_peers), len(without_peers)
        without_ids = {peer.recipe_id for peer in without_peers}

        occurrences: dict[str, set[str]] = {}
        for peer in peers.peers:
            for canonical in {line.canonical for line in peer.ingredient_lines}:
                occurrences.setdefault(canonical, set()).add(peer.recipe_id)

        alpha = float(self.config["laplace_alpha"])
        candidates: list[CandidateEvidence] = []
        conflicts: list[CandidateEvidence] = []
        rejected: set[str] = set()
        thresholds = {
            "peer_pool_size": int(self.config["peer_pool_size"]),
            "minimum_peer_support": int(self.config["minimum_peer_support"]),
            "minimum_candidate_support": int(self.config["minimum_candidate_support"]),
            "laplace_alpha": alpha,
            "max_lift_for_score": float(self.config["max_lift_for_score"]),
            "peer_title_minimum_tokens": int(self.config["peer_title_minimum_tokens"]),
            "peer_direct_minimum_count": int(self.config["peer_direct_minimum_count"]),
            "candidate_limit": int(self.config["candidate_limit"]),
            "score_weights": dict(self.config["score_weights"]),
            **{
                f"{grade}_{key}": value
                for grade, values in self.config["evidence_grades"].items()
                for key, value in values.items()
            },
        }
        for canonical, ids in occurrences.items():
            n_with = len(ids & with_ids)
            n_without = len(ids & without_ids)
            if not self._candidate_allowed(
                canonical, restrictions, remove, remove_group, already_present
            ):
                continue
            if n_without < int(self.config["minimum_candidate_support"]):
                continue
            grade, rate_with, rate_without, difference, lift = grade_evidence(
                n_with=with_count,
                n_without=without_count,
                with_count=n_with,
                without_count=n_without,
                thresholds=self.config,
                alpha=alpha,
            )
            if difference == 0:
                continue
            max_lift = float(self.config["max_lift_for_score"])
            normalized_lift = min(lift, max_lift) / max_lift
            weights = self.config["score_weights"]
            score = (
                float(weights["frequency_difference"]) * difference
                + float(weights["lift"]) * normalized_lift
            )
            evidence = CandidateEvidence(
                canonical=canonical,
                with_count=n_with,
                without_count=n_without,
                with_rate=rate_with,
                without_rate=rate_without,
                frequency_difference=difference,
                lift=lift,
                evidence_score=score,
                evidence_grade=grade,
                with_recipe_ids=tuple(sorted(ids & with_ids)),
                support_recipe_ids=tuple(sorted(ids & without_ids)),
            )
            if difference < 0:
                if grade == "conflicting":
                    conflicts.append(evidence)
                continue
            violations = self._final_restriction_violations(
                lines, removed, canonical, restrictions, remove, remove_group
            )
            if violations:
                rejected.update(violations)
                continue
            if grade in {"strong", "weak"}:
                candidates.append(evidence)

        candidates.sort(
            key=lambda item: (
                -item.evidence_score,
                -item.frequency_difference,
                -item.lift,
                -item.without_count,
                item.canonical,
            )
        )
        conflicts.sort(key=lambda item: (item.frequency_difference, item.canonical))
        candidates = candidates[: int(self.config["candidate_limit"])]
        if not removed:
            candidates.clear()
            conflicts.clear()
        direct_min = int(self.config["peer_direct_minimum_count"])
        direct_peers = sum(
            peer.title_overlap >= int(self.config["peer_title_minimum_tokens"])
            for peer in peers.peers
        )
        indirect = peers.n_peers > 0 and direct_peers < direct_min
        if candidates:
            grade = (
                "strong" if any(item.evidence_grade == "strong" for item in candidates) else "weak"
            )
        elif conflicts:
            grade = "conflicting"
        else:
            grade = "none"

        notes = [f"Peer retrieval used {peers.retrieval_mode}."]
        if remove_group:
            uncertain_lines = [
                line.raw
                for line in removed
                if self.taxonomy.classify(line.canonical, remove_group).status == "uncertain"
            ]
            if uncertain_lines:
                notes.append(
                    "Ambiguous lines were treated as removable for this draft: "
                    + "; ".join(uncertain_lines)
                )
        if indirect:
            notes.append("Peers have limited title overlap; evidence is indirect.")
        if not removed:
            notes.append(f"No ingredient line matching {remove!r} was found in the target recipe.")
            grade = "none"
        if not candidates:
            notes.append(str(self.config["no_candidate_note"]))
        if rejected:
            notes.append(
                "Candidates that left a hard restriction in the final recipe were rejected."
            )
        return SubstitutionReport(
            target_recipe_id=recipe_id,
            target_title=target.title or "",
            remove=remove,
            remove_group=remove_group,
            removed_lines=tuple(line.raw for line in removed),
            n_peers=peers.n_peers,
            with_x_count=with_count,
            without_x_count=without_count,
            retrieval_mode=peers.retrieval_mode,
            indirect=indirect,
            direct_peer_count=direct_peers,
            peer_recipe_ids=tuple(peer.recipe_id for peer in peers.peers),
            candidates=tuple(candidates),
            conflicting_signals=tuple(conflicts[: int(self.config["candidate_limit"])]),
            evidence_grade=grade,
            thresholds=thresholds,
            restrictions={
                "exclude_ingredients": list(restrictions.exclude_ingredients),
                "excluded_groups": list(restrictions.excluded_groups),
            },
            rejected_for_final_restrictions=tuple(sorted(rejected)),
            formula=(
                "smoothed_rate=(count+alpha)/(peer_group_size+2*alpha); "
                "frequency_difference=without_rate-with_rate; "
                "lift=without_rate/with_rate; score=weight_difference*difference "
                "+ weight_lift*min(lift,max_lift)/max_lift"
            ),
            notes=tuple(notes),
        )

    def _replacement_patterns(self, report: SubstitutionReport) -> tuple[re.Pattern, ...]:
        if report.remove_group:
            return tuple(self.taxonomy.groups[report.remove_group]["match_patterns"])
        patterns = self._remove_patterns.get(report.remove.casefold())
        if patterns:
            return patterns[0]
        return (re.compile(rf"(?<!\w){re.escape(report.remove)}s?(?!\w)", re.IGNORECASE),)

    def build_plan(self, report: SubstitutionReport) -> SubstitutionPlan:
        """Preserve source lines and instructions while annotating a deterministic draft edit."""
        target = self.repository.get_recipe(report.target_recipe_id)
        if target is None:
            raise KeyError(f"Recipe {report.target_recipe_id!r} was not found")
        lines = self.repository.ingredient_lines_for((report.target_recipe_id,))[
            report.target_recipe_id
        ]
        original_ingredients = tuple(line.raw for line in lines)
        try:
            source_ingredients = json.loads(target.ingredients_raw or "[]")
        except json.JSONDecodeError:
            source_ingredients = list(original_ingredients)
        replacement_candidate = report.candidates[0] if report.candidates else None
        replacement = replacement_candidate.canonical if replacement_candidate else None
        remove_group = report.remove_group
        removed_set = set(report.removed_lines)
        updated: list[str] = []
        changes: list[IngredientChange] = []
        for original in source_ingredients:
            if original in removed_set:
                changes.append(
                    IngredientChange(
                        original,
                        replacement,
                        replacement_candidate.evidence_grade if replacement_candidate else "none",
                    )
                )
                if replacement:
                    updated.append(
                        f"SUGGESTED (quantity not inferred): {replacement} — replaces original line: {original}"
                    )
                else:
                    updated.append(f"UNRESOLVED removal: {original}")
            else:
                updated.append(original)

        original_instructions = target.instructions_raw or ""
        revised = original_instructions
        for pattern in self._replacement_patterns(report):
            label = replacement or f"[removed {report.remove}; no supported replacement]"
            revised = pattern.sub(
                lambda match, source=revised, replacement_text=label: self._replacement_for_mention(
                    match, source, report, replacement_text
                ),
                revised,
            )
        note = str(self.config["instruction_note"])
        if not replacement:
            note = str(self.config["no_candidate_note"])
        revised = f"{revised.rstrip()}\n\nADAPTATION NOTE (not verified): {note}".strip()

        removed_key = (remove_group or report.remove).casefold()
        effect_map = self.roles.get("removed_ingredient_effects", {})
        predicted = [effect_map.get(removed_key, effect_map.get("default", ""))]
        candidate_effects = self.roles.get("candidate_effects", {})
        if replacement:
            predicted.append(
                candidate_effects.get(replacement.casefold(), candidate_effects.get("default", ""))
            )
        predicted = [item for item in predicted if item]
        uncertainty = list(report.notes)
        if report.indirect:
            uncertainty.append(
                "Do not treat this as a same-recipe adaptation; peer similarity is indirect."
            )
        if not report.candidates:
            uncertainty.append(str(self.config["no_candidate_note"]))
        if replacement:
            uncertainty.append("Replacement quantities and cooking behavior were not validated.")
        if not target.has_instructions:
            uncertainty.append("The source recipe has no usable instructions to revise.")
        return SubstitutionPlan(
            report=report,
            original_ingredients=original_ingredients,
            updated_ingredients=tuple(updated),
            changes=tuple(changes),
            original_instructions=original_instructions,
            revised_instructions=revised,
            predicted_effects=tuple(predicted),
            uncertainty=tuple(dict.fromkeys(uncertainty)),
            disclaimer=str(self.roles["disclaimer"]),
        )

    def substitute(
        self,
        recipe_id: str,
        remove: str,
        restrictions: Constraints | None = None,
    ) -> SubstitutionPlan:
        report = self.mine_substitutes(recipe_id, remove, restrictions)
        return self.build_plan(report)

    def _replacement_for_mention(
        self,
        match: re.Match[str],
        text: str,
        report: SubstitutionReport,
        replacement: str,
    ) -> str:
        """Do not edit an instruction mention ruled out by a configured product exclusion."""
        if report.remove_group:
            left = max(0, match.start() - 50)
            right = min(len(text), match.end() + 50)
            context = text[left:right]
            if any(
                pattern.search(context)
                for pattern in self.taxonomy.groups[report.remove_group]["exclude_patterns"]
            ):
                return match.group(0)
        return replacement
