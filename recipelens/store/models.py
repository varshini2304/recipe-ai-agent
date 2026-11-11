"""Typed records shared by the read-only store layer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


@dataclass(frozen=True, slots=True)
class Filter:
    """Hard recipe constraints applied before either retrieval ranker scores rows."""

    include_ingredients: tuple[str, ...] = ()
    exclude_ingredients: tuple[str, ...] = ()
    include_mode: Literal["all", "any"] = "all"
    match_mode: Literal["exact", "family"] = "family"
    excluded_taxonomy_groups: tuple[str, ...] = ()
    min_steps: int | None = None
    max_steps: int | None = None
    step_metric: Literal["step_count", "sentence_count"] = "step_count"
    exclude_low_confidence: bool = False
    exclude_title_duplicates: bool = False


DEFAULT_FILTER = Filter()


@dataclass(frozen=True, slots=True)
class RecipeRecord:
    recipe_id: str
    source: str
    original_key: str
    title: str | None
    ingredients_raw: str | None
    instructions_raw: str | None
    step_count: int
    sentence_count: int
    instructions_low_confidence: bool
    ingredient_count: int
    has_title: bool
    has_ingredients: bool
    has_instructions: bool
    title_dup_group: str | None
    canonical_ingredients: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True, slots=True)
class IngredientLine:
    recipe_id: str
    position: int
    raw: str
    canonical: str
    qty: str | None
    unit: str | None
    name: str
    prep: str | None


@dataclass(frozen=True, slots=True)
class FTSMatch:
    recipe_id: str
    title: str
    bm25: float
    matched_terms: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class VectorMatch:
    recipe_id: str
    cosine: float


@dataclass(frozen=True, slots=True)
class SearchResult:
    recipe_id: str
    title: str
    score: float
    score_breakdown: dict[str, float]
    matched_terms: tuple[str, ...]
    ingredients_raw: str | None
    instructions_raw: str | None
