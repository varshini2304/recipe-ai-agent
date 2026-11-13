"""Schemas for conversation planning and orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from recipelens.services.matcher import PantryItem

IntentType = Literal[
    "search",
    "refine",
    "analytics",
    "match",
    "recipe_detail",
    "substitute",
    "unsupported",
    "chitchat",
    "reset",
]

ALLOWED_INTENTS: frozenset[str] = frozenset(
    {
        "search",
        "refine",
        "analytics",
        "match",
        "recipe_detail",
        "substitute",
        "unsupported",
        "chitchat",
        "reset",
    }
)

ALLOWED_ANALYTICS_TYPES: frozenset[str] = frozenset(
    {
        "count_with",
        "common_ingredients",
        "ingredient_count_stats",
        "rank_by_steps",
    }
)


@dataclass(frozen=True, slots=True)
class QueryPlan:
    """Structured plan emitted by the intent parser."""

    intent: IntentType
    query_text: str = ""
    include_ingredients: tuple[str, ...] = ()
    exclude_ingredients: tuple[str, ...] = ()
    excluded_groups: tuple[str, ...] = ()
    max_steps: int | None = None
    pantry: tuple[PantryItem, ...] = ()
    analytics_type: str | None = (
        None  # count_with | common_ingredients | ingredient_count_stats | rank_by_steps
    )
    recipe_ref: str | None = None  # e.g. "the second one", "2", or recipe ID like "fn:..."
    top_k: int = 10
    order: str = "asc"
    step_metric: str = "step_count"
    analytics_mode: str = "all"  # "all" or "any" for count_with
    remove_term: str | None = None
    remove_group: str | None = None
    prefer_fewer_missing: bool = False
    prefer_fewer_steps: bool = False
    unsupported_reason: str | None = None
    clarification_question: str | None = None
    raw_message: str = ""

    def __post_init__(self) -> None:
        if self.intent not in ALLOWED_INTENTS:
            raise ValueError(
                f"Unknown intent {self.intent!r}; must be one of {sorted(ALLOWED_INTENTS)}"
            )
        if self.analytics_type is not None and self.analytics_type not in ALLOWED_ANALYTICS_TYPES:
            raise ValueError(
                f"Unknown analytics_type {self.analytics_type!r}; must be one of {sorted(ALLOWED_ANALYTICS_TYPES)}"
            )
        # Normalize collections to tuples if caller passed lists
        if not isinstance(self.include_ingredients, tuple):
            object.__setattr__(self, "include_ingredients", tuple(self.include_ingredients))
        if not isinstance(self.exclude_ingredients, tuple):
            object.__setattr__(self, "exclude_ingredients", tuple(self.exclude_ingredients))
        if not isinstance(self.excluded_groups, tuple):
            object.__setattr__(self, "excluded_groups", tuple(self.excluded_groups))
        if not isinstance(self.pantry, tuple):
            object.__setattr__(self, "pantry", tuple(self.pantry))
