"""Tests for conversation orchestrator (Phase 4A): state, intent, router, composer, verifier."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from recipelens.orchestrator.chat import ChatSession
from recipelens.orchestrator.composer import TemplateComposer
from recipelens.orchestrator.intent import RuleBasedIntentParser
from recipelens.orchestrator.router import Router, ToolResult
from recipelens.orchestrator.schemas import QueryPlan
from recipelens.orchestrator.state import SessionState
from recipelens.orchestrator.verifier import GroundingVerifier
from recipelens.services.analytics import AnalyticsService
from recipelens.services.matcher import Matcher, PantryItem
from recipelens.services.taxonomy import IngredientTaxonomy
from recipelens.store.models import Filter, RecipeRecord, SearchResult
from recipelens.store.repository import RecipeRepository
from tests.matcher_fixture import build_fixture_db

ROOT = Path(__file__).resolve().parents[1]


# --------------------------------------------------------------------------- Fast unit tests


def test_multiturn_search_constraint_merge() -> None:
    """Multi-turn test: search 'penne pasta' -> 'I cannot have dairy' preserves query."""
    parser = RuleBasedIntentParser()
    state = SessionState()

    # Turn 1: Initial search
    p1 = parser.parse("penne pasta", state)
    state = state.merge(p1)
    assert state.query_text == "penne pasta"
    assert state.active_mode == "search"
    assert state.excluded_groups == ()

    # Turn 2: Follow-up constraint
    p2 = parser.parse("I cannot have dairy", state)
    assert p2.intent == "refine"
    assert p2.excluded_groups == ("dairy",)
    state = state.merge(p2)
    assert state.query_text == "penne pasta"  # Preserved!
    assert state.excluded_groups == ("dairy",)
    assert "dairy" in state.matcher_constraints.excluded_groups

    # Turn 3: Second constraint
    p3 = parser.parse("actually make it gluten-free too", state)
    assert p3.intent == "refine"
    assert p3.excluded_groups == ("gluten",)
    state = state.merge(p3)
    assert state.query_text == "penne pasta"  # Still preserved!
    assert state.excluded_groups == ("dairy", "gluten")
    assert set(state.matcher_constraints.excluded_groups) == {"dairy", "gluten"}


def test_multiturn_matcher_constraint_merge() -> None:
    """Matcher multi-turn: pantry + no peanuts -> exclude eggs too."""
    parser = RuleBasedIntentParser()
    state = SessionState()

    # Turn 1: Pantry input
    p1 = parser.parse("I have eggs, onions, tomatoes, rice, no peanuts, at most 6 steps", state)
    assert p1.intent == "match"
    assert p1.max_steps == 6
    assert p1.excluded_groups == ("peanuts",)
    state = state.merge(p1)
    assert state.active_mode == "match"
    assert state.max_steps == 6
    assert state.excluded_groups == ("peanuts",)
    assert len(state.pantry) >= 4

    # Turn 2: Follow-up exclusion
    p2 = parser.parse("exclude eggs too", state)
    assert p2.intent == "refine"
    assert "eggs" in p2.excluded_groups
    state = state.merge(p2)
    assert state.active_mode == "match"
    assert set(state.excluded_groups) == {"peanuts", "eggs"}
    assert "eggs" in state.matcher_constraints.excluded_groups
    assert state.max_steps == 6
    assert len(state.pantry) >= 4  # Pantry preserved!


def test_reset_clears_state() -> None:
    """Reset intent clears active query, constraints, and pantry."""
    parser = RuleBasedIntentParser()
    state = SessionState(
        query_text="chicken curry",
        excluded_groups=("dairy",),
        max_steps=5,
        pantry=(PantryItem("chicken"),),
    )
    plan = parser.parse("reset", state)
    assert plan.intent == "reset"
    new_state = state.merge(plan)
    assert new_state.query_text == ""
    assert new_state.excluded_groups == ()
    assert new_state.max_steps is None
    assert new_state.pantry == ()


def test_unsupported_nutrition_query() -> None:
    """Asking for calories or nutrition yields unsupported intent and clear reason."""
    parser = RuleBasedIntentParser()
    state = SessionState()
    plan = parser.parse("how many calories does this recipe have?", state)
    assert plan.intent == "unsupported"
    assert plan.unsupported_reason is not None

    composer = TemplateComposer()
    result = ToolResult(kind="unsupported", unsupported_reason=plan.unsupported_reason)
    answer = composer.compose(result, state)
    assert "Unsupported request" in answer
    assert "calories" in answer.lower() or "nutritional" in answer.lower()


def test_ambiguous_reference_asks_clarification() -> None:
    """Reference like 'the second one' with no previous search results prompts clarification."""
    parser = RuleBasedIntentParser()
    state = SessionState()  # Empty results
    plan = parser.parse("tell me about the second one", state)
    assert plan.clarification_question is not None
    assert "Which recipe" in plan.clarification_question


def test_grounding_verifier_catches_fabricated_id() -> None:
    """Verifier flags fabricated recipe IDs that do not exist in the tool result."""
    verifier = GroundingVerifier()
    res = SearchResult(
        recipe_id="ar:valid123",
        title="Real Recipe",
        score=0.95,
        score_breakdown={},
        matched_terms=(),
        ingredients_raw=None,
        instructions_raw=None,
    )
    tool_result = ToolResult(kind="search", data=[res])

    # Legitimate answer
    valid_answer = "1. Real Recipe [ID: ar:valid123]"
    check_valid = verifier.verify(valid_answer, tool_result)
    assert check_valid.is_grounded is True

    # Hallucinated answer
    fake_answer = "1. Fake Recipe [ID: ar:fabricated999]"
    check_fake = verifier.verify(fake_answer, tool_result)
    assert check_fake.is_grounded is False
    assert "ar:fabricated999" in check_fake.ungrounded_ids


def test_orchestrator_with_fixture_db(tmp_path: Path) -> None:
    """Fast integration test using synthetic fixture database."""
    db_path = build_fixture_db(tmp_path / "test.sqlite3")
    repo = RecipeRepository(db_path=db_path)
    taxonomy = IngredientTaxonomy(repository=repo)
    analytics = AnalyticsService(repository=repo, taxonomy=taxonomy)
    matcher = Matcher(repository=repo, taxonomy=taxonomy)

    # Mock search service returning fixture recipes
    search_mock = MagicMock()
    search_mock.search.return_value = [
        SearchResult(
            recipe_id="syn:egg-fried-rice",
            title="Egg Fried Rice",
            score=0.03,
            score_breakdown={},
            matched_terms=("rice",),
            ingredients_raw='["rice"]',
            instructions_raw="Cook rice",
        )
    ]

    session = ChatSession(
        repository=repo,
        search_service=search_mock,
        analytics_service=analytics,
        matcher_service=matcher,
    )

    # 1. Search turn
    ans1 = session.turn("fried rice")
    assert "Egg Fried Rice" in ans1
    assert "syn:egg-fried-rice" in ans1
    assert "fried rice" in session.state_summary()

    # 2. Detail turn
    ans2 = session.turn("tell me about the 1st one")
    assert "Ingredients:" in ans2
    assert "Egg Fried Rice" in ans2

    # 3. Analytics turn
    ans3 = session.turn("how many recipes have rice AND onion?")
    assert "Recipes analyzed:" in ans3
    assert "Formula:" in ans3


# --------------------------------------------------------------------------- Real DB integration test


@pytest.mark.slow
def test_real_db_multiturn_flow() -> None:
    """Integration test against full real database: search -> constraint -> analytics -> match."""
    session = ChatSession.build()

    # 1. Search
    ans1 = session.turn("penne pasta")
    assert "Found" in ans1
    assert "state: [query: penne pasta]" in session.state_summary()

    # 2. Add dairy constraint
    ans2 = session.turn("I cannot have dairy")
    assert "dairy" in session.state_summary()
    assert "exclude" in session.state_summary() or "no dairy" in session.state_summary()

    # 3. Analytics
    ans3 = session.turn("How many recipes have garlic AND onion?")
    assert "Recipes analyzed:" in ans3
    assert "Formula:" in ans3

    # 4. Pantry match
    ans4 = session.turn("I have eggs, onions, tomatoes, rice, no peanuts, at most 6 steps")
    assert "matching your pantry" in ans4 or "recipe(s)" in ans4

    # 5. Follow-up refine
    ans5 = session.turn("exclude eggs too")
    assert "eggs" in session.state_summary()
