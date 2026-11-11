"""Add sentence/confidence columns and populate them for the current SQLite corpus."""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

from tqdm import tqdm

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from recipelens.data.steps import count_sentences, instructions_low_confidence

DB_PATH = ROOT / "data" / "recipelens.sqlite3"


def migrate(db_path: Path = DB_PATH) -> None:
    with sqlite3.connect(db_path) as connection:
        columns = {row[1] for row in connection.execute("PRAGMA table_info(recipes)")}
        if "sentence_count" not in columns:
            connection.execute(
                "ALTER TABLE recipes ADD COLUMN sentence_count INTEGER NOT NULL DEFAULT 0"
            )
        if "instructions_low_confidence" not in columns:
            connection.execute(
                "ALTER TABLE recipes ADD COLUMN instructions_low_confidence INTEGER NOT NULL DEFAULT 1"
            )
        rows = connection.execute(
            "SELECT recipe_id, instructions_clean FROM recipes ORDER BY recipe_id"
        ).fetchall()
        connection.executemany(
            "UPDATE recipes SET sentence_count=?, instructions_low_confidence=? WHERE recipe_id=?",
            (
                (
                    count_sentences(instructions),
                    int(instructions_low_confidence(instructions)),
                    recipe_id,
                )
                for recipe_id, instructions in tqdm(rows, desc="Refresh instruction metrics")
            ),
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_recipes_sentence_count ON recipes(sentence_count)"
        )
    print(f"Updated instruction metrics in {db_path}")


if __name__ == "__main__":
    migrate()
