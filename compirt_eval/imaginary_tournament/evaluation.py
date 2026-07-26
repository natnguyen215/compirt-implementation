"""Simulate a tournament with freshly randomized teams and report player PPG.

Each game samples distinct fitted players, shuffles them into two teams, and
samples a packet of fitted tossups.  The Stage 1 posterior medians generate the
first buzzer and correctness.  A correct tossup scores +10 for the player and
draws a 0/10/20/30 bonus from the Stage 2 population-average predictive score
distribution; an incorrect buzz scores -5.  Bonuses affect team scores but not
individual PPG, matching quizbowl individual standings.

Powers, bouncebacks, overtime, substitutions, and score corrections are not
modeled.  Every sampled player is treated as active for the whole game.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from datasets import load_from_disk


from compirt_eval.diagnostics.match_simulation import _bonus_probability_pools
from compirt_eval.common.metrics import inverse_logit
from compirt_eval.scenario_a_tossups.parameters import (
    difficulty_adjustment_at,
    load_difficulty_adjustment_curves,
    load_difficulty_link,
    load_difficulty_scale,
)


POINTS_CORRECT = 10
POINTS_NEG = -5
BONUS_SCORES = np.asarray([0, 10, 20, 30], dtype=int)


@dataclass(frozen=True)
class TournamentInputs:
    """Saved fitted quantities and question lengths used by the simulator."""

    player_ids: np.ndarray
    theta: np.ndarray
    thresholds: np.ndarray
    tossups: pd.DataFrame
    question_lengths: pd.Series
    bonus_probability: np.ndarray
    adjustments: object
    difficulty_link: str
    difficulty_scale: float
    correctness_scale: float
    correctness_bias: float


def _numbered_columns(frame, prefix):
    """Return numbered columns such as theta_1, theta_2 in numeric order."""
    return sorted(
        (
            column
            for column in frame.columns
            if column.startswith(prefix)
            and column.removeprefix(prefix).isdigit()
        ),
        key=lambda column: int(column.removeprefix(prefix)),
    )


def _load_question_lengths(data_dir, split, fitted_tossup_ids):
    """Load token counts for fitted tossups in one HuggingFace data split."""
    dataset = load_from_disk(str(Path(data_dir) / "tossups"))
    if split not in dataset:
        choices = ", ".join(dataset.keys())
        raise ValueError(f"Unknown split {split!r}; choose one of: {choices}")
    questions = dataset[split].select_columns(["tossup_id", "tokens"]).to_pandas()
    questions["tossup_id"] = questions["tossup_id"].astype(str)
    questions = questions[questions["tossup_id"].isin(fitted_tossup_ids)].copy()
    questions["T_j"] = questions["tokens"].map(len).clip(lower=1)
    return questions.drop_duplicates("tossup_id").set_index("tossup_id")["T_j"]


def _normalize_tossup_weights(tossups):
    """Expose topic weights as relevance columns used by the common replay."""
    has_standard_weights = bool(
        _numbered_columns(tossups, "alpha_") or _numbered_columns(tossups, "r_")
    )
    topic_columns = _numbered_columns(tossups, "topic_weight_")
    if has_standard_weights or not topic_columns:
        return tossups
    return tossups.rename(
        columns={
            column: f"r_{column.removeprefix('topic_weight_')}"
            for column in topic_columns
        }
    )


def load_tournament_inputs(
    pyramidal_results, compositional_results, data_dir, split
):
    """Load and validate the two fitted stages needed for the tournament."""
    pyramidal_results = Path(pyramidal_results)
    compositional_results = Path(compositional_results)
    required = [
        pyramidal_results / "players.csv",
        pyramidal_results / "tossups.csv",
        compositional_results / "bonus_part_predictions.csv",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing fitted result files: " + ", ".join(missing))

    players = pd.read_csv(required[0], dtype={"player_id": str})
    tossups = pd.read_csv(required[1], dtype={"tossup_id": str}).set_index(
        "tossup_id"
    )
    tossups = _normalize_tossup_weights(tossups)
    theta_columns = _numbered_columns(players, "theta_")
    if not theta_columns or "c" not in players:
        raise ValueError("players.csv must contain c and numbered theta columns")

    question_lengths = _load_question_lengths(data_dir, split, tossups.index)
    tossups = tossups.loc[tossups.index.intersection(question_lengths.index)].copy()
    question_lengths = question_lengths.reindex(tossups.index)
    if tossups.empty:
        raise ValueError("No fitted tossups matched the requested data split")

    bonus_parts = pd.read_csv(required[2])
    _, _, bonus_probability = _bonus_probability_pools(bonus_parts)
    bonus_probability = np.asarray(bonus_probability, dtype=float)
    if bonus_probability.shape != (4,) or not np.isfinite(bonus_probability).all():
        raise ValueError("Stage 2 did not produce a valid four-score bonus distribution")
    bonus_probability /= bonus_probability.sum()

    scale, bias = 1.0, 0.0
    summary_path = pyramidal_results / "summary.json"
    if summary_path.exists():
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        scale = float(summary.get("correctness_scale", 1.0))
        bias = float(summary.get("correctness_bias", 0.0))

    return TournamentInputs(
        player_ids=players["player_id"].astype(str).to_numpy(),
        theta=players[theta_columns].to_numpy(dtype=float),
        thresholds=players["c"].to_numpy(dtype=float),
        tossups=tossups,
        question_lengths=question_lengths,
        bonus_probability=bonus_probability,
        adjustments=load_difficulty_adjustment_curves(pyramidal_results),
        difficulty_link=load_difficulty_link(pyramidal_results),
        difficulty_scale=load_difficulty_scale(pyramidal_results),
        correctness_scale=scale,
        correctness_bias=bias,
    )


def _question_curve(tossup_id, tossup, total_tokens, inputs):
    """Return one tossup's relevance vector and token-level difficulty."""
    weight_columns = _numbered_columns(inputs.tossups, "alpha_")
    if not weight_columns:
        weight_columns = _numbered_columns(inputs.tossups, "r_")
    theta_dimensions = inputs.theta.shape[1]
    if len(weight_columns) != theta_dimensions:
        raise ValueError(
            "Saved theta and tossup discrimination/relevance dimensions must match"
        )
    weights = tossup[weight_columns].to_numpy(dtype=float)
    relative = np.arange(1, total_tokens + 1, dtype=float) / total_tokens

    if {"beta", "gamma", "mu"}.issubset(tossup.index):
        beta = float(tossup["beta"])
        gamma = float(tossup["gamma"])
        mu = float(tossup["mu"])
        if inputs.difficulty_link == "tanh":
            difficulty = beta * np.tanh(gamma * (mu - relative))
        else:
            difficulty = beta * inverse_logit(gamma * (mu - relative))
    else:
        gamma_columns = _numbered_columns(inputs.tossups, "gamma_")
        mu_columns = _numbered_columns(inputs.tossups, "mu_")
        parameter_prefix = "bias_" if inputs.difficulty_link == "biased_tanh" else "beta_"
        parameter_columns = _numbered_columns(inputs.tossups, parameter_prefix)
        dimensions = {
            len(weights),
            len(parameter_columns),
            len(gamma_columns),
            len(mu_columns),
        }
        if len(dimensions) != 1 or not weights.size:
            raise ValueError(
                "Saved relevance, difficulty, gamma, and mu dimensions must match"
            )
        parameter = tossup[parameter_columns].to_numpy(dtype=float)[:, None]
        gamma = tossup[gamma_columns].to_numpy(dtype=float)[:, None]
        mu = tossup[mu_columns].to_numpy(dtype=float)[:, None]
        if inputs.difficulty_link == "biased_tanh":
            per_dimension = inputs.difficulty_scale * np.tanh(
                gamma * (mu - relative[None, :]) + parameter
            )
        elif inputs.difficulty_link == "tanh":
            per_dimension = parameter * np.tanh(
                gamma * (mu - relative[None, :])
            )
        else:
            per_dimension = parameter * inverse_logit(
                gamma * (mu - relative[None, :])
            )
        difficulty = weights @ per_dimension

    adjustment = difficulty_adjustment_at(
        inputs.adjustments, tossup_id, relative
    )
    if adjustment is not None:
        difficulty = difficulty + adjustment
    return weights, np.asarray(difficulty, dtype=float)


def _simulate_tossup(roster, question, inputs, question_cache, rng):
    """Draw one first-buzz outcome and return its player, team, and score."""
    tossup_id = str(question)
    if tossup_id not in question_cache:
        total_tokens = int(inputs.question_lengths.loc[tossup_id])
        question_cache[tossup_id] = _question_curve(
            tossup_id, inputs.tossups.loc[tossup_id], total_tokens, inputs
        )
    weights, difficulty = question_cache[tossup_id]
    skill = inputs.theta[roster] @ weights
    logits = skill[:, None] - difficulty[None, :]
    hazard = inverse_logit(logits - inputs.thresholds[roster, None])
    someone_hazard = 1.0 - np.prod(1.0 - hazard, axis=0)
    survival = np.concatenate(
        ([1.0], np.cumprod(1.0 - someone_hazard[:-1]))
    )
    no_buzz = np.prod(1.0 - hazard, axis=0)
    weights_at_token = hazard * (
        no_buzz[None, :] / np.clip(1.0 - hazard, 1e-6, None)
    )
    attribution = weights_at_token / np.clip(
        weights_at_token.sum(axis=0, keepdims=True), 1e-12, None
    )
    player_mass = survival[None, :] * someone_hazard[None, :] * attribution
    dead_mass = float(np.prod(1.0 - someone_hazard))
    outcome_probability = np.append(player_mass.reshape(-1), dead_mass)
    outcome_probability /= outcome_probability.sum()
    outcome = int(rng.choice(len(outcome_probability), p=outcome_probability))
    if outcome == player_mass.size:
        return None

    player_slot, token = divmod(outcome, player_mass.shape[1])
    correct_probability = float(
        inverse_logit(
            inputs.correctness_scale * logits[player_slot, token]
            + inputs.correctness_bias
        )
    )
    correct = bool(rng.random() < correct_probability)
    return {
        "player_index": int(roster[player_slot]),
        "team_slot": 0 if player_slot < len(roster) // 2 else 1,
        "points": POINTS_CORRECT if correct else POINTS_NEG,
        "correct": correct,
    }


def simulate_imaginary_tournament(
    inputs,
    games=1000,
    players_per_team=4,
    tossups_per_game=20,
    seed=42,
):
    """Run randomized games and return per-player PPG, games, and a summary."""
    if games < 1:
        raise ValueError("games must be at least one")
    if players_per_team < 1:
        raise ValueError("players_per_team must be at least one")
    roster_size = 2 * players_per_team
    if len(inputs.player_ids) < roster_size:
        raise ValueError(
            f"Need at least {roster_size} fitted players for two complete teams"
        )
    if tossups_per_game < 1:
        raise ValueError("tossups_per_game must be at least one")
    if len(inputs.tossups) < tossups_per_game:
        raise ValueError(
            f"Need at least {tossups_per_game} fitted tossups in the selected split"
        )

    rng = np.random.default_rng(seed)
    player_games = np.zeros(len(inputs.player_ids), dtype=int)
    player_points = np.zeros(len(inputs.player_ids), dtype=int)
    player_gets = np.zeros(len(inputs.player_ids), dtype=int)
    player_negs = np.zeros(len(inputs.player_ids), dtype=int)
    player_wins = np.zeros(len(inputs.player_ids), dtype=float)
    questions = inputs.tossups.index.to_numpy()
    question_cache = {}
    game_rows = []

    progress_interval = max(1, games // 20)
    for game_number in range(1, games + 1):
        roster = rng.choice(len(inputs.player_ids), size=roster_size, replace=False)
        packet = rng.choice(questions, size=tossups_per_game, replace=False)
        team_scores = np.zeros(2, dtype=int)
        tossup_scores = np.zeros(2, dtype=int)
        dead_tossups = 0
        player_games[roster] += 1

        for question in packet:
            result = _simulate_tossup(
                roster, question, inputs, question_cache, rng
            )
            if result is None:
                dead_tossups += 1
                continue
            player_index = result["player_index"]
            team_slot = result["team_slot"]
            points = result["points"]
            player_points[player_index] += points
            tossup_scores[team_slot] += points
            team_scores[team_slot] += points
            if result["correct"]:
                player_gets[player_index] += 1
                team_scores[team_slot] += int(
                    rng.choice(BONUS_SCORES, p=inputs.bonus_probability)
                )
            else:
                player_negs[player_index] += 1

        if team_scores[0] > team_scores[1]:
            winner = "team_1"
            player_wins[roster[:players_per_team]] += 1.0
        elif team_scores[1] > team_scores[0]:
            winner = "team_2"
            player_wins[roster[players_per_team:]] += 1.0
        else:
            winner = "tie"
            player_wins[roster] += 0.5
        game_rows.append(
            {
                "game_id": f"imaginary-{game_number:04d}",
                "team_1_player_ids": "|".join(
                    inputs.player_ids[roster[:players_per_team]]
                ),
                "team_2_player_ids": "|".join(
                    inputs.player_ids[roster[players_per_team:]]
                ),
                "team_1_tossup_points": int(tossup_scores[0]),
                "team_2_tossup_points": int(tossup_scores[1]),
                "team_1_score": int(team_scores[0]),
                "team_2_score": int(team_scores[1]),
                "winner": winner,
                "dead_tossups": dead_tossups,
            }
        )
        if game_number % progress_interval == 0 or game_number == games:
            print(
                f"Imaginary tournament: {game_number:,}/{games:,} games complete",
                flush=True,
            )

    appeared = player_games > 0
    player_frame = pd.DataFrame(
        {
            "player_id": inputs.player_ids[appeared],
            "games": player_games[appeared],
            "tossups_heard": player_games[appeared] * tossups_per_game,
            "gets": player_gets[appeared],
            "negs": player_negs[appeared],
            "tossup_points": player_points[appeared],
            "ppg": player_points[appeared] / player_games[appeared],
            "pp20": 20.0
            * player_points[appeared]
            / (player_games[appeared] * tossups_per_game),
            "win_percentage": player_wins[appeared] / player_games[appeared],
        }
    ).sort_values(["ppg", "tossup_points", "player_id"], ascending=[False, False, True])
    player_frame.insert(0, "rank", np.arange(1, len(player_frame) + 1))
    player_frame = player_frame.reset_index(drop=True)
    game_frame = pd.DataFrame(game_rows)
    total_player_games = int(player_games.sum())
    summary = {
        "seed": seed,
        "games": games,
        "players_per_team": players_per_team,
        "tossups_per_game": tossups_per_game,
        "eligible_players": len(inputs.player_ids),
        "players_appearing": int(appeared.sum()),
        "eligible_tossups": len(inputs.tossups),
        "aggregate_ppg": float(player_points.sum() / total_player_games),
        "mean_team_score": float(
            game_frame[["team_1_score", "team_2_score"]].to_numpy().mean()
        ),
        "dead_tossup_rate": float(game_frame["dead_tossups"].sum() / (games * tossups_per_game)),
        "top_player_id": str(player_frame.iloc[0]["player_id"]),
        "top_player_ppg": float(player_frame.iloc[0]["ppg"]),
    }
    return player_frame, game_frame, summary


def write_outputs(output_dir, player_frame, game_frame, summary):
    """Write the tournament's player table, game table, and summary."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    player_frame.to_csv(output_dir / "player_ppg.csv", index=False)
    game_frame.to_csv(output_dir / "games.csv", index=False)
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
