"""Plot style shared by the bonus, tossup, and comparison figures.

Light-mode tokens and the ordinal difficulty ramp come from the dataviz
reference palette; the ramp was validated with `validate_palette.js --ordinal`.
"""

import textwrap

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

SURFACE, INK, SECONDARY, MUTED = "#fcfcfb", "#0b0b0b", "#52514e", "#898781"
GRID, BASELINE = "#e1e0d9", "#c3c2b7"
ACCENT = "#2a78d6"
LABELS = {"easy": "#86b6ef", "medium": "#2a78d6", "hard": "#104281"}
BLUES = LinearSegmentedColormap.from_list("blues", [
    "#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"])
AXIS_NAMES = {k: f"Axis {k}" for k in (1, 2, 3)}

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "font.family": "sans-serif", "font.size": 9, "text.color": INK,
    "axes.edgecolor": BASELINE, "axes.labelcolor": SECONDARY, "axes.linewidth": 0.8,
    "axes.titlesize": 10, "axes.titleweight": "bold", "axes.titlelocation": "left",
    "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": MUTED, "ytick.color": MUTED, "xtick.labelcolor": SECONDARY, "ytick.labelcolor": SECONDARY,
    "grid.color": GRID, "grid.linewidth": 0.8, "legend.frameon": False,
})


def subcategory_name(name):
    return name[:-1] + " (general)" if name.endswith("/") else name.replace("Geography/CE", "Geo/CE")


def grid(ax, axis="x"):
    ax.grid(axis=axis)
    ax.set_axisbelow(True)


def finish(fig, path, title, subtitle):
    """Place the title and subtitle above everything the axes draw, then save to path."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    boxes = [ax.get_tightbbox(renderer).transformed(fig.transFigure.inverted()) for ax in fig.axes]
    left, top = min(b.x0 for b in boxes), max(b.y1 for b in boxes)
    line = 1 / (72 * fig.get_figheight())  # one point in figure coordinates
    subtitle = textwrap.fill(subtitle, width=int(fig.get_figwidth() * 15))
    fig.text(left, top + 8 * line, subtitle, ha="left", va="bottom", color=SECONDARY, fontsize=9, linespacing=1.4)
    lines = subtitle.count("\n") + 1
    fig.text(left, top + (14 + 13 * lines) * line, title, ha="left", va="bottom", color=INK,
             fontsize=12, fontweight="bold")
    path.parent.mkdir(exist_ok=True)
    fig.savefig(path, dpi=200, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
