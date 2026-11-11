from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from recipelens.services.search import build_search
from recipelens.services.taxonomy import IngredientTaxonomy
from recipelens.store.models import Filter
from recipelens.store.repository import RecipeRepository
from recipelens.store.vector_index import load_vector_index

ROOT = Path(__file__).resolve().parents[1]

pytestmark = pytest.mark.slow


def test_penne_then_no_dairy_search_keeps_hard_filter() -> None:
    search = build_search()
    first = search.search("penne pasta", top_k=5)
    dairy_free = search.search(
        "penne pasta",
        Filter(excluded_taxonomy_groups=("dairy",)),
        top_k=5,
    )
    assert first
    assert dairy_free
    taxonomy = IngredientTaxonomy()
    recipe_ids = [result.recipe_id for result in dairy_free]
    placeholders = ",".join("?" for _ in recipe_ids)
    repository = RecipeRepository(ROOT / "data" / "recipelens.sqlite3")
    blocked = set(taxonomy.canonical_ids_for_group("dairy", repository))
    with repository._connect() as connection:
        lines = pd.read_sql_query(
            f"SELECT recipe_id, canonical FROM ingredient_lines WHERE recipe_id IN ({placeholders})",
            connection,
            params=recipe_ids,
        )
    pandas_violations = set(lines.loc[lines["canonical"].isin(blocked), "recipe_id"])
    assert not pandas_violations
    for result in dairy_free:
        explanation = taxonomy.explain_exclusion(result.recipe_id, "dairy")
        assert not explanation.lines
        assert result.ingredients_raw is not None
        assert hasattr(result, "instructions_raw")


def test_numpy_index_is_normalized_and_scores_only_allowed_ids() -> None:
    index = load_vector_index()
    assert index.indexed_rows == 5_000
    assert index.searchable_rows_full == 122_971
    assert np.isclose(np.linalg.norm(index.matrix[0].astype("float32")), 1.0, atol=1e-5)
    query = index.matrix[0].astype("float32")
    allowed = [index.ids[1], index.ids[7]]
    matches = index.search(query, allowed, top_k=2)
    assert {match.recipe_id for match in matches} == set(allowed)
    assert matches[0].cosine >= matches[1].cosine
