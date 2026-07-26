"""Prediction figures owned by Scenario B bonus evaluation."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from compirt_eval.common.report_paths import graph_path


def team_ppb_plot(teams, output_dir):
    """Plot predicted against observed points per bonus, one point per team."""
    team_ppb = teams.groupby("team_id", as_index=False).agg(
        observed_ppb=("total_points", "mean"),
        predicted_ppb=("predicted_points", "mean"),
    )
    if team_ppb.empty:
        return
    ppb_mae = float(
        (team_ppb["observed_ppb"] - team_ppb["predicted_ppb"]).abs().mean()
    )
    fig, ax = plt.subplots(figsize=(6.5, 6.5))
    ax.scatter(
        team_ppb["observed_ppb"],
        team_ppb["predicted_ppb"],
        s=16,
        alpha=0.4,
        label=f"MAE = {ppb_mae:.3f} ({len(team_ppb):,} teams)",
    )
    ax.plot([0, 30], [0, 30], "--", color="0.5")
    ax.set(
        title="Predicted versus observed points per bonus by team",
        xlabel="Observed PPB",
        ylabel="Predicted PPB",
        xlim=(0, 30),
        ylim=(0, 30),
    )
    ax.grid(alpha=0.25)
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(
        graph_path(output_dir, "bonus_team_ppb_predictions.png", "bonus"), dpi=160
    )
    plt.close(fig)


def bonus_score_by_observed_plot(teams, output_dir):
    """Plot predicted expected points grouped by observed bonus score."""
    scores = (0, 10, 20, 30)
    score_groups = [
        (
            score,
            teams.loc[teams["total_points"] == score, "predicted_points"].to_numpy(),
        )
        for score in scores
    ]
    score_groups = [(score, values) for score, values in score_groups if len(values)]
    if not score_groups:
        return

    observed_scores, groups = zip(*score_groups)
    positions = np.arange(len(groups))
    fig, ax = plt.subplots(figsize=(8, 6))
    boxes = ax.boxplot(
        groups,
        positions=positions,
        widths=0.55,
        patch_artist=True,
        showfliers=False,
        medianprops={"color": "black"},
    )
    for box in boxes["boxes"]:
        box.set(facecolor="tab:blue", alpha=0.25)
    rng = np.random.default_rng(0)
    for position, values in zip(positions, groups):
        jitter = rng.normal(position, 0.055, len(values))
        ax.scatter(jitter, values, s=12, alpha=0.2, color="tab:blue")
    means = [values.mean() for values in groups]
    ax.scatter(positions, means, marker="D", color="tab:orange", label="Mean prediction")
    ax.scatter(
        positions,
        observed_scores,
        marker="x",
        s=70,
        color="black",
        label="Ideal prediction",
    )
    tick_labels = [f"{score}\n(n={len(values)})" for score, values in score_groups]
    ax.set_xticks(positions, tick_labels)
    ax.set(
        title="Predicted bonus points by observed score",
        xlabel="Observed bonus points",
        ylabel="Predicted expected bonus points",
        ylim=(-1, 31),
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(
        graph_path(output_dir, "bonus_response_score_predictions.png", "bonus"), dpi=160
    )
    plt.close(fig)
