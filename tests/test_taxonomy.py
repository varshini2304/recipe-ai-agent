from pathlib import Path

import pytest

from recipelens.services.taxonomy import IngredientTaxonomy
from recipelens.store.repository import RecipeRepository

ROOT = Path(__file__).resolve().parents[1]


def test_peanut_butter_and_coconut_milk_are_not_dairy() -> None:
    taxonomy = IngredientTaxonomy(repository=RecipeRepository(ROOT / "data" / "recipelens.sqlite3"))
    assert taxonomy.classify("peanut butter", "dairy").status == "excluded"
    assert taxonomy.classify("coconut milk", "dairy").status == "excluded"
    assert taxonomy.classify("almond butter", "dairy").status == "excluded"
    assert taxonomy.classify("butter beans", "dairy").status == "excluded"
    assert taxonomy.classify("cream of tartar", "dairy").status == "excluded"
    assert taxonomy.classify("chicken broth", "meat").status == "uncertain"


@pytest.mark.slow
def test_taxonomy_explanation_returns_original_ingredient_line() -> None:
    repository = RecipeRepository(ROOT / "data" / "recipelens.sqlite3")
    taxonomy = IngredientTaxonomy(repository=repository)
    with repository._connect() as connection:
        recipe_id = connection.execute(
            "SELECT recipe_id FROM ingredient_lines WHERE canonical='butter' LIMIT 1"
        ).fetchone()[0]
    explanation = taxonomy.explain_exclusion(recipe_id, "dairy")
    assert explanation.lines
    assert any(line.canonical == "butter" and line.status == "match" for line in explanation.lines)
    assert all(line.raw for line in explanation.lines)
