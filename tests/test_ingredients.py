from recipelens.data.ingredients import parse_ingredient


def test_quantity_unit_and_prep_parsing() -> None:
    parsed = parse_ingredient("1 1/2 tablespoons scallions, finely chopped ADVERTISEMENT")
    assert parsed.qty == "1 1/2"
    assert parsed.unit == "tablespoon"
    assert parsed.name == "scallion"
    assert parsed.canonical == "green onion"
    assert parsed.prep == "finely chopped"


def test_explicit_plural_rule_and_products_remain_distinct() -> None:
    assert parse_ingredient("2 tomatoes").canonical == "tomato"
    assert parse_ingredient("garlic").canonical == "garlic"
    assert parse_ingredient("garlic powder").canonical == "garlic powder"
    assert parse_ingredient("butter").canonical == "butter"
    assert parse_ingredient("peanut butter").canonical == "peanut butter"
    assert parse_ingredient("milk").canonical == "milk"
    assert parse_ingredient("coconut milk").canonical == "coconut milk"


def test_source_text_is_kept_in_parsed_result() -> None:
    raw = "1 cup cilantro ADVERTISEMENT"
    assert parse_ingredient(raw).raw == raw
