"""Try the Task 2 matcher without any LLM.

Examples:
  python scripts/cli_match.py --have eggs onions tomatoes rice --exclude peanut --max-steps 6 \\
      --prefer-fewer-missing --top 5
  python scripts/cli_match.py --have eggs onions tomatoes rice --exclude peanut --exclude eggs --max-steps 6
  python scripts/cli_match.py --have "eggs:4" "olive oil:0.25:cup" --exclude-group dairy --json
Pantry item syntax: name[:qty[:unit]]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from recipelens.services.matcher import (
    Constraints,
    Matcher,
    MatchReport,
    PantryItem,
    Preferences,
)
from recipelens.store.repository import RecipeRepository


def parse_item(text: str) -> PantryItem:
    name, _, rest = text.partition(":")
    qty_text, _, unit = rest.partition(":")
    return PantryItem(name.strip(), float(qty_text) if qty_text else None, unit.strip() or None)


def render(report: MatchReport) -> str:
    out = [f"status: {report.status}   (candidates: {report.candidates_total}, scored: {report.candidates_scored})"]
    out.append("pantry: " + ", ".join(f"{p.input_name}->{p.canonical} [{p.match_mode}]" for p in report.pantry))
    for title, rows in (("RESULTS", report.results), ("VIOLATING ALTERNATIVES (not eligible!)", report.violating_alternatives)):
        if not rows:
            continue
        out.append(f"\n== {title} ==")
        for r in rows:
            out.append(f"#{r.rank} {r.recipe_id}  {r.title}  score={r.score:.3f}  steps={r.step_count}")
            out.append(f"   matched: {', '.join(m.pantry_name for m in r.matched) or '-'}")
            out.append(f"   missing: {'; '.join(r.missing) or '-'}")
            if r.assumed_staples:
                out.append(f"   assumed staples: {'; '.join(r.assumed_staples)}")
            for v in r.violations:
                out.append(f"   VIOLATES [{v.kind}]: {v.detail} {list(v.lines)}")
            out.append(f"   why: {r.why}")
    out.append("\nnotes:")
    out.extend(f"  - {n}" for n in report.notes)
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--have", nargs="+", required=True)
    parser.add_argument("--exclude", action="append", default=[], help="excluded ingredient (repeatable)")
    parser.add_argument("--exclude-group", action="append", default=[], help="taxonomy group, e.g. dairy")
    parser.add_argument("--max-steps", type=int)
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--prefer-fewer-missing", action="store_true")
    parser.add_argument("--prefer-fewer-steps", action="store_true")
    parser.add_argument("--no-staples", action="store_true", help="do not assume salt/pepper/water/oil")
    parser.add_argument("--db", type=Path, default=None)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    repository = RecipeRepository(args.db) if args.db else RecipeRepository()
    report = Matcher(repository).match(
        [parse_item(x) for x in args.have],
        Constraints(
            exclude_ingredients=tuple(args.exclude),
            excluded_groups=tuple(args.exclude_group),
            max_steps=args.max_steps,
        ),
        Preferences(
            prefer_fewer_missing=args.prefer_fewer_missing,
            prefer_fewer_steps=args.prefer_fewer_steps,
            assume_staples=False if args.no_staples else None,
        ),
        top_k=args.top,
    )
    print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False) if args.json else render(report))


if __name__ == "__main__":
    main()
