"""Shared training-command construction for drop-robustness launchers."""

from __future__ import annotations

import argparse
from pathlib import Path

from run_scripts.common.lib.ablation import path_for_command, tournament_args

FAMILY_DEFAULTS = {
    "plain": {"dimensions": 1, "steps": 1000, "lr": 0.02},
    "baseline": {"dimensions": 5, "steps": 5000, "lr": 0.005},
    "multidim": {"dimensions": 5, "steps": 3000, "lr": 0.01},
}


def family_config(args: argparse.Namespace, model: str) -> dict[str, object]:
    """Per-family training knobs, with any global overrides applied."""
    config = dict(FAMILY_DEFAULTS[model])
    if args.dimensions is not None:
        config["dimensions"] = args.dimensions
    if args.steps is not None:
        config["steps"] = args.steps
    if args.lr is not None:
        config["lr"] = args.lr
    return config


def train_command(
    args: argparse.Namespace,
    model: str,
    output_dir: Path,
    seed: int,
    drop_file: Path | None = None,
) -> list[str]:
    """Build one family-specific trainer invocation."""
    python = str(args.python)
    if model == "baseline":
        command = [python, "train_pyramidal.py"]
    elif model == "multidim":
        command = [
            python,
            "-m",
            "multidimensional.multidim_mirt.train_pyramidal",
            "--difficulty-link",
            args.difficulty_link,
        ]
    elif model == "plain":
        command = [python, "-m", "simple_mirt.train_plain_irt"]
    else:
        raise ValueError(f"Unknown model: {model}")
    config = family_config(args, model)
    command += [
        "--split",
        args.split,
        *tournament_args(args.tournament),
        "--dimensions",
        str(config["dimensions"]),
        "--steps",
        str(config["steps"]),
        "--lr",
        str(config["lr"]),
        "--seed",
        str(seed),
        "--device",
        args.device,
        "--output-dir",
        path_for_command(output_dir),
    ]
    if args.data_dir is not None:
        command += ["--data-dir", path_for_command(args.data_dir)]
    if drop_file is not None:
        command += ["--drop-events", path_for_command(drop_file)]
    return command
