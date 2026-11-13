"""Run machine-checkable cases against the real local Recipe Box chat pipeline."""

from __future__ import annotations

import json
import re
import sqlite3
import sys
import time
from collections import Counter
from functools import cache
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from recipelens.data.ingredients import parse_ingredient
from recipelens.orchestrator.chat import ChatSession
from recipelens.orchestrator.state import SessionState
from recipelens.services.analytics import AnalysisReport
from recipelens.services.matcher import MatchReport
from recipelens.services.substitution import SubstitutionPlan

DB_PATH = ROOT / "data" / "recipelens.sqlite3"


@cache
def _config(name: str) -> dict[str, Any]:
    return yaml.safe_load((ROOT / "config" / name).read_text(encoding="utf-8")) or {}


def _raw_frames() -> tuple[pd.DataFrame, pd.DataFrame]:
    with sqlite3.connect(DB_PATH) as connection:
        recipes = pd.read_sql_query(
            "SELECT recipe_id, title, instructions_raw, ingredient_count, has_ingredients "
            "FROM recipes", connection
        )
        ingredients = pd.read_sql_query(
            "SELECT recipe_id, position, raw FROM ingredient_lines ORDER BY recipe_id, position",
            connection,
        )
    return recipes, ingredients


def _head(raw: str) -> str:
    return raw.split(",", 1)[0].strip().casefold()


def _family_match(raw: str, family: str) -> bool:
    """Independent raw-line family matcher; does not read ingredient_lines.canonical."""
    rule = _config("families.yaml")["families"][family]
    cleaned = raw
    for pattern in _config("cleaning.yaml").get("noise_patterns", []):
        cleaned = re.sub(pattern, "", cleaned)
    head = _head(cleaned)
    if any(re.search(pattern, head, re.IGNORECASE) for pattern in rule["exclude_patterns"]):
        return False
    return any(re.search(pattern, head, re.IGNORECASE) for pattern in rule["match_patterns"])


def _taxonomy_hit(raw: str, group: str) -> bool:
    rule = _config("taxonomy.yaml")["groups"][group]
    if any(re.search(pattern, raw, re.IGNORECASE) for pattern in rule["exclude_patterns"]):
        return False
    return any(
        re.search(pattern, raw, re.IGNORECASE)
        for pattern in (*rule["match_patterns"], *rule.get("uncertain_patterns", []))
    )


def _independent_steps(text: str | None) -> int:
    """Recompute the configured newline/single-block rule from original instruction text."""
    if not text:
        return 0
    cfg = _config("steps.yaml")
    boilerplate = [re.compile(p, re.IGNORECASE) for p in cfg["boilerplate_patterns"]]
    blocks = [part.strip() for part in text.splitlines() if part.strip()]
    blocks = [part for part in blocks if not any(p.fullmatch(part) for p in boilerplate)]
    if len(blocks) == 1:
        return len(re.split(cfg["sentence_boundary_pattern"], blocks[0]))
    return len(blocks)


def _ground_truth(recipes: pd.DataFrame, recipe_lines: pd.DataFrame) -> dict[str, Any]:
    all_count = int(recipes.recipe_id.nunique())
    usable_count = int(recipes.has_ingredients.sum())
    recipe_lines = recipe_lines.dropna(subset=["raw"]).copy()
    family_sets = {
        key: set(recipe_lines.loc[
            recipe_lines.raw.map(lambda raw, family=key: _family_match(raw, family)), "recipe_id"
        ])
        for key in ("garlic", "onion", "tomato")
    }
    both = family_sets["garlic"] & family_sets["onion"]

    # Pandas builds an independent frequency table by parsing original source lines.
    parsed = recipe_lines.assign(
        raw_canonical=recipe_lines.raw.map(lambda line: parse_ingredient(line).canonical)
    )
    common = (
        parsed.drop_duplicates(["recipe_id", "raw_canonical"])
        .groupby("raw_canonical").recipe_id.nunique().sort_values(ascending=False)
    )

    tomato_rows = recipes.loc[recipes.recipe_id.isin(family_sets["tomato"])].copy()
    tomato_rows["independent_steps"] = tomato_rows.instructions_raw.map(_independent_steps)
    action_patterns = [
        re.compile(p, re.IGNORECASE)
        for p in _config("steps.yaml")["low_confidence"]["action_patterns"]
    ]
    low = _config("steps.yaml")["low_confidence"]
    tomato_rows["independent_low_confidence"] = tomato_rows.instructions_raw.map(
        lambda text: not text
        or len(text.strip()) < int(low["minimum_characters"])
        or sum(len(p.findall(text)) for p in action_patterns)
        < int(low["minimum_action_matches"])
    )
    eligible_tomato = tomato_rows.loc[~tomato_rows.independent_low_confidence].copy()
    eligible_tomato = eligible_tomato.sort_values(
        ["independent_steps", "ingredient_count", "recipe_id"], kind="stable"
    )
    return {
        "all": all_count,
        "usable": usable_count,
        "garlic_onion": len(both),
        "garlic_onion_percent": 100 * len(both) / usable_count,
        "tomato_top5": eligible_tomato.head(5).recipe_id.tolist(),
        "common_top1": str(common.index[0]) if len(common) else None,
    }


def _check(
    check: str,
    session: ChatSession,
    truth: dict[str, Any],
    raw: pd.DataFrame,
    answer: str,
) -> tuple[bool, str, int]:
    result = session.last_result
    if result is None:
        return False, "No structured result captured", 0
    if check == "search_excludes_dairy":
        ids = [row.recipe_id for row in (result.data or [])]
        lines = raw.loc[raw.recipe_id.isin(ids), ["recipe_id", "raw"]].dropna()
        violations = sum(_taxonomy_hit(line, "dairy") for line in lines.raw)
        return violations == 0, f"results={len(ids)}, raw dairy-line violations={violations}", violations
    if check == "raw_count_garlic_onion":
        report = result.report
        ok_type = isinstance(report, AnalysisReport)
        row = report.rows[0] if ok_type and report.rows else {}
        ok = (
            ok_type
            and row.get("count") == truth["garlic_onion"]
            and report.filters.get("match_mode") == "family"
            and report.denominator == truth["usable"]
            and report.secondary_denominator == truth["all"]
        )
        details = (
            f"raw-line pandas truth={truth['garlic_onion']}/{truth['usable']}="
            f"{truth['garlic_onion_percent']:.4f}%; report={row}; "
            f"count_delta={row.get('count', 0) - truth['garlic_onion']}; "
            f"percentage_point_delta={row.get('percentage', 0.0) - truth['garlic_onion_percent']:.4f}; "
            f"mode={report.filters.get('match_mode') if ok_type else None}; "
            f"denominator={report.denominator if ok_type else None}"
        )
        return bool(ok), details, 0
    if check == "raw_rank_tomato":
        report = result.report
        ids = [row.get("recipe_id") for row in report.rows] if isinstance(report, AnalysisReport) else []
        ok = ids == truth["tomato_top5"]
        return ok, f"independent raw-line IDs={truth['tomato_top5']}; pipeline IDs={ids}; metric={getattr(report, 'metric', None)}", 0
    if check == "common_raw_ingredients":
        report = result.report
        actual = report.rows[0].get("canonical") if isinstance(report, AnalysisReport) and report.rows else None
        ok = actual == truth["common_top1"]
        return ok, f"independent raw-line top ingredient={truth['common_top1']!r}; pipeline={actual!r}", 0
    if check == "unsupported_refusal":
        return result.kind == "unsupported", f"tool kind={result.kind}", 0
    if check == "clarification":
        return result.kind == "clarification", f"tool kind={result.kind}", 0
    if check.startswith(("match_", "quantity_status_", "no_match_")):
        report = result.report
        if not isinstance(report, MatchReport):
            return False, f"expected MatchReport, got {type(report).__name__}", 0
        ids = [item.recipe_id for item in report.results]
        lines = raw.loc[raw.recipe_id.isin(ids), ["recipe_id", "raw"]].dropna()
        violations = 0
        if check in {"match_no_peanuts_six_steps", "match_excludes_eggs"}:
            group = "peanuts" if check == "match_no_peanuts_six_steps" else None
            for line in lines.raw:
                if group and _taxonomy_hit(line, group):
                    violations += 1
                if check == "match_excludes_eggs" and re.search(r"\beggs?\b", line, re.IGNORECASE):
                    violations += 1
        if check == "match_no_peanuts_six_steps":
            ok = violations == 0 and all(item.step_count <= 6 for item in report.results)
        elif check == "match_excludes_eggs":
            ok = violations == 0
        elif check == "no_match_separate_alternatives":
            ok = report.status == "no_eligible_match" and not report.results and all(
                item.violations for item in report.violating_alternatives
            ) and bool(report.violating_alternatives) and "[VIOLATING]" in answer
            return ok, f"status={report.status}, eligible={len(report.results)}, labelled violators={len(report.violating_alternatives)}", 0
        else:
            statuses = [
                matched.quantity_check
                for recipe in (*report.results, *report.violating_alternatives)
                for matched in recipe.matched
            ]
            wanted = check.removeprefix("quantity_status_")
            ok = wanted in statuses
            return ok, f"requested={wanted}, observed status counts={dict(Counter(statuses))}", 0
        return ok, f"status={report.status}, results={len(ids)}, raw constraint violations={violations}", violations
    if check.startswith("substitution_"):
        plan = result.report
        if not isinstance(plan, SubstitutionPlan):
            return False, f"expected SubstitutionPlan, got {type(plan).__name__}", 0
        evidence = plan.report
        if check == "substitution_has_evidence":
            ok = evidence.evidence_grade in {"weak", "strong"} and evidence.n_peers > 0
        elif check == "substitution_conflicting_no_candidate":
            ok = evidence.evidence_grade == "conflicting" and not evidence.candidates
        else:
            ok = evidence.evidence_grade == "none" and not evidence.candidates
        detail = (
            f"grade={evidence.evidence_grade}, n_peers={evidence.n_peers}, "
            f"with-X={evidence.with_x_count}, without-X={evidence.without_x_count}, "
            f"thresholds={evidence.thresholds}, candidates={[c.canonical for c in evidence.candidates]}"
        )
        return ok, detail, 0
    return False, f"Unknown check {check}", 0


def _markdown(results: list[dict[str, Any]], truth: dict[str, Any], total_latency: float) -> str:
    lines = [
        "# RecipeLens evaluation",
        "",
        "Generated by `python eval/run_eval.py` against the local full database. Ground truth uses",
        "raw ingredient lines (not the canonical column), independent pandas aggregation, and",
        "configured raw-text patterns. The chatbot pipeline is deterministic; no LLM is used here.",
        "",
        f"Corpus: {truth['all']:,} all recipes; {truth['usable']:,} usable-ingredient recipes.",
        (f"Independent raw-line garlic AND onion: {truth['garlic_onion']:,} / {truth['usable']:,} "
         f"= {truth['garlic_onion_percent']:.4f}% (usable-ingredient denominator)."),
        f"Total measured chat latency: {total_latency:.2f}s.",
        "",
        "| Case | Status | Hard violations | Citation validity | Verifier | Latency | Details |",
        "|---|---|---:|---|---|---:|---|",
    ]
    for item in results:
        lines.append(
            f"| {item['id']} | {'PASS' if item['passed'] else 'FAIL'} | {item['violations']} | "
            f"{'valid' if item['citations_valid'] else 'INVALID'} | "
            f"{'grounded' if item['verifier_grounded'] else 'FLAG: ' + item['verifier_details']} | "
            f"{item['latency']:.2f}s | {item['details'].replace('|', '/')} |"
        )
    lines.extend([
        "",
        f"Hard-constraint violations across evaluated result sets: **{sum(r['violations'] for r in results)}**.",
        f"Valid cited recipe IDs: **{sum(r['citations_valid'] for r in results)}/{len(results)} cases**.",
        f"Verifier flags: **{sum(not r['verifier_grounded'] for r in results)}**.",
        "",
        "## What worked / What failed / Why",
        "",
        (ROOT / "eval" / "assessment.md").read_text(encoding="utf-8").split("## What worked / What failed / Why", 1)[-1].strip(),
        "",
        "## One-shot baseline",
        "",
    ])
    cache = ROOT / "eval" / ".cache" / "oneshot.json"
    if cache.exists():
        baseline = json.loads(cache.read_text(encoding="utf-8"))
        lines.append(f"Gemini `{baseline['model']}` with no tools answered the same question:\n\n> {baseline['answer']}")
    else:
        lines.append("No Gemini key was available; the one-shot answer is to be collected manually (see `eval/oneshot_example.md`).")
    lines.extend(["", f"Computed answer alongside the manual baseline slot: **{truth['garlic_onion']:,} / {truth['usable']:,} = {truth['garlic_onion_percent']:.4f}%** (raw-line pandas ground truth).", ""])
    return "\n".join(lines)


def main() -> int:
    if not DB_PATH.exists():
        raise SystemExit(f"Database not found at {DB_PATH}; run `make ingest` first.")
    cases = yaml.safe_load((ROOT / "eval" / "cases.yaml").read_text(encoding="utf-8"))["cases"]
    recipes, raw = _raw_frames()
    truth = _ground_truth(recipes, raw)
    session = ChatSession.build(DB_PATH)
    rows: list[dict[str, Any]] = []
    for case in cases:
        session.state = SessionState.reset()
        started = time.perf_counter()
        answers = [session.turn(message) for message in case["turns"]]
        latency = time.perf_counter() - started
        passed, details, violations = _check(
            case["check"], session, truth, raw, "\n".join(answers)
        )
        ids = set(re.findall(r"\b(?:ar|fn|epi):[^\s`\],]+", "\n".join(answers)))
        with sqlite3.connect(DB_PATH) as connection:
            valid_ids = {rid for (rid,) in connection.execute(
                "SELECT recipe_id FROM recipes WHERE recipe_id IN (" + ",".join("?" for _ in ids) + ")", tuple(ids)
            )} if ids else set()
        citations_valid = ids == valid_ids
        verification = session.last_verification
        item = {
            "id": case["id"], "passed": passed, "details": details,
            "violations": violations, "citations_valid": citations_valid,
            "verifier_grounded": bool(verification and verification.is_grounded),
            "verifier_details": verification.details if verification else "not run",
            "latency": latency,
        }
        rows.append(item)
        print(f"{'PASS' if passed else 'FAIL'} {case['id']} ({latency:.2f}s): {details}")
    total_latency = sum(item["latency"] for item in rows)
    (ROOT / "EVAL.md").write_text(_markdown(rows, truth, total_latency), encoding="utf-8")
    print(f"\nWrote EVAL.md: {sum(x['passed'] for x in rows)}/{len(rows)} passed; "
          f"{sum(x['violations'] for x in rows)} hard violations; {total_latency:.2f}s total.")
    return 0 if all(row["passed"] for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
