"""Grounding verifier: cross-checks cited recipe IDs and numeric claims against ToolResult."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from recipelens.orchestrator.router import ToolResult
from recipelens.services.analytics import AnalysisReport
from recipelens.services.matcher import MatchReport
from recipelens.store.models import RecipeRecord, SearchResult

EXPLICIT_ID_PATTERN = re.compile(r"\[ID:\s*([^\]]+)\]")
GENERIC_ID_PATTERN = re.compile(r"\b((?:ar|fn|ip|epi):[^\s\],]+)")
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
        explicit = EXPLICIT_ID_PATTERN.findall(text)
        if explicit:
            return list(dict.fromkeys(explicit))
        return list(dict.fromkeys(GENERIC_ID_PATTERN.findall(text)))

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
        """Collect source numbers and common display formats from the tool output."""
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
                    allowed.add(f"{val * 100:.2f}%")

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

        # Include numeric text from grounded titles, original ingredient lines, and details.
        # Numeric ID fragments are removed from both sides before comparison.
        for value in NUMBER_PATTERN.findall(repr(result)):
            allowed.add(value)
            allowed.add(value.replace(",", ""))

        # List positions are derived from the returned candidate order and count.
        result_count = len(result.data) if isinstance(result.data, list) else 0
        if isinstance(result.report, MatchReport):
            result_count = max(result_count, len(result.report.results))
        for rank in range(1, result_count + 1):
            add_num(rank)

        return allowed

    def verify(self, answer: str, result: ToolResult) -> GroundingVerification:
        """Check cited recipe IDs and numeric claims against ToolResult."""
        cited_ids = self.extract_recipe_ids(answer)
        allowed_ids = self._collect_allowed_ids(result)
        ungrounded_ids = tuple(rid for rid in cited_ids if rid not in allowed_ids)
        without_ids = EXPLICIT_ID_PATTERN.sub("", answer)
        without_ids = GENERIC_ID_PATTERN.sub("", without_ids)
        without_list_ranks = re.sub(r"(?m)^\s*\d+\.\s", "", without_ids)
        cited_numbers = NUMBER_PATTERN.findall(without_list_ranks)
        allowed_numbers = self._collect_allowed_numbers(result)
        ungrounded_numbers = tuple(
            number
            for number in cited_numbers
            if number not in allowed_numbers and number.replace(",", "") not in allowed_numbers
        )

        if ungrounded_ids or ungrounded_numbers:
            problems = []
            if ungrounded_ids:
                problems.append(f"ungrounded recipe IDs: {', '.join(ungrounded_ids)}")
            if ungrounded_numbers:
                problems.append(f"ungrounded numbers: {', '.join(ungrounded_numbers)}")
            return GroundingVerification(
                is_grounded=False,
                ungrounded_ids=ungrounded_ids,
                ungrounded_numbers=ungrounded_numbers,
                details="Answer contains " + "; ".join(problems),
            )

        return GroundingVerification(
            is_grounded=True,
            details="All cited recipe IDs and numeric claims are grounded in the tool result.",
        )
