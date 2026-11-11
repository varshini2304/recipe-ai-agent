"""Audit canonicals of the form <name>, <prep> skipped by family head patterns."""

from __future__ import annotations

import re
import sqlite3
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "recipelens.sqlite3"

from recipelens.services.ingredient_families import IngredientFamilies
from recipelens.store.repository import RecipeRepository

repo = RecipeRepository(DB_PATH)
families = IngredientFamilies(repo)

terms = ["tomato", "garlic", "onion", "green onion"]

conn = sqlite3.connect(DB_PATH)
# Get counts per canonical
cursor = conn.cursor()
rows = cursor.execute(
    "SELECT canonical, COUNT(DISTINCT recipe_id) AS n_recipes FROM ingredient_lines GROUP BY canonical"
).fetchall()
conn.close()

for term in terms:
    matched_variants = set(families.variants(term))
    includes, excludes = families.rules[term]
    
    # We look for canonicals containing a comma
    # where the head before comma names the ingredient (e.g. 'tomato, ...', 'onion, ...')
    # but that canonical is NOT in matched_variants.
    skipped_comma_prep = []
    
    term_pattern = re.compile(rf"\b{term}s?\b", re.IGNORECASE)
    
    for canonical, n_recipes in rows:
        if "," in canonical and canonical not in matched_variants:
            head = canonical.split(",", 1)[0].strip()
            # If the head names the term
            if term_pattern.search(head):
                # Check if it was skipped due to an intentional exclusion pattern
                hit_exclusions = [p.pattern for p in excludes if p.search(canonical)]
                head_matched = any(p.search(head) for p in includes)
                skipped_comma_prep.append({
                    "canonical": canonical,
                    "recipes": n_recipes,
                    "head": head,
                    "head_matched": head_matched,
                    "exclusions": hit_exclusions,
                })
                
    # Separate into:
    # A) skipped because exclusions matched (e.g. tomato sauce, garlic powder, green onion in onion)
    # B) skipped because head pattern failed to match (e.g. head patterns were too strict)
    head_misses = [x for x in skipped_comma_prep if not x["exclusions"] and not x["head_matched"]]
    
    print(f"\n==========================================")
    print(f"FAMILY: {term.upper()}")
    print(f"Total comma canonicals skipped: {len(skipped_comma_prep)}")
    print(f"Head misses (truly missed by head pattern): {len(head_misses)} canonicals, {sum(x['recipes'] for x in head_misses)} recipes")
    print(f"Top 20 head misses:")
    head_misses.sort(key=lambda x: -x["recipes"])
    for x in head_misses[:20]:
        print(f"  - canonical: {x['canonical']!r} (recipes: {x['recipes']}) | head: {x['head']!r}")


