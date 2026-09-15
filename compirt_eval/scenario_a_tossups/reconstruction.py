"""Reconstruct first-buzz probabilities from saved posterior parameters.

The end-inclusive diagnostic distribution covers timing, player attribution,
correctness, and dead mass. Model-specific difficulty curves are decoded by
``parameters``; this module combines them with each event's fitted roster.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from compirt_race import first_buzz_distribution as race_distribution

from compirt_eval.common.figures import numeric_columns
from compirt_eval.common.metrics import inverse_logit
from compirt_eval.scenario_a_tossups.parameters import (
    _buzz_parameter_prefix,
    _parameter_columns,
    _saved_difficulty_components,
    _saved_difficulty_curve,
    _supports_first_buzz_reconstruction,
    difficulty_adjustment_at,
    load_difficulty_adjustment_curves,
    load_difficulty_link,
    load_difficulty_scale,
    load_terminal_intercepts,
    perception_slice_indices,
    sliced_perception_columns,
)

DifficultyAdjustments = tuple[dict[str, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class _TimingEvaluationInputs:
    """Saved posterior tables needed for first-buzz evaluation."""

    players: pd.DataFrame
    tossups: pd.DataFrame
    predictions: pd.DataFrame
    adjustments: DifficultyAdjustments | None
    link: str
    difficulty_scale: float
    buzz_parameter_prefix: str
    terminal_intercepts: tuple[float, float]


def event_first_buzz_components(
    event,
    players,
    tossups,
    adjustments=None,
    link="sigmoid",
    buzz_parameter_prefix=None,
    difficulty_scale=1.0,
    terminal_intercepts=(0.0, 0.0),
    reconstruction_cache=None,
):
    """Reconstruct timing, player attribution, and correctness for one event.

    The probability that someone buzzes at a token is conserved exactly.  It is
    divided among players in proportion to the probability that each player is
    the only buzzer at that token, matching the model-analysis convention used
    elsewhere in this repository.  The returned player-token masses plus the
    dead mass sum to one up to floating-point error.
    """
    # Reconstruct the phase-0 field: bounceback rows repeat opposing players
    # after a neg and would inflate first-buzz mass. Minimal frames may omit z.
    if "z" in event.columns:
        event = event[~event["z"].astype(str).str.startswith("BOUNCE")]
    tossup_id = event["tossup_id"].iloc[0]
    tossup = tossups.loc[tossup_id]
    roster = players.loc[event["player_id"].astype(str)]
    # Reuse the saved parameter schema and question curves across event rosters.
    cache = reconstruction_cache if reconstruction_cache is not None else {}
    schema = cache.get("schema")
    if schema is None:
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
        if buzz_parameter_prefix is None:
            buzz_parameter_prefix = _buzz_parameter_prefix(tossups)
        correctness_weights = _parameter_columns(tossups)["alpha"]
        hazard_weights = _parameter_columns(tossups, buzz_parameter_prefix)["alpha"]
        schema = {
            "theta_columns": theta_columns,
            "alpha_columns": alpha_columns,
            "beta_columns": beta_columns,
            "sliced_alpha_columns": sliced_alpha_columns,
            "sliced_beta_columns": sliced_beta_columns,
            "perceived_difficulty": perceived_difficulty,
            "sliced_perceived_difficulty": sliced_perceived_difficulty,
            "perceived_logit": perceived_logit,
            "buzz_parameter_prefix": buzz_parameter_prefix,
            "correctness_weights": correctness_weights,
            "hazard_weights": hazard_weights,
        }
        cache["schema"] = schema
    theta_columns = schema["theta_columns"]
    alpha_columns = schema["alpha_columns"]
    beta_columns = schema["beta_columns"]
    sliced_alpha_columns = schema["sliced_alpha_columns"]
    sliced_beta_columns = schema["sliced_beta_columns"]
    perceived_difficulty = schema["perceived_difficulty"]
    sliced_perceived_difficulty = schema["sliced_perceived_difficulty"]
    perceived_logit = schema["perceived_logit"]
    buzz_parameter_prefix = schema["buzz_parameter_prefix"]
    correctness_weights = schema["correctness_weights"]
    hazard_weights = schema["hazard_weights"]
    if perceived_difficulty and not (
        len(alpha_columns) == len(beta_columns) == len(theta_columns)
    ):
        raise ValueError(
            "Perceived Bernstein theta, alpha, and beta dimensions must match"
        )
    if sliced_perceived_difficulty and not (
        sliced_alpha_columns
        and sliced_beta_columns
        and all(
            len(columns) == len(theta_columns)
            for columns in sliced_alpha_columns + sliced_beta_columns
        )
    ):
        raise ValueError(
            "Sliced perceived Bernstein theta, alpha, and beta dimensions "
            "must match"
        )
    if (
        not theta_columns
        or len(theta_columns) != len(correctness_weights)
        or len(theta_columns) != len(hazard_weights)
    ):
        raise ValueError(
            "Saved theta and discrimination/relevance dimensions must be present and match"
        )

    total_tokens = int(event["T_j"].iloc[0])
    static_key = ("tossup", str(tossup_id), total_tokens)
    static = cache.get(static_key)
    if static is None:
        positions = np.arange(1, total_tokens + 1, dtype=float)
        relative = positions / total_tokens
        hazard_difficulty = _saved_difficulty_curve(
            tossup,
            relative,
            link,
            difficulty_scale,
            parameter_prefix=buzz_parameter_prefix,
        )
        correctness_difficulty = _saved_difficulty_curve(
            tossup, relative, link, difficulty_scale
        )
        if hazard_difficulty is None or correctness_difficulty is None:
            raise ValueError("Saved tossup parameters cannot reconstruct difficulty")
        adjustment = difficulty_adjustment_at(adjustments, tossup_id, relative)
        if adjustment is not None:
            # TF-IDF runs: replay the effective difficulty d' the model trained on.
            hazard_difficulty = hazard_difficulty + adjustment
            correctness_difficulty = correctness_difficulty + adjustment
        static = {
            "relative": relative,
            "hazard_difficulty": hazard_difficulty,
            "correctness_difficulty": correctness_difficulty,
            "difficulty_components": (
                _saved_difficulty_components(tossup, relative)
                if perceived_difficulty or sliced_perceived_difficulty
                else None
            ),
        }
        cache[static_key] = static
    relative = static["relative"]
    hazard_difficulty = static["hazard_difficulty"]
    correctness_difficulty = static["correctness_difficulty"]
    theta = roster[theta_columns].to_numpy(dtype=float)
    correctness_skill = theta @ tossup[correctness_weights].to_numpy(dtype=float)
    hazard_skill = theta @ tossup[hazard_weights].to_numpy(dtype=float)
    # Double-difficulty models give the final cell an intercept because it also
    # covers the post-reading buzz window; other families pass zeros.
    end_correct, end_hazard = terminal_intercepts
    terminal = np.zeros_like(relative)
    terminal[-1] = 1.0
    if perceived_logit:
        logits = (
            roster["alpha"].to_numpy(dtype=float)[:, None]
            * (hazard_skill[:, None] - hazard_difficulty[None, :])
            + roster["beta"].to_numpy(dtype=float)[:, None]
        )
    elif sliced_perceived_difficulty:
        components = static["difficulty_components"]
        if components is None:
            raise ValueError("Saved tossup parameters cannot reconstruct difficulty")
        per_dimension, _effective = components
        relevance = tossup[hazard_weights].to_numpy(dtype=float)
        alpha = np.stack(
            [
                roster[columns].to_numpy(dtype=float)
                for columns in sliced_alpha_columns
            ],
            axis=1,
        )
        beta = np.stack(
            [
                roster[columns].to_numpy(dtype=float)
                for columns in sliced_beta_columns
            ],
            axis=1,
        )
        slice_index = perception_slice_indices(relative)
        selected_alpha = alpha[:, slice_index, :]
        selected_beta = beta[:, slice_index, :]
        logits = np.sum(
            relevance[None, None, :]
            * (
                theta[:, None, :]
                - selected_alpha * per_dimension.T[None, :, :]
                + selected_beta
            ),
            axis=2,
        )
    elif perceived_difficulty:
        components = static["difficulty_components"]
        if components is None:
            raise ValueError("Saved tossup parameters cannot reconstruct difficulty")
        per_dimension, _effective = components
        relevance = tossup[hazard_weights].to_numpy(dtype=float)
        alpha = roster[alpha_columns].to_numpy(dtype=float)
        beta = roster[beta_columns].to_numpy(dtype=float)
        logits = np.sum(
            relevance[None, :, None]
            * (
                theta[:, :, None]
                - alpha[:, :, None] * per_dimension[None, :, :]
                + beta[:, :, None]
            ),
            axis=1,
        )
    else:
        logits = (
            hazard_skill[:, None]
            - hazard_difficulty[None, :]
            - roster["c"].to_numpy(dtype=float)[:, None]
            + end_hazard * terminal[None, :]
        )
    # The same categorical cell law used in the training likelihood. Work
    # from logits so saturated sigmoid probabilities cannot change attribution.
    player_first_buzz_mass, dead_mass = race_distribution(logits)
    first_buzz_mass = player_first_buzz_mass.sum(axis=0)
    correctness_intercept = (
        roster["a"].to_numpy(dtype=float) if "a" in roster else np.zeros(len(roster))
    )
    correctness_probability = inverse_logit(
        correctness_skill[:, None]
        + correctness_intercept[:, None]
        - correctness_difficulty[None, :]
        + end_correct * terminal[None, :]
    )
    player_ids = roster.index.astype(str).to_numpy()
    player_to_team = dict(
        zip(event["player_id"].astype(str), event["team_id"].astype(str))
    ) if "team_id" in event else {}
    return {
        "relative_position": relative,
        # Exposed for downstream post-neg prediction. These are the same
        # fitted per-player token logits used to construct the phase-0 mass;
        # no additional model or test-outcome fitting is introduced.
        "hazard_logits": logits,
        "first_buzz_mass": first_buzz_mass,
        "dead_mass": dead_mass,
        "player_first_buzz_mass": player_first_buzz_mass,
        "correctness_probability": correctness_probability,
        "player_ids": player_ids,
        "team_ids": np.asarray(
            [player_to_team.get(player_id, "Unknown") for player_id in player_ids]
        ),
    }


def _event_first_buzz_mass(
    event,
    players,
    tossups,
    adjustments=None,
    link="sigmoid",
    buzz_parameter_prefix=None,
    difficulty_scale=1.0,
    terminal_intercepts=(0.0, 0.0),
):
    """Return per-token relative positions, first-buzz mass, and dead mass."""
    components = event_first_buzz_components(
        event,
        players,
        tossups,
        adjustments,
        link,
        buzz_parameter_prefix,
        difficulty_scale,
        terminal_intercepts,
    )
    return (
        components["relative_position"],
        components["first_buzz_mass"],
        components["dead_mass"],
    )


def first_buzz_distribution(
    event,
    players,
    tossups,
    n_bins=12,
    adjustments=None,
    link="sigmoid",
    buzz_parameter_prefix=None,
    difficulty_scale=1.0,
    terminal_intercepts=(0.0, 0.0),
):
    """Reconstruct team first-buzz mass from saved posterior median parameters.

    This replays the fitted Eq. 5 hazards outside Pyro as an end-inclusive
    diagnostic distribution: it returns how much first-buzz probability falls
    in each relative-position bin plus the probability remaining after the
    final token. The training likelihood follows the paper's Eq. 6/13
    convention S(T_j) = product over s < T_j, so this diagnostic should not be
    read as a byte-for-byte replay of its dead-tossup censoring term.
    """
    relative, first_buzz_mass, dead_mass = _event_first_buzz_mass(
        event,
        players,
        tossups,
        adjustments,
        link,
        buzz_parameter_prefix,
        difficulty_scale,
        terminal_intercepts,
    )
    bin_index = np.clip((relative * n_bins).astype(int), 0, n_bins - 1)
    binned_mass = np.zeros(n_bins)
    np.add.at(binned_mass, bin_index, first_buzz_mass)
    return binned_mass, dead_mass


def conditional_expected_buzz_position(
    event,
    players,
    tossups,
    adjustments=None,
    link="sigmoid",
    buzz_parameter_prefix=None,
    difficulty_scale=1.0,
    terminal_intercepts=(0.0, 0.0),
):
    """Return E[relative position | a buzz occurs] for one event's roster.

    Matches the trainers' 'expected_first_buzz_positions' convention after the
    buzz-conditioning fix: the expectation is normalized by the fitted buzz
    mass, with a question-end fallback when that mass is numerically zero.
    """
    relative, first_buzz_mass, _ = _event_first_buzz_mass(
        event,
        players,
        tossups,
        adjustments,
        link,
        buzz_parameter_prefix,
        difficulty_scale,
        terminal_intercepts,
    )
    buzz_mass = float(first_buzz_mass.sum())
    if buzz_mass <= 1e-9:
        return 1.0
    return float((relative * first_buzz_mass).sum() / buzz_mass)


def _load_timing_evaluation_inputs(results_dir):
    """Return saved timing inputs, or ``None`` for unsupported result sets."""
    required = [
        results_dir / "players.csv",
        results_dir / "tossups.csv",
        results_dir / "tossup_predictions.csv",
    ]
    if not all(path.exists() for path in required):
        return None

    players = pd.read_csv(required[0], dtype={"player_id": str}).set_index(
        "player_id"
    )
    tossups = pd.read_csv(required[1], dtype={"tossup_id": str}).set_index(
        "tossup_id"
    )
    predictions = pd.read_csv(
        required[2], dtype={"player_id": str, "tossup_id": str}
    )
    has_perception = (
        {"alpha_1", "beta_1"}.issubset(players.columns)
        or {"alpha_first_1", "beta_first_1"}.issubset(players.columns)
        or {"alpha", "beta"}.issubset(players.columns)
    )
    if predictions.empty or ("c" not in players and not has_perception):
        return None
    buzz_parameter_prefix = _buzz_parameter_prefix(tossups)
    if not _supports_first_buzz_reconstruction(
        players, tossups, buzz_parameter_prefix
    ):
        return None
    return _TimingEvaluationInputs(
        players=players,
        tossups=tossups,
        predictions=predictions,
        adjustments=load_difficulty_adjustment_curves(results_dir),
        link=load_difficulty_link(results_dir),
        difficulty_scale=load_difficulty_scale(results_dir),
        buzz_parameter_prefix=buzz_parameter_prefix,
        terminal_intercepts=load_terminal_intercepts(results_dir),
    )
