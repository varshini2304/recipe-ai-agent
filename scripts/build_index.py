"""Build a resumable, batched title-plus-ingredients embedding index."""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
import time
from pathlib import Path

import numpy as np
import yaml
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.prepare_search import prepare_fts

DB_PATH = ROOT / "data" / "recipelens.sqlite3"
CONFIG_PATH = ROOT / "config" / "store.yaml"


def _read_corpus(db_path: Path, limit: int | None) -> tuple[list[str], list[str], str, int]:
    connection = sqlite3.connect(db_path)
    full_count = connection.execute(
        "SELECT COUNT(*) FROM recipes WHERE has_title=1 AND has_ingredients=1"
    ).fetchone()[0]
    if limit is not None:
        sql = (
            "SELECT recipe_id, title_clean, ingredients_text FROM ("
            "SELECT r.recipe_id, r.title_clean, r.source, r.original_key, "
            "COALESCE((SELECT group_concat(il.canonical, ' ') FROM ingredient_lines il "
            "WHERE il.recipe_id=r.recipe_id), '') AS ingredients_text, "
            "ROW_NUMBER() OVER (PARTITION BY r.source ORDER BY r.original_key) AS source_position "
            "FROM recipes r WHERE r.has_title=1 AND r.has_ingredients=1) "
            "ORDER BY source_position, source LIMIT ?"
        )
        rows = connection.execute(sql, (limit,)).fetchall()
    else:
        sql = (
            "SELECT r.recipe_id, r.title_clean, "
            "COALESCE((SELECT group_concat(il.canonical, ' ') FROM ingredient_lines il "
            "WHERE il.recipe_id=r.recipe_id), '') "
            "FROM recipes r WHERE r.has_title=1 AND r.has_ingredients=1 "
            "ORDER BY r.source, r.original_key"
        )
        rows = connection.execute(sql).fetchall()
    connection.close()
    ids = [row[0] for row in rows]
    texts = [f"{row[1]}\nIngredients: {row[2]}" for row in rows]
    digest = hashlib.sha256()
    for recipe_id, text in zip(ids, texts):
        digest.update(recipe_id.encode())
        digest.update(b"\0")
        digest.update(text.encode("utf-8"))
        digest.update(b"\n")
    return ids, texts, digest.hexdigest(), full_count


def build_index(
    *,
    limit: int | None = None,
    batch_size: int | None = None,
    resume: bool = True,
    db_path: Path = DB_PATH,
    config_path: Path = CONFIG_PATH,
) -> dict[str, float | int | str]:
    started = time.perf_counter()
    config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    model_name = config["embedding_model"]
    backend = config.get("vector_backend", "numpy")
    if backend not in {"numpy", "faiss"}:
        raise ValueError(f"Unsupported vector backend {backend!r}")
    if backend == "faiss":
        try:
            import faiss
        except ImportError as error:
            raise RuntimeError(
                "config selects faiss, but importing faiss is blocked or unavailable"
            ) from error
    batch = batch_size or int(config["embedding_batch_size"])
    dtype_name = str(config.get("embedding_dtype", "float32"))
    if dtype_name not in {"float32", "float16"}:
        raise ValueError("embedding_dtype must be either float32 or float16")
    dtype = np.float16 if dtype_name == "float16" else np.float32
    root = config_path.resolve().parents[1]
    index_dir = root / config["index_dir"]
    index_dir.mkdir(parents=True, exist_ok=True)
    ids, texts, corpus_signature, full_count = _read_corpus(db_path, limit)
    if not ids:
        raise ValueError("No recipes meet both has_title and has_ingredients search quality flags.")
    prepare_fts(db_path)
    model = SentenceTransformer(model_name, local_files_only=True)
    dimension = int(model.get_embedding_dimension())
    checkpoint_vectors = index_dir / "vectors.checkpoint.npy"
    checkpoint_meta = index_dir / "checkpoint.json"
    completed = 0
    base_elapsed = 0.0
    if resume and checkpoint_vectors.exists() and checkpoint_meta.exists():
        saved = json.loads(checkpoint_meta.read_text(encoding="utf-8"))
        if (
            saved.get("signature") == corpus_signature
            and saved.get("model") == model_name
            and saved.get("dimension") == dimension
            and saved.get("dtype") == dtype_name
            and saved.get("total") == len(ids)
        ):
            completed = min(int(saved.get("completed", 0)), len(ids))
            base_elapsed = float(saved.get("elapsed_seconds", 0.0))
    if completed:
        matrix = np.load(checkpoint_vectors, mmap_mode="r+")
    else:
        matrix = np.lib.format.open_memmap(
            checkpoint_vectors, mode="w+", dtype=dtype, shape=(len(ids), dimension)
        )
    batches_since_save = 0
    last_saved = completed
    checkpoint_interval = int(config.get("checkpoint_every_batches", 5))
    progress = tqdm(total=len(ids), initial=completed, desc="Embedding recipes")
    try:
        for start in range(completed, len(ids), batch):
            end = min(start + batch, len(ids))
            vectors = model.encode(
                texts[start:end],
                batch_size=batch,
                show_progress_bar=False,
                normalize_embeddings=True,
                convert_to_numpy=True,
            )
            matrix[start:end] = np.asarray(vectors, dtype=dtype)
            progress.update(end - start)
            batches_since_save += 1
            if batches_since_save >= checkpoint_interval or end == len(ids):
                matrix.flush()
                state = {
                    "signature": corpus_signature,
                    "model": model_name,
                    "dimension": dimension,
                    "dtype": dtype_name,
                    "total": len(ids),
                    "completed": end,
                    "elapsed_seconds": base_elapsed + time.perf_counter() - started,
                }
                temporary_meta = checkpoint_meta.with_suffix(".json.tmp")
                temporary_meta.write_text(json.dumps(state, indent=2), encoding="utf-8")
                temporary_meta.replace(checkpoint_meta)
                last_saved = end
                batches_since_save = 0
    except KeyboardInterrupt:
        matrix.flush()
        state = {
            "signature": corpus_signature,
            "model": model_name,
            "dimension": dimension,
            "dtype": dtype_name,
            "total": len(ids),
            "completed": last_saved,
            "elapsed_seconds": base_elapsed + time.perf_counter() - started,
        }
        temporary_meta = checkpoint_meta.with_suffix(".json.tmp")
        temporary_meta.write_text(json.dumps(state, indent=2), encoding="utf-8")
        temporary_meta.replace(checkpoint_meta)
        raise
    finally:
        progress.close()
    matrix.flush()
    del matrix
    final_matrix = index_dir / "vectors.npy"
    checkpoint_vectors.replace(final_matrix)
    (index_dir / "ids.json").write_text(json.dumps(ids), encoding="utf-8")
    elapsed = base_elapsed + time.perf_counter() - started
    metadata = {
        "embedding_model": model_name,
        "dimension": dimension,
        "dtype": dtype_name,
        "indexed_rows": len(ids),
        "searchable_rows_full": full_count,
        "corpus_signature": corpus_signature,
        "elapsed_seconds": elapsed,
        "subset_limit": limit,
    }
    (index_dir / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    (index_dir / "checkpoint.json").unlink(missing_ok=True)
    (index_dir / "ids.checkpoint.json").unlink(missing_ok=True)
    if backend == "faiss":
        try:
            import faiss
        except ImportError as error:
            raise RuntimeError(
                "config selects faiss, but importing faiss is blocked or unavailable"
            ) from error
        faiss_index = faiss.IndexFlatIP(dimension)
        vectors = np.asarray(np.load(final_matrix, mmap_mode="r"), dtype=np.float32)
        faiss_index.add(vectors)
        faiss.write_index(faiss_index, str(index_dir / "vectors.faiss"))
    estimated = elapsed * full_count / len(ids)
    result = {
        "indexed_rows": len(ids),
        "searchable_rows_full": full_count,
        "elapsed_seconds": elapsed,
        "full_build_estimate_seconds": estimated,
        "model": model_name,
        "backend": backend,
        "matrix": str(final_matrix),
    }
    print(json.dumps(result, indent=2))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--limit", type=int, default=None, help="Build a deterministic development subset."
    )
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument(
        "--no-resume", action="store_true", help="Ignore checkpoint data and start from row zero."
    )
    args = parser.parse_args()
    if args.limit is not None and args.limit <= 0:
        parser.error("--limit must be greater than zero")
    build_index(limit=args.limit, batch_size=args.batch_size, resume=not args.no_resume)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
