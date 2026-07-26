"""Tossup correctness calibration, stratified by buzz timing.

A single aggregate reliability curve ('compirt_eval.common.figures.reliability_plot',
used directly by 'evaluate_tossups') can hide whether the model is
well-calibrated early in a question but overconfident late, or vice versa.
'stratified_tossup_reliability_plot' breaks the same calibration check into
five fixed relative-position bands so that pattern is visible.  These are
equal-width fifths of the question, not sample-dependent empirical quantiles.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from compirt_eval.common.metrics import calibration_table, classification_metrics
from compirt_eval.common.report_paths import csv_path, graph_path


BUZZ_POSITION_EDGES = (0.0, 0.2, 0.4, 0.6, 0.8, 1.0)
BUZZ_POSITION_LABELS = (
    "Q1 (0-.2)",
    "Q2 (.2-.4)",
    "Q3 (.4-.6)",
    "Q4 (.6-.8)",
    "Q5 (.8-1)",
)


def stratified_tossup_reliability_plot(buzz, output_dir):
    """Plot tossup calibration separately for five fixed position bands."""
    buzz = buzz.copy()
    buzz["position_group"] = pd.cut(
        buzz["relative_position"],
        bins=BUZZ_POSITION_EDGES,
        labels=BUZZ_POSITION_LABELS,
        include_lowest=True,
    )
    rows = []
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.plot([0, 1], [0, 1], "--", color="0.5", label="Perfect calibration")
    for label in BUZZ_POSITION_LABELS:
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
        graph_path(
            output_dir, "tossup_reliability_by_buzz_position.png", "tossup"
        ),
        dpi=160
    )
    plt.close(fig)
    pd.DataFrame(rows).to_csv(
        csv_path(output_dir, "tossup_metrics_by_buzz_position.csv"), index=False
    )
