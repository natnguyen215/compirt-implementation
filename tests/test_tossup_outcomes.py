"""Tests for recorded tossup ownership, game, and PPG metrics."""

import json

import numpy as np
import pandas as pd
import pytest

from compirt_eval.scenario_a_tossups.outcomes import (
    NO_SCORE,
    NO_BUZZ,
    replay_tossup,
    replay_rng,
    round_metrics,
    _event_outcomes,
    _recorded_outcome_rows,
    game_predictions,
    player_leaderboards,
    rank_player_totals,
)


def test_recorded_outcome_uses_literal_values_and_bounceback_scorer() -> None:
    buzzes = pd.DataFrame(
        {
            "buzz_id": ["g::buzz-1", "g::buzz-2"],
            "game_id": ["g", "g"],
            "tossup_id": ["q", "q"],
            "player_id": ["p1", "p2"],
            "team_id": ["a", "b"],
            "token_position": [2, 4],
            "value": [-5, 10],
        }
    )

    outcome = _recorded_outcome_rows(buzzes)["g::q"]

    assert outcome["first_player"] == "p1"
    assert outcome["scorer_player"] == "p2"
    assert outcome["player_points"] == {"p1": -5.0, "p2": 10.0}
    assert outcome["team_points"] == {"a": -5.0, "b": 10.0}


def event_frame():
    return pd.DataFrame({
        "game_id": ["g", "g"], "tournament_id": ["t", "t"],
        "tossup_id": ["q", "q"], "player_id": ["p1", "p2"],
        "team_id": ["a", "b"], "z": ["BUZZ", "CENSORED"],
        "y": [0.0, np.nan], "t_star": [1, 1],
    })


def test_event_replays_earliest_threshold_not_integrated_argmax():
    components = {
        "player_ids": np.asarray(["p1", "p2"]),
        "team_ids": np.asarray(["a", "b"]),
        # These diagnostic masses deliberately disagree with the token replay.
        "player_first_buzz_mass": np.asarray([[0.8, 0, 0], [0.1, 0, 0]]),
        "dead_mass": 0.1,
        "hazard_logits": np.asarray([[-1, -1, 1], [-1, 0, 2]]),
        "correctness_probability": np.asarray([[1, 1, 1], [0, 0.5, 1]]),
    }
    outcome, rows = _event_outcomes("g::q", event_frame(), components)
    assert outcome["predicted_first_player_id"] == "p2"
    assert outcome["predicted_first_team_id"] == "b"
    assert outcome["predicted_scorer_player_id"] == "p2"
    assert outcome["predicted_first_token_position"] == 2
    assert [row["predicted_tossup_points"] for row in rows] == [0, 10]
    changed_truth = event_frame().assign(t_star=3, y=1)
    changed, _ = _event_outcomes("g::q", changed_truth, components)
    assert changed["predicted_buzz_sequence"] == outcome["predicted_buzz_sequence"]


def test_bounceback_locks_entire_team_and_uses_later_correctness():
    points, buzzes = replay_tossup(
        ["p1", "p2", "p3"], ["a", "a", "b"],
        [[0, 2, 2], [-1, 5, 5], [-1, -1, 0]],
        [[0.49, 1, 1], [1, 1, 1], [0, 0, 0.5]],
    )
    assert points.tolist() == [-5, 0, 10]
    assert [buzz["player_id"] for buzz in buzzes] == ["p1", "p3"]
    assert [buzz["token_position"] for buzz in buzzes] == [1, 3]


@pytest.mark.parametrize("logits,correctness,expected", [
    ([[0, 0, 0], [-1, 0, 0]], [[0, 0, 0], [0, 0, 0]], [-5, 0]),
    ([[-1, -1, 0], [-1, -1, -1]], [[0, 0, 0], [1, 1, 1]], [0, 0]),
    ([[-0.01]*3, [-0.01]*3], [[1]*3, [1]*3], [0, 0]),
])
def test_misses_terminal_and_subthreshold_dead_question(logits, correctness, expected):
    points, _ = replay_tossup(["p1", "p2"], ["a", "b"], logits, correctness)
    assert points.tolist() == expected


def test_same_token_ties_are_seeded_uniform_and_ignore_roster_order():
    winners = set()
    for event_id in range(30):
        outcomes = []
        for ids, logits in [(["z", "a"], [[10], [0]]), (["a", "z"], [[0], [10]])]:
            points, buzzes = replay_tossup(ids, ids, logits, [[1], [1]], rng=replay_rng(event_id))
            outcomes.append(buzzes[0]["player_id"])
            assert points.sum() == 10
        assert outcomes[0] == outcomes[1]
        winners.add(outcomes[0])
    # Both eligible players win ties; the highest probability or lowest ID is
    # not a privileged winner. Different event keys get independent draws.
    assert winners == {"a", "z"}


def test_no_threshold_crossing_predicts_no_buzz_even_with_high_total_buzz_mass():
    components = {"player_ids": np.asarray(["p1", "p2"]),
                  "team_ids": np.asarray(["a", "b"]),
                  "hazard_logits": np.full((2, 20), -0.01),
                  "correctness_probability": np.ones((2, 20))}
    outcome, _ = _event_outcomes("g::q", event_frame(), components)
    assert outcome["predicted_first_player_id"] == NO_BUZZ
    assert outcome["predicted_scorer_player_id"] == NO_SCORE
    assert json.loads(outcome["predicted_buzz_sequence"]) == []


def test_replay_requires_logits_instead_of_falling_back_to_argmax():
    with pytest.raises(ValueError, match="hazard logits"):
        _event_outcomes("g::q", event_frame(), {
            "player_ids": np.asarray(["p1", "p2"]),
            "team_ids": np.asarray(["a", "b"]),
        })


def test_calibration_is_applied_at_replayed_buzz():
    components = {"player_ids": np.asarray(["p1", "p2"]),
                  "team_ids": np.asarray(["a", "b"]),
                  "hazard_logits": np.asarray([[0, -1], [-1, -1]]),
                  "correctness_probability": np.full((2, 2), 0.4)}
    _, raw = _event_outcomes("g::q", event_frame(), components)
    _, calibrated = _event_outcomes("g::q", event_frame(), components, bias=1)
    assert raw[0]["predicted_tossup_points"] == -5
    assert calibrated[0]["predicted_tossup_points"] == 10


def test_game_predictions_use_tossup_only_margin_and_exclude_actual_ties() -> None:
    players = pd.DataFrame(
        [
            {
                "tournament_id": "t", "game_id": "g1", "event_id": "e1",
                "team_id": "a", "actual_tossup_points": 10,
                "predicted_tossup_points": 7,
            },
            {
                "tournament_id": "t", "game_id": "g1", "event_id": "e1",
                "team_id": "b", "actual_tossup_points": -5,
                "predicted_tossup_points": 1,
            },
            {
                "tournament_id": "t", "game_id": "g2", "event_id": "e2",
                "team_id": "a", "actual_tossup_points": 0,
                "predicted_tossup_points": 2,
            },
            {
                "tournament_id": "t", "game_id": "g2", "event_id": "e2",
                "team_id": "b", "actual_tossup_points": 0,
                "predicted_tossup_points": 1,
            },
        ]
    )

    games = game_predictions(players).set_index("game_id")

    assert games.loc["g1", "actual_tossup_margin"] == 15
    assert games.loc["g1", "predicted_tossup_margin"] == 6
    assert games.loc["g1", "absolute_tossup_margin_error"] == 9
    assert bool(games.loc["g1", "winner_correct"])
    assert pd.isna(games.loc["g2", "winner_correct"])


def test_games_and_rounds_use_replayed_points_even_if_legacy_pmf_disagrees():
    players = pd.DataFrame([
        {"tournament_id": "t", "game_id": "g", "event_id": "g::q", "team_id": "a",
         "actual_tossup_points": -5, "predicted_tossup_points": -5},
        {"tournament_id": "t", "game_id": "g", "event_id": "g::q", "team_id": "b",
         "actual_tossup_points": 10, "predicted_tossup_points": 10},
    ])
    events = pd.DataFrame({"tournament_id": ["t"], "game_id": ["g"],
                           "predicted_margin_pmf": [json.dumps({"10": 1})]})
    official = pd.DataFrame({"game_id": ["g"], "round": ["round1"]})
    games = game_predictions(players, events, official)
    game = games.iloc[0]
    assert game["predicted_tossup_winner"] == "b"
    assert game["predicted_tossup_margin"] == -15
    rounds = round_metrics(games)
    assert rounds.iloc[0]["round"] == "round1"
    assert rounds.iloc[0]["tossup_game_winner_accuracy"] == 1
    assert rounds.iloc[0]["tossup_game_margin_mae"] == 0


def test_player_ppg_leaderboard_credits_unique_games_and_ranks_deterministically() -> None:
    rows = []
    for event_id, game_id in (("e1", "g1"), ("e2", "g1"), ("e3", "g2")):
        rows.extend(
            [
                {
                    "tournament_id": "t", "game_id": game_id,
                    "event_id": event_id, "player_id": "p1",
                    "actual_tossup_points": 10, "predicted_tossup_points": 2,
                },
                {
                    "tournament_id": "t", "game_id": game_id,
                    "event_id": event_id, "player_id": "p2",
                    "actual_tossup_points": 0, "predicted_tossup_points": 4,
                },
            ]
        )

    leaderboard, metrics = player_leaderboards(pd.DataFrame(rows))
    leaderboard = leaderboard.set_index("player_id")

    assert leaderboard.loc["p1", "games"] == 2
    assert leaderboard.loc["p1", "actual_ppg"] == 15
    assert leaderboard.loc["p1", "actual_rank"] == 1
    assert leaderboard.loc["p2", "predicted_rank"] == 1
    assert metrics.iloc[0]["ppg_spearman"] == pytest.approx(-1)

    tied, tied_metrics = rank_player_totals(
        pd.DataFrame(
            {
                "tournament_id": ["t", "t"],
                "player_id": ["z", "a"],
                "actual_tossup_points": [0, 0],
                "predicted_tossup_points": [0, 0],
                "games": [1, 1],
            }
        )
    )
    assert tied.sort_values("predicted_rank")["player_id"].tolist() == ["a", "z"]
    assert pd.isna(tied_metrics.iloc[0]["ppg_spearman"])


def saved_replay_fixture(tmp_path):
    from compirt_eval.scenario_a_tossups.outcomes import evaluate_tossup_outcomes

    results = tmp_path / "pyramidal"
    results.mkdir()
    pd.DataFrame({"player_id": ["p1", "p2"], "theta_1": [-1, 1], "c": [-3, 0.8]}).to_csv(
        results / "players.csv", index=False
    )
    pd.DataFrame({
        "tossup_id": ["q", "dead"], "alpha_1": [1, 1],
        "beta": [2, 100], "gamma": [8, 8], "mu": [0.5, 2],
    }).to_csv(results / "tossups.csv", index=False)
    frames = []
    for game, question in [("g1", "q"), ("g1", "dead"), ("g2", "q")]:
        frame = event_frame().assign(game_id=game, tossup_id=question, event_id=f"{game}::{question}", T_j=4)
        if question == "dead":
            frame["z"] = "NO-BUZZ"
            frame["y"] = np.nan
        frames.append(frame)
    pd.concat(frames).to_csv(results / "tossup_predictions.csv", index=False)
    buzzes = pd.DataFrame({
        "game_id": ["g1", "g1", "g2"], "tossup_id": ["q"] * 3,
        "player_id": ["p1", "p2", "p1"], "team_id": ["a", "b", "a"],
        "token_position": [1, 4, 1], "value": [-5, 10, 10],
    })
    official = pd.DataFrame({
        "game_id": ["g1", "g2"], "tournament_id": ["t", "t"],
        "tossups_read": [2, 1], "round": [1, 2],
    })
    return evaluate_tossup_outcomes, results, buzzes, official


def test_saved_game_replay_drives_scores_ppg_rounds_and_exports(tmp_path):
    evaluate, results, buzzes, official = saved_replay_fixture(tmp_path)
    summary, events, players, games, leaderboard = evaluate(
        results, tmp_path / "evaluation", recorded_buzzes=buzzes, official_games=official
    )
    assert len(events) == 3  # includes the dead question
    assert len(games) == 2
    assert summary["tossup_replay_incomplete_games"] == 0
    assert summary["tossup_game_winner_accuracy"] == 0.5
    assert summary["tossup_game_margin_mae"] == 12.5
    leaderboard = leaderboard.set_index("player_id")
    assert leaderboard.loc["p1", "predicted_ppg"] == -5
    assert leaderboard.loc["p2", "predicted_ppg"] == 10
    assert leaderboard.loc["p1", "actual_ppg"] == 2.5
    assert leaderboard.loc["p2", "actual_ppg"] == 5
    assert leaderboard["games"].tolist() == [2, 2]
    assert players["predicted_tossup_points"].sum() == 10
    rounds = pd.read_csv(tmp_path / "evaluation/csvs/tossup_round_metrics.csv")
    assert rounds["tossup_game_winner_accuracy"].tolist() == [1, 0]
    sequence = json.loads(events.loc[events.event_id == "g1::q", "predicted_buzz_sequence"].iloc[0])
    assert [buzz["token_position"] for buzz in sequence] == [1, 4]
    assert [buzz["points"] for buzz in sequence] == [-5, 10]


@pytest.mark.parametrize("missing", ["question_parameters", "recorded_scoring", "question_rows"])
def test_incomplete_game_is_excluded_from_ppg_and_all_game_totals(tmp_path, missing):
    evaluate, results, buzzes, official = saved_replay_fixture(tmp_path)
    if missing == "question_parameters":
        tossups = pd.read_csv(results / "tossups.csv")
        tossups[tossups.tossup_id != "dead"].to_csv(results / "tossups.csv", index=False)
    elif missing == "recorded_scoring":
        buzzes = buzzes[buzzes.game_id != "g1"]
    else:
        predictions = pd.read_csv(results / "tossup_predictions.csv")
        predictions[predictions.tossup_id != "dead"].to_csv(results / "tossup_predictions.csv", index=False)
    summary, events, players, games, leaderboard = evaluate(results, recorded_buzzes=buzzes, official_games=official)
    assert summary["tossup_replay_incomplete_games"] == 1
    assert games["game_id"].tolist() == ["g2"]
    assert set(events.game_id) == set(players.game_id) == {"g2"}
    assert leaderboard["games"].tolist() == [1, 1]


def test_saved_replay_includes_player_correctness_intercept(tmp_path):
    evaluate, results, buzzes, official = saved_replay_fixture(tmp_path)
    players = pd.read_csv(results / "players.csv")
    players["a"] = [5.0, 0.0]
    players.to_csv(results / "players.csv", index=False)
    _, events, _, _, leaderboard = evaluate(results, recorded_buzzes=buzzes, official_games=official)
    scored = events[events.tossup_id == "q"]
    assert set(scored.predicted_first_player_id) == {"p1"}
    assert set(scored.predicted_first_token_position) == {1}
    assert set(scored.predicted_scorer_player_id) == {"p1"}
    assert leaderboard.set_index("player_id").loc["p1", "predicted_ppg"] == 10
