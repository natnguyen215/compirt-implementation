"""Randomized-roster, tossup-only tournaments using the shared token replay."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from datasets import load_from_disk

from compirt_eval.scenario_a_tossups.outcomes import replay_tossup


from compirt_eval.common.figures import numeric_columns, vector_weight_columns
from compirt_eval.common.metrics import inverse_logit
from compirt_eval.scenario_a_tossups.parameters import (
    _buzz_parameter_prefix,
    _parameter_columns,
    _saved_difficulty_components,
    _saved_difficulty_curve,
    difficulty_adjustment_at,
    load_difficulty_adjustment_curves,
    load_difficulty_link,
    load_difficulty_scale,
    load_terminal_intercepts,
    perception_slice_indices,
    sliced_perception_columns,
)


POINTS_CORRECT = 10
POINTS_NEG = -5


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
    terminal_intercepts: tuple[float, float] = (0.0, 0.0)
    perception_alpha: np.ndarray | None = None
    perception_beta: np.ndarray | None = None
    perceived_logit_alpha: np.ndarray | None = None
    perceived_logit_beta: np.ndarray | None = None


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
    has_standard_weights = bool(vector_weight_columns(tossups))
    topic_columns = numeric_columns(tossups, "topic_weight_")
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
    """Load Stage 1; the legacy compositional path is accepted but unused."""
    pyramidal_results = Path(pyramidal_results)
    required = [
        pyramidal_results / "players.csv",
        pyramidal_results / "tossups.csv",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing fitted result files: " + ", ".join(missing))

    players = pd.read_csv(required[0], dtype={"player_id": str})
    tossups = pd.read_csv(required[1], dtype={"tossup_id": str}).set_index(
        "tossup_id"
    )
    tossups = _normalize_tossup_weights(tossups)
    theta_columns = numeric_columns(players, "theta_")
    alpha_columns = numeric_columns(players, "alpha_")
    beta_columns = numeric_columns(players, "beta_")
    sliced_alpha_columns = sliced_perception_columns(players, "alpha")
    sliced_beta_columns = sliced_perception_columns(players, "beta")
    perceived_difficulty = bool(alpha_columns or beta_columns)
    sliced_perceived_difficulty = bool(
        sliced_alpha_columns or sliced_beta_columns
    )
    perceived_logit = {"alpha", "beta"}.issubset(players.columns)
    if not theta_columns or (
        "c" not in players
        and not perceived_logit
        and not (len(alpha_columns) == len(beta_columns) == len(theta_columns))
        and not (
            sliced_alpha_columns
            and sliced_beta_columns
            and all(
                len(columns) == len(theta_columns)
                for columns in sliced_alpha_columns + sliced_beta_columns
            )
        )
    ):
        raise ValueError(
            "players.csv must contain theta plus c, scalar alpha/beta, or matching "
            "numbered alpha/beta"
        )

    question_lengths = _load_question_lengths(data_dir, split, tossups.index)
    tossups = tossups.loc[tossups.index.intersection(question_lengths.index)].copy()
    question_lengths = question_lengths.reindex(tossups.index)
    if tossups.empty:
        raise ValueError("No fitted tossups matched the requested data split")

    scale, bias = 1.0, 0.0
    summary_path = pyramidal_results / "summary.json"
    if summary_path.exists():
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        scale = float(summary.get("correctness_scale", 1.0))
        bias = float(summary.get("correctness_bias", 0.0))

    return TournamentInputs(
        player_ids=players["player_id"].astype(str).to_numpy(),
        theta=players[theta_columns].to_numpy(dtype=float),
        thresholds=(
            players["c"].to_numpy(dtype=float)
            if "c" in players
            else np.zeros(len(players), dtype=float)
        ),
        tossups=tossups,
        question_lengths=question_lengths,
        bonus_probability=np.asarray([1.0, 0.0, 0.0, 0.0]),
        adjustments=load_difficulty_adjustment_curves(pyramidal_results),
        difficulty_link=load_difficulty_link(pyramidal_results),
        difficulty_scale=load_difficulty_scale(pyramidal_results),
        correctness_scale=scale,
        correctness_bias=bias,
        perception_alpha=(
            np.stack(
                [
                    players[columns].to_numpy(dtype=float)
                    for columns in sliced_alpha_columns
                ],
                axis=1,
            )
            if sliced_perceived_difficulty
            else (
                players[alpha_columns].to_numpy(dtype=float)
                if perceived_difficulty
                else None
            )
        ),
        perception_beta=(
            np.stack(
                [
                    players[columns].to_numpy(dtype=float)
                    for columns in sliced_beta_columns
                ],
                axis=1,
            )
            if sliced_perceived_difficulty
            else (
                players[beta_columns].to_numpy(dtype=float)
                if perceived_difficulty
                else None
            )
        ),
        terminal_intercepts=load_terminal_intercepts(pyramidal_results),
        perceived_logit_alpha=(
            players["alpha"].to_numpy(dtype=float) if perceived_logit else None
        ),
        perceived_logit_beta=(
            players["beta"].to_numpy(dtype=float) if perceived_logit else None
        ),
    )


def _question_curve(tossup_id, tossup, total_tokens, inputs):
    """Return branch-specific relevance and token-level difficulty.

    The difficulty replay itself is the shared Scenario A reader, so scalar,
    multidimensional, polynomial, and monotone fits are all handled by the same
    code the standard evaluator uses.
    """
    hazard_prefix = _buzz_parameter_prefix(inputs.tossups)
    correctness_columns = _parameter_columns(inputs.tossups)["alpha"]
    hazard_columns = _parameter_columns(inputs.tossups, hazard_prefix)["alpha"]
    if (
        len(correctness_columns) != inputs.theta.shape[1]
        or len(hazard_columns) != inputs.theta.shape[1]
    ):
        raise ValueError(
            "Saved theta and tossup discrimination/relevance dimensions must match"
        )
    relative = np.arange(1, total_tokens + 1, dtype=float) / total_tokens
    hazard_difficulty = _saved_difficulty_curve(
        tossup,
        relative,
        inputs.difficulty_link,
        inputs.difficulty_scale,
        hazard_prefix,
    )
    correctness_difficulty = _saved_difficulty_curve(
        tossup,
        relative,
        inputs.difficulty_link,
        inputs.difficulty_scale,
    )
    if hazard_difficulty is None or correctness_difficulty is None:
        raise ValueError(
            f"Saved parameters cannot reconstruct difficulty for tossup {tossup_id!r}"
        )
    adjustment = difficulty_adjustment_at(inputs.adjustments, tossup_id, relative)
    if adjustment is not None:
        hazard_difficulty = hazard_difficulty + adjustment
        correctness_difficulty = correctness_difficulty + adjustment
    per_dimension = None
    if inputs.perception_alpha is not None:
        components = _saved_difficulty_components(tossup, relative)
        if components is None:
            raise ValueError(
                f"Saved parameters cannot reconstruct dimensions for {tossup_id!r}"
            )
        per_dimension = components[0]
    result = (
        tossup[hazard_columns].to_numpy(dtype=float),
        tossup[correctness_columns].to_numpy(dtype=float),
        np.asarray(hazard_difficulty, dtype=float),
        np.asarray(correctness_difficulty, dtype=float),
    )
    return (*result, per_dimension) if per_dimension is not None else result


def _simulate_tossup(roster, question, inputs, question_cache, rng):
    """Replay one whole tossup and return all buzzes, including continuations."""
    tossup_id = str(question)
    if tossup_id not in question_cache:
        total_tokens = int(inputs.question_lengths.loc[tossup_id])
        question_cache[tossup_id] = _question_curve(
            tossup_id, inputs.tossups.loc[tossup_id], total_tokens, inputs
        )
    cached = question_cache[tossup_id]
    (
        hazard_weights,
        correctness_weights,
        hazard_difficulty,
        correctness_difficulty,
    ) = cached[:4]
    hazard_difficulty_by_dimension = cached[4] if len(cached) == 5 else None
    theta = inputs.theta[roster]
    hazard_skill = theta @ hazard_weights
    correctness_skill = theta @ correctness_weights
    if inputs.perceived_logit_alpha is not None:
        hazard_logits = (
            inputs.perceived_logit_alpha[roster, None]
            * (hazard_skill[:, None] - hazard_difficulty[None, :])
            + inputs.perceived_logit_beta[roster, None]
        )
    elif inputs.perception_alpha is not None:
        if inputs.perception_alpha.ndim == 3:
            relative = np.arange(1, hazard_difficulty.shape[0] + 1, dtype=float)
            relative /= hazard_difficulty.shape[0]
            slice_index = perception_slice_indices(relative)
            selected_alpha = inputs.perception_alpha[roster][:, slice_index, :]
            selected_beta = inputs.perception_beta[roster][:, slice_index, :]
            hazard_logits = np.sum(
                hazard_weights[None, None, :]
                * (
                    theta[:, None, :]
                    - selected_alpha
                    * hazard_difficulty_by_dimension.T[None, :, :]
                    + selected_beta
                ),
                axis=2,
            )
        else:
            hazard_logits = np.sum(
                hazard_weights[None, :, None]
                * (
                    theta[:, :, None]
                    - inputs.perception_alpha[roster, :, None]
                    * hazard_difficulty_by_dimension[None, :, :]
                    + inputs.perception_beta[roster, :, None]
                ),
                axis=1,
            )
    else:
        hazard_logits = (hazard_skill[:, None] - hazard_difficulty[None, :]
                         - inputs.thresholds[roster, None])
    end_correct, end_hazard = inputs.terminal_intercepts
    # Match the fitted reconstruction: perception families encode their own
    # hazard transform; the standard branch adds the terminal hazard intercept.
    if inputs.perceived_logit_alpha is None and inputs.perception_alpha is None:
        hazard_logits[:, -1] += end_hazard
    correct_logits = correctness_skill[:, None] - correctness_difficulty[None, :]
    correct_logits[:, -1] += end_correct
    correctness = inverse_logit(inputs.correctness_scale * correct_logits + inputs.correctness_bias)
    teams = np.asarray([str(i // (len(roster) // 2)) for i in range(len(roster))])
    _points, buzzes = replay_tossup(inputs.player_ids[roster], teams, hazard_logits, correctness, rng=rng)
    lookup = dict(zip(inputs.player_ids[roster].astype(str), roster))
    return [dict(buzz, player_index=int(lookup[buzz["player_id"]]), team_slot=int(buzz["team_id"]))
            for buzz in buzzes]


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
            if not result:
                dead_tossups += 1
                continue
            for buzz in result:
                player_index = buzz["player_index"]
                team_slot = buzz["team_slot"]
                points = int(buzz["points"])
                player_points[player_index] += points
                tossup_scores[team_slot] += points
                team_scores[team_slot] += points
                if buzz["correct"]:
                    player_gets[player_index] += 1
                elif points < 0:
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
        "evaluation_method": "token_threshold_replay",
        "buzz_tie_break": "seeded_uniform",
        "buzz_threshold": 0.5,
        "correctness_threshold": 0.5,
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
