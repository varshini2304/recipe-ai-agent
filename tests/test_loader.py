import json
import sqlite3
from pathlib import Path

import pytest

from recipelens.data.loader import make_recipe
from recipelens.store.models import Filter
from recipelens.store.repository import RecipeRepository
from scripts.ingest import build_database, file_record_count, source_files


def test_ids_stay_stable_across_two_ingest_runs(tmp_path: Path) -> None:
    source = tmp_path / "recipes_raw_nosource_ar.json"
    source.write_text(
        json.dumps({"source-key": {"title": "Soup", "ingredients": [], "instructions": None}})
    )
    db = tmp_path / "recipes.sqlite3"
    build_database([source], db)
    with sqlite3.connect(db) as connection:
        first = connection.execute("SELECT recipe_id FROM recipes").fetchall()
    build_database([source], db)
    with sqlite3.connect(db) as connection:
        second = connection.execute("SELECT recipe_id FROM recipes").fetchall()
    assert first == second == [("ar:source-key",)]


@pytest.mark.slow
def test_real_database_row_counts_equal_source_counts() -> None:
    from scripts.ingest import DB_PATH

    assert DB_PATH.exists(), (
        "Run `python scripts/ingest.py` before this source-data integration test."
    )
    with sqlite3.connect(DB_PATH) as connection:
        actual = dict(connection.execute("SELECT source, COUNT(*) FROM recipes GROUP BY source"))
    expected = {
        path.stem.removeprefix("recipes_raw_nosource_"): file_record_count(path)
        for path in source_files()
    }
    assert actual == expected


@pytest.mark.slow
def test_quality_flags_retain_missing_source_rows() -> None:
    from scripts.ingest import DB_PATH

    with sqlite3.connect(DB_PATH) as connection:
        total, missing = connection.execute(
            "SELECT COUNT(*), SUM(has_title=0 OR has_ingredients=0 OR has_instructions=0) FROM recipes"
        ).fetchone()
    assert total == 125_164
    assert missing > 0


def test_raw_source_text_is_preserved_separately_from_clean_fields() -> None:
    original = {
        "title": "  Example title  ",
        "ingredients": ["1 cup scallions ADVERTISEMENT"],
        "instructions": " Stir gently.\n",
    }
    recipe, parsed = make_recipe("fn", "raw-key", original, None)
    assert recipe["title"] == original["title"]
    assert recipe["title_clean"] == "Example title"
    assert json.loads(recipe["ingredients_raw"]) == original["ingredients"]
    assert recipe["instructions_raw"] == original["instructions"]
    assert recipe["instructions_clean"] == "Stir gently."
    assert recipe["sentence_count"] == 1
    assert recipe["instructions_low_confidence"] == 1
    assert parsed[0].raw == original["ingredients"][0]


def test_filter_metric_selects_step_or_sentence_count(tmp_path: Path) -> None:
    source = tmp_path / "recipes_raw_nosource_ar.json"
    source.write_text(
        json.dumps(
            {
                "metric-case": {
                    "title": "Metric Case",
                    "ingredients": ["1 cup flour"],
                    "instructions": "Bake until set. Cool completely.\nServe warm.",
                }
            }
        ),
        encoding="utf-8",
    )
    database = tmp_path / "metrics.sqlite3"
    build_database([source], database)
    repository = RecipeRepository(database)
    by_steps = repository.filter_ids(Filter(min_steps=3, step_metric="step_count"))
    by_sentences = repository.filter_ids(Filter(min_steps=3, step_metric="sentence_count"))
    assert by_steps == []
    assert by_sentences == ["ar:metric-case"]
