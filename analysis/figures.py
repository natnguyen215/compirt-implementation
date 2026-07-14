"""Plot styling and the figure builders used by the analysis modules."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from compirt_eval.outputs import graph_path

# Buzz thirds, difficulty buckets and player quartiles are all *ordered*
# levels, not distinct identities, so they take a single-hue ordinal ramp
# rather than categorical hues.
ORDINAL_3 = ["#86b6ef", "#2a78d6", "#104281"]
ORDINAL_4 = ["#86b6ef", "#5598e7", "#256abf", "#104281"]
ACCENT = "#2a78d6"
INK = "#0b0b0b"
MUTED = "#52514e"
GRID = "#d8d7d2"


def style(ax, title, xlabel, ylabel):
    """Recessive grid and axes, so the marks carry the chart."""
    ax.set_title(title, fontsize=10.5, color=INK, loc="left", pad=10)
    ax.set_xlabel(xlabel, fontsize=9, color=MUTED)
    ax.set_ylabel(ylabel, fontsize=9, color=MUTED)
    ax.grid(True, color=GRID, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=9)


def save(figure, path, title):
    figure.suptitle(title, fontsize=12, color=INK, x=0.01, ha="left")
    figure.tight_layout()
    figure.savefig(path, dpi=160, facecolor="white")
    plt.close(figure)
    print(f"wrote {path}")


def plot_overall(tossups, bonuses, output_dir):
    """The paper's four metrics, one panel each — they share no scale."""
    figure, axes = plt.subplots(1, 4, figsize=(17, 3.9))
    panels = (
        (tossups, "auc", "Tossup AUC (higher better)"),
        (tossups, "log_loss", "Tossup log loss (lower better)"),
        (tossups, "buzz_position_mae", "Buzz-position MAE (lower better)"),
        (bonuses, "ppb_mae", "Bonus PPB MAE (lower better)"),
    )
    for ax, (frame, metric, label) in zip(axes, panels):
        if metric not in frame.columns:
            continue
        ax.plot(frame["dimension"], frame[metric], color=ACCENT, linewidth=2, marker="o",
                markersize=7)
        style(ax, label, "Skill dimension", "")
        ax.set_xticks(frame["dimension"])
    save(
        figure,
        graph_path(output_dir, "overall_by_dimension.png"),
        "The paper's four metrics across the skill-dimension sweep",
    )


def plot_position(position, labels, output_dir):
    """The tension itself: log loss and AUC rank the thirds in opposite orders."""
    figure, axes = plt.subplots(1, 3, figsize=(14, 4.2))
    panels = (
        ("log_loss", "Log loss (lower better)"),
        ("auc", "AUC (higher better)"),
        ("buzz_position_mae", "Buzz-position MAE (lower better)"),
    )
    for ax, (metric, label) in zip(axes, panels):
        for color, group in zip(ORDINAL_3, labels):
            series = position[position["position_group"] == group].sort_values("dimension")
            ax.plot(series["dimension"], series[metric], color=color, linewidth=2, marker="o",
                    markersize=7, label=group)
        style(ax, label, "Skill dimension", "")
        ax.set_xticks(sorted(position["dimension"].unique()))
    axes[0].legend(frameon=False, fontsize=9, labelcolor=MUTED)
    save(
        figure,
        graph_path(output_dir, "buzz_position.png"),
        "Early buzzes gain most in log loss but least in AUC — the metrics disagree",
    )


def plot_calibration_discrimination(position, labels, output_dir):
    """Settle the early-vs-late argument that AUC and log loss cannot."""
    figure, axes = plt.subplots(1, 3, figsize=(14, 4.2))
    panels = (
        ("reliability", "Reliability — miscalibration (lower better)"),
        ("resolution", "Resolution — discrimination (higher better)"),
        ("brier", "Brier score (lower better)"),
    )
    for ax, (metric, label) in zip(axes, panels):
        for color, group in zip(ORDINAL_3, labels):
            series = position[position["position_group"] == group].sort_values("dimension")
            ax.plot(series["dimension"], series[metric], color=color, linewidth=2, marker="o",
                    markersize=7, label=group)
        style(ax, label, "Skill dimension", "")
        ax.set_xticks(sorted(position["dimension"].unique()))
    axes[0].legend(frameon=False, fontsize=9, labelcolor=MUTED)
    save(
        figure,
        graph_path(output_dir, "calibration_vs_discrimination.png"),
        "Brier decomposition: early buzzes buy calibration, late buzzes buy discrimination",
    )


def plot_difficulty(difficulty, definitions, output_dir):
    """One column per difficulty definition; the split-half column is the
    leak-free one and adjudicates."""
    present = [d for d in definitions if d in set(difficulty["difficulty_definition"])]
    figure, axes = plt.subplots(2, len(present), figsize=(4.9 * len(present), 7.6),
                                squeeze=False)
    for column, definition in enumerate(present):
        subset = difficulty[difficulty["difficulty_definition"] == definition]
        low, high = subset["dimension"].min(), subset["dimension"].max()
        loss = subset.pivot_table(index="bucket_rank", columns="dimension", values="log_loss")
        auc = subset.pivot_table(index="bucket_rank", columns="dimension", values="auc")
        panels = (
            ((loss[low] - loss[high]).to_numpy(), f"Log-loss reduction, dim {low}→{high}"),
            ((auc[high] - auc[low]).to_numpy(), f"AUC gain, dim {low}→{high}"),
        )
        for row, (values, label) in enumerate(panels):
            ax = axes[row][column]
            names = [f"Q{index + 1}" for index in range(len(values))]
            ax.bar(names, values, color=ORDINAL_4[: len(values)], width=0.62)
            style(ax, f"{label}\nby {definition}", "Difficulty quartile (Q1 = hardest)",
                  "Improvement")
            for index, value in enumerate(values):
                ax.text(index, value, f"{value:+.3f}", ha="center", va="bottom", fontsize=8,
                        color=MUTED)
            ax.margins(y=0.18)
    save(
        figure,
        graph_path(output_dir, "difficulty_gains.png"),
        "Harder questions gain more — and the gradient survives the leak-free definition",
    )


def plot_category_gains(gains, counts, output_dir, filename, title):
    """Horizontal bars of per-category improvement (long names)."""
    ordered = gains.sort_values()
    span = ordered.max() - ordered.min() or 1.0
    colors = [
        ORDINAL_4[min(int((value - ordered.min()) / span * len(ORDINAL_4)), len(ORDINAL_4) - 1)]
        for value in ordered
    ]
    figure, ax = plt.subplots(figsize=(9, 6))
    ax.barh(ordered.index, ordered.to_numpy(), color=colors, height=0.7)
    ax.axvline(0.0, color=MUTED, linewidth=1)
    for index, (name, value) in enumerate(ordered.items()):
        ax.text(value, index, f"  {value:+.4f} (n={counts.get(name, 0):,})", va="center",
                fontsize=7.5, color=MUTED)
    style(ax, "", "Log-loss reduction (higher = dimensionality helped)", "")
    ax.margins(x=0.30)
    save(figure, graph_path(output_dir, filename), title)


def plot_player_gains(quartiles, output_dir):
    """Who the extra dimensions actually help, by quartile of each covariate."""
    covariates = quartiles["covariate"].unique()
    figure, axes = plt.subplots(1, len(covariates), figsize=(5.2 * len(covariates), 4.2),
                                squeeze=False)
    for ax, covariate in zip(axes[0], covariates):
        subset = quartiles[quartiles["covariate"] == covariate]
        # Negative delta = the multidimensional model predicts the player
        # better; flip the sign so a taller bar reads as "helped more".
        values = -subset["mean_log_loss_delta"].to_numpy()
        ax.bar(subset["quartile"], values, color=ORDINAL_4[: len(values)], width=0.62)
        style(ax, f"By {covariate}", "", "Log-loss reduction, dim 1→reference")
        for index, value in enumerate(values):
            ax.text(index, value, f"{value:.3f}", ha="center", va="bottom", fontsize=8,
                    color=MUTED)
        ax.margins(y=0.18)
    save(
        figure,
        graph_path(output_dir, "player_gains.png"),
        "Who gains from extra dimensions, by player-covariate quartile",
    )
