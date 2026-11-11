"""Try recipe search services directly without an LLM."""

from __future__ import annotations

import argparse
import json
import sys

from recipelens.services.search import build_search
from recipelens.store.models import Filter


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Free-text recipe search")
    parser.add_argument(
        "--no-dairy", action="store_true", help="Apply the approved dairy exclusion group"
    )
    parser.add_argument(
        "--exclude", action="append", default=[], help="Exclude an exact canonical ingredient"
    )
    parser.add_argument("--min-steps", type=int)
    parser.add_argument("--max-steps", type=int)
    parser.add_argument(
        "--match-mode",
        choices=("family", "exact"),
        default="family",
        help="Ingredient containment matching mode (default: family)",
    )
    parser.add_argument(
        "--step-metric",
        choices=("step_count", "sentence_count"),
        default="step_count",
        help="Metric used by min/max step filters",
    )
    parser.add_argument("--top-k", type=int, default=10)
    args = parser.parse_args()
    groups = ("dairy",) if args.no_dairy else ()
    recipe_filter = Filter(
        exclude_ingredients=tuple(args.exclude),
        excluded_taxonomy_groups=groups,
        min_steps=args.min_steps,
        max_steps=args.max_steps,
        match_mode=args.match_mode,
        step_metric=args.step_metric,
    )
    search = build_search()
    indexed, full = search.index_coverage
    print(
        f"Vector coverage: {indexed:,} / {full:,}; SQLite FTS covers all eligible recipes.",
        file=sys.stderr,
    )
    results = search.search(args.query, recipe_filter, top_k=args.top_k)
    for result in results:
        print(
            json.dumps(
                {
                    "recipe_id": result.recipe_id,
                    "title": result.title,
                    "score": result.score,
                    "score_breakdown": result.score_breakdown,
                    "matched_terms": result.matched_terms,
                    "ingredients_raw": result.ingredients_raw,
                    "instructions_raw": result.instructions_raw,
                },
                ensure_ascii=False,
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
