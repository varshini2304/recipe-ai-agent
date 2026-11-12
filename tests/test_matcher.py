"""Matcher tests run on a small SYNTHETIC database (see tests/matcher_fixture.py)."""

from __future__ import annotations

import re

import pytest

from recipelens.services.matcher import (
    Constraints,
    Matcher,
    PantryItem,
    Preferences,
    parse_quantity,
)
from recipelens.store.repository import RecipeRepository
from tests.matcher_fixture import RECIPES, build_fixture_db

PANTRY = [PantryItem("eggs"), PantryItem("onions"), PantryItem("tomatoes"), PantryItem("rice")]


@pytest.fixture(scope="module")
def matcher(tmp_path_factory: pytest.TempPathFactory) -> Matcher:
    db = build_fixture_db(tmp_path_factory.mktemp("fixture") / "fixture.sqlite3")
    return Matcher(RecipeRepository(db))


def ids(report) -> list[str]:
    return [r.recipe_id for r in report.results]


def test_assignment_example_eggs_onions_tomatoes_rice(matcher: Matcher) -> None:
    report = matcher.match(
        PANTRY,
        Constraints(exclude_ingredients=("peanut",), max_steps=6),
        Preferences(prefer_fewer_missing=True),
        top_k=5,
    )
    assert report.status == "ok"
    assert len(report.results) == 5
    # Peanut recipe, 10-step recipe, no-instruction and terse recipes must not appear.
    for forbidden in ("syn:peanut-noodles", "syn:slow-braise", "syn:no-instructions", "syn:terse"):
        assert forbidden not in ids(report)
    # The omelette uses all four pantry items and needs nothing non-staple (parsley is optional).
    top = report.results[0]
    assert top.recipe_id == "syn:omelette"
    assert {m.canonical for m in top.matched} == {"egg", "onion", "tomato", "rice"}
    assert top.missing == ()
    assert top.assumed_staples == ("salt", "pepper")
    assert top.optional_not_counted == ("1 tablespoon parsley, optional",)
    assert [r.rank for r in report.results] == [1, 2, 3, 4, 5]
    assert all(r.step_count <= 6 for r in report.results)
    # Scores are non-increasing and each result explains itself with its own numbers.
    scores = [r.score for r in report.results]
    assert scores == sorted(scores, reverse=True)
    assert f"{top.score:.3f}" in top.why


def test_matched_missing_and_unused_are_consistent(matcher: Matcher) -> None:
    report = matcher.match(PANTRY, Constraints(max_steps=6), top_k=10)
    for r in report.results:
        used = {m.pantry_name for m in r.matched}
        assert used | set(r.unused_pantry) == {p.name for p in PANTRY}
        assert used.isdisjoint(r.unused_pantry)
        accounted = (
            sum(len(m.recipe_lines) for m in r.matched)
            + len(r.missing)
            + len(r.assumed_staples)
            + len(r.optional_not_counted)
        )
        assert accounted >= r.ingredient_count  # a line can match two pantry items, never fewer


def test_follow_up_exclude_eggs_updates_results_and_is_pure(matcher: Matcher) -> None:
    base = Constraints(exclude_ingredients=("peanut",), max_steps=6)
    first = matcher.match(PANTRY, base, top_k=10)
    again = matcher.match(PANTRY, base, top_k=10)
    assert first.to_dict() == again.to_dict()  # pure function of its inputs
    second = matcher.match(PANTRY, base.with_excluded("eggs"), top_k=10)
    assert "syn:shakshuka" in ids(first)
    assert "syn:omelette" in ids(first)
    assert "syn:shakshuka" not in ids(second)
    assert "syn:omelette" not in ids(second)
    assert "syn:egg-fried-rice" not in ids(second)
    assert ids(second)  # non-egg recipes remain


def test_eggplant_is_not_an_egg_and_tomato_sauce_is_not_a_tomato(matcher: Matcher) -> None:
    egg_only = matcher.match([PantryItem("eggs")], Constraints(), top_k=20)
    assert "syn:eggplant" not in ids(egg_only)
    tomato_only = matcher.match([PantryItem("tomatoes")], Constraints(), top_k=20)
    assert "syn:pasta-sauce" not in ids(tomato_only)
    sauce = matcher.match([PantryItem("tomato sauce")], Constraints(), top_k=20)
    assert ids(sauce) == ["syn:pasta-sauce"]  # naming the product explicitly allows it


def test_no_eligible_match_offers_separate_marked_alternatives(matcher: Matcher) -> None:
    report = matcher.match(
        [PantryItem("peanut butter"), PantryItem("noodles")],
        Constraints(exclude_ingredients=("peanut",)),
    )
    assert report.status == "no_eligible_match"
    assert report.results == ()
    assert report.violating_alternatives
    top = report.violating_alternatives[0]
    assert top.recipe_id == "syn:peanut-noodles"
    assert any(v.kind == "excluded_ingredient" for v in top.violations)
    assert any("not" in note.lower() and "relaxed" in note.lower() for note in report.notes)


def test_uncertain_taxonomy_hit_is_kept_out_of_main_ranking(matcher: Matcher) -> None:
    report = matcher.match(
        [PantryItem("rice"), PantryItem("onion")],
        Constraints(excluded_groups=("dairy",)),
        top_k=10,
    )
    assert "syn:mushroom-casserole" not in ids(report)  # cream of mushroom soup = uncertain dairy
    assert "syn:tomato-cream-soup" not in ids(report)
    blocked = matcher.match(
        [PantryItem("cream of mushroom soup")], Constraints(excluded_groups=("dairy",)), top_k=5
    )
    assert blocked.status == "no_eligible_match"
    kinds = {v.kind for a in blocked.violating_alternatives for v in a.violations}
    assert "possible_taxonomy_group" in kinds


def test_step_limit_excludes_missing_and_low_confidence_instructions(matcher: Matcher) -> None:
    pantry = [PantryItem("eggs"), PantryItem("tomatoes")]
    limited = matcher.match(pantry, Constraints(max_steps=6), top_k=20)
    assert "syn:no-instructions" not in ids(limited)  # step_count 0 must not pass "<= 6"
    assert "syn:terse" not in ids(limited)
    assert limited.low_confidence_excluded >= 1
    assert any("low-confidence" in n for n in limited.notes)
    unlimited = matcher.match(pantry, Constraints(), top_k=20)
    assert "syn:terse" in ids(unlimited)


def test_staples_reported_not_dropped_and_toggle(matcher: Matcher) -> None:
    pantry = [PantryItem("rice")]
    on = matcher.match(pantry, Constraints(), Preferences(assume_staples=True), top_k=20)
    plain_on = next(r for r in on.results if r.recipe_id == "syn:plain-rice")
    assert plain_on.missing == ()
    assert set(plain_on.assumed_staples) == {"2 cups water", "salt"}
    off = matcher.match(pantry, Constraints(), Preferences(assume_staples=False), top_k=20)
    plain_off = next(r for r in off.results if r.recipe_id == "syn:plain-rice")
    assert set(plain_off.missing) == {"2 cups water", "salt"}
    assert plain_off.assumed_staples == ()


def test_quantity_checks(matcher: Matcher) -> None:
    enough = matcher.match([PantryItem("eggs", 4)], Constraints(), top_k=20)
    short = matcher.match([PantryItem("eggs", 2)], Constraints(), top_k=20)
    shakshuka = lambda rep: next(r for r in rep.results if r.recipe_id == "syn:shakshuka")
    assert shakshuka(enough).matched[0].quantity_check == "sufficient"
    assert shakshuka(short).matched[0].quantity_check == "insufficient"
    assert shakshuka(short).quantity_check == "insufficient"
    assert shakshuka(short).score < shakshuka(enough).score  # shortfall earns reduced credit
    # cups -> tablespoons are convertible; cups -> cans are not.
    convertible = matcher.match([PantryItem("olive oil", 0.25, "cup")], Constraints(), top_k=20)
    tomato_rice = next(r for r in convertible.results if r.recipe_id == "syn:tomato-rice")
    assert tomato_rice.matched[0].quantity_check == "sufficient"  # 4 tbsp needed 2
    mismatch = matcher.match([PantryItem("rice", 3, "can")], Constraints(), top_k=20)
    unit_clash = next(r for r in mismatch.results if r.recipe_id == "syn:tomato-rice")
    assert unit_clash.matched[0].quantity_check == "not_verified"
    assert unit_clash.quantity_check == "not_verified"
    none_given = matcher.match([PantryItem("rice")], Constraints(), top_k=3)
    assert all(r.quantity_check == "no_quantities_given" for r in none_given.results)


def test_preferences_reweight_but_never_filter(matcher: Matcher) -> None:
    plain = matcher.match(PANTRY, Constraints(), top_k=20)
    fewer_steps = matcher.match(PANTRY, Constraints(), Preferences(prefer_fewer_steps=True), top_k=20)
    assert set(ids(plain)) == set(ids(fewer_steps))
    assert fewer_steps.effective_weights["steps"] > plain.effective_weights["steps"]
    assert abs(sum(fewer_steps.effective_weights.values()) - 1.0) < 1e-3


def test_unknown_pantry_item_is_flagged_not_silently_ignored(matcher: Matcher) -> None:
    report = matcher.match([PantryItem("dragonfruit"), PantryItem("rice")], Constraints())
    unknown = next(p for p in report.pantry if p.input_name == "dragonfruit")
    assert not unknown.found_in_dataset
    assert any("dragonfruit" in n for n in report.notes)


def test_no_hard_constraint_violation_by_independent_raw_line_check(matcher: Matcher) -> None:
    constraints = Constraints(exclude_ingredients=("peanut", "eggs"), excluded_groups=("dairy",), max_steps=6)
    report = matcher.match(PANTRY, constraints, top_k=20)
    assert report.secondary_exclusions == 0 or report.status == "ok"
    word = re.compile(r"\b(?:peanuts?|eggs?)\b|\b(?:milk|cream|cheese|butter)\b", re.IGNORECASE)
    for r in report.results:
        raw_lines = RECIPES[r.recipe_id][1]  # source-of-truth fixture text, not the canonical column
        assert not any(word.search(line) for line in raw_lines), r.recipe_id
        assert r.step_count <= 6
        assert r.violations == ()


def test_original_title_ingredients_and_instructions_are_preserved(matcher: Matcher) -> None:
    report = matcher.match([PantryItem("rice")], Constraints(), top_k=20)
    for r in report.results:
        title, ingredients, instructions = RECIPES[r.recipe_id]
        assert r.title == title
        assert list(r.ingredient_lines) == ingredients
        assert r.instructions_raw == instructions


def test_input_validation(matcher: Matcher) -> None:
    with pytest.raises(ValueError):
        matcher.match([], Constraints())
    with pytest.raises(KeyError):
        matcher.match(PANTRY, Constraints(excluded_groups=("not-a-group",)))
    with pytest.raises(ValueError):
        matcher.match(PANTRY, Constraints(), top_k=0)


@pytest.mark.parametrize(
    ("text", "expected"),
    [("2", 2.0), ("1/2", 0.5), ("1 1/2", 1.5), ("½", 0.5), ("1½", 1.5), ("0.25", 0.25),
     ("2-3", None), ("", None), (None, None), ("a few", None), ("1/0", None)],
)  # fmt: skip
def test_parse_quantity(text: str | None, expected: float | None) -> None:
    assert parse_quantity(text) == pytest.approx(expected) if expected is not None else parse_quantity(text) is None


def test_scrape_noise_hidden_in_display_but_kept_in_original_lines(matcher: Matcher) -> None:
    report = matcher.match([PantryItem("rice")], Constraints(), top_k=20)
    noisy = next(r for r in report.results if r.recipe_id == "syn:noisy")
    assert noisy.missing == ("1 cup spinach",)
    assert noisy.assumed_staples == ("1 tablespoon olive oil",)
    assert noisy.matched[0].recipe_lines == ("1 cup rice",)
    assert "1 cup spinach ADVERTISEMENT" in noisy.ingredient_lines  # original text preserved
