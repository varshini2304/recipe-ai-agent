"""Compare canonical exact/token-family matches with regex hits in ingredients_raw."""

from __future__ import annotations

import json
import re
import sqlite3
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "recipelens.sqlite3"
TERMS = {"tomato": r"\btomato(?:es)?\b", "garlic": r"\bgarlic\b", "onion": r"\bonions?\b"}


def audit(db_path: Path = DB_PATH) -> tuple[str, dict]:
    connection = sqlite3.connect(db_path)
    recipes = connection.execute(
        "SELECT recipe_id, has_ingredients, ingredients_raw FROM recipes"
    ).fetchall()
    all_count = len(recipes)
    usable_ids = {recipe_id for recipe_id, has_ingredients, _ in recipes if has_ingredients}
    canonical_recipe_ids: defaultdict[str, set[str]] = defaultdict(set)
    for recipe_id, canonical in connection.execute(
        "SELECT recipe_id, canonical FROM ingredient_lines"
    ):
        canonical_recipe_ids[canonical].add(recipe_id)
    canonical_counts = {name: len(ids) for name, ids in canonical_recipe_ids.items()}
    family_rules = yaml.safe_load((ROOT / "config" / "families.yaml").read_text(encoding="utf-8"))[
        "families"
    ]
    family_stats = {}
    canonical_family_ids_by_term = {}
    raw_family_ids_by_term = {}
    for term, definitions in family_rules.items():
        includes = [re.compile(pattern, re.IGNORECASE) for pattern in definitions["match_patterns"]]
        excludes = [
            re.compile(pattern, re.IGNORECASE) for pattern in definitions["exclude_patterns"]
        ]
        canonical_family_ids = {
            recipe_id
            for canonical, ids in canonical_recipe_ids.items()
            if any(
                pattern.search(canonical.split(",", maxsplit=1)[0].strip()) for pattern in includes
            )
            and not any(pattern.search(canonical) for pattern in excludes)
            for recipe_id in ids
        }
        raw_family_ids = set()
        for recipe_id, _has_ingredients, raw_json in recipes:
            if raw_json is None:
                continue
            source_lines = json.loads(raw_json)
            if any(
                any(pattern.search(line.split(",", maxsplit=1)[0].strip()) for pattern in includes)
                and not any(pattern.search(line) for pattern in excludes)
                for line in source_lines
                if isinstance(line, str)
            ):
                raw_family_ids.add(recipe_id)
        family_stats[term] = (len(canonical_family_ids), len(raw_family_ids))
        canonical_family_ids_by_term[term] = canonical_family_ids
        raw_family_ids_by_term[term] = raw_family_ids
    exact_ids: dict[str, set[str]] = {}
    variant_counts: dict[str, list[tuple[str, int]]] = {}
    for term, expression in TERMS.items():
        pattern = re.compile(expression, re.IGNORECASE)
        variants = sorted(
            (name, count) for name, count in canonical_counts.items() if pattern.search(name)
        )
        variant_counts[term] = variants
        exact_ids[term] = canonical_recipe_ids.get(term, set())
    raw_ids: dict[str, set[str]] = {term: set() for term in TERMS}
    raw_and_ids: set[str] = set()
    for recipe_id, _has_ingredients, raw_json in recipes:
        if raw_json is None:
            continue
        parsed = json.loads(raw_json)
        if not isinstance(parsed, list):
            continue
        text = "\n".join(item for item in parsed if isinstance(item, str))
        found = {
            term for term, expression in TERMS.items() if re.search(expression, text, re.IGNORECASE)
        }
        for term in found:
            raw_ids[term].add(recipe_id)
        if {"garlic", "onion"}.issubset(found):
            raw_and_ids.add(recipe_id)
    exact_and_ids = exact_ids["garlic"] & exact_ids["onion"]
    stats = {
        "all_recipes": all_count,
        "usable_ingredient_recipes": len(usable_ids),
        "terms": {},
        "garlic_and_onion": {
            "exact_count": len(exact_and_ids),
            "raw_regex_count_usable": len(raw_and_ids & usable_ids),
            "raw_regex_count_all": len(raw_and_ids),
            "gap_usable": len(raw_and_ids & usable_ids) - len(exact_and_ids),
        },
    }
    rows = [
        "# Ingredient match audit",
        "",
        "Canonical counts use `ingredient_lines`; raw regex counts search the JSON-decoded original `ingredients_raw` lines directly.",
        "Primary denominator: recipes with usable ingredients. Secondary denominator: all recipe rows.",
        "",
        "| Term | Exact canonical | Canonical token family | Raw-text regex (usable) | Gap: raw minus exact | Raw-text regex (all recipes) |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for term in TERMS:
        variants = variant_counts[term]
        family_ids = set().union(*(canonical_recipe_ids[name] for name, _count in variants))
        exact_count = len(exact_ids[term])
        raw_usable = len(raw_ids[term] & usable_ids)
        stats["terms"][term] = {
            "exact_canonical": exact_count,
            "canonical_token_family": len(family_ids),
            "raw_regex_usable": raw_usable,
            "raw_minus_exact": raw_usable - exact_count,
            "raw_regex_all": len(raw_ids[term]),
            "canonical_variants": variants,
        }
        rows.append(
            f"| {term} | {exact_count:,} | {len(family_ids):,} | {raw_usable:,} | "
            f"{raw_usable - exact_count:+,} | {len(raw_ids[term]):,} |"
        )
    combo = stats["garlic_and_onion"]
    rows.extend(
        [
            "",
            "## Garlic AND onion",
            "",
            f"Exact canonical AND: **{combo['exact_count']:,}** recipes; raw regex AND among usable-ingredient recipes: **{combo['raw_regex_count_usable']:,}**; gap: **{combo['gap_usable']:+,}**.",
            f"Raw regex AND among all recipes: **{combo['raw_regex_count_all']:,}**. Usable denominator: **{len(usable_ids):,}**; all-recipes denominator: **{all_count:,}**.",
            "",
            "## Every canonical variant containing the token",
        ]
    )
    # Place reviewed family results ahead of the exhaustive variant listing.
    family_rows = [
        "## Reviewed family rules: canonical results vs raw-line regex",
        "",
        "Rules come from owner-approved `config/families.yaml`.",
        "| Term | Canonical family recipes | Raw-line regex recipes | Canonical minus raw |",
        "|---|---:|---:|---:|",
        *[
            f"| {term} | {canonical_n:,} | {raw_n:,} | {canonical_n - raw_n:+,} |"
            for term, (canonical_n, raw_n) in family_stats.items()
        ],
        "",
        f"Family garlic AND onion: canonical **{len(canonical_family_ids_by_term['garlic'] & canonical_family_ids_by_term['onion']):,}**; raw-line regex **{len(raw_family_ids_by_term['garlic'] & raw_family_ids_by_term['onion']):,}**.",
        "",
        "## Every canonical variant containing the token",
        "",
    ]
    rows[-2:] = family_rows
    for term in TERMS:
        rows.extend([f"### {term}", "", "| Canonical value | Recipes |", "|---|---:|"])
        rows.extend(f"| {name} | {count:,} |" for name, count in variant_counts[term])
        rows.append("")
    connection.close()
    return "\n".join(rows) + "\n", stats


if __name__ == "__main__":
    report, _ = audit()
    target = ROOT / "INGREDIENT_MATCH_AUDIT.md"
    target.write_text(report, encoding="utf-8")
    print(target)
    print(report.split("## Every canonical variant", maxsplit=1)[0])
