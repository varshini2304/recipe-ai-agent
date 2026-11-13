# RecipeLens

Conversational recipe chatbot and deterministic culinary intelligence over the Recipe Box dataset (125,164 recipes).

## Dataset

The raw recipe datasets are not tracked in this repository to keep repository size lean and reproducible.

The dataset originates from the [Recipe Box dataset](https://eightportions.com/datasets/Recipes/) by Ryan Lee, distributed under the Open Database License (ODbL) / Database Contents License (DbCL) (see `data_raw/LICENSE` when downloaded).

To automatically download and extract the dataset:
```bash
python scripts/download_data.py
```

Alternatively, download `recipes_raw.zip` from [eightportions.com](https://eightportions.com/datasets/Recipes/) and place the three JSON files into `data_raw/`:
- `recipes_raw_nosource_ar.json` (Allrecipes: 39,802 records)
- `recipes_raw_nosource_epi.json` (Epicurious: 25,323 records)
- `recipes_raw_nosource_fn.json` (Food Network: 60,039 records)

To run data ingestion and build the SQLite database and search index:
```bash
python scripts/ingest.py
python scripts/build_index.py
```

## Substitution evidence (Task 3)

Substitution suggestions compare ingredient frequencies in same-dish peers. Evidence grades are
computed from the configured peer support, frequency difference, and lift thresholds in
`config/substitution.yaml`. The output always reports peer counts and supporting recipe IDs. A
candidate is an observed association, not a validated recipe adaptation; amounts and method
changes are not inferred, and the response makes no medical-safety claim. Optional external search
is disabled.

The current local index has 122,971 rows and uses hybrid FTS5 plus vector retrieval for substitution
peers. Its recorded build took 3,622 seconds (about 60 minutes). Index files and raw data are
ignored by Git. On a fresh clone, they must be downloaded/ingested and built locally. Until the
vector index covers the complete searchable corpus, substitution peer lookup uses FTS5 across the
SQLite corpus only, and the response labels that retrieval mode explicitly.

Regenerate the Task 3 conversations with `python scripts/generate_substitution_demos.py`; this
replays the scripts under `scripts/demo_scripts/` and appends the resulting live output to
`docs/DEMO_CONVERSATIONS.md`.
