"""Contracts shared by the two perceived-difficulty Bernstein test suites.

`perceived_difficulty_bernstein` (per-dimension alpha/beta, optionally sliced by
thirds of the question) and `perceived_logit_bernstein` (one scalar alpha/beta
per player) differ only in the shape of the player perception parameters. The
save/reload/replay contract is identical, so it lives here instead of being
written out once per suite.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import torch

from compirt_eval.scenario_a_tossups.reconstruction import event_first_buzz_components
from holdout.frozen_predict import (
    _load_tossup_posterior,
    detect_tossup_parameter_schema,
)


def assert_frozen_replay_matches(
    tmp_path, data, fit, *, model, save_parameters, schema, dimensions=3
):
    """Save `fit`, reload it, and assert the replay reproduces the native fit.

    Covers the whole round trip a holdout fold depends on: the saved CSVs are
    detected as `schema`, `holdout.frozen_predict` rebuilds a posterior whose
    row predictions match the in-memory ones, and the NumPy evaluator's event
    masses agree with the same hazards computed through the Torch model.

    Returns the saved `(players, tossups, rebuilt)` so callers can assert the
    column layout their own schema is responsible for.
    """
    save_parameters(tmp_path, data, fit)
    players = pd.read_csv(tmp_path / "players.csv")
    tossups = pd.read_csv(tmp_path / "tossups.csv")
    assert detect_tossup_parameter_schema(tossups, players) == schema

    rebuilt = _load_tossup_posterior(
        players, tossups, data, dimensions=dimensions, device="cpu", schema=schema
    )
    for native, replay in zip(
        model.posterior_row_predictions(data, fit),
        model.posterior_row_predictions(data, rebuilt),
    ):
        torch.testing.assert_close(native, replay, rtol=1e-5, atol=1e-6)

    _assert_evaluator_masses_match_model(model, data, fit, players, tossups)
    return players, tossups, rebuilt


def _assert_evaluator_masses_match_model(model, data, fit, players, tossups):
    """Check the evaluator's first-buzz PMF against hand-computed hazards.

    One synthetic event puts all three players on the first tossup, so the
    per-player buzz mass plus the dead mass must be exactly one, and the dead
    mass must equal the probability that nobody buzzes at any token.
    """
    tokens = 4
    event = pd.DataFrame(
        {
            "event_id": ["e1"] * 3,
            "tossup_id": [data["tossup_ids"][0]] * 3,
            "player_id": data["player_ids"],
            "T_j": [tokens] * 3,
            "z": ["BUZZ", "CENSORED", "CENSORED"],
        }
    )
    components = event_first_buzz_components(
        event, players.set_index("player_id"), tossups.set_index("tossup_id")
    )
    assert np.isclose(
        components["player_first_buzz_mass"].sum() + components["dead_mass"], 1.0
    )

    question = 0
    positions = torch.arange(1, tokens + 1, dtype=torch.float32).expand(3, -1)
    total_tokens = torch.full_like(positions, float(tokens))
    hazard = torch.sigmoid(
        model.hazard_logit(
            fit["theta"].unsqueeze(1),
            fit["r"][question].view(1, 1, -1),
            fit["start_difficulty"][question].view(1, 1, -1),
            fit["total_drop"][question].view(1, 1, -1),
            fit["drop_proportions"][question].view(1, 1, 3, 3),
            fit["alpha"].unsqueeze(1),
            fit["beta"].unsqueeze(1),
            positions,
            total_tokens,
        )
    )
    expected_dead = torch.prod(1.0 - hazard).item()
    assert np.isclose(components["dead_mass"], expected_dead, rtol=1e-5)
