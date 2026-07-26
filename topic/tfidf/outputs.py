"""Output helpers shared by fixed- and learned-topic TF-IDF runs."""

from __future__ import annotations

import csv

import numpy as np
import pandas as pd


TOPIC_TFIDF_LAMBDAS_FILENAME = "topic_tfidf_lambdas.csv"


def lambda_mapping(topic_labels, lambdas) -> dict[str, float]:
    """Return fitted topic lambdas as a JSON-ready label-to-value mapping."""
    values = lambdas.detach().cpu().tolist()
    return {str(label): float(value) for label, value in zip(topic_labels, values)}


def save_lambdas(output_dir, topic_labels, lambdas):
    """Write one nonnegative cumulative-TF-IDF lambda per topic coordinate."""
    path = output_dir / TOPIC_TFIDF_LAMBDAS_FILENAME
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=["topic_dimension", "topic_label", "lambda_tfidf"]
        )
        writer.writeheader()
        for dimension, (label, value) in enumerate(
            zip(topic_labels, lambdas.detach().cpu().tolist()), start=1
        ):
            writer.writerow(
                {
                    "topic_dimension": dimension,
                    "topic_label": str(label),
                    "lambda_tfidf": float(value),
                }
            )


def save_adjustment_curves(
    output_dir,
    data,
    observations,
    topic_weight,
    lambdas,
    n_points=201,
):
    """Write signed aggregate difficulty adjustments for evaluator replay.

    The topic-weighted effective curve receives
    '-tfidf_prefix_j(t) * sum_k r_jk * lambda_k'. Sampling that scalar on a
    relative-position grid lets evaluation reproduce adjusted difficulty and
    first-buzz timing without reconstructing the original text corpus.
    """
    prefix = data["tfidf_prefix"].detach().cpu().numpy()
    weights = topic_weight.detach().cpu().numpy()
    lambda_values = lambdas.detach().cpu().numpy()
    weighted_lambdas = weights @ lambda_values
    tossup_lengths = observations.groupby("tossup_id")["T_j"].first()
    grid = np.linspace(0.0, 1.0, n_points)
    values = np.zeros((len(data["tossup_ids"]), n_points))
    for index, tossup_id in enumerate(data["tossup_ids"]):
        total_tokens = int(tossup_lengths[tossup_id])
        tokens = np.clip(
            np.rint(grid * total_tokens).astype(int),
            1,
            min(total_tokens, prefix.shape[1]),
        )
        values[index] = -weighted_lambdas[index] * prefix[index, tokens - 1]
    frame = pd.DataFrame(
        values, columns=[f"adjustment_{point:03d}" for point in range(n_points)]
    )
    frame.insert(0, "tossup_id", data["tossup_ids"])
    frame.to_csv(output_dir / "tfidf_adjustment_curves.csv", index=False)
