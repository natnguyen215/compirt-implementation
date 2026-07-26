"""Scenario-agnostic metric primitives for CompIRT evaluation.

This module contains only probability and classification calculations reused
by multiple evaluation scenarios. Tossup-specific and bonus-specific scoring
lives in each scenario's ``metrics`` module.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import (
    log_loss,
    roc_auc_score,
)


def inverse_logit(logits):
    """Return sigmoid(logits), clipping only to keep NumPy exp finite."""
    return 1.0 / (1.0 + np.exp(-np.clip(logits, -60, 60)))


def expected_calibration_error(y, probability, n_bins=10):
    """Measure how closely predicted probabilities match observed frequencies.

    Predictions are grouped into probability bins. For each non-empty bin, the
    absolute gap between mean confidence and observed success rate is weighted
    by the bin's fraction of all observations.
    """
    y = np.asarray(y, dtype=float)
    probability = np.asarray(probability, dtype=float)
    if len(y) == 0:
        return float("nan")

    bins = np.linspace(0.0, 1.0, n_bins + 1)
    bucket = np.clip(np.digitize(probability, bins) - 1, 0, n_bins - 1)
    error = 0.0
    for index in range(n_bins):
        selected = bucket == index
        if selected.any():
            error += selected.mean() * abs(
                y[selected].mean() - probability[selected].mean()
            )
    return float(error)


def binary_brier_score(y, probability):
    """Return the mean squared error of binary probability forecasts.

    The score rewards probabilities that are both discriminative and
    appropriately confident. Zero is perfect and one is the worst possible
    score.
    """
    y = np.asarray(y, dtype=float)
    probability = np.asarray(probability, dtype=float)
    if len(y) == 0:
        return float("nan")
    return float(np.mean((probability - y) ** 2))


def sharpness_metrics(probability):
    """Describe the concentration of forecasts without using the outcomes.

    Calibration says whether probabilities are trustworthy; sharpness says
    how far forecasts move away from an uninformative middle probability.
    These quantities should therefore always be read alongside calibration.
    """
    probability = np.asarray(probability, dtype=float)
    if len(probability) == 0:
        return {
            "probability_std": float("nan"),
            "probability_p10": float("nan"),
            "probability_p50": float("nan"),
            "probability_p90": float("nan"),
            "mean_predictive_variance": float("nan"),
        }
    return {
        "probability_std": float(np.std(probability)),
        "probability_p10": float(np.quantile(probability, 0.10)),
        "probability_p50": float(np.quantile(probability, 0.50)),
        "probability_p90": float(np.quantile(probability, 0.90)),
        "mean_predictive_variance": float(np.mean(probability * (1 - probability))),
    }


def calibration_table(y, probability, n_bins=10):
    """Summarize confidence, accuracy, and sample count by probability bin."""
    frame = pd.DataFrame(
        {
            "y": np.asarray(y, dtype=float),
            "probability": np.asarray(probability, dtype=float),
        }
    )
    frame["bin"] = pd.cut(
        frame["probability"],
        bins=np.linspace(0, 1, n_bins + 1),
        include_lowest=True,
    )
    return frame.groupby("bin", observed=True).agg(
        predicted=("probability", "mean"),
        observed=("y", "mean"),
        count=("y", "size"),
    )


def classification_metrics(y, probability):
    """Return AUC, binary log loss, expected calibration error, and accuracy.

    These are the standard binary-classification metrics the paper reports for
    tossup correctness and bonus parts (Scenarios A and B); they are computed
    here on the in-sample fitted predictions.
    """
    y = np.asarray(y, dtype=float)
    if len(y) == 0:
        empty = {
            "auc": float("nan"),
            "log_loss": float("nan"),
            "ece": float("nan"),
            "brier": float("nan"),
            "accuracy": float("nan"),
            "all_correct_accuracy": float("nan"),
            "accuracy_lift_over_all_correct": float("nan"),
        }
        return {**empty, **sharpness_metrics([])}

    # Clip away exact 0/1 so log loss never sees log(0).
    raw_probability = np.clip(np.asarray(probability, dtype=float), 0.0, 1.0)
    probability = np.clip(raw_probability, 1e-6, 1 - 1e-6)
    # AUC is undefined when every label is the same class.
    auc = float("nan") if len(np.unique(y)) < 2 else roc_auc_score(y, probability)
    accuracy = float(((raw_probability >= 0.5) == y.astype(bool)).mean())
    all_correct_accuracy = float(y.mean())
    metrics = {
        "auc": auc,
        "log_loss": log_loss(y, probability, labels=[0, 1]),
        "ece": expected_calibration_error(y, raw_probability),
        "brier": binary_brier_score(y, raw_probability),
        "accuracy": accuracy,
        # The canonical reference predicts every attempt correct; it stays
        # fixed across data slices rather than acting as a majority-class oracle.
        "all_correct_accuracy": all_correct_accuracy,
        "accuracy_lift_over_all_correct": accuracy - all_correct_accuracy,
    }
    metrics.update(sharpness_metrics(raw_probability))
    return metrics


def ranked_probability_score(distribution, observed_index):
    """Return normalized RPS for one forecast over ordered outcome classes.

    The normalization by ``K - 1`` places the score in [0, 1], where zero is
    perfect.  For bonuses the four classes are 0, 10, 20, and 30 points.
    """
    distribution = np.asarray(distribution, dtype=float)
    if distribution.ndim != 1 or len(distribution) < 2:
        raise ValueError("RPS requires a one-dimensional distribution over >=2 classes")
    if not 0 <= int(observed_index) < len(distribution):
        raise ValueError("Observed class index is outside the forecast distribution")
    distribution = distribution / distribution.sum()
    forecast_cdf = np.cumsum(distribution)[:-1]
    observed_cdf = (np.arange(len(distribution) - 1) >= int(observed_index)).astype(float)
    return float(np.mean((forecast_cdf - observed_cdf) ** 2))


def stratified_prediction_metrics(
    frame, target_column, probability_column, scenario, strata
):
    """Return classification, calibration, and sharpness metrics by stratum.

    ``strata`` maps a readable stratum name to a column in ``frame``.  An
    aggregate row is included so every slice has a directly comparable parent.
    """
    rows = []

    def add_row(stratum, value, group):
        rows.append(
            {
                "scenario": scenario,
                "stratum": stratum,
                "value": value,
                "observations": len(group),
                **classification_metrics(group[target_column], group[probability_column]),
            }
        )

    add_row("aggregate", "all", frame)
    for stratum, column in strata.items():
        if column not in frame:
            continue
        for value, group in frame.groupby(column, dropna=False, observed=True):
            add_row(stratum, "Unknown" if pd.isna(value) else str(value), group)
    return pd.DataFrame(rows)
