"""Precompute frozen Qwen3-Embedding-8B vectors for tossups and bonuses.

This is the one-time embedding step 'train_pyramidal.py'/'train_compositional.py'
read from disk (they never call the embedding model themselves) -- the same role
'run_lda.py'/'run_plda.py' play for the topic variant's fixed 'r' vectors, just
with a neural text embedder instead of a topic model.

Each tossup's full question text and each bonus's leadin + part text are fed
through the embedder with an instruction prefix, following Qwen3-Embedding's
documented instruction format:

    "Instruct: {task description}\\nQuery: {text}"

One embedding is computed per tossup and per bonus (not per clue/part) because
'r_j' is a fixed property of the question, like the topic model's fixed topic
mixture -- it does not vary with buzz position or bonus part.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

EMBEDDING_MIRT_DIR = REPO_ROOT / "multidimensional" / "embedding_mirt"

# Keep every HF-Hub artifact this script touches -- the downloaded
# Qwen3-Embedding-8B weights, the hub cache, and the cached login token --
# under multidimensional/embedding_mirt/ instead of the default
# '~/.cache/huggingface', so a fresh checkout is self-contained. Must be set
# before 'huggingface_hub' is imported (directly or via
# 'sentence_transformers'/'datasets') since it reads this env var at import time.
os.environ.setdefault("HF_HOME", str(EMBEDDING_MIRT_DIR / "hf_cache"))

from compirt_data import DEFAULT_DATA_DIR, filter_tournament, load_hf_tables


DEFAULT_MODEL = "Qwen/Qwen3-Embedding-8B"
DEFAULT_INSTRUCTION = (
    "Represent this quizbowl question to predict its difficulty and the "
    "skills it rewards"
)
DEFAULT_OUTPUT_DIR = EMBEDDING_MIRT_DIR / "outputs"


def bonus_text(leadin: str, parts) -> str:
    """Concatenate a bonus's leadin and part texts into one document."""
    part_texts = [str(part["text"]) for part in parts if part and part.get("text")]
    return " ".join([str(leadin or "")] + part_texts).strip()


def build_documents(tables) -> tuple[list[str], list[str], list[str], list[str]]:
    """Return '(tossup_ids, tossup_texts, bonus_ids, bonus_texts)' from the tables."""
    tossups = tables["tossups"]
    tossup_ids = tossups["tossup_id"].astype(str).tolist()
    tossup_texts = tossups["question"].fillna("").astype(str).tolist()

    bonuses = tables["bonuses"]
    bonus_ids = bonuses["bonus_id"].astype(str).tolist()
    bonus_texts = [
        bonus_text(leadin, parts)
        for leadin, parts in zip(bonuses["leadin"], bonuses["parts"])
    ]
    return tossup_ids, tossup_texts, bonus_ids, bonus_texts


def embed_texts(model, texts: list[str], instruction: str, batch_size: int) -> np.ndarray:
    """Embed 'texts' with the Qwen3 instruction format, batched."""
    prompted = [f"Instruct: {instruction}\nQuery: {text}" for text in texts]
    embeddings = model.encode(
        prompted,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    return embeddings.astype(np.float32)


def save_embedding_cache(path: Path, ids: list[str], embeddings: np.ndarray) -> None:
    np.savez(path, ids=np.array(ids, dtype=object), embeddings=embeddings)


def run(args):
    """Load the linked tables, embed every tossup and bonus, and cache to disk."""
    from sentence_transformers import SentenceTransformer

    args.output_dir.mkdir(parents=True, exist_ok=True)
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    tossup_ids, tossup_texts, bonus_ids, bonus_texts = build_documents(tables)
    print(f"Tossups: {len(tossup_ids):,}  Bonuses: {len(bonus_ids):,}")

    model = SentenceTransformer(args.model, device=args.device)

    tossup_embeddings = embed_texts(model, tossup_texts, args.instruction, args.batch_size)
    save_embedding_cache(
        args.output_dir / "tossup_embeddings.npz", tossup_ids, tossup_embeddings
    )

    bonus_embeddings = embed_texts(model, bonus_texts, args.instruction, args.batch_size)
    save_embedding_cache(
        args.output_dir / "bonus_embeddings.npz", bonus_ids, bonus_embeddings
    )

    metadata = {
        "model": args.model,
        "instruction": args.instruction,
        "embedding_dim": int(tossup_embeddings.shape[1]),
        "tossups": len(tossup_ids),
        "bonuses": len(bonus_ids),
    }
    (args.output_dir / "embedding_metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    print(f"Saved embeddings to {args.output_dir}")
    return metadata


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--instruction", default=DEFAULT_INSTRUCTION)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


if __name__ == "__main__":
    run(parse_args())
