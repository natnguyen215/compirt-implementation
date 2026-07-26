"""Pure scoring calculations owned by Scenario A tossup evaluation.

These functions operate on saved tossup prediction frames and return tables;
they do not read files or create figures. Shared binary-classification metrics
remain in :mod:`compirt_eval.common.metrics`.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def buzz_position_bias_table(events, edges, labels):
    """Return signed buzz-position error rows: one overall plus one per band.

    The signed error is predicted minus observed relative position, so a
    positive value means the buzz was predicted later than it happened.
    Errors of opposite sign early and late in the question can cancel in the
    overall row, which is why the fixed observed-position bands are reported
    alongside it.
    """
    error = (
        events["predicted_relative_position"] - events["observed_relative_position"]
    )
    rows = [
        {
            "band": "overall",
            "events": len(events),
            "mean_signed_error": float(error.mean()),
            "median_signed_error": float(error.median()),
        }
    ]
    bands = pd.cut(
        events["observed_relative_position"],
        bins=list(edges),
        labels=list(labels),
        include_lowest=True,
    )
    for label, band_error in error.groupby(bands, observed=False):
        rows.append(
            {
                "band": str(label),
                "events": int(band_error.size),
                "mean_signed_error": float(band_error.mean()),
                "median_signed_error": float(band_error.median()),
            }
        )
    return pd.DataFrame(rows)


def tossup_joint_event_scores(predictions):
    """Return one fitted competing-risks log-score row per tossup event.

    The saved prediction rows contain the three factors used by the model
    likelihood: every rostered player's survival to the stopping token, the
    first buzzer's hazard at that token, and the probability of the observed
    correctness result. A dead tossup contains only the roster survival term.
    """
    columns = [
        "event_id",
        "game_id",
        "tossup_id",
        "observed_outcome",
        "observed_player_id",
        "observed_token",
        "observed_relative_position",
        "observed_correct",
        "survival_probability",
        "hazard_probability",
        "correctness_outcome_probability",
        "joint_event_probability",
        "joint_event_log_loss",
    ]
    required = {
        "event_id",
        "z",
        "predicted_survival",
        "predicted_hazard",
        "predicted_correct",
    }
    if predictions.empty or not required.issubset(predictions.columns):
        return pd.DataFrame(columns=columns)

    # Evaluation is phase-0-only for comparability. Bounceback runs add phase-1
    # 'BOUNCE-*' rows sharing an event_id; their survival must not multiply into
    # this score without their (excluded) hazard/correctness event terms, or the
    # result is neither a phase-0 nor a full-sequence likelihood. Dropping them
    # keeps a clean phase-0 competing-risks score. 'z' is always present; the
    # prefix is absent from pre-bounceback runs.
    predictions = predictions[~predictions["z"].astype(str).str.startswith("BOUNCE")]

    rows = []
    for event_id, event in predictions.groupby("event_id", sort=False):
        survival = np.clip(
            event["predicted_survival"].to_numpy(dtype=float), 0.0, 1.0
        )
        survival_probability = float(np.prod(survival))
        joint_probability = survival_probability
        buzz = event[event["z"] == "BUZZ"]

        row = {
            "event_id": event_id,
            "game_id": event["game_id"].iloc[0] if "game_id" in event else "",
            "tossup_id": (
                event["tossup_id"].iloc[0] if "tossup_id" in event else ""
            ),
            "survival_probability": survival_probability,
        }
        if buzz.empty:
            row.update(
                {
                    "observed_outcome": "dead",
                    "observed_player_id": "",
                    "observed_token": np.nan,
                    "observed_relative_position": np.nan,
                    "observed_correct": np.nan,
                    "hazard_probability": np.nan,
                    "correctness_outcome_probability": np.nan,
                }
            )
        else:
            if len(buzz) != 1:
                raise ValueError(
                    f"Tossup event {event_id!r} requires exactly one BUZZ row"
                )
            observed = buzz.iloc[0]
            hazard = float(np.clip(observed["predicted_hazard"], 0.0, 1.0))
            correctness = float(np.clip(observed["predicted_correct"], 0.0, 1.0))
            observed_correct = int(observed["y"])
            correctness_outcome = (
                correctness if observed_correct else 1.0 - correctness
            )
            joint_probability *= hazard * correctness_outcome
            row.update(
                {
                    "observed_outcome": (
                        "correct_buzz" if observed_correct else "incorrect_buzz"
                    ),
                    "observed_player_id": observed.get("player_id", ""),
                    "observed_token": observed.get("t_star", np.nan),
                    "observed_relative_position": observed.get(
                        "relative_position", np.nan
                    ),
                    "observed_correct": observed_correct,
                    "hazard_probability": hazard,
                    "correctness_outcome_probability": correctness_outcome,
                }
            )
        row["joint_event_probability"] = joint_probability
        row["joint_event_log_loss"] = float(
            -np.log(np.clip(joint_probability, 1e-12, 1.0))
        )
        rows.append(row)
    return pd.DataFrame(rows, columns=columns)
