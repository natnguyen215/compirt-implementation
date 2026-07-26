#!/usr/bin/env python3
"""Fit and analyze the multidimensional tanh seed-noise-floor study.

The runner trains the same Stage-1 model on identical data under several SVI
seeds, then delegates all saved-fit scoring to ``compirt_eval.noise_floor``.
Completed seed fits are reused by default; ``--rerun`` refits them and
``--collect-only`` rebuilds the analysis without launching training.

    .venv/bin/python \
        run_scripts/multidimensional/multidim/run_multidim_noise_floor.py
"""

from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_data import DEFAULT_DATA_DIR
from compirt_eval.noise_floor.evaluation import (
    DEFAULT_LINK,
    DEFAULT_ROOT,
    DEFAULT_SPLIT,
    analyze,
)
from utils.run_logging import resolve_result_root

DEFAULT_SEEDS = (42, 7, 123, 2024, 31337)
DEFAULT_GPUS = ("0", "1")
TRAINER = REPO_ROOT / "multidimensional" / "multidim_mirt" / "train_pyramidal.py"


def train_command(args: argparse.Namespace, seed: int, output_dir: Path) -> list[str]:
    """Construct one seed fit with the historical study defaults."""
    command = [
        str(args.python),
        str(TRAINER),
        "--split",
        args.split,
        "--dimensions",
        str(args.dimensions),
        "--difficulty-link",
        args.difficulty_link,
        "--steps",
        str(args.steps),
        "--lr",
        str(args.lr),
        "--device",
        args.device,
        "--seed",
        str(seed),
        "--output-dir",
        str(output_dir),
    ]
    if args.data_dir is not None:
        command.extend(("--data-dir", str(args.data_dir)))
    return command


def _run_wave(
    args: argparse.Namespace,
    assignments: list[tuple[int, str]],
) -> None:
    """Run one at-most-one-process-per-GPU wave and fail on any bad fit."""
    running = []
    for seed, gpu in assignments:
        output_dir = args.root / f"seed_{seed}" / "pyramidal"
        expected = output_dir / "summary.json"
        if expected.exists() and not args.rerun:
            print(f"skip seed={seed}: {expected} exists", flush=True)
            continue

        output_dir.mkdir(parents=True, exist_ok=True)
        log_path = args.root / f"seed_{seed}" / "run.log"
        log_handle = log_path.open("w", encoding="utf-8")
        command = train_command(args, seed, output_dir)
        environment = os.environ.copy()
        if args.device == "cuda":
            environment["CUDA_VISIBLE_DEVICES"] = gpu
        print(
            f"launching seed={seed} on "
            f"{'GPU ' + gpu if args.device == 'cuda' else 'CPU'} -> {output_dir}",
            flush=True,
        )
        print("+ " + shlex.join(command), flush=True)
        try:
            process = subprocess.Popen(
                command,
                cwd=REPO_ROOT,
                env=environment,
                stdout=log_handle,
                stderr=subprocess.STDOUT,
            )
        except BaseException:
            log_handle.close()
            raise
        running.append((seed, process, log_handle))

    failures = []
    for seed, process, log_handle in running:
        returncode = process.wait()
        log_handle.close()
        if returncode:
            failures.append((seed, returncode))
    if failures:
        details = ", ".join(f"seed {seed}: exit {code}" for seed, code in failures)
        raise RuntimeError(f"noise-floor training failed ({details})")


def run_training(args: argparse.Namespace) -> None:
    """Schedule seeds in the same two-GPU waves as the historical launcher."""
    assignments = [
        (seed, args.gpus[index % len(args.gpus)])
        for index, seed in enumerate(args.seeds)
    ]
    for start in range(0, len(assignments), len(args.gpus)):
        _run_wave(args, assignments[start : start + len(args.gpus)])


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--seeds", nargs="+", type=int, default=list(DEFAULT_SEEDS))
    parser.add_argument(
        "--gpus",
        nargs="+",
        default=list(DEFAULT_GPUS),
        help="CUDA device IDs used one per concurrent fit (default: 0 1)",
    )
    parser.add_argument("--split", default=DEFAULT_SPLIT)
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--dimensions", type=int, default=5)
    parser.add_argument(
        "--difficulty-link", choices=("sigmoid", "tanh"), default=DEFAULT_LINK
    )
    parser.add_argument("--steps", type=int, default=3000)
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument(
        "--python",
        type=Path,
        default=Path(
            os.environ.get("PYTHON", REPO_ROOT / ".venv" / "bin" / "python")
        ),
    )
    parser.add_argument(
        "--rerun",
        action="store_true",
        help="Refit seeds even when their summary.json already exists.",
    )
    parser.add_argument(
        "--collect-only",
        action="store_true",
        help="Only rebuild predicted_ppg_by_seed.csv from completed seed fits.",
    )
    args = parser.parse_args(argv)
    args.root = Path(resolve_result_root(args.root, "in_sample"))
    if not args.root.is_absolute():
        args.root = REPO_ROOT / args.root
    if args.data_dir is not None and not args.data_dir.is_absolute():
        args.data_dir = REPO_ROOT / args.data_dir
    if args.dimensions < 1:
        parser.error("--dimensions must be at least 1")
    if args.steps < 1:
        parser.error("--steps must be at least 1")
    return args


def main(argv=None) -> None:
    args = parse_args(argv)
    if not args.collect_only:
        run_training(args)
        print("ALL NOISE-FLOOR RUNS DONE", flush=True)
    analyze(
        root=args.root,
        split=args.split,
        data_dir=args.data_dir or DEFAULT_DATA_DIR,
        link=args.difficulty_link,
    )


if __name__ == "__main__":
    main()
