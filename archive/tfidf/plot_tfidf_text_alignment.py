"""Align a fitted TF-IDF run's difficulty curves to the actual question text.

'plot_tfidf_difficulty_curves.py' shows d(t) and d'(t) against relative
position; this script shows which words the drop sits on. Each figure stacks
three panels over one tossup:

1. the base difficulty d(t), the effective d'(t), and the TF-IDF reduction,
   with the observed buzz histogram, sentence boundaries, and the token span
   over which d'(t) does the bulk of its falling;
2. the per-token TF-IDF weight that drives the reduction, with the heaviest
   clue words labelled;
3. the question text itself, colored by token weight, with the drop span's
   words boxed.

Token alignment note: the model reads 'tfidf_prefix[j, t]' at the *raw* token
position t, but that matrix is built over tokens surviving
'tfidf_features.normalize_token' (numerals and bare punctuation are dropped,
~6% of tokens in 2024), so the modeled reveal runs ahead of the text. Both
curves are plotted.
"""

from __future__ import annotations

import argparse
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import Normalize

from compirt_data import DEFAULT_DATA_DIR, filter_tournament, load_hf_tables
from compirt_eval.common.figures import short_id
from compirt_eval.scenario_a_tossups.difficulty import selected_tossups
from tfidf.plot_tfidf_difficulty_curves import (
    _relevance_mass,
    _saved_difficulty,
    load_run_context,
)
from tfidf.tfidf_features import _document_idf, _tokens_from_value, normalize_token


WRAP_WIDTH = 128
TEXT_COLORMAP = "YlOrRd"


def raw_token_weights(tossups, tossup_ids):
    """Return per-raw-token normalized TF-IDF weights, keyed by tossup id.

    Weights reproduce the fitted feature exactly ('tf * idf', normalized to sum
    to 1.0 per question) but are laid back out over the *raw* token sequence,
    with dropped tokens carrying weight 0.0, so they can be read against the
    displayed text.
    """
    ordered_tokens = [
        _tokens_from_value(tossups.loc[tossup_id, "tokens"]) for tossup_id in tossup_ids
    ]
    idf = _document_idf(ordered_tokens)

    weights = {}
    for tossup_id, filtered in zip(tossup_ids, ordered_tokens):
        raw_tokens = [str(token) for token in tossups.loc[tossup_id, "tokens"]]
        counts = pd.Series(filtered).value_counts().to_dict()
        length = max(1, len(filtered))
        scores = np.array(
            [
                (counts[token] / length) * idf[token]
                if (token := normalize_token(raw_token)) is not None
                else 0.0
                for raw_token in raw_tokens
            ]
        )
        total = scores.sum()
        weights[tossup_id] = scores / total if total > 0 else scores
    return weights


def slugify(tossup_id):
    """Return a filesystem-safe stem for a tossup id."""
    return str(tossup_id).replace("::", "_").replace("/", "-").replace(" ", "-")


def giveaway_token(raw_tokens):
    """Return the index of the 'for ten points' marker, or None."""
    lowered = [token.lower() for token in raw_tokens]
    for index in range(len(lowered) - 1):
        if lowered[index] in {"ten", "10"} and lowered[index + 1].startswith("point"):
            return index
    return None


def drop_span(curve, positions, low=0.1, high=0.9):
    """Return '(start, midpoint, end)' positions bracketing the curve's fall.

    Levels are fractions of the curve's total range, walked from its maximum
    down to its minimum, so the span is where the difficulty actually collapses
    rather than wherever the fitted sigmoid midpoint 'mu' happens to sit.
    """
    top, bottom = float(curve.max()), float(curve.min())
    if top - bottom < 1e-6:
        return None
    levels = [bottom + fraction * (top - bottom) for fraction in (high, 0.5, low)]
    crossings = []
    for level in levels:
        below = np.nonzero(curve <= level)[0]
        crossings.append(float(positions[below[0]]) if below.size else float(positions[-1]))
    return tuple(crossings)


def tossup_panels(ax_curve, ax_stem, context):
    """Draw the curve and token-weight panels; record the drop spans on context."""
    raw_tokens = context["raw_tokens"]
    T = len(raw_tokens)
    token_axis = np.arange(1, T + 1)

    # --- panel 1: difficulty over the token axis -------------------------
    relative = token_axis / T
    base = _saved_difficulty(context["row"], relative)
    mass = _relevance_mass(context["row"])
    effective = base - context["lambda"] * mass * context["text_prefix"]
    model_effective = base - context["lambda"] * mass * context["model_prefix"]

    buzz_axis = ax_curve.twinx()
    buzz_axis.hist(
        context["buzz_positions"] * T,
        bins=np.linspace(1, T, 25),
        color="tab:orange",
        alpha=0.20,
        label=f"Observed buzzes (n={len(context['buzz_positions'])})",
    )
    buzz_axis.set_ylabel("Buzz count", color="tab:orange")
    buzz_axis.tick_params(axis="y", colors="tab:orange")

    ax_curve.plot(token_axis, base, color="tab:blue", lw=1.4, alpha=0.7, label="Base d(t)")
    ax_curve.plot(
        token_axis,
        effective,
        color="black",
        lw=2.2,
        label="Effective d'(t), text-aligned",
    )
    ax_curve.plot(
        token_axis,
        model_effective,
        color="tab:purple",
        lw=1.1,
        ls=":",
        label="d'(t) as the model indexed it",
    )
    ax_curve.plot(
        token_axis,
        -context["lambda"] * mass * context["text_prefix"],
        color="tab:green",
        lw=1.2,
        ls="--",
        label="TF-IDF reduction",
    )

    base_span = drop_span(base, token_axis)
    effective_span = drop_span(effective, token_axis)
    context["base_span"] = None if base_span is None else (int(base_span[0]), int(base_span[2]))
    context["effective_span"] = (
        None if effective_span is None else (int(effective_span[0]), int(effective_span[2]))
    )
    for span, color, label in (
        (base_span, "tab:blue", "base d(t)"),
        (effective_span, "tab:red", "effective d'(t)"),
    ):
        if span is None:
            continue
        start, middle, end = span
        ax_curve.axvspan(start, end, color=color, alpha=0.07)
        ax_curve.axvline(middle, color=color, lw=1.0, alpha=0.55)
        ax_curve.annotate(
            f"{label} 90→10%: tokens {int(start)}–{int(end)}",
            xy=(middle, 1.0),
            xycoords=("data", "axes fraction"),
            xytext=(4, -9 if color == "tab:red" else -21),
            textcoords="offset points",
            va="top",
            fontsize=7,
            color=color,
        )

    for boundary in context["sentence_boundaries"]:
        if 1 <= boundary <= T:
            ax_curve.axvline(boundary, color="0.75", lw=0.7, ls="-")
    if context["giveaway"] is not None:
        ax_curve.axvline(
            context["giveaway"] + 1, color="tab:brown", lw=1.2, ls="-.", label="'for 10 points'"
        )

    ax_curve.set(xlim=(1, T), ylabel="Difficulty (logits)")
    ax_curve.grid(alpha=0.2)
    curve_handles, curve_labels = ax_curve.get_legend_handles_labels()
    buzz_handles, buzz_labels = buzz_axis.get_legend_handles_labels()
    ax_curve.legend(
        curve_handles + buzz_handles, curve_labels + buzz_labels, fontsize=6.5, loc="lower left"
    )
    ax_curve.set_title(
        f"{short_id(context['tossup_id'])} — {context['answer']}", fontsize=9, loc="left"
    )

    # --- panel 2: per-token TF-IDF weight --------------------------------
    weights = context["weights"]
    ax_stem.vlines(token_axis, 0, weights, color="tab:green", lw=1.0, alpha=0.8)
    heaviest = np.argsort(weights)[::-1][:8]
    for index in heaviest:
        ax_stem.annotate(
            raw_tokens[index].strip(",.;:"),
            xy=(index + 1, weights[index]),
            xytext=(0, 2),
            textcoords="offset points",
            fontsize=6,
            rotation=45,
            ha="left",
        )
    if effective_span is not None:
        ax_stem.axvspan(effective_span[0], effective_span[2], color="tab:red", alpha=0.07)
    if base_span is not None:
        ax_stem.axvspan(base_span[0], base_span[2], color="tab:blue", alpha=0.07)
    ax_stem.set(
        xlim=(1, T),
        ylim=(0, float(weights.max()) * 1.55 if weights.max() > 0 else 1),
        xlabel="Token position",
        ylabel="Token\nTF-IDF",
    )
    ax_stem.grid(alpha=0.15)


def wrap_placements(raw_tokens):
    """Return '(index, token, column, line)' for a monospace character grid."""
    column, line = 0, 0
    placements = []
    for index, token in enumerate(raw_tokens):
        if column and column + len(token) > WRAP_WIDTH:
            column, line = 0, line + 1
        placements.append((index, token, column, line))
        column += len(token) + 1
    return placements, line


def draw_text_panel(fig, ax, context):
    """Lay the question out in monospace, background-shaded by token weight.

    The character grid is exact only if one character is one data unit wide, so
    the font size is derived from the axes' measured width rather than fixed.
    """
    raw_tokens = context["raw_tokens"]
    weights = context["weights"]
    ax.set_axis_off()
    scale = float(weights.max()) or 1.0
    normalizer = Normalize(vmin=0.0, vmax=scale)
    colormap = plt.get_cmap(TEXT_COLORMAP)

    placements, last_line = wrap_placements(raw_tokens)
    ax.set(xlim=(-0.5, WRAP_WIDTH), ylim=(last_line + 1.4, -1))

    fig.canvas.draw()
    axes_points = ax.get_window_extent().width / fig.dpi * 72.0
    # DejaVu Sans Mono advances 0.602 em per character.
    fontsize = min(11.0, axes_points / (0.602 * WRAP_WIDTH))

    for index, token, column, line in placements:
        weight = weights[index]
        ax.text(
            column,
            line,
            token,
            fontfamily="monospace",
            fontsize=fontsize,
            va="center",
            ha="left",
            color="0.15" if weight > 0 else "0.6",
            bbox=dict(
                facecolor=colormap(normalizer(weight)),
                alpha=0.85,
                pad=0.9,
                linewidth=0,
                edgecolor="none",
            )
            if weight > 0.02 * scale
            else None,
        )

    for key, color, offset in (
        ("base_span", "tab:blue", 0.34),
        ("effective_span", "tab:red", 0.48),
    ):
        span = context.get(key)
        if span is None:
            continue
        for line in range(last_line + 1):
            inside = [
                (column, column + len(token))
                for index, token, column, row in placements
                if row == line and span[0] <= index + 1 <= span[1]
            ]
            if inside:
                ax.plot(
                    [min(start for start, _ in inside), max(end for _, end in inside)],
                    [line + offset] * 2,
                    color=color,
                    lw=2.0,
                    solid_capstyle="butt",
                )

    ax.text(
        0,
        last_line + 1.1,
        "background = token TF-IDF weight   |   blue underline = base d(t) 90→10% drop   |   "
        "red underline = effective d'(t) 90→10% drop",
        fontsize=7,
        color="0.4",
    )


def build_context(tossup_id, parameters, predictions, tossups, data, summary, weights):
    """Collect everything one tossup figure needs."""
    index = data["tossup_index"][tossup_id]
    raw_tokens = [str(token) for token in tossups.loc[tossup_id, "tokens"]]
    T = len(raw_tokens)
    token_weights = weights[tossup_id]

    text_prefix = np.cumsum(token_weights)
    model_prefix_full = data["tfidf_prefix"][index].detach().cpu().numpy()
    model_prefix = model_prefix_full[: min(T, model_prefix_full.size)]
    if model_prefix.size < T:
        model_prefix = np.pad(model_prefix, (0, T - model_prefix.size), mode="edge")

    rows = predictions[predictions["tossup_id"] == tossup_id]
    return {
        "tossup_id": tossup_id,
        "row": parameters.loc[tossup_id],
        "raw_tokens": raw_tokens,
        "weights": token_weights,
        "text_prefix": text_prefix,
        "model_prefix": model_prefix,
        "lambda": float(summary["tfidf_clue_effect"]),
        "buzz_positions": rows.loc[rows["z"] == "BUZZ", "relative_position"].to_numpy(),
        "sentence_boundaries": np.asarray(
            tossups.loc[tossup_id, "sentence_boundaries"], dtype=int
        ),
        "giveaway": giveaway_token(raw_tokens),
        "answer": textwrap.shorten(
            str(tossups.loc[tossup_id, "answer"]).replace("<b>", "").replace("</b>", "")
            .replace("<u>", "").replace("</u>", ""),
            width=70,
            placeholder="…",
        ),
    }


def corpus_overview(contexts, output_path):
    """Plot where the modeled drop lands relative to text landmarks."""
    records = []
    for context in contexts:
        T = len(context["raw_tokens"])
        relative = np.arange(1, T + 1) / T
        base = _saved_difficulty(context["row"], relative)
        effective = base - context["lambda"] * _relevance_mass(context["row"]) * context[
            "text_prefix"
        ]
        span = drop_span(effective, relative)
        base_span_positions = drop_span(base, relative)
        if span is None:
            continue
        records.append(
            {
                "drop_midpoint": span[1],
                "base_midpoint": base_span_positions[1] if base_span_positions else np.nan,
                "giveaway": (
                    (context["giveaway"] + 1) / T
                    if context["giveaway"] is not None
                    else np.nan
                ),
                "mean_buzz": float(np.mean(context["buzz_positions"]))
                if len(context["buzz_positions"])
                else np.nan,
                "last_sentence": float(context["sentence_boundaries"][-1]) / T
                if len(context["sentence_boundaries"])
                else np.nan,
            }
        )
    if not records:
        raise ValueError("No tossup has a non-constant effective difficulty curve")
    frame = pd.DataFrame(records)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.2))
    bins = np.linspace(0, 1, 26)
    axes[0].hist(
        frame["drop_midpoint"],
        bins=bins,
        color="black",
        alpha=0.6,
        label="d'(t) drop midpoint",
    )
    axes[0].hist(
        frame["base_midpoint"].dropna(),
        bins=bins,
        histtype="step",
        lw=1.4,
        color="tab:blue",
        label="base d(t) drop midpoint",
    )
    axes[0].hist(
        frame["giveaway"].dropna(),
        bins=bins,
        color="tab:brown",
        alpha=0.45,
        label="'for 10 points'",
    )
    axes[0].hist(
        frame["mean_buzz"].dropna(),
        bins=bins,
        color="tab:orange",
        alpha=0.40,
        label="mean observed buzz",
    )
    axes[0].set(
        xlabel="Relative position",
        ylabel="Tossups",
        title="Where the drop sits in the question",
    )
    axes[0].legend(fontsize=7)
    axes[0].grid(alpha=0.2)

    axes[1].scatter(frame["drop_midpoint"], frame["mean_buzz"], s=8, alpha=0.35, color="tab:blue")
    axes[1].plot([0, 1], [0, 1], color="0.6", lw=1.0, ls="--")
    correlation = frame[["drop_midpoint", "mean_buzz"]].corr().iloc[0, 1]
    axes[1].set(
        xlabel="d'(t) drop midpoint",
        ylabel="Mean observed buzz position",
        title=f"Drop vs. actual buzzing (r = {correlation:.2f})",
        xlim=(0, 1),
        ylim=(0, 1),
    )
    axes[1].grid(alpha=0.2)

    fig.suptitle("TF-IDF effective difficulty against question landmarks", fontsize=11)
    fig.tight_layout()
    fig.savefig(output_path, dpi=160)
    plt.close(fig)
    return frame


def load_hf_tossups(data_dir, summary):
    """Return the tossup table for the run's split, indexed by tossup id."""
    tables = filter_tournament(
        load_hf_tables(data_dir, summary.get("split", "all")),
        summary.get("tournament") or None,
    )
    return tables["tossups"].set_index("tossup_id")


def plot_text_alignment(results_dir, output_dir, data_dir, count, tossup_ids):
    """Write per-tossup text-aligned figures plus the corpus overview."""
    summary, data = load_run_context(results_dir, data_dir)
    data["tossup_index"] = {
        tossup_id: index for index, tossup_id in enumerate(data["tossup_ids"])
    }
    parameters = pd.read_csv(results_dir / "tossups.csv").set_index("tossup_id")
    predictions = pd.read_csv(results_dir / "tossup_predictions.csv")

    tables = load_hf_tossups(data_dir, summary)
    weights = raw_token_weights(tables, list(data["tossup_ids"]))

    selected = tossup_ids or [
        tossup_id
        for tossup_id in selected_tossups(predictions, count=count)
        if tossup_id in parameters.index and tossup_id in data["tossup_index"]
    ]
    missing = [
        tossup_id
        for tossup_id in selected
        if tossup_id not in parameters.index
        or tossup_id not in data["tossup_index"]
    ]
    if missing:
        raise ValueError(f"Unknown tossup ids: {', '.join(missing)}")
    if not selected:
        raise ValueError("No tossups available for TF-IDF text-alignment plotting")

    output_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for tossup_id in selected:
        context = build_context(
            tossup_id, parameters, predictions, tables, data, summary, weights
        )
        text_lines = 1 + wrap_placements(context["raw_tokens"])[1]
        fig, axes = plt.subplots(
            3,
            1,
            figsize=(14, 6.2 + 0.28 * text_lines),
            gridspec_kw={"height_ratios": [3.1, 1.0, 0.32 * text_lines + 0.4]},
        )
        tossup_panels(axes[0], axes[1], context)
        fig.tight_layout()
        draw_text_panel(fig, axes[2], context)
        path = output_dir / f"text_alignment_{slugify(tossup_id)}.png"
        fig.savefig(path, dpi=160)
        plt.close(fig)
        written.append(path)

    all_contexts = [
        build_context(tossup_id, parameters, predictions, tables, data, summary, weights)
        for tossup_id in data["tossup_ids"]
        if tossup_id in parameters.index
    ]
    overview_path = output_dir / "drop_vs_text_landmarks.png"
    corpus_overview(all_contexts, overview_path)
    written.append(overview_path)
    return written


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--count", type=int, default=6)
    parser.add_argument("--tossup-id", action="append", default=[])
    args = parser.parse_args()
    if args.count < 1:
        raise ValueError("--count must be at least 1")
    if args.output_dir is None:
        args.output_dir = args.results_dir.parent / "evaluation" / "graphs" / "text_alignment"
    return args


if __name__ == "__main__":
    args = parse_args()
    for path in plot_text_alignment(
        args.results_dir, args.output_dir, args.data_dir, args.count, args.tossup_id
    ):
        print(path)
