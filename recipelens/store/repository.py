"""Small typed, read-only SQLite queries for recipes and canonical ingredients."""

from __future__ import annotations

import json
import re
import sqlite3
from collections.abc import Iterable
from pathlib import Path

from recipelens.store.models import DEFAULT_FILTER, Filter, FTSMatch, IngredientLine, RecipeRecord

DEFAULT_DB = Path(__file__).resolve().parents[2] / "data" / "recipelens.sqlite3"
_QUERY_WORD = re.compile(r"[\w'-]+", re.UNICODE)


class RecipeRepository:
    """Provide read-only recipe access; index creation is deliberately a separate script."""

    def __init__(self, db_path: Path = DEFAULT_DB) -> None:
        self.db_path = db_path.resolve()
        self._canonical_cache: list[tuple[str, int]] | None = None

    def _connect(self) -> sqlite3.Connection:
        uri = self.db_path.as_uri() + "?mode=ro"
        connection = sqlite3.connect(uri, uri=True)
        connection.row_factory = sqlite3.Row
        return connection

    @staticmethod
    def _where(
        recipe_filter: Filter,
        excluded_canonical: tuple[str, ...] = (),
        *,
        search_eligible: bool = False,
        include_variants: tuple[tuple[str, ...], ...] | None = None,
    ) -> tuple[str, list[object]]:
        clauses = ["1=1"]
        parameters: list[object] = []
        metric_column = {
            "step_count": "step_count",
            "sentence_count": "sentence_count",
        }.get(recipe_filter.step_metric)
        if metric_column is None:
            raise ValueError("step_metric must be 'step_count' or 'sentence_count'")
        if search_eligible:
            clauses.extend(["r.has_title = 1", "r.has_ingredients = 1"])
        if recipe_filter.min_steps is not None:
            clauses.append(f"r.{metric_column} >= ?")
            parameters.append(recipe_filter.min_steps)
        if recipe_filter.max_steps is not None:
            clauses.append(f"r.{metric_column} <= ?")
            parameters.append(recipe_filter.max_steps)
        if recipe_filter.exclude_low_confidence:
            clauses.append("r.instructions_low_confidence = 0")
        if recipe_filter.exclude_title_duplicates:
            clauses.append("r.title_dup_group IS NULL")
        include = tuple(
            dict.fromkeys(
                x.casefold().strip() for x in recipe_filter.include_ingredients if x.strip()
            )
        )
        if include:
            groups = include_variants or tuple((term,) for term in include)
            packed = json.dumps([list(dict.fromkeys(group)) for group in groups])
            clauses.append(
                "r.recipe_id IN (SELECT il.recipe_id FROM ingredient_lines il "
                "JOIN (SELECT CAST(g.key AS INTEGER) AS group_id, v.value AS canonical "
                "FROM json_each(?) AS g, json_each(g.value) AS v) wanted "
                "ON wanted.canonical=il.canonical GROUP BY il.recipe_id "
                + (
                    "HAVING COUNT(DISTINCT wanted.group_id) >= 1"
                    if recipe_filter.include_mode == "any"
                    else "HAVING COUNT(DISTINCT wanted.group_id) = ?"
                )
                + ")"
            )
            parameters.append(packed)
            if recipe_filter.include_mode == "all":
                parameters.append(len(groups))
        excluded = tuple(
            dict.fromkeys(
                [x.casefold().strip() for x in recipe_filter.exclude_ingredients if x.strip()]
                + [x.casefold().strip() for x in excluded_canonical if x.strip()]
            )
        )
        if excluded:
            clauses.append(
                "r.recipe_id NOT IN (SELECT il.recipe_id FROM ingredient_lines il "
                "WHERE il.canonical IN (SELECT value FROM json_each(?)))"
            )
            parameters.append(json.dumps(excluded))
        return " AND ".join(clauses), parameters

    @staticmethod
    def _record(row: sqlite3.Row, canonical: tuple[str, ...] = ()) -> RecipeRecord:
        return RecipeRecord(
            recipe_id=row["recipe_id"],
            source=row["source"],
            original_key=row["original_key"],
            title=row["title"],
            ingredients_raw=row["ingredients_raw"],
            instructions_raw=row["instructions_raw"],
            step_count=row["step_count"],
            sentence_count=row["sentence_count"],
            instructions_low_confidence=bool(row["instructions_low_confidence"]),
            ingredient_count=row["ingredient_count"],
            has_title=bool(row["has_title"]),
            has_ingredients=bool(row["has_ingredients"]),
            has_instructions=bool(row["has_instructions"]),
            title_dup_group=row["title_dup_group"],
            canonical_ingredients=canonical,
        )

    def get_recipe(self, recipe_id: str) -> RecipeRecord | None:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT * FROM recipes WHERE recipe_id = ?", (recipe_id,)
            ).fetchone()
            if row is None:
                return None
            canonical = tuple(
                r[0]
                for r in connection.execute(
                    "SELECT canonical FROM ingredient_lines WHERE recipe_id = ? ORDER BY position",
                    (recipe_id,),
                )
            )
            return self._record(row, canonical)

    def recipes_for_ids(self, recipe_ids: Iterable[str]) -> dict[str, RecipeRecord]:
        ids = list(dict.fromkeys(recipe_ids))
        found: dict[str, RecipeRecord] = {}
        with self._connect() as connection:
            for offset in range(0, len(ids), 500):
                chunk = ids[offset : offset + 500]
                placeholders = ",".join("?" for _ in chunk)
                rows = connection.execute(
                    f"SELECT * FROM recipes WHERE recipe_id IN ({placeholders})",
                    chunk,
                ).fetchall()
                for row in rows:
                    found[row["recipe_id"]] = self._record(row)
        return found

    def filter_ids(
        self,
        recipe_filter: Filter = DEFAULT_FILTER,
        *,
        excluded_canonical: tuple[str, ...] = (),
        search_eligible: bool = False,
        require_ingredients: bool = False,
        require_title: bool = False,
        require_instructions: bool = False,
        id_subset: tuple[str, ...] | list[str] | None = None,
        include_variants: tuple[tuple[str, ...], ...] | None = None,
    ) -> list[str]:
        where, params = self._where(
            recipe_filter,
            excluded_canonical,
            search_eligible=search_eligible,
            include_variants=include_variants,
        )
        if id_subset is not None:
            where += " AND r.recipe_id IN (SELECT value FROM json_each(?))"
            params.append(json.dumps(id_subset))
        if require_ingredients and not search_eligible:
            where += " AND r.has_ingredients=1"
        if require_title and not search_eligible:
            where += " AND r.has_title=1"
        if require_instructions:
            where += " AND r.has_instructions=1"
        with self._connect() as connection:
            rows = connection.execute(
                f"SELECT r.recipe_id FROM recipes r WHERE {where}", params
            ).fetchall()
        return [row[0] for row in rows]

    def recipes_for_filter(
        self,
        recipe_filter: Filter = DEFAULT_FILTER,
        *,
        excluded_canonical: tuple[str, ...] = (),
        search_eligible: bool = False,
        require_ingredients: bool = False,
        require_title: bool = False,
        require_instructions: bool = False,
        include_variants: tuple[tuple[str, ...], ...] | None = None,
    ) -> list[RecipeRecord]:
        where, params = self._where(
            recipe_filter,
            excluded_canonical,
            search_eligible=search_eligible,
            include_variants=include_variants,
        )
        if require_ingredients and not search_eligible:
            where += " AND r.has_ingredients=1"
        if require_title and not search_eligible:
            where += " AND r.has_title=1"
        if require_instructions:
            where += " AND r.has_instructions=1"
        with self._connect() as connection:
            rows = connection.execute(f"SELECT r.* FROM recipes r WHERE {where}", params).fetchall()
        return [self._record(row) for row in rows]

    def ingredient_lines_for(
        self, recipe_ids: Iterable[str]
    ) -> dict[str, tuple[IngredientLine, ...]]:
        ids = list(dict.fromkeys(recipe_ids))
        result: dict[str, list[IngredientLine]] = {recipe_id: [] for recipe_id in ids}
        with self._connect() as connection:
            for offset in range(0, len(ids), 500):
                chunk = ids[offset : offset + 500]
                placeholders = ",".join("?" for _ in chunk)
                rows = connection.execute(
                    f"SELECT recipe_id, position, raw, canonical, qty, unit, name, prep "
                    f"FROM ingredient_lines WHERE recipe_id IN ({placeholders}) "
                    "ORDER BY recipe_id, position",
                    chunk,
                )
                for row in rows:
                    result[row["recipe_id"]].append(IngredientLine(**dict(row)))
        return {recipe_id: tuple(lines) for recipe_id, lines in result.items()}

    def canonical_counts(self, limit: int | None = 100) -> list[tuple[str, int]]:
        if limit is None and self._canonical_cache is not None:
            return self._canonical_cache
        limit_sql = "" if limit is None else " LIMIT ?"
        parameters: tuple[object, ...] = () if limit is None else (limit,)
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT canonical, COUNT(DISTINCT recipe_id) AS n FROM ingredient_lines "
                f"GROUP BY canonical ORDER BY n DESC, canonical{limit_sql}",
                parameters,
            ).fetchall()
        result = [(row["canonical"], row["n"]) for row in rows]
        if limit is None:
            self._canonical_cache = result
        return result

    def top_overlap_ids(
        self,
        include_variants: tuple[tuple[str, ...], ...],
        recipe_filter: Filter = DEFAULT_FILTER,
        *,
        excluded_canonical: tuple[str, ...] = (),
        require_instructions: bool = False,
        min_overlap: int = 1,
        limit: int = 5000,
    ) -> tuple[list[tuple[str, int]], int]:
        """Rank search-eligible recipes by how many ingredient groups they contain.

        Each element of ``include_variants`` is one wanted ingredient (a tuple of acceptable
        canonical values). Returns ``([(recipe_id, overlap), ...], total_candidates)`` ordered by
        overlap desc, then fewer total ingredients, then recipe_id; the list is capped at
        ``limit`` while ``total_candidates`` counts every recipe that met ``min_overlap``.
        Hard constraints in ``recipe_filter`` / ``excluded_canonical`` apply before ranking.
        """
        groups = [list(dict.fromkeys(group)) for group in include_variants if group]
        if not groups:
            return [], 0
        where, where_params = self._where(
            recipe_filter, excluded_canonical, search_eligible=True
        )
        if require_instructions:
            where += " AND r.has_instructions=1"
        packed = json.dumps(groups)
        body = (
            "FROM recipes r JOIN ingredient_lines il ON il.recipe_id = r.recipe_id "
            "JOIN (SELECT CAST(g.key AS INTEGER) AS group_id, v.value AS canonical "
            "FROM json_each(?) AS g, json_each(g.value) AS v) wanted "
            "ON wanted.canonical = il.canonical "
            f"WHERE {where} GROUP BY r.recipe_id "
            "HAVING COUNT(DISTINCT wanted.group_id) >= ?"
        )
        with self._connect() as connection:
            total = connection.execute(
                f"SELECT COUNT(*) FROM (SELECT r.recipe_id {body})",
                [packed, *where_params, min_overlap],
            ).fetchone()[0]
            rows = connection.execute(
                "SELECT r.recipe_id, COUNT(DISTINCT wanted.group_id) AS overlap "
                f"{body} ORDER BY overlap DESC, r.ingredient_count ASC, r.recipe_id ASC LIMIT ?",
                [packed, *where_params, min_overlap, limit],
            ).fetchall()
        return [(row["recipe_id"], int(row["overlap"])) for row in rows], int(total)

    def ingredient_line_records_for(self, recipe_id: str) -> tuple[tuple[str, str], ...]:
        """Return original source line and canonical value for a recipe, in source order."""
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT raw, canonical FROM ingredient_lines WHERE recipe_id=? ORDER BY position",
                (recipe_id,),
            ).fetchall()
        return tuple((row["raw"], row["canonical"]) for row in rows)

    def counts(self) -> dict[str, int]:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT COUNT(*) AS all_recipes, SUM(has_ingredients=1) AS usable_ingredients, "
                "SUM(has_title=1 AND has_ingredients=1) AS search_eligible FROM recipes"
            ).fetchone()
        return {
            "all_recipes": int(row["all_recipes"]),
            "usable_ingredients": int(row["usable_ingredients"]),
            "search_eligible": int(row["search_eligible"]),
        }

    def count_low_confidence(
        self,
        recipe_filter: Filter = DEFAULT_FILTER,
        *,
        excluded_canonical: tuple[str, ...] = (),
        include_variants: tuple[tuple[str, ...], ...] | None = None,
        require_ingredients: bool = False,
        require_instructions: bool = False,
    ) -> int:
        """Count flagged candidates after all other filter conditions, before confidence exclusion."""
        from dataclasses import replace

        candidate_filter = replace(recipe_filter, exclude_low_confidence=False)
        where, parameters = self._where(
            candidate_filter,
            excluded_canonical,
            include_variants=include_variants,
        )
        where += " AND r.instructions_low_confidence=1"
        if require_ingredients:
            where += " AND r.has_ingredients=1"
        if require_instructions:
            where += " AND r.has_instructions=1"
        with self._connect() as connection:
            return int(
                connection.execute(
                    f"SELECT COUNT(*) FROM recipes r WHERE {where}", parameters
                ).fetchone()[0]
            )

    def fts_search(
        self,
        query: str,
        recipe_filter: Filter,
        limit: int,
        *,
        title_weight: float,
        ingredient_weight: float,
        excluded_canonical: tuple[str, ...] = (),
        include_variants: tuple[tuple[str, ...], ...] | None = None,
    ) -> list[FTSMatch]:
        tokens = list(dict.fromkeys(_QUERY_WORD.findall(query.casefold())))
        if not tokens:
            return []
        fts_query = " OR ".join(f'"{token.replace(chr(34), "")}"' for token in tokens)
        if title_weight < 0 or ingredient_weight < 0:
            raise ValueError("FTS weights must be non-negative")
        where, where_params = self._where(
            recipe_filter,
            excluded_canonical,
            search_eligible=True,
            include_variants=include_variants,
        )
        sql = (
            f"SELECT f.recipe_id, r.title, f.ingredients, bm25(recipe_fts, 0.0, {title_weight}, {ingredient_weight}) AS rank "
            "FROM recipe_fts f JOIN recipes r ON r.recipe_id=f.recipe_id "
            f"WHERE recipe_fts MATCH ? AND {where} ORDER BY rank LIMIT ?"
        )
        with self._connect() as connection:
            rows = connection.execute(sql, [fts_query, *where_params, limit]).fetchall()
        results = []
        for row in rows:
            text = f"{row['title']} {row['ingredients']}".casefold()
            matched = tuple(
                token for token in tokens if re.search(rf"(?<!\w){re.escape(token)}(?!\w)", text)
            )
            results.append(FTSMatch(row["recipe_id"], row["title"], float(row["rank"]), matched))
        return results
