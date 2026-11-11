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


def test_ingredient_families_product_and_green_onion_rules() -> None:
    from unittest.mock import MagicMock

    from recipelens.services.ingredient_families import IngredientFamilies

    mock_repo = MagicMock()
    mock_repo.canonical_counts.return_value = [
        ("tomato", 100),
        ("diced tomato", 50),
        ("can tomato sauce", 30),
        ("tomato paste", 20),
        ("garlic", 80),
        ("garlic clove", 40),
        ("garlic powder", 25),
        ("onion", 90),
        ("chopped onion", 45),
        ("green onion", 60),
        ("chopped green onion", 30),
    ]
    families = IngredientFamilies(mock_repo)
    tomato_vars = families.variants("tomato")
    assert "tomato" in tomato_vars
    assert "diced tomato" in tomato_vars
    assert "can tomato sauce" not in tomato_vars
    assert "tomato paste" not in tomato_vars

    sauce_vars = families.variants("tomato sauce")
    assert "can tomato sauce" in sauce_vars

    garlic_vars = families.variants("garlic")
    assert "garlic" in garlic_vars
    assert "garlic powder" not in garlic_vars

    powder_vars = families.variants("garlic powder")
    assert "garlic powder" in powder_vars

    onion_vars = families.variants("onion")
    assert "onion" in onion_vars
    assert "green onion" not in onion_vars
    assert "chopped green onion" not in onion_vars

    green_vars = families.variants("green onion")
    assert "green onion" in green_vars
    assert "chopped green onion" in green_vars
    assert "onion" not in green_vars
