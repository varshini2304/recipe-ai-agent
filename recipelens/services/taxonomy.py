"""Config-driven ingredient group matching with exclusions and explicit uncertainty."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

from recipelens.store.repository import RecipeRepository

ROOT = Path(__file__).resolve().parents[2]
TAXONOMY_PATH = ROOT / "config" / "taxonomy.yaml"


@dataclass(frozen=True, slots=True)
class Classification:
    status: str
    pattern: str | None = None


@dataclass(frozen=True, slots=True)
class TriggeringLine:
    raw: str
    canonical: str
    status: str
    pattern: str


@dataclass(frozen=True, slots=True)
class ExclusionExplanation:
    recipe_id: str
    group: str
    lines: tuple[TriggeringLine, ...]

    @property
    def is_uncertain(self) -> bool:
        return any(line.status == "uncertain" for line in self.lines)


class IngredientTaxonomy:
    """Match canonical ingredient text and preserve ambiguous cases as uncertain."""

    def __init__(
        self,
        config_path: Path = TAXONOMY_PATH,
        repository: RecipeRepository | None = None,
    ) -> None:
        self.repository = repository or RecipeRepository()
        document = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        self.groups: dict[str, dict[str, tuple[re.Pattern[str], ...]]] = {}
        self._canonical_group_cache: dict[tuple[str, bool], tuple[str, ...]] = {}
        for group, definitions in document.get("groups", {}).items():
            self.groups[group] = {
                key: tuple(
                    re.compile(pattern, re.IGNORECASE) for pattern in definitions.get(key, [])
                )
                for key in ("match_patterns", "exclude_patterns", "uncertain_patterns")
            }

    def group_names(self) -> tuple[str, ...]:
        return tuple(self.groups)

    def classify(self, canonical: str, group: str) -> Classification:
        if group not in self.groups:
            raise KeyError(
                f"Unknown taxonomy group {group!r}; configured groups: {', '.join(self.groups)}"
            )
        rules = self.groups[group]
        for pattern in rules["exclude_patterns"]:
            if pattern.search(canonical):
                return Classification("excluded", pattern.pattern)
        for pattern in rules["uncertain_patterns"]:
            if pattern.search(canonical):
                return Classification("uncertain", pattern.pattern)
        for pattern in rules["match_patterns"]:
            if pattern.search(canonical):
                return Classification("match", pattern.pattern)
        return Classification("none")

    def canonical_ids_for_group(
        self,
        group: str,
        repository: RecipeRepository | None = None,
        *,
        include_uncertain: bool = True,
    ) -> tuple[str, ...]:
        repository = repository or self.repository
        cache_key = (group, include_uncertain)
        if repository is self.repository and cache_key in self._canonical_group_cache:
            return self._canonical_group_cache[cache_key]
        statuses = {"match", "uncertain"} if include_uncertain else {"match"}
        result = tuple(
            canonical
            for canonical, _count in repository.canonical_counts(limit=None)
            if self.classify(canonical, group).status in statuses
        )
        if repository is self.repository:
            self._canonical_group_cache[cache_key] = result
        return result

    def explain_exclusion(
        self,
        recipe_id: str,
        group: str,
        repository: RecipeRepository | None = None,
    ) -> ExclusionExplanation:
        repository = repository or self.repository
        triggered = []
        for raw, canonical in repository.ingredient_line_records_for(recipe_id):
            result = self.classify(canonical, group)
            if result.status in {"match", "uncertain"} and result.pattern is not None:
                triggered.append(TriggeringLine(raw, canonical, result.status, result.pattern))
        return ExclusionExplanation(recipe_id, group, tuple(triggered))
