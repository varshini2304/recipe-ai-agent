"""Chat orchestrator engine coordinating intent parsing, state, routing, and verification."""

from __future__ import annotations

from pathlib import Path

from recipelens.orchestrator.composer import TemplateComposer
from recipelens.orchestrator.intent import IntentParser, RuleBasedIntentParser
from recipelens.orchestrator.router import Router, ToolResult
from recipelens.orchestrator.schemas import QueryPlan
from recipelens.orchestrator.state import SessionState
from recipelens.orchestrator.verifier import GroundingVerification, GroundingVerifier
from recipelens.services.analytics import AnalyticsService
from recipelens.services.matcher import Matcher
from recipelens.services.search import HybridSearch, build_search
from recipelens.services.taxonomy import IngredientTaxonomy
from recipelens.store.repository import RecipeRepository

ROOT = Path(__file__).resolve().parents[2]


class ChatSession:
    """Manages multi-turn conversation flow, constraint delta merging, and grounded answers."""

    def __init__(
        self,
        repository: RecipeRepository,
        search_service: HybridSearch,
        analytics_service: AnalyticsService,
        matcher_service: Matcher,
        parser: IntentParser | None = None,
        router: Router | None = None,
        composer: TemplateComposer | None = None,
        verifier: GroundingVerifier | None = None,
    ) -> None:
        self.repository = repository
        self.search_service = search_service
        self.analytics_service = analytics_service
        self.matcher_service = matcher_service
        self.parser = parser or RuleBasedIntentParser()
        self.router = router or Router(
            repository=repository,
            search_service=search_service,
            analytics_service=analytics_service,
            matcher_service=matcher_service,
        )
        self.composer = composer or TemplateComposer()
        self.verifier = verifier or GroundingVerifier()
        self.state = SessionState.reset()
        # Kept for evaluation and debugging; callers can inspect the structured tool output
        # without trying to reconstruct it from rendered prose.
        self.last_plan: QueryPlan | None = None
        self.last_result: ToolResult | None = None
        self.last_verification: GroundingVerification | None = None

    @classmethod
    def build(cls, db_path: Path | None = None) -> ChatSession:
        """Factory initializing all required services against the local repository."""
        repo = RecipeRepository(db_path=db_path) if db_path else RecipeRepository()
        taxonomy = IngredientTaxonomy(repository=repo)
        search = build_search(repository=repo)
        analytics = AnalyticsService(repository=repo, taxonomy=taxonomy)
        matcher = Matcher(repository=repo, taxonomy=taxonomy)
        return cls(
            repository=repo,
            search_service=search,
            analytics_service=analytics,
            matcher_service=matcher,
        )

    def state_summary(self) -> str:
        """One-line summary of active constraints and query."""
        chips = self.state.constraint_chips()
        if not chips:
            return "state: [none]"
        return f"state: [{' | '.join(chips)}]"

    def turn(self, message: str) -> str:
        """Execute a single conversational turn."""
        plan: QueryPlan = self.parser.parse(message, self.state)
        self.last_plan = plan
        merged_state: SessionState = self.state.merge(plan)

        result: ToolResult = self.router.route(plan, merged_state)
        self.last_result = result

        # Update last result IDs in state if search or match returned candidates
        if result.kind == "search" and isinstance(result.data, list):
            result_ids = [r.recipe_id for r in result.data]
            titles = {r.recipe_id: r.title for r in result.data}
            merged_state = merged_state.with_results(result_ids, titles)
        elif result.kind == "match" and result.report:
            result_ids = [m.recipe_id for m in result.report.results]
            titles = {m.recipe_id: m.title for m in result.report.results}
            merged_state = merged_state.with_results(result_ids, titles)
        elif result.kind == "substitution" and result.report:
            merged_state = merged_state.with_focused_recipe(result.report.report.target_recipe_id)

        self.state = merged_state
        answer: str = self.composer.compose(result, self.state)

        # Grounding check
        verification: GroundingVerification = self.verifier.verify(answer, result)
        self.last_verification = verification
        if not verification.is_grounded:
            answer += f"\n\n[Warning: Grounding check failed: {verification.details}]"

        return answer
