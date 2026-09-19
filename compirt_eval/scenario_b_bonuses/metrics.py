"""Pure scoring calculations owned by Scenario B bonus evaluation.

This module converts saved bonus-part and team prediction frames into
bonus-response score distributions and aggregate metrics. It performs no file
I/O and creates no figures.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error

from compirt_eval.common.metrics import (
    classification_metrics,
    ranked_probability_score,
)


def bonus_parts_with_difficulty(parts, bonuses=None):
    """Join declared part difficulty by bonus ID and zero-based part index."""
    parts = parts.copy()
    if bonuses is not None:
        labels = pd.DataFrame(
            [
                {"bonus_id": bonus.bonus_id, "part_index": index,
                 "difficulty": part.get("difficulty", "")}
                for bonus in bonuses.itertuples(index=False)
                for index, part in enumerate(bonus.parts)
            ],
            columns=["bonus_id", "part_index", "difficulty"],
        )
        parts = parts.drop(columns="difficulty", errors="ignore").merge(
            labels, on=["bonus_id", "part_index"], how="left", validate="many_to_one"
        )
    if "difficulty" not in parts:
        parts["difficulty"] = "unknown"
    labels = parts["difficulty"].fillna("").astype(str).str.strip().str.lower()
    parts["difficulty"] = labels.where(labels.isin(["easy", "medium", "hard"]), "unknown")
    return parts


def bonus_accuracy_by_difficulty(parts):
    """Micro accuracy and denominator for each declared difficulty, including unknown."""
    parts = bonus_parts_with_difficulty(parts)
    matches = (parts["predicted_correct"] >= 0.5) == parts["correct"].astype(bool)
    return pd.DataFrame([
        {"difficulty": difficulty, "parts": int(selected.sum()),
         "part_accuracy": float(matches[selected].mean())}
        for difficulty in ("easy", "medium", "hard", "unknown")
        for selected in [parts["difficulty"].eq(difficulty)]
    ])


def bonus_score_distribution(part_probabilities):
    """Return probabilities of scoring 0, 10, 20, or 30 on a three-part bonus."""
    probabilities = np.asarray(part_probabilities, dtype=float)
    if probabilities.shape != (3,):
        raise ValueError("A standard bonus response must contain exactly three parts")
    distribution = np.array([1.0])
    for probability in np.clip(probabilities, 0.0, 1.0):
        distribution = np.convolve(distribution, [1 - probability, probability])
    return distribution


def bonus_ranked_probability_scores(parts):
    """Return proper-score details for each complete three-part bonus response."""
    if "response_id" not in parts or parts.empty:
        return pd.DataFrame(
            columns=[
                "response_id",
                "observed_points",
                "probability_0",
                "probability_10",
                "probability_20",
                "probability_30",
                "rps",
                "observed_score_probability",
                "score_log_loss",
            ]
        )
    rows = []
    for response_id, response in parts.groupby("response_id", sort=False):
        if len(response) != 3:
            continue
        if "part_index" in response:
            response = response.sort_values("part_index")
        distribution = bonus_score_distribution(response["predicted_correct"].to_numpy())
        observed_index = int(response["correct"].sum())
        observed_probability = float(distribution[observed_index])
        rows.append(
            {
                "response_id": response_id,
                "observed_points": 10 * observed_index,
                "probability_0": distribution[0],
                "probability_10": distribution[1],
                "probability_20": distribution[2],
                "probability_30": distribution[3],
                "rps": ranked_probability_score(distribution, observed_index),
                "observed_score_probability": observed_probability,
                "score_log_loss": float(
                    -np.log(np.clip(observed_probability, 1e-12, 1.0))
                ),
            }
        )
    return pd.DataFrame(rows)


def _macro_group_mean(values, groups):
    """Average within each observed group, then weight groups equally."""
    if groups is None or not len(values):
        return float("nan")
    return float(values.groupby(groups).mean().mean())


def bonus_metrics(parts, teams, response_scores=None):
    """Return part-, exact-bonus-, and team-level PPB metrics.

    Part correctness is reported as both a micro average and macro averages by
    team and bonus question. Exact accuracy requires all three part
    classifications to match. PPB pools responses by team before calculating
    mean absolute error, giving every observed team equal weight.
    'response_scores' lets a caller that already built the per-response score
    table pass it in rather than paying for the response walk twice.
    """
    metrics = classification_metrics(parts["correct"], parts["predicted_correct"])
    metrics["part_accuracy"] = metrics.pop("accuracy")
    metrics["part_all_correct_accuracy"] = metrics.pop("all_correct_accuracy")
    for row in bonus_accuracy_by_difficulty(parts).itertuples(index=False):
        metrics[f"part_accuracy_{row.difficulty}"] = row.part_accuracy
        metrics[f"part_count_{row.difficulty}"] = row.parts
    part_matches = (parts["predicted_correct"] >= 0.5) == parts["correct"].astype(bool)
    metrics["part_accuracy_macro_team"] = _macro_group_mean(
        part_matches, parts["team_id"] if "team_id" in parts else None
    )
    metrics["part_accuracy_macro_bonus"] = _macro_group_mean(
        part_matches, parts["bonus_id"] if "bonus_id" in parts else None
    )
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

    if response_scores is None:
        response_scores = bonus_ranked_probability_scores(parts)
    metrics["ranked_probability_score"] = (
        float(response_scores["rps"].mean()) if not response_scores.empty else float("nan")
    )
    metrics["ranked_probability_score_responses"] = len(response_scores)
    metrics["bonus_total_score_log_loss"] = (
        float(response_scores["score_log_loss"].mean())
        if not response_scores.empty
        else float("nan")
    )
    metrics["bonus_total_score_log_loss_responses"] = len(response_scores)

    team_ppb = teams.groupby("team_id", as_index=False).agg(
        observed_ppb=("total_points", "mean"),
        predicted_ppb=("predicted_points", "mean"),
    )
    metrics["ppb_mae"] = (
        mean_absolute_error(team_ppb["observed_ppb"], team_ppb["predicted_ppb"])
        if not team_ppb.empty
        else float("nan")
    )
    return metrics
