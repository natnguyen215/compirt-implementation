"""Slice scoring shared by the analysis modules.

Metrics are never reimplemented here: classification and bonus metrics come
from `compirt_eval.metrics`, the same functions the committed evaluator calls,
so a slice can never silently drift from the headline number it decomposes.
The only additions are the Murphy decomposition of the Brier score (which the
evaluator does not report) and the buzz-position error over the merged
prediction frame.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, median_absolute_error

from compirt_eval.metrics import bonus_metrics, classification_metrics

LOWER_IS_BETTER = {
    "log_loss",
    "ece",
    "brier",
    "reliability",
    "buzz_position_mae",
    "buzz_position_median_absolute_error",
    "per_bonus_points_mae",
    "ppb_mae",
}


def murphy_decomposition(y, probability, n_bins=10):
    """Split the Brier score into calibration and discrimination.

    Brier = reliability - resolution + uncertainty (Murphy 1973). This settles
    arguments that AUC and log loss cannot: log loss confounds *being
    calibrated* with *telling cases apart*, and AUC ignores calibration
    entirely, so when they rank slices in opposite orders neither adjudicates.

    - `reliability` (lower better): squared gap between predicted and observed
      frequency within each probability bin — pure calibration.
    - `resolution` (higher better): how far each bin's observed rate departs
      from the base rate — pure discrimination.
    - `uncertainty`: the base rate's own variance. A property of the slice, not
      the model, so it cancels in any between-dimension comparison.

    Binned, so exact only up to discretization; `residual` reports how far the
    identity misses and should be ~0.
    """
    y = np.asarray(y, dtype=float)
    probability = np.clip(np.asarray(probability, dtype=float), 0.0, 1.0)
    if len(y) == 0:
        return dict.fromkeys(
            ("brier", "reliability", "resolution", "uncertainty", "base_rate", "residual"),
            float("nan"),
        )

    base_rate = float(y.mean())
    brier = float(np.mean((probability - y) ** 2))

    bins = np.linspace(0.0, 1.0, n_bins + 1)
    bucket = np.clip(np.digitize(probability, bins) - 1, 0, n_bins - 1)
    reliability = 0.0
    resolution = 0.0
    for index in range(n_bins):
        selected = bucket == index
        count = int(selected.sum())
        if count == 0:
            continue
        reliability += count * (probability[selected].mean() - y[selected].mean()) ** 2
        resolution += count * (y[selected].mean() - base_rate) ** 2
    reliability /= len(y)
    resolution /= len(y)
    uncertainty = base_rate * (1.0 - base_rate)

    return {
        "brier": brier,
        "reliability": float(reliability),
        "resolution": float(resolution),
        "uncertainty": float(uncertainty),
        "base_rate": base_rate,
        "residual": float(brier - (reliability - resolution + uncertainty)),
    }


def buzz_position_error(frame):
    """Buzz-position MAE, defined exactly as compirt_eval.tossups.evaluate_tossups.

    The pyramidal model's own metric — *when* a player buzzes, not just whether
    they are right. It conditions on a buzz having happened, so dead tossups
    are outside it by construction.
    """
    if "predicted_relative_position" not in frame.columns:
        return {}
    events = frame.dropna(subset=["observed_relative_position", "predicted_relative_position"])
    if events.empty:
        return {
            "buzz_position_mae": float("nan"),
            "buzz_position_median_absolute_error": float("nan"),
        }
    observed = events["observed_relative_position"]
    predicted = events["predicted_relative_position"]
    return {
        "buzz_position_mae": float(mean_absolute_error(observed, predicted)),
        "buzz_position_median_absolute_error": float(
            median_absolute_error(observed, predicted)
        ),
    }


def score(frame):
    """Every tossup metric for one slice, plus its size.

    `classification_metrics` drops the `accuracy` key entirely on an empty
    frame, so seed the row with NaNs first — otherwise an empty slice yields a
    row with different columns from every other row.
    """
    row = {
        "observations": len(frame),
        "auc": float("nan"),
        "log_loss": float("nan"),
        "ece": float("nan"),
        "accuracy": float("nan"),
    }
    row.update(classification_metrics(frame["y"], frame["predicted_correct"]))
    row.update(murphy_decomposition(frame["y"], frame["predicted_correct"]))
    row.update(buzz_position_error(frame))
    return row


def score_bonuses(parts, teams):
    """Every bonus metric for one slice, via the committed `bonus_metrics`.

    PPB is a game/team-level quantity, so it needs the team table as well as
    the parts table — which is why this cannot reuse `score`.
    """
    row = {"observations": len(parts), "responses": len(teams)}
    if parts.empty or teams.empty:
        return row
    row.update(bonus_metrics(parts, teams))
    row.update(murphy_decomposition(parts["correct"], parts["predicted_correct"]))
    return row


def is_monotone(frame, metric):
    """Does `metric` improve at every consecutive dimension?

    A weak noise filter, not a significance test: under iid noise with no trend
    the chance of six same-direction steps is ~1/64, and correlated metrics on
    the same predictions are not independent confirmations.
    """
    usable = frame.dropna(subset=[metric]).sort_values("dimension")
    if len(usable) < 3:
        return False
    steps = usable[metric].diff().dropna()
    return bool((steps < 0).all() if metric in LOWER_IS_BETTER else (steps > 0).all())


def endpoint_change(frame, metric, **filters):
    """(first, last, change, monotone, n) for one metric over the sweep."""
    subset = frame
    for column, value in filters.items():
        subset = subset[subset[column] == value]
    subset = subset.dropna(subset=[metric]).sort_values("dimension")
    if subset.empty:
        return float("nan"), float("nan"), float("nan"), False, 0
    return (
        subset[metric].iloc[0],
        subset[metric].iloc[-1],
        subset[metric].iloc[-1] - subset[metric].iloc[0],
        is_monotone(subset, metric),
        int(subset["observations"].iloc[0]),
    )


def print_frame(title, frame):
    """Print one table the way every module reports: name, then the frame."""
    pd.set_option("display.width", 220)
    print(f"\n== {title} ==")
    print(frame.to_string(index=False, float_format=lambda v: f"{v:.4f}"))
