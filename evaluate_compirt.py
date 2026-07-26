"""Evaluate saved CompIRT fitted predictions and create readable reports.

'main' consumes the CSV files written by 'train_pyramidal.py' and
'train_compositional.py' and dispatches to the two evaluation scenarios from
the paper:

* 'compirt_eval.scenario_a_tossups.evaluate_tossups' -- Scenario A, Stage 1 first-buzz
  correctness, calibration, and timing (paper Section 5.1; Eq. 3-7, 13);
* 'compirt_eval.scenario_b_bonuses.evaluation.evaluate_bonuses' -- Scenario B, Stage 2 bonus-part and
  points-per-bonus metrics plus optional synergy (paper Section 5.2; Eq. 8, 10, 11).

Shared building blocks live in 'compirt_eval.common'; scenario-specific metric
math lives beside each scenario's evaluator.

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

from compirt_data import DEFAULT_DATA_DIR, filter_tournament, load_hf_tables
from compirt_eval.scenario_b_bonuses.evaluation import evaluate_bonuses
from compirt_eval.common.reports import (
    experiment_report_markdown,
    write_eval_docs_summary,
)
from compirt_eval.common.figures import stratified_ece_plot
from compirt_eval.diagnostics.match_simulation import simulate_match_winners
from compirt_eval.common.report_paths import csv_path, evaluation_output_dirs, graph_path
from compirt_eval.diagnostics.posterior_predictive import evaluate_saved_ppc
from compirt_eval.scenario_a_tossups import evaluate_tossups

# Public evaluation helpers available from this entry-point module.
from compirt_eval.common.figures import density_estimate
from compirt_eval.scenario_b_bonuses.metrics import bonus_metrics
from compirt_eval.scenario_a_tossups import first_buzz_distribution

__all__ = ["bonus_metrics", "density_estimate", "first_buzz_distribution", "main"]


def main():
    """Load both stages' saved predictions and write metrics, plots, and report."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pyramidal-results", type=Path, required=True)
    parser.add_argument("--compositional-results", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--game-simulations", type=int, default=500)
    parser.add_argument("--game-seed", type=int, default=42)
    parser.add_argument(
        "--skip-game-simulation",
        action="store_true",
        help="skip the optional raw-game match winner diagnostic",
    )
    args = parser.parse_args()
    evaluation_output_dirs(args.output_dir)
    # Saved CSVs make evaluation repeatable without rerunning model training.
    tossup = evaluate_tossups(args.pyramidal_results, args.output_dir)
    bonus = evaluate_bonuses(args.compositional_results, args.output_dir)
    evaluate_saved_ppc(
        args.pyramidal_results, args.compositional_results, args.output_dir
    )
    game = {}
    if not args.skip_game_simulation:
        tables = filter_tournament(
            load_hf_tables(args.data_dir, args.split), args.tournament
        )
        game, _ = simulate_match_winners(
            args.pyramidal_results,
            args.compositional_results,
            args.output_dir,
            tables["games"],
            simulations=args.game_simulations,
            seed=args.game_seed,
        )
    pd.DataFrame([tossup]).to_csv(
        csv_path(args.output_dir, "tossup_metrics.csv"), index=False
    )
    pd.DataFrame([bonus]).to_csv(
        csv_path(args.output_dir, "bonus_metrics.csv"), index=False
    )
    pd.DataFrame([game]).to_csv(
        csv_path(args.output_dir, "game_metrics.csv"), index=False
    )
    diagnostic_paths = [
        csv_path(args.output_dir, "tossup_prediction_diagnostics_by_stratum.csv"),
        csv_path(args.output_dir, "bonus_prediction_diagnostics_by_stratum.csv"),
    ]
    diagnostic_frames = [pd.read_csv(path) for path in diagnostic_paths if path.exists()]
    if diagnostic_frames:
        diagnostics = pd.concat(diagnostic_frames, ignore_index=True)
        diagnostics.to_csv(
            csv_path(args.output_dir, "prediction_diagnostics_by_stratum.csv"),
            index=False,
        )
        stratified_ece_plot(
            diagnostics,
            graph_path(args.output_dir, "prediction_ece_by_stratum.png", "diagnostics"),
        )
    # Create a small Markdown report that can be read without loading pandas.
    report = experiment_report_markdown(args.output_dir, tossup, bonus, game)
    (args.output_dir / "experiment_report.md").write_text(report, encoding="utf-8")
    write_eval_docs_summary(args.output_dir)


if __name__ == "__main__":
    main()
