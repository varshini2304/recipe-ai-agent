"""Reproducibly inspect source shape, completeness, duplicates, and text noise."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data_raw"
SOURCES = ("ar", "epi", "fn")


def inspect() -> dict[str, Any]:
    source_keys: dict[str, set[str]] = {}
    result: dict[str, Any] = {}
    noise_pattern = re.compile(r"advertisement|\bhttps?://|\bwww\.|©|\bcopyright\b", re.IGNORECASE)
    for source in SOURCES:
        path = RAW / f"recipes_raw_nosource_{source}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise TypeError(f"Expected a top-level object in {path.name}")
        source_keys[source] = set(data)
        missing = Counter()
        empty = Counter()
        duplicates = Counter()
        ingredient_noise: Counter[str] = Counter()
        instruction_noise: Counter[str] = Counter()
        instruction_types = Counter()
        examples = []
        for key, record in data.items():
            if not isinstance(record, dict):
                continue
            if len(examples) < 2:
                examples.append({"key": key, **record})
            for field in ("title", "ingredients", "instructions"):
                value = record.get(field)
                if field not in record or value is None:
                    missing[field] += 1
                elif (
                    isinstance(value, str)
                    and not value.strip()
                    or isinstance(value, list)
                    and not any(isinstance(item, str) and item.strip() for item in value)
                ):
                    empty[field] += 1
            title = record.get("title")
            if isinstance(title, str) and title.strip():
                duplicates[title.strip().casefold()] += 1
            instructions = record.get("instructions")
            if isinstance(instructions, str):
                instruction_types[
                    "newline-separated" if "\n" in instructions else "single-block"
                ] += 1
            elif instructions is not None:
                instruction_types[type(instructions).__name__] += 1
            for field, counter in (
                ("ingredients", ingredient_noise),
                ("instructions", instruction_noise),
            ):
                value = record.get(field)
                chunks = value if isinstance(value, list) else [value]
                for chunk in chunks:
                    if isinstance(chunk, str) and noise_pattern.search(chunk):
                        counter[chunk.strip()[:160]] += 1
        result[source] = {
            "count": len(data),
            "top_level_type": type(data).__name__,
            "fields": sorted(
                {field for row in data.values() if isinstance(row, dict) for field in row}
            ),
            "sample_records": examples,
            "missing": dict(missing),
            "empty": dict(empty),
            "duplicate_title_groups": sum(count > 1 for count in duplicates.values()),
            "records_in_duplicate_title_groups": sum(
                count for count in duplicates.values() if count > 1
            ),
            "instruction_formats": dict(instruction_types),
            "ingredient_noise": ingredient_noise.most_common(10),
            "instruction_noise": instruction_noise.most_common(10),
        }
    seen: dict[str, list[str]] = {}
    for source, keys in source_keys.items():
        for key in keys:
            seen.setdefault(key, []).append(source)
    collisions = {key: sources for key, sources in seen.items() if len(sources) > 1}
    result["cross_source_key_collisions"] = {
        "count": len(collisions),
        "examples": list(collisions.items())[:20],
    }
    return result


if __name__ == "__main__":
    print(json.dumps(inspect(), indent=2, ensure_ascii=False))
