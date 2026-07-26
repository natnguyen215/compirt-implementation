"""Seeded quizbowl match-outcome diagnostic from the two fitted stages.

Each tossup has one first-buzz outcome (or is dead), a correct buzz scores +10
and draws a 0/10/20/30 bonus, and an incorrect buzz scores -5. Powers,
bouncebacks, overtime, and score corrections are outside this diagnostic. The
output is a model-derived winner forecast under these simplified scoring rules.
Pyro's ``Predictive`` runs this generative scoring process forward.
"""

from __future__ import annotations

import json
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyro
import pyro.distributions as dist
import torch
from pyro.infer import Predictive

from compirt_eval.common.figures import reliability_plot
from compirt_eval.common.metrics import inverse_logit
from compirt_eval.common.report_paths import csv_path, graph_path
from compirt_eval.scenario_a_tossups.parameters import (
    _supports_first_buzz_reconstruction,
    load_difficulty_adjustment_curves,
    load_difficulty_link,
)
from compirt_eval.scenario_a_tossups.timing import event_first_buzz_components
from compirt_eval.scenario_b_bonuses.metrics import bonus_ranked_probability_scores


SCORE_PROBABILITY_COLUMNS = [
    "probability_0",
    "probability_10",
    "probability_20",
    "probability_30",
]


@dataclass(frozen=True)
class _GameSimulationInputs:
    """Fitted quantities needed to simulate a single game's events."""

    players: pd.DataFrame
    tossups: pd.DataFrame
    predictions: pd.DataFrame
    team_bonus: dict
    tier_bonus: dict
    global_bonus: np.ndarray
    adjustments: dict
    link: str
    correctness_scale: float
    correctness_bias: float


def _bonus_probability_pools(parts):
    """Return team, tier, and global predicted bonus-score distributions."""
    scores = bonus_ranked_probability_scores(parts)
    if scores.empty:
        uniform = np.full(4, 0.25)
        return {}, {}, uniform
    metadata_columns = ["response_id", "team_id"]
    if "tier" in parts:
        metadata_columns.append("tier")
    metadata = parts[metadata_columns].drop_duplicates("response_id")
    scores = scores.merge(metadata, on="response_id", how="left")
    team = {
        str(key): group[SCORE_PROBABILITY_COLUMNS].mean().to_numpy(dtype=float)
        for key, group in scores.groupby("team_id")
    }
    tier = (
        {
            str(key): group[SCORE_PROBABILITY_COLUMNS].mean().to_numpy(dtype=float)
            for key, group in scores.groupby("tier")
        }
        if "tier" in scores
        else {}
    )
    global_distribution = scores[SCORE_PROBABILITY_COLUMNS].mean().to_numpy(dtype=float)
    return team, tier, global_distribution / global_distribution.sum()


def _print_game_progress(completed, total, next_percentage):
    """Print the latest newly reached 5% milestone and return the next one."""
    if total <= 0:
        return next_percentage
    completed_percentage = 100.0 * completed / total
    reached_percentage = min(100, int(completed_percentage // 5) * 5)
    if reached_percentage < next_percentage:
        return next_percentage
    print(
        f"Game simulation: {completed:,}/{total:,} games complete "
        f"({reached_percentage}%)",
        flush=True,
    )
    return reached_percentage + 5


def _load_simulation_inputs(pyramidal_results, compositional_results):
    """Load fitted stages and return ``None`` when simulation is unavailable."""
    paths = [
        pyramidal_results / "players.csv",
        pyramidal_results / "tossups.csv",
        pyramidal_results / "tossup_predictions.csv",
        compositional_results / "bonus_part_predictions.csv",
    ]
    if not all(path.exists() for path in paths):
        return None

    players = pd.read_csv(paths[0], dtype={"player_id": str}).set_index("player_id")
    tossups = pd.read_csv(paths[1], dtype={"tossup_id": str}).set_index("tossup_id")
    predictions = pd.read_csv(
        paths[2], dtype={"player_id": str, "tossup_id": str}
    )
    parts = pd.read_csv(paths[3])
    if predictions.empty or not _supports_first_buzz_reconstruction(players, tossups):
        return None

    team_bonus, tier_bonus, global_bonus = _bonus_probability_pools(parts)
    scale, bias = 1.0, 0.0
    summary_path = pyramidal_results / "summary.json"
    if summary_path.exists():
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        scale = float(summary.get("correctness_scale", 1.0))
        bias = float(summary.get("correctness_bias", 0.0))

    return _GameSimulationInputs(
        players=players,
        tossups=tossups,
        predictions=predictions,
        team_bonus=team_bonus,
        tier_bonus=tier_bonus,
        global_bonus=global_bonus,
        adjustments=load_difficulty_adjustment_curves(pyramidal_results),
        link=load_difficulty_link(pyramidal_results),
        correctness_scale=scale,
        correctness_bias=bias,
    )


def _event_simulation_inputs(event, inputs, game_teams):
    """Return one tossup's fitted distributions for the Pyro game model."""
    tossup_id = str(event["tossup_id"].iloc[0])
    if tossup_id not in inputs.tossups.index or not set(
        event["player_id"]
    ).issubset(inputs.players.index):
        return None

    components = event_first_buzz_components(
        event,
        inputs.players,
        inputs.tossups,
        inputs.adjustments,
        inputs.link,
    )
    first_buzz_mass = components["player_first_buzz_mass"]
    # The terminal no-buzz outcome is the last category in this categorical draw.
    outcome_probability = np.append(first_buzz_mass.reshape(-1), components["dead_mass"])
    outcome_probability /= outcome_probability.sum()
    raw_correct = components["correctness_probability"].reshape(-1)
    raw_logit = np.log(
        np.clip(raw_correct, 1e-8, 1 - 1e-8)
        / np.clip(1 - raw_correct, 1e-8, 1)
    )
    correct_probability = inverse_logit(
        inputs.correctness_scale * raw_logit + inputs.correctness_bias
    )
    event_tier = str(event["tier"].iloc[0]) if "tier" in event else "Unknown"
    player_team_slots = [
        game_teams.index(str(team_id)) if str(team_id) in game_teams else -1
        for team_id in components["team_ids"]
    ]
    team_slots = np.repeat(player_team_slots, first_buzz_mass.shape[1])
    bonus_probability = [
        inputs.team_bonus.get(
            team_id, inputs.tier_bonus.get(event_tier, inputs.global_bonus)
        )
        for team_id in game_teams
    ]
    return {
        "first_buzz": torch.as_tensor(outcome_probability, dtype=torch.float32),
        "correct": torch.as_tensor(correct_probability, dtype=torch.float32),
        "team_slot": torch.as_tensor(team_slots, dtype=torch.long),
        "bonus": torch.as_tensor(np.stack(bonus_probability), dtype=torch.float32),
    }


def _game_model(events):
    """Run the simplified match-scoring generative process once."""
    scores = None
    for event_index, event in enumerate(events):
        # Categories 0..n-1 are the per-player first buzzes; the final category
        # is the dead tossup, so 'buzzed' is false exactly when it is drawn.
        outcome = pyro.sample(
            f"first_buzz_{event_index}",
            dist.Categorical(probs=event["first_buzz"]),
        )
        if scores is None:
            scores = event["first_buzz"].new_zeros(outcome.shape + (2,))
        buzzed = outcome < len(event["correct"])
        # Clamp the dead category back onto a real player so the correctness /
        # team lookups stay in range; its contribution is masked out below.
        outcome = outcome.clamp(max=len(event["correct"]) - 1)
        team_slot = event["team_slot"][outcome]
        correct = pyro.sample(
            f"correct_{event_index}",
            dist.Bernoulli(probs=event["correct"][outcome]),
        )
        bonus_score = pyro.sample(
            f"bonus_{event_index}",
            dist.Categorical(probs=event["bonus"][team_slot.clamp(min=0)]),
        )
        # +10 plus the 0/10/20/30 bonus on a correct buzz, -5 on a neg.
        event_score = torch.where(correct.bool(), 10 + 10 * bonus_score, -5)
        for slot in range(2):
            # Credit the buzzing team only; dead tossups score nothing.
            scores[..., slot] += torch.where(
                buzzed & (team_slot == slot), event_score, 0
            )
    return scores


def _simulate_game(game_id, game, game_events, inputs, simulations):
    """Return one output row, or ``None`` when the game cannot be simulated."""
    game_teams = [str(value) for value in game["team_ids"]]
    actual_scores = np.asarray(game["final_scores"], dtype=float)
    if len(game_teams) != 2 or len(actual_scores) != 2:
        return None

    events = []
    for _, event in game_events.groupby("event_id", sort=False):
        simulation_inputs = _event_simulation_inputs(event, inputs, game_teams)
        if simulation_inputs is not None:
            events.append(simulation_inputs)
    if not events:
        return None

    scores = (
        Predictive(
            _game_model,
            num_samples=simulations,
            return_sites=("_RETURN",),
            parallel=True,
        )(events)["_RETURN"]
        .detach()
        .cpu()
        .numpy()
    )

    predicted_win_probability = float(
        (scores[:, 0] > scores[:, 1]).mean()
        + 0.5 * (scores[:, 0] == scores[:, 1]).mean()
    )
    actual_winner = (
        int(np.argmax(actual_scores)) if actual_scores[0] != actual_scores[1] else -1
    )
    predicted_winner = 0 if predicted_win_probability >= 0.5 else 1
    return {
        "game_id": game_id,
        "team_1_id": game_teams[0],
        "team_2_id": game_teams[1],
        "actual_team_1_score": actual_scores[0],
        "actual_team_2_score": actual_scores[1],
        "predicted_team_1_score": scores[:, 0].mean(),
        "predicted_team_2_score": scores[:, 1].mean(),
        "team_1_win_probability": predicted_win_probability,
        "actual_winner": "tie" if actual_winner < 0 else game_teams[actual_winner],
        "predicted_winner": game_teams[predicted_winner],
        "winner_correct": (
            np.nan if actual_winner < 0 else predicted_winner == actual_winner
        ),
        "usable_tossups": len(events),
        "simulations": simulations,
    }


def _match_metrics(frame, simulations):
    """Aggregate decisive-game winner accuracy and Brier score."""
    decisive = frame[frame["winner_correct"].notna()] if not frame.empty else frame
    if decisive.empty:
        return {}
    team_1_won = (
        decisive["actual_winner"].astype(str) == decisive["team_1_id"].astype(str)
    ).astype(float)
    return {
        "match_winner_accuracy": float(decisive["winner_correct"].astype(float).mean()),
        "match_winner_brier": float(
            np.mean((decisive["team_1_win_probability"] - team_1_won) ** 2)
        ),
        "match_games": len(decisive),
        "match_simulations_per_game": simulations,
    }


def _plot_match_predictions(frame, output_dir):
    """Plot win-probability reliability and simulated-versus-actual scores."""
    decisive = frame[frame["winner_correct"].notna()]
    if not decisive.empty:
        team_1_won = (
            decisive["actual_winner"].astype(str) == decisive["team_1_id"].astype(str)
        ).astype(float)
        reliability_plot(
            team_1_won,
            decisive["team_1_win_probability"],
            "Match winner reliability",
            graph_path(output_dir, "match_winner_reliability.png", "match"),
        )
    observed = pd.concat(
        [frame["actual_team_1_score"], frame["actual_team_2_score"]],
        ignore_index=True,
    )
    predicted = pd.concat(
        [frame["predicted_team_1_score"], frame["predicted_team_2_score"]],
        ignore_index=True,
    )
    fig, ax = plt.subplots(figsize=(6.5, 6.5))
    ax.scatter(observed, predicted, s=12, alpha=0.2)
    limit = 1.05 * max(float(observed.max()), float(predicted.max()), 1.0)
    ax.plot([0, limit], [0, limit], "--", color="0.5")
    ax.set(
        title=f"Simulated versus actual final scores ({len(observed):,} game-teams)",
        xlabel="Actual score",
        ylabel="Simulated expected score",
        xlim=(min(0.0, float(observed.min())), limit),
        ylim=(min(0.0, float(predicted.min())), limit),
    )
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, "match_score_predictions.png", "match"), dpi=160)
    plt.close(fig)


def simulate_match_winners(
    pyramidal_results,
    compositional_results,
    output_dir,
    games,
    simulations=500,
    seed=42,
):
    """Simulate final scores and report winner probability for each real game."""
    if simulations < 1:
        raise ValueError("simulations must be at least one")
    inputs = _load_simulation_inputs(pyramidal_results, compositional_results)
    if inputs is None:
        return {}, pd.DataFrame()

    pyro.set_rng_seed(seed)
    game_lookup = games.set_index("game_id")
    predictions = inputs.predictions[
        inputs.predictions["game_id"].isin(game_lookup.index)
    ]
    game_groups = predictions.groupby("game_id", sort=False)
    total_games = game_groups.ngroups
    print(
        f"Game simulation: {total_games:,} games, "
        f"{simulations:,} replicas per game",
        flush=True,
    )
    next_progress_percentage = 5
    rows = []
    for game_number, (game_id, game_events) in enumerate(game_groups, start=1):
        # Reaching the next group means the preceding game is fully processed,
        # including games skipped by a validation guard.
        if game_number > 1:
            next_progress_percentage = _print_game_progress(
                game_number - 1, total_games, next_progress_percentage
            )
        row = _simulate_game(
            game_id,
            game_lookup.loc[game_id],
            game_events,
            inputs,
            simulations,
        )
        if row is not None:
            rows.append(row)
    _print_game_progress(total_games, total_games, next_progress_percentage)
    frame = pd.DataFrame(rows)
    frame.to_csv(csv_path(output_dir, "game_predictions.csv"), index=False)
    if not frame.empty:
        _plot_match_predictions(frame, output_dir)
    return _match_metrics(frame, simulations), frame
