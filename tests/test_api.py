"""API tests on the synthetic fixture DB (no embeddings model required)."""

from __future__ import annotations

import re
import sys
import types
from pathlib import Path

import pytest

if "sentence_transformers" not in sys.modules:  # keep tests runnable without the model package
    try:
        import sentence_transformers  # noqa: F401
    except ImportError:
        stub = types.ModuleType("sentence_transformers")
        stub.SentenceTransformer = object  # type: ignore[attr-defined]
        sys.modules["sentence_transformers"] = stub

from fastapi.testclient import TestClient

from recipelens.api.app import create_app
from recipelens.api.session import DetailedChatSession, clean_text
from recipelens.services.analytics import AnalyticsService
from recipelens.services.matcher import Matcher
from recipelens.services.taxonomy import IngredientTaxonomy
from recipelens.store.models import SearchResult
from recipelens.store.repository import RecipeRepository
from tests.matcher_fixture import build_fixture_db


class TitleSearch:
    """Deterministic stand-in for hybrid search: title-word match over the fixture DB."""

    index_coverage = (0, 0)

    def __init__(self, repo: RecipeRepository) -> None:
        self.repo = repo

    def search(self, query, recipe_filter=None, top_k=None):
        words = [w for w in query.casefold().split() if w]
        ids = self.repo.filter_ids(recipe_filter) if recipe_filter else []
        recs = self.repo.recipes_for_ids(ids)
        hits = [r for r in recs.values() if any(w in (r.title or "").casefold() for w in words)]
        return [
            SearchResult(r.recipe_id, r.title or "", 1.0, {"bm25": 1.0, "vector": 0.0, "rrf": 1.0},
                         tuple(words), None, None)
            for r in sorted(hits, key=lambda r: r.recipe_id)[: top_k or 10]
        ]  # fmt: skip


@pytest.fixture()
def client(tmp_path: Path) -> TestClient:
    db = build_fixture_db(tmp_path / "fx.db")
    repo = RecipeRepository(db_path=db)
    tax = IngredientTaxonomy(repository=repo)

    def factory() -> DetailedChatSession:
        return DetailedChatSession(
            repo, TitleSearch(repo), AnalyticsService(repo, tax), Matcher(repo, tax)
        )

    return TestClient(create_app(session_factory=factory))


def test_health_and_index(client: TestClient) -> None:
    assert client.get("/api/health").json() == {"status": "ok"}
    assert client.get("/").status_code == 200


def test_chat_match_then_exclude_chip(client: TestClient) -> None:
    r = client.post(
        "/api/chat",
        json={"message": "I have eggs, onions, tomatoes, rice, no peanuts, at most 6 steps"},
    ).json()
    sid = r["session_id"]
    assert r["payload"]["kind"] == "match"
    assert r["verification"]["grounded"] is True
    kinds = {c["kind"] for c in r["state"]["chip_items"]}
    assert {"pantry", "group", "max_steps"} <= kinds
    r2 = client.post("/api/chat", json={"session_id": sid, "message": "exclude eggs too"}).json()
    assert "eggs" in r2["state"]["excluded_groups"]
    for m in r2["payload"]["results"]:
        assert all(i["pantry_name"] != "egg" for i in m["matched"])
        assert not any(re.search(r"\beggs?\b", x.casefold()) for x in m["missing"])


def test_chip_remove_reruns(client: TestClient) -> None:
    r = client.post("/api/chat", json={"message": "I have eggs, onions, no peanuts"}).json()
    sid = r["session_id"]
    r2 = client.post(
        "/api/chip/remove", json={"session_id": sid, "kind": "group", "value": "peanuts"}
    ).json()
    assert all(c["kind"] != "group" for c in r2["state"]["chip_items"])
    assert r2["payload"]["kind"] == "match"


def test_chip_remove_bad_kind(client: TestClient) -> None:
    sid = client.post("/api/chat", json={"message": "hello"}).json()["session_id"]
    assert (
        client.post("/api/chip/remove", json={"session_id": sid, "kind": "nope"}).status_code == 400
    )


def test_unsupported_is_refused(client: TestClient) -> None:
    r = client.post("/api/chat", json={"message": "how many calories in pasta"}).json()
    assert r["payload"]["kind"] == "unsupported"


def test_analytics_include_terms_do_not_leak_to_followup(client: TestClient) -> None:
    first = client.post(
        "/api/chat", json={"message": "How many recipes have garlic AND onion?"}
    ).json()
    sid = first["session_id"]
    assert first["state"]["include_ingredients"] == []

    followup = client.post(
        "/api/chat",
        json={"session_id": sid, "message": "What are the most common ingredients?"},
    ).json()
    report = followup["payload"]
    assert report["kind"] == "analytics"
    assert report["n_analyzed"] == report["denominator"]
    assert followup["state"]["include_ingredients"] == []


def test_reset_clears_state(client: TestClient) -> None:
    sid = client.post("/api/chat", json={"message": "I have eggs"}).json()["session_id"]
    st = client.post("/api/reset", json={"session_id": sid}).json()["state"]
    assert st["chip_items"] == []


def test_recipe_404_and_stats(client: TestClient) -> None:
    assert client.get("/api/recipe", params={"id": "nope:1"}).status_code == 404
    assert client.get("/api/stats").json()["counts"]["all_recipes"] > 0
    assert client.post("/api/chat", json={"message": "  "}).status_code == 400


def test_clean_text_strips_noise() -> None:
    assert clean_text("2 cloves garlic ADVERTISEMENT") == "2 cloves garlic"
    assert clean_text("first ADVERTISEMENT\n  second") == "first\n  second"
