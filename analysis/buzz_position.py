"""Does dimensionality help early or late buzzes — and via calibration or discrimination?

    .venv/bin/python -m analysis.buzz_position

Splits buzzes into early/middle/late thirds of relative position and reports
each third's metrics across the sweep. Log loss and AUC rank the thirds in
opposite orders, so the module also prints the Murphy decomposition
(Brier = reliability − resolution + uncertainty), which separates calibration
from discrimination additively instead of by argument. The established
reading: early buzzes gain *calibration* (the 1-D model is overconfident
there), late buzzes gain *discrimination*.
"""

from __future__ import annotations

import pandas as pd

from compirt_eval.outputs import csv_path, evaluation_output_dirs

from analysis.data import base_parser, load_buzzes, require_dimensions
from analysis.figures import plot_calibration_discrimination, plot_position
from analysis.metrics import endpoint_change, print_frame, score

POSITION_LABELS = ["Early third", "Middle third", "Late third"]
# Mirrors compirt_eval.tossups.reliability.stratified_tossup_reliability_plot.
POSITION_BINS = [0.0, 1 / 3, 2 / 3, 1.0]


def by_position(sweep_dir, dimensions):
    """Metrics split into early/middle/late buzz-position thirds."""
    rows = []
    for dimension in dimensions:
        buzzes = load_buzzes(sweep_dir, dimension)
        groups = pd.cut(
            buzzes["relative_position"],
            bins=POSITION_BINS,
            labels=POSITION_LABELS,
            include_lowest=True,
        )
        for label in POSITION_LABELS:
            rows.append(
                {
                    "dimension": dimension,
                    "position_group": label,
                    **score(buzzes[groups == label]),
                }
            )
    return pd.DataFrame(rows)


def change_table(position):
    """Per-third metric changes across the sweep, one row per third."""
    rows = []
    for group in POSITION_LABELS:
        row = {"position_group": group,
               "n": endpoint_change(position, "log_loss", position_group=group)[4]}
        for metric in ("log_loss", "auc", "reliability", "resolution", "buzz_position_mae"):
            row[f"d_{metric}"] = endpoint_change(position, metric, position_group=group)[2]
        rows.append(row)
    return pd.DataFrame(rows)


def main():
    arguments = base_parser(__doc__).parse_args()
    evaluation_output_dirs(arguments.output_dir)
    dimensions = require_dimensions(arguments.sweep_dir)

    position = by_position(arguments.sweep_dir, dimensions)
    print_frame(
        f"changes dim {min(dimensions)}→{max(dimensions)} by buzz third "
        "(d_reliability<0 = better calibrated, d_resolution>0 = better discrimination)",
        change_table(position),
    )
    residual = position["residual"].abs().max()
    print(f"\nmax |Murphy decomposition residual| = {residual:.1e} (should be ~0)")

    position.to_csv(csv_path(arguments.output_dir, "metrics_by_buzz_position.csv"), index=False)
    print(f"wrote {csv_path(arguments.output_dir, 'metrics_by_buzz_position.csv')}")
    plot_position(position, POSITION_LABELS, arguments.output_dir)
    plot_calibration_discrimination(position, POSITION_LABELS, arguments.output_dir)


if __name__ == "__main__":
    main()
