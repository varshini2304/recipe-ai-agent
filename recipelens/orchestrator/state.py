"""Session state for multi-turn conversation and constraint delta management."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Any

from recipelens.orchestrator.schemas import QueryPlan
from recipelens.services.matcher import Constraints, PantryItem, Preferences


def _merge_tuples(*tuples: tuple[str, ...]) -> tuple[str, ...]:
    """Merge strings preserving order and eliminating duplicates case-insensitively."""
    seen: set[str] = set()
    result: list[str] = []
    for t in tuples:
        for item in t:
            clean = item.strip()
            if not clean:
                continue
            key = clean.casefold()
            if key not in seen:
                seen.add(key)
                result.append(clean)
    return tuple(result)


@dataclass(frozen=True, slots=True)
class SessionState:
    """Immutable session state tracking active search, matcher constraints, and history."""

    query_text: str = ""
    include_ingredients: tuple[str, ...] = ()
    exclude_ingredients: tuple[str, ...] = ()
    excluded_groups: tuple[str, ...] = ()
    max_steps: int | None = None
    step_metric: str = "step_count"
    pantry: tuple[PantryItem, ...] = ()
    matcher_constraints: Constraints = field(default_factory=Constraints)
    matcher_preferences: Preferences = field(default_factory=Preferences)
    last_result_ids: tuple[str, ...] = ()
    last_result_titles: dict[str, str] = field(default_factory=dict)
    focused_recipe_id: str | None = None
    active_mode: str = "search"  # search | match | analytics | recipe_detail
    turn_count: int = 0

    @classmethod
    def reset(cls) -> SessionState:
        """Create a pristine session state."""
        return cls()

    def with_results(
        self,
        result_ids: tuple[str, ...] | list[str],
        titles: dict[str, str] | None = None,
    ) -> SessionState:
        """Update last shown results after search or match execution."""
        return replace(
            self,
            last_result_ids=tuple(result_ids),
            last_result_titles=dict(titles or {}),
        )

    def with_focused_recipe(self, recipe_id: str | None) -> SessionState:
        """Update currently focused recipe ID."""
        return replace(self, focused_recipe_id=recipe_id)

    def merge(self, plan: QueryPlan) -> SessionState:
        """Merge a QueryPlan into state.

        Follow-ups are deltas:
        - "I cannot have dairy" adds dairy to excluded_groups, keeping active query and other filters.
        - "exclude eggs too" updates both active search and matcher Constraints.
        - Hard constraints are NEVER dropped on follow-ups.
        - "start over" / "reset" resets everything.
        """
        if plan.intent == "reset":
            return SessionState.reset()

        # Merge ingredients and taxonomy groups
        new_inc = _merge_tuples(self.include_ingredients, plan.include_ingredients)
        new_exc_ing = _merge_tuples(self.exclude_ingredients, plan.exclude_ingredients)
        new_exc_grp = _merge_tuples(self.excluded_groups, plan.excluded_groups)

        # Max steps: new constraint overrides if provided
        new_max_steps = plan.max_steps if plan.max_steps is not None else self.max_steps
        new_step_metric = plan.step_metric or self.step_metric

        # Update Matcher Constraints
        m_constraints = self.matcher_constraints
        if new_exc_ing:
            m_constraints = m_constraints.with_excluded(*new_exc_ing)
        if new_exc_grp:
            m_constraints = m_constraints.with_excluded_groups(*new_exc_grp)
        if new_max_steps is not None:
            m_constraints = replace(
                m_constraints,
                max_steps=new_max_steps,
                step_metric=new_step_metric,
            )

        # Update Matcher Preferences
        m_preferences = self.matcher_preferences
        if plan.prefer_fewer_missing:
            m_preferences = replace(m_preferences, prefer_fewer_missing=True)
        if plan.prefer_fewer_steps:
            m_preferences = replace(m_preferences, prefer_fewer_steps=True)

        # Query text & Pantry:
        # If new query text is non-empty, use it; otherwise retain existing
        if plan.intent == "search" and plan.query_text:
            new_query = plan.query_text
            new_mode = "search"
        elif plan.intent == "match":
            new_query = self.query_text
            new_mode = "match"
        elif plan.intent == "analytics":
            new_query = plan.query_text if plan.query_text else self.query_text
            new_mode = "analytics"
        elif plan.intent == "refine":
            new_query = self.query_text
            new_mode = self.active_mode or "search"
        else:
            new_query = self.query_text
            new_mode = self.active_mode

        # Pantry: update if plan provided a pantry
        if plan.pantry:
            new_pantry = plan.pantry
        else:
            new_pantry = self.pantry

        # Focused recipe
        new_focused = self.focused_recipe_id
        if plan.intent in {"recipe_detail", "substitute"} and plan.recipe_ref:
            ref = plan.recipe_ref.strip()
            # If reference is an integer rank (1-indexed)
            if ref.isdigit():
                idx = int(ref) - 1
                if 0 <= idx < len(self.last_result_ids):
                    new_focused = self.last_result_ids[idx]
            elif ref in self.last_result_ids or ":" in ref:
                new_focused = ref

        return replace(
            self,
            query_text=new_query,
            include_ingredients=new_inc,
            exclude_ingredients=new_exc_ing,
            excluded_groups=new_exc_grp,
            max_steps=new_max_steps,
            step_metric=new_step_metric,
            pantry=new_pantry,
            matcher_constraints=m_constraints,
            matcher_preferences=m_preferences,
            focused_recipe_id=new_focused,
            active_mode=new_mode,
            turn_count=self.turn_count + 1,
        )

    def constraint_chips(self) -> list[str]:
        """Generate human-readable constraint labels for UI chips or CLI headers."""
        chips: list[str] = []
        if self.query_text:
            chips.append(f"query: {self.query_text}")
        if self.include_ingredients:
            chips.append(f"include: {', '.join(self.include_ingredients)}")
        if self.exclude_ingredients:
            chips.append(f"exclude: {', '.join(self.exclude_ingredients)}")
        if self.excluded_groups:
            chips.append(f"no {', '.join(self.excluded_groups)}")
        if self.max_steps is not None:
            chips.append(f"max {self.max_steps} steps")
        if self.pantry:
            p_names = [p.name for p in self.pantry]
            chips.append(
                f"pantry ({len(p_names)}): {', '.join(p_names[:4])}{'...' if len(p_names) > 4 else ''}"
            )
        return chips

    def to_dict(self) -> dict[str, Any]:
        """Convert state to a JSON-serializable dictionary."""
        return {
            "query_text": self.query_text,
            "include_ingredients": list(self.include_ingredients),
            "exclude_ingredients": list(self.exclude_ingredients),
            "excluded_groups": list(self.excluded_groups),
            "max_steps": self.max_steps,
            "step_metric": self.step_metric,
            "pantry": [{"name": p.name, "qty": p.qty, "unit": p.unit} for p in self.pantry],
            "matcher_constraints": {
                "exclude_ingredients": list(self.matcher_constraints.exclude_ingredients),
                "excluded_groups": list(self.matcher_constraints.excluded_groups),
                "max_steps": self.matcher_constraints.max_steps,
                "step_metric": self.matcher_constraints.step_metric,
            },
            "last_result_ids": list(self.last_result_ids),
            "last_result_titles": dict(self.last_result_titles),
            "focused_recipe_id": self.focused_recipe_id,
            "active_mode": self.active_mode,
            "turn_count": self.turn_count,
            "chips": self.constraint_chips(),
        }
