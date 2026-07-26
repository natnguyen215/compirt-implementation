#!/usr/bin/env python3
"""Build a category one-hot 'topic vector' file from ground-truth labels.

This produces a drop-in replacement for document_latent_vectors.csv where each
document's vector is a one-hot over its true top-level quizbowl category instead
of a learned PLDA topic. Feeding this to the same topic-weighted pipeline gives
the *upper bound* on how much category-conditioning can help: if perfect
categories don't beat the global-skill model, no learned-topic method will.

The source PLDA file supplies the document IDs and labels used to build the
one-hot encoding.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from topic.utils.categories import UNKNOWN, top_level_category
from topic.utils.outputs import (
    DEFAULT_CATEGORY_OUTPUT_DIR,
    DEFAULT_TOPIC_VECTORS,
    REPO_ROOT,
)


def main() -> None:
    """Build the category one-hot vectors CSV and the dimension-index CSV."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_TOPIC_VECTORS)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_CATEGORY_OUTPUT_DIR)
    args = parser.parse_args()

    # Load document IDs and labels from the topic-vector file.
    frame = pd.read_csv(args.source, dtype={"document_id": str})
    if "labels" not in frame or "document_id" not in frame:
        raise ValueError("source must contain document_id and labels columns")

    # Map each document's raw label to a canonical category, then fix the
    # dimension order: sorted real categories first, UNKNOWN last (if present).
    categories = frame["labels"].map(top_level_category)
    names = sorted(c for c in categories.unique() if c != UNKNOWN)
    if (categories == UNKNOWN).any():
        names.append(UNKNOWN)
    index = {name: i for i, name in enumerate(names)}

    # One-hot encode each document's category into latent_topic_* columns.
    columns = [f"latent_topic_{i:02d}" for i in range(len(names))]
    onehot = pd.DataFrame(0.0, index=frame.index, columns=columns)
    for row, name in enumerate(categories):
        onehot.iat[row, index[name]] = 1.0

    # Write the drop-in vectors CSV (document_id + metadata + one-hot columns).
    out = pd.concat(
        [
            frame[["document_id"]].assign(
                question_type=frame.get("question_type"),
                category=categories,
            ),
            onehot,
        ],
        axis=1,
    )
    args.out_dir.mkdir(parents=True, exist_ok=True)
    vectors_path = args.out_dir / "document_latent_vectors.csv"
    out.to_csv(vectors_path, index=False)

    # Write the dimension -> category index, then print a run summary.
    mapping = pd.DataFrame(
        {"dimension": range(len(names)), "column": columns, "category": names}
    )
    mapping.to_csv(args.out_dir / "category_index.csv", index=False)

    print(f"Wrote {vectors_path}  rows={len(out)}  DIMENSIONS={len(names)}")
    print("Category dimensions:")
    print(mapping.to_string(index=False))
    print(
        f"\nDocuments with no label -> '{UNKNOWN}': "
        f"{(categories == UNKNOWN).sum()}/{len(categories)}"
    )
    print(
        f"\nRun with:  DIMENSIONS={len(names)} "
        f"TOPIC_VECTORS={vectors_path.relative_to(REPO_ROOT)}"
    )


if __name__ == "__main__":
    main()
