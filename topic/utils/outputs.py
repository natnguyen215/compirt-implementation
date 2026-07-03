"""Paths and saved-file schema helpers for topic-model outputs."""

from __future__ import annotations

import csv
from collections.abc import Sequence
from pathlib import Path


TOPIC_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = TOPIC_ROOT.parent
DEFAULT_DATABASE = REPO_ROOT / "data" / "database.db"
DEFAULT_OUTPUT_ROOT = TOPIC_ROOT / "fixed" / "outputs"
DEFAULT_PLDA_OUTPUT_DIR = DEFAULT_OUTPUT_ROOT / "plda"
DEFAULT_LDA_OUTPUT_DIR = DEFAULT_OUTPUT_ROOT / "lda"
DEFAULT_CATEGORY_OUTPUT_DIR = DEFAULT_OUTPUT_ROOT / "category"

DOCUMENT_VECTOR_FILENAME = "document_latent_vectors.csv"
DEFAULT_TOPIC_VECTORS = DEFAULT_PLDA_OUTPUT_DIR / DOCUMENT_VECTOR_FILENAME
LATENT_TOPIC_PREFIX = "latent_topic_"


def latent_topic_columns(dimensions: int) -> list[str]:
    """Return standard latent-topic column names for a vector width."""
    return [f"{LATENT_TOPIC_PREFIX}{index:02d}" for index in range(dimensions)]


def document_vector_fieldnames(dimensions: int) -> list[str]:
    """Return the standard topic-vector CSV columns."""
    return [
        "document_id",
        "source_document_id",
        "question_type",
        "labels",
        "token_count",
        "latent_mass",
        *latent_topic_columns(dimensions),
    ]


def document_vector_row(
    source: dict[str, object],
    latent_dist: Sequence[float],
) -> dict[str, object]:
    """Build one standard topic-vector CSV row from source metadata and a vector."""
    row: dict[str, object] = {
        "document_id": source["document_id"],
        "source_document_id": source["source_document_id"],
        "question_type": source["question_type"],
        "labels": "|".join(source["labels"]),
        "token_count": len(source["words"]),
        "latent_mass": sum(latent_dist),
    }
    for index, value in enumerate(latent_dist):
        row[f"{LATENT_TOPIC_PREFIX}{index:02d}"] = value
    return row


def load_dimension_labels(path: Path) -> dict[int, str]:
    """Read a 'dimension,column,category' CSV into 1-based dimension labels."""
    labels: dict[int, str] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            name = (row.get("category") or row.get("name") or "").strip()
            if name:
                labels[int(row["dimension"]) + 1] = name
    return labels
