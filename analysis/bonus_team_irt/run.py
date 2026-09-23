"""Fit bonus-only team IRT, then score frozen predictions on matched games."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyro
import torch

from analysis.bonus_team_irt.model import (
    matched_games, observations, predict, team_irt, training_tensors,
)
from compirt_data import DEFAULT_DATA_DIR, load_hf_tables
from compirt_eval.scenario_b_bonuses.metrics import bonus_parts_with_difficulty
from holdout.game_splits import GameHoldoutSpec, game_holdout_masks, game_holdout_split_name
from utils.run_logging import resolve_result_root
from utils.training import convergence_summary, fit_svi, require_device


DD_ROOT = "results/compirt/holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal"
MULTIDIM_ROOT = "results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold"


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reference_paths(args, fold):
    return {f"{family}_{arm}": Path(root) / f"fold_{fold}" / "holdout" / arm / "bonus_part_predictions.csv"
            for family, root in (("dd", args.dd_root), ("multidim", args.multidim_root))
            for arm in ("compositional", "synergy")}


def fit_arm(train, test, output, args, dimensions):
    output.mkdir(parents=True, exist_ok=True)
    if not (output / "summary.json").exists():
        pyro.set_rng_seed(args.seed)
        data = training_tensors(train, args.device)
        print(f"Fitting {output}: {len(train):,} parts, {dimensions}D, {args.steps} steps", flush=True)
        medians, _, losses = fit_svi(
            team_irt, model_kwargs={"data": data, "dimensions": dimensions},
            n_steps=args.steps, lr=args.lr, posterior_output_dir=output,
            posterior_draws=0, posterior_seed=args.seed,
        )
        parameters = {key: value.detach().cpu().numpy() for key, value in medians.items()}
        if not np.isfinite(losses).all() or not all(np.isfinite(v).all() for v in parameters.values()):
            raise ValueError("Nonfinite fit")
        np.savez_compressed(output / "parameters.npz", **parameters)
        write_json(output / "ids.json", {"team_ids": data["team_ids"], "part_ids": data["part_ids"]})
        pd.DataFrame({"step": np.arange(1, len(losses) + 1), "loss": losses}).to_csv(output / "losses.csv", index=False)
        teams = pd.DataFrame({"team_id": data["team_ids"]})
        parts = pd.DataFrame({"bonus_part_id": data["part_ids"], "beta": parameters["beta"]})
        for dimension in range(dimensions):
            teams[f"theta_{dimension + 1}"] = parameters["theta"][:, dimension]
            parts[f"alpha_{dimension + 1}"] = parameters["alpha"][:, dimension]
        teams.to_csv(output / "team_skills.csv", index=False)
        parts.to_csv(output / "bonus_parts.csv", index=False)
        write_json(output / "summary.json", {
            "dimensions": dimensions, "steps": args.steps, "seed": args.seed, "lr": args.lr,
            "train_parts": len(train), "train_teams": len(teams), "train_bonus_parts": len(parts),
            "prediction": "sigmoid at training posterior medians",
            **convergence_summary(losses),
        })
    else:
        print(f"Resume saved fit {output}", flush=True)
    # Always replay the serialized fit, including immediately after fitting.
    with np.load(output / "parameters.npz") as saved:
        parameters = dict(saved)
    ids = json.loads((output / "ids.json").read_text())
    predictions = test.copy()
    predictions["predicted_correct"] = predict(test, parameters, **ids)
    predictions.to_csv(output / "bonus_part_predictions.csv", index=False)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    parser.add_argument("--split", default="year_2024")
    parser.add_argument("--n-folds", type=int, default=5)
    parser.add_argument("--folds", nargs="+", type=int, default=list(range(5)))
    parser.add_argument("--dimensions", nargs="+", type=int, default=[1, 3])
    parser.add_argument("--steps", type=int, default=3000)
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--split-seed", type=int, default=42)
    parser.add_argument("--device", choices=["cpu", "cuda"], default="cuda")
    parser.add_argument("--dd-root", default=DD_ROOT)
    parser.add_argument("--multidim-root", default=MULTIDIM_ROOT)
    parser.add_argument("--stage", choices=["all", "fit", "evaluate"], default="all")
    args = parser.parse_args()
    if args.steps < 1 or args.lr <= 0 or min(args.dimensions) < 1:
        parser.error("steps, lr and dimensions must be positive")
    if len(set(args.folds)) != len(args.folds) or len(set(args.dimensions)) != len(args.dimensions):
        parser.error("folds and dimensions must be unique")
    for fold in args.folds:
        game_holdout_split_name(args.split, "train", args.n_folds, fold, args.split_seed)
    return args


def main():
    args = parse_args()
    torch.set_num_threads(1)
    if args.stage != "evaluate":
        require_device(args.device)
    root = Path(resolve_result_root(args.output_dir, "holdout"))
    tables = load_hf_tables(args.data_dir, args.split)
    frame = bonus_parts_with_difficulty(observations(tables), tables["bonuses"])
    if frame.observation_id.duplicated().any():
        raise ValueError("Duplicate source observations")
    config = {key: value for key, value in vars(args).items() if key != "stage"}
    config["data_sha256"] = hashlib.sha256(pd.util.hash_pandas_object(frame, index=False).values.tobytes()).hexdigest()
    config["games_sha256"] = hashlib.sha256(tables["games"].to_json().encode()).hexdigest()
    config["priors"] = {"theta": "Normal(0,1)", "alpha": "Gamma(2,2) shape/rate", "beta": "Normal(0,1)"}
    config["code_sha256"] = {str(path): sha256(path) for path in [
        *sorted(Path("analysis/bonus_team_irt").glob("*.py")),
        Path("utils/training.py"), Path("holdout/game_splits.py"),
        Path("compirt_eval/scenario_b_bonuses/metrics.py"),
        Path("compirt_eval/scenario_b_bonuses/outcomes.py"),
        Path("compirt_eval/common/metrics.py"), Path("compirt_eval/common/categories.py"),
    ]}
    config["reference_sha256"] = {}
    for fold in args.folds:
        expected = game_holdout_split_name(args.split, "train", args.n_folds, fold, args.split_seed)
        for path in reference_paths(args, fold).values():
            summary = path.parents[2] / "train" / path.parent.name / "summary.json"
            if json.loads(summary.read_text())["split"] != expected:
                raise ValueError(f"Reference training split mismatch: {summary}")
            for source in (path, summary):
                config["reference_sha256"][str(source)] = sha256(source)
    config_path = root / "configuration.json"
    if config_path.exists() and json.loads(config_path.read_text()) != config:
        raise ValueError("Configuration, inputs or code changed; use a fresh output root")
    if args.stage == "evaluate" and not config_path.exists():
        raise ValueError("Evaluation requires an existing fitted run")
    write_json(config_path, config)
    selected_games = []
    for fold in args.folds:
        output = root / f"fold_{fold}"
        output.mkdir(parents=True, exist_ok=True)
        mask = game_holdout_masks(tables, GameHoldoutSpec(args.split, "test", args.n_folds, fold, args.split_seed))
        test_games = tables["games"].loc[mask]
        train = frame[~frame.game_id.isin(test_games.game_id)].copy()
        test = frame[frame.game_id.isin(test_games.game_id)].copy()
        references = {name: pd.read_csv(path) for name, path in reference_paths(args, fold).items()}
        exclusions = matched_games(train, test, references)
        exclusions.to_csv(output / "excluded_games.csv", index=False)
        games = test_games[~test_games.game_id.isin(exclusions.game_id)]
        test = test[test.game_id.isin(games.game_id)].copy()
        if set(train.game_id) & set(test.game_id):
            raise ValueError("Train/test game overlap")
        selected_games.append(games)
        write_json(output / "split.json", {
            "train_game_ids": sorted(tables["games"].loc[~mask, "game_id"]),
            "original_test_game_ids": sorted(test_games.game_id),
            "scored_game_ids": sorted(games.game_id),
            "train_parts": len(train), "test_parts": len(test),
            "excluded_games": len(exclusions),
            "disjoint_games": True,
        })
        if args.stage != "evaluate":
            for dimensions in args.dimensions:
                fit_arm(train, test, output / f"team_irt_{dimensions}d", args, dimensions)
        for name, reference in references.items():
            destination = output / name
            destination.mkdir(exist_ok=True)
            matched = test.copy()
            matched["predicted_correct"] = matched.observation_id.map(reference.set_index("observation_id").predicted_correct)
            matched.to_csv(destination / "bonus_part_predictions.csv", index=False)
    games = pd.concat(selected_games, ignore_index=True)
    if games.game_id.duplicated().any():
        raise ValueError("Overlapping evaluation folds")
    if args.stage != "fit":
        from analysis.bonus_team_irt.report import evaluate
        evaluate(root, args, tables, games)


if __name__ == "__main__":
    main()
