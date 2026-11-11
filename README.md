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
