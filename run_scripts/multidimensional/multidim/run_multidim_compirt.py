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

# Add the repository root to sys.path for direct script invocation.
REPO_ROOT = Path(__file__).resolve().parents[3]
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

PYTHON = Path(
    os.environ.get("PYTHON", str(REPO_ROOT / ".venv" / "bin" / "python"))
)


def run(args: list[str]) -> None:
    """Print and run a child command."""
    printable = [str(arg) for arg in args]
    print("+ " + shlex.join(printable), flush=True)
    run_logged(printable, cwd=REPO_ROOT)


def tournament_args(tournament: str) -> list[str]:
    return ["--tournament", tournament] if tournament else []


def run_bonus_stage(
    *,
    split: str,
    tournament: str,
    output_root: str,
    output_name: str,
    bonus_steps: str,
    lr: str,
    seed: str,
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
            "--seed",
            seed,
            "--device",
            device,
            "--output-dir",
            f"{output_root}/{output_name}",
            *extra_args,
        ]
    )


def evaluate_branch(
    *,
    output_root: str,
    model_name: str,
    output_name: str,
    split: str,
    tournament: str,
    game_simulations: str,
) -> None:
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
            "--split",
            split,
            *tournament_args(tournament),
            "--game-simulations",
            game_simulations,
        ]
    )


def compare_bonus_branches(output_root: str) -> None:
    """Write no-synergy versus synergy bonus-metric comparison artifacts."""
    run(
        [
            PYTHON,
            "run_scripts/common/run_synergy_comparison.py",
            "--compositional-metrics",
            f"{output_root}/evaluation/csvs/bonus_metrics.csv",
            "--synergy-metrics",
            f"{output_root}/synergy-evaluation/csvs/bonus_metrics.csv",
            "--output-dir",
            f"{output_root}/comparison",
        ]
    )


def main() -> None:
    """Resolve settings and run multidimensional fitting and diagnostics."""
    gpu = env_default("GPU", "0")
    split = env_default("SPLIT", "year_2024")
    tournament = env_unset_only("TOURNAMENT", "")
    output_root = resolve_result_root(
        env_default("ROOT", "results/compirt/in_sample/multidim/multidim-all2024"), "in_sample"
    )
    pyramidal_steps = env_default("PYRAMIDAL_STEPS", "3000")
    bonus_steps = env_default("BONUS_STEPS", "2000")
    dimensions = env_default("DIMENSIONS", "5")
    difficulty_link = env_default("DIFFICULTY_LINK", "sigmoid")
    synergy_dimensions = env_default("SYNERGY_DIMENSIONS", "3")
    lr = env_default("LR", "0.01")
    seed = env_default("SEED", "42")
    device = env_default("DEVICE", "cuda")
    save_synergy_details = env_default("SAVE_SYNERGY_DETAILS", "0")
    calibrate_correctness = env_default("CALIBRATE_CORRECTNESS", "0")
    include_bounceback = env_default("INCLUDE_BOUNCEBACK", "0")
    ppc_draws = env_default("PPC_DRAWS", "20")
    ppc_max_events = env_default("PPC_MAX_EVENTS", "500")
    game_simulations = env_default("GAME_SIMULATIONS", "500")
    run_recovery = env_default("RUN_PARAMETER_RECOVERY", "1")
    recovery_steps = env_default("RECOVERY_STEPS", "800")
    calibrate_args = (
        ["--calibrate-correctness"] if calibrate_correctness == "1" else []
    )
    mplconfigdir = env_default("MPLCONFIGDIR", "/tmp/matplotlib-compirt")
    pytorch_cuda_alloc_conf = env_default(
        "PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True"
    )
    warn_env_knob_typos()

    os.environ["CUDA_VISIBLE_DEVICES"] = gpu
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    os.environ["MPLCONFIGDIR"] = mplconfigdir
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = pytorch_cuda_alloc_conf

    # Capture the resolved configuration and all stage output in one run log.
    if os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(Path(output_root) / "run.log")
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/multidimensional/multidim/run_multidim_compirt.py",
                "ROOT": output_root,
                "MODEL": "multidim",
                "SPLIT": split,
                "TOURNAMENT": tournament or "<all>",
                "DEVICE": device,
                "GPU": gpu,
                "DIMENSIONS": dimensions,
                "DIFFICULTY_LINK": difficulty_link,
                "PYRAMIDAL_STEPS": pyramidal_steps,
                "BONUS_STEPS": bonus_steps,
                "LR": lr,
                "SEED": seed,
                "RUN_SYNERGY": "1",
                "SYNERGY_DIMENSIONS": synergy_dimensions,
                "SAVE_SYNERGY_DETAILS": save_synergy_details,
                "CALIBRATE_CORRECTNESS": calibrate_correctness,
                "INCLUDE_BOUNCEBACK": include_bounceback,
                "PPC_DRAWS": ppc_draws,
                "PPC_MAX_EVENTS": ppc_max_events,
                "GAME_SIMULATIONS": game_simulations,
                "RUN_PARAMETER_RECOVERY": run_recovery,
                "RECOVERY_STEPS": recovery_steps,
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
        # Fail before training if the requested CUDA runtime is unavailable.
        cuda_check = (
            "import torch; "
            "assert torch.cuda.is_available(), 'CUDA is unavailable'; "
            "print(torch.cuda.get_device_name(0))"
        )
        run([PYTHON, "-c", cuda_check])

    # Stage 1 fits vector-valued player skills and tossup difficulty curves.
    pyramidal_args = [
        PYTHON,
        "multidimensional/multidim_mirt/train_pyramidal.py",
        "--split",
        split,
        *tournament_args(tournament),
        "--dimensions",
        dimensions,
        "--difficulty-link",
        difficulty_link,
        "--steps",
        pyramidal_steps,
        "--lr",
        lr,
        "--seed",
        seed,
        "--device",
        device,
        "--output-dir",
        f"{output_root}/pyramidal",
        "--ppc-draws",
        ppc_draws,
        "--ppc-max-events",
        ppc_max_events,
    ]
    pyramidal_args.extend(calibrate_args)
    if include_bounceback == "1":
        pyramidal_args.append("--include-bounceback")
    run(pyramidal_args)

    # Both Stage-2 branches consume the same frozen Stage-1 player skills.
    run_bonus_stage(
        split=split,
        tournament=tournament,
        output_root=output_root,
        output_name="compositional",
        bonus_steps=bonus_steps,
        lr=lr,
        seed=seed,
        device=device,
        extra_args=[
            *calibrate_args,
            "--ppc-draws",
            ppc_draws,
            "--ppc-max-responses",
            ppc_max_events,
        ],
    )

    synergy_args = ["--use-synergy", "--synergy-dimensions", synergy_dimensions]
    if save_synergy_details == "1":
        synergy_args.append("--save-synergy-details")
    synergy_args.extend(calibrate_args)
    synergy_args.extend(
        ["--ppc-draws", ppc_draws, "--ppc-max-responses", ppc_max_events]
    )
    run_bonus_stage(
        split=split,
        tournament=tournament,
        output_root=output_root,
        output_name="synergy",
        bonus_steps=bonus_steps,
        lr=lr,
        seed=seed,
        device=device,
        extra_args=synergy_args,
    )

    # Evaluate both branches, run the bounded recovery diagnostic, and compare.
    evaluate_branch(
        output_root=output_root,
        model_name="compositional",
        output_name="evaluation",
        split=split,
        tournament=tournament,
        game_simulations=game_simulations,
    )
    evaluate_branch(
        output_root=output_root,
        model_name="synergy",
        output_name="synergy-evaluation",
        split=split,
        tournament=tournament,
        game_simulations=game_simulations,
    )
    if run_recovery == "1":
        run(
            [
                PYTHON,
                "run_scripts/multidimensional/multidim/run_parameter_recovery.py",
                "--output-dir",
                f"{output_root}/compirt_eval/parameter-recovery",
                "--steps",
                recovery_steps,
                "--seed",
                seed,
            ]
        )
    compare_bonus_branches(output_root)
    print(f"Finished. Inspect {output_root}/synergy-evaluation/experiment_report.md")


if __name__ == "__main__":
    main()
