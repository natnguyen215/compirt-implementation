"""Load and align cached question embeddings, and save/load the fitted projection.

'embed_questions.py' precomputes a frozen Qwen3-Embedding-8B vector per tossup
and per bonus and caches them to '.npz' files (embedding dimensionality runs
into the thousands, unlike the topic model's handful of 'latent_topic_N'
columns, so a wide CSV would be impractical). This module loads those caches
and orders them to match a training run's tossup/bonus-part ids, the same
fail-loud alignment contract as
'topic/fixed/topic_compirt/topics.py:align_tossup_topic_weights'.

It also saves and loads the fitted linear projection ('r_projection_weight',
'r_projection_bias') so the compositional (bonus) stage can reuse the exact
transform fit during pyramidal (tossup) training instead of learning its own.
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


def save_projection(path: str | Path, weight: torch.Tensor, bias: torch.Tensor) -> None:
    """Save the fitted 'r' projection so the compositional stage can reuse it frozen."""
    np.savez(
        path,
        weight=weight.detach().cpu().numpy(),
        bias=bias.detach().cpu().numpy(),
    )


def load_projection(path: str | Path, device="cpu") -> tuple[torch.Tensor, torch.Tensor]:
    """Load a frozen 'r' projection saved by the pyramidal training run."""
    cache = np.load(path)
    weight = torch.tensor(cache["weight"], dtype=torch.float32, device=device)
    bias = torch.tensor(cache["bias"], dtype=torch.float32, device=device)
    return weight, bias


def check_projection_shapes(
    weight: torch.Tensor,
    embedding: torch.Tensor,
    theta: torch.Tensor,
    *,
    projection_path,
    embeddings_path,
    player_skills_path,
) -> None:
    """Raise a clear error if a frozen projection doesn't match its inputs.

    Without this check a mismatched pairing of '--embeddings'/'--projection'/
    '--player-skills' files would only surface as a bare matmul or broadcast
    shape error deep inside 'project_relevance'/'compositional_model'.
    """
    if weight.shape[0] != embedding.shape[1]:
        raise ValueError(
            f"{projection_path} expects embedding dim {weight.shape[0]}, but "
            f"{embeddings_path} has dim {embedding.shape[1]} -- are --embeddings "
            "and --projection from the same embed_questions.py run?"
        )
    if weight.shape[1] != theta.shape[1]:
        raise ValueError(
            f"{projection_path} produces {weight.shape[1]} relevance dimensions, "
            f"but {player_skills_path} has {theta.shape[1]} theta dimensions -- "
            "are --projection and --player-skills from the same paired "
            "train_pyramidal.py run?"
        )
