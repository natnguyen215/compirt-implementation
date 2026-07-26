#!/usr/bin/env python3
"""Random-drop robustness curves for the player-ranking comparators (Tier 1).

Following the uniform data-dropping experiment of arXiv 2508.11847: for each
drop fraction and replicate, remove a random set of buzz events, refit each
Stage-1 model at one fixed seed, and measure how far each method's
predicted-PPG ranking drifts from its own full-data ranking. The raw
actual-PPG ranking is recomputed on the same dropped frames without a refit.

Per-family noise floors (full data, alternate seeds) are recorded as
fraction-0 rows: a drop-induced change smaller than a family's own seed
jitter is not a finding. All fits are resumable off their summary.json.

    .venv/bin/python run_scripts/common/run_drop_robustness.py --help
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_data import DEFAULT_DATA_DIR
from compirt_eval.common.player_scoring import build_observations
from compirt_eval.drop_robustness.figures import save_tier1_outputs
from compirt_eval.drop_robustness.layout import (
    cell_dir,
    droplist_path,
    fraction_label,
    full_dir,
    noise_dir,
)
from compirt_eval.drop_robustness.perturbations import (
    random_drop_events,
    write_drop_list,
)
from compirt_eval.drop_robustness.tier1 import collect_results
from run_scripts.common.lib.ablation import (
    Stage,
    configure_environment,
    path_for_command,
    repo_path,
    run_stage,
    save_ablation_config,
    start_run_log,
    validate_ablation_resume,
)
from run_scripts.common.lib.drop_training import FAMILY_DEFAULTS, train_command
from utils.run_logging import format_run_log_header, resolve_result_root

DEFAULT_ROOT = Path("results/compirt/in_sample/common/drop-robustness")
DEFAULT_FRACTIONS = (0.001, 0.005, 0.01, 0.05)
DEFAULT_NOISE_SEEDS = (7, 123)


def generate_droplists(args: argparse.Namespace, observations: pd.DataFrame) -> None:
    """Write every (fraction, replicate) drop list up front.

    Existing files are never regenerated: completed fits were trained against
    exactly the file on disk, so the saved list is the artifact of record.
    """
    for fraction in args.fractions:
        for replicate in range(1, args.replicates + 1):
            path = droplist_path(args.root, fraction, replicate)
            if path.exists():
                continue
            rng = np.random.default_rng(
                [args.drop_seed, int(round(fraction * 1e6)), replicate]
            )
            write_drop_list(path, random_drop_events(observations, fraction, rng))
            print(f"wrote {path_for_command(path)}", flush=True)


def build_stages(args: argparse.Namespace) -> list[Stage]:
    """Full fit, noise-seed fits, and every drop cell for each family."""
    stages = []
    for model in args.models:
        full = full_dir(args.root, model)
        stages.append(
            Stage(
                f"{model}-full",
                full / "summary.json",
                train_command(args, model, full, args.seed),
            )
        )
        for seed in args.noise_seeds:
            noise = noise_dir(args.root, model, seed)
            stages.append(
                Stage(
                    f"{model}-noise-seed{seed}",
                    noise / "summary.json",
                    train_command(args, model, noise, seed),
                )
            )
        for fraction in args.fractions:
            for replicate in range(1, args.replicates + 1):
                cell = cell_dir(args.root, model, fraction, replicate)
                stages.append(
                    Stage(
                        f"{model}-frac{fraction_label(fraction)}-rep{replicate}",
                        cell / "summary.json",
                        train_command(
                            args,
                            model,
                            cell,
                            args.seed,
                            drop_file=droplist_path(args.root, fraction, replicate),
                        ),
                    )
                )
    return stages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument(
        "--models",
        nargs="+",
        choices=tuple(FAMILY_DEFAULTS),
        default=list(FAMILY_DEFAULTS),
    )
    parser.add_argument(
        "--fractions", nargs="+", type=float, default=list(DEFAULT_FRACTIONS)
    )
    parser.add_argument("--replicates", type=int, default=3)
    parser.add_argument(
        "--drop-seed",
        type=int,
        default=2025,
        help="RNG seed for generating the random drop lists",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="one fixed model seed for every full and dropped fit",
    )
    parser.add_argument(
        "--noise-seeds",
        nargs="*",
        type=int,
        default=list(DEFAULT_NOISE_SEEDS),
        help="alternate seeds for the full-data noise-floor fits",
    )
    parser.add_argument("--split", default="year_2024")
    parser.add_argument("--tournament")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument(
        "--difficulty-link", choices=("sigmoid", "tanh"), default="sigmoid"
    )
    parser.add_argument(
        "--dimensions", type=int, help="override every family's dimension default"
    )
    parser.add_argument(
        "--steps", type=int, help="override every family's step default (smoke runs)"
    )
    parser.add_argument("--lr", type=float, help="override every family's lr default")
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument(
        "--python",
        type=Path,
        default=Path(os.environ.get("PYTHON", REPO_ROOT / ".venv" / "bin" / "python")),
    )
    parser.add_argument(
        "--rerun",
        action="store_true",
        help="Run stages even when their expected output files already exist.",
    )
    parser.add_argument(
        "--collect-only",
        action="store_true",
        help="Only rebuild the aggregate CSV and graphs from existing run folders.",
    )
    args = parser.parse_args()
    args.root = Path(resolve_result_root(repo_path(args.root), "in_sample"))
    args.data_dir = repo_path(args.data_dir)
    if args.replicates < 1:
        raise ValueError("--replicates must be at least 1")
    return args


def main() -> None:
    args = parse_args()
    configure_environment()
    start_run_log(args.root)
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/common/run_drop_robustness.py",
                "ROOT": path_for_command(args.root),
                "MODELS": args.models,
                "FRACTIONS": args.fractions,
                "REPLICATES": args.replicates,
                "DROP_SEED": args.drop_seed,
                "SEED": args.seed,
                "NOISE_SEEDS": args.noise_seeds,
                "SPLIT": args.split,
                "TOURNAMENT": args.tournament or "<all>",
                "DIFFICULTY_LINK": args.difficulty_link,
                "DEVICE": args.device,
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
        observations = build_observations(
            args.split,
            args.tournament,
            args.data_dir or DEFAULT_DATA_DIR,
        )
        generate_droplists(args, observations)
        stages = build_stages(args)
        validate_ablation_resume(args.root, stages, args.rerun)
        config_path = save_ablation_config(args.root, args, stages)
        print(f"Wrote run configuration to {path_for_command(config_path)}\n", flush=True)
        for stage in stages:
            run_stage(stage, args.rerun)

    metrics = collect_results(args)
    output = save_tier1_outputs(args.root, metrics)
    print(f"\nWrote aggregate metrics to {path_for_command(output)}")
    print(f"Wrote aggregate graphs to {path_for_command(args.root / 'graphs')}")


if __name__ == "__main__":
    main()
