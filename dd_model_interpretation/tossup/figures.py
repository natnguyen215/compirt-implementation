"""Draw the figure in README.md from data/subcategory_relevance.csv.

Run from the repository root after analyze.py:

    .venv/bin/python -B -m dd_model_interpretation.tossup.figures
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from dd_model_interpretation.shared.style import AXIS_NAMES, BLUES, MUTED, SECONDARY, finish, subcategory_name

HERE = Path(__file__).parent
DATA, FIGURES = HERE / "data", HERE / "figures"


def relevance_heatmaps(table):
    table = table.sort_values("hazard_r_1", ascending=False)
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 7.4), gridspec_kw={"wspace": 0.08})
    top = table[["hazard_r_1", "hazard_r_2", "hazard_r_3"]].to_numpy().max()
    for ax, columns, title in [(axes[0], ["hazard_r_1", "hazard_r_2", "hazard_r_3"], "Hazard (buzz timing)"),
                               (axes[1], ["r_1", "r_2", "r_3"], "Correctness")]:
        # One shared color scale, so the flatter correctness relevance reads as flatter.
        image = ax.imshow(table[columns].to_numpy(), cmap=BLUES, vmin=0, vmax=top, aspect="auto")
        ax.set_xticks(range(3), [AXIS_NAMES[k] for k in (1, 2, 3)])
        ax.xaxis.tick_top()
        ax.tick_params(length=0)
        ax.set_title(title, pad=34)
        for spine in ax.spines.values():
            spine.set_visible(False)
    axes[0].set_yticks(range(len(table)), [f"{subcategory_name(s)}  ({n})" for s, n in zip(table.index, table.n)])
    axes[1].set_yticks([])
    bar = fig.colorbar(image, ax=axes, orientation="horizontal", fraction=0.03, pad=0.02, aspect=50)
    bar.set_label("mean relevance (each tossup's three weights sum to 1)", color=SECONDARY)
    bar.outline.set_visible(False)
    bar.ax.tick_params(color=MUTED, labelcolor=SECONDARY, length=2)
    finish(fig, FIGURES / "hazard_vs_correctness.png",
           "Hazard relevance carries the subject structure; correctness relevance varies less",
           "Mean tossup relevance by subcategory (≥15 tossups; counts in parentheses), season DD fit, one shared "
           "color scale. Subcategory explains 40–69% of tossup-level hazard relevance and 6–8% of correctness relevance.")


def main():
    table = pd.read_csv(DATA / "subcategory_relevance.csv", index_col=0)
    relevance_heatmaps(table)
    print("\n".join(sorted(str(p) for p in FIGURES.glob("*.png"))))


if __name__ == "__main__":
    main()
