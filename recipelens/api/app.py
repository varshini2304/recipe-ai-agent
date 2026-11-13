"""FastAPI application: chat, constraint chips, recipe lookup, dataset stats."""

from __future__ import annotations

import uuid
from collections.abc import AsyncIterator, Callable
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from recipelens.api.serialize import recipe_to_dict, serialize_result, serialize_state
from recipelens.api.session import DetailedChatSession, TurnOutcome

ROOT = Path(__file__).resolve().parents[2]
WEB_DIR = ROOT / "web"


class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None


class SessionRequest(BaseModel):
    session_id: str


class ChipRequest(BaseModel):
    session_id: str
    kind: str
    value: str | None = None


def _outcome_json(sid: str, out: TurnOutcome) -> dict[str, Any]:
    v = out.verification
    return {
        "session_id": sid,
        "answer": out.answer,
        "intent": out.plan.intent,
        "payload": serialize_result(out.result),
        "state": serialize_state(out.state),
        "verification": {
            "grounded": v.is_grounded,
            "ungrounded_ids": list(v.ungrounded_ids),
            "ungrounded_numbers": list(v.ungrounded_numbers),
        },
        "trace": {
            "intent": out.plan.intent,
            "analytics_type": out.plan.analytics_type,
            "timings_ms": out.timings_ms,
            "tool_kind": out.result.kind,
        },
    }


def create_app(
    session_factory: Callable[[], DetailedChatSession] | None = None,
    stats_provider: Callable[[DetailedChatSession], dict[str, Any]] | None = None,
) -> FastAPI:
    """Build the app. Services are injectable so tests can use a fixture DB."""
    sessions: dict[str, DetailedChatSession] = {}
    shared: dict[str, DetailedChatSession] = {}

    def make() -> DetailedChatSession:
        if session_factory is not None:
            return session_factory()
        if "base" not in shared:
            shared["base"] = _default_session()
        b = shared["base"]
        return DetailedChatSession(
            b.repository, b.search_service, b.analytics_service, b.matcher_service
        )

    def get(sid: str | None) -> tuple[str, DetailedChatSession]:
        if sid and sid in sessions:
            return sid, sessions[sid]
        new_id = sid or uuid.uuid4().hex[:12]
        sessions[new_id] = make()
        return new_id, sessions[new_id]

    def warm_default_session() -> None:
        """Load the local model and repository before accepting the first chat request."""
        if session_factory is None:
            make()

    @asynccontextmanager
    async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
        warm_default_session()
        yield

    app = FastAPI(title="RecipeLens", version="1.0", lifespan=lifespan)

    @app.post("/api/chat")
    def chat(req: ChatRequest) -> dict[str, Any]:
        if not req.message.strip():
            raise HTTPException(400, "Empty message")
        sid, s = get(req.session_id)
        return _outcome_json(sid, s.turn_detailed(req.message.strip()))

    @app.post("/api/reset")
    def reset(req: SessionRequest) -> dict[str, Any]:
        sessions.pop(req.session_id, None)
        sid, s = get(req.session_id)
        return {"session_id": sid, "state": serialize_state(s.state)}

    @app.get("/api/state")
    def state(session_id: str) -> dict[str, Any]:
        sid, s = get(session_id)
        return {"session_id": sid, "state": serialize_state(s.state)}

    @app.post("/api/chip/remove")
    def chip_remove(req: ChipRequest) -> dict[str, Any]:
        sid, s = get(req.session_id)
        try:
            s.remove_constraint(req.kind, req.value)
        except ValueError as exc:
            raise HTTPException(400, str(exc)) from exc
        out = s.rerun()
        if out is None:
            return {
                "session_id": sid,
                "answer": None,
                "payload": None,
                "state": serialize_state(s.state),
            }
        return _outcome_json(sid, out)

    @app.get("/api/recipe")
    def recipe(id: str, session_id: str | None = None) -> dict[str, Any]:
        _, s = get(session_id)
        rec = s.repository.get_recipe(id)
        if rec is None:
            raise HTTPException(404, f"Recipe {id!r} not found")
        return recipe_to_dict(rec)

    @app.get("/api/stats")
    def stats() -> dict[str, Any]:
        _, s = get(None)
        if stats_provider:
            return stats_provider(s)
        return default_stats(s)

    @app.get("/api/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    if WEB_DIR.exists():
        app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")

        @app.get("/")
        def index() -> FileResponse:
            return FileResponse(WEB_DIR / "index.html")

    return app


def _default_session() -> DetailedChatSession:
    from recipelens.orchestrator.chat import ChatSession

    base = ChatSession.build()
    return DetailedChatSession(
        base.repository, base.search_service, base.analytics_service, base.matcher_service
    )


def default_stats(s: DetailedChatSession) -> dict[str, Any]:
    """Real corpus numbers straight from the repository (nothing hardcoded)."""
    counts = s.repository.counts()
    top = [{"canonical": name, "count": n} for name, n in s.repository.canonical_counts(limit=40)]
    out: dict[str, Any] = {"counts": counts, "top_ingredients": top[:12]}
    cov = getattr(s.search_service, "index_coverage", None)
    if cov:
        out["index_coverage"] = {"indexed": cov[0], "searchable": cov[1]}
    return out


app_factory = create_app
