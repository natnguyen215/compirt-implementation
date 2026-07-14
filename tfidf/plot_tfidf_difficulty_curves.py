"""Plot cumulative TF-IDF difficulty diagnostics for a fitted TF-IDF run."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from compirt_eval.figures import short_id
from compirt_eval.metrics import difficulty_curve
from compirt_eval.tossups.difficulty import selected_tossups
from tfidf.pyramidal_tfidf_model import (
    CUMULATIVE_DIFFICULTY,
    tfidf_score_at,
)
from tfidf.tfidf_features import attach_tfidf_prefix_scores


def load_run_context(results_dir: Path, data_dir: Path):
    """Load saved run outputs and recompute aligned TF-IDF feature matrices."""
    summary_path = results_dir / "summary.json"
    if not summary_path.exists():
        raise FileNotFoundError(f"Missing summary: {summary_path}")
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    split = summary.get("split", "all")
    tournament = summary.get("tournament") or None
    tables = filter_tournament(load_hf_tables(data_dir, split), tournament)
    observations = build_tossup_observations(tables)
    data = tossup_tensors(observations)
    tfidf_feature_summary = summary.get("tfidf_features", {})
    attach_tfidf_prefix_scores(
        data,
        tables,
        normalize=tfidf_feature_summary.get("normalized", True),
    )
    return summary, data


def _numbered_labels(row, prefix):
    return sorted(
        (
            label
            for label in row.index
            if isinstance(label, str)
            and label.startswith(prefix)
            and label.removeprefix(prefix).isdigit()
        ),
        key=lambda label: int(label.removeprefix(prefix)),
    )


def _relevance_labels(row):
    """Return vector-weight columns: 'r_*' for multidim runs, 'alpha_*' for older ones."""
    relevance_columns = _numbered_labels(row, "r_")
    alpha_columns = _numbered_labels(row, "alpha_")
    if relevance_columns and alpha_columns:
        raise ValueError("Saved vector weights must use either r_* or alpha_*, not both")
    return relevance_columns or alpha_columns


def _multidim_columns(row):
    return {
        "r": _relevance_labels(row),
        "beta": _numbered_labels(row, "beta_"),
        "gamma": _numbered_labels(row, "gamma_"),
        "mu": _numbered_labels(row, "mu_"),
    }


def _saved_difficulty(row, positions):
    """Return scalar or relevance-weighted multidim difficulty over 'positions'.

    Scalar runs save 'beta'/'gamma'/'mu' columns; multidim runs save numbered
    'r_K'/'beta_K'/'gamma_K'/'mu_K' columns, which are collapsed with the
    same 'sum_k r_jk * d_jk(t)' weighting the model uses.
    """
    positions = np.asarray(positions, dtype=float)
    if {"beta", "gamma", "mu"}.issubset(row.index):
        return difficulty_curve(row.beta, row.gamma, row.mu, positions)

    columns = _multidim_columns(row)
    if not all(columns[name] for name in ("r", "beta", "gamma", "mu")):
        raise ValueError("TF-IDF plot requires scalar or multidim difficulty columns")
    dimensions = {len(columns[name]) for name in ("r", "beta", "gamma", "mu")}
    if len(dimensions) != 1:
        raise ValueError("Multidim TF-IDF difficulty columns must have matching widths")

    r = row[columns["r"]].to_numpy(dtype=float)
    per_dimension = difficulty_curve(
        row[columns["beta"]].to_numpy(dtype=float)[:, None],
        row[columns["gamma"]].to_numpy(dtype=float)[:, None],
        row[columns["mu"]].to_numpy(dtype=float)[:, None],
        positions[None, :],
    )
    return r @ per_dimension


def _relevance_mass(row):
    """Return sum_k r_jk for multidim rows, or 1.0 for scalar rows."""
    columns = _multidim_columns(row)
    if columns["r"] and not {"beta", "gamma", "mu"}.issubset(row.index):
        return float(row[columns["r"]].to_numpy(dtype=float).sum())
    return 1.0


def curve_components(row, features, summary, relative_positions):
    """Return base/effective curves plus the TF-IDF diagnostic series."""
    token_positions = np.maximum(
        1, np.rint(relative_positions * features["T"]).astype(int)
    )
    token_positions = np.minimum(token_positions, features["T"])
    t = features["prefix"].new_tensor(token_positions)
    base = _saved_difficulty(row, relative_positions)
    prefix = tfidf_score_at(features["prefix"], t).detach().cpu().numpy()
    variant = summary.get("tfidf_variant", CUMULATIVE_DIFFICULTY)
    if variant != CUMULATIVE_DIFFICULTY:
        raise ValueError(f"Unknown TF-IDF variant in summary: {variant}")
    adjustment = -float(summary["tfidf_clue_effect"]) * prefix * _relevance_mass(row)
    return {
        "base": base,
        "effective": base + adjustment,
        "delta": adjustment,
        "delta_label": "Difficulty reduction",
        "score": prefix,
        "score_label": "idf_prefix",
    }


def plot_curves(results_dir: Path, output_dir: Path, data_dir: Path, count: int):
    """Write TF-IDF variant diagnostic plots."""
    summary, data = load_run_context(results_dir, data_dir)
    parameters = pd.read_csv(results_dir / "tossups.csv").set_index("tossup_id")
    predictions = pd.read_csv(results_dir / "tossup_predictions.csv")
    tossup_index = {tossup_id: index for index, tossup_id in enumerate(data["tossup_ids"])}

    selected = [
        tossup_id
        for tossup_id in selected_tossups(predictions, count=count)
        if tossup_id in parameters.index and tossup_id in tossup_index
    ]
    if not selected:
        raise ValueError("No tossups available for TF-IDF plotting")

    output_dir.mkdir(parents=True, exist_ok=True)
    columns = 2
    rows = math.ceil(len(selected) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(13, 4.3 * rows), squeeze=False)
    positions = np.linspace(0.0, 1.0, 160)
    variant = summary.get("tfidf_variant", CUMULATIVE_DIFFICULTY)

    for ax, tossup_id in zip(axes.flat, selected):
        row = parameters.loc[tossup_id]
        index = tossup_index[tossup_id]
        T = int(predictions.loc[predictions["tossup_id"] == tossup_id, "T_j"].iloc[0])
        features = {
            "T": T,
            "prefix": data["tfidf_prefix"][index],
        }
        curves = curve_components(row, features, summary, positions)

        buzz_positions = predictions.loc[
            (predictions["tossup_id"] == tossup_id) & (predictions["z"] == "BUZZ"),
            "relative_position",
        ]
        ax.hist(
            buzz_positions,
            bins=np.linspace(0, 1, 11),
            color="tab:orange",
            alpha=0.22,
            label=f"Observed buzzes (n={len(buzz_positions)})",
        )
        curve_ax = ax.twinx()
        curve_ax.plot(
            positions,
            curves["base"],
            color="tab:blue",
            linewidth=1.5,
            alpha=0.65,
            label="Base difficulty d(t)",
        )
        curve_ax.plot(
            positions,
            curves["effective"],
            color="black",
            linewidth=2.2,
            label="Effective difficulty d'(t)",
        )
        curve_ax.plot(
            positions,
            curves["delta"],
            color="tab:green",
            linewidth=1.4,
            linestyle="--",
            label=curves["delta_label"],
        )
        score_ax = ax.twinx()
        score_ax.spines["right"].set_position(("axes", 1.09))
        score_ax.plot(
            positions,
            curves["score"],
            color="tab:red",
            linewidth=1.0,
            alpha=0.6,
            label=curves["score_label"],
        )
        if curves["score_label"] == "idf_prefix":
            score_ax.set_ylim(-0.03, 1.03)
        score_ax.set_yticks([])

        ax.set(
            title=short_id(tossup_id),
            xlabel="Relative position",
            ylabel="Buzz count",
            xlim=(0, 1),
        )
        curve_ax.set_ylabel("Difficulty / logit delta")
        ax.grid(alpha=0.2)
        handles, labels = ax.get_legend_handles_labels()
        curve_handles, curve_labels = curve_ax.get_legend_handles_labels()
        score_handles, score_labels = score_ax.get_legend_handles_labels()
        ax.legend(
            handles + curve_handles + score_handles,
            labels + curve_labels + score_labels,
            fontsize=6.5,
            loc="upper right",
        )

    for ax in axes.flat[len(selected):]:
        ax.set_visible(False)
    fig.suptitle(f"TF-IDF {variant} diagnostics and empirical buzz locations")
    fig.tight_layout()
    output_path = output_dir / "tfidf_effective_difficulty_curves.png"
    fig.savefig(output_path, dpi=160)
    plt.close(fig)
    return output_path


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--count", type=int, default=6)
    args = parser.parse_args()
    if args.count < 1:
        raise ValueError("--count must be at least 1")
    if args.output_dir is None:
        args.output_dir = args.results_dir.parent / "evaluation" / "graphs"
    return args


if __name__ == "__main__":
    args = parse_args()
    path = plot_curves(args.results_dir, args.output_dir, args.data_dir, args.count)
    print(path)
