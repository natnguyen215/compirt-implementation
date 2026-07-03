"""Compare fitted player skill across two independent pyramidal runs.

If the same players are refit on a different split/holdout run, their skill
magnitude and relative rank should be roughly stable; large swings suggest
either genuine skill drift or an under-identified fit. This is purely a
diagnostic between two saved 'players.csv' files -- it does not affect
training or the main evaluation metrics.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.figures import numeric_columns, short_id
from compirt_eval.outputs import csv_path, graph_path


def player_skill_stability_plot(primary_dir, comparison_dir, output_dir):
    """Compare player skill magnitude and rank across two fitted pyramidal runs."""
    left = pd.read_csv(primary_dir / "players.csv", dtype={"player_id": str})
    right = pd.read_csv(comparison_dir / "players.csv", dtype={"player_id": str})
    for frame in (left, right):
        if "theta_norm" not in frame:
            frame["theta_norm"] = np.linalg.norm(
                frame[numeric_columns(frame, "theta_")].to_numpy(dtype=float), axis=1
            )
    comparison = left[["player_id", "theta_norm"]].merge(
        right[["player_id", "theta_norm"]],
        on="player_id",
        suffixes=("_primary", "_comparison"),
    )
    if comparison.empty:
        return
    comparison["rank_primary"] = comparison["theta_norm_primary"].rank(ascending=False)
    comparison["rank_comparison"] = comparison["theta_norm_comparison"].rank(ascending=False)
    comparison["absolute_rank_change"] = (
        comparison["rank_comparison"] - comparison["rank_primary"]
    ).abs()
    comparison.to_csv(csv_path(output_dir, "player_skill_stability.csv"), index=False)

    fig, (skill_ax, rank_ax) = plt.subplots(1, 2, figsize=(12, 5.5))
    skill_ax.scatter(
        comparison["theta_norm_primary"],
        comparison["theta_norm_comparison"],
        alpha=0.5,
    )
    skill_limit = max(
        comparison["theta_norm_primary"].max(),
        comparison["theta_norm_comparison"].max(),
    )
    skill_ax.plot([0, skill_limit], [0, skill_limit], "--", color="0.5")
    skill_ax.set(
        title="Skill magnitude stability",
        xlabel=primary_dir.name,
        ylabel=comparison_dir.name,
    )
    rank_ax.scatter(comparison["rank_primary"], comparison["rank_comparison"], alpha=0.5)
    rank_limit = max(comparison["rank_primary"].max(), comparison["rank_comparison"].max())
    rank_ax.plot([1, rank_limit], [1, rank_limit], "--", color="0.5")
    rank_ax.invert_xaxis()
    rank_ax.invert_yaxis()
    rank_ax.set(
        title="Player rank stability",
        xlabel=primary_dir.name,
        ylabel=comparison_dir.name,
    )
    for _, row in comparison.nlargest(min(8, len(comparison)), "absolute_rank_change").iterrows():
        rank_ax.annotate(
            short_id(row["player_id"], 18),
            (row["rank_primary"], row["rank_comparison"]),
            fontsize=7,
        )
    for ax in (skill_ax, rank_ax):
        ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, "player_skill_stability.png"), dpi=160)
    plt.close(fig)
