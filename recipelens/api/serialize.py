"""Convert tool results into JSON for the UI. Pure functions; no computation of facts."""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
from typing import Any

from recipelens.api.session import clean_text
from recipelens.orchestrator.router import ToolResult
from recipelens.orchestrator.state import SessionState
from recipelens.services.analytics import AnalysisReport
from recipelens.services.matcher import MatchReport, RecipeMatch
from recipelens.services.substitution import SubstitutionPlan
from recipelens.store.models import RecipeRecord, SearchResult


def _plain(obj: Any) -> Any:
    if is_dataclass(obj) and not isinstance(obj, type):
        return _plain(asdict(obj))
    if isinstance(obj, dict):
        return {str(k): _plain(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple, set, frozenset)):
        return [_plain(v) for v in obj]
    return obj


def _lines(raw: str | None) -> list[str]:
    import json

    if not raw:
        return []
    try:
        data = json.loads(raw)
        if isinstance(data, list):
            return [clean_text(str(x)) for x in data if clean_text(str(x))]
    except (ValueError, TypeError):
        pass
    return [clean_text(x) for x in raw.splitlines() if clean_text(x)]


def recipe_to_dict(r: RecipeRecord) -> dict[str, Any]:
    return {
        "recipe_id": r.recipe_id,
        "title": clean_text(r.title),
        "source": r.source,
        "ingredients": _lines(r.ingredients_raw),
        "instructions": clean_text(r.instructions_raw),
        "step_count": r.step_count,
        "sentence_count": r.sentence_count,
        "ingredient_count": r.ingredient_count,
        "instructions_low_confidence": r.instructions_low_confidence,
    }


def _search_item(r: SearchResult, rank: int) -> dict[str, Any]:
    return {
        "rank": rank,
        "recipe_id": r.recipe_id,
        "title": clean_text(r.title),
        "score": r.score,
        "score_breakdown": r.score_breakdown,
        "matched_terms": list(r.matched_terms),
    }


def _match_item(m: RecipeMatch) -> dict[str, Any]:
    return {
        "recipe_id": m.recipe_id,
        "title": clean_text(m.title),
        "rank": m.rank,
        "score": m.score,
        "score_breakdown": m.score_breakdown,
        "matched": _plain(m.matched),
        "missing": list(m.missing),
        "assumed_staples": list(m.assumed_staples),
        "optional_not_counted": list(m.optional_not_counted),
        "unused_pantry": list(m.unused_pantry),
        "step_count": m.step_count,
        "step_metric": m.step_metric,
        "instructions_low_confidence": m.instructions_low_confidence,
        "ingredient_count": m.ingredient_count,
        "why": m.why if isinstance(m.why, str) else _plain(m.why),
        "violations": _plain(m.violations),
    }


def _match_report(rep: MatchReport) -> dict[str, Any]:
    return {
        "status": rep.status,
        "results": [_match_item(m) for m in rep.results],
        "violating_alternatives": [_match_item(m) for m in rep.violating_alternatives],
        "candidates_total": rep.candidates_total,
        "candidates_scored": rep.candidates_scored,
        "truncated": rep.truncated,
        "low_confidence_excluded": rep.low_confidence_excluded,
        "effective_weights": _plain(rep.effective_weights),
        "notes": list(rep.notes),
    }


def _analytics(rep: AnalysisReport) -> dict[str, Any]:
    return {
        "filters": _plain(rep.filters),
        "n_analyzed": rep.n_analyzed,
        "denominator": rep.denominator,
        "denominator_label": rep.denominator_label,
        "secondary_denominator": rep.secondary_denominator,
        "secondary_denominator_label": rep.secondary_denominator_label,
        "formula": rep.formula,
        "normalization_notes": rep.normalization_notes,
        "metric": rep.metric,
        "cutoff_tie_count": rep.cutoff_tie_count,
        "rows": _plain(rep.rows),
    }


def _substitution(plan: SubstitutionPlan) -> dict[str, Any]:
    out = _plain(plan)
    out["original_ingredients"] = [clean_text(x) for x in plan.original_ingredients]
    out["updated_ingredients"] = [clean_text(x) for x in plan.updated_ingredients]
    return out


def serialize_result(result: ToolResult) -> dict[str, Any]:
    """Structured payload for the result panel, keyed by result kind."""
    kind = result.kind
    if kind == "search":
        items = [_search_item(r, i) for i, r in enumerate(result.data or [], 1)]
        return {"kind": kind, "items": items}
    if kind == "match" and isinstance(result.report, MatchReport):
        return {"kind": kind, **_match_report(result.report)}
    if kind == "analytics" and isinstance(result.report, AnalysisReport):
        return {"kind": kind, **_analytics(result.report)}
    if kind == "substitution" and isinstance(result.report, SubstitutionPlan):
        return {"kind": kind, **_substitution(result.report)}
    if kind == "recipe_detail" and isinstance(result.data, RecipeRecord):
        return {"kind": kind, "recipe": recipe_to_dict(result.data)}
    return {"kind": kind, "warnings": list(result.warnings)}


def serialize_state(state: SessionState) -> dict[str, Any]:
    """State plus structured, removable chips (kind/value drive the ✕ action)."""
    d = state.to_dict()
    chips: list[dict[str, Any]] = []
    if state.query_text:
        chips.append({"kind": "query", "value": state.query_text, "label": state.query_text})
    for x in state.include_ingredients:
        chips.append({"kind": "include", "value": x, "label": f"with {x}"})
    for x in state.exclude_ingredients:
        chips.append({"kind": "exclude", "value": x, "label": f"no {x}"})
    for x in state.excluded_groups:
        chips.append({"kind": "group", "value": x, "label": f"no {x}"})
    if state.max_steps is not None:
        chips.append(
            {
                "kind": "max_steps",
                "value": str(state.max_steps),
                "label": f"≤ {state.max_steps} steps",
            }
        )
    for p in state.pantry:
        chips.append({"kind": "pantry", "value": p.name, "label": p.name})
    d["chip_items"] = chips
    return d
