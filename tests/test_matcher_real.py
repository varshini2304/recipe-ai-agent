"""Matcher checks against the REAL database. Slow; run with `make test-all`."""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path

import pytest

from recipelens.services.matcher import Constraints, Matcher, PantryItem, Preferences
from recipelens.store.repository import RecipeRepository

pytestmark = pytest.mark.slow
DB = Path(__file__).resolve().parents[1] / "data" / "recipelens.sqlite3"
PANTRY = [PantryItem("eggs"), PantryItem("onions"), PantryItem("tomatoes"), PantryItem("rice")]


def _raw_lines(recipe_ids: list[str]) -> dict[str, list[str]]:
    """Independent of the canonical column: read the original ingredient text straight from SQLite."""
    with sqlite3.connect(DB) as connection:
        placeholders = ",".join("?" for _ in recipe_ids)
        rows = connection.execute(
            f"SELECT recipe_id, raw FROM ingredient_lines WHERE recipe_id IN ({placeholders})",
            recipe_ids,
        ).fetchall()
    out: dict[str, list[str]] = {rid: [] for rid in recipe_ids}
    for rid, raw in rows:
        out[rid].append(raw)
    return out


@pytest.fixture(scope="module")
def matcher() -> Matcher:
    return Matcher(RecipeRepository(DB))


def test_assignment_example_on_real_data(matcher: Matcher) -> None:
    report = matcher.match(
        PANTRY,
        Constraints(exclude_ingredients=("peanut",), max_steps=6),
        Preferences(prefer_fewer_missing=True),
        top_k=5,
    )
    assert report.status == "ok"
    assert len(report.results) == 5
    raw = _raw_lines([r.recipe_id for r in report.results])
    for r in report.results:
        assert 1 <= r.step_count <= 6
        assert not any(re.search(r"\bpeanuts?\b", line, re.IGNORECASE) for line in raw[r.recipe_id])
        assert r.violations == ()
    assert report.secondary_exclusions == 0


def test_exclude_eggs_follow_up_on_real_data(matcher: Matcher) -> None:
    base = Constraints(exclude_ingredients=("peanut",), max_steps=6)
    report = matcher.match(PANTRY, base.with_excluded("eggs"), top_k=5)
    raw = _raw_lines([r.recipe_id for r in report.results])
    for r in report.results:
        assert not any(re.search(r"\beggs?\b", line, re.IGNORECASE) for line in raw[r.recipe_id])


def test_no_eligible_match_on_real_data(matcher: Matcher) -> None:
    report = matcher.match(
        [PantryItem("peanut butter"), PantryItem("peanuts")],
        Constraints(exclude_ingredients=("peanut",)),
    )
    assert report.status == "no_eligible_match"
    assert report.results == ()
    assert report.violating_alternatives
    assert all(a.violations for a in report.violating_alternatives)
