"""Tossup correctness calibration, stratified by buzz timing.

A single aggregate reliability curve ('compirt_eval.figures.reliability_plot',
used directly by 'evaluate_tossups') can hide whether the model is
well-calibrated early in a question but overconfident late, or vice versa.
'stratified_tossup_reliability_plot' breaks the same calibration check into
early/middle/late buzz-position thirds so that pattern is visible.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from compirt_eval.metrics import calibration_table, classification_metrics
from compirt_eval.outputs import csv_path, graph_path


def stratified_tossup_reliability_plot(buzz, output_dir):
    """Plot tossup calibration separately for early, middle, and late buzzes."""
    labels = ["Early third", "Middle third", "Late third"]
    buzz = buzz.copy()
    buzz["position_group"] = pd.cut(
        buzz["relative_position"],
        bins=[0.0, 1 / 3, 2 / 3, 1.0],
        labels=labels,
        include_lowest=True,
    )
    rows = []
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.plot([0, 1], [0, 1], "--", color="0.5", label="Perfect calibration")
    for label in labels:
        group = buzz[buzz["position_group"] == label]
        if group.empty:
            continue
        metrics = classification_metrics(group["y"], group["predicted_correct"])
        rows.append({"position_group": label, "observations": len(group), **metrics})
        calibration = calibration_table(group["y"], group["predicted_correct"], n_bins=8)
        ax.plot(
            calibration["predicted"],
            calibration["observed"],
            "o-",
            label=f"{label} (n={len(group):,}, ECE={metrics['ece']:.3f})",
        )
    ax.set(
        title="Tossup reliability by buzz position",
        xlabel="Predicted probability",
        ylabel="Observed correctness",
        xlim=(0, 1),
        ylim=(0, 1),
    )
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(
        graph_path(output_dir, "tossup_reliability_by_buzz_position.png"), dpi=160
    )
    plt.close(fig)
    pd.DataFrame(rows).to_csv(
        csv_path(output_dir, "tossup_metrics_by_buzz_position.csv"), index=False
    )
