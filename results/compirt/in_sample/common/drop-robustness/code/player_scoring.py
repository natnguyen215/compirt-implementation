"""Rotation-invariant player scoring shared by ranking-stability studies.

This module parametrizes the predicted-PPG roster walk by model family so the
drop-robustness evaluators can score baseline (scalar-difficulty) and multidim
Stage-1 fits and the raw actual-PPG ranking on one shared observation frame.

Every ranking here is a rotation-invariant scalar per player (replayed points,
never raw theta_k coordinates), so it is comparable across refits.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import torch

from compirt_eval.scenario_a_tossups.outcomes import replay_rng, replay_tossup

import pyramidal_model as baseline_model
from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from multidimensional.multidim_mirt import pyramidal_model as multidim_model

POINTS_CORRECT = 10.0
POINTS_NEG = -5.0


def build_observations(split, tournament=None, data_dir=DEFAULT_DATA_DIR):
    """Load tables and build the full tossup observation frame."""
    tables = filter_tournament(load_hf_tables(data_dir, split), tournament)
    return build_tossup_observations(tables)


def tensors_and_games(observations):
    """Index an observation frame into tensors and games-played denominators."""
    data = tossup_tensors(observations, "cpu")
    if "team_id" in observations:
        data["replay_team_ids"] = observations["team_id"].astype(str).to_numpy()
    games = observations.groupby("player_id")["game_id"].nunique()
    return observations, data, games


def _numbered_columns(frame, prefix):
    names = [
        c for c in frame.columns if c.startswith(prefix) and c[len(prefix):].isdigit()
    ]
    names.sort(key=lambda c: int(c[len(prefix):]))
    return torch.tensor(frame[names].to_numpy(), dtype=torch.float32)


def load_posterior(run_dir, data, family):
    """Load saved Stage-1 point estimates aligned to the tensor index order.

    'run_dir' is the directory holding players.csv/tossups.csv. The weight
    vector is returned under "r" for both families (the baseline saves it as
    'alpha_*'); baseline difficulty params are scalar per tossup, multidim
    ones carry a trailing dimension axis — the roster walk broadcasts both.
    """
    run_dir = Path(run_dir)
    players = pd.read_csv(run_dir / "players.csv").set_index("player_id")
    tossups = pd.read_csv(run_dir / "tossups.csv").set_index("tossup_id")
    players = players.loc[data["player_ids"]]
    tossups = tossups.loc[data["tossup_ids"]]

    posterior = {
        "theta": _numbered_columns(players, "theta_"),
        "c": torch.tensor(players["c"].to_numpy(), dtype=torch.float32),
    }
    if family == "baseline":
        posterior["r"] = _numbered_columns(tossups, "alpha_")
        for name in ("beta", "gamma", "mu"):
            posterior[name] = torch.tensor(
                tossups[name].to_numpy(), dtype=torch.float32
            )
    elif family == "multidim":
        for name in ("r", "beta", "gamma", "mu"):
            posterior[name] = _numbered_columns(tossups, f"{name}_")
    else:
        raise ValueError(f"Unknown family for load_posterior: {family}")
    summary_path = run_dir / "summary.json"
    summary = json.loads(summary_path.read_text()) if summary_path.exists() else {}
    posterior["correctness_scale"] = float(summary.get("correctness_scale", 1.0))
    posterior["correctness_bias"] = float(summary.get("correctness_bias", 0.0))
    return posterior


def predicted_player_points(data, posterior, family, link="sigmoid"):
    """Replay total tossup points with the shared token-threshold policy."""
    model = {"baseline": baseline_model, "multidim": multidim_model}.get(family)
    if model is None:
        raise ValueError(f"Unknown family for predicted_player_points: {family}")
    points = np.zeros(len(data["player_ids"]))
    phase0 = data.get("is_phase0", torch.ones_like(data["event"], dtype=torch.bool))
    for event in range(len(data["event_ids"])):
        rows = torch.where((data["event"] == event) & phase0)[0]
        if not len(rows):
            continue
        roster = data["player"][rows]
        question = int(data["tossup"][rows[0]])
        total = int(data["T_j"][rows[0]])
        t = torch.arange(1, total + 1, dtype=torch.float32)[None, :]
        theta = posterior["theta"][roster, None, :]
        args = [theta, posterior["r"][question], posterior["beta"][question],
                posterior["gamma"][question], posterior["mu"][question]]
        extra = [link] if family == "multidim" else []
        hazard = model.hazard_logit(*args, posterior["c"][roster, None], t, total, *extra)
        correctness_logit = model.correctness_logit(*args, t, total, *extra)
        correctness = torch.sigmoid(
            posterior.get("correctness_scale", 1.0) * correctness_logit
            + posterior.get("correctness_bias", 0.0)
        )
        ids = np.asarray(data["player_ids"])[roster.numpy()]
        if "replay_team_ids" not in data and len(roster) > 1:
            raise ValueError("Team IDs are required for opponent-only replay scoring")
        teams = data["replay_team_ids"][rows.numpy()] if "replay_team_ids" in data else ids
        event_points, _buzzes = replay_tossup(
            ids, teams, hazard.detach().numpy(), correctness.detach().numpy(),
            rng=replay_rng(data["event_ids"][event]),
        )
        np.add.at(points, roster.numpy(), event_points)
    return torch.tensor(points, dtype=torch.float32)


def predicted_ppg(run_dir, data, games, family, link="sigmoid"):
    """Predicted points-per-game ranking series from a saved Stage-1 fit."""
    posterior = load_posterior(run_dir, data, family)
    points = predicted_player_points(data, posterior, family, link).numpy()
    ppg = pd.Series(points, index=list(data["player_ids"]), name="pred_ppg")
    ppg = ppg / games.reindex(ppg.index)
    return ppg.dropna()


def actual_ppg(observations):
    """Literal recorded tossup points per unique inferred-lineup game."""
    if "actual_player_tossup_points" not in observations:
        raise ValueError("Actual PPG requires literal recorded tossup points, including bouncebacks")
    games = observations.groupby("player_id")["game_id"].nunique()
    totals = (
        observations.drop_duplicates(["event_id", "player_id"])
        .groupby("player_id")["actual_player_tossup_points"].sum()
    )
    return (totals.reindex(games.index, fill_value=0.0) / games).rename("actual_ppg")
