"""Deterministic template renderer for tool results (no LLM)."""

from __future__ import annotations

import json
from typing import Any

from recipelens.orchestrator.router import ToolResult
from recipelens.orchestrator.state import SessionState
from recipelens.services.analytics import AnalysisReport
from recipelens.services.matcher import MatchReport, RecipeMatch
from recipelens.store.models import RecipeRecord, SearchResult


class TemplateComposer:
    """Renders structured ToolResults into user-facing conversational responses."""

    def compose(self, result: ToolResult, state: SessionState) -> str:
        """Compose a user-facing response from ToolResult and current SessionState."""
        if result.kind == "reset":
            return "Session state has been reset. All previous searches, pantry items, and constraints have been cleared."

        if result.kind == "unsupported":
            reason = result.unsupported_reason or "The requested operation is not supported by the dataset."
            return f"Unsupported request: {reason}"

        if result.kind == "clarification":
            return result.clarification_question or "Could you please clarify your request?"

        if result.kind == "chitchat":
            return (
                "Hello! I am RecipeLens, your conversational recipe assistant.\n\n"
                "Here is what I can help you with:\n"
                "• **Search**: Find recipes by name or keywords (e.g. 'penne pasta', 'lemon chicken').\n"
                "• **Multi-turn Refinements**: Add constraints across turns (e.g. 'I cannot have dairy', 'actually make it gluten-free too', 'at most 6 steps').\n"
                "• **Pantry Matching**: Tell me what you have on hand (e.g. 'I have eggs, onions, tomatoes, rice, no peanuts, at most 6 steps').\n"
                "• **Recipe Analytics**: Compute exact dataset statistics (e.g. 'How many recipes have garlic AND onion?', 'Show me tomato recipes with fewest steps').\n"
                "• **Recipe Details**: Ask about any search or match result (e.g. 'tell me about the 1st one')."
            )

        if result.kind == "recipe_detail":
            return self._compose_recipe_detail(result.data)

        if result.kind == "search":
            return self._compose_search(result.data, state)

        if result.kind == "match":
            return self._compose_match(result.report, state)

        if result.kind == "analytics":
            return self._compose_analytics(result.report, state)

        if result.kind == "error":
            warnings = " ".join(result.warnings) if result.warnings else "An unknown error occurred."
            return f"Error: {warnings}"

        return "Response generated successfully."

    def _compose_search(self, results: list[SearchResult], state: SessionState) -> str:
        if not results:
            constraints_desc = ", ".join(state.constraint_chips())
            return (
                f"No recipes found matching \"{state.query_text}\""
                + (f" with active constraints ({constraints_desc})" if constraints_desc else "")
                + ". Try relaxing a filter or searching for a broader term."
            )

        lines: list[str] = []
        active_chips = state.constraint_chips()
        chip_str = f" [Filters: {', '.join(active_chips)}]" if active_chips else ""
        lines.append(f"Found {len(results)} recipes for \"{state.query_text}\"{chip_str}:\n")

        for idx, r in enumerate(results, 1):
            lines.append(f"{idx}. **{r.title}** [ID: {r.recipe_id}]")
            if r.matched_terms:
                lines.append(f"   Matched terms: {', '.join(r.matched_terms)}")

        if state.excluded_groups:
            lines.append(
                f"\n*Note: All results strictly exclude taxonomy groups: {', '.join(state.excluded_groups)}.*"
            )
        lines.append("\nYou can view instructions for any recipe (e.g. 'tell me about the 1st one') or refine constraints (e.g. 'exclude eggs too').")
        return "\n".join(lines)

    def _compose_match(self, report: MatchReport | None, state: SessionState) -> str:
        if not report:
            return "No matching report available."

        lines: list[str] = []

        if report.status == "ok":
            lines.append(f"Found {len(report.results)} recipe(s) matching your pantry items:\n")
            for m in report.results:
                matched_names = [item.pantry_name for item in m.matched]
                lines.append(f"{m.rank}. **{m.title}** [ID: {m.recipe_id}] (Score: {m.score:.2f})")
                lines.append(f"   • Matched pantry: {', '.join(matched_names) if matched_names else 'none'}")
                lines.append(f"   • Missing to buy: {', '.join(m.missing) if m.missing else 'None (complete pantry match!)'}")
                if m.assumed_staples:
                    lines.append(f"   • Assumed staples: {', '.join(m.assumed_staples)}")
                lines.append(f"   • Steps: {m.step_count} ({m.step_metric})")
                lines.append(f"   • Why: {m.why}")
                lines.append("")
        else:
            lines.append("No recipe satisfies every hard constraint. Your constraints were NOT relaxed silently.\n")
            if report.violating_alternatives:
                lines.append("The closest violating alternatives (breaking at least one constraint) are:\n")
                for m in report.violating_alternatives:
                    violation_descs = [f"{v.kind}: {v.detail}" for v in m.violations]
                    matched_names = [item.pantry_name for item in m.matched]
                    lines.append(f"{m.rank}. **[VIOLATING] {m.title}** [ID: {m.recipe_id}]")
                    lines.append(f"   • Violations: {'; '.join(violation_descs)}")
                    lines.append(f"   • Matched pantry: {', '.join(matched_names) if matched_names else 'none'}")
                    lines.append(f"   • Missing to buy: {', '.join(m.missing) if m.missing else 'none'}")
                    lines.append(f"   • Steps: {m.step_count}")
                    lines.append("")

        if report.notes:
            lines.append("Notes:")
            for note in report.notes:
                lines.append(f"• {note}")

        return "\n".join(lines).strip()

    def _compose_analytics(self, report: AnalysisReport | None, state: SessionState) -> str:
        if not report:
            return "No analysis report available."

        lines: list[str] = []
        lines.append("### RecipeLens Analytics Report\n")
        lines.append(f"• **Recipes analyzed:** {report.n_analyzed:,}")
        lines.append(f"• **Primary denominator:** {report.denominator_label}")
        if report.secondary_denominator_label:
            lines.append(f"• **Secondary denominator:** {report.secondary_denominator_label}")
        lines.append(f"• **Formula:** `{report.formula}`")
        lines.append(f"• **Normalization notes:** {report.normalization_notes}\n")

        # Format rows based on structure
        if not report.rows:
            lines.append("No records matched the analytical criteria.")
            return "\n".join(lines)

        first_row = report.rows[0]
        if "count" in first_row and "percentage" in first_row and "canonical" not in first_row:
            # count_with single row
            cnt = first_row["count"]
            pct = first_row["percentage"]
            pct_all = first_row.get("percentage_all_recipes", 0.0)
            lines.append(
                f"**Result:** **{cnt:,}** recipes match ({pct:.2f}% of usable-ingredient recipes; {pct_all:.2f}% of total dataset)."
            )
        elif "canonical" in first_row:
            # common_ingredients
            lines.append("**Top ingredients:**\n")
            for idx, r in enumerate(report.rows, 1):
                lines.append(f"{idx}. `{r['canonical']}`: {r['count']:,} recipes ({r['percentage']:.2f}%)")
        elif "mean" in first_row and "median" in first_row:
            # ingredient_count_stats
            m_val = first_row["mean"]
            med_val = first_row["median"]
            min_val = first_row["min"]
            max_val = first_row["max"]
            lines.append(f"• **Mean ingredient count:** {m_val:.2f}" if m_val is not None else "• Mean: N/A")
            lines.append(f"• **Median ingredient count:** {med_val:.1f}" if med_val is not None else "• Median: N/A")
            lines.append(f"• **Range:** {min_val} to {max_val}" if min_val is not None else "• Range: N/A")
        elif "step_count" in first_row or "metric_value" in first_row:
            # rank_by_steps
            lines.append(f"**Ranked recipes by {report.metric}:**\n")
            for idx, r in enumerate(report.rows, 1):
                lines.append(
                    f"{idx}. **{r['title']}** [ID: {r['recipe_id']}] — {report.metric}: {r['metric_value']}, ingredients: {r['ingredient_count']}"
                )
            if report.cutoff_tie_count and report.cutoff_tie_count > 1:
                lines.append(f"\n*(Cutoff ties: {report.cutoff_tie_count} recipes tied at step count)*")

        return "\n".join(lines)

    def _compose_recipe_detail(self, recipe: RecipeRecord | None) -> str:
        if not recipe:
            return "Recipe record not found."

        lines: list[str] = []
        lines.append(f"## {recipe.title}")
        lines.append(f"**Recipe ID:** `{recipe.recipe_id}` (Source: {recipe.source})\n")
        lines.append(f"• **Step count:** {recipe.step_count} (sentence count: {recipe.sentence_count})")
        lines.append(f"• **Ingredient count:** {recipe.ingredient_count}\n")

        lines.append("### Ingredients:")
        if recipe.ingredients_raw:
            try:
                raw_items = json.loads(recipe.ingredients_raw)
                for item in raw_items:
                    lines.append(f"• {item}")
            except (json.JSONDecodeError, TypeError):
                lines.append(recipe.ingredients_raw)
        else:
            lines.append("No ingredients listed.")

        lines.append("\n### Instructions:")
        if recipe.instructions_raw:
            lines.append(recipe.instructions_raw)
        else:
            lines.append("No instructions provided.")

        return "\n".join(lines)
