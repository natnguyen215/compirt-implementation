"""Compare saved no-synergy and synergy bonus evaluation metrics."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.eval_docs import markdown_table, write_eval_docs_summary


LOWER_IS_BETTER = {
    "log_loss",
    "ece",
    "per_bonus_points_mae",
    "ppb_mae",
}
LEGACY_METRIC_NAMES = {
    "exact_score_accuracy": "rounded_score_accuracy",
}


def resolve_metrics_path(path: Path) -> Path:
    """Return the requested metrics file, accepting the legacy flat eval layout."""
    if path.exists():
        return path
    nested = path.parent / "csvs" / path.name
    if nested.exists():
        return nested
    return path


def evaluation_dir_from_metrics_path(path: Path) -> Path | None:
    """Infer an evaluation directory from a bonus_metrics.csv path."""
    resolved = resolve_metrics_path(path)
    if not resolved.exists():
        return None
    if resolved.parent.name == "csvs":
        return resolved.parent.parent
    return resolved.parent


def comparison_plot(comparison, output_dir):
    """Plot an honest overall comparison of the two fitted bonus variants."""
    if comparison.empty:
        return

    columns = 3
    rows = math.ceil(len(comparison) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(12, 3.2 * rows), squeeze=False)
    for ax, row in zip(axes.flat, comparison.itertuples(index=False)):
        values = [row.no_synergy, row.synergy]
        bars = ax.bar(
            ["No synergy", "Synergy"],
            values,
            color=["tab:blue", "tab:orange"],
            alpha=0.75,
        )
        finite = [value for value in values if np.isfinite(value)]
        if finite:
            padding = max(
                max(finite) - min(finite),
                max(abs(value) for value in finite) * 0.08,
                1e-3,
            )
            ax.set_ylim(min(0, min(finite) - padding), max(finite) + padding)
        for bar, value in zip(bars, values):
            if np.isfinite(value):
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    value,
                    f"{value:.3g}",
                    ha="center",
                    va="bottom",
                    fontsize=8,
                )
        direction = (
            "lower is better"
            if row.metric in LOWER_IS_BETTER
            else "higher is better"
        )
        ax.set_title(f"{row.metric}\n{direction}", fontsize=10)
        ax.tick_params(axis="x", labelrotation=15)
        ax.grid(alpha=0.2, axis="y")
    for ax in axes.flat[len(comparison):]:
        ax.set_visible(False)
    fig.suptitle("Overall fitted bonus-model comparison")
    fig.tight_layout()
    fig.savefig(output_dir / "bonus_model_comparison.png", dpi=160)
    plt.close(fig)


def normalize_metric_names(row: pd.Series) -> pd.Series:
    """Return a metrics row using current metric names where legacy CSVs differ."""
    renamed = row.rename(index=LEGACY_METRIC_NAMES)
    return renamed[~renamed.index.duplicated(keep="first")]


def main():
    """Diff two saved bonus-metric CSVs and write a comparison CSV, figure, and report.

    Reads the 'bonus_metrics.csv' from a no-synergy and a synergy evaluation
    run, aligns their shared metrics, and records which variant wins each one
    in-sample. The result is diagnostic only -- both runs are scored on their
    training observations, so it does not show that synergy generalizes.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compositional-metrics", type=Path, required=True)
    parser.add_argument("--synergy-metrics", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    compositional = pd.read_csv(
        resolve_metrics_path(args.compositional_metrics)
    ).iloc[0]
    synergy = pd.read_csv(resolve_metrics_path(args.synergy_metrics)).iloc[0]
    compositional = normalize_metric_names(compositional)
    synergy = normalize_metric_names(synergy)
    common_metrics = [metric for metric in compositional.index if metric in synergy.index]

    rows = []
    for metric in common_metrics:
        compositional_value = pd.to_numeric(compositional[metric], errors="coerce")
        synergy_value = pd.to_numeric(synergy[metric], errors="coerce")
        if pd.isna(compositional_value) or pd.isna(synergy_value):
            continue
        compositional_value = float(compositional_value)
        synergy_value = float(synergy_value)
        delta = synergy_value - compositional_value
        if delta == 0:
            better = "tie"
        elif metric in LOWER_IS_BETTER:
            better = "synergy" if delta < 0 else "no-synergy"
        else:
            better = "synergy" if delta > 0 else "no-synergy"
        rows.append(
            {
                "metric": metric,
                "no_synergy": compositional_value,
                "synergy": synergy_value,
                "synergy_minus_no_synergy": delta,
                "better_in_sample": better,
            }
        )

    comparison = pd.DataFrame(rows)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    comparison.to_csv(args.output_dir / "bonus_model_comparison.csv", index=False)
    comparison_plot(comparison, args.output_dir)
    report = (
        "# CompIRT Bonus Model Comparison\n\n"
        + markdown_table(comparison)
        + "\n\nThese metrics use the same observations for training and evaluation. "
        "They diagnose fit but do not establish that synergy generalizes to "
        "unseen team compositions.\n"
    )
    (args.output_dir / "bonus_model_comparison.md").write_text(report, encoding="utf-8")
    comparison_csv = args.output_dir / "bonus_model_comparison.csv"
    for metrics_path_arg in (args.compositional_metrics, args.synergy_metrics):
        evaluation_dir = evaluation_dir_from_metrics_path(metrics_path_arg)
        if evaluation_dir is not None:
            write_eval_docs_summary(evaluation_dir, comparison_csv)


if __name__ == "__main__":
    main()
