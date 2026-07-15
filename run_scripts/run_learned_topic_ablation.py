#!/usr/bin/env python3
"""Run a held-out learned-topic CompIRT topic-count ablation with synergy only.

The learned (joint sLDA) family ties the topic count to the IRT skill
dimensionality, so sweeping '--dimensions' sweeps the number of topics K. Each
topic count gets its own run directory under the ablation root. The runner
intentionally calls the underlying training/evaluation entry points directly so
it can skip the no-synergy compositional branch used by the standard holdout
driver.

Stage 2 never receives '--dimensions': 'train_joint_compositional' infers K from
the saved player skills and validates it against the frozen topic-word matrix.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-compirt")

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_eval.outputs import csv_path
from run_scripts.lib.ablation import (
    Stage,
    add_shared_sweep_arguments,
    configure_environment,
    finalize_shared_sweep_args,
    optional_path_args,
    path_for_command,
    read_metrics,
    read_summary,
    repo_path,
    run_dir,
    run_stage,
    save_ablation_config,
    save_metric_plot,
    start_run_log,
    tossup_accuracy_from_predictions,
    tournament_args,
)
from utils.run_logging import format_run_log_header

DEFAULT_ROOT = Path("results/compirt/holdout/learned-topic-ablation")
DEFAULT_DIMENSIONS = tuple(range(1, 16))
DEFAULT_PLOT_DIMENSIONS = tuple(range(1, 16))
# The TF-IDF learned trainer takes the same topic/vocabulary/holdout-prior flags
# as the plain learned one, so the sweep only swaps Stage 1 and the evaluator
# that replays its saved TF-IDF adjustment curves. Stage 2 is unchanged.
PYRAMIDAL_MODULES = {
    "learned": ("topic.learned.train_joint_pyramidal", "topic.fixed.evaluate_topic_compirt"),
    "learned-tfidf": ("topic.tfidf.train_learned_pyramidal", "topic.tfidf.evaluate"),
}
# Topic-model settings carried into every aggregate CSV row: 'topic/learned'
# warns that an unrecorded bow_weight makes a run irreproducible, and the same
# argument applies to the Dirichlet alpha and the vocabulary knobs.
TOPIC_SUMMARY_FIELDS = (
    "bow_weight",
    "topic_concentration",
    "vocab_size",
    "vocab_size_limit",
    "min_df",
    "rm_top",
    "seed",
)


def topic_model_args(args: argparse.Namespace) -> list[str]:
    """Return the topic-model knobs both stages share."""
    return [
        "--bow-weight",
        str(args.bow_weight),
        "--topic-concentration",
        str(args.topic_concentration),
    ]


def vocabulary_args(args: argparse.Namespace) -> list[str]:
    """Return the Stage-1-only vocabulary knobs; Stage 2 inherits them."""
    return [
        "--vocab-size",
        str(args.vocab_size),
        "--min-df",
        str(args.min_df),
        "--rm-top",
        str(args.rm_top),
    ]


def build_stages(args: argparse.Namespace, dimension: int) -> list[Stage]:
    """Build the exact training/evaluation commands for one ablation point."""
    root = args.root
    current_run = run_dir(root, dimension)
    train_pyr = current_run / "train" / "pyramidal"
    holdout_pyr = current_run / "holdout" / "pyramidal"
    holdout_synergy = current_run / "holdout" / "synergy"
    holdout_synergy_eval = current_run / "holdout" / "synergy-evaluation"

    python = path_for_command(args.python)
    data_args = optional_path_args("--data-dir", args.data_dir)
    database_args = optional_path_args("--database", args.database)
    train_filter_args = data_args + database_args + tournament_args(args.tournament)
    calibration_args = ["--calibrate-correctness"] if args.calibrate_correctness else []
    # The learned trainer declares this as a plain store_true flag, so it is
    # either appended or omitted -- there is no --no- form to pass.
    predict_args = ["--predict-buzz-positions"] if args.predict_buzz_positions else []
    synergy_detail_args = ["--save-synergy-details"] if args.save_synergy_details else []
    topic_args = topic_model_args(args)
    pyramidal_module, evaluate_module = PYRAMIDAL_MODULES[args.pyramidal_module]

    return [
        Stage(
            "train-pyramidal",
            train_pyr / "summary.json",
            [
                python,
                "-m",
                pyramidal_module,
                "--split",
                args.train_split,
                *train_filter_args,
                "--dimensions",
                str(dimension),
                *vocabulary_args(args),
                *topic_args,
                "--steps",
                str(args.pyramidal_steps),
                "--lr",
                str(args.lr),
                "--seed",
                str(args.seed),
                "--device",
                args.device,
                *predict_args,
                *calibration_args,
                "--output-dir",
                path_for_command(train_pyr),
            ],
        ),
        Stage(
            "holdout-pyramidal",
            holdout_pyr / "summary.json",
            [
                python,
                "-m",
                pyramidal_module,
                "--split",
                args.test_split,
                *train_filter_args,
                "--dimensions",
                str(dimension),
                *vocabulary_args(args),
                *topic_args,
                "--steps",
                str(args.pyramidal_steps),
                "--lr",
                str(args.lr),
                "--seed",
                str(args.seed),
                "--device",
                args.device,
                "--train-posterior",
                path_for_command(train_pyr / "player_posterior.csv"),
                # Required alongside --train-posterior: the held-out pass reuses
                # the trained topic-word matrix and vocabulary.
                "--train-topic-model",
                path_for_command(train_pyr),
                "--new-player-prior",
                args.new_player_prior,
                *predict_args,
                *calibration_args,
                "--output-dir",
                path_for_command(holdout_pyr),
            ],
        ),
        Stage(
            "synergy",
            holdout_synergy / "summary.json",
            [
                python,
                "-m",
                "topic.learned.train_joint_compositional",
                "--split",
                args.test_split,
                *train_filter_args,
                "--player-skills",
                path_for_command(holdout_pyr / "players.csv"),
                # Frozen topics come from the training run, not the held-out one.
                "--topic-model-dir",
                path_for_command(train_pyr),
                *topic_args,
                "--steps",
                str(args.bonus_steps),
                "--lr",
                str(args.lr),
                "--seed",
                str(args.seed),
                "--device",
                args.device,
                "--use-synergy",
                "--synergy-dimensions",
                str(args.synergy_dimensions),
                *synergy_detail_args,
                *calibration_args,
                "--output-dir",
                path_for_command(holdout_synergy),
            ],
        ),
        Stage(
            "synergy-evaluation",
            holdout_synergy_eval / "experiment_report.md",
            [
                python,
                "-m",
                evaluate_module,
                "--pyramidal-results",
                path_for_command(holdout_pyr),
                "--compositional-results",
                path_for_command(holdout_synergy),
                "--output-dir",
                path_for_command(holdout_synergy_eval),
            ],
        ),
    ]


def collect_run(root: Path, dimension: int) -> dict[str, object]:
    """Collect summaries and held-out metrics for one topic count."""
    current_run = run_dir(root, dimension)
    train_pyr = current_run / "train" / "pyramidal"
    holdout_pyr = current_run / "holdout" / "pyramidal"
    synergy = current_run / "holdout" / "synergy"
    evaluation = current_run / "holdout" / "synergy-evaluation"

    row: dict[str, object] = {
        "dimension": dimension,
        "run_path": path_for_command(current_run),
    }
    row.update(
        read_summary(
            train_pyr / "summary.json",
            "train_pyramidal",
            {name: name for name in TOPIC_SUMMARY_FIELDS},
        )
    )
    row.update(read_summary(holdout_pyr / "summary.json", "holdout_pyramidal"))
    row.update(
        read_summary(
            synergy / "summary.json",
            "synergy",
            {"synergy_dimensions": "synergy_dimensions", "synergy_tau": "tau"},
        )
    )
    row.update(read_metrics(evaluation, "bonus_metrics.csv", "bonus"))
    row.update(read_metrics(evaluation, "tossup_metrics.csv", "tossup"))
    if "tossup_accuracy" not in row:
        accuracy = tossup_accuracy_from_predictions(holdout_pyr / "tossup_predictions.csv")
        if accuracy is not None:
            row["tossup_accuracy"] = accuracy
    return row


def collect_results(root: Path, dimensions: list[int]) -> pd.DataFrame:
    """Collect all ablation rows ordered by topic count."""
    rows = [collect_run(root, dimension) for dimension in dimensions]
    return pd.DataFrame(rows).sort_values("dimension").reset_index(drop=True)


def save_aggregate_outputs(root: Path, frame: pd.DataFrame) -> Path:
    """Write the aggregate CSV and all ablation graphs."""
    csv_output = csv_path(root, "learned_topic_ablation_metrics.csv")
    frame.to_csv(csv_output, index=False)
    plots = (
        ("bonus_log_loss", "bonus_validation_loss_vs_topics.png",
         "Bonus Val. Log Loss", "Bonus validation loss vs topic count"),
        ("bonus_part_accuracy", "bonus_validation_accuracy_vs_topics.png",
         "Bonus Val. Part Accuracy", "Bonus validation accuracy vs topic count"),
        ("tossup_log_loss", "tossup_validation_loss_vs_topics.png",
         "Tossup Val. Log Loss", "Tossup validation loss vs topic count"),
        ("tossup_auc", "tossup_validation_auc_vs_topics.png",
         "Tossup Val. AUC", "Tossup validation AUC vs topic count"),
        ("tossup_accuracy", "tossup_validation_accuracy_vs_topics.png",
         "Tossup Val. Accuracy", "Tossup validation accuracy vs topic count"),
    )
    for metric, filename, ylabel, title in plots:
        save_metric_plot(
            frame,
            root,
            metric,
            filename,
            ylabel,
            title,
            xlabel="Number of topics (K)",
        )
    return csv_output


def parse_args() -> argparse.Namespace:
    """Parse command-line options for the ablation runner."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dimensions",
        type=int,
        nargs="+",
        default=list(DEFAULT_DIMENSIONS),
        help="Topic counts (== IRT skill dimensions) to run.",
    )
    parser.add_argument(
        "--plot-dimensions",
        type=int,
        nargs="+",
        default=list(DEFAULT_PLOT_DIMENSIONS),
        help="Topic counts to include in the aggregate CSV and graphs.",
    )
    parser.add_argument("--synergy-dimensions", type=int, default=3)
    parser.add_argument(
        "--pyramidal-module",
        choices=tuple(PYRAMIDAL_MODULES),
        default="learned",
        help="Stage-1 trainer to sweep: joint sLDA, or its per-topic TF-IDF variant.",
    )
    parser.add_argument("--database", type=Path)
    parser.add_argument(
        "--bow-weight",
        type=float,
        default=0.1,
        help="Scale on the LDA word likelihood vs. the outcome likelihood. At the "
        "trainer's default of 1.0 words dominate and topics come out nearly "
        "unsupervised, so this runner defaults lower; sweep ~0.05-1.0 against a "
        "held-out IRT metric.",
    )
    parser.add_argument(
        "--topic-concentration",
        type=float,
        default=1.0,
        help="Dirichlet alpha for theta_doc; lower (<1) gives sparser topic mixes.",
    )
    parser.add_argument("--vocab-size", type=int, default=2000)
    parser.add_argument("--min-df", type=int, default=2)
    parser.add_argument("--rm-top", type=int, default=20)
    parser.add_argument("--seed", type=int, default=42)
    add_shared_sweep_arguments(parser, DEFAULT_ROOT)
    args = finalize_shared_sweep_args(parser.parse_args())
    args.database = repo_path(args.database)
    if any(dimension < 1 for dimension in args.dimensions):
        raise ValueError("--dimensions values must all be at least 1")
    if any(dimension < 1 for dimension in args.plot_dimensions):
        raise ValueError("--plot-dimensions values must all be at least 1")
    if args.synergy_dimensions < 1:
        raise ValueError("--synergy-dimensions must be at least 1")
    if args.bow_weight < 0:
        raise ValueError("--bow-weight must not be negative")
    if args.topic_concentration <= 0:
        raise ValueError("--topic-concentration must be positive")
    return args


def main() -> None:
    """Run the ablation, then write aggregate metrics and plots."""
    args = parse_args()
    configure_environment()
    start_run_log(args.root)
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/run_learned_topic_ablation.py",
                "ROOT": path_for_command(args.root),
                "MODEL": f"{args.pyramidal_module}-topic-ablation",
                "PYRAMIDAL_MODULE": PYRAMIDAL_MODULES[args.pyramidal_module][0],
                "EVALUATE_MODULE": PYRAMIDAL_MODULES[args.pyramidal_module][1],
                "TRAIN_SPLIT": args.train_split,
                "TEST_SPLIT": args.test_split,
                "TOURNAMENT": args.tournament or "<all>",
                "DEVICE": args.device,
                "GPU": os.environ.get("GPU", "unknown"),
                "DIMENSIONS": args.dimensions,
                "PLOT_DIMENSIONS": args.plot_dimensions,
                "SYNERGY_DIMENSIONS": args.synergy_dimensions,
                "BOW_WEIGHT": args.bow_weight,
                "TOPIC_CONCENTRATION": args.topic_concentration,
                "VOCAB_SIZE": args.vocab_size,
                "MIN_DF": args.min_df,
                "RM_TOP": args.rm_top,
                "SEED": args.seed,
                "PYRAMIDAL_STEPS": args.pyramidal_steps,
                "BONUS_STEPS": args.bonus_steps,
                "LR": args.lr,
                "NEW_PLAYER_PRIOR": args.new_player_prior,
                "CALIBRATE_CORRECTNESS": args.calibrate_correctness,
                "PREDICT_BUZZ_POSITIONS": args.predict_buzz_positions,
                "SAVE_SYNERGY_DETAILS": args.save_synergy_details,
                "COLLECT_ONLY": args.collect_only,
                "RERUN": args.rerun,
                "PYTHON": path_for_command(args.python),
                "DATA_DIR": path_for_command(args.data_dir)
                if args.data_dir is not None
                else "",
                "DATABASE": path_for_command(args.database)
                if args.database is not None
                else "",
            }
        ),
        flush=True,
    )

    if not args.collect_only:
        # Written before training so a crashed sweep still records what it tried,
        # and never on a --collect-only pass, which would otherwise overwrite the
        # real sweep's settings with the aggregation run's defaults.
        config_path = save_ablation_config(args.root, args)
        print(f"Wrote run configuration to {path_for_command(config_path)}\n", flush=True)
        for dimension in args.dimensions:
            print(f"\n=== learned-topic ablation: {dimension} topics ===", flush=True)
            for stage in build_stages(args, dimension):
                run_stage(stage, args.rerun)

    metrics = collect_results(args.root, args.plot_dimensions)
    csv_output = save_aggregate_outputs(args.root, metrics)
    print(f"\nWrote aggregate metrics to {path_for_command(csv_output)}")
    print(f"Wrote aggregate graphs to {path_for_command(args.root / 'graphs')}")


if __name__ == "__main__":
    main()
