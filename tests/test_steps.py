from recipelens.data.steps import count_sentences, count_steps, instructions_low_confidence
from recipelens.store.models import Filter


def test_empty_and_boilerplate_instructions_count_zero() -> None:
    assert count_steps(None) == 0
    assert count_steps("") == 0
    assert count_steps("\nADVERTISEMENT\n") == 0


def test_newline_blocks_are_steps_and_empty_lines_are_ignored() -> None:
    assert count_steps("Step one.\n\nStep two.\n") == 2


def test_single_block_uses_sentence_fallback() -> None:
    assert count_steps("Preheat oven. Bake until golden. Serve warm.") == 3


def test_single_numbered_block_without_sentence_end_is_one_step() -> None:
    assert count_steps("1. Stir until smooth") == 1


def test_sentence_count_splits_sentences_inside_newline_blocks() -> None:
    text = "Step one. Continue mixing.\nStep two"
    assert count_steps(text) == 2
    assert count_sentences(text) == 3


def test_low_confidence_uses_configured_short_text_and_action_rules() -> None:
    assert instructions_low_confidence("Serve.")
    assert instructions_low_confidence("A detailed paragraph with no cooking action verb present.")
    assert not instructions_low_confidence("Bake the dish in a hot oven until it is golden brown.")


def test_family_mode_is_default_and_exact_remains_selectable() -> None:
    assert Filter().match_mode == "family"
    assert Filter(match_mode="exact").match_mode == "exact"
