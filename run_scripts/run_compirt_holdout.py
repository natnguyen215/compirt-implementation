#!/usr/bin/env python3
"""Held-out temporal CompIRT runner: train on one split, evaluate the next.

This implements the paper's primary temporal split (Section 4.2): player skills
are learned on 'TRAIN_SPLIT' (e.g. 2024) and Scenario A/B are evaluated on the
held-out 'TEST_SPLIT' (e.g. 2025). Question parameters are co-estimated
transductively on the test split; returning players keep their training posterior
as a prior and new players draw a tier-conditioned prior ('NEW_PLAYER_PRIOR=flat'
selects the N(0, I) ablation).

Per variant the flow is:
1. Stage-1 train on TRAIN_SPLIT  -> 'train/pyramidal' (+ 'player_posterior.csv')
2. Stage-1 held-out pass on TEST_SPLIT with those priors -> 'holdout/pyramidal'
3. Stage-2 on TEST_SPLIT using the held-out player skills -> 'holdout/<bonus>'
4. evaluate Scenario A/B on the held-out predictions -> 'holdout/evaluation'

Environment variables:

* 'MODEL'           baseline | multidim | topic | learned  (default baseline)
* 'TRAIN_SPLIT' / 'TEST_SPLIT'                    (default year_2024 / year_2025)
* 'NEW_PLAYER_PRIOR' tier | flat                    (default tier)
* 'ROOT'            output root                      (default results/compirt/holdout/<MODEL>)
* 'TOURNAMENT'      restrict to a tournament prefix; "" = whole split
* 'PYRAMIDAL_STEPS' / 'BONUS_STEPS' / 'DIMENSIONS' / 'LR' / 'DEVICE'
* 'RUN_SYNERGY' defaults to 1 for 'MODEL=multidim' and 0 otherwise
* 'SYNERGY_DIMENSIONS' / 'SAVE_SYNERGY_DETAILS' configure the synergy branch
* 'PREDICT_BUZZ_POSITIONS' 1 writes expected first-buzz position diagnostics
* 'CALIBRATE_CORRECTNESS' 1 enables the same Platt scale+bias calibration as
  the full-data runners
* 'TOPIC_VECTORS'   topic variant document-vector CSV (optional override)
* 'DATABASE'        learned variant question-text DB (optional override)
"""

from __future__ import annotations

import os
import shlex
import sys
from pathlib import Path

# This script lives in run_scripts/, so the repo root is one directory up. Add it
# to sys.path before importing repo packages so the script works when invoked
# directly (python run_scripts/run_compirt_holdout.py), not only as a module.
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


def env_default(name: str, default: str) -> str:
    value = os.environ.get(name)
    return default if value in (None, "") else value


def env_unset_only(name: str, default: str) -> str:
    return os.environ.get(name, default)


def run(args: list[str]) -> None:
    printable = [str(a) for a in args]
    print("+ " + shlex.join(printable), flush=True)
    run_logged(printable, cwd=REPO_ROOT)


def tournament_args(tournament: str) -> list[str]:
    return ["--tournament", tournament] if tournament else []


def run_bonus_stage(
    scripts: dict[str, str],
    split: str,
    tournament: str,
    player_skills: str,
    output_dir: str,
    steps: str,
    lr: str,
    device: str,
    extra_args: list[str],
) -> None:
    """Fit one held-out bonus branch from a saved pyramidal player table."""
    run([
        PYTHON, "-m", scripts["compositional"],
        "--split", split, *tournament_args(tournament),
        "--player-skills", player_skills,
        "--steps", steps, "--lr", lr, "--device", device,
        "--output-dir", output_dir, *extra_args,
    ])


# Per-variant module names (run as 'python -m' from the repo root) and the
# extra args each stage needs. '{train_pyr}' is filled with the training
# pyramidal output dir (it holds the frozen topics the learned variant reuses).
MODELS = {
    "baseline": {
        "pyramidal": "train_pyramidal",
        "compositional": "train_compositional",
        "evaluate": "evaluate_compirt",
    },
    "multidim": {
        "pyramidal": "multidimensional.multidim_mirt.train_pyramidal",
        "compositional": "train_compositional",
        "evaluate": "evaluate_compirt",
    },
    "topic": {
        "pyramidal": "topic.fixed.train_topic_pyramidal",
        "compositional": "topic.fixed.train_topic_compositional",
        "evaluate": "topic.fixed.evaluate_topic_compirt",
    },
    "learned": {
        "pyramidal": "topic.learned.train_joint_pyramidal",
        "compositional": "topic.learned.train_joint_compositional",
        "evaluate": "evaluate_compirt",
    },
}


def main() -> None:
    model = env_default("MODEL", "baseline")
    if model not in MODELS:
        raise SystemExit(f"MODEL must be one of {sorted(MODELS)}, got {model!r}")
    scripts = MODELS[model]

    train_split = env_default("TRAIN_SPLIT", "year_2024")
    test_split = env_default("TEST_SPLIT", "year_2025")
    new_player_prior = env_default("NEW_PLAYER_PRIOR", "tier")
    tournament = env_unset_only("TOURNAMENT", "")
    root = resolve_result_root(
        env_default("ROOT", f"results/compirt/holdout/{model}"), "holdout"
    )
    pyramidal_steps = env_default("PYRAMIDAL_STEPS", "3000")
    bonus_steps = env_default("BONUS_STEPS", "2000")
    dimensions = env_default("DIMENSIONS", "5")
    lr = env_default("LR", "0.01")
    device = env_default("DEVICE", "cpu")
    calibrate_correctness = env_default("CALIBRATE_CORRECTNESS", "0")
    run_synergy = env_default("RUN_SYNERGY", "1" if model == "multidim" else "0")
    synergy_dimensions = env_default("SYNERGY_DIMENSIONS", "3")
    save_synergy_details = env_default("SAVE_SYNERGY_DETAILS", "0")
    predict_buzz_positions = env_default("PREDICT_BUZZ_POSITIONS", "1")
    if run_synergy == "1" and scripts["compositional"] != "train_compositional":
        raise SystemExit("RUN_SYNERGY=1 is only wired for the root compositional stage")

    topic_vectors = os.environ.get("TOPIC_VECTORS")
    database = os.environ.get("DATABASE")
    mplconfigdir = env_default("MPLCONFIGDIR", "/tmp/matplotlib-compirt")

    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    os.environ["MPLCONFIGDIR"] = mplconfigdir

    train_pyr = f"{root}/train/pyramidal"
    holdout_pyr = f"{root}/holdout/pyramidal"
    holdout_bonus = f"{root}/holdout/compositional"
    holdout_synergy = f"{root}/holdout/synergy"
    holdout_eval = f"{root}/holdout/evaluation"
    holdout_synergy_eval = f"{root}/holdout/synergy-evaluation"

    if os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(Path(root) / "run.log")
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/run_compirt_holdout.py",
                "ROOT": root,
                "MODEL": model,
                "TRAIN_SPLIT": train_split,
                "TEST_SPLIT": test_split,
                "NEW_PLAYER_PRIOR": new_player_prior,
                "TOURNAMENT": tournament or "<all>",
                "DEVICE": device,
                "GPU": os.environ.get("GPU", "unknown"),
                "DIMENSIONS": dimensions,
                "PYRAMIDAL_STEPS": pyramidal_steps,
                "BONUS_STEPS": bonus_steps,
                "LR": lr,
                "RUN_SYNERGY": run_synergy,
                "SYNERGY_DIMENSIONS": synergy_dimensions,
                "SAVE_SYNERGY_DETAILS": save_synergy_details,
                "CALIBRATE_CORRECTNESS": calibrate_correctness,
                "PREDICT_BUZZ_POSITIONS": predict_buzz_positions,
                "TOPIC_VECTORS": topic_vectors or "",
                "DATABASE": database or "",
                "MPLCONFIGDIR": mplconfigdir,
                "PYTHON": PYTHON,
                "TRAIN_PYRAMIDAL_OUTPUT": train_pyr,
                "HOLDOUT_PYRAMIDAL_OUTPUT": holdout_pyr,
                "HOLDOUT_COMPOSITIONAL_OUTPUT": holdout_bonus,
                "HOLDOUT_SYNERGY_OUTPUT": holdout_synergy
                if run_synergy == "1"
                else "",
                "HOLDOUT_EVALUATION_OUTPUT": holdout_eval,
                "HOLDOUT_SYNERGY_EVALUATION_OUTPUT": holdout_synergy_eval
                if run_synergy == "1"
                else "",
                "HOLDOUT_COMPARISON_OUTPUT": f"{root}/holdout/comparison"
                if run_synergy == "1"
                else "",
            }
        ),
        flush=True,
    )

    # Variant-specific extra args.
    #
    # baseline/multidim: --dimensions is the skill dimensionality.
    # topic:    skill dimensionality is fixed by the topic-vector column count, so
    #           --dimensions is NOT passed; only the (optional) vector file is.
    # learned:  --dimensions is the topic/skill count and must match the frozen
    #           topic-word matrix, so it is passed to every stage.
    pyr_extra: list[str] = []
    comp_extra: list[str] = []
    if model in ("baseline", "multidim"):
        pyr_extra += ["--dimensions", dimensions]
    elif model == "topic":
        if topic_vectors:
            pyr_extra += ["--topic-vectors", topic_vectors]
            comp_extra += ["--topic-vectors", topic_vectors]
    elif model == "learned":
        pyr_extra += ["--dimensions", dimensions]
        if database:
            pyr_extra += ["--database", database]
            comp_extra += ["--database", database]
        # Bonus stage reuses the frozen topics from the TRAINING pyramidal run.
        comp_extra += ["--topic-model-dir", train_pyr]
    if calibrate_correctness == "1":
        pyr_extra += ["--calibrate-correctness"]
        comp_extra += ["--calibrate-correctness"]
    if predict_buzz_positions == "1":
        pyr_extra += ["--predict-buzz-positions"]

    # 1. Stage-1 training on the historical split.
    run([
        PYTHON, "-m", scripts["pyramidal"],
        "--split", train_split, *tournament_args(tournament),
        "--steps", pyramidal_steps, "--lr", lr, "--device", device,
        "--output-dir", train_pyr, *pyr_extra,
    ])

    # 2. Stage-1 held-out transductive pass on the test split with informative
    #    player priors built from the training posterior.
    heldout_pyr_extra = list(pyr_extra)
    if model == "learned":
        heldout_pyr_extra += ["--train-topic-model", train_pyr]
    run([
        PYTHON, "-m", scripts["pyramidal"],
        "--split", test_split, *tournament_args(tournament),
        "--steps", pyramidal_steps, "--lr", lr, "--device", device,
        "--train-posterior", f"{train_pyr}/player_posterior.csv",
        "--new-player-prior", new_player_prior,
        "--output-dir", holdout_pyr, *heldout_pyr_extra,
    ])

    # 3. Stage-2 bonus model on the test split using the held-out player skills.
    run_bonus_stage(
        scripts,
        test_split,
        tournament,
        f"{holdout_pyr}/players.csv",
        holdout_bonus,
        bonus_steps,
        lr,
        device,
        comp_extra,
    )

    if run_synergy == "1":
        synergy_extra = [
            "--use-synergy",
            "--synergy-dimensions",
            synergy_dimensions,
        ]
        if save_synergy_details == "1":
            synergy_extra.append("--save-synergy-details")
        synergy_extra.extend(comp_extra)
        run_bonus_stage(
            scripts,
            test_split,
            tournament,
            f"{holdout_pyr}/players.csv",
            holdout_synergy,
            bonus_steps,
            lr,
            device,
            synergy_extra,
        )

    # 4. Scenario A/B evaluation on the held-out predictions.
    run([
        PYTHON, "-m", scripts["evaluate"],
        "--pyramidal-results", holdout_pyr,
        "--compositional-results", holdout_bonus,
        "--output-dir", holdout_eval,
    ])

    if run_synergy == "1":
        run([
            PYTHON, "-m", scripts["evaluate"],
            "--pyramidal-results", holdout_pyr,
            "--compositional-results", holdout_synergy,
            "--output-dir", holdout_synergy_eval,
        ])
        run([
            PYTHON, "-m", "compare_compirt",
            "--compositional-metrics",
            f"{holdout_eval}/csvs/bonus_metrics.csv",
            "--synergy-metrics",
            f"{holdout_synergy_eval}/csvs/bonus_metrics.csv",
            "--output-dir",
            f"{root}/holdout/comparison",
        ])

    print(f"Finished held-out {model} run. Scenario A/B metrics in {holdout_eval}.")
    if run_synergy == "1":
        print(f"Synergy metrics in {holdout_synergy_eval}.")


if __name__ == "__main__":
    main()
