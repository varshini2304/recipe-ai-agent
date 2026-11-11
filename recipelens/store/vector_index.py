"""Persistent cosine vector search with a pure NumPy default and optional FAISS."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Protocol

import numpy as np
import yaml
from sentence_transformers import SentenceTransformer

from recipelens.store.models import VectorMatch

ROOT = Path(__file__).resolve().parents[2]
STORE_CONFIG = ROOT / "config" / "store.yaml"


class VectorIndex(Protocol):
    """Search an embedding matrix over a caller-supplied already-filtered ID set."""

    model_name: str
    ids: list[str]
    indexed_rows: int
    searchable_rows_full: int

    def encode_query(self, text: str) -> np.ndarray: ...

    def search(
        self, query_vector: np.ndarray, allowed_ids: list[str], top_k: int
    ) -> list[VectorMatch]: ...


class _PersistentIndex:
    def __init__(self, index_dir: Path) -> None:
        self.index_dir = index_dir
        metadata = json.loads((index_dir / "metadata.json").read_text(encoding="utf-8"))
        self.model_name = metadata["embedding_model"]
        self.indexed_rows = int(metadata["indexed_rows"])
        self.searchable_rows_full = int(metadata["searchable_rows_full"])
        self.ids = json.loads((index_dir / "ids.json").read_text(encoding="utf-8"))
        self.positions = {recipe_id: i for i, recipe_id in enumerate(self.ids)}
        self.matrix = np.load(index_dir / "vectors.npy", mmap_mode="r")
        self._model: SentenceTransformer | None = None

    def encode_query(self, text: str) -> np.ndarray:
        if self._model is None:
            self._model = SentenceTransformer(self.model_name, local_files_only=True)
        vector = self._model.encode([text], normalize_embeddings=True, convert_to_numpy=True)
        return np.asarray(vector[0], dtype=np.float32)


class NumpyVectorIndex(_PersistentIndex):
    """L2-normalized matrix search; filtered vectors are scored before top-k selection."""

    def search(
        self, query_vector: np.ndarray, allowed_ids: list[str], top_k: int
    ) -> list[VectorMatch]:
        pairs = [
            (self.positions[recipe_id], recipe_id)
            for recipe_id in allowed_ids
            if recipe_id in self.positions
        ]
        if not pairs or top_k <= 0:
            return []
        positions = np.fromiter((pair[0] for pair in pairs), dtype=np.int64, count=len(pairs))
        vectors = np.asarray(self.matrix[positions], dtype=np.float32)
        query = np.asarray(query_vector, dtype=np.float32)
        scores = np.clip(vectors @ query, -1.0, 1.0)
        take = min(top_k, len(scores))
        selected = np.argpartition(scores, len(scores) - take)[-take:]
        selected = selected[np.argsort(scores[selected])[::-1]]
        return [VectorMatch(pairs[i][1], float(scores[i])) for i in selected]


class FaissVectorIndex(_PersistentIndex):
    """Optional exact inner-product index; the allowed subset is scored before ranking."""

    def __init__(self, index_dir: Path) -> None:
        super().__init__(index_dir)
        try:
            import faiss
        except ImportError as error:
            raise RuntimeError(
                "FAISS backend requested, but importing faiss is unavailable on this machine"
            ) from error
        faiss_file = index_dir / "vectors.faiss"
        if not faiss_file.exists():
            raise FileNotFoundError(
                f"FAISS index not found: {faiss_file}; rebuild with vector_backend: faiss"
            )
        self._faiss = faiss
        self.faiss_index = faiss.read_index(str(faiss_file))

    def search(
        self, query_vector: np.ndarray, allowed_ids: list[str], top_k: int
    ) -> list[VectorMatch]:
        pairs = [
            (self.positions[recipe_id], recipe_id)
            for recipe_id in allowed_ids
            if recipe_id in self.positions
        ]
        if not pairs or top_k <= 0:
            return []
        query = np.asarray(query_vector, dtype=np.float32)[None, :]
        using_persisted_index = len(pairs) == len(self.ids)
        if using_persisted_index:
            index = self.faiss_index
        else:
            positions = np.fromiter((pair[0] for pair in pairs), dtype=np.int64, count=len(pairs))
            vectors = np.asarray(self.matrix[positions], dtype=np.float32)
            index = self._faiss.IndexFlatIP(vectors.shape[1])
            index.add(vectors)
        scores, rows = index.search(query, min(top_k, len(pairs)))
        return [
            VectorMatch(
                self.ids[int(i)] if using_persisted_index else pairs[int(i)][1], float(score)
            )
            for score, i in zip(scores[0], rows[0])
            if i >= 0
        ]


def read_store_config(path: Path = STORE_CONFIG) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_vector_index(config_path: Path = STORE_CONFIG) -> VectorIndex:
    config = read_store_config(config_path)
    index_dir = ROOT / config["index_dir"]
    backend = config.get("vector_backend", "numpy")
    if backend == "numpy":
        return NumpyVectorIndex(index_dir)
    if backend == "faiss":
        try:
            import faiss  # noqa: F401
        except ImportError as error:
            raise RuntimeError("FAISS backend selected, but `import faiss` failed") from error
        return FaissVectorIndex(index_dir)
    raise ValueError(f"Unsupported vector backend {backend!r}; expected 'numpy' or 'faiss'.")
