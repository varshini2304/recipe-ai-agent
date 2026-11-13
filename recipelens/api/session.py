"""Chat session variant that exposes the structured result of each turn (for the UI)."""

from __future__ import annotations

import re
import time
from dataclasses import dataclass, field, replace

from recipelens.orchestrator.chat import ChatSession
from recipelens.orchestrator.router import ToolResult
from recipelens.orchestrator.schemas import QueryPlan
from recipelens.orchestrator.state import SessionState
from recipelens.orchestrator.verifier import GroundingVerification
from recipelens.services.matcher import Constraints

NOISE = re.compile(r"[ \t]*ADVERTISEMENT[ \t]*", re.IGNORECASE)


def clean_text(text: str | None) -> str:
    """Hide scrape noise in displayed text only (stored data is untouched)."""
    cleaned = NOISE.sub(" ", text or "")
    return re.sub(r"[ \t]+\r?\n", "\n", cleaned).strip()


@dataclass(slots=True)
class TurnOutcome:
    """Everything the UI needs from one conversational turn."""

    answer: str
    plan: QueryPlan
    result: ToolResult
    state: SessionState
    verification: GroundingVerification
    timings_ms: dict[str, float] = field(default_factory=dict)


class DetailedChatSession(ChatSession):
    """ChatSession whose turn() also returns plan, tool result, verification and timings."""

    def turn_detailed(self, message: str) -> TurnOutcome:
        t0 = time.perf_counter()
        previous_include = self.state.include_ingredients
        plan = self.parser.parse(message, self.state)
        t1 = time.perf_counter()
        merged = self.state.merge(plan)
        result = self.router.route(plan, merged)
        t2 = time.perf_counter()
        # Analytics include terms belong to that report, not to later unrelated questions.
        if plan.intent == "analytics" and result.kind == "analytics":
            merged = replace(merged, include_ingredients=previous_include)
        merged = self._remember(result, merged)
        self.state = merged
        answer = clean_text(self.composer.compose(result, self.state))
        verification = self.verifier.verify(answer, result)
        if not verification.is_grounded:
            answer += f"\n\n[Warning: Grounding check failed: {verification.details}]"
        t3 = time.perf_counter()
        return TurnOutcome(
            answer=answer,
            plan=plan,
            result=result,
            state=self.state,
            verification=verification,
            timings_ms={
                "parse": round((t1 - t0) * 1000, 1),
                "tools": round((t2 - t1) * 1000, 1),
                "compose_verify": round((t3 - t2) * 1000, 1),
            },
        )

    def _remember(self, result: ToolResult, state: SessionState) -> SessionState:
        if result.kind == "search" and isinstance(result.data, list):
            return state.with_results(
                [r.recipe_id for r in result.data], {r.recipe_id: r.title for r in result.data}
            )
        if result.kind == "match" and result.report:
            rows = result.report.results
            return state.with_results(
                [m.recipe_id for m in rows], {m.recipe_id: m.title for m in rows}
            )
        if result.kind == "substitution" and result.report:
            return state.with_focused_recipe(result.report.report.target_recipe_id)
        return state

    def remove_constraint(self, kind: str, value: str | None = None) -> None:
        """Drop one active constraint (UI chip ✕). Hard constraints never drop silently."""
        s = self.state
        key = (value or "").casefold()
        keep = lambda items: tuple(x for x in items if x.casefold() != key)
        if kind == "exclude":
            s = replace(s, exclude_ingredients=keep(s.exclude_ingredients))
        elif kind == "group":
            s = replace(s, excluded_groups=keep(s.excluded_groups))
        elif kind == "include":
            s = replace(s, include_ingredients=keep(s.include_ingredients))
        elif kind == "max_steps":
            s = replace(s, max_steps=None)
        elif kind == "pantry":
            s = replace(s, pantry=tuple(p for p in s.pantry if p.name.casefold() != key))
        elif kind == "query":
            s = replace(s, query_text="")
        else:
            raise ValueError(f"unknown constraint kind {kind!r}")
        mc = Constraints(max_steps=s.max_steps, step_metric=s.step_metric)
        if s.exclude_ingredients:
            mc = mc.with_excluded(*s.exclude_ingredients)
        if s.excluded_groups:
            mc = mc.with_excluded_groups(*s.excluded_groups)
        self.state = replace(s, matcher_constraints=mc)

    def rerun(self) -> TurnOutcome | None:
        """Re-execute the active search/match under the current constraints."""
        s = self.state
        if s.active_mode == "match" and s.pantry:
            plan = QueryPlan(intent="match", raw_message="(constraints changed)")
        elif s.query_text:
            plan = QueryPlan(
                intent="search", query_text=s.query_text, raw_message="(constraints changed)"
            )
        else:
            return None
        t0 = time.perf_counter()
        result = self.router.route(plan, s)
        self.state = self._remember(result, s)
        answer = clean_text(self.composer.compose(result, self.state))
        verification = self.verifier.verify(answer, result)
        return TurnOutcome(
            answer=answer,
            plan=plan,
            result=result,
            state=self.state,
            verification=verification,
            timings_ms={"tools": round((time.perf_counter() - t0) * 1000, 1)},
        )
