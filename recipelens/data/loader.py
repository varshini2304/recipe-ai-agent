"""Incremental reader for the Recipe Box keyed JSON files."""

from __future__ import annotations

import json
import logging
import re
from collections import Counter
from collections.abc import Iterator
from functools import lru_cache
from pathlib import Path
from typing import Any

import ijson

from recipelens.data.ingredients import ParsedIngredient, parse_ingredient
from recipelens.data.steps import count_sentences, count_steps, instructions_low_confidence

LOGGER = logging.getLogger(__name__)


def iter_source_records(path: Path) -> Iterator[tuple[str, dict[str, Any]]]:
    """Yield top-level mapping entries without loading an entire source file in memory."""
    with path.open("rb") as stream:
        for key, record in ijson.kvitems(stream, ""):
            if not isinstance(record, dict):
                record = {}
            yield str(key), record


def source_name(path: Path) -> str:
    """Extract the known Recipe Box source suffix from an inspected filename."""
    prefix = "recipes_raw_nosource_"
    if not path.stem.startswith(prefix):
        raise ValueError(f"Unexpected Recipe Box source filename: {path.name}")
    return path.stem.removeprefix(prefix)


def title_duplicate_groups(paths: list[Path]) -> dict[tuple[str, str], str]:
    """Return stable source-scoped group IDs for repeated normalized titles."""
    titles: Counter[tuple[str, str]] = Counter()
    records: list[tuple[str, str, str]] = []
    for path in paths:
        source = source_name(path)
        for key, record in iter_source_records(path):
            title = record.get("title")
            normalized = title.strip().casefold() if isinstance(title, str) else ""
            if normalized:
                titles[(source, normalized)] += 1
                records.append((source, key, normalized))
    # Hashing keeps arbitrary source titles out of group identifiers while remaining stable.
    import hashlib

    return {
        (source, key): "title:" + hashlib.sha1(f"{source}:{title}".encode()).hexdigest()[:16]
        for source, key, title in records
        if titles[(source, title)] > 1
    }


def clean_string(value: Any) -> str | None:
    return value.strip() if isinstance(value, str) and value.strip() else None


@lru_cache(maxsize=1)
def _noise_patterns() -> tuple[str, ...]:
    patterns_path = Path(__file__).resolve().parents[2] / "config" / "cleaning.yaml"
    import yaml

    return tuple(
        yaml.safe_load(patterns_path.read_text(encoding="utf-8")).get("noise_patterns", [])
    )


def ingredient_values(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    patterns = _noise_patterns()
    clean_lines = []
    for line in value:
        if not isinstance(line, str):
            continue
        normalized = line.strip()
        for pattern in patterns:
            result = re.sub(pattern, "", normalized).strip()
            if result != normalized:
                LOGGER.info("ingredient scrape-noise removal fired: %r -> %r", normalized, result)
            normalized = result
        if normalized:
            clean_lines.append(normalized)
    return clean_lines


def clean_instructions(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    cleaned = value.strip()
    for pattern in _noise_patterns():
        result = re.sub(pattern, "", cleaned).strip()
        if result != cleaned:
            LOGGER.info("instruction scrape-noise removal fired")
        cleaned = result
    return cleaned or None


def make_recipe(
    source: str, original_key: str, record: dict[str, Any], duplicate_group: str | None
) -> tuple[dict[str, Any], list[ParsedIngredient]]:
    title_raw = record.get("title")
    ingredients_raw = record.get("ingredients")
    instructions_raw = record.get("instructions")
    title = clean_string(title_raw)
    instructions = clean_instructions(instructions_raw)
    ingredients = ingredient_values(ingredients_raw)
    raw_lines = (
        [line for line in ingredients_raw if isinstance(line, str)]
        if isinstance(ingredients_raw, list)
        else []
    )
    # Parse the untouched source lines so ingredient_lines.raw remains auditable.
    parsed = []
    for line in raw_lines:
        item = parse_ingredient(line)
        if item.canonical:
            parsed.append(item)
    values: dict[str, Any] = {
        "recipe_id": f"{source}:{original_key}",
        "source": source,
        "original_key": original_key,
        "title": title_raw if isinstance(title_raw, str) else None,
        "title_raw": title_raw if isinstance(title_raw, str) else None,
        "title_clean": title,
        "title_dup_group": duplicate_group,
        "ingredients_raw": json.dumps(ingredients_raw, ensure_ascii=False)
        if ingredients_raw is not None
        else None,
        "instructions_raw": instructions_raw if isinstance(instructions_raw, str) else None,
        "ingredients_clean": json.dumps(ingredients, ensure_ascii=False),
        "instructions_clean": instructions,
        "step_count": count_steps(instructions),
        "sentence_count": count_sentences(instructions),
        "instructions_low_confidence": int(instructions_low_confidence(instructions)),
        "ingredient_count": len(parsed),
        "has_title": int(title is not None),
        "has_ingredients": int(bool(ingredients)),
        "has_instructions": int(instructions is not None),
    }
    return values, parsed
