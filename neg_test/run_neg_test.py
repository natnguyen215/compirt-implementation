"""5-fold cross-validated neg / buzz comparison across difficulty-curve models.

For each model config and each game-holdout fold of `year_2024`, this runs the
transductive held-out pass:

  1. Stage-1 train on the fold's TRAIN games  -> player_posterior.csv
  2. Stage-1 held-out pass on the fold's TEST games, with those player priors
     (question params co-estimated on the test games)  -> held-out predictions

Neg and buzz statistics are then read straight from the held-out Stage-1 tossup
predictions (no Stage-2 / bonus step is needed for those metrics), averaged over
folds, and written to `results/neg_test/summary.csv`.

Models compared:
  multidim            multidim sigmoid, no calibration
  multidim-cal        multidim sigmoid + constant Platt calibration
  per-position-cal    test_additions, position-varying correctness calibration
  ta-timing           test_additions, decoupled buzz-timing term
  ta-both             test_additions, timing + position-varying calibration
  bernstein-drop2     monotone Bernstein polynomial (degree 5, drop conc. 2.0)

Everything lands under `results/neg_test/` (outside the in_sample / holdout
tiers, as requested). Env knobs: DEVICE GPU DIMENSIONS PYR_STEPS LR SEED N_FOLDS
CONFIGS FOLDS RERUN STAGE (run|aggregate|all).

Run from the repo root::

    .venv/bin/python -m neg_test.run_neg_test
"""

from __future__ import annotations

import os
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import numpy as np
import pandas as pd

from utils.run_logging import env_default, run_logged, tee_run_output
from compirt_eval.common.metrics import classification_metrics

PYTHON = os.environ.get("PYTHON", str(REPO_ROOT / ".venv" / "bin" / "python"))

# config name -> (Stage-1 trainer module, model flags applied to BOTH passes).
CONFIGS = {
    "multidim": ("multidimensional.multidim_mirt.train_pyramidal", []),
    "multidim-cal": (
        "multidimensional.multidim_mirt.train_pyramidal",
        ["--calibrate-correctness"],
    ),
    "per-position-cal": ("test_additions.train_pyramidal", ["--improve-correctness"]),
    "ta-timing": ("test_additions.train_pyramidal", ["--improve-timing"]),
    "ta-timing-cal": (
        "test_additions.train_pyramidal",
        ["--improve-timing", "--calibrate-correctness"],
    ),
    "ta-both": (
        "test_additions.train_pyramidal",
        ["--improve-timing", "--improve-correctness"],
    ),
    "bernstein-drop2": (
        "polynomial_compirt.train_pyramidal",
        ["--degree", "5", "--drop-concentration", "2.0"],
    ),
}


def stage1(module, split, output_dir, flags, common, train_posterior=None):
    """Run one Stage-1 fit (train or held-out) unless its marker already exists."""
    marker = output_dir / "summary.json"
    if marker.exists() and env_default("RERUN", "0") != "1":
        print(f"skip (exists): {output_dir}")
        return
    args = [
        PYTHON, "-m", module,
        "--split", split,
        "--dimensions", common["dim"],
        "--steps", common["steps"],
        "--lr", common["lr"],
        "--seed", common["seed"],
        "--device", common["device"],
        *flags,
        "--output-dir", str(output_dir),
    ]
    if train_posterior is not None:
        args += ["--train-posterior", str(train_posterior), "--new-player-prior", "tier"]
    run_logged(args, cwd=REPO_ROOT)


def run_all(root, configs, folds, common):
    """Train + held-out each (config, fold)."""
    base_split = common["base_split"]
    n_folds, seed = common["n_folds"], common["seed"]
    for config in configs:
        module, flags = CONFIGS[config]
        for fold in folds:
            train_split = f"game-holdout:{base_split}:train:{n_folds}:{fold}:{seed}"
            test_split = f"game-holdout:{base_split}:test:{n_folds}:{fold}:{seed}"
            fold_dir = root / config / f"fold{fold}"
            train_dir = fold_dir / "train" / "pyramidal"
            holdout_dir = fold_dir / "holdout" / "pyramidal"
            print(f"\n===== {config} | fold {fold} | TRAIN =====")
            stage1(module, train_split, train_dir, flags, common)
            print(f"===== {config} | fold {fold} | HELD-OUT =====")
            stage1(
                module, test_split, holdout_dir, flags, common,
                train_posterior=train_dir / "player_posterior.csv",
            )


def fold_metrics(holdout_dir):
    """Neg + buzz statistics from one held-out fold's Stage-1 predictions."""
    df = pd.read_csv(holdout_dir / "tossup_predictions.csv", low_memory=False)
    b = df[df["z"] == "BUZZ"].dropna(subset=["y", "predicted_correct"])
    y, p = b["y"].to_numpy(), b["predicted_correct"].to_numpy()
    m = classification_metrics(y, p)
    be = pd.read_csv(holdout_dir / "buzz_event_predictions.csv")
    mae = float(
        (be["observed_relative_position"] - be["predicted_relative_position"]).abs().mean()
    )
    return {
        "neg_calib_gap": abs((1 - y).mean() - (1 - p).mean()),
        "corr_log_loss": m["log_loss"],
        "corr_ece": m["ece"],
        "corr_auc": m["auc"],
        "buzz_pos_mae": mae,
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
    metrics = ["neg_calib_gap", "corr_log_loss", "corr_ece", "corr_auc", "buzz_pos_mae"]
    summary = (
        by_fold.groupby("config")[metrics]
        .agg(["mean", "std"])
        .reindex([c for c in configs if c in set(by_fold["config"])])
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
    root = Path(env_default("ROOT", "results/neg_test"))
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
    folds = [int(f) for f in env_default("FOLDS", ",".join(map(str, range(common["n_folds"])))).split(",")]
    stage = env_default("STAGE", "all")

    if os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(root / "run.log")
    print(f"neg_test | configs={configs} folds={folds} device={device} "
          f"steps={common['steps']} dim={common['dim']} root={root}")

    if stage in ("run", "all"):
        run_all(root, configs, folds, common)
    if stage in ("aggregate", "all"):
        aggregate(root, configs, folds)


if __name__ == "__main__":
    main()
