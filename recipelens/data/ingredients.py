"""Simple, auditable ingredient parsing and config-driven canonicalization."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import yaml

LOGGER = logging.getLogger(__name__)
_QTY = r"(?:\d+\s+\d+\/\d+|\d+\/\d+|\d+(?:\.\d+)?|[½⅓⅔¼¾⅛⅜⅝⅞])"
_UNIT_RE = re.compile(r"^([A-Za-z.]+)\b\s*(.*)$")


@dataclass(frozen=True, slots=True)
class ParsedIngredient:
    raw: str
    qty: str | None
    unit: str | None
    name: str
    prep: str | None
    canonical: str


@lru_cache(maxsize=8)
def load_synonyms(path: Path | None = None) -> dict[str, str]:
    config_path = path or Path(__file__).resolve().parents[2] / "config" / "synonyms.yaml"
    data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    return {
        str(key).casefold(): str(value).casefold()
        for key, value in data.get("synonyms", {}).items()
    }


@lru_cache(maxsize=8)
def _config(name: str) -> dict:
    path = Path(__file__).resolve().parents[2] / "config" / name
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def parse_ingredient(raw: str, synonyms: dict[str, str] | None = None) -> ParsedIngredient:
    """Parse common quantity/unit prefixes; retain source text even when parsing is partial."""
    rules = synonyms if synonyms is not None else load_synonyms()
    text = raw.strip()
    qty_match = re.match(rf"^({_QTY})\s*(.*)$", text)
    qty = qty_match.group(1) if qty_match else None
    remainder = qty_match.group(2).strip() if qty_match else text
    cleaning = _config("cleaning.yaml")
    for pattern in cleaning.get("noise_patterns", []):
        remainder = re.sub(pattern, "", remainder).strip()
    unit = None
    unit_match = _UNIT_RE.match(remainder)
    units = _config("units.yaml").get("units", {})
    normalized_units = {str(k).casefold(): str(v).casefold() for k, v in units.items()}
    if unit_match and unit_match.group(1).rstrip(".").casefold() in normalized_units:
        token = unit_match.group(1).rstrip(".").casefold()
        unit = normalized_units[token]
        remainder = unit_match.group(2).strip()
    # A leading parenthetical brand/size is often not part of the food name.
    remainder = re.sub(r"^\([^)]*\)\s*", "", remainder)
    prep_pattern = cleaning.get("prep_pattern", r"\s*,\s*(?=to taste\b)")
    parts = re.split(prep_pattern, remainder, maxsplit=1, flags=re.IGNORECASE)
    name = parts[0].strip(" ,.").casefold()
    prep = parts[1].strip(" ,.") if len(parts) > 1 else None
    plurals = {
        str(k).casefold(): str(v).casefold() for k, v in cleaning.get("plural_singular", {}).items()
    }
    if name in plurals:
        normalized_name = plurals[name]
        LOGGER.info("ingredient plural normalization fired: %r -> %r", name, normalized_name)
        name = normalized_name
    elif " " in name:
        words = name.rsplit(" ", maxsplit=1)
        singular = plurals.get(words[1], words[1])
        if singular != words[1]:
            LOGGER.info("ingredient plural normalization fired: %r -> %r", words[1], singular)
        name = f"{words[0]} {singular}"
    canonical = rules.get(name, name)
    if canonical != name:
        LOGGER.info("ingredient normalization fired: %r -> %r", name, canonical)
    return ParsedIngredient(raw=raw, qty=qty, unit=unit, name=name, prep=prep, canonical=canonical)
