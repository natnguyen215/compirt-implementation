#!/usr/bin/env python3
"""Run the embedding-relevance CompIRT pipeline (see 'multidimensional/embedding_mirt/README.md').

Mirrors 'run_scripts/run_multidim_compirt.py' -- same env-var driven
pyramidal -> compositional -> synergy -> evaluate -> compare flow -- with two
differences specific to this variant: a one-time embed step before pyramidal
(skipped if the cached '.npz' files already exist), and the compositional /
synergy stages take an extra '--projection' pointing at the fitted
'r_projection.npz' from this run's own pyramidal stage (frozen, not retrained).

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

# This script lives in run_scripts/, so the repo root is one directory up. Add it
# to sys.path before importing repo packages so the script works when invoked
# directly (python run_scripts/run_embedding_compirt.py), not only as a module.
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from utils.run_logging import (
    format_run_log_header,
    resolve_result_root,
    run_logged,
    tee_run_output,
)

PYTHON = Path(
    os.environ.get("PYTHON", str(REPO_ROOT / ".venv" / "bin" / "python"))
)

EMBEDDING_MIRT_DIR = REPO_ROOT / "multidimensional" / "embedding_mirt"
TOSSUP_EMBEDDINGS = EMBEDDING_MIRT_DIR / "outputs" / "tossup_embeddings.npz"
BONUS_EMBEDDINGS = EMBEDDING_MIRT_DIR / "outputs" / "bonus_embeddings.npz"


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
    projection_path: str,
    bonus_steps: str,
    lr: str,
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
    output_root = resolve_result_root(
        env_default("ROOT", "results/compirt/in_sample/embedding-all2024"), "in_sample"
    )
    # Steps/LR match the repo's topic-family convention (embedding_mirt is the
    # neural-embedding sibling of topic/fixed's frozen-vector 'r'), not
    # multidim_mirt's freely-learned-alpha convention.
    pyramidal_steps = env_default("PYRAMIDAL_STEPS", "5000")
    bonus_steps = env_default("BONUS_STEPS", "3000")
    dimensions = env_default("DIMENSIONS", "5")
    projection_hidden_dim = env_default("PROJECTION_HIDDEN_DIM", "128")
    synergy_dimensions = env_default("SYNERGY_DIMENSIONS", "3")
    lr = env_default("LR", "0.005")
    device = env_default("DEVICE", "cuda")
    embed_device = env_default("EMBED_DEVICE", device)
    force_embed = env_default("FORCE_EMBED", "0")
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
                "RUNNER": "run_scripts/run_embedding_compirt.py",
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

    if force_embed == "1" or not TOSSUP_EMBEDDINGS.exists() or not BONUS_EMBEDDINGS.exists():
        run([PYTHON, "-m", "multidimensional.embedding_mirt.embed_questions", "--device", embed_device])
    else:
        print(f"Skipping embed step; cache found at {TOSSUP_EMBEDDINGS}", flush=True)

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
        "--device",
        device,
        "--output-dir",
        f"{output_root}/pyramidal",
    ]
    if predict_buzz_positions == "1":
        pyramidal_args.append("--predict-buzz-positions")
    pyramidal_args.extend(calibrate_args)
    run(pyramidal_args)

    projection_path = f"{output_root}/pyramidal/r_projection.npz"

    run_bonus_stage(
        split,
        tournament,
        output_root,
        "compositional",
        projection_path,
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
        projection_path,
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
