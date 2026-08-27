#!/usr/bin/env python3
"""Run a held-out multidim CompIRT dimension ablation with synergy only.

Each dimension gets its own run directory under the ablation root. The runner
calls the training and evaluation entry points directly and executes the
synergy branch for each dimension.

'--pyramidal-module' picks the Stage-1 trainer: the plain multidim MIRT model or
the TF-IDF multidim variant, which take the same dimension and held-out-prior
flags. Both branches use 'train_compositional' for Stage 2.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-compirt")

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_eval.common.report_paths import csv_path
from run_scripts.common.lib.ablation import (
    Stage,
    add_shared_sweep_arguments,
    configure_environment,
    finalize_shared_sweep_args,
    optional_path_args,
    path_for_command,
    read_metrics,
    read_summary,
    run_dir,
    run_stage,
    save_ablation_config,
    save_metric_plot,
    start_run_log,
    tossup_accuracy_from_predictions,
    tournament_args,
    validate_ablation_resume,
)
from utils.run_logging import format_run_log_header

DEFAULT_ROOT = Path("results/compirt/holdout/multidim/multidim-ablation")
DEFAULT_DIMENSIONS = (11, 12, 13, 14, 15)
DEFAULT_PLOT_DIMENSIONS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

# The selected module determines the Stage-1 model. 'build_stages' also adds
# the difficulty flag supported by that module.
PYRAMIDAL_MODULES = {
    "multidim": "multidimensional.multidim_mirt.train_pyramidal",
    "multidim-tanhbias": "multidimensional.multidim_mirt.train_pyramidal_tanhbias",
    "tfidf-multidim": "tfidf.multidim.train_pyramidal",
}


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
    train_filter_args = data_args + tournament_args(args.tournament)
    calibration_args = ["--calibrate-correctness"] if args.calibrate_correctness else []
    synergy_detail_args = ["--save-synergy-details"] if args.save_synergy_details else []
    alpha_prior_args = ["--alpha-prior", args.alpha_prior]
    # Each Stage-1 trainer takes a different difficulty flag: the plain multidim
    # trainer chooses a link, the biased-tanh variant takes a fixed scale, and the
    # TF-IDF variant takes neither.
    if args.pyramidal_module == "multidim":
        difficulty_args = ["--difficulty-link", args.difficulty_link]
    elif args.pyramidal_module == "multidim-tanhbias":
        difficulty_args = ["--difficulty-scale", str(args.difficulty_scale)]
    else:
        difficulty_args = []

    return [
        Stage(
            "train-pyramidal",
            train_pyr / "summary.json",
            [
                python,
                "-m",
                PYRAMIDAL_MODULES[args.pyramidal_module],
                "--split",
                args.train_split,
                *train_filter_args,
                "--dimensions",
                str(dimension),
                *difficulty_args,
                "--steps",
                str(args.pyramidal_steps),
                "--lr",
                str(args.lr),
                "--seed",
                str(args.seed),
                "--device",
                args.device,
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
                PYRAMIDAL_MODULES[args.pyramidal_module],
                "--split",
                args.test_split,
                *train_filter_args,
                "--dimensions",
                str(dimension),
                *difficulty_args,
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
                "--new-player-prior",
                args.new_player_prior,
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
                "train_compositional",
                "--split",
                args.test_split,
                *train_filter_args,
                "--player-skills",
                path_for_command(holdout_pyr / "players.csv"),
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
                *alpha_prior_args,
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
                "evaluate_compirt",
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
    """Collect summaries and held-out metrics for one dimension."""
    current_run = run_dir(root, dimension)
    train_pyr = current_run / "train" / "pyramidal"
    holdout_pyr = current_run / "holdout" / "pyramidal"
    synergy = current_run / "holdout" / "synergy"
    evaluation = current_run / "holdout" / "synergy-evaluation"

    row: dict[str, object] = {
        "dimension": dimension,
        "run_path": path_for_command(current_run),
    }
    row.update(read_summary(train_pyr / "summary.json", "train_pyramidal"))
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
    """Collect all ablation rows ordered by dimension."""
    rows = [collect_run(root, dimension) for dimension in dimensions]
    return pd.DataFrame(rows).sort_values("dimension").reset_index(drop=True)


def save_aggregate_outputs(root: Path, frame: pd.DataFrame) -> Path:
    """Write the aggregate CSV and all ablation graphs."""
    csv_output = csv_path(root, "multidim_ablation_metrics.csv")
    frame.to_csv(csv_output, index=False)
    save_metric_plot(
        frame,
        root,
        "bonus_log_loss",
        "bonus_validation_loss_vs_dimensions.png",
        "Bonus Val. Log Loss",
        "Bonus validation loss vs latent dimensions",
    )
    save_metric_plot(
        frame,
        root,
        "bonus_part_accuracy",
        "bonus_validation_accuracy_vs_dimensions.png",
        "Bonus Val. Part Accuracy",
        "Bonus validation accuracy vs latent dimensions",
    )
    save_metric_plot(
        frame,
        root,
        "tossup_log_loss",
        "tossup_validation_loss_vs_dimensions.png",
        "Tossup Val. Log Loss",
        "Tossup validation loss vs latent dimensions",
    )
    save_metric_plot(
        frame,
        root,
        "tossup_auc",
        "tossup_validation_auc_vs_dimensions.png",
        "Tossup Val. AUC",
        "Tossup validation AUC vs latent dimensions",
    )
    save_metric_plot(
        frame,
        root,
        "tossup_accuracy",
        "tossup_validation_accuracy_vs_dimensions.png",
        "Tossup Val. Accuracy",
        "Tossup validation accuracy vs latent dimensions",
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
        help="Latent skill dimensions to run.",
    )
    parser.add_argument(
        "--plot-dimensions",
        type=int,
        nargs="+",
        default=list(DEFAULT_PLOT_DIMENSIONS),
        help="Latent skill dimensions to include in the aggregate CSV and graphs.",
    )
    parser.add_argument("--synergy-dimensions", type=int, default=3)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--pyramidal-module",
        choices=tuple(PYRAMIDAL_MODULES),
        default="multidim",
        help="Stage-1 trainer to sweep: plain multidim MIRT or its TF-IDF variant.",
    )
    parser.add_argument(
        "--alpha-prior",
        choices=("normal", "gamma"),
        default="gamma",
        help=(
            "Bonus-part discrimination prior. 'gamma' matches the Gamma(2, 2) "
            "relevance vector of the multidim pyramidal stage."
        ),
    )
    parser.add_argument(
        "--difficulty-link",
        choices=("sigmoid", "tanh"),
        default="sigmoid",
        help="Difficulty link inside d_jk(t) for the plain multidim trainer; "
        "tanh lets difficulty go negative late.",
    )
    parser.add_argument(
        "--difficulty-scale",
        type=float,
        default=5.0,
        help="Fixed amplitude of the biased-tanh difficulty curve for the "
        "multidim-tanhbias trainer: d_jk(t) = tanh(... + bias_jk) * scale.",
    )
    add_shared_sweep_arguments(parser, DEFAULT_ROOT)
    args = finalize_shared_sweep_args(parser.parse_args())
    if args.difficulty_link != "sigmoid" and args.pyramidal_module != "multidim":
        raise ValueError(
            "--difficulty-link is only supported by --pyramidal-module multidim"
        )
    if args.difficulty_scale <= 0:
        raise ValueError("--difficulty-scale must be positive")
    if any(dimension < 1 for dimension in args.dimensions):
        raise ValueError("--dimensions values must all be at least 1")
    if any(dimension < 1 for dimension in args.plot_dimensions):
        raise ValueError("--plot-dimensions values must all be at least 1")
    if args.synergy_dimensions < 1:
        raise ValueError("--synergy-dimensions must be at least 1")
    return args


def main() -> None:
    """Run the ablation, then write aggregate metrics and plots."""
    args = parse_args()
    configure_environment()
    start_run_log(args.root)
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/multidimensional/multidim/run_multidim_ablation.py",
                "ROOT": path_for_command(args.root),
                "MODEL": f"{args.pyramidal_module}-ablation",
                "PYRAMIDAL_MODULE": PYRAMIDAL_MODULES[args.pyramidal_module],
                "TRAIN_SPLIT": args.train_split,
                "TEST_SPLIT": args.test_split,
                "TOURNAMENT": args.tournament or "<all>",
                "DEVICE": args.device,
                "GPU": os.environ.get("GPU", "unknown"),
                "SURVIVAL_CHUNK": os.environ.get("COMPIRT_SURVIVAL_CHUNK", "full-batch"),
                "DIMENSIONS": args.dimensions,
                "PLOT_DIMENSIONS": args.plot_dimensions,
                "SYNERGY_DIMENSIONS": args.synergy_dimensions,
                "ALPHA_PRIOR": args.alpha_prior,
                "DIFFICULTY_LINK": args.difficulty_link
                if args.pyramidal_module == "multidim"
                else "",
                "DIFFICULTY_SCALE": args.difficulty_scale
                if args.pyramidal_module == "multidim-tanhbias"
                else "",
                "PYRAMIDAL_STEPS": args.pyramidal_steps,
                "BONUS_STEPS": args.bonus_steps,
                "LR": args.lr,
                "SEED": args.seed,
                "NEW_PLAYER_PRIOR": args.new_player_prior,
                "CALIBRATE_CORRECTNESS": args.calibrate_correctness,
                "SAVE_SYNERGY_DETAILS": args.save_synergy_details,
                "COLLECT_ONLY": args.collect_only,
                "RERUN": args.rerun,
                "PYTHON": path_for_command(args.python),
                "DATA_DIR": path_for_command(args.data_dir)
                if args.data_dir is not None
                else "",
            }
        ),
        flush=True,
    )

    if not args.collect_only:
        stages = [
            stage
            for dimension in args.dimensions
            for stage in build_stages(args, dimension)
        ]
        validate_ablation_resume(
            args.root, stages, args.rerun, allow_partial_resume=True
        )
        # Record the run configuration before training. Collect-only passes keep
        # the configuration written by the training sweep.
        config_path = save_ablation_config(args.root, args, stages)
        print(f"Wrote run configuration to {path_for_command(config_path)}\n", flush=True)
        for stage in stages:
            run_stage(stage, args.rerun)

    metrics = collect_results(args.root, args.plot_dimensions)
    csv_output = save_aggregate_outputs(args.root, metrics)
    print(f"\nWrote aggregate metrics to {path_for_command(csv_output)}")
    print(f"Wrote aggregate graphs to {path_for_command(args.root / 'graphs')}")


if __name__ == "__main__":
    main()
