"""Load and align cached question embeddings, and save/load the fitted projection.

'embed_questions.py' precomputes a frozen Qwen3-Embedding-8B vector per tossup
and per bonus and caches them to '.npz' files (embedding dimensionality runs
into the thousands, unlike the topic model's handful of 'latent_topic_N'
columns, so a wide CSV would be impractical). This module loads those caches
and orders them to match a training run's tossup/bonus-part ids, the same
fail-loud alignment contract as
'topic/fixed/topic_compirt/topics.py:align_tossup_topic_weights'.

It also saves and loads the fitted relevance projection so the compositional
(bonus) stage can reuse the exact transform fit during pyramidal (tossup)
training instead of learning its own.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import numpy as np
import torch

from topic.fixed.topic_compirt.topics import bonus_id_from_part_id


def load_embedding_cache(path: str | Path) -> tuple[list[str], np.ndarray]:
    """Return '(ids, embeddings)' from an '.npz' file written by 'embed_questions.py'."""
    # allow_pickle=True is required because 'ids' is an object array of strings;
    # the file is one this codebase produces itself (embed_questions.py), not
    # untrusted input.
    cache = np.load(path, allow_pickle=True)
    ids = [str(value) for value in cache["ids"]]
    embeddings = cache["embeddings"].astype(np.float32)
    if len(ids) != embeddings.shape[0]:
        raise ValueError(
            f"{path} has {len(ids)} ids but {embeddings.shape[0]} embedding rows"
        )
    duplicates = [value for value, count in Counter(ids).items() if count > 1]
    if duplicates:
        raise ValueError(f"{path} has duplicate embedding ids: {duplicates[:5]}")
    if not np.isfinite(embeddings).all():
        raise ValueError(f"{path} contains NaN or infinite embedding values")
    return ids, embeddings


def _align(ids: list[str], embeddings: np.ndarray, requested_ids, *, id_label: str) -> np.ndarray:
    """Return 'embeddings' reordered to match 'requested_ids' exactly."""
    index = {value: position for position, value in enumerate(ids)}
    requested = [str(value) for value in requested_ids]
    missing = [value for value in requested if value not in index]
    if missing:
        preview = ", ".join(missing[:5])
        if len(missing) > 5:
            preview += ", ..."
        raise ValueError(f"Missing embeddings for {id_label}: {preview}")
    return embeddings[[index[value] for value in requested]]


def align_tossup_embeddings(data: dict, path: str | Path) -> torch.Tensor:
    """Load tossup embeddings ordered like 'data["tossup_ids"]'."""
    ids, embeddings = load_embedding_cache(path)
    aligned = _align(ids, embeddings, data["tossup_ids"], id_label="tossup_id")
    return torch.tensor(aligned, dtype=torch.float32, device=data["y"].device)


def align_bonus_embeddings(data: dict, path: str | Path) -> torch.Tensor:
    """Load bonus embeddings ordered like 'data["part_ids"]' via base bonus IDs.

    All three parts of a bonus share one embedding, the same sharing rule
    'topic/fixed/topic_compirt/topics.py:align_bonus_topic_weights' uses for
    fixed topic vectors.
    """
    ids, embeddings = load_embedding_cache(path)
    bonus_ids = [bonus_id_from_part_id(part_id) for part_id in data["part_ids"]]
    aligned = _align(ids, embeddings, bonus_ids, id_label="bonus_id")
    return torch.tensor(aligned, dtype=torch.float32, device=data["y"].device)


def center_embeddings(
    embedding: torch.Tensor, embedding_mean: torch.Tensor | None
) -> torch.Tensor:
    """Subtract the tossup-training embedding mean when one is available."""
    if embedding_mean is None:
        return embedding
    return embedding - embedding_mean


def _tensor_array(value: torch.Tensor) -> np.ndarray:
    return value.detach().cpu().numpy()


def save_projection(
    path: str | Path,
    projection,
    bias: torch.Tensor | None = None,
    *,
    embedding_mean: torch.Tensor | None = None,
) -> None:
    """Save the fitted 'r' projection so the compositional stage can reuse it frozen."""
    arrays = {}
    if isinstance(projection, dict):
        kind = projection.get("kind", "linear")
        arrays["kind"] = np.array(kind)
        if kind == "ffn":
            arrays.update(
                {
                    "input_weight": _tensor_array(projection["input_weight"]),
                    "hidden_bias": _tensor_array(projection["hidden_bias"]),
                    "output_weight": _tensor_array(projection["output_weight"]),
                    "output_bias": _tensor_array(projection["output_bias"]),
                }
            )
        elif kind == "linear":
            arrays.update(
                {
                    "weight": _tensor_array(projection["weight"]),
                    "bias": _tensor_array(projection["bias"]),
                }
            )
        else:
            raise ValueError(f"Unknown relevance projection kind: {kind}")
    else:
        if bias is None:
            raise TypeError("save_projection(weight, bias) requires a bias tensor")
        arrays.update(
            {
                "kind": np.array("linear"),
                "weight": _tensor_array(projection),
                "bias": _tensor_array(bias),
            }
        )
    if embedding_mean is not None:
        arrays["embedding_mean"] = _tensor_array(embedding_mean)
    np.savez(path, **arrays)


def _load_tensor(cache, key: str, device) -> torch.Tensor:
    return torch.tensor(cache[key], dtype=torch.float32, device=device)


def load_projection(path: str | Path, device="cpu"):
    """Load a frozen 'r' projection saved by the pyramidal training run.

    Old linear projections return '(weight, bias)' for backward compatibility.
    New FFN projections return a projection dict; use 'load_projection_state'
    when the caller also needs the saved embedding mean.
    """
    projection, _ = load_projection_state(path, device)
    if projection["kind"] == "linear":
        return projection["weight"], projection["bias"]
    return projection


def load_projection_state(
    path: str | Path, device="cpu"
) -> tuple[dict[str, torch.Tensor | str], torch.Tensor | None]:
    """Load a frozen relevance projection and optional tossup embedding mean."""
    cache = np.load(path)
    kind = str(cache["kind"].item()) if "kind" in cache.files else "linear"
    if kind == "ffn":
        projection = {
            "kind": "ffn",
            "input_weight": _load_tensor(cache, "input_weight", device),
            "hidden_bias": _load_tensor(cache, "hidden_bias", device),
            "output_weight": _load_tensor(cache, "output_weight", device),
            "output_bias": _load_tensor(cache, "output_bias", device),
        }
    elif kind == "linear":
        projection = {
            "kind": "linear",
            "weight": _load_tensor(cache, "weight", device),
            "bias": _load_tensor(cache, "bias", device),
        }
    else:
        raise ValueError(f"Unknown relevance projection kind in {path}: {kind}")
    embedding_mean = (
        _load_tensor(cache, "embedding_mean", device)
        if "embedding_mean" in cache.files
        else None
    )
    return projection, embedding_mean


def _projection_input_dim(projection) -> int:
    if isinstance(projection, torch.Tensor):
        return int(projection.shape[0])
    if isinstance(projection, tuple):
        return int(projection[0].shape[0])
    if projection["kind"] == "ffn":
        return int(projection["input_weight"].shape[0])
    return int(projection["weight"].shape[0])


def _projection_output_dim(projection) -> int:
    if isinstance(projection, torch.Tensor):
        return int(projection.shape[1])
    if isinstance(projection, tuple):
        return int(projection[0].shape[1])
    if projection["kind"] == "ffn":
        return int(projection["output_weight"].shape[1])
    return int(projection["weight"].shape[1])


def check_projection_shapes(
    projection,
    embedding: torch.Tensor,
    theta: torch.Tensor,
    *,
    projection_path,
    embeddings_path,
    player_skills_path,
    embedding_mean: torch.Tensor | None = None,
) -> None:
    """Raise a clear error if a frozen projection doesn't match its inputs.

    Without this check a mismatched pairing of '--embeddings'/'--projection'/
    '--player-skills' files would only surface as a bare matmul or broadcast
    shape error deep inside 'project_relevance'/'compositional_model'.
    """
    input_dim = _projection_input_dim(projection)
    output_dim = _projection_output_dim(projection)
    if input_dim != embedding.shape[1]:
        raise ValueError(
            f"{projection_path} expects embedding dim {input_dim}, but "
            f"{embeddings_path} has dim {embedding.shape[1]} -- are --embeddings "
            "and --projection from the same embed_questions.py run?"
        )
    if embedding_mean is not None and embedding_mean.shape[0] != embedding.shape[1]:
        raise ValueError(
            f"{projection_path} stores embedding mean dim {embedding_mean.shape[0]}, "
            f"but {embeddings_path} has dim {embedding.shape[1]} -- are --embeddings "
            "and --projection from the same embed_questions.py run?"
        )
    if output_dim != theta.shape[1]:
        raise ValueError(
            f"{projection_path} produces {output_dim} relevance dimensions, "
            f"but {player_skills_path} has {theta.shape[1]} theta dimensions -- "
            "are --projection and --player-skills from the same paired "
            "train_pyramidal.py run?"
        )
