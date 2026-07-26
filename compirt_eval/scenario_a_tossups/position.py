"""Buzz-position error metrics and figures for Scenario A."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, median_absolute_error

from compirt_eval.common.report_paths import csv_path, graph_path
from compirt_eval.scenario_a_tossups.metrics import buzz_position_bias_table
from compirt_eval.scenario_a_tossups.reliability import (
    BUZZ_POSITION_EDGES,
    BUZZ_POSITION_LABELS,
)


def evaluate_buzz_positions(events, output_dir):
    """Write buzz-position diagnostics and return their scalar metrics."""
    if events.empty:
        return {}
    bias_table = buzz_position_bias_table(
        events, BUZZ_POSITION_EDGES, BUZZ_POSITION_LABELS
    )
    bias_table.to_csv(csv_path(output_dir, "buzz_position_bias.csv"), index=False)
    metrics = {
        "buzz_position_mae": mean_absolute_error(
            events["observed_relative_position"],
            events["predicted_relative_position"],
        ),
        "buzz_position_median_absolute_error": median_absolute_error(
            events["observed_relative_position"],
            events["predicted_relative_position"],
        ),
        "buzz_position_bias": float(bias_table.loc[0, "mean_signed_error"]),
    }

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(
        events["observed_relative_position"],
        events["predicted_relative_position"],
        alpha=0.25,
    )
    ax.plot([0, 1], [0, 1], "--", color="0.5")
    ax.set(
        title="Observed versus predicted buzz position",
        xlabel="Observed",
        ylabel="Predicted",
        xlim=(0, 1),
        ylim=(0, 1),
    )
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(
        graph_path(output_dir, "tossup_position_predictions.png", "tossup"),
        dpi=160,
    )
    plt.close(fig)
    _binned_buzz_position_plot(events, output_dir)
    return metrics


def _binned_buzz_position_plot(events, output_dir, bins=10):
    """Plot conditional mean buzz-position predictions in observed bands."""
    edges = np.linspace(0.0, 1.0, bins + 1)
    grouped = events.groupby(
        pd.cut(events["observed_relative_position"], edges, include_lowest=True),
        observed=True,
    )["predicted_relative_position"]
    summary = pd.DataFrame(
        {
            "predicted_mean": grouped.mean(),
            "predicted_p10": grouped.quantile(0.10),
            "predicted_p90": grouped.quantile(0.90),
            "events": grouped.size(),
        }
    )
    summary.index = [interval.mid for interval in summary.index]
    fig, ax = plt.subplots(figsize=(6.5, 6))
    ax.plot([0, 1], [0, 1], "--", color="0.5", label="Perfect calibration")
    ax.fill_between(
        summary.index,
        summary["predicted_p10"],
        summary["predicted_p90"],
        alpha=0.2,
        label="10th-90th percentile",
    )
    ax.plot(summary.index, summary["predicted_mean"], "o-", label="Mean prediction")
    ax.set(
        title=f"Binned buzz-position calibration ({len(events):,} events)",
        xlabel="Observed position (bin center)",
        ylabel="Predicted position",
        xlim=(0, 1),
        ylim=(0, 1),
    )
    ax.grid(alpha=0.25)
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(
        graph_path(output_dir, "tossup_position_calibration.png", "tossup"), dpi=160
    )
    plt.close(fig)
