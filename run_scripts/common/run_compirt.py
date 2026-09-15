#!/usr/bin/env python3
"""Configurable CUDA CompIRT experiment runner.

Environment variables:

* 'TOURNAMENT=""' includes every tournament in the selected split.
* 'ROOT' chooses the output root.
* 'RUN_SYNERGY=1' also fits and evaluates the synergy variant.
"""

from __future__ import annotations

import os
import shlex
import sys
from pathlib import Path

# Add the repository root to sys.path for direct script invocation.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from utils.run_logging import (
    env_default,
    env_unset_only,
    format_run_log_header,
    resolve_result_root,
    run_logged,
    tee_run_output,
    warn_env_knob_typos,
)

PYTHON = Path(os.environ.get("PYTHON", str(REPO_ROOT / ".venv" / "bin" / "python")))


def run(args: list[str]) -> None:
    """Print and run a child command."""
    print("+ " + shlex.join(args), flush=True)
    run_logged(args, cwd=REPO_ROOT)


def tournament_args(tournament: str) -> list[str]:
    return ["--tournament", tournament] if tournament else []


def run_compositional(
    *,
    split: str,
    tournament: str,
    output_root: str,
    bonus_steps: str,
    lr: str,
    seed: str,
    model_name: str,
    extra_args: list[str] | None = None,
) -> None:
    run(
        [
            str(PYTHON),
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
            "--seed",
            seed,
            "--device",
            "cuda",
            "--output-dir",
            f"{output_root}/{model_name}",
            *(extra_args or []),
        ]
    )


def evaluate(output_root: str, model_name: str, output_name: str) -> None:
    run(
        [
            str(PYTHON),
            "evaluate_compirt.py",
            "--pyramidal-results",
            f"{output_root}/pyramidal",
            "--compositional-results",
            f"{output_root}/{model_name}",
            "--output-dir",
            f"{output_root}/{output_name}",
        ]
    )


def main() -> None:
    """Resolve run settings and execute the complete baseline CompIRT pipeline."""
    # Configuration. Set TOURNAMENT="" to include every tournament in the split.
    gpu = env_default("GPU", "0")
    split = env_default("SPLIT", "year_2024")
    tournament = env_unset_only("TOURNAMENT", "2024-acf-regionals")
    output_root = resolve_result_root(
        env_default("ROOT", "results/compirt/in_sample/baseline/cuda-regionals-2024"),
        "in_sample",
    )
    pyramidal_steps = env_default("PYRAMIDAL_STEPS", "3000")
    bonus_steps = env_default("BONUS_STEPS", "2000")
    dimensions = env_default("DIMENSIONS", "3")
    synergy_dimensions = env_default("SYNERGY_DIMENSIONS", "3")
    lr = env_default("LR", "0.01")
    seed = env_default("SEED", "42")
    run_synergy = env_default("RUN_SYNERGY", "0")
    save_synergy_details = env_default("SAVE_SYNERGY_DETAILS", "0")
    calibrate_correctness = env_default("CALIBRATE_CORRECTNESS", "0")
    include_bounceback = env_default("INCLUDE_BOUNCEBACK", "0")
    calibrate_args = (
        ["--calibrate-correctness"] if calibrate_correctness == "1" else []
    )
    mplconfigdir = env_default("MPLCONFIGDIR", "/tmp/matplotlib-compirt")
    pytorch_cuda_alloc_conf = env_default(
        "PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True"
    )
    warn_env_knob_typos()

    os.environ["CUDA_VISIBLE_DEVICES"] = gpu
    os.environ["PYTHONUNBUFFERED"] = "1"
    os.environ["MPLCONFIGDIR"] = mplconfigdir
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = pytorch_cuda_alloc_conf

    # Capture the resolved configuration and all stage output in one run log.
    if os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(Path(output_root) / "run.log")
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/common/run_compirt.py",
                "ROOT": output_root,
                "MODEL": "baseline",
                "SPLIT": split,
                "TOURNAMENT": tournament or "<all>",
                "DEVICE": "cuda",
                "GPU": gpu,
                "DIMENSIONS": dimensions,
                "PYRAMIDAL_STEPS": pyramidal_steps,
                "BONUS_STEPS": bonus_steps,
                "LR": lr,
                "SEED": seed,
                "RUN_SYNERGY": run_synergy,
                "SYNERGY_DIMENSIONS": synergy_dimensions,
                "SAVE_SYNERGY_DETAILS": save_synergy_details,
                "CALIBRATE_CORRECTNESS": calibrate_correctness,
                "INCLUDE_BOUNCEBACK": include_bounceback,
                "MPLCONFIGDIR": mplconfigdir,
                "PYTORCH_CUDA_ALLOC_CONF": pytorch_cuda_alloc_conf,
                "PYTHON": PYTHON,
                "PYRAMIDAL_OUTPUT": f"{output_root}/pyramidal",
                "COMPOSITIONAL_OUTPUT": f"{output_root}/compositional",
                "SYNERGY_OUTPUT": f"{output_root}/synergy"
                if run_synergy == "1"
                else "",
                "EVALUATION_OUTPUT": f"{output_root}/evaluation",
                "SYNERGY_EVALUATION_OUTPUT": f"{output_root}/synergy-evaluation"
                if run_synergy == "1"
                else "",
                "COMPARISON_OUTPUT": f"{output_root}/comparison"
                if run_synergy == "1"
                else "",
            }
        ),
        flush=True,
    )

    # Fail before training if the requested CUDA runtime is unavailable.
    cuda_check = (
        "import torch; "
        "assert torch.cuda.is_available(), 'CUDA is unavailable'; "
        "print(torch.cuda.get_device_name(0))"
    )
    run([str(PYTHON), "-c", cuda_check])

    # Stage 1 fits player skills and tossup timing/correctness parameters.
    pyramidal_args = [
        str(PYTHON),
        "train_pyramidal.py",
        "--split",
        split,
        *tournament_args(tournament),
        "--dimensions",
        dimensions,
        "--steps",
        pyramidal_steps,
        "--lr",
        lr,
        "--seed",
        seed,
        "--device",
        "cuda",
        "--output-dir",
        f"{output_root}/pyramidal",
    ]
    pyramidal_args.extend(calibrate_args)
    if include_bounceback == "1":
        pyramidal_args.append("--include-bounceback")
    run(pyramidal_args)

    # Stage 2 fits the standard bonus model from the frozen Stage-1 skills.
    run_compositional(
        split=split,
        tournament=tournament,
        output_root=output_root,
        bonus_steps=bonus_steps,
        lr=lr,
        seed=seed,
        model_name="compositional",
        extra_args=list(calibrate_args),
    )

    if run_synergy == "1":
        # The optional branch refits Stage 2 with player-pair synergy profiles.
        synergy_args = ["--use-synergy", "--synergy-dimensions", synergy_dimensions]
        if save_synergy_details == "1":
            synergy_args.append("--save-synergy-details")
        synergy_args.extend(calibrate_args)
        run_compositional(
            split=split,
            tournament=tournament,
            output_root=output_root,
            bonus_steps=bonus_steps,
            lr=lr,
            seed=seed,
            model_name="synergy",
            extra_args=synergy_args,
        )

    # Evaluate each fitted bonus branch, then compare them when both exist.
    evaluate(output_root, "compositional", "evaluation")

    if run_synergy == "1":
        evaluate(output_root, "synergy", "synergy-evaluation")
        run(
            [
                str(PYTHON),
                "run_scripts/common/run_synergy_comparison.py",
                "--compositional-metrics",
                f"{output_root}/evaluation/csvs/bonus_metrics.csv",
                "--synergy-metrics",
                f"{output_root}/synergy-evaluation/csvs/bonus_metrics.csv",
                "--output-dir",
                f"{output_root}/comparison",
            ]
        )

    print(f"Finished. Inspect {output_root}/evaluation/experiment_report.md")
    if run_synergy == "1":
        print(f"Compare it with {output_root}/synergy-evaluation/experiment_report.md")
        print(f"Direct comparison: {output_root}/comparison/bonus_model_comparison.md")


if __name__ == "__main__":
    main()
