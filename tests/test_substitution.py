"""Fast synthetic tests for substitution intent and configured evidence grading."""

from __future__ import annotations

from pathlib import Path

import yaml

from recipelens.orchestrator.intent import RuleBasedIntentParser
from recipelens.orchestrator.state import SessionState
from recipelens.services.substitution import grade_evidence

ROOT = Path(__file__).resolve().parents[1]
CONFIG = yaml.safe_load((ROOT / "config" / "substitution.yaml").read_text(encoding="utf-8"))


def test_parser_recognizes_egg_removal_and_target_phrase() -> None:
    plan = RuleBasedIntentParser().parse("remove eggs from banana bread", SessionState())
    assert plan.intent == "substitute"
    assert plan.remove_term == "eggs"
    assert plan.remove_group == "eggs"
    assert plan.recipe_ref == "banana bread"


def test_parser_keeps_dairy_restriction_for_cream_replacement() -> None:
    plan = RuleBasedIntentParser().parse(
        "replace cream without dairy in recipe ar:abc123", SessionState()
    )
    assert plan.intent == "substitute"
    assert plan.remove_term == "cream"
    assert plan.remove_group is None
    assert plan.excluded_groups == ("dairy",)
    assert plan.recipe_ref == "ar:abc123"


def test_evidence_grades_follow_configured_numeric_thresholds() -> None:
    common = {"thresholds": CONFIG, "alpha": CONFIG["laplace_alpha"]}
    strong = grade_evidence(n_with=8, n_without=8, with_count=0, without_count=5, **common)
    weak = grade_evidence(n_with=3, n_without=3, with_count=0, without_count=2, **common)
    conflicting = grade_evidence(n_with=5, n_without=5, with_count=5, without_count=0, **common)
    none = grade_evidence(n_with=2, n_without=2, with_count=0, without_count=1, **common)
    assert strong[0] == "strong"
    assert weak[0] == "weak"
    assert conflicting[0] == "conflicting"
    assert none[0] == "none"
