#!/usr/bin/env python3
"""Run the multidimensional-difficulty CompIRT pipeline.

Environment variables:

* 'SPLIT' / 'TOURNAMENT' select data; 'TOURNAMENT=""' means whole split.
* 'ROOT' chooses the output root.
* 'DIMENSIONS', 'PYRAMIDAL_STEPS', 'BONUS_STEPS', 'LR', and 'DEVICE'
  control fitting.
* 'CALIBRATE_CORRECTNESS=1' enables correctness-only calibration in both
  stages.
* 'SYNERGY_DIMENSIONS' controls the always-on synergy branch.
"""

from __future__ import annotations

import os
import shlex
import sys
from pathlib import Path

# This script lives in run_scripts/, so the repo root is one directory up. Add it
# to sys.path before importing repo packages so the script works when invoked
# directly (python run_scripts/run_multidim_compirt.py), not only as a module.
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from utils.run_logging import format_run_log_header, run_logged, tee_run_output

PYTHON = Path(
    os.environ.get("PYTHON", str(REPO_ROOT / ".venv" / "bin" / "python"))
)


def env_default(name: str, default: str) -> str:
    """Return an environment value, treating unset or empty as missing."""
    value = os.environ.get(name)
    return default if value in (None, "") else value


def env_unset_only(name: str, default: str) -> str:
    """Return an environment value, treating only unset as missing."""
    return os.environ.get(name, default)


def run(args: list[str]) -> None:
    """Print and run a child command."""
    printable = [str(arg) for arg in args]
    print("+ " + shlex.join(printable), flush=True)
    run_logged(printable, cwd=REPO_ROOT)


def tournament_args(tournament: str) -> list[str]:
    return ["--tournament", tournament] if tournament else []


def run_bonus_stage(
    split: str,
    tournament: str,
    output_root: str,
    output_name: str,
    bonus_steps: str,
    lr: str,
    device: str,
    extra_args: list[str],
) -> None:
    """Fit one compositional bonus branch from the multidim player skills."""
    run(
        [
            PYTHON,
            "train_compositional.py",
            "--split",
            split,
            *tournament_args(tournament),
            "--player-skills",
            f"{output_root}/pyramidal/players.csv",
            "--steps",
            bonus_steps,
            "--lr",
            lr,
            "--device",
            device,
            "--output-dir",
            f"{output_root}/{output_name}",
            *extra_args,
        ]
    )


def evaluate_branch(output_root: str, model_name: str, output_name: str) -> None:
    """Evaluate one saved bonus branch against the shared pyramidal outputs."""
    run(
        [
            PYTHON,
            "evaluate_compirt.py",
            "--pyramidal-results",
            f"{output_root}/pyramidal",
            "--compositional-results",
            f"{output_root}/{model_name}",
            "--output-dir",
            f"{output_root}/{output_name}",
        ]
    )


def compare_bonus_branches(output_root: str) -> None:
    """Write no-synergy versus synergy bonus-metric comparison artifacts."""
    run(
        [
            PYTHON,
            "compare_compirt.py",
            "--compositional-metrics",
            f"{output_root}/evaluation/csvs/bonus_metrics.csv",
            "--synergy-metrics",
            f"{output_root}/synergy-evaluation/csvs/bonus_metrics.csv",
            "--output-dir",
            f"{output_root}/comparison",
        ]
    )


def main() -> None:
    gpu = env_default("GPU", "0")
    split = env_default("SPLIT", "year_2024")
    tournament = env_unset_only("TOURNAMENT", "")
    output_root = env_default("ROOT", "results/compirt/in_sample/multidim-all2024")
    pyramidal_steps = env_default("PYRAMIDAL_STEPS", "3000")
    bonus_steps = env_default("BONUS_STEPS", "2000")
    dimensions = env_default("DIMENSIONS", "5")
    synergy_dimensions = env_default("SYNERGY_DIMENSIONS", "3")
    lr = env_default("LR", "0.01")
    device = env_default("DEVICE", "cuda")
    predict_buzz_positions = env_default("PREDICT_BUZZ_POSITIONS", "1")
    save_synergy_details = env_default("SAVE_SYNERGY_DETAILS", "0")
    calibrate_correctness = env_default("CALIBRATE_CORRECTNESS", "0")
    calibrate_args = (
        ["--calibrate-correctness"] if calibrate_correctness == "1" else []
    )
    mplconfigdir = env_default("MPLCONFIGDIR", "/tmp/matplotlib-compirt")
    pytorch_cuda_alloc_conf = env_default(
        "PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True"
    )

    os.environ["CUDA_VISIBLE_DEVICES"] = gpu
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    os.environ["MPLCONFIGDIR"] = mplconfigdir
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = pytorch_cuda_alloc_conf

    if os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(Path(output_root) / "run.log")
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/run_multidim_compirt.py",
                "ROOT": output_root,
                "MODEL": "multidim",
                "SPLIT": split,
                "TOURNAMENT": tournament or "<all>",
                "DEVICE": device,
                "GPU": gpu,
                "DIMENSIONS": dimensions,
                "PYRAMIDAL_STEPS": pyramidal_steps,
                "BONUS_STEPS": bonus_steps,
                "LR": lr,
                "RUN_SYNERGY": "1",
                "SYNERGY_DIMENSIONS": synergy_dimensions,
                "SAVE_SYNERGY_DETAILS": save_synergy_details,
                "CALIBRATE_CORRECTNESS": calibrate_correctness,
                "PREDICT_BUZZ_POSITIONS": predict_buzz_positions,
                "MPLCONFIGDIR": mplconfigdir,
                "PYTORCH_CUDA_ALLOC_CONF": pytorch_cuda_alloc_conf,
                "PYTHON": PYTHON,
                "PYRAMIDAL_OUTPUT": f"{output_root}/pyramidal",
                "COMPOSITIONAL_OUTPUT": f"{output_root}/compositional",
                "SYNERGY_OUTPUT": f"{output_root}/synergy",
                "EVALUATION_OUTPUT": f"{output_root}/evaluation",
                "SYNERGY_EVALUATION_OUTPUT": f"{output_root}/synergy-evaluation",
                "COMPARISON_OUTPUT": f"{output_root}/comparison",
            }
        ),
        flush=True,
    )

    if device == "cuda":
        cuda_check = (
            "import torch; "
            "assert torch.cuda.is_available(), 'CUDA is unavailable'; "
            "print(torch.cuda.get_device_name(0))"
        )
        run([PYTHON, "-c", cuda_check])

    pyramidal_args = [
        PYTHON,
        "multidim_mirt/train_pyramidal.py",
        "--split",
        split,
        *tournament_args(tournament),
        "--dimensions",
        dimensions,
        "--steps",
        pyramidal_steps,
        "--lr",
        lr,
        "--device",
        device,
        "--output-dir",
        f"{output_root}/pyramidal",
    ]
    if predict_buzz_positions == "1":
        pyramidal_args.append("--predict-buzz-positions")
    pyramidal_args.extend(calibrate_args)
    run(pyramidal_args)

    run_bonus_stage(
        split,
        tournament,
        output_root,
        "compositional",
        bonus_steps,
        lr,
        device,
        calibrate_args,
    )

    synergy_args = ["--use-synergy", "--synergy-dimensions", synergy_dimensions]
    if save_synergy_details == "1":
        synergy_args.append("--save-synergy-details")
    synergy_args.extend(calibrate_args)
    run_bonus_stage(
        split,
        tournament,
        output_root,
        "synergy",
        bonus_steps,
        lr,
        device,
        synergy_args,
    )

    evaluate_branch(output_root, "compositional", "evaluation")
    evaluate_branch(output_root, "synergy", "synergy-evaluation")
    compare_bonus_branches(output_root)
    print(f"Finished. Inspect {output_root}/synergy-evaluation/experiment_report.md")


if __name__ == "__main__":
    main()
