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
* 'PREDICT_BUZZ_POSITIONS' 1 writes expected first-buzz position diagnostics
* 'CALIBRATE_CORRECTNESS' 1 enables the same Platt scale+bias calibration as
  the full-data runners
* 'RUN_C1_C4' 1 adds the paper Scenario C roster-generalization evaluation
* 'C1_C4_ITEM_STEPS' / 'C1_C4_MIN_CROSS_TEAM_GAMES' configure that opt-in
  evaluation
* 'TOPIC_VECTORS'   topic variant document-vector CSV (optional override)
* 'DATABASE'        learned variant question-text DB (optional override)
* 'TFIDF_VARIANT'   tfidf variant: cumulative-difficulty
* 'TFIDF_EFFECT_PRIOR_SCALE' / 'NO_NORMALIZE_TFIDF' configure cumulative tfidf
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
    # The learned family needs the topic-weighted evaluator: its tossups.csv
    # names the relevance weights 'topic_weight_*', which the root evaluator does
    # not recognize, so it would silently skip the difficulty/timing figures.
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
    difficulty_link = env_default("DIFFICULTY_LINK", "sigmoid")
    if difficulty_link != "sigmoid" and model != "multidim":
        raise SystemExit(
            f"DIFFICULTY_LINK={difficulty_link!r} is only supported for "
            f"MODEL=multidim; got MODEL={model!r}"
        )
    lr = env_default("LR", "0.01")
    device = env_default("DEVICE", "cpu")
    calibrate_correctness = env_default("CALIBRATE_CORRECTNESS", "0")
    run_synergy = env_default(
        "RUN_SYNERGY",
        "1" if model in ("multidim", "tfidf_multidim") else "0",
    )
    synergy_dimensions = env_default("SYNERGY_DIMENSIONS", "3")
    save_synergy_details = env_default("SAVE_SYNERGY_DETAILS", "0")
    predict_buzz_positions = env_default("PREDICT_BUZZ_POSITIONS", "1")
    run_c1_c4 = env_default("RUN_C1_C4", "0")
    c1_c4_item_steps = env_default("C1_C4_ITEM_STEPS", bonus_steps)
    c1_c4_min_cross_team_games = env_default("C1_C4_MIN_CROSS_TEAM_GAMES", "10")
    c1_c4_seed = env_default("C1_C4_SEED", "42")
    scenario_c_models = {"baseline", "multidim", "tfidf", "tfidf_multidim"}
    if run_c1_c4 == "1" and model not in scenario_c_models:
        raise SystemExit(
            "RUN_C1_C4=1 supports baseline, multidim, tfidf, and "
            f"tfidf_multidim; got MODEL={model!r}"
        )

    topic_vectors = os.environ.get("TOPIC_VECTORS")
    database = os.environ.get("DATABASE")
    tfidf_variant = env_default("TFIDF_VARIANT", "cumulative-difficulty")
    if tfidf_variant != "cumulative-difficulty":
        raise ValueError("Only TFIDF_VARIANT=cumulative-difficulty is supported")
    tfidf_effect_prior_scale = env_default("TFIDF_EFFECT_PRIOR_SCALE", "1.0")
    no_normalize_tfidf = env_default("NO_NORMALIZE_TFIDF", "0")
    tfidf_plot_count = env_default("TFIDF_PLOT_COUNT", "6")
    mplconfigdir = env_default("MPLCONFIGDIR", "/tmp/matplotlib-compirt")

    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    os.environ["MPLCONFIGDIR"] = mplconfigdir

    train_pyr = f"{root}/train/pyramidal"
    train_bonus = f"{root}/train/compositional"
    train_synergy = f"{root}/train/synergy"
    holdout_pyr = f"{root}/holdout/pyramidal"
    holdout_bonus = f"{root}/holdout/compositional"
    holdout_synergy = f"{root}/holdout/synergy"
    holdout_eval = f"{root}/holdout/evaluation"
    holdout_synergy_eval = f"{root}/holdout/synergy-evaluation"
    scenario_c_root = f"{root}/holdout/c1-c4"
    scenario_c_eval = f"{scenario_c_root}/evaluation"

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
                "DIFFICULTY_LINK": difficulty_link if model == "multidim" else "",
                "PYRAMIDAL_STEPS": pyramidal_steps,
                "BONUS_STEPS": bonus_steps,
                "LR": lr,
                "RUN_SYNERGY": run_synergy,
                "SYNERGY_DIMENSIONS": synergy_dimensions,
                "SAVE_SYNERGY_DETAILS": save_synergy_details,
                "CALIBRATE_CORRECTNESS": calibrate_correctness,
                "PREDICT_BUZZ_POSITIONS": predict_buzz_positions,
                "RUN_C1_C4": run_c1_c4,
                "C1_C4_ITEM_STEPS": c1_c4_item_steps if run_c1_c4 == "1" else "",
                "C1_C4_MIN_CROSS_TEAM_GAMES": c1_c4_min_cross_team_games if run_c1_c4 == "1" else "",
                "C1_C4_SEED": c1_c4_seed if run_c1_c4 == "1" else "",
                "TOPIC_VECTORS": topic_vectors or "",
                "DATABASE": database or "",
                "TFIDF_VARIANT": tfidf_variant
                if model in ("tfidf", "tfidf_multidim")
                else "",
                "TFIDF_EFFECT_PRIOR_SCALE": tfidf_effect_prior_scale
                if model in ("tfidf", "tfidf_multidim", "topic_tfidf", "learned_tfidf")
                else "",
                "NO_NORMALIZE_TFIDF": no_normalize_tfidf
                if model in ("tfidf", "tfidf_multidim", "topic_tfidf", "learned_tfidf")
                else "",
                "TFIDF_PLOT_COUNT": tfidf_plot_count
                if model in ("tfidf", "tfidf_multidim")
                else "",
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
    if model in ("baseline", "multidim", "tfidf", "tfidf_multidim"):
        pyr_extra += ["--dimensions", dimensions]
        if model == "multidim":
            pyr_extra += ["--difficulty-link", difficulty_link]
    elif model in ("topic", "topic_tfidf"):
        if topic_vectors:
            pyr_extra += ["--topic-vectors", topic_vectors]
            comp_extra += ["--topic-vectors", topic_vectors]
    elif model in ("learned", "learned_tfidf"):
        pyr_extra += ["--dimensions", dimensions]
        if database:
            pyr_extra += ["--database", database]
            comp_extra += ["--database", database]
        # Bonus stage reuses the frozen topics from the TRAINING pyramidal run.
        comp_extra += ["--topic-model-dir", train_pyr]
    if model in ("tfidf", "tfidf_multidim"):
        pyr_extra += [
            "--tfidf-variant",
            tfidf_variant,
            "--tfidf-effect-prior-scale",
            tfidf_effect_prior_scale,
        ]
        if no_normalize_tfidf == "1":
            pyr_extra += ["--no-normalize-tfidf"]
    if model in ("topic_tfidf", "learned_tfidf"):
        # The topic-tfidf trainers learn a per-topic lambda vector; the flag
        # name differs from the scalar tfidf family's --tfidf-effect-prior-scale.
        pyr_extra += ["--effect-prior-scale", tfidf_effect_prior_scale]
        if no_normalize_tfidf == "1":
            pyr_extra += ["--no-normalize-tfidf"]
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
    if model in ("learned", "learned_tfidf"):
        heldout_pyr_extra += ["--train-topic-model", train_pyr]
    run([
        PYTHON, "-m", scripts["pyramidal"],
        "--split", test_split, *tournament_args(tournament),
        "--steps", pyramidal_steps, "--lr", lr, "--device", device,
        "--train-posterior", f"{train_pyr}/player_posterior.csv",
        "--new-player-prior", new_player_prior,
        "--output-dir", holdout_pyr, *heldout_pyr_extra,
    ])

    # Scenario C transfers Stage-2 team parameters learned on the historical
    # split. These extra fits are opt-in and live outside the existing A/B
    # output paths, so RUN_C1_C4=0 preserves the current pipeline exactly.
    if run_c1_c4 == "1":
        historical_extra = [*comp_extra, "--seed", c1_c4_seed]
        run_bonus_stage(
            scripts,
            train_split,
            tournament,
            f"{train_pyr}/players.csv",
            train_bonus,
            bonus_steps,
            lr,
            device,
            historical_extra,
        )
        run_bonus_stage(
            scripts,
            train_split,
            tournament,
            f"{train_pyr}/players.csv",
            train_synergy,
            bonus_steps,
            lr,
            device,
            [
                "--use-synergy",
                "--synergy-dimensions",
                synergy_dimensions,
                "--save-synergy-details",
                *historical_extra,
            ],
        )

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

    if model in ("tfidf", "tfidf_multidim"):
        run([
            PYTHON, "-m", "tfidf.plot_tfidf_difficulty_curves",
            "--results-dir", holdout_pyr,
            "--output-dir", f"{holdout_eval}/graphs",
            "--count", tfidf_plot_count,
        ])

    if run_c1_c4 == "1":
        run([
            PYTHON,
            "-m",
            "run_scripts.run_scenario_c",
            "--train-split",
            train_split,
            "--test-split",
            test_split,
            *tournament_args(tournament),
            "--train-player-skills",
            f"{train_pyr}/players.csv",
            "--test-player-skills",
            f"{holdout_pyr}/players.csv",
            "--train-compositional",
            train_bonus,
            "--train-synergy",
            train_synergy,
            "--output-root",
            scenario_c_root,
            "--evaluation-dir",
            scenario_c_eval,
            "--steps",
            c1_c4_item_steps,
            "--lr",
            lr,
            "--seed",
            c1_c4_seed,
            "--min-cross-team-games",
            c1_c4_min_cross_team_games,
            "--device",
            device,
        ])
        print(f"Scenario C metrics in {scenario_c_eval}.")

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
