"""Focused tests for the randomized-team tournament evaluator."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from compirt_eval.imaginary_tournament import (
    TournamentInputs,
    simulate_imaginary_tournament,
    write_outputs,
)
from compirt_eval.imaginary_tournament.evaluation import _normalize_tossup_weights


def _toy_inputs():
    player_ids = np.asarray([f"player-{index}" for index in range(8)])
    tossup_ids = [f"tossup-{index}" for index in range(5)]
    return TournamentInputs(
        player_ids=player_ids,
        theta=np.linspace(-0.8, 1.2, 8).reshape(-1, 1),
        thresholds=np.linspace(1.8, 2.5, 8),
        tossups=pd.DataFrame(
            {
                "alpha_1": np.ones(5),
                "beta": np.linspace(0.6, 1.0, 5),
                "gamma": np.ones(5),
                "mu": np.full(5, 0.5),
            },
            index=tossup_ids,
        ),
        question_lengths=pd.Series(4, index=tossup_ids),
        bonus_probability=np.asarray([0.1, 0.2, 0.4, 0.3]),
        adjustments=None,
        difficulty_link="sigmoid",
        difficulty_scale=1.0,
        correctness_scale=1.0,
        correctness_bias=0.0,
    )


def test_random_tournament_is_seeded_and_ppg_has_the_right_denominator():
    first = simulate_imaginary_tournament(
        _toy_inputs(), games=12, players_per_team=2, tossups_per_game=3, seed=7
    )
    second = simulate_imaginary_tournament(
        _toy_inputs(), games=12, players_per_team=2, tossups_per_game=3, seed=7
    )
    first_players, first_games, first_summary = first
    second_players, second_games, second_summary = second

    pd.testing.assert_frame_equal(first_players, second_players)
    pd.testing.assert_frame_equal(first_games, second_games)
    assert first_summary == second_summary
    assert len(first_games) == 12
    assert first_players["games"].sum() == 12 * 4
    assert first_players["tossups_heard"].sum() == 12 * 4 * 3
    assert np.array_equal(
        first_players["tossup_points"],
        10 * first_players["gets"] - 5 * first_players["negs"],
    )
    assert np.allclose(
        first_players["ppg"],
        first_players["tossup_points"] / first_players["games"],
    )
    assert first_games["team_1_tossup_points"].sum() + first_games[
        "team_2_tossup_points"
    ].sum() == first_players["tossup_points"].sum()
    assert first_summary["games"] == 12


def test_random_tournament_rejects_an_oversized_roster():
    with pytest.raises(ValueError, match="at least 10 fitted players"):
        simulate_imaginary_tournament(
            _toy_inputs(), games=1, players_per_team=5, tossups_per_game=3
        )


def test_topic_weights_are_accepted_as_relevance_weights():
    tossups = pd.DataFrame(
        {
            "topic_weight_1": [0.25],
            "topic_weight_2": [0.75],
            "beta_1": [1.0],
            "beta_2": [2.0],
        }
    )
    normalized = _normalize_tossup_weights(tossups)
    assert {"r_1", "r_2"}.issubset(normalized.columns)
    assert not any(column.startswith("topic_weight_") for column in normalized)


def test_outputs_have_stable_filenames(tmp_path):
    players, games, summary = simulate_imaginary_tournament(
        _toy_inputs(), games=2, players_per_team=2, tossups_per_game=2, seed=11
    )
    write_outputs(tmp_path, players, games, summary)

    assert (tmp_path / "player_ppg.csv").exists()
    assert (tmp_path / "games.csv").exists()
    assert (tmp_path / "summary.json").exists()
