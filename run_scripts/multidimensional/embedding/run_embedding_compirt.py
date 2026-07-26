#!/usr/bin/env python3
"""Run the embedding-relevance CompIRT pipeline (see 'multidimensional/embedding_mirt/README.md').

The environment-driven pipeline runs embedding -> pyramidal -> compositional ->
synergy -> evaluation -> comparison. It reuses cached '.npz' embeddings when
available and passes the fitted 'r_projection.npz' from the pyramidal stage to
the compositional and synergy stages.

Environment variables:

* 'SPLIT' / 'TOURNAMENT' select data; 'TOURNAMENT=""' means whole split.
* 'ROOT' chooses the output root.
* 'DIMENSIONS', 'PROJECTION_HIDDEN_DIM', 'PYRAMIDAL_STEPS', 'BONUS_STEPS',
  'LR', and 'DEVICE' control fitting.
* 'CALIBRATE_CORRECTNESS=1' enables correctness-only calibration in both
  stages.
* 'SYNERGY_DIMENSIONS' controls the always-on synergy branch.
* 'EMBED_DEVICE' controls the device for the one-time embed step (defaults
  to 'DEVICE'); 'FORCE_EMBED=1' re-embeds even if the cache exists.
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

EMBEDDING_MIRT_DIR = REPO_ROOT / "multidimensional" / "embedding_mirt"
TOSSUP_EMBEDDINGS = EMBEDDING_MIRT_DIR / "outputs" / "tossup_embeddings.npz"
BONUS_EMBEDDINGS = EMBEDDING_MIRT_DIR / "outputs" / "bonus_embeddings.npz"


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
    projection_path: str,
    bonus_steps: str,
    lr: str,
    seed: str,
    device: str,
    extra_args: list[str],
) -> None:
    """Fit one compositional bonus branch from the fixed theta and frozen projection."""
    run(
        [
            PYTHON,
            "-m",
            "multidimensional.embedding_mirt.train_compositional",
            "--split",
            split,
            *tournament_args(tournament),
            "--player-skills",
            f"{output_root}/pyramidal/players.csv",
            "--projection",
            projection_path,
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
    """Resolve settings and run embedding, fitting, evaluation, and comparison."""
    gpu = env_default("GPU", "0")
    split = env_default("SPLIT", "year_2024")
    tournament = env_unset_only("TOURNAMENT", "")
    output_root = resolve_result_root(
        env_default("ROOT", "results/compirt/in_sample/embedding/embedding-all2024"), "in_sample"
    )
    # Use the topic-family step and learning-rate defaults for projected 'r'.
    pyramidal_steps = env_default("PYRAMIDAL_STEPS", "5000")
    bonus_steps = env_default("BONUS_STEPS", "3000")
    dimensions = env_default("DIMENSIONS", "5")
    projection_hidden_dim = env_default("PROJECTION_HIDDEN_DIM", "128")
    synergy_dimensions = env_default("SYNERGY_DIMENSIONS", "3")
    lr = env_default("LR", "0.005")
    seed = env_default("SEED", "42")
    device = env_default("DEVICE", "cuda")
    embed_device = env_default("EMBED_DEVICE", device)
    force_embed = env_default("FORCE_EMBED", "0")
    save_synergy_details = env_default("SAVE_SYNERGY_DETAILS", "0")
    calibrate_correctness = env_default("CALIBRATE_CORRECTNESS", "0")
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
                "RUNNER": "run_scripts/multidimensional/embedding/run_embedding_compirt.py",
                "ROOT": output_root,
                "MODEL": "embedding",
                "SPLIT": split,
                "TOURNAMENT": tournament or "<all>",
                "DEVICE": device,
                "GPU": gpu,
                "DIMENSIONS": dimensions,
                "PROJECTION_HIDDEN_DIM": projection_hidden_dim,
                "PYRAMIDAL_STEPS": pyramidal_steps,
                "BONUS_STEPS": bonus_steps,
                "LR": lr,
                "SEED": seed,
                "RUN_SYNERGY": "1",
                "SYNERGY_DIMENSIONS": synergy_dimensions,
                "SAVE_SYNERGY_DETAILS": save_synergy_details,
                "CALIBRATE_CORRECTNESS": calibrate_correctness,
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
        # Fail before embedding or training if CUDA is unavailable.
        cuda_check = (
            "import torch; "
            "assert torch.cuda.is_available(), 'CUDA is unavailable'; "
            "print(torch.cuda.get_device_name(0))"
        )
        run([PYTHON, "-c", cuda_check])

    # Build the frozen question embeddings once, then reuse the cache.
    if force_embed == "1" or not TOSSUP_EMBEDDINGS.exists() or not BONUS_EMBEDDINGS.exists():
        run([PYTHON, "-m", "multidimensional.embedding_mirt.embed_questions", "--device", embed_device])
    else:
        print(f"Skipping embed step; cache found at {TOSSUP_EMBEDDINGS}", flush=True)

    # Stage 1 learns player skills and the embedding-to-relevance projection.
    pyramidal_args = [
        PYTHON,
        "-m",
        "multidimensional.embedding_mirt.train_pyramidal",
        "--split",
        split,
        *tournament_args(tournament),
        "--dimensions",
        dimensions,
        "--projection-hidden-dim",
        projection_hidden_dim,
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
    ]
    pyramidal_args.extend(calibrate_args)
    run(pyramidal_args)

    projection_path = f"{output_root}/pyramidal/r_projection.npz"

    # Both Stage-2 branches reuse the fitted skills and projection.
    run_bonus_stage(
        split=split,
        tournament=tournament,
        output_root=output_root,
        output_name="compositional",
        projection_path=projection_path,
        bonus_steps=bonus_steps,
        lr=lr,
        seed=seed,
        device=device,
        extra_args=calibrate_args,
    )

    synergy_args = ["--use-synergy", "--synergy-dimensions", synergy_dimensions]
    if save_synergy_details == "1":
        synergy_args.append("--save-synergy-details")
    synergy_args.extend(calibrate_args)
    run_bonus_stage(
        split=split,
        tournament=tournament,
        output_root=output_root,
        output_name="synergy",
        projection_path=projection_path,
        bonus_steps=bonus_steps,
        lr=lr,
        seed=seed,
        device=device,
        extra_args=synergy_args,
    )

    # Evaluate both branches and write their direct comparison.
    evaluate_branch(output_root, "compositional", "evaluation")
    evaluate_branch(output_root, "synergy", "synergy-evaluation")
    compare_bonus_branches(output_root)
    print(f"Finished. Inspect {output_root}/synergy-evaluation/experiment_report.md")


if __name__ == "__main__":
    main()
