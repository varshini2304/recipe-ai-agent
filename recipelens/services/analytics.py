"""Complete-set deterministic recipe analytics with explicit denominator metadata."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from statistics import mean, median

from recipelens.services.ingredient_families import IngredientFamilies
from recipelens.services.taxonomy import IngredientTaxonomy
from recipelens.store.models import DEFAULT_FILTER, Filter
from recipelens.store.repository import RecipeRepository


@dataclass(frozen=True, slots=True)
class AnalysisReport:
    filters: dict
    n_analyzed: int
    denominator: int
    formula: str
    normalization_notes: str
    rows: list[dict]
    denominator_label: str
    secondary_denominator: int | None = None
    secondary_denominator_label: str | None = None
    cutoff_tie_count: int | None = None
    metric: str = "step_count"
    low_confidence_candidates: int = 0
    low_confidence_excluded: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


class AnalyticsService:
    def __init__(
        self, repository: RecipeRepository, taxonomy: IngredientTaxonomy | None = None
    ) -> None:
        self.repository = repository
        self.taxonomy = taxonomy or IngredientTaxonomy(repository=repository)
        self.families = IngredientFamilies(repository)

    def _include_variants(self, recipe_filter: Filter) -> tuple[tuple[str, ...], ...]:
        return self.families.variants_for(
            recipe_filter.include_ingredients, recipe_filter.match_mode
        )

    @staticmethod
    def _matching_note(recipe_filter: Filter, variants: tuple[tuple[str, ...], ...]) -> str:
        detail = {
            term: list(values) for term, values in zip(recipe_filter.include_ingredients, variants)
        }
        encoded = json.dumps(detail, ensure_ascii=False, separators=(",", ":"))
        return (
            f"match_mode={recipe_filter.match_mode}; modes=[exact, family] (default=family); "
            f"matched canonical variants: {encoded}"
        )

    def _excluded(self, recipe_filter: Filter) -> tuple[str, ...]:
        blocked: set[str] = set()
        for group in recipe_filter.excluded_taxonomy_groups:
            blocked.update(self.taxonomy.canonical_ids_for_group(group))
        return tuple(sorted(blocked))

    def count_with(
        self,
        include: list[str] | tuple[str, ...],
        mode: str = "all",
        recipe_filter: Filter = DEFAULT_FILTER,
    ) -> AnalysisReport:
        if mode not in {"all", "any"}:
            raise ValueError("mode must be 'all' or 'any'")
        terms = tuple(dict.fromkeys(term.casefold().strip() for term in include if term.strip()))
        if not terms:
            raise ValueError("include must contain at least one canonical ingredient")
        applied = Filter(
            include_ingredients=terms,
            exclude_ingredients=recipe_filter.exclude_ingredients,
            include_mode=mode,
            excluded_taxonomy_groups=recipe_filter.excluded_taxonomy_groups,
            match_mode=recipe_filter.match_mode,
            min_steps=recipe_filter.min_steps,
            max_steps=recipe_filter.max_steps,
            step_metric=recipe_filter.step_metric,
            exclude_low_confidence=recipe_filter.exclude_low_confidence,
            exclude_title_duplicates=recipe_filter.exclude_title_duplicates,
        )
        variants = self.families.variants_for(terms, recipe_filter.match_mode)
        matching = self.repository.filter_ids(
            applied,
            excluded_canonical=self._excluded(recipe_filter),
            include_variants=variants,
            require_ingredients=True,
        )
        counts = self.repository.counts()
        denominator = counts["usable_ingredients"]
        base_filter = Filter(
            exclude_ingredients=recipe_filter.exclude_ingredients,
            excluded_taxonomy_groups=recipe_filter.excluded_taxonomy_groups,
            min_steps=recipe_filter.min_steps,
            max_steps=recipe_filter.max_steps,
            exclude_title_duplicates=recipe_filter.exclude_title_duplicates,
            step_metric=recipe_filter.step_metric,
            exclude_low_confidence=recipe_filter.exclude_low_confidence,
        )
        n_analyzed = len(
            self.repository.filter_ids(
                base_filter,
                excluded_canonical=self._excluded(recipe_filter),
                require_ingredients=True,
            )
        )
        count = len(matching)
        low_confidence_candidates = self.repository.count_low_confidence(
            applied,
            excluded_canonical=self._excluded(recipe_filter),
            include_variants=variants,
            require_ingredients=True,
        )
        percent = 100.0 * count / denominator if denominator else 0.0
        all_percent = 100.0 * count / counts["all_recipes"] if counts["all_recipes"] else 0.0
        return AnalysisReport(
            filters={"include": list(terms), "mode": mode, **asdict(recipe_filter)},
            n_analyzed=n_analyzed,
            denominator=denominator,
            formula=f"count / usable-ingredient recipes * 100 = {count} / {denominator} * 100",
            normalization_notes=self._matching_note(applied, variants)
            + f"; metric={recipe_filter.step_metric}; cutoff ties=n/a; "
            + f"low-confidence candidates={low_confidence_candidates}; "
            + f"low-confidence excluded={recipe_filter.exclude_low_confidence}; canonical values come from ingredient_lines.",
            rows=[{"count": count, "percentage": percent, "percentage_all_recipes": all_percent}],
            denominator_label=f"usable-ingredient recipes = {denominator:,}",
            secondary_denominator=counts["all_recipes"],
            secondary_denominator_label=f"all recipes = {counts['all_recipes']:,}",
            metric=recipe_filter.step_metric,
            low_confidence_candidates=low_confidence_candidates,
            low_confidence_excluded=(
                low_confidence_candidates if recipe_filter.exclude_low_confidence else 0
            ),
        )

    def common_ingredients(
        self, recipe_filter: Filter = DEFAULT_FILTER, top_k: int = 20
    ) -> AnalysisReport:
        if top_k <= 0:
            raise ValueError("top_k must be positive")
        recipe_ids = self.repository.filter_ids(
            recipe_filter,
            excluded_canonical=self._excluded(recipe_filter),
            require_ingredients=True,
            include_variants=self._include_variants(recipe_filter),
        )
        lines = self.repository.ingredient_lines_for(recipe_ids)
        counts: dict[str, int] = {}
        for values in lines.values():
            for canonical in {line.canonical for line in values}:
                counts[canonical] = counts.get(canonical, 0) + 1
        ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:top_k]
        denominator = len(recipe_ids)
        base = self.repository.counts()["usable_ingredients"]
        low_confidence_candidates = self.repository.count_low_confidence(
            recipe_filter,
            excluded_canonical=self._excluded(recipe_filter),
            include_variants=self._include_variants(recipe_filter),
            require_ingredients=True,
        )
        return AnalysisReport(
            filters=asdict(recipe_filter),
            n_analyzed=denominator,
            denominator=denominator,
            formula="recipe frequency = distinct filtered recipes containing canonical ingredient; percentage = frequency / filtered usable-ingredient recipes * 100",
            normalization_notes=self._matching_note(
                recipe_filter, self._include_variants(recipe_filter)
            )
            + f"; metric={recipe_filter.step_metric}; cutoff ties=n/a; low-confidence candidates={low_confidence_candidates}; "
            + f"low-confidence excluded={recipe_filter.exclude_low_confidence}; canonical ingredient frequencies count each ingredient once per recipe.",
            rows=[
                {
                    "canonical": ingredient,
                    "count": count,
                    "percentage": 100.0 * count / denominator if denominator else 0.0,
                }
                for ingredient, count in ranked
            ],
            denominator_label=f"usable-ingredient recipes after filters = {denominator:,}; primary base = {base:,}",
            secondary_denominator=self.repository.counts()["all_recipes"],
            secondary_denominator_label=f"all recipes = {self.repository.counts()['all_recipes']:,}",
            metric=recipe_filter.step_metric,
            low_confidence_candidates=low_confidence_candidates,
            low_confidence_excluded=(
                low_confidence_candidates if recipe_filter.exclude_low_confidence else 0
            ),
        )

    def ingredient_count_stats(self, recipe_filter: Filter = DEFAULT_FILTER) -> AnalysisReport:
        recipes = self.repository.recipes_for_filter(
            recipe_filter,
            excluded_canonical=self._excluded(recipe_filter),
            require_ingredients=True,
            include_variants=self._include_variants(recipe_filter),
        )
        values = [recipe.ingredient_count for recipe in recipes]
        denominator = len(values)
        base = self.repository.counts()["usable_ingredients"]
        low_confidence_candidates = self.repository.count_low_confidence(
            recipe_filter,
            excluded_canonical=self._excluded(recipe_filter),
            include_variants=self._include_variants(recipe_filter),
            require_ingredients=True,
        )
        row = {
            "mean": mean(values) if values else None,
            "median": median(values) if values else None,
            "min": min(values) if values else None,
            "max": max(values) if values else None,
        }
        return AnalysisReport(
            filters=asdict(recipe_filter),
            n_analyzed=denominator,
            denominator=denominator,
            formula="mean and median of ingredient_count; min and max over every filtered recipe with usable ingredients",
            normalization_notes=self._matching_note(
                recipe_filter, self._include_variants(recipe_filter)
            )
            + f"; metric={recipe_filter.step_metric}; cutoff ties=n/a; low-confidence candidates={low_confidence_candidates}; "
            + f"low-confidence excluded={recipe_filter.exclude_low_confidence}; ingredient_count is retained nonblank ingredient lines.",
            rows=[row],
            denominator_label=f"usable-ingredient recipes after filters = {denominator:,}; primary base = {base:,}",
            secondary_denominator=self.repository.counts()["all_recipes"],
            secondary_denominator_label=f"all recipes = {self.repository.counts()['all_recipes']:,}",
            metric=recipe_filter.step_metric,
            low_confidence_candidates=low_confidence_candidates,
            low_confidence_excluded=(
                low_confidence_candidates if recipe_filter.exclude_low_confidence else 0
            ),
        )

    def rank_by_steps(
        self,
        recipe_filter: Filter = DEFAULT_FILTER,
        order: str = "asc",
        top_k: int = 20,
        metric: str | None = None,
        exclude_low_confidence: bool = True,
    ) -> AnalysisReport:
        if order not in {"asc", "desc"}:
            raise ValueError("order must be 'asc' or 'desc'")
        if top_k <= 0:
            raise ValueError("top_k must be positive")
        metric = metric or recipe_filter.step_metric
        if metric not in {"step_count", "sentence_count"}:
            raise ValueError("metric must be 'step_count' or 'sentence_count'")
        from dataclasses import replace

        candidate_filter = replace(recipe_filter, step_metric=metric, exclude_low_confidence=False)
        candidate_low_confidence = self.repository.count_low_confidence(
            candidate_filter,
            excluded_canonical=self._excluded(candidate_filter),
            include_variants=self._include_variants(candidate_filter),
            require_instructions=True,
        )
        rank_filter = replace(
            candidate_filter, step_metric=metric, exclude_low_confidence=exclude_low_confidence
        )
        recipes = self.repository.recipes_for_filter(
            rank_filter,
            excluded_canonical=self._excluded(rank_filter),
            require_instructions=True,
            include_variants=self._include_variants(rank_filter),
        )
        # Order applies only to steps; ties always use ingredient count and stable ID ascending.
        recipes.sort(
            key=lambda recipe: (
                getattr(recipe, metric) if order == "asc" else -getattr(recipe, metric),
                recipe.ingredient_count,
                recipe.recipe_id,
            )
        )
        rows = [
            {
                "recipe_id": recipe.recipe_id,
                "title": recipe.title,
                "step_count": recipe.step_count,
                "sentence_count": recipe.sentence_count,
                "metric_value": getattr(recipe, metric),
                "ingredient_count": recipe.ingredient_count,
                "instructions_low_confidence": recipe.instructions_low_confidence,
            }
            for recipe in recipes[:top_k]
        ]
        all_recipes = self.repository.counts()["all_recipes"]
        cutoff_value = rows[-1]["metric_value"] if rows else None
        cutoff_tie_count = (
            sum(getattr(recipe, metric) == cutoff_value for recipe in recipes) if rows else 0
        )
        return AnalysisReport(
            filters={**asdict(rank_filter), "order": order, "top_k": top_k},
            n_analyzed=len(recipes),
            denominator=self.repository.counts()["usable_ingredients"],
            formula=f"sort all eligible recipes by {metric} {order}, then ingredient_count ascending, then recipe_id ascending; return first {top_k}; cutoff tie count counts all included candidates at {metric}={cutoff_value}",
            normalization_notes=self._matching_note(
                rank_filter, self._include_variants(rank_filter)
            )
            + f"; metric={metric}; low-confidence candidates={candidate_low_confidence}; "
            + f"cutoff ties={cutoff_tie_count}; low-confidence excluded count="
            + f"{candidate_low_confidence if exclude_low_confidence else 0}; "
            + "step count follows the configured newline-block rule.",
            rows=rows,
            denominator_label=f"usable-ingredient recipes = {self.repository.counts()['usable_ingredients']:,}; analyzed filtered recipes with usable instructions = {len(recipes):,}",
            secondary_denominator=all_recipes,
            secondary_denominator_label=f"all recipes = {all_recipes:,}",
            cutoff_tie_count=cutoff_tie_count,
            metric=metric,
            low_confidence_candidates=candidate_low_confidence,
            low_confidence_excluded=(candidate_low_confidence if exclude_low_confidence else 0),
        )
