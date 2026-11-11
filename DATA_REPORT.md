# Recipe Box data report

Database generated from the three source JSON files. All recipe rows: **125,164**.

## Denominators and quality flags

**All recipes = 125,164**: every source record, including missing and incomplete records. **Recipes with usable ingredients = 122,971**: records with at least one nonblank ingredient line after configured scrape-noise removal. Ingredient-frequency statistics use this complete usable-ingredient subset; parsing failure does not remove a line from that denominator. Percentages in the table use each source's complete row count.

| Source | Rows | Missing title | Empty title | Missing ingredients | Empty/unusable ingredients | Missing instructions | Empty instructions | Duplicate title groups / rows |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ar | 39,802 | 280 (0.70%) | 0 (0.00%) | 280 (0.70%) | 0 (0.00%) | 280 (0.70%) | 0 (0.00%) | 441 / 910 |
| epi | 25,323 | 0 (0.00%) | 0 (0.00%) | 0 (0.00%) | 47 (0.19%) | 0 (0.00%) | 23 (0.09%) | 636 / 1,583 |
| fn | 60,039 | 289 (0.48%) | 0 (0.00%) | 237 (0.39%) | 1,629 (2.71%) | 411 (0.68%) | 0 (0.00%) | 3,931 / 11,079 |

Across sources, duplicate title group IDs: **5,008**, covering **13,572 rows**. Groups use trimmed, case-folded title equality; records are not deduplicated.

## Top 30 canonical ingredients

Frequency is the number of distinct recipes containing the canonical ingredient; the analytical base is all recipes with usable ingredients.

| Rank | Canonical ingredient | Recipes |
|---:|---|---:|
| 1 | salt | 29,615 |
| 2 | olive oil | 17,980 |
| 3 | all-purpose flour | 16,302 |
| 4 | butter | 16,200 |
| 5 | sugar | 16,004 |
| 6 | water | 13,495 |
| 7 | garlic | 13,475 |
| 8 | kosher salt | 11,384 |
| 9 | egg | 10,433 |
| 10 | unsalted butter | 10,413 |
| 11 | white sugar | 9,751 |
| 12 | vanilla extract | 9,557 |
| 13 | vegetable oil | 8,968 |
| 14 | extra-virgin olive oil | 8,464 |
| 15 | milk | 8,190 |
| 16 | baking powder | 7,727 |
| 17 | freshly ground black pepper | 7,207 |
| 18 | ground cinnamon | 7,156 |
| 19 | large egg | 6,905 |
| 20 | baking soda | 6,210 |
| 21 | heavy cream | 5,923 |
| 22 | honey | 5,445 |
| 23 | onion | 5,309 |
| 24 | fresh lemon juice | 4,987 |
| 25 | garlic clove | 4,855 |
| 26 | salt and freshly ground black pepper | 4,836 |
| 27 | ground black pepper | 4,714 |
| 28 | ground cumin | 4,327 |
| 29 | kosher salt and freshly ground black pepper | 4,325 |
| 30 | powdered sugar | 4,261 |

## Normalization rules

Ingredient quantities are extracted with the documented regex parser. Unit aliases come from `config/units.yaml`; noise patterns, prep separators, and explicit plural-to-singular mappings come from `config/cleaning.yaml`. Explicit synonym merges come only from `config/synonyms.yaml`; every plural and synonym merge logs an INFO record to `data/normalization.log` during scripted ingestion. Products such as garlic/garlic powder, butter/peanut butter, and milk/coconut milk remain separate.

Observed explicit synonym merges (ingredient lines):
- `scallion` -> `green onion`: 1,531
- `spring onion` -> `green onion`: 69
- `confectioners sugar` -> `powdered sugar`: 119
- `confectioners' sugar` -> `powdered sugar`: 2,915
- `icing sugar` -> `powdered sugar`: 27

Observed explicit plural-to-singular mappings (ingredient lines containing the source form):
- `tomatoes` -> `tomato`: 14,668
- `potatoes` -> `potato`: 8,588
- `leaves` -> `leaf`: 24,989
- `loaves` -> `loaf`: 207
- `berries` -> `berry`: 8,731
- `cherries` -> `cherry`: 1,730
- `halves` -> `half`: 3,123
- `cloves` -> `clove`: 24,437
- `limes` -> `lime`: 1,685
- `lemons` -> `lemon`: 1,992
- `onions` -> `onion`: 10,354
- `eggs` -> `egg`: 19,762
- `carrots` -> `carrot`: 6,010
- `peppers` -> `pepper`: 6,389
- `cheeses` -> `cheese`: 60
- `scallions` -> `scallion`: 4,274
- `ADVERTISEMENT` scrape-noise suffix removed from 361,287 ingredient lines.

## Source inspection

Sample source records (the reproducible inspector prints the complete sampled records):

- **ar**: `Slow Cooker Chicken and Dumplings` (key `rmK12Uau.ntP510KeImX506H6Mr6jTu`); `Awesome Slow Cooker Pot Roast` (key `5ZpZE8hSVdPk2ZXo1mZTyoPWJRSCPSm`)
- **epi**: `Christmas Eggnog ` (key `05zEpbSqcs9E0rcnCJWyZ9OgdH0MLby`); `Veal, Carrot and Chestnut Ragoût ` (key `mF5SZmoqxF4WtIlhLRvzuKk.z6s7P2S`)
- **fn**: `Grammie Hamblet's Deviled Crab` (key `p3pKOD6jIHEcjf20CCXohP8uqkG5dGi`); `Infineon Raceway Baked Beans` (key `S7aeOIrsrgT0jLP32jKGg4j.o9zi2DO`)

Instruction string layout by source (empty strings are counted as single-block strings):

| Source | Newline-separated strings | Single-block strings |
|---|---:|---:|
| ar | 39,522 | 0 |
| epi | 25,300 | 23 |
| fn | 49,541 | 10,087 |

Original keys shared across source files: **0**.

Representative noise strings found in source fields:
- **ar ingredients**: `ADVERTISEMENT` (39519); `1/2 teaspoon salt ADVERTISEMENT` (3455); `1 teaspoon vanilla extract ADVERTISEMENT` (2998)
- **epi ingredients**: `*Available at baking supply stores and www.sugarcraft.com.` (1); `1 1/2 ounces spiced rum, preferably Sailor Jerry (www.sailorjerry.com/rum)` (1); `**Genutine is a vegetable gelatin that is available online (visit www.le-sanctuaire.com).` (1)
- **epi instructions**: `1. Peel the potatoes and thickly slice into a bowl of cold water. 2. In heavy saucepan set over moderate heat, cook the ` (1); `1. Pound the lamb pieces lightly with a heavy-bladed knife to tenderize, and make shallow incisions in them. Place the l` (1); `Put the chickpeas in a large bowl and add enough cold water to cover them by at least 2 inches. Let soak overnight, then` (1)
- **fn ingredients**: `Read more at: http://www.foodnetwork.com/recipes/bobby-flay/tropical-fruit-salad-with-ginger-syrup.html?oc=linkback` (1); `2 silicone ice ball molds (available at www.muji.com)` (1); `Excerpted from "Al Roker's Big bad Book of Barbeque" Scribners 2002. Copyright 2002` (1)
- **fn instructions**: `Combine all the ingredients in a large bowl or pitcher with plenty of ice. Stir and serve!
Copyright 2010, Diageo, Norwa` (6); `©2010 Publix Super Markets, Inc.` (4); `Preheat the oven to 400 degrees F. Season the chicken with salt and pepper. Dredge in the flour and pat off the excess. ` (3)
