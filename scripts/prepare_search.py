"""Create or rebuild the FTS5 side index used by the read-only repository."""

from __future__ import annotations

import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "recipelens.sqlite3"


def prepare_fts(db_path: Path = DB_PATH, *, force: bool = False) -> int:
    """Populate a separate FTS5 table for recipes that meet the search-quality flags."""
    with sqlite3.connect(db_path) as connection:
        connection.execute(
            "CREATE VIRTUAL TABLE IF NOT EXISTS recipe_fts USING fts5("
            "recipe_id UNINDEXED, title, ingredients, tokenize='unicode61')"
        )
        expected = connection.execute(
            "SELECT COUNT(*) FROM recipes WHERE has_title=1 AND has_ingredients=1"
        ).fetchone()[0]
        current = connection.execute("SELECT COUNT(*) FROM recipe_fts").fetchone()[0]
        if force or current != expected:
            connection.execute("DELETE FROM recipe_fts")
            connection.execute(
                "INSERT INTO recipe_fts(rowid, recipe_id, title, ingredients) "
                "SELECT r.rowid, r.recipe_id, r.title_clean, "
                "COALESCE((SELECT group_concat(il.canonical, ' ') FROM ingredient_lines il "
                "WHERE il.recipe_id = r.recipe_id), '') "
                "FROM recipes r WHERE r.has_title=1 AND r.has_ingredients=1"
            )
        return expected


if __name__ == "__main__":
    print(f"FTS5 indexed {prepare_fts():,} searchable recipes.")
