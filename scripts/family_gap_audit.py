"""Explain approved family-mode/raw-regex differences with reproducible samples."""

from __future__ import annotations

import json
import random
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "recipelens.sqlite3"
REPORT_PATH = ROOT / "INGREDIENT_MATCH_AUDIT.md"
RAW_TOKEN_PATTERNS = {
    "tomato": re.compile(r"\btomato(?:es)?\b", re.IGNORECASE),
    "garlic": re.compile(r"\bgarlic\b", re.IGNORECASE),
    "onion": re.compile(r"\bonions?\b", re.IGNORECASE),
}


def _matching_line(
    text: str, includes: tuple[re.Pattern[str], ...], excludes: tuple[re.Pattern[str], ...]
) -> bool:
    head = text.split(",", maxsplit=1)[0].strip()
    return any(pattern.search(head) for pattern in includes) and not any(
        pattern.search(text) for pattern in excludes
    )


def _escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def build_gap_report(db_path: Path = DB_PATH) -> str:
    config = yaml.safe_load((ROOT / "config" / "gap_audit.yaml").read_text(encoding="utf-8"))
    seed = int(config["seed"])
    sample_size = int(config["sample_size_per_side"])
    families = yaml.safe_load((ROOT / "config" / "families.yaml").read_text(encoding="utf-8"))[
        "families"
    ]
    connection = sqlite3.connect(db_path)
    recipes = connection.execute("SELECT recipe_id, ingredients_raw FROM recipes").fetchall()
    line_rows = connection.execute(
        "SELECT recipe_id, raw, canonical FROM ingredient_lines ORDER BY recipe_id, position"
    ).fetchall()
    connection.close()

    lines_by_recipe: defaultdict[str, list[tuple[str, str]]] = defaultdict(list)
    canonical_matches: dict[str, set[str]] = {term: set() for term in families}
    raw_matches: dict[str, dict[str, str]] = {term: {} for term in families}
    compiled = {
        term: (
            tuple(re.compile(p, re.IGNORECASE) for p in rules["match_patterns"]),
            tuple(re.compile(p, re.IGNORECASE) for p in rules["exclude_patterns"]),
        )
        for term, rules in families.items()
    }
    for recipe_id, raw, canonical in line_rows:
        lines_by_recipe[recipe_id].append((raw, canonical))
        for term, (includes, excludes) in compiled.items():
            if _matching_line(canonical, includes, excludes):
                canonical_matches[term].add(recipe_id)

    raw_source_lines: dict[str, dict[str, str]] = {term: {} for term in families}
    for recipe_id, raw_json in recipes:
        if not raw_json:
            continue
        source_lines = json.loads(raw_json)
        if not isinstance(source_lines, list):
            continue
        for term, pattern in RAW_TOKEN_PATTERNS.items():
            for line in source_lines:
                if isinstance(line, str) and pattern.search(line):
                    raw_matches[term][recipe_id] = line
                    raw_source_lines[term][recipe_id] = line
                    break

    sections = [
        "## Family-mode vs raw-regex gap details",
        "",
        f"Samples use `random.Random({seed})` from `config/gap_audit.yaml`; each side contributes up to {sample_size} recipe IDs.",
        "Raw regex scans original ingredient lines for the token, including excluded products and mentions outside the ingredient head. Each sample includes its triggering source line.",
        "",
    ]
    for term in families:
        family_only = canonical_matches[term] - raw_matches[term].keys()
        regex_only = raw_matches[term].keys() - canonical_matches[term]
        family_variants: Counter[str] = Counter()
        regex_variants: Counter[str] = Counter()
        family_causes: dict[str, tuple[str, str]] = {}
        regex_causes: dict[str, tuple[str, str]] = {}
        exclusion_counts: Counter[str] = Counter()
        for recipe_id in family_only:
            matches = [
                (raw, canonical)
                for raw, canonical in lines_by_recipe[recipe_id]
                if _matching_line(canonical, *compiled[term])
            ]
            if matches:
                raw, canonical = matches[0]
                family_causes[recipe_id] = (raw, canonical)
                family_variants[canonical] += 1
        for recipe_id in regex_only:
            raw = raw_source_lines[term][recipe_id]
            canonical = next(
                (canonical for line, canonical in lines_by_recipe[recipe_id] if line == raw),
                "(no parsed ingredient line)",
            )
            regex_causes[recipe_id] = (raw, canonical)
            regex_variants[canonical] += 1
            for pattern in compiled[term][1]:
                if pattern.search(canonical) or pattern.search(raw):
                    exclusion_counts[pattern.pattern] += 1

        sections.extend(
            [
                f"### {term}",
                "",
                f"Family-not-regex recipes: **{len(family_only):,}**. Regex-not-family recipes: **{len(regex_only):,}**. Net canonical-family minus raw-regex gap: **{len(family_only) - len(regex_only):+,}**.",
                "",
                "Largest configured product exclusions observed in regex-not-family causes:",
                "",
            ]
        )
        if exclusion_counts:
            sections.extend(
                f"- `{pattern}`: {count:,} recipe causes"
                for pattern, count in exclusion_counts.most_common(5)
            )
        else:
            sections.append(
                "- No configured product exclusion matched these causes; the variant and sample tables show parse/source mismatches."
            )
        sections.append("")
        for heading, variants, candidates in (
            ("Family-not-regex", family_variants, family_only),
            ("Regex-not-family", regex_variants, regex_only),
        ):
            sections.extend(
                [
                    f"#### Top 20 {heading} canonical variants",
                    "",
                    "| Canonical variant | Recipes |",
                    "|---|---:|",
                ]
            )
            sections.extend(
                f"| {canonical} | {count:,} |"
                for canonical, count in sorted(
                    variants.items(), key=lambda item: (-item[1], item[0])
                )[:20]
            )
            sections.extend(["", f"#### Random sample: {heading} (up to {sample_size})", ""])
            rng = random.Random(seed + sum(map(ord, term + heading)))
            selected = rng.sample(sorted(candidates), min(sample_size, len(candidates)))
            sections.extend(
                [
                    "| Recipe ID | Triggering raw ingredient line | Canonical value |",
                    "|---|---|---|",
                ]
            )
            causes = family_causes if heading == "Family-not-regex" else regex_causes
            sections.extend(
                f"| `{recipe_id}` | {_escape_table(causes[recipe_id][0])} | {_escape_table(causes[recipe_id][1])} |"
                for recipe_id in selected
            )
            sections.append("")
    sections.extend(
        [
            "### Main sources of the gaps",
            "",
            "- **Onion family-only matches:** configured scallion and spring-onion synonym merges produce canonical `green onion` values that a literal raw `onion` regex misses.",
            "- **Regex-only matches:** raw ingredients that parse to a non-family canonical value, descriptions/noise retained in source lines, or preparation/product wording that the approved family excludes. Inspect the per-term top-20 tables to see the observed largest variants.",
            "- **Product exclusions:** tomato paste/sauce and garlic/onion powders are intentionally excluded from their base families; these often account for regex-only variants.",
            "",
        ]
    )
    return "\n".join(sections)


def main() -> None:
    report = REPORT_PATH.read_text(encoding="utf-8")
    marker = "## Family-mode vs raw-regex gap details"
    report = report.split(marker, maxsplit=1)[0].rstrip()
    report += "\n\n" + build_gap_report() + "\n"
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(f"Updated {REPORT_PATH}")


if __name__ == "__main__":
    main()
