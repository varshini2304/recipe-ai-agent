import json
import re
from pathlib import Path

import pandas as pd
import pytest

from recipelens.services.analytics import AnalyticsService
from recipelens.store.models import Filter
from recipelens.store.repository import RecipeRepository

pytestmark = pytest.mark.slow

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "recipelens.sqlite3"


def test_garlic_and_onion_count_matches_independent_pandas() -> None:
    repository = RecipeRepository(DB)
    report = AnalyticsService(repository).count_with(
        ["garlic", "onion"], mode="all", recipe_filter=Filter(match_mode="exact")
    )
    with repository._connect() as connection:
        lines = pd.read_sql_query(
            "SELECT recipe_id, canonical FROM ingredient_lines WHERE canonical IN ('garlic', 'onion')",
            connection,
        )
        recipes_count = pd.read_sql_query("SELECT COUNT(*) AS n FROM recipes", connection).iloc[
            0, 0
        ]
    grouped = lines.groupby("recipe_id")["canonical"].agg(set)
    pandas_count = sum({"garlic", "onion"}.issubset(items) for items in grouped)
    assert pandas_count == report.rows[0]["count"]
    assert report.denominator == 122_971
    assert report.secondary_denominator == recipes_count == 125_164
    assert abs(report.rows[0]["percentage"] - 100 * report.rows[0]["count"] / 122_971) < 1e-12


def test_five_tomato_recipes_with_fewest_steps_match_pandas() -> None:
    repository = RecipeRepository(DB)
    report = AnalyticsService(repository).rank_by_steps(
        Filter(include_ingredients=("tomato",), match_mode="exact"),
        order="asc",
        top_k=5,
    )
    with repository._connect() as connection:
        recipes = pd.read_sql_query(
            "SELECT recipe_id,title,step_count,sentence_count,ingredient_count,instructions_low_confidence FROM recipes WHERE has_instructions=1 AND instructions_low_confidence=0",
            connection,
        )
        tomato_ids = pd.read_sql_query(
            "SELECT DISTINCT recipe_id FROM ingredient_lines WHERE canonical='tomato'", connection
        )
    expected = (
        recipes.merge(tomato_ids, on="recipe_id")
        .sort_values(["step_count", "ingredient_count", "recipe_id"], ascending=[True, True, True])
        .head(5)
        .reset_index(drop=True)
    )
    assert [row["recipe_id"] for row in report.rows] == expected["recipe_id"].tolist()
    assert [row["metric_value"] for row in report.rows] == expected["step_count"].tolist()
    assert report.denominator == 122_971
    assert report.secondary_denominator == 125_164
    assert report.metric == "step_count"
    assert report.low_confidence_excluded == report.low_confidence_candidates
    assert all(not row["instructions_low_confidence"] for row in report.rows)
    cutoff = expected.iloc[-1]["step_count"]
    assert report.cutoff_tie_count == int(
        (recipes.merge(tomato_ids, on="recipe_id")["step_count"] == cutoff).sum()
    )
    assert all("ingredient_count" in row for row in report.rows)


def test_ingredient_stats_use_all_usable_ingredient_recipes() -> None:
    report = AnalyticsService(RecipeRepository(DB)).ingredient_count_stats()
    assert report.denominator == 122_971
    assert "usable-ingredient recipes" in report.denominator_label


def test_raw_regex_audit_for_tomato_garlic_onion_and_combination() -> None:
    patterns = {
        "tomato": re.compile(r"\btomato(?:es)?\b", re.IGNORECASE),
        "garlic": re.compile(r"\bgarlic\b", re.IGNORECASE),
        "onion": re.compile(r"\bonions?\b", re.IGNORECASE),
    }
    with RecipeRepository(DB)._connect() as connection:
        recipes = pd.read_sql_query(
            "SELECT recipe_id,has_ingredients,ingredients_raw FROM recipes", connection
        )
        canonical = pd.read_sql_query(
            "SELECT recipe_id,canonical FROM ingredient_lines", connection
        )
    raw_hits = {term: set() for term in patterns}
    for recipe in recipes.itertuples(index=False):
        raw = json.loads(recipe.ingredients_raw) if isinstance(recipe.ingredients_raw, str) else []
        text = "\n".join(line for line in raw if isinstance(line, str))
        for term, pattern in patterns.items():
            if pattern.search(text):
                raw_hits[term].add(recipe.recipe_id)
    canonical_hits = {
        term: set(canonical.loc[canonical.canonical.eq(term), "recipe_id"]) for term in patterns
    }
    expected = {"tomato": (1_205, 19_391), "garlic": (13_475, 37_344), "onion": (5_309, 36_905)}
    for term, (exact_count, regex_count) in expected.items():
        assert len(canonical_hits[term]) == exact_count
        assert len(raw_hits[term]) == regex_count
        assert len(raw_hits[term]) - len(canonical_hits[term]) > 0
    raw_and = raw_hits["garlic"] & raw_hits["onion"]
    exact_and = canonical_hits["garlic"] & canonical_hits["onion"]
    assert len(exact_and) == 1_731
    assert len(raw_and) == 20_245


def test_family_mode_is_reviewed_and_raw_regex_baselines_are_reported() -> None:
    service = AnalyticsService(RecipeRepository(DB))
    with service.repository._connect() as connection:
        raw_rows = pd.read_sql_query(
            "SELECT recipe_id,ingredients_raw FROM recipes WHERE has_ingredients=1", connection
        )
        canonical_rows = pd.read_sql_query(
            "SELECT recipe_id,canonical FROM ingredient_lines", connection
        )
    import re

    import yaml

    family_config = yaml.safe_load((ROOT / "config" / "families.yaml").read_text(encoding="utf-8"))[
        "families"
    ]
    expected_family = {"tomato": 13_656, "garlic": 32_434, "onion": 34_980}
    raw_family_counts = {"tomato": 12_011, "garlic": 30_357, "onion": 30_311}
    raw_family_ids_by_term = {}
    for term, definitions in family_config.items():
        includes = [re.compile(pattern, re.IGNORECASE) for pattern in definitions["match_patterns"]]
        excludes = [
            re.compile(pattern, re.IGNORECASE) for pattern in definitions["exclude_patterns"]
        ]
        raw_ids = set()
        for recipe in raw_rows.itertuples(index=False):
            raw = (
                json.loads(recipe.ingredients_raw)
                if isinstance(recipe.ingredients_raw, str)
                else []
            )
            if any(
                any(p.search(line.split(",", maxsplit=1)[0].strip()) for p in includes)
                and not any(p.search(line) for p in excludes)
                for line in raw
                if isinstance(line, str)
            ):
                raw_ids.add(recipe.recipe_id)
        assert len(raw_ids) == raw_family_counts[term]
        raw_family_ids_by_term[term] = raw_ids

        family = service.count_with([term], recipe_filter=Filter(match_mode="family"))
        variants = service.families.variants(term)
        pandas_ids = set(canonical_rows.loc[canonical_rows.canonical.isin(variants), "recipe_id"])
        assert family.rows[0]["count"] == expected_family[term] == len(pandas_ids)
        assert "match_mode=family" in family.normalization_notes
        exact = service.count_with([term], recipe_filter=Filter(match_mode="exact"))
        exact_ids = set(canonical_rows.loc[canonical_rows.canonical.eq(term), "recipe_id"])
        assert exact.rows[0]["count"] == len(exact_ids)
        assert "match_mode=exact" in exact.normalization_notes

    family_and = service.count_with(
        ["garlic", "onion"],
        mode="all",
        recipe_filter=Filter(match_mode="family"),
    )
    garlic_ids = set(
        canonical_rows.loc[
            canonical_rows.canonical.isin(service.families.variants("garlic")), "recipe_id"
        ]
    )
    onion_ids = set(
        canonical_rows.loc[
            canonical_rows.canonical.isin(service.families.variants("onion")), "recipe_id"
        ]
    )
    assert family_and.rows[0]["count"] == len(garlic_ids & onion_ids)
    raw_family_and = raw_family_ids_by_term["garlic"] & raw_family_ids_by_term["onion"]
    assert len(raw_family_and) == 14_821
