"""Hybrid SQLite FTS5 and vector retrieval with pre-ranking hard constraints."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from recipelens.services.ingredient_families import IngredientFamilies
from recipelens.services.taxonomy import IngredientTaxonomy
from recipelens.store.models import DEFAULT_FILTER, Filter, SearchResult
from recipelens.store.repository import RecipeRepository
from recipelens.store.vector_index import VectorIndex, load_vector_index

ROOT = Path(__file__).resolve().parents[2]
_TOKEN = re.compile(r"[\w'-]+", re.UNICODE)


class HybridSearch:
    def __init__(
        self,
        repository: RecipeRepository,
        vector_index: VectorIndex,
        taxonomy: IngredientTaxonomy,
        *,
        config_path: Path = ROOT / "config" / "store.yaml",
    ) -> None:
        self.repository = repository
        self.vector_index = vector_index
        self.taxonomy = taxonomy
        self.families = IngredientFamilies(repository)
        self.config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}

    @property
    def index_coverage(self) -> tuple[int, int]:
        """Return built vector rows and full searchable corpus size for honest dev reporting."""
        return self.vector_index.indexed_rows, self.vector_index.searchable_rows_full

    def search(
        self, query: str, recipe_filter: Filter = DEFAULT_FILTER, top_k: int | None = None
    ) -> list[SearchResult]:
        limit = top_k or int(self.config.get("search_limit", 20))
        if not query.strip() or limit <= 0:
            return []
        excluded_canonical: set[str] = set()
        for group in recipe_filter.excluded_taxonomy_groups:
            excluded_canonical.update(self.taxonomy.canonical_ids_for_group(group, self.repository))
        allowed = self.repository.filter_ids(
            recipe_filter,
            excluded_canonical=tuple(sorted(excluded_canonical)),
            search_eligible=True,
            id_subset=self.vector_index.ids,
            include_variants=self.families.variants_for(
                recipe_filter.include_ingredients,
                recipe_filter.match_mode,
            ),
        )
        if not allowed:
            return []
        query_vector = self.vector_index.encode_query(query)
        candidate_limit = max(
            limit * int(self.config["candidate_multiplier"]),
            int(self.config["candidate_floor"]),
        )
        vector_matches = self.vector_index.search(query_vector, allowed, candidate_limit)
        fts_matches = self.repository.fts_search(
            query,
            recipe_filter,
            candidate_limit,
            title_weight=float(self.config["fts_title_weight"]),
            ingredient_weight=float(self.config["fts_ingredients_weight"]),
            excluded_canonical=tuple(sorted(excluded_canonical)),
            include_variants=self.families.variants_for(
                recipe_filter.include_ingredients,
                recipe_filter.match_mode,
            ),
        )
        rrf_k = int(self.config["rrf_k"])
        ranks: dict[str, dict[str, float]] = {}
        matched_terms: dict[str, set[str]] = {}
        for rank, match in enumerate(fts_matches, 1):
            ranks.setdefault(match.recipe_id, {})["bm25"] = match.bm25
            matched_terms.setdefault(match.recipe_id, set()).update(match.matched_terms)
            ranks[match.recipe_id]["rrf"] = ranks[match.recipe_id].get("rrf", 0.0) + 1.0 / (
                rrf_k + rank
            )
        for rank, match in enumerate(vector_matches, 1):
            ranks.setdefault(match.recipe_id, {})["vector"] = match.cosine
            ranks[match.recipe_id]["rrf"] = ranks[match.recipe_id].get("rrf", 0.0) + 1.0 / (
                rrf_k + rank
            )
        titles: dict[str, str] = {match.recipe_id: match.title for match in fts_matches}
        results = []
        for recipe_id, breakdown in ranks.items():
            results.append(
                SearchResult(
                    recipe_id=recipe_id,
                    title=titles.get(recipe_id, ""),
                    score=breakdown["rrf"],
                    score_breakdown={
                        "bm25": breakdown.get("bm25", 0.0),
                        "vector": breakdown.get("vector", 0.0),
                        "rrf": breakdown["rrf"],
                    },
                    matched_terms=tuple(sorted(matched_terms.get(recipe_id, set()))),
                    ingredients_raw=None,
                    instructions_raw=None,
                )
            )
        results.sort(key=lambda result: (-result.score, result.recipe_id))
        complete = []
        records = self.repository.recipes_for_ids(result.recipe_id for result in results[:limit])
        for result in results[:limit]:
            recipe = records.get(result.recipe_id)
            if recipe is None or recipe.title is None:
                continue
            complete.append(
                SearchResult(
                    recipe_id=result.recipe_id,
                    title=recipe.title or result.title,
                    score=result.score,
                    score_breakdown=result.score_breakdown,
                    matched_terms=result.matched_terms,
                    ingredients_raw=recipe.ingredients_raw,
                    instructions_raw=recipe.instructions_raw,
                )
            )
        return complete


def build_search(repository: RecipeRepository | None = None) -> HybridSearch:
    from recipelens.services.taxonomy import IngredientTaxonomy

    repository = repository or RecipeRepository()
    return HybridSearch(repository, load_vector_index(), IngredientTaxonomy(repository=repository))
