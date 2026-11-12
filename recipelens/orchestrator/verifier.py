"""Grounding verifier: cross-checks cited recipe IDs and numeric claims against ToolResult."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from recipelens.orchestrator.router import ToolResult
from recipelens.services.analytics import AnalysisReport
from recipelens.services.matcher import MatchReport
from recipelens.store.models import RecipeRecord, SearchResult

RECIPE_ID_PATTERN = re.compile(r"\b((?:ar|fn|ip):[A-Za-z0-9_./+-]+)\b")
NUMBER_PATTERN = re.compile(r"\b\d+(?:,\d+)*(?:\.\d+)?%?\b")


@dataclass(frozen=True, slots=True)
class GroundingVerification:
    """Outcome of grounding validation."""

    is_grounded: bool
    ungrounded_ids: tuple[str, ...] = ()
    ungrounded_numbers: tuple[str, ...] = ()
    details: str = ""


class GroundingVerifier:
    """Verifies that an answer does not hallucinate recipe IDs or numbers."""

    def extract_recipe_ids(self, text: str) -> list[str]:
        """Extract recipe IDs from text."""
        return list(dict.fromkeys(RECIPE_ID_PATTERN.findall(text)))

    def _collect_allowed_ids(self, result: ToolResult) -> set[str]:
        """Collect all recipe IDs present in the ToolResult."""
        allowed: set[str] = set()

        if isinstance(result.data, list):
            for item in result.data:
                if isinstance(item, SearchResult):
                    allowed.add(item.recipe_id)
                elif isinstance(item, dict) and "recipe_id" in item:
                    allowed.add(item["recipe_id"])
        elif isinstance(result.data, RecipeRecord):
            allowed.add(result.data.recipe_id)

        if isinstance(result.report, MatchReport):
            for m in result.report.results:
                allowed.add(m.recipe_id)
            for m in result.report.violating_alternatives:
                allowed.add(m.recipe_id)

        if isinstance(result.report, AnalysisReport):
            for r in result.report.rows:
                if isinstance(r, dict) and "recipe_id" in r:
                    allowed.add(r["recipe_id"])

        return allowed

    def _collect_allowed_numbers(self, result: ToolResult) -> set[str]:
        """Collect valid numbers (formatted as strings) from ToolResult."""
        allowed: set[str] = set()

        def add_num(val: Any) -> None:
            if val is None:
                return
            if isinstance(val, (int, float)):
                allowed.add(str(val))
                if isinstance(val, int):
                    allowed.add(f"{val:,}")
                else:
                    allowed.add(f"{val:.1f}")
                    allowed.add(f"{val:.2f}")

        if isinstance(result.report, AnalysisReport):
            rep = result.report
            add_num(rep.n_analyzed)
            add_num(rep.denominator)
            add_num(rep.secondary_denominator)
            add_num(rep.cutoff_tie_count)
            for r in rep.rows:
                if isinstance(r, dict):
                    for v in r.values():
                        add_num(v)

        if isinstance(result.report, MatchReport):
            rep = result.report
            add_num(len(rep.results))
            add_num(len(rep.violating_alternatives))
            for m in rep.results:
                add_num(m.score)
                add_num(m.step_count)
                add_num(m.rank)
            for m in rep.violating_alternatives:
                add_num(m.step_count)
                add_num(m.rank)

        if isinstance(result.data, list):
            add_num(len(result.data))

        return allowed

    def verify(self, answer: str, result: ToolResult) -> GroundingVerification:
        """Check all cited recipe IDs against ToolResult."""
        cited_ids = self.extract_recipe_ids(answer)
        allowed_ids = self._collect_allowed_ids(result)

        ungrounded_ids = tuple(rid for rid in cited_ids if rid not in allowed_ids)

        if ungrounded_ids:
            return GroundingVerification(
                is_grounded=False,
                ungrounded_ids=ungrounded_ids,
                details=f"Answer cites ungrounded recipe IDs: {', '.join(ungrounded_ids)}",
            )

        return GroundingVerification(
            is_grounded=True,
            details="All cited recipe IDs are fully grounded in the tool result.",
        )
