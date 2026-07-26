"""CSV and figure writers for the two drop-robustness tiers."""

from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-compirt")

import matplotlib.pyplot as plt
import pandas as pd

from compirt_eval.common.report_paths import csv_path, graph_path

MODEL_COLORS = {
    "actual": "tab:gray",
    "plain": "tab:orange",
    "baseline": "tab:blue",
    "multidim": "tab:green",
}


def save_metric_curves(
    root: Path, frame: pd.DataFrame, metric: str, filename: str, ylabel: str
) -> None:
    """Plot drop curves and each model family's fraction-zero noise band."""
    fig, ax = plt.subplots(figsize=(8, 5))
    dropped = frame[frame["fraction"] > 0]
    for model, group in dropped.groupby("model"):
        curve = group.groupby("fraction")[metric].mean()
        color = MODEL_COLORS.get(model)
        ax.plot(curve.index, curve.values, marker="o", label=model, color=color)
        scatter = group[["fraction", metric]].dropna()
        ax.scatter(scatter["fraction"], scatter[metric], s=12, alpha=0.45, color=color)
    for model, group in frame[frame["fraction"] == 0.0].groupby("model"):
        values = group[metric].dropna()
        if values.empty:
            continue
        ax.axhspan(
            values.min(),
            values.max(),
            color=MODEL_COLORS.get(model),
            alpha=0.12,
            label=f"{model} seed noise",
        )
    ax.set_xscale("log")
    ax.set(
        title=f"{ylabel} vs. dropped-event fraction",
        xlabel="Fraction of buzz events dropped (log scale)",
        ylabel=ylabel,
    )
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(graph_path(root, filename), dpi=160)
    plt.close(fig)


def save_tier1_outputs(root: Path, frame: pd.DataFrame) -> Path:
    output = csv_path(root, "drop_robustness_metrics.csv")
    frame.to_csv(output, index=False)
    if not frame.empty:
        save_metric_curves(
            root, frame, "kendall_tau", "kendall_tau_vs_fraction.png", "Kendall tau"
        )
        save_metric_curves(
            root,
            frame,
            "jaccard_top10",
            "topk_jaccard_vs_fraction.png",
            "Top-10 Jaccard",
        )
    return output


def save_targeted_outputs(
    root: Path, frame: pd.DataFrame, actual: pd.DataFrame
) -> None:
    frame.to_csv(csv_path(root, "targeted_flip_metrics.csv"), index=False)
    actual.to_csv(csv_path(root, "actual_flip_curve.csv"), index=False)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        actual["n_dropped"],
        actual["gap"],
        label="actual",
        color=MODEL_COLORS["actual"],
        linewidth=1,
    )
    for model, group in frame.groupby("model"):
        group = group.dropna(subset=["gap"]).sort_values("n_dropped")
        color = MODEL_COLORS.get(model)
        ax.plot(
            group["n_dropped"], group["gap"], marker="o", label=model, color=color
        )
        std = group["noise_gap_std"].iloc[0]
        if pd.notna(std):
            base = group[group["n_dropped"] == 0]
            if not base.empty:
                ax.errorbar(
                    base["n_dropped"],
                    base["gap"],
                    yerr=std,
                    fmt="none",
                    color=color,
                    capsize=4,
                )
    ax.axhline(0.0, color="black", linewidth=0.8, linestyle="--")
    ax.set(
        title="Target-vs-rival PPG gap as events are dropped",
        xlabel="Dropped events (target's strongest evidence first)",
        ylabel="Predicted PPG gap (target - rival)",
    )
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(graph_path(root, "gap_vs_dropped.png"), dpi=160)
    plt.close(fig)
