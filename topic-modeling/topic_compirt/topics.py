"""Load and align fixed topic-proportion vectors for topic-weighted CompIRT."""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd
import torch


TOPIC_COLUMN_RE = re.compile(r"^latent_topic_(\d+)$")
BONUS_PART_SEPARATOR = "::part-"


def topic_columns(frame: pd.DataFrame) -> list[str]:
    """Return latent topic columns in numeric suffix order."""
    # Keep only latent_topic_N columns, paired with their numeric suffix.
    columns = []
    for column in frame.columns:
        match = TOPIC_COLUMN_RE.match(str(column))
        if match:
            columns.append((int(match.group(1)), column))
    # Sort by suffix so dimension order is stable regardless of CSV column order.
    return [column for _, column in sorted(columns)]


def load_topic_dataframe(
    path: str | Path,
    question_type: str | None = None,
    expected_dimensions: int | None = None,
) -> tuple[pd.DataFrame, list[str]]:
    """Read, validate, and normalize a topic-vector CSV.

    The returned frame is indexed by 'document_id' and contains normalized
    topic proportions in the returned topic columns.
    """
    # document_id is the required join key for aligning vectors to model rows.
    frame = pd.read_csv(path, dtype={"document_id": str})
    if "document_id" not in frame:
        raise ValueError(f"{path} must contain a document_id column")
    # Optionally restrict to one question_type (tossup/bonus) before validating.
    if question_type is not None:
        if "question_type" not in frame:
            raise ValueError(f"{path} must contain question_type for filtering")
        frame = frame[frame["question_type"] == question_type].copy()
        if frame.empty:
            raise ValueError(
                f"{path} contains no topic vectors with question_type={question_type!r}"
            )

    # Require latent_topic columns, and the exact count if the caller specified one.
    columns = topic_columns(frame)
    if not columns:
        raise ValueError(f"{path} does not contain latent_topic_XX columns")
    if expected_dimensions is not None and len(columns) != expected_dimensions:
        raise ValueError(
            f"Expected {expected_dimensions} topic dimensions, found {len(columns)}"
        )

    # Each document must appear exactly once.
    if frame["document_id"].duplicated().any():
        duplicate = frame.loc[frame["document_id"].duplicated(), "document_id"].iloc[0]
        raise ValueError(f"Duplicate topic vector for document_id {duplicate!r}")

    # Reject NaN/inf and zero-mass rows before normalizing.
    values = frame[columns].to_numpy(dtype=float)
    if not np.isfinite(values).all():
        raise ValueError("Topic vectors contain NaN or infinite values")
    row_sums = values.sum(axis=1)
    if (row_sums <= 0).any():
        bad_id = frame.loc[row_sums <= 0, "document_id"].iloc[0]
        raise ValueError(f"Topic vector for {bad_id!r} has zero total mass")

    # L1-normalize each row so topic proportions sum to 1, then index by document_id.
    frame.loc[:, columns] = values / row_sums[:, None]
    return frame.set_index("document_id", drop=False), columns


def align_topic_vectors(
    frame: pd.DataFrame,
    columns: list[str],
    document_ids,
    *,
    id_label: str = "document_id",
) -> np.ndarray:
    """Return topic vectors ordered to match 'document_ids'."""
    # Fail loudly (with a short preview) if any requested id has no topic vector.
    ids = [str(value) for value in document_ids]
    missing = [value for value in ids if value not in frame.index]
    if missing:
        preview = ", ".join(missing[:5])
        if len(missing) > 5:
            preview += ", ..."
        raise ValueError(f"Missing topic vectors for {id_label}: {preview}")
    # Reorder rows to exactly match the requested id order.
    return frame.loc[ids, columns].to_numpy(dtype=np.float32)


def bonus_id_from_part_id(part_id: str) -> str:
    """Return the base bonus ID from a 'bonus_id::part-N' identifier."""
    # Strip the trailing ::part-N suffix to recover the shared base bonus id.
    part_id = str(part_id)
    if BONUS_PART_SEPARATOR not in part_id:
        raise ValueError(f"Bonus part ID lacks {BONUS_PART_SEPARATOR!r}: {part_id}")
    return part_id.rsplit(BONUS_PART_SEPARATOR, 1)[0]


def align_tossup_topic_weights(
    data: dict,
    path: str | Path,
    expected_dimensions: int | None = None,
) -> tuple[torch.Tensor, list[str]]:
    """Load topic vectors ordered like 'data["tossup_ids"]'."""
    # Load tossup vectors, order them like data["tossup_ids"], move to data's device.
    frame, columns = load_topic_dataframe(
        path, question_type="tossup", expected_dimensions=expected_dimensions
    )
    values = align_topic_vectors(frame, columns, data["tossup_ids"], id_label="tossup_id")
    return torch.tensor(values, dtype=torch.float32, device=data["y"].device), columns


def align_bonus_topic_weights(
    data: dict,
    path: str | Path,
    expected_dimensions: int | None = None,
) -> tuple[torch.Tensor, list[str]]:
    """Load topic vectors ordered like 'data["part_ids"]' via base bonus IDs."""
    # Load bonus vectors, then map each part id to its base bonus id before aligning.
    frame, columns = load_topic_dataframe(
        path, question_type="bonus", expected_dimensions=expected_dimensions
    )
    bonus_ids = [bonus_id_from_part_id(part_id) for part_id in data["part_ids"]]
    # Order like data["part_ids"] (all parts of a bonus share one vector); move to device.
    values = align_topic_vectors(frame, columns, bonus_ids, id_label="bonus_id")
    return torch.tensor(values, dtype=torch.float32, device=data["y"].device), columns
