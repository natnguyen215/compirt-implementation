"""Evaluate saved CompIRT fitted predictions and create readable reports.

Start reading at 'main' below. It consumes the CSV files written by
'train_pyramidal.py' and 'train_compositional.py' and dispatches to the two
evaluation scenarios from the paper, each in its own module:

* 'compirt_eval.tossups.evaluate_tossups' -- Scenario A, Stage 1 first-buzz
  correctness, calibration, and timing (paper Section 5.1; Eq. 3-7, 13);
* 'compirt_eval.bonuses.evaluate_bonuses' -- Scenario B, Stage 2 bonus-part and
  points-per-bonus metrics plus optional synergy (paper Section 5.2; Eq. 8, 10, 11).

Shared building blocks live in 'compirt_eval.metrics' (metric/curve math) and
'compirt_eval.figures' (plotting primitives).

Important: these functions are model-agnostic and simply consume the saved
prediction CSVs. When fed a single-split run they report in-sample fit (useful
for optimization checks and model inspection). The temporal test runner uses
training posteriors as returning-player priors, then co-estimates test-player
and test-item parameters transductively as specified in paper Section 4.2. Its
metrics therefore measure a future tournament split under transductive
psychometric estimation, not fully inductive prediction of unseen questions.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from compirt_eval.bonuses import evaluate_bonuses
from compirt_eval.eval_docs import markdown_table, write_eval_docs_summary
from compirt_eval.outputs import csv_path, evaluation_output_dirs
from compirt_eval.tossups import evaluate_tossups, player_skill_stability_plot

# Re-exported so existing callers and tests can keep importing from this module.
from compirt_eval.metrics import bonus_metrics
from compirt_eval.figures import density_estimate
from compirt_eval.tossups import first_buzz_distribution


def main():
    """Load both stages' saved predictions and write metrics, plots, and report."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pyramidal-results", type=Path, required=True)
    parser.add_argument("--compositional-results", type=Path, required=True)
    parser.add_argument(
        "--comparison-pyramidal-results",
        type=Path,
        help="Optional second fitted pyramidal run for player-skill stability",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    evaluation_output_dirs(args.output_dir)
    # The evaluator intentionally consumes saved CSVs, so it can be rerun
    # without repeating expensive model training.
    tossup = evaluate_tossups(args.pyramidal_results, args.output_dir)
    bonus = evaluate_bonuses(args.compositional_results, args.output_dir)
    if args.comparison_pyramidal_results:
        player_skill_stability_plot(
            args.pyramidal_results,
            args.comparison_pyramidal_results,
            args.output_dir,
        )
    pd.DataFrame([tossup]).to_csv(
        csv_path(args.output_dir, "tossup_metrics.csv"), index=False
    )
    pd.DataFrame([bonus]).to_csv(
        csv_path(args.output_dir, "bonus_metrics.csv"), index=False
    )
    # Create a small Markdown report that can be read without loading pandas.
    report = (
        "# CompIRT Experiment Report\n\n"
        "## Tossup Metrics\n\n"
        + markdown_table(pd.DataFrame([tossup]))
        + "\n\n## Bonus Metrics\n\n"
        + markdown_table(pd.DataFrame([bonus]))
        + "\n\nGenerated figures include aggregate and buzz-position-stratified "
        "reliability, tossup difficulty over empirical buzz locations, "
        "per-dimension difficulty overlays for multidim fits, "
        "predicted-versus-empirical buzz timing, bonus PPB predictions, and "
        "player, tossup, bonus-part, and optional synergy parameter "
        "distributions and cross-run player-stability diagnostics.\n"
    )
    (args.output_dir / "experiment_report.md").write_text(report, encoding="utf-8")
    write_eval_docs_summary(args.output_dir)


if __name__ == "__main__":
    main()
