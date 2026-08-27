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

* 'MODEL'           baseline | multidim | topic | learned | tfidf |
                    tfidf_multidim | topic_tfidf | learned_tfidf
                    (default baseline)
* 'TRAIN_SPLIT' / 'TEST_SPLIT'                    (default year_2024 / year_2025)
* 'NEW_PLAYER_PRIOR' tier | flat                    (default tier)
* 'ROOT'            output root                      (default results/compirt/holdout/<MODEL>)
* 'TOURNAMENT'      restrict to a tournament prefix; "" = whole split
* 'PYRAMIDAL_STEPS' / 'BONUS_STEPS' / 'DIMENSIONS' / 'LR' / 'DEVICE'
* 'RUN_SYNERGY' defaults to 1 for 'MODEL=multidim' and 0 otherwise
* 'SYNERGY_DIMENSIONS' / 'SAVE_SYNERGY_DETAILS' configure the synergy branch
* 'CALIBRATE_CORRECTNESS' 1 enables the same Platt scale+bias calibration as
  the full-data runners
* 'RUN_C1_C4' 1 adds the paper Scenario C roster-generalization evaluation
* 'C1_C4_ITEM_STEPS' / 'C1_C4_MIN_CROSS_TEAM_GAMES' configure that opt-in
  evaluation
* 'TOPIC_VECTORS'   topic variant document-vector CSV (optional override)
* 'DATABASE'        learned variant question-text DB (optional override)
* 'TFIDF_EFFECT_PRIOR_SCALE' / 'NO_NORMALIZE_TFIDF' configure cumulative tfidf
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
    # Use d_jk(t) = tanh(... + bias_jk) * scale for Stage 1, followed by the
    # standard compositional and evaluation stages.
    "multidim_tanhbias": {
        "pyramidal": "multidimensional.multidim_mirt.train_pyramidal_tanhbias",
        "compositional": "train_compositional",
        "evaluate": "evaluate_compirt",
    },
    "topic": {
        "pyramidal": "topic.fixed.train_topic_pyramidal",
        "compositional": "topic.fixed.train_topic_compositional",
        "evaluate": "topic.fixed.evaluate_topic_compirt",
    },
    # Route learned-topic weights named 'topic_weight_*' through the evaluator
    # that produces their difficulty and timing figures.
    "learned": {
        "pyramidal": "topic.learned.train_joint_pyramidal",
        "compositional": "topic.learned.train_joint_compositional",
        "evaluate": "topic.fixed.evaluate_topic_compirt",
    },
    "tfidf": {
        "pyramidal": "tfidf.train_tfidf_pyramidal",
        "compositional": "train_compositional",
        "evaluate": "evaluate_compirt",
    },
    # Topic-specific TF-IDF (topic/tfidf): the topic families' Stage 1 with a
    # per-topic TF-IDF lambda; Stage 2 and metrics reuse the topic packages,
    # evaluated with the TF-IDF-aware replay evaluator.
    "topic_tfidf": {
        "pyramidal": "topic.tfidf.train_fixed_pyramidal",
        "compositional": "topic.fixed.train_topic_compositional",
        "evaluate": "topic.tfidf.evaluate",
    },
    "learned_tfidf": {
        "pyramidal": "topic.tfidf.train_learned_pyramidal",
        "compositional": "topic.learned.train_joint_compositional",
        "evaluate": "topic.tfidf.evaluate",
    },
    "tfidf_multidim": {
        "pyramidal": "tfidf.multidim.train_pyramidal",
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
    difficulty_scale: str
    lr: str
    seed: str
    device: str
    calibrate_correctness: str
    run_synergy: str
    synergy_dimensions: str
    save_synergy_details: str
    run_c1_c4: str
    c1_c4_item_steps: str
    c1_c4_min_cross_team_games: str
    c1_c4_seed: str
    topic_vectors: str | None
    database: str | None
    tfidf_effect_prior_scale: str
    no_normalize_tfidf: str
    tfidf_plot_count: str
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
    run_c1_c4 = env_default("RUN_C1_C4", "0")
    scenario_c_models = {"baseline", "multidim", "tfidf", "tfidf_multidim"}
    if run_c1_c4 == "1" and model not in scenario_c_models:
        raise SystemExit(
            "RUN_C1_C4=1 supports baseline, multidim, tfidf, and "
            f"tfidf_multidim; got MODEL={model!r}"
        )

    frozen_predict = env_default("FROZEN_PREDICT", "0")
    if frozen_predict == "1" and model != "multidim":
        raise SystemExit(
            "FROZEN_PREDICT=1 (frozen matrix-infill scoring) currently supports "
            f"MODEL=multidim only; got MODEL={model!r}"
        )
    if frozen_predict == "1" and run_c1_c4 == "1":
        raise SystemExit("FROZEN_PREDICT=1 is incompatible with RUN_C1_C4=1")

    bonus_steps = env_default("BONUS_STEPS", "2000")
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
        bonus_steps=bonus_steps,
        dimensions=env_default("DIMENSIONS", "5"),
        difficulty_link=difficulty_link,
        difficulty_scale=env_default("DIFFICULTY_SCALE", "5.0"),
        lr=env_default("LR", "0.01"),
        seed=env_default("SEED", "42"),
        device=env_default("DEVICE", "cpu"),
        calibrate_correctness=env_default("CALIBRATE_CORRECTNESS", "0"),
        run_synergy=env_default(
            "RUN_SYNERGY",
            "1"
            if model in ("multidim", "multidim_tanhbias", "tfidf_multidim")
            else "0",
        ),
        synergy_dimensions=env_default("SYNERGY_DIMENSIONS", "3"),
        save_synergy_details=env_default("SAVE_SYNERGY_DETAILS", "0"),
        run_c1_c4=run_c1_c4,
        c1_c4_item_steps=env_default("C1_C4_ITEM_STEPS", bonus_steps),
        c1_c4_min_cross_team_games=env_default(
            "C1_C4_MIN_CROSS_TEAM_GAMES", "10"
        ),
        c1_c4_seed=env_default("C1_C4_SEED", "42"),
        topic_vectors=os.environ.get("TOPIC_VECTORS"),
        database=os.environ.get("DATABASE"),
        tfidf_effect_prior_scale=env_default("TFIDF_EFFECT_PRIOR_SCALE", "1.0"),
        no_normalize_tfidf=env_default("NO_NORMALIZE_TFIDF", "0"),
        tfidf_plot_count=env_default("TFIDF_PLOT_COUNT", "6"),
        mplconfigdir=env_default("MPLCONFIGDIR", "/tmp/matplotlib-compirt"),
    )


def model_stage_args(config: HoldoutConfig, train_pyramidal: str):
    """Return family-specific Stage-1 and Stage-2 CLI arguments."""
    pyramidal: list[str] = []
    compositional: list[str] = []
    model = config.model

    # Fixed-topic vectors determine dimensionality from their columns, while
    # learned-topic runs must pass the shared latent dimension to Stage 1.
    if model in (
        "baseline",
        "multidim",
        "multidim_tanhbias",
        "tfidf",
        "tfidf_multidim",
    ):
        pyramidal += ["--dimensions", config.dimensions]
        if model == "multidim":
            pyramidal += ["--difficulty-link", config.difficulty_link]
        elif model == "multidim_tanhbias":
            pyramidal += ["--difficulty-scale", config.difficulty_scale]
    elif model in ("topic", "topic_tfidf"):
        if config.topic_vectors:
            pyramidal += ["--topic-vectors", config.topic_vectors]
            compositional += ["--topic-vectors", config.topic_vectors]
    elif model in ("learned", "learned_tfidf"):
        pyramidal += ["--dimensions", config.dimensions]
        if config.database:
            pyramidal += ["--database", config.database]
            compositional += ["--database", config.database]
        # Stage 2 uses the frozen topics learned by the training Stage 1.
        compositional += ["--topic-model-dir", train_pyramidal]

    if model in ("tfidf", "tfidf_multidim"):
        pyramidal += [
            "--tfidf-effect-prior-scale",
            config.tfidf_effect_prior_scale,
        ]
        if config.no_normalize_tfidf == "1":
            pyramidal.append("--no-normalize-tfidf")
    if model in ("topic_tfidf", "learned_tfidf"):
        # Topic-TF-IDF passes its per-topic lambda prior through this flag.
        pyramidal += ["--effect-prior-scale", config.tfidf_effect_prior_scale]
        if config.no_normalize_tfidf == "1":
            pyramidal.append("--no-normalize-tfidf")
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
    scenario_c_root: str
    scenario_c_evaluation: str


def output_paths(root: str) -> HoldoutPaths:
    """Resolve the established train/holdout result-directory contract."""
    scenario_c_root = f"{root}/holdout/c1-c4"
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
        scenario_c_root=scenario_c_root,
        scenario_c_evaluation=f"{scenario_c_root}/evaluation",
    )


def run_log_fields(config: HoldoutConfig, paths: HoldoutPaths):
    """Return the public run metadata in its established field order."""
    tfidf_models = {"tfidf", "tfidf_multidim", "topic_tfidf", "learned_tfidf"}
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
        "DIFFICULTY_SCALE": config.difficulty_scale
        if config.model == "multidim_tanhbias"
        else "",
        "PYRAMIDAL_STEPS": config.pyramidal_steps,
        "BONUS_STEPS": config.bonus_steps,
        "LR": config.lr,
        "SEED": config.seed,
        "RUN_SYNERGY": config.run_synergy,
        "SYNERGY_DIMENSIONS": config.synergy_dimensions,
        "SAVE_SYNERGY_DETAILS": config.save_synergy_details,
        "CALIBRATE_CORRECTNESS": config.calibrate_correctness,
        "RUN_C1_C4": config.run_c1_c4,
        "C1_C4_ITEM_STEPS": config.c1_c4_item_steps
        if config.run_c1_c4 == "1"
        else "",
        "C1_C4_MIN_CROSS_TEAM_GAMES": config.c1_c4_min_cross_team_games
        if config.run_c1_c4 == "1"
        else "",
        "C1_C4_SEED": config.c1_c4_seed if config.run_c1_c4 == "1" else "",
        "TOPIC_VECTORS": config.topic_vectors or "",
        "DATABASE": config.database or "",
        "TFIDF_EFFECT_PRIOR_SCALE": config.tfidf_effect_prior_scale
        if config.model in tfidf_models
        else "",
        "NO_NORMALIZE_TFIDF": config.no_normalize_tfidf
        if config.model in tfidf_models
        else "",
        "TFIDF_PLOT_COUNT": config.tfidf_plot_count
        if config.model in ("tfidf", "tfidf_multidim")
        else "",
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
    heldout_pyr_extra = list(pyr_extra)
    if config.model in ("learned", "learned_tfidf"):
        heldout_pyr_extra += ["--train-topic-model", paths.train_pyramidal]
    stages.append(HoldoutStage("holdout-pyramidal", [
        PYTHON, "-m", scripts["pyramidal"],
        "--split", config.test_split, *tournament_args(config.tournament),
        "--steps", config.pyramidal_steps, "--lr", config.lr,
        "--seed", config.seed, "--device", config.device,
        "--train-posterior", f"{paths.train_pyramidal}/player_posterior.csv",
        "--new-player-prior", config.new_player_prior,
        "--output-dir", paths.holdout_pyramidal, *heldout_pyr_extra,
    ]))

    # Scenario C transfers Stage-2 team parameters learned on the historical
    # split. Its opt-in fits write to dedicated output paths.
    if config.run_c1_c4 == "1":
        historical_extra = list(comp_extra)
        stages.append(HoldoutStage(
            "train-compositional",
            bonus_stage_command(
                scripts,
                split=config.train_split,
                tournament=config.tournament,
                player_skills=f"{paths.train_pyramidal}/players.csv",
                output_dir=paths.train_bonus,
                steps=config.bonus_steps,
                lr=config.lr,
                seed=config.c1_c4_seed,
                device=config.device,
                extra_args=historical_extra,
            ),
        ))
        stages.append(HoldoutStage(
            "train-synergy",
            bonus_stage_command(
                scripts,
                split=config.train_split,
                tournament=config.tournament,
                player_skills=f"{paths.train_pyramidal}/players.csv",
                output_dir=paths.train_synergy,
                steps=config.bonus_steps,
                lr=config.lr,
                seed=config.c1_c4_seed,
                device=config.device,
                extra_args=[
                    "--use-synergy",
                    "--synergy-dimensions",
                    config.synergy_dimensions,
                    "--save-synergy-details",
                    *historical_extra,
                ],
            ),
        ))

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

    if config.model in ("tfidf", "tfidf_multidim"):
        stages.append(HoldoutStage("tfidf-difficulty-plots", [
            PYTHON, "-m", "tfidf.plot_tfidf_difficulty_curves",
            "--results-dir", paths.holdout_pyramidal,
            "--output-dir", f"{paths.holdout_evaluation}/graphs",
            "--count", config.tfidf_plot_count,
        ]))

    if config.run_c1_c4 == "1":
        stages.append(HoldoutStage("scenario-c", [
            PYTHON,
            "-m",
            "run_scripts.common.run_scenario_c",
            "--train-split",
            config.train_split,
            "--test-split",
            config.test_split,
            *tournament_args(config.tournament),
            "--train-player-skills",
            f"{paths.train_pyramidal}/players.csv",
            "--test-player-skills",
            f"{paths.holdout_pyramidal}/players.csv",
            "--train-compositional",
            paths.train_bonus,
            "--train-synergy",
            paths.train_synergy,
            "--output-root",
            paths.scenario_c_root,
            "--evaluation-dir",
            paths.scenario_c_evaluation,
            "--steps",
            config.c1_c4_item_steps,
            "--lr",
            config.lr,
            "--seed",
            config.c1_c4_seed,
            "--min-cross-team-games",
            config.c1_c4_min_cross_team_games,
            "--device",
            config.device,
        ], f"Scenario C metrics in {paths.scenario_c_evaluation}."))

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
