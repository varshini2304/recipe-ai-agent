# Store

SQLite schema and database artifacts for RecipeLens.

## Vector index

`config/store.yaml` selects the vector backend. The default is the exact NumPy cosine
backend; it reads an L2-normalized float32 matrix via memory mapping and ranks only
the recipe IDs that pass structured filters. Optional FAISS uses inner product on the
same normalized vectors and only loads when `import faiss` succeeds.

The matrix, ID map, and metadata are written to `data/index/`. The index text is the
original title followed by canonical ingredients. `scripts/build_index.py` batches
embeddings and writes resumable checkpoints every configured number of batches.
Run `python scripts/build_index.py --limit N` for a deterministic development subset.

On this machine, the final stratified 5,000-row MiniLM build took 159.17 seconds.
Linear extrapolation to 122,971 searchable recipes is about 3,915 seconds (65 minutes).
This is a CPU/machine-specific estimate. The full build awaits the user's decision.
