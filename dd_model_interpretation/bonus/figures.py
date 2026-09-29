"""Draw the four core bonus interpretation figures from saved analysis tables and fitted predictions.

Run from the repository root:
    .venv/bin/python -B -m dd_model_interpretation.bonus.figures
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde

from dd_model_interpretation.shared.common import BONUS_FIT

from dd_model_interpretation.shared.style import (
    AXIS_NAMES, BLUES, INK, LABELS, finish, grid,
)

HERE = Path(__file__).parent
DATA, FIGURES = HERE / "data", HERE / "figures"
SETS = {
    "2024-acf-fall::fall": "Fall 2024",
    "2024-acf-winter::2024-11-16": "Winter 2024",
    "2025-acf-regionals::2025-02-01": "Regionals 2025",
    "2025-acf-nationals::04192025": "Nationals 2025",
}


def bandwidth(values):
    """Scott's rule in data units, chosen once for each comparison scale."""
    return np.std(values, ddof=1) * len(values) ** (-1 / 5)


def density_grid(values, width):
    return np.linspace(np.min(values) - 4 * width, np.max(values) + 4 * width, 600)


def density(values, x, width):
    # scipy's factor multiplies the sample SD; use the same absolute bandwidth
    # for every group so different sample sizes do not change the smoothing.
    return gaussian_kde(values, bw_method=width / np.std(values, ddof=1))(x)


def difficulty_density(ax, parts, x, width):
    for label, color in LABELS.items():
        values = parts.loc[parts.label == label, "rd"].to_numpy()
        y = density(values, x, width)
        ax.fill_between(x, y, color=color, alpha=0.10, lw=0)
        ax.plot(x, y, color=color, lw=2,
                label=f"{label.capitalize()} (n = {len(values):,})")
    ax.set_xlabel("Difficulty D = r·d (higher = harder)")
    ax.set_ylabel("Density")
    ax.set_ylim(bottom=0)
    grid(ax, "y")
    ax.legend(fontsize=8)


def difficulty_distribution(parts, x, width):
    fig, ax = plt.subplots(figsize=(8.6, 3.8))
    difficulty_density(ax, parts, x, width)
    finish(fig, FIGURES / "difficulty_distribution.png",
           "How do fitted difficulties compare with the declared labels?",
           f"Gaussian density estimates; common bandwidth {width:.2f} difficulty units. "
           "Each part counts once within its label; each curve has total area 1. "
           "All 3,888 parts are included. Curves show smoothed estimates of the distributions.")


def difficulty_by_set(parts, x, width):
    if set(parts["set"]) != set(SETS):
        raise ValueError("Update SETS to label every question set in parts.csv")
    fig, axes = plt.subplots(2, 2, figsize=(9.4, 6.8), sharex=True, sharey=True)
    fig.subplots_adjust(hspace=0.42, wspace=0.2)
    for ax, (key, title) in zip(axes.flat, SETS.items()):
        rows = parts[parts["set"] == key]
        difficulty_density(ax, rows, x, width)
        ax.set_title(f"{title} ({len(rows) // 3:,} bonuses)")
        ax.legend(labels=[label.capitalize() for label in LABELS], ncol=3, loc="upper left",
                  fontsize=8, handles=ax.get_legend_handles_labels()[0])
    peak = max(line.get_ydata().max() for ax in axes.flat for line in ax.lines)
    axes[0, 0].set_ylim(0, peak * 1.25)
    finish(fig, FIGURES / "difficulty_by_set.png",
           "How do difficulty distributions change across question sets?",
           f"Identical axes and bandwidth ({width:.2f}) across panels and the overall figure. "
           "Each label's curve has total area 1; each part counts once. "
           "Panels refer to question sets, with mirror sites pooled.")


def team_skill(parts):
    obs = pd.read_csv(BONUS_FIT / "bonus_part_predictions.csv",
                      usecols=["bonus_part_id", "aggregate"])
    rsum = obs.bonus_part_id.map(parts.set_index("bonus_part_id").rsum)
    if rsum.isna().any() or (rsum <= 0).any():
        raise ValueError("Every saved attempt must match a part with positive sum(r)")
    # Saved aggregate = r·ts(R), hence s = w·ts(R) = aggregate / sum(r).
    return (obs["aggregate"] / rsum).to_numpy()


def location_vs_team_skill(parts):
    skill = team_skill(parts)
    width = bandwidth(parts["loc"].to_numpy())
    x = density_grid(np.concatenate([parts["loc"].to_numpy(), skill]), width)
    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    for label, color in LABELS.items():
        values = parts.loc[parts.label == label, "loc"].to_numpy()
        ax.plot(x, density(values, x, width), color=color, lw=2,
                label=f"{label.capitalize()} normalized difficulty")
    y = density(skill, x, width)
    ax.fill_between(x, y, color=INK, alpha=0.08)
    ax.plot(x, y, color=INK, lw=2, linestyle="--", label="Normalized team skill")
    ax.set_xlabel("Normalized difficulty and normalized team skill")
    ax.set_ylabel("Density")
    ax.set_ylim(bottom=0)
    ax.legend(fontsize=8, loc="center left", bbox_to_anchor=(1.01, 0.5))
    grid(ax, "y")
    finish(fig, FIGURES / "location_vs_team_skill.png",
           "Normalized difficulty compared with normalized team skill",
           "Both use the same normalized relevance weights for each part. "
           "Difficulty counts distinct parts; skill counts team–part attempts. "
           f"Smooth density curves with common bandwidth {width:.2f}; each curve has total area 1.")


def direction_clusters(parts):
    groups = parts.groupby("direction_k4")
    centers = groups[["w1", "w2", "w3"]].mean()
    # Saved cluster IDs are arbitrary; display them as numbered groups without
    # assigning subject names or imposing a threshold for "balanced" weights.
    centers = centers.sort_index()
    names = [f"Group {c + 1} ({groups.size()[c]:,} parts)" for c in centers.index]
    categories = parts.groupby("category", sort=True)
    category_means = categories[["w1", "w2", "w3"]].mean()
    category_names = [
        f"{name.replace('Geography/CE', 'Geography / Current Events')} ({categories.size()[name]:,} parts)"
        for name in category_means.index
    ]
    fig, axes = plt.subplots(2, 1, figsize=(7.2, 8.2),
                             gridspec_kw={"height_ratios": [len(centers), len(category_means)],
                                          "hspace": 0.48})
    for ax, table, labels, title in [
        (axes[0], centers, names, "Four k-means groups"),
        (axes[1], category_means, category_names, "All recorded subject categories"),
    ]:
        ax.imshow(table, cmap=BLUES, vmin=0, vmax=1, aspect="auto")
        ax.set_xticks(range(3), [AXIS_NAMES[k] for k in (1, 2, 3)])
        ax.xaxis.tick_top()
        ax.set_yticks(range(len(table)), labels)
        ax.set_title(title, pad=38)
        ax.tick_params(length=0)
        for spine in ax.spines.values():
            spine.set_visible(False)
        for y, values in enumerate(table.to_numpy()):
            for x, value in enumerate(values):
                ax.text(x, y, f"{value:.1%}", ha="center", va="center",
                        color="white" if value > .5 else INK)
    finish(fig, FIGURES / "direction_clusters.png",
           "How much weight does each group put on each skill axis?",
           "Cells show average relevance shares, not category proportions or correctness probabilities. "
           "Equal shares would be 33.3% on each axis. Top: groups learned from relevance. "
           "Bottom: recorded subject categories. Every row sums to 100% before rounding; both panels use the same scale.")


def main():
    parts = pd.read_csv(DATA / "parts.csv")
    # A single bandwidth in difficulty units makes all label/set curves comparable.
    width = bandwidth(parts.rd.to_numpy())
    x = density_grid(parts.rd.to_numpy(), width)
    difficulty_distribution(parts, x, width)
    difficulty_by_set(parts, x, width)
    location_vs_team_skill(parts)
    direction_clusters(parts)
    print("\n".join(sorted(str(p) for p in FIGURES.glob("*.png"))))


if __name__ == "__main__":
    main()
