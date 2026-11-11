"""Resolve reviewed ingredient family names to canonical values from the database."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from recipelens.store.repository import RecipeRepository

ROOT = Path(__file__).resolve().parents[2]
FAMILIES_PATH = ROOT / "config" / "families.yaml"


class IngredientFamilies:
    """Apply only the explicitly reviewed match and product-exclusion patterns."""

    def __init__(self, repository: RecipeRepository, config_path: Path = FAMILIES_PATH) -> None:
        self.repository = repository
        self._cache: dict[str, tuple[str, ...]] = {}
        document = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        self.rules = {
            name.casefold(): (
                tuple(re.compile(p, re.IGNORECASE) for p in value.get("match_patterns", [])),
                tuple(re.compile(p, re.IGNORECASE) for p in value.get("exclude_patterns", [])),
            )
            for name, value in document.get("families", {}).items()
        }

    def variants(self, term: str) -> tuple[str, ...]:
        """Return matching canonical values, falling back to exact for unconfigured terms."""
        normalized = term.casefold().strip()
        if normalized in self._cache:
            return self._cache[normalized]
        if normalized not in self.rules:
            result = (normalized,)
            self._cache[normalized] = result
            return result
        includes, excludes = self.rules[normalized]
        values = []
        for canonical, _count in self.repository.canonical_counts(limit=None):
            if any(pattern.search(canonical) for pattern in excludes):
                continue
            # Preparation after a comma is excluded before evaluating the ingredient head.
            ingredient_head = canonical.split(",", maxsplit=1)[0].strip()
            if any(pattern.search(ingredient_head) for pattern in includes):
                values.append(canonical)
        result = tuple(sorted(values))
        self._cache[normalized] = result
        return result

    def variants_for(self, terms: tuple[str, ...], mode: str) -> tuple[tuple[str, ...], ...]:
        if mode == "exact":
            return tuple((term.casefold().strip(),) for term in terms if term.strip())
        if mode == "family":
            return tuple(self.variants(term) for term in terms if term.strip())
        raise ValueError("match_mode must be 'exact' or 'family'")
