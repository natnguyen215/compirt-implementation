"""Rotation-invariant player scoring shared by ranking-stability studies.

This module parametrizes the predicted-PPG roster walk by model family so the
noise-floor and drop-robustness evaluators can score baseline
(scalar-difficulty) and multidim Stage-1 fits, the plain-IRT comparator, and
the raw actual-PPG ranking on one shared observation frame.

Every ranking here is a rotation-invariant scalar per player (expected points,
never raw theta_k coordinates), so it is comparable across refits.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import torch

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
    return posterior


def predicted_player_points(data, posterior, family, link="sigmoid"):
    """Expected total tossup points per player under this fit (competing risks).

    Regroup rows into per-event rosters, walk token by token, split the
    "someone buzzes" mass across present players in proportion to each
    player's first-buzz-alone probability, and score +10 correct / -5 neg.
    """
    n_events = len(data["event_ids"])
    counts = torch.bincount(data["event"], minlength=n_events)
    max_roster = int(counts.max().item())
    roster = data["player"].new_zeros((n_events, max_roster))
    roster_mask = torch.zeros((n_events, max_roster), dtype=torch.bool)
    next_slot = [0] * n_events
    event_tossup = data["tossup"].new_zeros(n_events)
    event_T = data["T_j"].new_ones(n_events)
    for row in range(len(data["event"])):
        event = int(data["event"][row].item())
        slot = next_slot[event]
        roster[event, slot] = data["player"][row]
        roster_mask[event, slot] = True
        event_tossup[event] = data["tossup"][row]
        event_T[event] = data["T_j"][row]
        next_slot[event] += 1

    theta = posterior["theta"][roster]
    r = posterior["r"][event_tossup].unsqueeze(1)
    beta = posterior["beta"][event_tossup].unsqueeze(1)
    gamma = posterior["gamma"][event_tossup].unsqueeze(1)
    mu = posterior["mu"][event_tossup].unsqueeze(1)
    c = posterior["c"][roster]

    n_players = len(data["player_ids"])
    player_points = torch.zeros(n_players)
    event_survival = torch.ones(n_events)
    for position in range(1, int(event_T.max().item()) + 1):
        active_event = position <= event_T
        t = torch.full((n_events, max_roster), float(position))
        T = event_T.unsqueeze(1).expand_as(t)
        if family == "baseline":
            hazard_logits = baseline_model.hazard_logit(theta, r, beta, gamma, mu, c, t, T)
            correct_logits = baseline_model.correctness_logit(theta, r, beta, gamma, mu, t, T)
        elif family == "multidim":
            hazard_logits = multidim_model.hazard_logit(theta, r, beta, gamma, mu, c, t, T, link)
            correct_logits = multidim_model.correctness_logit(theta, r, beta, gamma, mu, t, T, link)
        else:
            raise ValueError(f"Unknown family for predicted_player_points: {family}")
        hazard = torch.sigmoid(hazard_logits)
        hazard = torch.where(roster_mask, hazard, torch.zeros_like(hazard))
        p_correct = torch.sigmoid(correct_logits)

        # P(nobody buzzes) is the product of each player's no-buzz probability.
        prod_no_buzz = torch.prod(1.0 - hazard, dim=1)
        total_hazard = 1.0 - prod_no_buzz
        # Split the "someone buzzes" mass across present players in proportion
        # to each player's first-buzz-alone probability, so attribution sums to
        # total_hazard (conserves probability under the model's own aggregation).
        weight = hazard * (prod_no_buzz.unsqueeze(1) / (1.0 - hazard).clamp_min(1e-6))
        weight_sum = weight.sum(dim=1, keepdim=True).clamp_min(1e-12)
        attribution = total_hazard.unsqueeze(1) * weight / weight_sum
        attribution = torch.where(
            active_event.unsqueeze(1), attribution, torch.zeros_like(attribution)
        )
        # Expected points if this player is the first buzzer at t.
        value = p_correct * POINTS_CORRECT + (1.0 - p_correct) * POINTS_NEG
        contribution = event_survival.unsqueeze(1) * attribution * value
        player_points.scatter_add_(0, roster.reshape(-1), contribution.reshape(-1))

        total_hazard = torch.where(active_event, total_hazard, torch.zeros_like(total_hazard))
        event_survival = event_survival * (1.0 - total_hazard)
    return player_points


def predicted_ppg(run_dir, data, games, family, link="sigmoid"):
    """Predicted points-per-game ranking series from a saved Stage-1 fit."""
    posterior = load_posterior(run_dir, data, family)
    points = predicted_player_points(data, posterior, family, link).numpy()
    ppg = pd.Series(points, index=list(data["player_ids"]), name="pred_ppg")
    ppg = ppg / games.reindex(ppg.index)
    return ppg.dropna()


def plain_irt_expected_ppg(run_dir, observations, games):
    """Expected PPG under a fitted plain-IRT run (simple_mirt.train_plain_irt).

    Sums fitted P(convert) = sigmoid(theta_i . alpha_j - d_j) over each
    player's observed cells, scaled by +10 per conversion (the plain model has
    no buzz/neg concept, so there is no -5 term), divided by games played.
    """
    from simple_mirt.train_plain_irt import response_matrix_from_observations

    run_dir = Path(run_dir)
    players = pd.read_csv(run_dir / "players.csv").set_index("player_id")
    questions = pd.read_csv(run_dir / "questions.csv").set_index("tossup_id")
    _, mask, player_ids, tossup_ids = response_matrix_from_observations(observations)

    theta = _numbered_columns(players.loc[player_ids], "theta_")
    alpha = _numbered_columns(questions.loc[tossup_ids], "alpha_")
    d = torch.tensor(questions.loc[tossup_ids, "d"].to_numpy(), dtype=torch.float32)
    p = torch.sigmoid(theta @ alpha.T - d)
    p = torch.where(mask, p, torch.zeros_like(p))
    points = POINTS_CORRECT * p.sum(dim=1).numpy()
    ppg = pd.Series(points, index=player_ids, name="plain_ppg")
    ppg = ppg / games.reindex(ppg.index)
    return ppg.dropna()


def actual_ppg(observations):
    """Raw points-per-game from the observation rows, no model.

    Uses the same +10/-5 scoring as the predicted walk (not the database's
    power-aware buzz values) so the ranking is recomputable on dropped rows.
    Players with games but no buzzes score 0.
    """
    games = observations.groupby("player_id")["game_id"].nunique()
    buzzes = observations[observations["z"] == "BUZZ"]
    points = buzzes["y"].astype(float) * POINTS_CORRECT + (
        1.0 - buzzes["y"].astype(float)
    ) * POINTS_NEG
    totals = points.groupby(buzzes["player_id"]).sum()
    totals = totals.reindex(games.index).fillna(0.0)
    return (totals / games).rename("actual_ppg")

