"""Substitution cases against the full Recipe Box DB and full vector index."""

from __future__ import annotations

from pathlib import Path

import pytest

from recipelens.orchestrator.composer import TemplateComposer
from recipelens.orchestrator.router import ToolResult
from recipelens.orchestrator.state import SessionState
from recipelens.services.matcher import Constraints
from recipelens.services.search import build_search
from recipelens.services.substitution import SubstitutionService
from recipelens.services.taxonomy import IngredientTaxonomy
from recipelens.store.repository import RecipeRepository

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def substitution() -> SubstitutionService:
    repository = RecipeRepository()
    taxonomy = IngredientTaxonomy(repository=repository)
    return SubstitutionService(repository, taxonomy, build_search(repository))


pytestmark = pytest.mark.slow


def test_real_banana_bread_without_eggs(substitution: SubstitutionService) -> None:
    """A low evidence result remains explicit instead of inventing an egg replacement."""
    plan = substitution.substitute("ar:.LVTAbd.H6F8XNOTQGLT3xw1/zp2WTK", "eggs")
    report = plan.report
    assert report.target_title == "Bates Banana Bread"
    assert report.removed_lines == ("2 eggs ADVERTISEMENT",)
    assert report.n_peers == report.with_x_count + report.without_x_count
    assert report.without_x_count > 0
    assert report.evidence_grade in {"weak", "none"}
    assert "quantity not inferred" in " ".join(plan.updated_ingredients).casefold()
    assert "not medical advice" in plan.disclaimer.casefold()


def test_real_cream_replacement_honors_dairy_restriction(
    substitution: SubstitutionService,
) -> None:
    plan = substitution.substitute(
        "ar:Iw3zHeyFE3YKc.RK2rZXb2vr.v0BfJu",
        "cream",
        Constraints(excluded_groups=("dairy",)),
    )
    report = plan.report
    assert report.target_title == "Lemon Cream Pasta with Chicken"
    assert report.n_peers == report.with_x_count + report.without_x_count
    assert report.with_x_count > 0 and report.without_x_count > 0
    assert report.candidates
    assert report.evidence_grade in {"strong", "weak"}
    assert "along with the olive oil and lemon zest" in plan.revised_instructions.casefold()
    for candidate in report.candidates:
        assert substitution.taxonomy.classify(candidate.canonical, "dairy").status not in {
            "match",
            "uncertain",
        }
        assert candidate.support_recipe_ids
        assert candidate.with_count >= 0 and candidate.without_count >= 0
    answer = TemplateComposer().compose(
        ToolResult(kind="substitution", data=plan, report=plan), SessionState()
    )
    assert "### Evidence from dataset (IDs)" in answer
    assert "Predicted effects (not verified)" in answer
    assert "not claims from the dataset" in answer
    assert "### Uncertainty" in answer


def test_real_conflicting_case_does_not_claim_a_reliable_adaptation(
    substitution: SubstitutionService,
) -> None:
    plan = substitution.substitute(
        "ar:1KH6SDul5dwa5KiXHtzBpZD8hyEdGJ2",
        "cream",
        Constraints(excluded_groups=("dairy",)),
    )
    assert plan.report.evidence_grade == "conflicting"
    assert plan.report.candidates == ()
    assert plan.report.conflicting_signals
    assert all(signal.with_recipe_ids for signal in plan.report.conflicting_signals)
    assert any("reliable adaptation cannot be supported" in note for note in plan.uncertainty)
