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

* 'MODEL'           baseline | multidim                (default baseline)
* 'TRAIN_SPLIT' / 'TEST_SPLIT'                    (default year_2024 / year_2025)
* 'NEW_PLAYER_PRIOR' tier | flat                    (default tier)
* 'ROOT'            output root                      (default results/compirt/holdout/<MODEL>)
* 'TOURNAMENT'      restrict to a tournament prefix; "" = whole split
* 'PYRAMIDAL_STEPS' / 'BONUS_STEPS' / 'DIMENSIONS' / 'LR' / 'DEVICE'
* 'RUN_SYNERGY' defaults to 1 for 'MODEL=multidim' and 0 otherwise
* 'SYNERGY_DIMENSIONS' / 'SAVE_SYNERGY_DETAILS' configure the synergy branch
* 'CALIBRATE_CORRECTNESS' 1 enables the same Platt scale+bias calibration as
  the full-data runners
"""

from __future__ import annotations

import os
import shlex
import sys
from dataclasses import dataclass
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

PYTHON = Path(
    os.environ.get("PYTHON", str(REPO_ROOT / ".venv" / "bin" / "python"))
)


def run(args: list[str]) -> None:
    printable = [str(a) for a in args]
    print("+ " + shlex.join(printable), flush=True)
    run_logged(printable, cwd=REPO_ROOT)


def tournament_args(tournament: str) -> list[str]:
    return ["--tournament", tournament] if tournament else []


def bonus_stage_command(
    scripts: dict[str, str],
    *,
    split: str,
    tournament: str,
    player_skills: str,
    output_dir: str,
    steps: str,
    lr: str,
    seed: str,
    device: str,
    extra_args: list[str],
) -> list[str]:
    """Build one Stage-2 command without executing it."""
    return [
        PYTHON, "-m", scripts["compositional"],
        "--split", split, *tournament_args(tournament),
        "--player-skills", player_skills,
        "--steps", steps, "--lr", lr, "--seed", seed, "--device", device,
        "--output-dir", output_dir, *extra_args,
    ]


# Per-variant module names (run as 'python -m' from the repo root).
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
}


@dataclass(frozen=True)
class HoldoutConfig:
    """Resolved environment contract for one temporal-holdout run."""

    model: str
    frozen_predict: str
    train_split: str
    test_split: str
    new_player_prior: str
    tournament: str
    root: str
    pyramidal_steps: str
    bonus_steps: str
    dimensions: str
    difficulty_link: str
    lr: str
    seed: str
    device: str
    calibrate_correctness: str
    run_synergy: str
    synergy_dimensions: str
    save_synergy_details: str
    mplconfigdir: str


def resolve_config() -> HoldoutConfig:
    """Resolve and validate all environment-controlled runner settings."""
    model = env_default("MODEL", "baseline")
    if model not in MODELS:
        raise SystemExit(f"MODEL must be one of {sorted(MODELS)}, got {model!r}")

    difficulty_link = env_default("DIFFICULTY_LINK", "sigmoid")
    if difficulty_link != "sigmoid" and model != "multidim":
        raise SystemExit(
            f"DIFFICULTY_LINK={difficulty_link!r} is only supported for "
            f"MODEL=multidim; got MODEL={model!r}"
        )

    frozen_predict = env_default("FROZEN_PREDICT", "0")
    if frozen_predict == "1" and model != "multidim":
        raise SystemExit(
            "FROZEN_PREDICT=1 (frozen matrix-infill scoring) currently supports "
            f"MODEL=multidim only; got MODEL={model!r}"
        )

    return HoldoutConfig(
        model=model,
        frozen_predict=frozen_predict,
        train_split=env_default("TRAIN_SPLIT", "year_2024"),
        test_split=env_default("TEST_SPLIT", "year_2025"),
        new_player_prior=env_default("NEW_PLAYER_PRIOR", "tier"),
        tournament=env_unset_only("TOURNAMENT", ""),
        root=resolve_result_root(
            env_default("ROOT", f"results/compirt/holdout/{model}"), "holdout"
        ),
        pyramidal_steps=env_default("PYRAMIDAL_STEPS", "3000"),
        bonus_steps=env_default("BONUS_STEPS", "2000"),
        dimensions=env_default("DIMENSIONS", "5"),
        difficulty_link=difficulty_link,
        lr=env_default("LR", "0.01"),
        seed=env_default("SEED", "42"),
        device=env_default("DEVICE", "cpu"),
        calibrate_correctness=env_default("CALIBRATE_CORRECTNESS", "0"),
        run_synergy=env_default("RUN_SYNERGY", "1" if model == "multidim" else "0"),
        synergy_dimensions=env_default("SYNERGY_DIMENSIONS", "3"),
        save_synergy_details=env_default("SAVE_SYNERGY_DETAILS", "0"),
        mplconfigdir=env_default("MPLCONFIGDIR", "/tmp/matplotlib-compirt"),
    )


def model_stage_args(config: HoldoutConfig, train_pyramidal: str):
    """Return family-specific Stage-1 and Stage-2 CLI arguments."""
    pyramidal: list[str] = ["--dimensions", config.dimensions]
    compositional: list[str] = []
    if config.model == "multidim":
        pyramidal += ["--difficulty-link", config.difficulty_link]
    if config.calibrate_correctness == "1":
        pyramidal.append("--calibrate-correctness")
        compositional.append("--calibrate-correctness")
    return pyramidal, compositional


@dataclass(frozen=True)
class HoldoutPaths:
    """Stable output layout shared by every holdout model family."""

    train_pyramidal: str
    train_bonus: str
    train_synergy: str
    holdout_pyramidal: str
    holdout_bonus: str
    holdout_synergy: str
    holdout_evaluation: str
    holdout_synergy_evaluation: str
    comparison: str


def output_paths(root: str) -> HoldoutPaths:
    """Resolve the established train/holdout result-directory contract."""
    return HoldoutPaths(
        train_pyramidal=f"{root}/train/pyramidal",
        train_bonus=f"{root}/train/compositional",
        train_synergy=f"{root}/train/synergy",
        holdout_pyramidal=f"{root}/holdout/pyramidal",
        holdout_bonus=f"{root}/holdout/compositional",
        holdout_synergy=f"{root}/holdout/synergy",
        holdout_evaluation=f"{root}/holdout/evaluation",
        holdout_synergy_evaluation=f"{root}/holdout/synergy-evaluation",
        comparison=f"{root}/holdout/comparison",
    )


def run_log_fields(config: HoldoutConfig, paths: HoldoutPaths):
    """Return the public run metadata in its established field order."""
    return {
        "RUNNER": "run_scripts/common/run_compirt_holdout.py",
        "ROOT": config.root,
        "MODEL": config.model,
        "FROZEN_PREDICT": config.frozen_predict,
        "TRAIN_SPLIT": config.train_split,
        "TEST_SPLIT": config.test_split,
        "NEW_PLAYER_PRIOR": config.new_player_prior,
        "TOURNAMENT": config.tournament or "<all>",
        "DEVICE": config.device,
        "GPU": os.environ.get("GPU", "unknown"),
        "DIMENSIONS": config.dimensions,
        "DIFFICULTY_LINK": config.difficulty_link
        if config.model == "multidim"
        else "",
        "PYRAMIDAL_STEPS": config.pyramidal_steps,
        "BONUS_STEPS": config.bonus_steps,
        "LR": config.lr,
        "SEED": config.seed,
        "RUN_SYNERGY": config.run_synergy,
        "SYNERGY_DIMENSIONS": config.synergy_dimensions,
        "SAVE_SYNERGY_DETAILS": config.save_synergy_details,
        "CALIBRATE_CORRECTNESS": config.calibrate_correctness,
        "MPLCONFIGDIR": config.mplconfigdir,
        "PYTHON": PYTHON,
        "TRAIN_PYRAMIDAL_OUTPUT": paths.train_pyramidal,
        "HOLDOUT_PYRAMIDAL_OUTPUT": paths.holdout_pyramidal,
        "HOLDOUT_COMPOSITIONAL_OUTPUT": paths.holdout_bonus,
        "HOLDOUT_SYNERGY_OUTPUT": paths.holdout_synergy
        if config.run_synergy == "1"
        else "",
        "HOLDOUT_EVALUATION_OUTPUT": paths.holdout_evaluation,
        "HOLDOUT_SYNERGY_EVALUATION_OUTPUT": paths.holdout_synergy_evaluation
        if config.run_synergy == "1"
        else "",
        "HOLDOUT_COMPARISON_OUTPUT": paths.comparison
        if config.run_synergy == "1"
        else "",
    }


@dataclass(frozen=True)
class HoldoutStage:
    """One command in the temporal holdout workflow."""

    name: str
    command: list[str]
    completion_message: str | None = None


def build_frozen_holdout_stages(
    config: HoldoutConfig, paths: HoldoutPaths
) -> list[HoldoutStage]:
    """Construct the frozen matrix-infill command sequence (no test refitting).

    Stage 1 trains on the training split; Stage 2 (and synergy) train on the
    training split too, since they are the source of the frozen bonus
    parameters. The test split is then *scored* by 'holdout.frozen_predict',
    which replays both stages at the training medians rather than fitting. The
    evaluation / synergy / comparison stages are the established ones and read
    the frozen prediction CSVs unchanged.
    """
    scripts = MODELS[config.model]
    train_split = config.train_split
    test_split = config.test_split
    tournament = config.tournament
    lr = config.lr
    seed = config.seed
    device = config.device
    bonus_steps = config.bonus_steps
    train_pyr = paths.train_pyramidal
    train_bonus = paths.train_bonus
    train_synergy = paths.train_synergy
    holdout_pyr = paths.holdout_pyramidal
    holdout_bonus = paths.holdout_bonus
    holdout_synergy = paths.holdout_synergy
    pyr_extra, comp_extra = model_stage_args(config, train_pyr)
    calibrate = ["--calibrate-correctness"] if config.calibrate_correctness == "1" else []

    stages: list[HoldoutStage] = []
    # 1. Stage-1 training on the training split (source of frozen tossup params).
    stages.append(HoldoutStage("train-pyramidal", [
        PYTHON, "-m", scripts["pyramidal"],
        "--split", train_split, *tournament_args(tournament),
        "--steps", config.pyramidal_steps, "--lr", lr, "--seed", seed,
        "--device", device, "--output-dir", train_pyr, *pyr_extra,
    ]))
    # 2. Stage-2 training on the training split (source of frozen bonus params).
    stages.append(HoldoutStage(
        "train-compositional",
        bonus_stage_command(
            scripts, split=train_split, tournament=tournament,
            player_skills=f"{train_pyr}/players.csv", output_dir=train_bonus,
            steps=bonus_steps, lr=lr, seed=seed, device=device,
            extra_args=list(comp_extra),
        ),
    ))
    if config.run_synergy == "1":
        # --save-synergy-details writes player_synergy_profiles.csv, which the
        # frozen bonus scorer freezes as psi.
        stages.append(HoldoutStage(
            "train-synergy",
            bonus_stage_command(
                scripts, split=train_split, tournament=tournament,
                player_skills=f"{train_pyr}/players.csv", output_dir=train_synergy,
                steps=bonus_steps, lr=lr, seed=seed, device=device,
                extra_args=[
                    "--use-synergy", "--synergy-dimensions", config.synergy_dimensions,
                    "--save-synergy-details", *comp_extra,
                ],
            ),
        ))

    # 3. Frozen Stage-1 scoring of the test split at the training medians.
    stages.append(HoldoutStage("frozen-pyramidal", [
        PYTHON, "-m", "holdout.frozen_predict", "tossup",
        "--split", test_split, *tournament_args(tournament),
        "--train-pyramidal", train_pyr,
        "--dimensions", config.dimensions,
        "--difficulty-link", config.difficulty_link,
        "--device", device, "--output-dir", holdout_pyr, *calibrate,
    ]))
    # 4. Frozen Stage-2 scoring of the test split at the training medians.
    stages.append(HoldoutStage("frozen-compositional", [
        PYTHON, "-m", "holdout.frozen_predict", "bonus",
        "--split", test_split, *tournament_args(tournament),
        "--train-pyramidal", train_pyr, "--train-compositional", train_bonus,
        "--device", device, "--output-dir", holdout_bonus, *calibrate,
    ]))
    if config.run_synergy == "1":
        stages.append(HoldoutStage("frozen-synergy", [
            PYTHON, "-m", "holdout.frozen_predict", "bonus",
            "--split", test_split, *tournament_args(tournament),
            "--train-pyramidal", train_pyr, "--train-compositional", train_synergy,
            "--use-synergy",
            "--device", device, "--output-dir", holdout_synergy, *calibrate,
        ]))

    # 5. Scenario A/B evaluation on the frozen predictions (established stages).
    stages.append(HoldoutStage("holdout-evaluation", [
        PYTHON, "-m", scripts["evaluate"],
        "--pyramidal-results", holdout_pyr,
        "--compositional-results", holdout_bonus,
        "--output-dir", paths.holdout_evaluation,
    ]))
    if config.run_synergy == "1":
        stages.append(HoldoutStage("holdout-synergy-evaluation", [
            PYTHON, "-m", scripts["evaluate"],
            "--pyramidal-results", holdout_pyr,
            "--compositional-results", holdout_synergy,
            "--output-dir", paths.holdout_synergy_evaluation,
        ]))
        stages.append(HoldoutStage("compare-bonus-models", [
            PYTHON, "run_scripts/common/run_synergy_comparison.py",
            "--compositional-metrics",
            f"{paths.holdout_evaluation}/csvs/bonus_metrics.csv",
            "--synergy-metrics",
            f"{paths.holdout_synergy_evaluation}/csvs/bonus_metrics.csv",
            "--output-dir", paths.comparison,
        ]))
    return stages


def build_holdout_stages(
    config: HoldoutConfig, paths: HoldoutPaths
) -> list[HoldoutStage]:
    """Construct the established holdout command sequence without running it."""
    if config.frozen_predict == "1":
        return build_frozen_holdout_stages(config, paths)
    scripts = MODELS[config.model]

    pyr_extra, comp_extra = model_stage_args(config, paths.train_pyramidal)
    stages: list[HoldoutStage] = []
    # 1. Stage-1 training on the historical split.
    stages.append(HoldoutStage("train-pyramidal", [
        PYTHON, "-m", scripts["pyramidal"],
        "--split", config.train_split, *tournament_args(config.tournament),
        "--steps", config.pyramidal_steps, "--lr", config.lr,
        "--seed", config.seed, "--device", config.device,
        "--output-dir", paths.train_pyramidal, *pyr_extra,
    ]))

    # 2. Stage-1 held-out transductive pass on the test split with informative
    #    player priors built from the training posterior.
    stages.append(HoldoutStage("holdout-pyramidal", [
        PYTHON, "-m", scripts["pyramidal"],
        "--split", config.test_split, *tournament_args(config.tournament),
        "--steps", config.pyramidal_steps, "--lr", config.lr,
        "--seed", config.seed, "--device", config.device,
        "--train-posterior", f"{paths.train_pyramidal}/player_posterior.csv",
        "--new-player-prior", config.new_player_prior,
        "--output-dir", paths.holdout_pyramidal, *pyr_extra,
    ]))

    # 3. Stage-2 bonus model on the test split using the held-out player skills.
    stages.append(HoldoutStage(
        "holdout-compositional",
        bonus_stage_command(
            scripts,
            split=config.test_split,
            tournament=config.tournament,
            player_skills=f"{paths.holdout_pyramidal}/players.csv",
            output_dir=paths.holdout_bonus,
            steps=config.bonus_steps,
            lr=config.lr,
            seed=config.seed,
            device=config.device,
            extra_args=comp_extra,
        ),
    ))

    if config.run_synergy == "1":
        synergy_extra = [
            "--use-synergy",
            "--synergy-dimensions",
            config.synergy_dimensions,
        ]
        if config.save_synergy_details == "1":
            synergy_extra.append("--save-synergy-details")
        synergy_extra.extend(comp_extra)
        stages.append(HoldoutStage(
            "holdout-synergy",
            bonus_stage_command(
                scripts,
                split=config.test_split,
                tournament=config.tournament,
                player_skills=f"{paths.holdout_pyramidal}/players.csv",
                output_dir=paths.holdout_synergy,
                steps=config.bonus_steps,
                lr=config.lr,
                seed=config.seed,
                device=config.device,
                extra_args=synergy_extra,
            ),
        ))

    # 4. Scenario A/B evaluation on the held-out predictions.
    stages.append(HoldoutStage("holdout-evaluation", [
        PYTHON, "-m", scripts["evaluate"],
        "--pyramidal-results", paths.holdout_pyramidal,
        "--compositional-results", paths.holdout_bonus,
        "--output-dir", paths.holdout_evaluation,
    ]))

    if config.run_synergy == "1":
        stages.append(HoldoutStage("holdout-synergy-evaluation", [
            PYTHON, "-m", scripts["evaluate"],
            "--pyramidal-results", paths.holdout_pyramidal,
            "--compositional-results", paths.holdout_synergy,
            "--output-dir", paths.holdout_synergy_evaluation,
        ]))
        stages.append(HoldoutStage("compare-bonus-models", [
            PYTHON, "run_scripts/common/run_synergy_comparison.py",
            "--compositional-metrics",
            f"{paths.holdout_evaluation}/csvs/bonus_metrics.csv",
            "--synergy-metrics",
            f"{paths.holdout_synergy_evaluation}/csvs/bonus_metrics.csv",
            "--output-dir",
            paths.comparison,
        ]))

    return stages


def configure_run(config: HoldoutConfig, paths: HoldoutPaths) -> None:
    """Configure logging and environment defaults before executing stages."""
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    os.environ["MPLCONFIGDIR"] = config.mplconfigdir
    if os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(Path(config.root) / "run.log")
    print(format_run_log_header(run_log_fields(config, paths)), flush=True)


def execute_stages(stages: list[HoldoutStage]) -> None:
    """Run stages in order and emit stage-specific completion messages."""
    for stage in stages:
        run(stage.command)
        if stage.completion_message:
            print(stage.completion_message)


def report_completion(config: HoldoutConfig, paths: HoldoutPaths) -> None:
    """Report the established final output locations."""
    print(
        f"Finished held-out {config.model} run. "
        f"Scenario A/B metrics in {paths.holdout_evaluation}."
    )
    if config.run_synergy == "1":
        print(f"Synergy metrics in {paths.holdout_synergy_evaluation}.")


def main() -> None:
    config = resolve_config()
    warn_env_knob_typos()
    paths = output_paths(config.root)
    configure_run(config, paths)
    execute_stages(build_holdout_stages(config, paths))
    report_completion(config, paths)


if __name__ == "__main__":
    main()
