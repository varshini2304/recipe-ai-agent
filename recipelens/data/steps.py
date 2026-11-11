"""Deterministic instruction metrics and a config-driven confidence heuristic."""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

import yaml

CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "steps.yaml"


@lru_cache(maxsize=1)
def _patterns() -> tuple[
    tuple[re.Pattern[str], ...], re.Pattern[str], tuple[re.Pattern[str], ...], int, int
]:
    config = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    boilerplate = tuple(
        re.compile(pattern, re.IGNORECASE) for pattern in config["boilerplate_patterns"]
    )
    sentence_boundary = re.compile(config["sentence_boundary_pattern"])
    confidence = config["low_confidence"]
    action_patterns = tuple(
        re.compile(pattern, re.IGNORECASE) for pattern in confidence["action_patterns"]
    )
    minimum_characters = int(confidence["minimum_characters"])
    minimum_action_matches = int(confidence["minimum_action_matches"])
    return (
        boilerplate,
        sentence_boundary,
        action_patterns,
        minimum_characters,
        minimum_action_matches,
    )


def _instruction_blocks(instructions: str | None) -> list[str]:
    if not instructions:
        return []
    boilerplate, _sentence_boundary, _actions, _minimum, _minimum_actions = _patterns()
    return [
        line.strip()
        for line in instructions.splitlines()
        if line.strip() and not any(pattern.fullmatch(line.strip()) for pattern in boilerplate)
    ]


def _sentence_parts(block: str) -> list[str]:
    _boilerplate, sentence_boundary, _actions, _minimum, _minimum_actions = _patterns()
    text = re.sub(r"^\s*\d+[.)]\s*", "", block)
    return [part for part in sentence_boundary.split(text) if part.strip()]


def count_steps(instructions: str | None) -> int:
    """Count newline blocks, dropping empty/boilerplate lines; split sentences only for one block."""
    blocks = _instruction_blocks(instructions)
    if not blocks:
        return 0
    if len(blocks) > 1:
        return len(blocks)
    return len(_sentence_parts(blocks[0]))


def count_sentences(instructions: str | None) -> int:
    """Count sentence-like units per nonempty line using the configured punctuation boundary.

    A line without sentence-ending punctuation still counts as one unit. This intentionally
    differs from `step_count` for multi-line recipes where a line may contain several sentences.
    """
    return sum(len(_sentence_parts(block)) for block in _instruction_blocks(instructions))


def instructions_low_confidence(instructions: str | None) -> bool:
    """Flag short or action-word-free text; thresholds and verb-like patterns live in YAML."""
    blocks = _instruction_blocks(instructions)
    text = " ".join(blocks)
    _boilerplate, _sentence_boundary, actions, minimum_characters, minimum_action_matches = (
        _patterns()
    )
    if len(text) < minimum_characters:
        return True
    action_matches = sum(len(pattern.findall(text)) for pattern in actions)
    return action_matches < minimum_action_matches
