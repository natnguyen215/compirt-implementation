"""Headline metrics by skill dimension, with the reconciliation guardrail.

    .venv/bin/python -m analysis.overall

Prints the whole-population tossup and bonus metric series across the sweep,
verifies the recomputed totals against the sweep's own committed metric CSVs
(so every other module's slices provably decompose the same numbers the
committed reports headline), and writes the by-dimension CSVs and the
four-metric overview figure.

Both stages' series are comparable across dimensions now that the baseline's
bonus loadings are Normal like its tossup stage. If the bonus series ever turns
erratic again (non-monotone, tau jumping between adjacent dims), suspect a
reintroduced basis-dependence at the Stage-1/Stage-2 interface before believing
it — see analysis/README.md ground rule 2.
"""

from __future__ import annotations

import pandas as pd

from compirt_eval.outputs import csv_path, evaluation_output_dirs, metrics_path

from analysis.data import (
    BONUS_BRANCH,
    base_parser,
    holdout_dir,
    load_bonus_parts,
    load_bonus_teams,
    load_buzzes,
    require_dimensions,
)
from analysis.figures import plot_overall
from analysis.metrics import print_frame, score, score_bonuses

RECONCILE_TOLERANCE = 1e-6


def by_dimension(sweep_dir, dimensions):
    """Whole-population held-out tossup metrics at each skill dimension."""
    return pd.DataFrame(
        [
            {"dimension": dimension, **score(load_buzzes(sweep_dir, dimension))}
            for dimension in dimensions
        ]
    )


def bonuses_by_dimension(sweep_dir, dimensions):
    """Whole-population held-out bonus metrics at each skill dimension."""
    return pd.DataFrame(
        [
            {
                "dimension": dimension,
                **score_bonuses(
                    load_bonus_parts(sweep_dir, dimension),
                    load_bonus_teams(sweep_dir, dimension),
                ),
            }
            for dimension in dimensions
        ]
    )


def reconcile(sweep_dir, dimensions, tossups, bonuses):
    """Check recomputed totals against the metrics the sweep's evaluator wrote."""
    rows = []
    checks = (
        (
            "tossup",
            tossups,
            "tossup_metrics.csv",
            ("auc", "log_loss", "ece", "accuracy", "buzz_position_mae",
             "buzz_position_median_absolute_error"),
        ),
        (
            "bonus",
            bonuses,
            "bonus_metrics.csv",
            ("auc", "log_loss", "ece", "accuracy", "part_accuracy", "exact_acc",
             "per_bonus_points_mae", "ppb_mae"),
        ),
    )
    for scenario, recomputed, filename, names in checks:
        for dimension in dimensions:
            evaluation = (
                holdout_dir(sweep_dir, dimension) / BONUS_BRANCH / "compositional-evaluation"
            )
            path = metrics_path(evaluation, filename)
            if not path.exists():
                continue
            committed = pd.read_csv(path).iloc[0]
            ours = recomputed[recomputed["dimension"] == dimension].iloc[0]
            for metric in names:
                if metric not in committed or metric not in ours:
                    continue
                rows.append(
                    {
                        "scenario": scenario,
                        "dimension": dimension,
                        "metric": metric,
                        "committed": committed[metric],
                        "recomputed": ours[metric],
                        "abs_diff": abs(committed[metric] - ours[metric]),
                    }
                )
    return pd.DataFrame(rows)


def main():
    parser = base_parser(__doc__)
    parser.add_argument(
        "--skip-reconcile",
        action="store_true",
        help="Skip verifying recomputed totals against the committed metric CSVs.",
    )
    arguments = parser.parse_args()
    evaluation_output_dirs(arguments.output_dir)

    dimensions = require_dimensions(arguments.sweep_dir)
    print(f"dimensions: {dimensions}")

    tossups = by_dimension(arguments.sweep_dir, dimensions)
    bonuses = bonuses_by_dimension(arguments.sweep_dir, dimensions)

    if not arguments.skip_reconcile:
        check = reconcile(arguments.sweep_dir, dimensions, tossups, bonuses)
        print(f"\nreconciliation vs committed metric CSVs ({len(check)} checks):")
        for scenario, group in check.groupby("scenario"):
            print(f"  {scenario:8s} worst abs diff {group['abs_diff'].max():.2e}")
        if check["abs_diff"].max() > RECONCILE_TOLERANCE:
            print(check[check["abs_diff"] > RECONCILE_TOLERANCE].to_string(index=False))
            raise SystemExit("recomputed metrics disagree with the committed evaluator")
        print("  ok — slices decompose the same numbers the committed reports headline")

    tossup_columns = ["dimension", "observations", "auc", "log_loss", "ece",
                      "buzz_position_mae", "brier", "reliability", "resolution"]
    print_frame("tossup metrics by dimension", tossups[tossup_columns])
    bonus_columns = ["dimension", "observations", "auc", "log_loss", "exact_acc",
                     "per_bonus_points_mae", "ppb_mae"]
    print_frame("bonus metrics by dimension", bonuses[bonus_columns])

    for name, frame in (
        ("metrics_by_dimension.csv", tossups),
        ("bonus_metrics_by_dimension.csv", bonuses),
    ):
        frame.to_csv(csv_path(arguments.output_dir, name), index=False)
        print(f"\nwrote {csv_path(arguments.output_dir, name)}  ({len(frame)} rows)")
    plot_overall(tossups, bonuses, arguments.output_dir)


if __name__ == "__main__":
    main()
