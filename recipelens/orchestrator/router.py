"""Service router: dispatches QueryPlan and SessionState to appropriate backend services."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from recipelens.orchestrator.schemas import QueryPlan
from recipelens.orchestrator.state import SessionState
from recipelens.services.analytics import AnalysisReport, AnalyticsService
from recipelens.services.matcher import Constraints, Matcher, MatchReport
from recipelens.services.search import HybridSearch
from recipelens.services.substitution import SubstitutionPlan, SubstitutionService
from recipelens.store.models import Filter
from recipelens.store.repository import RecipeRepository


@dataclass(frozen=True, slots=True)
class ToolResult:
    """Standardized output container produced by service execution."""

    kind: str  # search | analytics | match | recipe_detail | clarification | unsupported | chitchat | reset | error
    data: Any = None
    report: AnalysisReport | MatchReport | SubstitutionPlan | None = None
    warnings: tuple[str, ...] = ()
    clarification_question: str | None = None
    unsupported_reason: str | None = None


class Router:
    """Dispatches plans and states to services with strict constraint preservation."""

    def __init__(
        self,
        repository: RecipeRepository,
        search_service: HybridSearch,
        analytics_service: AnalyticsService,
        matcher_service: Matcher,
        substitution_service: SubstitutionService | None = None,
    ) -> None:
        self.repository = repository
        self.search_service = search_service
        self.analytics_service = analytics_service
        self.matcher_service = matcher_service
        self.substitution_service = substitution_service or SubstitutionService(
            repository,
            matcher_service.taxonomy,
            search_service if isinstance(search_service, HybridSearch) else None,
        )

    def _resolve_substitution_target(
        self, reference: str | None, state: SessionState
    ) -> tuple[str | None, str | None]:
        """Resolve an ID, previous-result ordinal, or unique title phrase."""
        if not reference:
            if state.focused_recipe_id:
                return state.focused_recipe_id, None
            return None, "Which recipe should I adapt? Include its exact title or recipe ID."
        ref = reference.strip()
        if ref.isdigit():
            rank = int(ref) - 1
            if 0 <= rank < len(state.last_result_ids):
                return state.last_result_ids[rank], None
            return (
                None,
                "There is no recipe at that position in the previous results. Give a recipe title or ID.",
            )
        if ":" in ref:
            recipe = self.repository.get_recipe(ref)
            return (ref, None) if recipe else (None, f"I could not find recipe ID {ref!r}.")
        matches = self.repository.find_recipes_by_title(ref)
        exact = [row for row in matches if (row.title or "").strip().casefold() == ref.casefold()]
        if len(exact) == 1:
            return exact[0].recipe_id, None
        if len(matches) == 1:
            return matches[0].recipe_id, None
        if matches:
            return (
                None,
                "That title matches multiple recipes. Please include the exact title or stable recipe ID.",
            )
        return (
            None,
            f"I could not find a recipe matching {ref!r}. Please provide its exact title or ID.",
        )

    def _build_filter(self, state: SessionState, include: tuple[str, ...] = ()) -> Filter:
        """Construct a store Filter preserving all active constraints from state."""
        return Filter(
            include_ingredients=include or state.include_ingredients,
            exclude_ingredients=state.exclude_ingredients,
            excluded_taxonomy_groups=state.excluded_groups,
            max_steps=state.max_steps,
            step_metric=state.step_metric,  # type: ignore[arg-type]
            match_mode="family",
            exclude_low_confidence=state.max_steps is not None,
        )

    def route(self, plan: QueryPlan, state: SessionState) -> ToolResult:
        """Dispatch query plan given current merged session state."""
        # 1. Reset
        if plan.intent == "reset":
            return ToolResult(kind="reset", data=None)

        # 2. Unsupported
        if plan.intent == "unsupported":
            return ToolResult(
                kind="unsupported",
                data=None,
                unsupported_reason=plan.unsupported_reason,
            )

        # 3. Clarification
        if plan.clarification_question:
            return ToolResult(
                kind="clarification",
                data=None,
                clarification_question=plan.clarification_question,
            )

        # 4. Chitchat
        if plan.intent == "chitchat":
            return ToolResult(kind="chitchat", data=None)

        if plan.intent == "substitute":
            if not plan.remove_term:
                return ToolResult(
                    kind="clarification",
                    clarification_question="Which ingredient or configured group should be removed?",
                )
            recipe_id, question = self._resolve_substitution_target(plan.recipe_ref, state)
            if question or recipe_id is None:
                return ToolResult(kind="clarification", clarification_question=question)
            excluded_groups = tuple(
                dict.fromkeys((*state.matcher_constraints.excluded_groups, *plan.excluded_groups))
            )
            excluded_terms = tuple(
                dict.fromkeys(
                    (*state.matcher_constraints.exclude_ingredients, *plan.exclude_ingredients)
                )
            )
            hard_filter = Constraints(
                exclude_ingredients=excluded_terms,
                excluded_groups=excluded_groups,
                max_steps=state.matcher_constraints.max_steps,
                step_metric=state.matcher_constraints.step_metric,
                exclude_low_confidence=state.matcher_constraints.exclude_low_confidence,
            )
            plan_result = self.substitution_service.substitute(
                recipe_id, plan.remove_term, hard_filter
            )
            return ToolResult(kind="substitution", data=plan_result, report=plan_result)

        # 5. Recipe Detail
        if plan.intent == "recipe_detail":
            target_id = state.focused_recipe_id
            if not target_id and plan.recipe_ref:
                ref = plan.recipe_ref.strip()
                if ref.isdigit():
                    idx = int(ref) - 1
                    if 0 <= idx < len(state.last_result_ids):
                        target_id = state.last_result_ids[idx]
                elif ref in state.last_result_ids or ":" in ref:
                    target_id = ref

            if not target_id:
                return ToolResult(
                    kind="clarification",
                    clarification_question="Which recipe would you like to view? Please specify a number or recipe ID.",
                )

            recipe = self.repository.get_recipe(target_id)
            if not recipe:
                return ToolResult(
                    kind="error",
                    warnings=(f"Recipe '{target_id}' was not found in the database.",),
                )
            return ToolResult(kind="recipe_detail", data=recipe)

        # 6. Analytics
        if plan.intent == "analytics":
            base_filter = self._build_filter(state, include=plan.include_ingredients)
            atype = plan.analytics_type

            if atype == "count_with":
                if not plan.include_ingredients:
                    return ToolResult(
                        kind="clarification",
                        clarification_question="Which ingredients would you like to count? (e.g. 'How many recipes have garlic AND onion?')",
                    )
                report = self.analytics_service.count_with(
                    include=plan.include_ingredients,
                    mode=plan.analytics_mode or "all",
                    recipe_filter=base_filter,
                )
                return ToolResult(kind="analytics", data=report.rows, report=report)

            if atype == "common_ingredients":
                report = self.analytics_service.common_ingredients(
                    recipe_filter=base_filter,
                    top_k=plan.top_k or 20,
                )
                return ToolResult(kind="analytics", data=report.rows, report=report)

            if atype == "ingredient_count_stats":
                report = self.analytics_service.ingredient_count_stats(recipe_filter=base_filter)
                return ToolResult(kind="analytics", data=report.rows, report=report)

            if atype == "rank_by_steps":
                report = self.analytics_service.rank_by_steps(
                    recipe_filter=base_filter,
                    order=plan.order or "asc",
                    top_k=plan.top_k or 10,
                    metric=state.step_metric,
                )
                return ToolResult(kind="analytics", data=report.rows, report=report)

            return ToolResult(
                kind="error",
                warnings=(f"Unsupported analytics operation '{atype}'.",),
            )

        # 7. Pantry Match
        if plan.intent == "match" or (plan.intent == "refine" and state.active_mode == "match"):
            if not state.pantry:
                return ToolResult(
                    kind="clarification",
                    clarification_question="What ingredients do you have in your pantry? (e.g. 'I have eggs, onions, tomatoes, rice')",
                )
            report = self.matcher_service.match(
                pantry=state.pantry,
                constraints=state.matcher_constraints,
                preferences=state.matcher_preferences,
                top_k=plan.top_k or 5,
            )
            return ToolResult(
                kind="match",
                data=report.results,
                report=report,
                warnings=tuple(report.notes),
            )

        # 8. Search (or refine on active search)
        query = state.query_text
        if not query:
            return ToolResult(
                kind="clarification",
                clarification_question="What would you like to search for? (e.g. 'penne pasta' or 'chocolate cake')",
            )
        recipe_filter = self._build_filter(state)
        results = self.search_service.search(
            query=query,
            recipe_filter=recipe_filter,
            top_k=plan.top_k or 10,
        )
        return ToolResult(kind="search", data=results)
