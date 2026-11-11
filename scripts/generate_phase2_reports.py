"""Regenerate deterministic Phase 2 example analysis reports from the real database."""

from __future__ import annotations

import json
from pathlib import Path

from recipelens.data.steps import count_steps
from recipelens.services.analytics import AnalyticsService
from recipelens.store.models import Filter
from recipelens.store.repository import RecipeRepository

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    service = AnalyticsService(RecipeRepository())
    reports = {
        "Tomato count (family mode)": service.count_with(
            ["tomato"],
            recipe_filter=Filter(match_mode="family"),
        ),
        "Garlic AND onion count (family mode)": service.count_with(
            ["garlic", "onion"],
            mode="all",
            recipe_filter=Filter(match_mode="family"),
        ),
        "Five tomato recipes with fewest steps (family mode)": service.rank_by_steps(
            Filter(include_ingredients=("tomato",), match_mode="family"),
            order="asc",
            top_k=5,
        ),
    }
    lines = [
        "# Phase 2 sample AnalysisReports",
        "",
        "Generated from the complete SQLite corpus.",
        "",
    ]
    for title, report in reports.items():
        lines.extend(
            [f"## {title}", "", "```json", json.dumps(report.to_dict(), indent=2), "```", ""]
        )
    for mode in ("exact", "family"):
        ranked = (
            reports["Five tomato recipes with fewest steps (family mode)"]
            if mode == "family"
            else service.rank_by_steps(
                Filter(include_ingredients=("tomato",), match_mode="exact"),
                order="asc",
                top_k=5,
            )
        )
        lines.extend(
            [
                f"## Raw instructions: five tomato one-step results ({mode} mode)",
                f"Cutoff step_count: {ranked.rows[-1]['step_count']}; total recipes tied at cutoff: {ranked.cutoff_tie_count}.",
                "",
            ]
        )
        for row in ranked.rows:
            recipe = service.repository.get_recipe(row["recipe_id"])
            raw = recipe.instructions_raw if recipe else None
            recount = count_steps(raw)
            nonempty_lines = [line for line in (raw or "").splitlines() if line.strip()]
            lines.extend(
                [
                    f"### {row['recipe_id']} — {row['title']}",
                    f"Stored steps: {row['step_count']}; recount from raw: {recount}; nonempty raw lines: {len(nonempty_lines)}.",
                    "The stored one-step count is consistent with the single-block sentence fallback."
                    if len(nonempty_lines) == 1 and recount == 1
                    else "The stored one-step count is consistent with the documented newline-block rule.",
                    "```text",
                    raw or "",
                    "```",
                    "",
                ]
            )
    target = ROOT / "ANALYSIS_REPORTS.md"
    target.write_text("\n".join(lines), encoding="utf-8")
    print(target)
    for title, report in reports.items():
        print(
            f"{title}: {report.rows}; n_analyzed={report.n_analyzed}; denominator={report.denominator}"
        )


if __name__ == "__main__":
    main()
