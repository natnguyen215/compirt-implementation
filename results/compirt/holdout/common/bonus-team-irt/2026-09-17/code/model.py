"""Independent team and bonus-part parameters, fitted on training bonuses only."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pyro
import pyro.distributions as dist
import torch


def observations(tables):
    rows = []
    for response in tables["bonus_responses"].itertuples(index=False):
        if len(response.parts_correct) != 3 or response.total_points != 10 * sum(response.parts_correct):
            raise ValueError("Expected standard three-part, ten-point bonuses")
        for index, correct in enumerate(response.parts_correct):
            rows.append({
                "observation_id": f"{response.response_id}::part-{index + 1}",
                "response_id": response.response_id, "game_id": response.game_id,
                "team_id": response.team_id, "bonus_id": response.bonus_id,
                "bonus_part_id": f"{response.bonus_id}::part-{index + 1}",
                "part_index": index, "correct": float(correct),
                "total_points": response.total_points,
            })
    frame = pd.DataFrame(rows)
    frame = frame.merge(tables["games"][["game_id", "tournament_id"]],
                        on="game_id", validate="many_to_one")
    frame = frame.merge(tables["tournaments"][["tournament_id", "tier"]],
                        on="tournament_id", validate="many_to_one")
    return frame.merge(tables["bonuses"][["bonus_id", "category", "subcategory"]],
                       on="bonus_id", validate="many_to_one")


def training_tensors(frame, device):
    team_ids = sorted(frame.team_id.unique())
    part_ids = sorted(frame.bonus_part_id.unique())
    team_index = {value: index for index, value in enumerate(team_ids)}
    part_index = {value: index for index, value in enumerate(part_ids)}
    return {
        "team_ids": team_ids, "part_ids": part_ids,
        "team": torch.tensor(frame.team_id.map(team_index).to_numpy(), device=device),
        "part": torch.tensor(frame.bonus_part_id.map(part_index).to_numpy(), device=device),
        "y": torch.tensor(frame.correct.to_numpy(), dtype=torch.float32, device=device),
    }


def team_irt(data, dimensions):
    zero = data["y"].new_tensor(0.0)
    one = data["y"].new_tensor(1.0)
    with pyro.plate("teams", len(data["team_ids"])):
        theta = pyro.sample("theta", dist.Normal(zero, one).expand([dimensions]).to_event(1))
    with pyro.plate("parts", len(data["part_ids"])):
        alpha = pyro.sample("alpha", dist.Gamma(2 * one, 2 * one).expand([dimensions]).to_event(1))
        beta = pyro.sample("beta", dist.Normal(zero, one))
    logits = (theta[data["team"]] * alpha[data["part"]]).sum(-1) - beta[data["part"]]
    with pyro.plate("observations", len(data["y"])):
        pyro.sample("correct", dist.Bernoulli(logits=logits), obs=data["y"])


def predict(frame, parameters, team_ids, part_ids):
    """Replay saved medians; labels never enter parameter lookup or logits."""
    teams = pd.Index(team_ids).get_indexer(frame.team_id)
    parts = pd.Index(part_ids).get_indexer(frame.bonus_part_id)
    if (teams < 0).any() or (parts < 0).any():
        raise ValueError("Frozen prediction requires training team and part coverage")
    logits = (parameters["theta"][teams] * parameters["alpha"][parts]).sum(-1) - parameters["beta"][parts]
    return 1 / (1 + np.exp(-np.clip(logits, -60, 60)))


def matched_games(train, test, references):
    """Exclude whole games with unseen parameters or incomplete reference rows."""
    uncovered = ~test.team_id.isin(train.team_id) | ~test.bonus_part_id.isin(train.bonus_part_id)
    reasons = {game: {"unseen_team_or_part"} for game in test.loc[uncovered, "game_id"]}
    for name, reference in references.items():
        if reference.observation_id.duplicated().any():
            raise ValueError(f"Duplicate reference predictions: {name}")
        p = reference.predicted_correct
        if not np.isfinite(p).all() or not p.between(0, 1).all():
            raise ValueError(f"Invalid reference probabilities: {name}")
        shared = test.merge(reference, on="observation_id", suffixes=("", "_saved"), validate="one_to_one")
        for column in ("correct", "game_id", "response_id", "team_id", "bonus_part_id", "part_index"):
            if not shared[column].eq(shared[f"{column}_saved"]).all():
                raise ValueError(f"Reference labels or identity disagree: {name}, {column}")
        if not set(reference.observation_id) <= set(test.observation_id):
            raise ValueError(f"Reference contains observations outside the test fold: {name}")
        for game in test.loc[~test.observation_id.isin(reference.observation_id), "game_id"]:
            reasons.setdefault(game, set()).add(f"missing_{name}")
    return pd.DataFrame([{"game_id": game, "reason": ";".join(sorted(reason))}
                         for game, reason in sorted(reasons.items())], columns=["game_id", "reason"])
