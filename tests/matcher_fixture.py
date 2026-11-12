"""SYNTHETIC fixture database for matcher tests.

These ~15 recipes are hand-written to exercise specific matcher behaviours. They are NOT part of the
Recipe Box dataset and must never be quoted as real data. Ingredient lines go through the real
ingestion parser, and instruction metrics through the real step counter.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from recipelens.data.ingredients import parse_ingredient
from recipelens.data.steps import count_sentences, count_steps, instructions_low_confidence

ROOT = Path(__file__).resolve().parents[1]

RECIPES: dict[str, tuple[str, list[str], str]] = {
    "syn:tomato-rice": (
        "Tomato Rice",
        ["2 cups cooked rice", "3 tomatoes", "1 onion, chopped", "2 tablespoons olive oil", "salt to taste"],
        "Chop the onion.\nHeat the oil and cook the onion.\nAdd tomatoes and simmer.\nStir in the rice and serve.",
    ),
    "syn:egg-fried-rice": (
        "Egg Fried Rice",
        ["3 large eggs", "2 cups cooked rice", "1 onion", "2 tablespoons vegetable oil", "1 tablespoon soy sauce"],
        "Beat the eggs.\nHeat the oil and fry the onion.\nAdd the rice and soy sauce.\nPour in the eggs and stir.\nServe hot.",
    ),
    "syn:shakshuka": (
        "Shakshuka",
        ["4 eggs", "4 tomatoes", "1 onion, chopped", "2 cloves garlic, minced", "1 teaspoon cumin", "salt"],
        "Cook the onion and garlic.\nAdd tomatoes and cumin and simmer.\nCrack the eggs into the sauce.\nCover and cook until set.\nServe.",
    ),
    "syn:peanut-noodles": (
        "Peanut Noodles",
        ["1/2 cup peanut butter", "8 ounces noodles", "2 tablespoons soy sauce", "1 onion"],
        "Boil the noodles.\nWhisk the peanut butter and soy sauce.\nToss together and serve.",
    ),
    "syn:slow-braise": (
        "Slow Braise",
        ["4 eggs", "2 tomatoes", "2 onions", "1 cup rice", "1 pound beef"],
        "Chop the onions.\nBrown the beef.\nAdd the onions.\nAdd the tomatoes.\nCover with water.\nSimmer for an hour.\nAdd the rice.\nSimmer again.\nBeat in the eggs.\nServe.",
    ),
    "syn:tomato-cream-soup": (
        "Tomato Cream Soup",
        ["4 tomatoes", "1 onion", "1 cup heavy cream", "2 tablespoons butter"],
        "Melt the butter and cook the onion.\nAdd the tomatoes and simmer.\nBlend and stir in the cream.\nServe warm.",
    ),
    "syn:mushroom-casserole": (
        "Mushroom Rice Casserole",
        ["1 can cream of mushroom soup", "1 cup rice", "1 onion"],
        "Mix everything in a dish.\nBake for 40 minutes.\nServe.",
    ),
    "syn:plain-rice": (
        "Plain Rice",
        ["1 cup rice", "2 cups water", "salt"],
        "Bring the water to a boil. Add the rice and simmer for 15 minutes.",
    ),
    "syn:garlic-rub": (
        "Garlic Rub",
        ["2 tablespoons garlic powder", "1 teaspoon salt", "1 teaspoon paprika"],
        "Mix the spices.\nRub onto the meat.\nRoast.",
    ),
    "syn:no-instructions": (
        "Mystery Egg Tomato Dish",
        ["2 eggs", "2 tomatoes"],
        "",
    ),
    "syn:terse": (
        "Terse Egg Tomato",
        ["2 eggs", "2 tomatoes"],
        "Mix.",
    ),
    "syn:omelette": (
        "Everything Omelette",
        ["1 large egg", "1 tomato", "1/2 onion", "1 cup rice", "salt", "pepper", "1 tablespoon parsley, optional"],
        "Beat the egg.\nCook the onion and tomato.\nAdd the rice.\nPour in the egg.\nFold and serve.",
    ),
    "syn:eggplant": (
        "Eggplant Bake",
        ["1 eggplant", "1 cup shredded cheese", "1 onion"],
        "Slice the eggplant.\nLayer with cheese.\nBake until golden.",
    ),
    "syn:noisy": (
        "Noisy Rice",
        ["1 cup rice ADVERTISEMENT", "1 cup spinach ADVERTISEMENT", "1 tablespoon olive oil ADVERTISEMENT"],
        "Cook the rice.\nWilt the spinach.\nStir together and serve.",
    ),
    "syn:pasta-sauce": (
        "Pasta with Tomato Sauce",
        ["1 cup tomato sauce", "8 ounces pasta", "1 onion"],
        "Boil the pasta.\nHeat the sauce.\nCombine and serve.",
    ),
}


def build_fixture_db(path: Path) -> Path:
    connection = sqlite3.connect(path)
    connection.executescript((ROOT / "store" / "schema.sql").read_text(encoding="utf-8"))
    for recipe_id, (title, ingredients, instructions) in RECIPES.items():
        parsed = [parse_ingredient(line) for line in ingredients]
        connection.execute(
            "INSERT INTO recipes (recipe_id, source, original_key, title, title_raw, title_clean, "
            "title_dup_group, ingredients_raw, instructions_raw, ingredients_clean, instructions_clean, "
            "step_count, sentence_count, instructions_low_confidence, ingredient_count, "
            "has_title, has_ingredients, has_instructions) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                recipe_id, "syn", recipe_id.split(":")[1], title, title, title, None,
                json.dumps(ingredients), instructions, json.dumps(ingredients), instructions,
                count_steps(instructions), count_sentences(instructions),
                int(instructions_low_confidence(instructions)), len(ingredients),
                1, 1, int(bool(instructions.strip())),
            ),
        )  # fmt: skip
        connection.executemany(
            "INSERT INTO ingredient_lines(recipe_id, position, raw, canonical, qty, unit, name, prep) "
            "VALUES (?,?,?,?,?,?,?,?)",
            [
                (recipe_id, i, x.raw, x.canonical, x.qty, x.unit, x.name, x.prep)
                for i, x in enumerate(parsed)
            ],
        )
    connection.commit()
    connection.close()
    return path
