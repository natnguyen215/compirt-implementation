"""Token-threshold tossup replays, recorded game scores, and player rankings."""

from __future__ import annotations

import json
import hashlib
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

from compirt_eval.common.metrics import inverse_logit
from compirt_eval.common.report_paths import csv_path
from compirt_eval.scenario_a_tossups.reconstruction import (
    _load_timing_evaluation_inputs,
    event_first_buzz_components,
)


POINTS_CORRECT = 10.0
POINTS_NEG = -5.0
NO_SCORE = "no_score"
NO_BUZZ = "no_buzz"
OUTCOME_SCHEMA_VERSION = 3
REPLAY_SEED = 42

OUTCOME_METRICS = (
    "first_buzzer_player_replay_accuracy",
    "first_buzzer_team_replay_accuracy",
    "tossup_scorer_player_replay_accuracy",
    "tossup_scorer_team_replay_accuracy",
    "tossup_game_winner_accuracy",
    "tossup_game_margin_mae",
    "tossup_game_zero_margin_mae",
    "tournament_player_ppg_spearman",
    "tournament_player_ppg_mae",
    "tournament_player_ppg_top10_overlap",
    "tournament_player_ppg_top10_random_overlap",
    "tournament_player_ppg_top10_adjusted_overlap",
)


def _recorded_outcome_rows(buzzes: pd.DataFrame) -> dict[str, dict]:
    """Return complete actual scoring sequences keyed by ``game::tossup``."""
    if buzzes is None or buzzes.empty:
        return {}
    required = {"game_id", "tossup_id", "player_id", "team_id", "value"}
    if not required.issubset(buzzes.columns):
        return {}
    ordered = buzzes.copy()
    if "token_position" not in ordered:
        ordered["token_position"] = 0
    if "buzz_id" in ordered:
        suffix = pd.to_numeric(
            ordered["buzz_id"].astype(str).str.rsplit("-", n=1).str[-1],
            errors="coerce",
        )
        ordered["_buzz_order"] = suffix.fillna(0)
    else:
        ordered["_buzz_order"] = np.arange(len(ordered))
    ordered = ordered.sort_values(
        ["game_id", "tossup_id", "token_position", "_buzz_order"],
        kind="stable",
    )
    result = {}
    for (game_id, tossup_id), event in ordered.groupby(
        ["game_id", "tossup_id"], sort=False
    ):
        first = event.iloc[0]
        positive = event[event["value"] > 0]
        scorer = positive.iloc[0] if not positive.empty else None
        result[f"{game_id}::{tossup_id}"] = {
            "first_player": str(first["player_id"]),
            "first_team": str(first["team_id"]),
            "first_value": float(first["value"]),
            "scorer_player": NO_SCORE if scorer is None else str(scorer["player_id"]),
            "scorer_team": NO_SCORE if scorer is None else str(scorer["team_id"]),
            "player_points": {
                str(key): float(value)
                for key, value in event.groupby("player_id")["value"].sum().items()
            },
            "player_teams": {
                str(row.player_id): str(row.team_id)
                for row in event.itertuples(index=False)
            },
            "team_points": {
                str(key): float(value)
                for key, value in event.groupby("team_id")["value"].sum().items()
            },
        }
    return result


def _saved_recorded_outcomes(predictions: pd.DataFrame) -> dict[str, dict]:
    """Read complete outcomes embedded by current observation builders."""
    required = {
        "actual_first_buzz_value",
        "actual_scorer_player_id",
        "actual_scorer_team_id",
        "actual_player_tossup_points",
        "actual_team_tossup_points",
    }
    if not required.issubset(predictions.columns):
        return {}
    result = {}
    for event_id, event in predictions.groupby("event_id", sort=False):
        buzz = event[event["z"] == "BUZZ"]
        first = None if buzz.empty else buzz.iloc[0]
        player_points = (
            event.groupby(event["player_id"].astype(str))["actual_player_tossup_points"]
            .first()
            .astype(float)
            .to_dict()
        )
        team_points = (
            event.groupby(event["team_id"].astype(str))["actual_team_tossup_points"]
            .first()
            .astype(float)
            .to_dict()
        )
        representative = event.iloc[0]
        result[str(event_id)] = {
            "first_player": NO_BUZZ if first is None else str(first["player_id"]),
            "first_team": NO_BUZZ if first is None else str(first["team_id"]),
            "first_value": float(representative["actual_first_buzz_value"]),
            "scorer_player": str(representative["actual_scorer_player_id"]),
            "scorer_team": str(representative["actual_scorer_team_id"]),
            "player_points": player_points,
            "player_teams": dict(
                zip(event["player_id"].astype(str), event["team_id"].astype(str))
            ),
            "team_points": team_points,
        }
    return result


@lru_cache(maxsize=16)
def _source_outcome_tables(split: str):
    """Cache raw buzz and game tables while backfilling many model families."""
    from compirt_data import load_hf_tables

    tables = load_hf_tables(split=split)
    return tables["tossup_buzzes"], tables["games"]


def _result_split(results_dir: Path) -> str | None:
    summary_path = Path(results_dir) / "summary.json"
    if not summary_path.exists():
        return None
    return json.loads(summary_path.read_text(encoding="utf-8")).get("split")


def _load_recorded_outcomes(results_dir: Path, predictions: pd.DataFrame):
    """Load literal outcomes, preferring the self-contained saved columns."""
    embedded = _saved_recorded_outcomes(predictions)
    if embedded:
        return embedded
    split = _result_split(results_dir)
    if not split:
        return {}
    try:
        buzzes, _games = _source_outcome_tables(str(split))
    except (FileNotFoundError, ImportError, KeyError, ValueError):
        return {}
    game_ids = set(predictions["game_id"].astype(str))
    buzzes = buzzes[buzzes["game_id"].astype(str).isin(game_ids)]
    return _recorded_outcome_rows(buzzes)


def _load_recorded_games(results_dir: Path, predictions: pd.DataFrame):
    split = _result_split(results_dir)
    if not split:
        return None
    try:
        _buzzes, games = _source_outcome_tables(str(split))
    except (FileNotFoundError, ImportError, KeyError, ValueError):
        return None
    game_ids = set(predictions["game_id"].astype(str))
    return games[games["game_id"].astype(str).isin(game_ids)]


def _calibration(results_dir: Path) -> tuple[float, float]:
    """Return saved correctness calibration, using identity when absent."""
    path = Path(results_dir) / "summary.json"
    if not path.exists():
        return 1.0, 0.0
    summary = json.loads(path.read_text(encoding="utf-8"))
    return (
        float(summary.get("correctness_scale", 1.0)),
        float(summary.get("correctness_bias", 0.0)),
    )


def _calibrate(probability: np.ndarray, scale: float, bias: float) -> np.ndarray:
    probability = np.clip(np.asarray(probability, dtype=float), 1e-8, 1 - 1e-8)
    logit = np.log(probability / (1.0 - probability))
    return inverse_logit(scale * logit + bias)


def replay_rng(event_id, seed=REPLAY_SEED):
    """Stable per-event randomness independent of grouping or worker order."""
    digest = hashlib.sha256(f"{seed}::{event_id}".encode("utf-8")).digest()
    return np.random.default_rng(int.from_bytes(digest[:16], "little"))


def replay_tossup(player_ids, team_ids, hazard_logits, correctness, rng=None):
    """Replay each token with a 0.5 buzz and correctness threshold.

    Same-token ties use seeded uniform choice over players sorted by ID,
    independent of roster row order. Randomness only resolves buzz ties.
    A miss locks out the whole team; reading resumes at the next token. Only
    the first, pre-terminal miss incurs -5. The terminal cell includes the
    post-reading window, so terminal misses and bounceback misses score zero.
    """
    player_ids = np.asarray(player_ids, dtype=str)
    team_ids = np.asarray(team_ids, dtype=str)
    logits = np.asarray(hazard_logits, dtype=float)
    correctness = np.asarray(correctness, dtype=float)
    if logits.ndim != 2 or logits.shape != correctness.shape:
        raise ValueError("Replay requires matching player-by-token hazard and correctness arrays")
    if logits.shape[0] != len(player_ids) or len(team_ids) != len(player_ids):
        raise ValueError("Replay roster and probability arrays must align")
    if len(set(player_ids)) != len(player_ids):
        raise ValueError("Replay roster must contain each player once")
    if np.isnan(logits).any() or not np.isfinite(correctness).all():
        raise ValueError("Replay probabilities must not contain missing values")
    if ((correctness < 0) | (correctness > 1)).any():
        raise ValueError("Correctness probabilities must be in [0, 1]")
    rng = np.random.default_rng(REPLAY_SEED) if rng is None else rng
    points = np.zeros(len(player_ids), dtype=float)
    buzzes = []
    locked_teams = set()
    order = np.argsort(player_ids, kind="stable")
    for token in range(logits.shape[1]):
        eligible = [i for i in order if team_ids[i] not in locked_teams and logits[i, token] >= 0.0]
        if not eligible:
            continue
        i = eligible[0] if len(eligible) == 1 else int(rng.choice(eligible))
        correct = bool(correctness[i, token] >= 0.5)
        value = POINTS_CORRECT if correct else (
            POINTS_NEG if not buzzes and token < logits.shape[1] - 1 else 0.0
        )
        points[i] += value
        buzzes.append({
            "player_id": str(player_ids[i]), "team_id": str(team_ids[i]),
            "token_position": token + 1, "correct": correct, "points": value,
            "buzz_probability": float(inverse_logit(logits[i, token])),
            "correctness_probability": float(correctness[i, token]),
        })
        if correct:
            break
        locked_teams.add(team_ids[i])
    return points, buzzes


def _event_outcomes(
    event_id, event, components, scale=1.0, bias=0.0, recorded=None
):
    """Return one event row and its per-player replayed/actual score rows."""
    phase0 = (
        event[~event["z"].astype(str).str.startswith("BOUNCE")]
        if "z" in event
        else event
    )
    if phase0.empty:
        return None, []

    player_ids = components["player_ids"].astype(str)
    team_ids = components["team_ids"].astype(str)
    has_team_labels = bool(
        "team_id" in phase0
        and phase0["team_id"].notna().all()
        and np.all(team_ids != "Unknown")
    )
    if "hazard_logits" not in components:
        raise ValueError("Token replay requires per-player hazard logits; first-buzz masses are insufficient")
    correctness = _calibrate(components["correctness_probability"], scale, bias)
    predicted_points, replay_buzzes = replay_tossup(
        player_ids, team_ids, components["hazard_logits"], correctness, rng=replay_rng(event_id)
    )
    first = replay_buzzes[0] if replay_buzzes else None
    scorer = next((buzz for buzz in replay_buzzes if buzz["correct"]), None)
    predicted_first_player = first["player_id"] if first else NO_BUZZ
    predicted_first_team = first["team_id"] if first else NO_BUZZ
    predicted_scorer_player = scorer["player_id"] if scorer else NO_SCORE
    predicted_scorer_team = scorer["team_id"] if scorer else NO_SCORE

    buzz = phase0[phase0["z"] == "BUZZ"]
    actual_player = NO_BUZZ
    actual_team = NO_BUZZ
    actual_scorer_player = NO_SCORE
    actual_scorer_team = NO_SCORE
    actual_points_by_player: dict[str, float] = {}
    actual_teams_by_player: dict[str, str] = {}
    actual_team_points: dict[str, float] = {}
    if recorded is not None:
        actual_player = str(recorded["first_player"])
        actual_team = str(recorded["first_team"])
        actual_scorer_player = str(recorded["scorer_player"])
        actual_scorer_team = str(recorded["scorer_team"])
        actual_points_by_player = dict(recorded["player_points"])
        actual_teams_by_player = dict(recorded.get("player_teams", {}))
        actual_team_points = dict(recorded["team_points"])
    elif not buzz.empty:
        observed = buzz.iloc[0]
        actual_player = str(observed["player_id"])
        actual_team = str(observed.get("team_id", "Unknown"))
        if "y" in observed and pd.notna(observed["y"]):
            correct = bool(int(observed["y"]))
            actual_points_by_player[actual_player] = (
                POINTS_CORRECT if correct else POINTS_NEG
            )
            if correct:
                actual_scorer_player = actual_player
                actual_scorer_team = actual_team
        actual_teams_by_player[actual_player] = actual_team
        actual_team_points[actual_team] = actual_points_by_player.get(
            actual_player, 0.0
        )

    tournament_id = (
        str(phase0["tournament_id"].iloc[0])
        if "tournament_id" in phase0
        else "Unknown"
    )
    game_id = str(phase0["game_id"].iloc[0])
    tossup_id = str(phase0["tossup_id"].iloc[0])

    event_row = {
        "event_id": event_id,
        "game_id": game_id,
        "tournament_id": tournament_id,
        "tossup_id": tossup_id,
        "actual_first_player_id": actual_player,
        "predicted_first_player_id": predicted_first_player,
        "actual_first_team_id": actual_team,
        "predicted_first_team_id": predicted_first_team,
        "first_player_correct": (
            np.nan
            if actual_player == NO_BUZZ
            else predicted_first_player == actual_player
        ),
        "first_team_correct": (
            np.nan
            if not has_team_labels or actual_team == NO_BUZZ
            else predicted_first_team == actual_team
        ),
        "actual_scorer_player_id": actual_scorer_player,
        "predicted_scorer_player_id": predicted_scorer_player,
        "actual_scorer_team_id": actual_scorer_team,
        "predicted_scorer_team_id": predicted_scorer_team,
        "scorer_player_correct": (
            predicted_scorer_player == actual_scorer_player
        ),
        "scorer_team_correct": (
            np.nan
            if not has_team_labels
            else predicted_scorer_team == actual_scorer_team
        ),
        "evaluation_method": "token_threshold_replay",
        "tossup_outcome_schema_version": OUTCOME_SCHEMA_VERSION,
        "replay_seed": REPLAY_SEED,
        "buzz_tie_break": "seeded_uniform",
        "buzz_threshold": 0.5,
        "correctness_threshold": 0.5,
        "predicted_first_token_position": first["token_position"] if first else np.nan,
        "predicted_buzz_sequence": json.dumps(replay_buzzes, sort_keys=True),
        "predicted_no_buzz": first is None,
        "predicted_no_score": scorer is None,
        "actual_team_points": json.dumps(actual_team_points, sort_keys=True),
        "roster_size": len(player_ids),
    }

    player_rows = []
    for index, (player_id, team_id) in enumerate(zip(player_ids, team_ids)):
        player_rows.append(
            {
                "event_id": event_id,
                "game_id": game_id,
                "tournament_id": tournament_id,
                "tossup_id": tossup_id,
                "player_id": player_id,
                "team_id": team_id,
                "predicted_tossup_points": predicted_points[index],
                "tossup_outcome_schema_version": OUTCOME_SCHEMA_VERSION,
                "actual_tossup_points": actual_points_by_player.get(player_id, 0.0),
            }
        )
    represented = set(player_ids)
    for player_id, actual_points in actual_points_by_player.items():
        if str(player_id) in represented:
            continue
        player_rows.append(
            {
                "event_id": event_id,
                "game_id": game_id,
                "tournament_id": tournament_id,
                "tossup_id": tossup_id,
                "player_id": str(player_id),
                "team_id": actual_teams_by_player.get(str(player_id), "Unknown"),
                "predicted_tossup_points": 0.0,
                "tossup_outcome_schema_version": OUTCOME_SCHEMA_VERSION,
                "actual_tossup_points": float(actual_points),
            }
        )
    return event_row, player_rows


def _winner(team_1, team_2, score_1, score_2) -> str:
    if score_1 > score_2:
        return team_1
    if score_2 > score_1:
        return team_2
    return "tie"


def game_predictions(
    player_predictions: pd.DataFrame,
    event_predictions: pd.DataFrame | None = None,
    official_games: pd.DataFrame | None = None,
) -> pd.DataFrame:
    """Aggregate literal recorded and replayed tossup points into games."""
    if player_predictions.empty:
        return pd.DataFrame()
    rows = []
    grouped = player_predictions.groupby(
        ["tournament_id", "game_id", "team_id"], as_index=False
    ).agg(
        actual_tossup_points=("actual_tossup_points", "sum"),
        predicted_tossup_points=("predicted_tossup_points", "sum"),
        usable_tossups=("event_id", "nunique"),
    )
    official_lookup = (
        official_games.assign(
            game_id=official_games["game_id"].astype(str)
        ).set_index("game_id")
        if official_games is not None and not official_games.empty
        else None
    )
    for (tournament_id, game_id), game in grouped.groupby(
        ["tournament_id", "game_id"], sort=False
    ):
        game = game.sort_values("team_id", kind="stable")
        if len(game) != 2:
            continue
        first, second = game.iloc[0], game.iloc[1]
        team_1, team_2 = str(first["team_id"]), str(second["team_id"])
        actual_1 = float(first["actual_tossup_points"])
        actual_2 = float(second["actual_tossup_points"])
        predicted_1 = float(first["predicted_tossup_points"])
        predicted_2 = float(second["predicted_tossup_points"])
        actual_winner = _winner(team_1, team_2, actual_1, actual_2)
        actual_margin = actual_1 - actual_2
        predicted_margin = predicted_1 - predicted_2
        predicted_winner = _winner(team_1, team_2, predicted_1, predicted_2)
        rows.append(
            {
                "tournament_id": tournament_id,
                "game_id": game_id,
                "team_1_id": team_1,
                "team_2_id": team_2,
                "actual_team_1_tossup_points": actual_1,
                "actual_team_2_tossup_points": actual_2,
                "predicted_team_1_tossup_points": predicted_1,
                "predicted_team_2_tossup_points": predicted_2,
                "actual_tossup_margin": actual_margin,
                "predicted_tossup_margin": predicted_margin,
                "evaluation_method": "token_threshold_replay",
                "tossup_outcome_schema_version": OUTCOME_SCHEMA_VERSION,
                "round": official_lookup.loc[str(game_id)].get("round", "Unknown")
                if official_lookup is not None and str(game_id) in official_lookup.index
                else "Unknown",
                "absolute_tossup_margin_error": abs(
                    predicted_margin - actual_margin
                ),
                "actual_tossup_winner": actual_winner,
                "predicted_tossup_winner": predicted_winner,
                "winner_correct": (
                    np.nan
                    if actual_winner == "tie"
                    else predicted_winner == actual_winner
                ),
                "usable_tossups": int(
                    min(first["usable_tossups"], second["usable_tossups"])
                ),
            }
        )
    return pd.DataFrame(rows)


def rank_player_totals(totals: pd.DataFrame):
    """Rank pre-aggregated tournament/player point and game totals."""
    if totals.empty:
        return pd.DataFrame(), pd.DataFrame()
    totals = totals.copy()
    totals["tossup_outcome_schema_version"] = OUTCOME_SCHEMA_VERSION
    totals["actual_ppg"] = totals["actual_tossup_points"] / totals["games"]
    totals["predicted_ppg"] = totals["predicted_tossup_points"] / totals["games"]

    leaderboard_rows = []
    metric_rows = []
    for tournament_id, tournament in totals.groupby("tournament_id", sort=True):
        tournament = tournament.copy()
        actual_order = tournament.sort_values(
            ["actual_ppg", "actual_tossup_points", "player_id"],
            ascending=[False, False, True], kind="stable",
        ).index
        predicted_order = tournament.sort_values(
            ["predicted_ppg", "predicted_tossup_points", "player_id"],
            ascending=[False, False, True], kind="stable",
        ).index
        tournament["actual_rank"] = pd.Series(
            np.arange(1, len(tournament) + 1), index=actual_order
        )
        tournament["predicted_rank"] = pd.Series(
            np.arange(1, len(tournament) + 1), index=predicted_order
        )
        tournament = tournament.sort_values("predicted_rank", kind="stable")
        leaderboard_rows.extend(tournament.to_dict("records"))

        count = len(tournament)
        correlation = np.nan
        if (
            count >= 2
            and tournament["actual_ppg"].nunique() > 1
            and tournament["predicted_ppg"].nunique() > 1
        ):
            correlation = float(
                spearmanr(
                    tournament["actual_ppg"], tournament["predicted_ppg"]
                ).statistic
            )
        cutoff = min(10, count)
        actual_top = set(tournament.nsmallest(cutoff, "actual_rank")["player_id"])
        predicted_top = set(
            tournament.nsmallest(cutoff, "predicted_rank")["player_id"]
        )
        random_overlap = cutoff / count
        overlap_rate = len(actual_top & predicted_top) / cutoff
        adjusted_overlap = (
            (overlap_rate - random_overlap) / (1.0 - random_overlap)
            if random_overlap < 1.0
            else np.nan
        )
        metric_rows.append(
            {
                "tournament_id": tournament_id,
                "players": count,
                "ppg_spearman": correlation,
                "ppg_mae": float(
                    (tournament["predicted_ppg"] - tournament["actual_ppg"])
                    .abs()
                    .mean()
                ),
                "top10_cutoff": cutoff,
                "top10_overlap_count": len(actual_top & predicted_top),
                "top10_overlap_rate": overlap_rate,
                "top10_random_overlap_rate": random_overlap,
                "top10_adjusted_overlap_rate": adjusted_overlap,
            }
        )
    return pd.DataFrame(leaderboard_rows), pd.DataFrame(metric_rows)


def player_leaderboards(player_predictions: pd.DataFrame):
    """Return tournament player PPG rows and per-tournament ranking metrics."""
    if player_predictions.empty:
        return pd.DataFrame(), pd.DataFrame()
    games = (
        player_predictions[["tournament_id", "player_id", "game_id"]]
        .drop_duplicates()
        .groupby(["tournament_id", "player_id"])
        .size()
        .rename("games")
    )
    totals = (
        player_predictions.groupby(["tournament_id", "player_id"], as_index=True)
        .agg(
            actual_tossup_points=("actual_tossup_points", "sum"),
            predicted_tossup_points=("predicted_tossup_points", "sum"),
        )
        .join(games)
        .reset_index()
    )
    return rank_player_totals(totals)


def _summary(events, games, ranking_metrics) -> dict[str, float | int]:
    summary: dict[str, float | int] = {
        **{name: np.nan for name in OUTCOME_METRICS},
        "tossup_outcome_schema_version": OUTCOME_SCHEMA_VERSION,
        "tossup_outcome_events": len(events),
        "tossup_replay_seed": REPLAY_SEED,
    }
    if not events.empty:
        for column, name in (
            ("first_player_correct", "first_buzzer_player_replay_accuracy"),
            ("first_team_correct", "first_buzzer_team_replay_accuracy"),
            ("scorer_player_correct", "tossup_scorer_player_replay_accuracy"),
            ("scorer_team_correct", "tossup_scorer_team_replay_accuracy"),
        ):
            eligible = events[column].dropna()
            summary[name] = (
                float(eligible.astype(float).mean()) if len(eligible) else np.nan
            )
            summary[f"{name}_events"] = int(len(eligible))
    if not games.empty:
        decisive = games["winner_correct"].dropna()
        summary.update(
            tossup_game_winner_accuracy=(
                float(decisive.astype(float).mean()) if len(decisive) else np.nan
            ),
            tossup_game_winner_accuracy_games=int(len(decisive)),
            tossup_game_margin_mae=float(
                games["absolute_tossup_margin_error"].mean()
            ),
            tossup_game_margin_mae_games=int(len(games)),
            tossup_game_zero_margin_mae=float(
                games["actual_tossup_margin"].abs().mean()
            ),
        )
    if not ranking_metrics.empty:
        summary.update(
            tournament_player_ppg_spearman=float(
                ranking_metrics["ppg_spearman"].mean()
            ),
            tournament_player_ppg_mae=float(ranking_metrics["ppg_mae"].mean()),
            tournament_player_ppg_top10_overlap=float(
                ranking_metrics["top10_overlap_rate"].mean()
            ),
            tournament_player_ppg_top10_random_overlap=float(
                ranking_metrics["top10_random_overlap_rate"].mean()
            ),
            tournament_player_ppg_top10_adjusted_overlap=float(
                ranking_metrics["top10_adjusted_overlap_rate"].mean()
            ),
            tournament_player_ppg_tournaments=int(len(ranking_metrics)),
        )
    return summary


def round_metrics(games):
    """Summarize the same replayed games within recorded tournament rounds."""
    if games.empty:
        return pd.DataFrame()
    return games.groupby(["tournament_id", "round"], as_index=False).agg(
        games=("game_id", "nunique"),
        tossup_game_winner_accuracy=("winner_correct", "mean"),
        tossup_game_winner_accuracy_games=("winner_correct", "count"),
        tossup_game_margin_mae=("absolute_tossup_margin_error", "mean"),
    )


def evaluate_tossup_outcomes(
    results_dir,
    output_dir=None,
    recorded_buzzes=None,
    official_games=None,
):
    """Evaluate saved Stage-1 outcomes and optionally write audit artifacts."""
    results_dir = Path(results_dir)
    inputs = _load_timing_evaluation_inputs(results_dir)
    if inputs is None:
        return {}, pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    scale, bias = _calibration(results_dir)
    recorded_outcomes = (
        _recorded_outcome_rows(recorded_buzzes)
        if recorded_buzzes is not None
        else _load_recorded_outcomes(results_dir, inputs.predictions)
    )
    if official_games is None:
        official_games = _load_recorded_games(results_dir, inputs.predictions)
    event_rows = []
    player_rows = []
    reconstruction_cache = {}
    incomplete_games = set()
    for event_id, event in inputs.predictions.groupby("event_id", sort=False):
        phase0 = event[~event["z"].astype(str).str.startswith("BOUNCE")]
        if phase0.empty:
            continue
        game_key = (str(phase0["tournament_id"].iloc[0]), str(phase0["game_id"].iloc[0]))
        # A first-buzz correctness label cannot recover late misses or the
        # opponent's recorded bounceback. Never use that proxy for game truth.
        if str(event_id) not in recorded_outcomes and (phase0["z"] == "BUZZ").any():
            incomplete_games.add(game_key)
            continue
        if "team_id" not in phase0 or phase0["team_id"].isna().any() or phase0["team_id"].nunique() != 2:
            incomplete_games.add(game_key)
            continue
        tossup_id = str(phase0["tossup_id"].iloc[0])
        player_ids = set(phase0["player_id"].astype(str))
        if tossup_id not in inputs.tossups.index or not player_ids.issubset(
            inputs.players.index
        ):
            incomplete_games.add(game_key)
            continue
        components = event_first_buzz_components(
            event,
            inputs.players,
            inputs.tossups,
            inputs.adjustments,
            inputs.link,
            inputs.buzz_parameter_prefix,
            inputs.difficulty_scale,
            inputs.terminal_intercepts,
            reconstruction_cache=reconstruction_cache,
        )
        event_row, rows = _event_outcomes(
            event_id,
            event,
            components,
            scale,
            bias,
            recorded=recorded_outcomes.get(str(event_id)),
        )
        if event_row is not None:
            event_rows.append(event_row)
            player_rows.extend(rows)
    events = pd.DataFrame(event_rows)
    players = pd.DataFrame(player_rows)
    # Exclude entire incomplete games so PPG never treats a partial game as
    # a full denominator. Include dead tossups in the event count.
    if not events.empty:
        counts = events.groupby(["tournament_id", "game_id"])["event_id"].nunique()
        if official_games is not None and "tossups_read" in official_games:
            expected_counts = dict(zip(official_games["game_id"].astype(str), official_games["tossups_read"]))
            for key, count in counts.items():
                expected = expected_counts.get(str(key[1]))
                if pd.notna(expected) and count != int(expected):
                    incomplete_games.add(key)
        if incomplete_games:
            events = events.loc[[
                (str(row.tournament_id), str(row.game_id)) not in incomplete_games
                for row in events.itertuples(index=False)
            ]].reset_index(drop=True)
            players = players.loc[[
                (str(row.tournament_id), str(row.game_id)) not in incomplete_games
                for row in players.itertuples(index=False)
            ]].reset_index(drop=True)
    games = game_predictions(players, events, official_games)
    leaderboard, ranking_metrics = player_leaderboards(players)
    summary = _summary(events, games, ranking_metrics)
    summary["tossup_replay_incomplete_games"] = len(incomplete_games)
    if output_dir is not None:
        output_dir = Path(output_dir)
        events.to_csv(
            csv_path(output_dir, "tossup_outcome_predictions.csv"), index=False
        )
        players.to_csv(
            csv_path(output_dir, "tossup_player_predictions.csv"), index=False
        )
        games.to_csv(
            csv_path(output_dir, "tossup_game_predictions.csv"), index=False
        )
        # Preserve the standard game artifact names used by all entry points.
        games.to_csv(csv_path(output_dir, "game_predictions.csv"), index=False)
        game_summary = {key: value for key, value in summary.items()
                        if key.startswith("tossup_game_") or key == "tossup_outcome_schema_version"}
        pd.DataFrame([game_summary]).to_csv(csv_path(output_dir, "game_metrics.csv"), index=False)
        round_metrics(games).to_csv(
            csv_path(output_dir, "tossup_round_metrics.csv"), index=False
        )
        leaderboard.to_csv(
            csv_path(output_dir, "player_ppg_leaderboard.csv"), index=False
        )
        ranking_metrics.to_csv(
            csv_path(output_dir, "player_ranking_metrics.csv"), index=False
        )
        pd.DataFrame([summary]).to_csv(
            csv_path(output_dir, "tossup_outcome_metrics.csv"), index=False
        )
    return summary, events, players, games, leaderboard
