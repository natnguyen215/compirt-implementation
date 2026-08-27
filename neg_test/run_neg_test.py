"""5-fold cross-validated neg / buzz comparison across difficulty-curve models.

For each model config and each game-holdout fold of `year_2024`, this runs the
transductive held-out pass:

  1. Stage-1 train on the fold's TRAIN games  -> player_posterior.csv
  2. Stage-1 held-out pass on the fold's TEST games, with those player priors
     (question params co-estimated on the test games)  -> held-out predictions

Neg and buzz statistics are then read straight from the held-out Stage-1 tossup
predictions (no Stage-2 / bonus step is needed for those metrics), averaged over
folds, and written to `summary.csv` at the run root.

Four difficulty-curve families are compared:

  multidim            multidim sigmoid (multidimensional.multidim_mirt)
  ta-*                test_additions with its decoupled buzz-timing term
  bernstein-drop2     monotone Bernstein polynomial (degree 5, drop conc. 2.0)
  dd-*                hazard_double_difficulty: the multidim and Bernstein
                      curves refit with a *separate* difficulty curve for
                      correctness and for the buzz hazard, so each `dd-` arm is
                      a direct A/B against the same-flagged arm above

Their correctness recalibration is named by suffix: no suffix is uncalibrated,
`-cal` adds the constant Platt scale+bias, and `-cal-noscale` keeps only the
additive bias. `per-position-cal` and `ta-both` instead use the test_additions
position-varying calibration. `CONFIGS` below holds the exact flags; `README.md`
holds the results — the fitted scale lands near 0.23, so the bias-only variants
trade a little calibration for much better neg discrimination.

Everything lands under `results/compirt/holdout/common/neg-test/`. These folds
train and evaluate on disjoint games, so they belong in the holdout tier, and
`common/` is the home for studies that span model families rather than
belonging to one. ROOT goes through `resolve_result_root` like every other
runner. Env knobs:
DEVICE GPU DIMENSIONS PYR_STEPS LR SEED N_FOLDS CONFIGS FOLDS RERUN EVALUATE
STAGE (run|aggregate|all). Set `EVALUATE=1` to also write the full Scenario A
evaluation beside each held-out fit.

Run from the repo root::

    .venv/bin/python -m neg_test.run_neg_test
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import pandas as pd

from compirt_eval.common.metrics import classification_metrics
from holdout.game_splits import game_holdout_split_name
from utils.run_logging import (
    env_default,
    resolve_result_root,
    run_logged,
    tee_run_output,
    warn_env_knob_typos,
)

PYTHON = os.environ.get("PYTHON", str(REPO_ROOT / ".venv" / "bin" / "python"))

# config name -> (Stage-1 trainer module, model flags applied to BOTH passes).
CONFIGS = {
    "multidim": ("multidimensional.multidim_mirt.train_pyramidal", []),
    "multidim-cal": (
        "multidimensional.multidim_mirt.train_pyramidal",
        ["--calibrate-correctness"],
    ),
    "multidim-cal-noscale": (
        "multidimensional.multidim_mirt.train_pyramidal",
        ["--calibrate-correctness", "--calibration-no-scale"],
    ),
    "per-position-cal": ("test_additions.train_pyramidal", ["--improve-correctness"]),
    "ta-timing": ("test_additions.train_pyramidal", ["--improve-timing"]),
    "ta-timing-cal": (
        "test_additions.train_pyramidal",
        ["--improve-timing", "--calibrate-correctness"],
    ),
    "ta-timing-cal-noscale": (
        "test_additions.train_pyramidal",
        ["--improve-timing", "--calibrate-correctness", "--calibration-no-scale"],
    ),
    "ta-both": (
        "test_additions.train_pyramidal",
        ["--improve-timing", "--improve-correctness"],
    ),
    "bernstein-drop2": (
        "polynomial_compirt.train_pyramidal",
        ["--degree", "5", "--drop-concentration", "2.0"],
    ),
    "bernstein-drop2-cal-noscale": (
        "polynomial_compirt.train_pyramidal",
        [
            "--degree", "5", "--drop-concentration", "2.0",
            "--calibrate-correctness", "--calibration-no-scale",
        ],
    ),
    # Separate correctness and hazard difficulty curves; flags mirror the
    # single-curve arm of the same name so each pair is a clean A/B.
    "dd-multidim": ("hazard_double_difficulty.multidim.train_pyramidal", []),
    "dd-multidim-cal-noscale": (
        "hazard_double_difficulty.multidim.train_pyramidal",
        ["--calibrate-correctness", "--calibration-no-scale"],
    ),
    "dd-bernstein-drop2": (
        "hazard_double_difficulty.bernstein.train_pyramidal",
        ["--degree", "5", "--drop-concentration", "2.0"],
    ),
    "dd-bernstein-drop05": (
        "hazard_double_difficulty.bernstein.train_pyramidal",
        ["--degree", "5", "--drop-concentration", "0.5"],
    ),
    "dd-bernstein-drop2-cal-noscale": (
        "hazard_double_difficulty.bernstein.train_pyramidal",
        [
            "--degree", "5", "--drop-concentration", "2.0",
            "--calibrate-correctness", "--calibration-no-scale",
        ],
    ),
}


def stage1(module, split, output_dir, flags, common, train_posterior=None):
    """Run one Stage-1 fit (train or held-out) unless its marker already exists."""
    marker = output_dir / "summary.json"
    if marker.exists() and env_default("RERUN", "0") != "1":
        print(f"skip (exists): {output_dir}")
        return
    args = [
        PYTHON,
        "-m",
        module,
        "--split",
        split,
        "--dimensions",
        common["dim"],
        "--steps",
        common["steps"],
        "--lr",
        common["lr"],
        "--seed",
        common["seed"],
        "--device",
        common["device"],
        *flags,
        "--output-dir",
        str(output_dir),
    ]
    if train_posterior is not None:
        args += [
            "--train-posterior",
            str(train_posterior),
            "--new-player-prior",
            "tier",
        ]
    run_logged(args, cwd=REPO_ROOT)


def evaluate_stage(holdout_dir):
    """Write the full tossup evaluation beside one held-out Stage-1 fit."""
    output_dir = holdout_dir.parent / "evaluation"
    marker = output_dir / "csvs" / "tossup_metrics.csv"
    if marker.exists() and env_default("RERUN", "0") != "1":
        print(f"skip (exists): {output_dir}")
        return
    run_logged(
        [
            PYTHON,
            "-m",
            "run_scripts.paper_model_selection.evaluate_fold",
            "--pyramidal-results",
            str(holdout_dir),
            "--output-dir",
            str(output_dir),
        ],
        cwd=REPO_ROOT,
    )


def run_all(root, configs, folds, common, evaluate=False):
    """Train + held-out each (config, fold)."""
    base_split = common["base_split"]
    n_folds, seed = common["n_folds"], common["seed"]
    for config in configs:
        module, flags = CONFIGS[config]
        for fold in folds:
            train_split = game_holdout_split_name(
                base_split, "train", n_folds, fold, seed
            )
            test_split = game_holdout_split_name(
                base_split, "test", n_folds, fold, seed
            )
            fold_dir = root / config / f"fold{fold}"
            train_dir = fold_dir / "train" / "pyramidal"
            holdout_dir = fold_dir / "holdout" / "pyramidal"
            print(f"\n===== {config} | fold {fold} | TRAIN =====")
            stage1(module, train_split, train_dir, flags, common)
            print(f"===== {config} | fold {fold} | HELD-OUT =====")
            stage1(
                module,
                test_split,
                holdout_dir,
                flags,
                common,
                train_posterior=train_dir / "player_posterior.csv",
            )
            if evaluate:
                print(f"===== {config} | fold {fold} | EVALUATE =====")
                evaluate_stage(holdout_dir)


def fold_metrics(holdout_dir):
    """Neg + buzz statistics from one held-out fold's Stage-1 predictions."""
    predictions = pd.read_csv(
        holdout_dir / "tossup_predictions.csv", low_memory=False
    )
    buzzes = predictions[predictions["z"] == "BUZZ"].dropna(
        subset=["y", "predicted_correct"]
    )
    observed = buzzes["y"].to_numpy()
    predicted = buzzes["predicted_correct"].to_numpy()
    correctness = classification_metrics(observed, predicted)
    events = pd.read_csv(holdout_dir / "buzz_event_predictions.csv")
    position_error = (
        events["observed_relative_position"] - events["predicted_relative_position"]
    ).abs()
    return {
        # A neg is a wrong first buzz, so the neg rate is 1 - the correct rate.
        "neg_calib_gap": abs((1 - observed).mean() - (1 - predicted).mean()),
        "corr_log_loss": correctness["log_loss"],
        "corr_ece": correctness["ece"],
        "corr_auc": correctness["auc"],
        "buzz_pos_mae": float(position_error.mean()),
    }


def aggregate(root, configs, folds):
    """Collect per-fold metrics and write per-fold + mean/std summaries."""
    rows = []
    for config in configs:
        for fold in folds:
            holdout_dir = root / config / f"fold{fold}" / "holdout" / "pyramidal"
            if not (holdout_dir / "tossup_predictions.csv").exists():
                print(f"missing predictions: {config} fold{fold}")
                continue
            rows.append({"config": config, "fold": fold, **fold_metrics(holdout_dir)})
    if not rows:
        raise SystemExit("No held-out predictions found to aggregate")
    by_fold = pd.DataFrame(rows)
    by_fold.to_csv(root / "summary_by_fold.csv", index=False)
    metrics = [
        "neg_calib_gap",
        "corr_log_loss",
        "corr_ece",
        "corr_auc",
        "buzz_pos_mae",
    ]
    collected = set(by_fold["config"])
    summary = (
        by_fold.groupby("config")[metrics]
        .agg(["mean", "std"])
        # Restore the CONFIGS order that groupby sorted away.
        .reindex([config for config in configs if config in collected])
    )
    summary.columns = [f"{m}_{s}" for m, s in summary.columns]
    summary = summary.round(4)
    summary.to_csv(root / "summary.csv")
    print("\n=== 5-fold mean (std) ===")
    show = summary[[f"{m}_mean" for m in metrics]].copy()
    show.columns = metrics
    print(show.to_string())
    print(f"\nWrote {root / 'summary.csv'} and {root / 'summary_by_fold.csv'}")


def main():
    root = Path(
        resolve_result_root(
            env_default("ROOT", "results/compirt/holdout/common/neg-test"),
            "holdout",
        )
    )
    root.mkdir(parents=True, exist_ok=True)
    device = env_default("DEVICE", "cuda")
    if device == "cuda":
        os.environ["CUDA_VISIBLE_DEVICES"] = env_default("GPU", "0")
    os.environ["PYTHONUNBUFFERED"] = "1"
    os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-compirt")

    common = {
        "base_split": env_default("BASE_SPLIT", "year_2024"),
        "n_folds": int(env_default("N_FOLDS", "5")),
        "dim": env_default("DIMENSIONS", "5"),
        "steps": env_default("PYR_STEPS", "3000"),
        "lr": env_default("LR", "0.01"),
        "seed": env_default("SEED", "42"),
        "device": device,
    }
    configs = env_default("CONFIGS", ",".join(CONFIGS)).split(",")
    all_folds = ",".join(str(fold) for fold in range(common["n_folds"]))
    folds = [int(fold) for fold in env_default("FOLDS", all_folds).split(",")]
    stage = env_default("STAGE", "all")
    evaluate = env_default("EVALUATE", "0") == "1"
    unknown_configs = [config for config in configs if config not in CONFIGS]
    if unknown_configs:
        raise SystemExit(f"Unknown CONFIGS values: {', '.join(unknown_configs)}")
    if common["n_folds"] < 2:
        raise SystemExit("N_FOLDS must be at least 2")
    invalid_folds = [fold for fold in folds if fold not in range(common["n_folds"])]
    if invalid_folds:
        raise SystemExit(f"FOLDS outside [0, {common['n_folds']}): {invalid_folds}")
    if stage not in {"run", "aggregate", "all"}:
        raise SystemExit("STAGE must be one of: run, aggregate, all")
    warn_env_knob_typos()

    if os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(root / "run.log", append=True)
    print(
        f"neg_test | configs={configs} folds={folds} device={device} "
        f"steps={common['steps']} dim={common['dim']} root={root}"
    )

    if stage in ("run", "all"):
        run_all(root, configs, folds, common, evaluate=evaluate)
    if stage in ("aggregate", "all"):
        aggregate(root, configs, folds)


if __name__ == "__main__":
    main()
