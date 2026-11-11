"""Build normalized SQLite rows and a report generated from that database."""

from __future__ import annotations

import logging
import sqlite3
import sys
from collections import Counter
from pathlib import Path

import yaml
from tqdm import tqdm

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from recipelens.data.ingredients import ParsedIngredient
from recipelens.data.loader import (
    iter_source_records,
    make_recipe,
    source_name,
    title_duplicate_groups,
)

RAW_DIR = ROOT / "data_raw"
DB_PATH = ROOT / "data" / "recipelens.sqlite3"
SCHEMA_PATH = ROOT / "store" / "schema.sql"


def source_files() -> list[Path]:
    paths = sorted(RAW_DIR.glob("recipes_raw_nosource_*.json"))
    expected = {"ar", "epi", "fn"}
    actual = {source_name(path) for path in paths}
    if actual != expected:
        raise FileNotFoundError(f"Expected {sorted(expected)} sources; found {sorted(actual)}")
    return paths


def file_record_count(path: Path) -> int:
    return sum(1 for _ in iter_source_records(path))


def _percent(value: int, denominator: int) -> str:
    return f"{value:,} ({value / denominator:.2%})"


def _add_record(
    connection: sqlite3.Connection, values: dict, ingredients: list[ParsedIngredient]
) -> None:
    columns = list(values)
    connection.execute(
        f"INSERT INTO recipes ({','.join(columns)}) VALUES ({','.join('?' for _ in columns)})",
        [values[column] for column in columns],
    )
    connection.executemany(
        "INSERT INTO ingredient_lines(recipe_id, position, raw, canonical, qty, unit, name, prep) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (values["recipe_id"], i, x.raw, x.canonical, x.qty, x.unit, x.name, x.prep)
            for i, x in enumerate(ingredients)
        ],
    )


def build_database(paths: list[Path] | None = None, db_path: Path = DB_PATH) -> None:
    files = paths or source_files()
    duplicate_groups = title_duplicate_groups(files)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as connection:
        connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        columns = {row[1] for row in connection.execute("PRAGMA table_info(recipes)")}
        if "sentence_count" not in columns:
            connection.execute(
                "ALTER TABLE recipes ADD COLUMN sentence_count INTEGER NOT NULL DEFAULT 0"
            )
        if "instructions_low_confidence" not in columns:
            connection.execute(
                "ALTER TABLE recipes ADD COLUMN instructions_low_confidence INTEGER NOT NULL DEFAULT 1"
            )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_recipes_sentence_count ON recipes(sentence_count)"
        )
        connection.execute("DELETE FROM recipe_fts")
        connection.execute("DELETE FROM ingredient_lines")
        connection.execute("DELETE FROM recipes")
        for path in files:
            source = source_name(path)
            count = file_record_count(path)
            for key, record in tqdm(
                iter_source_records(path), total=count, desc=f"Ingest {source}"
            ):
                values, ingredients = make_recipe(
                    source, key, record, duplicate_groups.get((source, key))
                )
                _add_record(connection, values, ingredients)
    print(f"Built {db_path}")


def make_report(db_path: Path = DB_PATH, output_path: Path = ROOT / "DATA_REPORT.md") -> str:
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    total = connection.execute("SELECT COUNT(*) FROM recipes").fetchone()[0]
    usable = connection.execute("SELECT COUNT(*) FROM recipes WHERE has_ingredients=1").fetchone()[
        0
    ]
    sources = connection.execute(
        "SELECT source, COUNT(*) AS n, "
        "SUM(title_raw IS NULL) AS title_missing, SUM(title_raw IS NOT NULL AND trim(title_raw)='') AS title_empty, "
        "SUM(ingredients_raw IS NULL) AS ingredients_missing, "
        "SUM(ingredients_raw IS NOT NULL AND has_ingredients=0) AS ingredients_empty, "
        "SUM(instructions_raw IS NULL) AS instructions_missing, "
        "SUM(instructions_raw IS NOT NULL AND trim(instructions_raw)='') AS instructions_empty, "
        "SUM(title_dup_group IS NOT NULL) AS duplicate_title_rows, COUNT(DISTINCT title_dup_group) AS duplicate_title_groups "
        "FROM recipes GROUP BY source ORDER BY source"
    ).fetchall()
    top = connection.execute(
        "SELECT canonical, COUNT(DISTINCT recipe_id) AS recipes FROM ingredient_lines "
        "WHERE canonical <> '' GROUP BY canonical ORDER BY recipes DESC, canonical LIMIT 30"
    ).fetchall()
    duplicate_stats = connection.execute(
        "SELECT COUNT(DISTINCT title_dup_group), COUNT(*) FROM recipes WHERE title_dup_group IS NOT NULL"
    ).fetchone()
    rules = yaml.safe_load((ROOT / "config" / "synonyms.yaml").read_text(encoding="utf-8"))[
        "synonyms"
    ]
    fired: Counter[tuple[str, str]] = Counter()
    for old, canonical in rules.items():
        count = connection.execute(
            "SELECT COUNT(*) FROM ingredient_lines WHERE name=? AND canonical=?", (old, canonical)
        ).fetchone()[0]
        if count:
            fired[(old, canonical)] = count
    cleaning = yaml.safe_load((ROOT / "config" / "cleaning.yaml").read_text(encoding="utf-8"))
    plural_fired: Counter[tuple[str, str]] = Counter()
    for plural, singular in cleaning.get("plural_singular", {}).items():
        count = connection.execute(
            "SELECT COUNT(*) FROM ingredient_lines WHERE lower(raw) LIKE ?",
            (f"%{plural.lower()}%",),
        ).fetchone()[0]
        if count:
            plural_fired[(plural, singular)] = count
    noise_hits = connection.execute(
        "SELECT COUNT(*) FROM ingredient_lines WHERE upper(raw) LIKE '%ADVERTISEMENT%'"
    ).fetchone()[0]
    denominator_text = (
        f"**All recipes = {total:,}**: every source record, including missing and incomplete records. "
        f"**Recipes with usable ingredients = {usable:,}**: records with at least one nonblank ingredient line after configured scrape-noise removal. "
        "Ingredient-frequency statistics use this complete usable-ingredient subset; parsing failure does not remove a line from that denominator. "
        "Percentages in the table use each source's complete row count."
    )
    lines = [
        "# Recipe Box data report",
        "",
        f"Database generated from the three source JSON files. All recipe rows: **{total:,}**.",
        "",
        "## Denominators and quality flags",
        "",
        denominator_text,
        "",
        "| Source | Rows | Missing title | Empty title | Missing ingredients | Empty/unusable ingredients | Missing instructions | Empty instructions | Duplicate title groups / rows |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in sources:
        n = row["n"]
        lines.append(
            f"| {row['source']} | {n:,} | {_percent(row['title_missing'], n)} | {_percent(row['title_empty'], n)} | "
            f"{_percent(row['ingredients_missing'], n)} | {_percent(row['ingredients_empty'], n)} | "
            f"{_percent(row['instructions_missing'], n)} | {_percent(row['instructions_empty'], n)} | "
            f"{row['duplicate_title_groups']:,} / {row['duplicate_title_rows']:,} |"
        )
    duplicate_text = (
        f"Across sources, duplicate title group IDs: **{duplicate_stats[0]:,}**, covering **{duplicate_stats[1]:,} rows**. "
        "Groups use trimmed, case-folded title equality; records are not deduplicated."
    )
    lines.extend(
        [
            "",
            duplicate_text,
            "",
            "## Top 30 canonical ingredients",
            "",
            "Frequency is the number of distinct recipes containing the canonical ingredient; the analytical base is all recipes with usable ingredients.",
            "",
            "| Rank | Canonical ingredient | Recipes |",
            "|---:|---|---:|",
        ]
    )
    lines.extend(
        f"| {rank} | {row['canonical']} | {row['recipes']:,} |" for rank, row in enumerate(top, 1)
    )
    normalization_text = (
        "Ingredient quantities are extracted with the documented regex parser. Unit aliases come from `config/units.yaml`; "
        "noise patterns, prep separators, and explicit plural-to-singular mappings come from `config/cleaning.yaml`. "
        "Explicit synonym merges come only from `config/synonyms.yaml`; every plural and synonym merge logs an INFO record to `data/normalization.log` during scripted ingestion. "
        "Products such as garlic/garlic powder, butter/peanut butter, and milk/coconut milk remain separate."
    )
    lines.extend(
        [
            "",
            "## Normalization rules",
            "",
            normalization_text,
            "",
            "Observed explicit synonym merges (ingredient lines):",
        ]
    )
    lines.extend(
        f"- `{old}` -> `{canonical}`: {count:,}" for (old, canonical), count in fired.items()
    )
    if not fired:
        lines.append("- No configured synonym merges occurred in this corpus.")
    lines.append("")
    lines.append(
        "Observed explicit plural-to-singular mappings (ingredient lines containing the source form):"
    )
    lines.extend(
        f"- `{plural}` -> `{singular}`: {count:,}"
        for (plural, singular), count in plural_fired.items()
    )
    if not plural_fired:
        lines.append("- No configured plural mappings appeared in ingredient lines.")
    lines.append(
        f"- `ADVERTISEMENT` scrape-noise suffix removed from {noise_hits:,} ingredient lines."
    )
    from scripts.inspect_data import inspect

    inspection = inspect()
    lines.extend(
        [
            "",
            "## Source inspection",
            "",
            "Sample source records (the reproducible inspector prints the complete sampled records):",
            "",
        ]
    )
    for source in ("ar", "epi", "fn"):
        examples = inspection[source]["sample_records"]
        titles = "; ".join(f"`{item.get('title')}` (key `{item['key']}`)" for item in examples)
        lines.append(f"- **{source}**: {titles}")
    lines.extend(
        [
            "",
            "Instruction string layout by source (empty strings are counted as single-block strings):",
            "",
            "| Source | Newline-separated strings | Single-block strings |",
            "|---|---:|---:|",
        ]
    )
    for source in ("ar", "epi", "fn"):
        formats = inspection[source]["instruction_formats"]
        lines.append(
            f"| {source} | {formats.get('newline-separated', 0):,} | {formats.get('single-block', 0):,} |"
        )
    collisions = inspection["cross_source_key_collisions"]
    lines.extend(
        [
            "",
            f"Original keys shared across source files: **{collisions['count']}**.",
            "",
            "Representative noise strings found in source fields:",
        ]
    )
    for source in ("ar", "epi", "fn"):
        for field, label in (
            ("ingredient_noise", "ingredients"),
            ("instruction_noise", "instructions"),
        ):
            examples = inspection[source][field][:3]
            if examples:
                display = "; ".join(
                    f"`{sample.replace('|', '/').replace('`', chr(39))[:120]}` ({count})"
                    for sample, count in examples
                )
                lines.append(f"- **{source} {label}**: {display}")
    report = "\n".join(lines) + "\n"
    output_path.write_text(report, encoding="utf-8")
    connection.close()
    return report


if __name__ == "__main__":
    log_path = ROOT / "data" / "normalization.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_path, level=logging.INFO, encoding="utf-8", format="%(asctime)s %(message)s"
    )
    build_database()
    make_report()
