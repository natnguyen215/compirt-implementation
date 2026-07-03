"""Metric and difficulty-curve definitions for CompIRT evaluation.

Pure NumPy/pandas computations shared by both evaluation scenarios:
the position-dependent difficulty curve (paper Eq. 3) and the
classification, calibration, and bonus-scoring metrics reported in
paper Section 5.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import (
    log_loss,
    mean_absolute_error,
    roc_auc_score,
)


def inverse_logit(logits):
    """Return sigmoid(logits), clipping only to keep NumPy exp finite."""
    return 1.0 / (1.0 + np.exp(-np.clip(logits, -60, 60)))


def difficulty_curve(beta, gamma, mu, positions):
    """Evaluate the saved pyramidal difficulty curve on relative positions.

    This is the NumPy re-implementation of the model's Eq. 3 sigmoid difficulty,
    used to redraw fitted curves from saved 'beta', 'gamma', and 'mu'.
    """
    # Clip the sigmoid argument to +-60 so np.exp stays finite; sigmoid is
    # already saturated to 0/1 well before that, so the curve is unchanged.
    argument = np.clip(gamma * (mu - positions), -60, 60)
    return beta / (1.0 + np.exp(-argument))


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
    """Return AUC, binary log loss, and expected calibration error.

    These are the standard binary-classification metrics the paper reports for
    tossup correctness and bonus parts (Scenarios A and B); they are computed
    here on the in-sample fitted predictions.
    """
    y = np.asarray(y, dtype=float)
    if len(y) == 0:
        return {"auc": float("nan"), "log_loss": float("nan"), "ece": float("nan")}

    # Clip away exact 0/1 so log loss never sees log(0).
    probability = np.clip(np.asarray(probability, dtype=float), 1e-6, 1 - 1e-6)
    # AUC is undefined when every label is the same class.
    auc = float("nan") if len(np.unique(y)) < 2 else roc_auc_score(y, probability)
    return {
        "auc": auc,
        "log_loss": log_loss(y, probability, labels=[0, 1]),
        "ece": expected_calibration_error(y, probability),
        "accuracy": float(((probability >= 0.5) == y.astype(bool)).mean()),
    }


def bonus_metrics(parts, teams):
    """Return the paper's part-, bonus-, and game-level bonus metrics.

    Covers part-level classification (AUC/log-loss/ECE/accuracy), strict exact
    bonus-part recovery, rounded-score recovery, per-bonus points MAE, and
    points-per-bonus (PPB) MAE, which the paper defines at the game/team level
    (Scenario B).
    """
    metrics = classification_metrics(parts["correct"], parts["predicted_correct"])
    part_matches = (parts["predicted_correct"] >= 0.5) == parts["correct"].astype(bool)
    metrics["part_accuracy"] = float(part_matches.mean())
    if len(parts) and "response_id" in parts:
        exact_by_response = pd.DataFrame(
            {
                "response_id": parts["response_id"],
                "part_matches": part_matches,
            }
        ).groupby("response_id").agg(
            all_parts_match=("part_matches", "all"),
            part_count=("part_matches", "size"),
        )
        metrics["exact_acc"] = float(
            (
                exact_by_response["all_parts_match"]
                & (exact_by_response["part_count"] == 3)
            ).mean()
        )
    else:
        metrics["exact_acc"] = float("nan")

    # A standard three-part bonus can only score 0, 10, 20, or 30 points; snap
    # the continuous expected-points prediction to the nearest of these.
    possible_scores = np.asarray([0, 10, 20, 30])
    predicted_score_index = np.abs(
        teams["predicted_points"].to_numpy()[:, None] - possible_scores[None, :]
    ).argmin(axis=1)
    metrics["rounded_score_accuracy"] = float(
        (
            possible_scores[predicted_score_index]
            == teams["total_points"].to_numpy()
        ).mean()
    )
    metrics["per_bonus_points_mae"] = mean_absolute_error(
        teams["total_points"], teams["predicted_points"]
    )

    # The paper defines PPB at the game/team level, so average all bonuses heard
    # by a team in a game before calculating its prediction error.
    game_ppb = teams.groupby(["game_id", "team_id"], as_index=False).agg(
        observed_ppb=("total_points", "mean"),
        predicted_ppb=("predicted_points", "mean"),
    )
    metrics["ppb_mae"] = mean_absolute_error(
        game_ppb["observed_ppb"], game_ppb["predicted_ppb"]
    )
    return metrics
