"""One-off helper: applies the matcher's two edits to existing files. Safe to run twice.

Run from the repo root:   python apply_matcher_changes.py
"""
from pathlib import Path

METHOD = '    def top_overlap_ids(\n        self,\n        include_variants: tuple[tuple[str, ...], ...],\n        recipe_filter: Filter = DEFAULT_FILTER,\n        *,\n        excluded_canonical: tuple[str, ...] = (),\n        require_instructions: bool = False,\n        min_overlap: int = 1,\n        limit: int = 5000,\n    ) -> tuple[list[tuple[str, int]], int]:\n        """Rank search-eligible recipes by how many ingredient groups they contain.\n\n        Each element of ``include_variants`` is one wanted ingredient (a tuple of acceptable\n        canonical values). Returns ``([(recipe_id, overlap), ...], total_candidates)`` ordered by\n        overlap desc, then fewer total ingredients, then recipe_id; the list is capped at\n        ``limit`` while ``total_candidates`` counts every recipe that met ``min_overlap``.\n        Hard constraints in ``recipe_filter`` / ``excluded_canonical`` apply before ranking.\n        """\n        groups = [list(dict.fromkeys(group)) for group in include_variants if group]\n        if not groups:\n            return [], 0\n        where, where_params = self._where(\n            recipe_filter, excluded_canonical, search_eligible=True\n        )\n        if require_instructions:\n            where += " AND r.has_instructions=1"\n        packed = json.dumps(groups)\n        body = (\n            "FROM recipes r JOIN ingredient_lines il ON il.recipe_id = r.recipe_id "\n            "JOIN (SELECT CAST(g.key AS INTEGER) AS group_id, v.value AS canonical "\n            "FROM json_each(?) AS g, json_each(g.value) AS v) wanted "\n            "ON wanted.canonical = il.canonical "\n            f"WHERE {where} GROUP BY r.recipe_id "\n            "HAVING COUNT(DISTINCT wanted.group_id) >= ?"\n        )\n        with self._connect() as connection:\n            total = connection.execute(\n                f"SELECT COUNT(*) FROM (SELECT r.recipe_id {body})",\n                [packed, *where_params, min_overlap],\n            ).fetchone()[0]\n            rows = connection.execute(\n                "SELECT r.recipe_id, COUNT(DISTINCT wanted.group_id) AS overlap "\n                f"{body} ORDER BY overlap DESC, r.ingredient_count ASC, r.recipe_id ASC LIMIT ?",\n                [packed, *where_params, min_overlap, limit],\n            ).fetchall()\n        return [(row["recipe_id"], int(row["overlap"])) for row in rows], int(total)\n\n'
FAMILIES = '  egg:\n    # Head-anchored: matches "egg", "large egg", "hard-boiled egg"; not egg white/yolk/noodles/eggplant.\n    match_patterns:\n      - "\\\\beggs?\\\\s*$"\n    exclude_patterns:\n      - "\\\\beggplants?\\\\b"\n      - "\\\\begg (?:substitute|replacer|beaters)\\\\b"\n  rice:\n    # Matches "rice", "cooked rice", "long-grain white rice"; not rice flour/vinegar/wine/paper/noodles.\n    match_patterns:\n      - "\\\\brice\\\\s*$"\n    exclude_patterns:\n      - "\\\\brice (?:flour|vinegar|wine|paper|noodles?|milk|cereal|krispies|syrup|bran)\\\\b"\n      - "\\\\b(?:puffed|crispy|crisped) rice\\\\b"\n'


def edit(path, fn):
    p = Path(path)
    raw = p.read_bytes().decode("utf-8-sig") if path.endswith(".yaml") else p.read_bytes().decode("utf-8")
    crlf = "\r\n" in raw
    text = raw.replace("\r\n", "\n")
    new = fn(text)
    if new == text:
        print(f"{path}: already up to date")
        return
    if crlf:
        new = new.replace("\n", "\r\n")
    p.write_bytes(new.encode("utf-8"))
    print(f"{path}: updated")


def repo_edit(s):
    if "def top_overlap_ids" in s:
        return s
    a = """        self.db_path = db_path.resolve()
"""
    assert a in s, "repository.py __init__ not found - is this the right folder?"
    s = s.replace(a, a + "        self._canonical_cache: list[tuple[str, int]] | None = None\n", 1)
    b = """    def canonical_counts(self, limit: int | None = 100) -> list[tuple[str, int]]:
"""
    assert b in s, "canonical_counts not found"
    s = s.replace(b, b + "        if limit is None and self._canonical_cache is not None:\n            return self._canonical_cache\n", 1)
    c = """        return [(row["canonical"], row["n"]) for row in rows]
"""
    assert c in s, "canonical_counts return not found"
    s = s.replace(
        c,
        "        result = [(row[\"canonical\"], row[\"n\"]) for row in rows]\n"
        "        if limit is None:\n            self._canonical_cache = result\n        return result\n\n" + METHOD.rstrip("\n") + "\n",
        1,
    )
    return s


def fam_edit(s):
    if "\n  egg:\n" in s:
        return s
    return (s if s.endswith("\n") else s + "\n") + FAMILIES


edit("recipelens/store/repository.py", repo_edit)
edit("config/families.yaml", fam_edit)
print("Done. Now run: python -m pytest tests/test_matcher.py")
