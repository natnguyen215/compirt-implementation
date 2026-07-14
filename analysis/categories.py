"""Do the extra dimensions capture topic specialization?

    .venv/bin/python -m analysis.categories

Two views, in order of evidentiary weight:

1. **Tossup-side category slice** (the one that can answer the question):
   joins `tossup_id → category` through the local HuggingFace `tossups` table
   and reports per-category log-loss changes across the sweep, plus the direct
   specialization test — within each player, are the gains concentrated on the
   player's own strongest category? Player-category strength is measured from
   the 2024 training season, so it is exogenous to the 2025 outcomes being
   scored. (Established answer: no — gains land *off*-specialty, consistent
   with the dimensions fixing overconfidence where knowledge runs out.)

2. **Bonus-side category slice.** With the corrected Normal Stage-2 loadings
   the bonus series is comparable across dimensions; its category gains are
   nearly uniform (the roster near-max pools over individual specialization),
   which is itself informative next to the tossup side's 20x spread.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from compirt_eval.outputs import csv_path, evaluation_output_dirs

from analysis.data import (
    base_parser,
    load_bonus_parts,
    load_bonus_teams,
    load_buzzes,
    load_tossup_categories,
    require_dimensions,
)
from analysis.figures import plot_category_gains
from analysis.metrics import print_frame, score, score_bonuses

EPSILON = 1e-6


def per_row_log_loss(buzzes):
    probability = buzzes["predicted_correct"].clip(EPSILON, 1 - EPSILON)
    outcome = buzzes["y"].astype(float)
    return -(outcome * np.log(probability) + (1 - outcome) * np.log(1 - probability))


def by_tossup_category(sweep_dir, dimensions, categories):
    """Full tossup metrics per question category at each dimension."""
    rows = []
    for dimension in dimensions:
        buzzes = load_buzzes(sweep_dir, dimension)
        assigned = buzzes["tossup_id"].map(categories)
        for category in assigned.dropna().unique():
            rows.append(
                {
                    "dimension": dimension,
                    "category": category,
                    **score(buzzes[assigned == category]),
                }
            )
    return pd.DataFrame(rows)


def specialization_test(sweep_dir, low, reference, categories, min_strength_buzzes):
    """Within player, do gains concentrate on the player's strongest category?

    Strength per (player, category) is 2024 buzz accuracy — a different season
    from the one being scored, so no label leak. Gains are per-buzz log-loss
    improvements dim `low` → `reference` on 2025.
    """
    train = load_buzzes(sweep_dir, low, leg="train")
    strength = (
        train.assign(category=train["tossup_id"].map(categories))
        .dropna(subset=["category"])
        .groupby(["player_id", "category"])["y"]
        .agg(["mean", "size"])
    )
    strength = strength[strength["size"] >= min_strength_buzzes]

    baseline = load_buzzes(sweep_dir, low)
    multidim = load_buzzes(sweep_dir, reference)
    frame = baseline[["player_id", "tossup_id"]].copy()
    frame["category"] = frame["tossup_id"].map(categories)
    frame["gain"] = (per_row_log_loss(baseline) - per_row_log_loss(multidim)).to_numpy()
    frame = frame.dropna(subset=["category"])
    frame = frame.join(strength["mean"].rename("strength_2024"),
                       on=["player_id", "category"], how="inner")

    # Double-demeaned interaction: remove each player's average gain and each
    # category's average gain, leaving the pure within-player concentration.
    centered_gain = (
        frame["gain"]
        - frame.groupby("player_id")["gain"].transform("mean")
        - frame.groupby("category")["gain"].transform("mean")
        + frame["gain"].mean()
    )
    centered_strength = (
        frame["strength_2024"]
        - frame.groupby("player_id")["strength_2024"].transform("mean")
        - frame.groupby("category")["strength_2024"].transform("mean")
        + frame["strength_2024"].mean()
    )
    interaction_r, interaction_p = stats.pearsonr(centered_strength, centered_gain)

    # Coarser, more robust: each player's gain on their single best 2024
    # category vs their gain elsewhere.
    best = (
        strength.reset_index()
        .sort_values("mean")
        .groupby("player_id")
        .tail(1)
        .set_index("player_id")["category"]
    )
    frame["is_best"] = frame["player_id"].map(best) == frame["category"]
    paired = frame.groupby(["player_id", "is_best"])["gain"].mean().unstack().dropna()
    t, p = stats.ttest_rel(paired[True], paired[False])

    return {
        "pairs": len(frame),
        "interaction_r": interaction_r,
        "interaction_p": interaction_p,
        "players_paired": len(paired),
        "gain_on_best_category": paired[True].mean(),
        "gain_elsewhere": paired[False].mean(),
        "paired_t": t,
        "paired_p": p,
    }


def by_bonus_category(sweep_dir, dimensions):
    """Full bonus metrics per category, including PPB.

    The team table carries no `category`, but each `response_id` is one team's
    attempt at one bonus — all three parts share a category — so `response_id`
    carries the category across.
    """
    rows = []
    for dimension in dimensions:
        parts = load_bonus_parts(sweep_dir, dimension)
        teams = load_bonus_teams(sweep_dir, dimension)
        category_by_response = parts.drop_duplicates("response_id").set_index("response_id")[
            "category"
        ]
        team_categories = teams["response_id"].map(category_by_response)
        for category, part_group in parts.groupby("category"):
            rows.append(
                {
                    "dimension": dimension,
                    "category": category,
                    **score_bonuses(part_group, teams[team_categories == category]),
                }
            )
    return pd.DataFrame(rows)


def category_change_table(frame, low, reference, high):
    """Per-category log-loss reduction at the reference and final dimensions."""
    wide = frame.pivot_table(index="category", columns="dimension", values="log_loss")
    counts = frame[frame["dimension"] == low].set_index("category")["observations"]
    table = pd.DataFrame(
        {
            "n": counts,
            f"d_ll_1to{reference}": wide[low] - wide[reference],
            f"d_ll_1to{high}": wide[low] - wide[high],
        }
    )
    return table.sort_values(f"d_ll_1to{high}", ascending=False).reset_index()


def main():
    parser = base_parser(__doc__)
    parser.add_argument(
        "--reference-dimension",
        type=int,
        default=5,
        help="Multidimensional model the 1-D baseline is contrasted against.",
    )
    parser.add_argument(
        "--min-strength-buzzes",
        type=int,
        default=5,
        help="Minimum 2024 buzzes for a (player, category) strength estimate.",
    )
    arguments = parser.parse_args()
    evaluation_output_dirs(arguments.output_dir)
    dimensions = require_dimensions(arguments.sweep_dir)
    low, high = min(dimensions), max(dimensions)
    reference = arguments.reference_dimension

    categories = load_tossup_categories()
    tossup_frame = by_tossup_category(arguments.sweep_dir, dimensions, categories)
    changes = category_change_table(tossup_frame, low, reference, high)
    print_frame(f"tossup log-loss reduction by category (dim {low}→{reference} and →{high})",
                changes)

    test = specialization_test(
        arguments.sweep_dir, low, reference, categories, arguments.min_strength_buzzes
    )
    print(
        f"\nwithin-player specialization test (2024 strength, {test['pairs']:,} buzz rows):\n"
        f"  double-demeaned interaction r = {test['interaction_r']:+.4f} "
        f"(p = {test['interaction_p']:.2g})\n"
        f"  gain on own best category {test['gain_on_best_category']:+.4f} vs elsewhere "
        f"{test['gain_elsewhere']:+.4f} "
        f"(paired t = {test['paired_t']:+.2f}, p = {test['paired_p']:.2g}, "
        f"n = {test['players_paired']} players)"
    )

    bonus_frame = by_bonus_category(arguments.sweep_dir, dimensions)

    for name, frame in (
        ("metrics_by_tossup_category.csv", tossup_frame),
        ("metrics_by_bonus_category.csv", bonus_frame),
    ):
        frame.to_csv(csv_path(arguments.output_dir, name), index=False)
        print(f"wrote {csv_path(arguments.output_dir, name)}  ({len(frame)} rows)")

    gains = changes.set_index("category")[f"d_ll_1to{high}"]
    plot_category_gains(
        gains,
        changes.set_index("category")["n"],
        arguments.output_dir,
        "tossup_category_gains.png",
        f"Tossup log-loss reduction by category, dim {low}→{high}",
    )


if __name__ == "__main__":
    main()
