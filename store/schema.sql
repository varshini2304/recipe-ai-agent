PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS recipes (
    recipe_id TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    original_key TEXT NOT NULL,
    title TEXT,
    title_raw TEXT,
    title_clean TEXT,
    title_dup_group TEXT,
    ingredients_raw TEXT,
    instructions_raw TEXT,
    ingredients_clean TEXT NOT NULL,
    instructions_clean TEXT,
    step_count INTEGER NOT NULL,
    sentence_count INTEGER NOT NULL,
    instructions_low_confidence INTEGER NOT NULL CHECK (instructions_low_confidence IN (0, 1)),
    ingredient_count INTEGER NOT NULL,
    has_title INTEGER NOT NULL CHECK (has_title IN (0, 1)),
    has_ingredients INTEGER NOT NULL CHECK (has_ingredients IN (0, 1)),
    has_instructions INTEGER NOT NULL CHECK (has_instructions IN (0, 1)),
    UNIQUE(source, original_key)
);

CREATE TABLE IF NOT EXISTS ingredient_lines (
    recipe_id TEXT NOT NULL REFERENCES recipes(recipe_id) ON DELETE CASCADE,
    position INTEGER NOT NULL,
    raw TEXT NOT NULL,
    canonical TEXT NOT NULL,
    qty TEXT,
    unit TEXT,
    name TEXT NOT NULL,
    prep TEXT,
    PRIMARY KEY(recipe_id, position)
);

CREATE INDEX IF NOT EXISTS idx_recipes_source ON recipes(source);
CREATE INDEX IF NOT EXISTS idx_recipes_title_dup_group ON recipes(title_dup_group);
CREATE INDEX IF NOT EXISTS idx_recipes_step_count ON recipes(step_count);
CREATE INDEX IF NOT EXISTS idx_ingredient_lines_canonical ON ingredient_lines(canonical);
CREATE INDEX IF NOT EXISTS idx_ingredient_lines_recipe ON ingredient_lines(recipe_id);

-- Search text is rebuilt by scripts/prepare_search.py from title + canonical ingredients.
CREATE VIRTUAL TABLE IF NOT EXISTS recipe_fts USING fts5(
    recipe_id UNINDEXED,
    title,
    ingredients,
    tokenize='unicode61'
);
