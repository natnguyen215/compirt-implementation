"""Do harder questions gain more from extra skill dimensions?

    .venv/bin/python -m analysis.difficulty

Buckets tossups into difficulty quartiles under three *model-free* definitions
and reports each bucket's metric change across the sweep. Binning by the
model's own fitted `beta` would be circular, so every definition comes from
observed data alone:

- `p_value`: the classical item-difficulty p-value (share of buzzes converted).
  Low = hard. **It has a label leak**: it is the mean of the very `y` being
  scored, so binning on it conditions on the outcome and can manufacture
  apparent heterogeneity.
- `split_half_p_value`: the same statistic, estimated on a random half of each
  tossup's buzzes while only the *other* half is scored. Leak-free — this is
  the definition that adjudicates. Pass several `--seed`s to confirm the
  gradient is not a property of one fold draw.
- `mean_buzz_position`: how deep the field had to listen before buzzing.
  High = hard; never touches `y`. It measures pyramidality rather than
  knowledge difficulty, so it is expected to stay flat.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from compirt_eval.outputs import csv_path, evaluation_output_dirs

from analysis.data import base_parser, load_buzzes, require_dimensions
from analysis.figures import plot_difficulty
from analysis.metrics import endpoint_change, print_frame, score

DIFFICULTY_DEFINITIONS = ("p_value", "split_half_p_value", "mean_buzz_position")
# Higher is harder for buzz position; lower is harder for the p-values.
HARDER_IS_HIGHER = {"mean_buzz_position"}


def split_half_folds(buzzes, seed):
    """A fixed 0/1 fold per buzz event, shared by every dimension."""
    generator = np.random.default_rng(seed)
    return pd.Series(generator.integers(0, 2, size=len(buzzes)), index=buzzes.index)


def tossup_difficulty(sweep_dir, dimensions, min_buzzes, seed):
    """Rank tossups by the three difficulty definitions.

    Computed once from the first dimension — the observed columns are asserted
    identical across dimensions — so the buckets are the same at every sweep
    point.
    """
    buzzes = load_buzzes(sweep_dir, dimensions[0])
    folds = split_half_folds(buzzes, seed)

    grouped = buzzes.groupby("tossup_id")
    difficulty = pd.DataFrame(
        {
            "buzzes": grouped.size(),
            "p_value": grouped["y"].mean(),
            "mean_buzz_position": grouped["relative_position"].mean(),
        }
    )
    estimation = buzzes[folds == 0]
    difficulty["split_half_p_value"] = estimation.groupby("tossup_id")["y"].mean()
    difficulty["estimation_buzzes"] = estimation.groupby("tossup_id").size()

    difficulty = difficulty.reset_index()
    # A p-value over a handful of buzzes is mostly noise, and the split-half
    # variant needs enough buzzes to survive being halved.
    difficulty = difficulty[
        (difficulty["buzzes"] >= min_buzzes)
        & (difficulty["estimation_buzzes"] >= max(2, min_buzzes // 2))
    ]
    return difficulty, folds


def by_difficulty(sweep_dir, dimensions, difficulty, folds, definition, quantiles):
    """Metrics bucketed into difficulty quantiles under one definition."""
    ranked = difficulty.dropna(subset=[definition]).copy()
    # `duplicates="drop"` because a coarse p-value over few buzzes has heavy ties.
    ranked["bucket"] = pd.qcut(ranked[definition], q=quantiles, duplicates="drop")
    labels = list(ranked["bucket"].cat.categories)
    # The definitions run in opposite directions — a LOW p-value means hard, a
    # HIGH mean buzz position means hard. Rank always counts from 0 = hardest.
    ordered = labels[::-1] if definition in HARDER_IS_HIGHER else labels

    rows = []
    for dimension in dimensions:
        buzzes = load_buzzes(sweep_dir, dimension)
        # The split-half estimate is only leak-free if scored on the held-out fold.
        if definition == "split_half_p_value":
            buzzes = buzzes[folds == 1]
        buzzes = buzzes.merge(ranked[["tossup_id", "bucket"]], on="tossup_id", how="inner")
        for index, label in enumerate(ordered):
            rows.append(
                {
                    "dimension": dimension,
                    "difficulty_definition": definition,
                    "bucket": str(label),
                    "bucket_rank": index,
                    **score(buzzes[buzzes["bucket"] == label]),
                }
            )
    return pd.DataFrame(rows)


def gradient_table(difficulty_frame, quantiles):
    """Log-loss reduction per bucket, one row per definition (Q1 = hardest)."""
    rows = []
    for definition in DIFFICULTY_DEFINITIONS:
        if definition not in set(difficulty_frame["difficulty_definition"]):
            continue
        cells = {
            f"Q{rank + 1}": -endpoint_change(
                difficulty_frame, "log_loss",
                difficulty_definition=definition, bucket_rank=rank,
            )[2]
            for rank in range(quantiles)
        }
        rows.append({"definition": definition, **cells,
                     "leak": "yes (bins on y)" if definition == "p_value" else "no"})
    return pd.DataFrame(rows)


def main():
    parser = base_parser(__doc__)
    parser.add_argument("--difficulty-quantiles", type=int, default=4)
    parser.add_argument(
        "--min-tossup-buzzes",
        type=int,
        default=10,
        help="Drop tossups with fewer buzzes; their p-value is mostly noise.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        nargs="+",
        default=[42],
        help="Fold seeds for the split-half definition; pass several to check "
        "the gradient is stable across fold draws.",
    )
    arguments = parser.parse_args()
    evaluation_output_dirs(arguments.output_dir)
    dimensions = require_dimensions(arguments.sweep_dir)

    frames = []
    for seed in arguments.seed:
        difficulty, folds = tossup_difficulty(
            arguments.sweep_dir, dimensions, arguments.min_tossup_buzzes, seed
        )
        frame = pd.concat(
            [
                by_difficulty(arguments.sweep_dir, dimensions, difficulty, folds,
                              definition, arguments.difficulty_quantiles)
                for definition in DIFFICULTY_DEFINITIONS
            ],
            ignore_index=True,
        )
        frame["fold_seed"] = seed
        frames.append(frame)
        print_frame(
            f"log-loss reduction dim {min(dimensions)}→{max(dimensions)} by difficulty "
            f"quartile (Q1 = hardest), fold seed {seed}",
            gradient_table(frame, arguments.difficulty_quantiles),
        )

    combined = pd.concat(frames, ignore_index=True)
    combined.to_csv(csv_path(arguments.output_dir, "metrics_by_difficulty.csv"), index=False)
    print(f"\nwrote {csv_path(arguments.output_dir, 'metrics_by_difficulty.csv')}")
    plot_difficulty(frames[0], DIFFICULTY_DEFINITIONS, arguments.output_dir)


if __name__ == "__main__":
    main()
