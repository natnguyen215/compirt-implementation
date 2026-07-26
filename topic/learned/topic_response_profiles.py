"""Diagnostic: profile each supervised topic by its questions' outcomes.

Assigns every question its primary topic (the argmax of its topic vector) and
aggregates the real buzz/correctness outcomes of the questions in each topic.
This checks whether the supervised topics actually separate difficulty -- i.e.
that correct/incorrect propagated into the topics.

Run it on the 'document_latent_vectors.csv' produced by
'train_joint_pyramidal.py'::

    .venv/bin/python -m topic.learned.topic_response_profiles \
        --vectors results/compirt/in_sample/topic/joint-slda/document_latent_vectors.csv \
        --split year_2024
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from topic.utils.outputs import LATENT_TOPIC_PREFIX

from compirt_data import (
    DEFAULT_DATA_DIR,
    build_bonus_part_observations,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
)
from topic.learned.slda_responses import (
    bonus_responses,
    tossup_buzz_positions,
    tossup_responses,
)


def latent_columns(frame: pd.DataFrame) -> list[str]:
    """Return the latent topic columns in numeric suffix order."""
    columns = [
        column for column in frame.columns if str(column).startswith(LATENT_TOPIC_PREFIX)
    ]
    return sorted(columns, key=lambda column: int(str(column)[len(LATENT_TOPIC_PREFIX) :]))


def build_profile(
    vectors: pd.DataFrame,
    correctness: dict[str, float],
    buzz_positions: dict[str, float],
    topics: pd.DataFrame | None,
) -> pd.DataFrame:
    """Aggregate per-question outcomes into one row per primary topic."""
    columns = latent_columns(vectors)
    if not columns:
        raise ValueError("No latent_topic_XX columns found in the vectors CSV.")

    # Primary topic = the dimension each question loads on most heavily.
    questions = pd.DataFrame(
        {
            "document_id": vectors["document_id"].astype(str),
            "primary_topic": vectors[columns].astype(float).to_numpy().argmax(axis=1),
        }
    )
    questions["correctness"] = questions["document_id"].map(correctness)
    questions["buzz_position"] = questions["document_id"].map(buzz_positions)

    # Reindex every aggregate onto the full 0..k-1 topic range, then assign
    # positionally so empty topics become explicit zero/NaN rows.
    grouped = questions.groupby("primary_topic")
    topic_index = pd.RangeIndex(len(columns), name="primary_topic")
    profile = pd.DataFrame(
        {
            "topic_id": range(len(columns)),
            "n_questions": grouped.size().reindex(topic_index, fill_value=0).to_numpy(),
            "mean_correctness": grouped["correctness"].mean().reindex(topic_index).to_numpy(),
            "mean_buzz_position": grouped["buzz_position"].mean().reindex(topic_index).to_numpy(),
        }
    )

    if topics is not None and "top_words" in topics:
        # Attach each topic's top words for interpretation.
        top_words = topics.set_index("topic_id")["top_words"]
        profile["top_words"] = profile["topic_id"].map(top_words)
    return profile


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--vectors",
        type=Path,
        required=True,
        help="document_latent_vectors.csv produced by train_joint_pyramidal.py.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument(
        "--output",
        type=Path,
        help="Defaults to topic_response_profiles.csv beside the vectors CSV.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    vectors = pd.read_csv(args.vectors, dtype={"document_id": str})

    # Recompute the real outcomes from the observation tables.
    tables = filter_tournament(
        load_hf_tables(args.data_dir, args.split), args.tournament
    )
    tossup_obs = build_tossup_observations(tables)
    bonus_obs = build_bonus_part_observations(tables)
    correctness = {**tossup_responses(tossup_obs), **bonus_responses(bonus_obs)}
    buzz_positions = tossup_buzz_positions(tossup_obs)

    topics_path = args.vectors.parent / "topics.csv"
    topics = pd.read_csv(topics_path) if topics_path.exists() else None

    profile = build_profile(vectors, correctness, buzz_positions, topics)

    output_path = args.output or args.vectors.parent / "topic_response_profiles.csv"
    profile.to_csv(output_path, index=False)
    print(profile.to_string(index=False))
    print(f"\nsaved topic response profiles to {output_path}")


if __name__ == "__main__":
    main()
