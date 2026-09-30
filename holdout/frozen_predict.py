"""Score held-out games with train-frozen parameters (matrix infill, no refit).

The transductive holdout runner refits question parameters on the test split.
This module instead replays both CompIRT stages at the *training* posterior
medians for the held-out games, so nothing is learned from the test outcomes:
it is the pure forward pass behind the frozen "matrix infill" evaluation.

Both stages already expose replay functions that take a ``posterior`` dict keyed
by the entity axis (``pyramidal_model.posterior_row_predictions`` /
``expected_first_buzz_positions``; ``compositional_model.posterior_predictions``).
Nothing in them requires the tensors to have come from SVI, so the whole scorer
is: build the *test* ``data`` dict from the test tables, assemble a
``posterior`` whose rows are the *train* medians aligned to the test entity
index, call those replay functions, and hand the results to the existing
``save_*`` writers.  The output directories are byte-schema-identical to a
trainer's, so ``evaluate_compirt`` consumes them unchanged.

The tossup scorer auto-detects the supported multidimensional and Bernstein
schemas. Bonus replay remains the standard compositional family.

Usage::

    python -m holdout.frozen_predict tossup --split game-holdout:...:test:5:0:42 \
        --train-pyramidal <root>/train/pyramidal --dimensions 5 \
        --difficulty-link sigmoid --output-dir <root>/holdout/pyramidal

    python -m holdout.frozen_predict bonus --split game-holdout:...:test:5:0:42 \
        --train-pyramidal <root>/train/pyramidal \
        --train-compositional <root>/train/compositional \
        --output-dir <root>/holdout/compositional
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd
import torch

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_data import (
    DEFAULT_DATA_DIR,
    bonus_tensors,
    build_bonus_part_observations,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from compositional_model import part_weight_site, posterior_predictions, validate_bonus_settings
from multidimensional.multidim_mirt import pyramidal_model as multidim_model
from train_compositional import load_player_skills
from multidimensional.multidim_mirt.train_pyramidal import save_multidim_parameters
from hazard_double_difficulty.bernstein import pyramidal_model as full_bernstein_model
from hazard_double_difficulty.perceived_difficulty_bernstein import (
    pyramidal_model as perceived_difficulty_bernstein_model,
)
from hazard_double_difficulty.perceived_logit_bernstein import (
    pyramidal_model as perceived_logit_bernstein_model,
)
from hazard_double_difficulty.multidim import pyramidal_model as double_sigmoid_model
from hazard_double_difficulty.bernstein.train_pyramidal import (
    save_double_difficulty_parameters as save_full_bernstein_parameters,
)
from hazard_double_difficulty.perceived_difficulty_bernstein.train_pyramidal import (
    save_perceived_parameters,
)
from hazard_double_difficulty.perceived_logit_bernstein.train_pyramidal import (
    save_perceived_logit_parameters,
)
from hazard_double_difficulty.multidim.train_pyramidal import (
    save_double_difficulty_parameters as save_double_sigmoid_parameters,
)
from utils.saving import save_bonus_predictions, save_tossup_predictions
from utils.training import require_device


FULL_BERNSTEIN = "full-double-bernstein"
POLYNOMIAL_BERNSTEIN = "single-curve-bernstein"
PERCEIVED_DIFFICULTY_BERNSTEIN = "perceived-difficulty-bernstein"
PERCEIVED_DIFFICULTY_SLICED_BERNSTEIN = (
    "perceived-difficulty-sliced-bernstein"
)
PERCEIVED_LOGIT_BERNSTEIN = "perceived-logit-bernstein"
DOUBLE_SIGMOID = "monotone-double-sigmoid"
MULTIDIM = "multidim"
LINEAR_SPLINE = "dd-linear-spline"


# --- aligned parameter loaders ------------------------------------------------


def _theta_dimensions(frame: pd.DataFrame) -> int:
    """Count numbered ``theta_k`` columns in a saved players frame."""
    return sum(
        1
        for column in frame.columns
        if column.startswith("theta_") and column.removeprefix("theta_").isdigit()
    )


def _numbered_columns(frame: pd.DataFrame, prefix: str, dimensions: int) -> list[str]:
    """Return ``prefix_1 .. prefix_K`` and confirm every column is present."""
    columns = [f"{prefix}_{k}" for k in range(1, dimensions + 1)]
    missing = [column for column in columns if column not in frame.columns]
    if missing:
        raise ValueError(f"{prefix} columns {missing} missing from frozen parameters")
    return columns


def _aligned_matrix(
    frame: pd.DataFrame, id_column: str, ids, columns: list[str], device
) -> torch.Tensor:
    """Return ``frame[columns]`` reindexed to ``ids`` order as a float tensor."""
    indexed = frame.set_index(frame[id_column].astype(str))
    values = indexed.loc[list(ids), columns].to_numpy(dtype="float32")
    return torch.tensor(values, dtype=torch.float32, device=device)


def _aligned_vector(frame: pd.DataFrame, id_column: str, ids, column: str, device):
    indexed = frame.set_index(frame[id_column].astype(str))
    values = indexed.loc[list(ids), column].to_numpy(dtype="float32")
    return torch.tensor(values, dtype=torch.float32, device=device)


def detect_tossup_parameter_schema(
    tossups: pd.DataFrame, players: pd.DataFrame | None = None
) -> str:
    """Detect frozen-replay schemas, preserving the multidim default."""
    columns = set(tossups.columns)
    if "hazard_spline_y_0_d1" in columns:
        return LINEAR_SPLINE
    if "hazard_start_difficulty_d1" in columns:
        return FULL_BERNSTEIN
    if (
        players is not None
        and {"alpha", "beta"}.issubset(players.columns)
        and "start_difficulty_d1" in columns
    ):
        return PERCEIVED_LOGIT_BERNSTEIN
    if (
        players is not None
        and {"alpha_first_1", "beta_first_1"}.issubset(players.columns)
        and "start_difficulty_d1" in columns
    ):
        return PERCEIVED_DIFFICULTY_SLICED_BERNSTEIN
    if (
        players is not None
        and {"alpha_1", "beta_1"}.issubset(players.columns)
        and "start_difficulty_d1" in columns
    ):
        return PERCEIVED_DIFFICULTY_BERNSTEIN
    if "start_difficulty_d1" in columns:
        return POLYNOMIAL_BERNSTEIN
    if "hazard_beta_1" in columns:
        return DOUBLE_SIGMOID
    return MULTIDIM


def _tossup_matrix(tossups, data, prefix, dimensions, device):
    """Return one numbered ``prefix_1..K`` block aligned to the test tossups."""
    return _aligned_matrix(
        tossups,
        "tossup_id",
        data["tossup_ids"],
        _numbered_columns(tossups, prefix, dimensions),
        device,
    )


def _both_curves(load_curve):
    """Run a curve loader over both branches and key it the way models expect.

    Correctness columns are saved unprefixed and hazard columns under
    ``hazard_``; the posterior keys they map to carry the matching suffix.
    """
    posterior = {}
    for prefix, suffix in (("", "correct"), ("hazard_", "hazard")):
        start, total, shares = load_curve(prefix)
        posterior[f"start_difficulty_{suffix}"] = start
        posterior[f"total_drop_{suffix}"] = total
        posterior[f"drop_proportions_{suffix}"] = shares
    return posterior


def _double_relevance(tossups, data, dimensions, device):
    """Load the two relevance vectors the vector double-difficulty families save."""
    return {
        f"r_{suffix}": _tossup_matrix(tossups, data, prefix, dimensions, device)
        for prefix, suffix in (("r", "correct"), ("hazard_r", "hazard"))
    }


def _aligned_bernstein_curve(frame, ids, prefix, dimensions, degree, device):
    indexed = frame.set_index(frame["tossup_id"].astype(str)).loc[list(ids)]
    dimension_range = range(1, dimensions + 1)
    start = [f"{prefix}start_difficulty_d{k}" for k in dimension_range]
    total = [f"{prefix}total_drop_d{k}" for k in dimension_range]
    shares = [
        f"{prefix}drop_share_{m}_d{k}"
        for k in dimension_range
        for m in range(1, degree + 1)
    ]
    return (
        torch.tensor(indexed[start].to_numpy(dtype="float32"), device=device),
        torch.tensor(indexed[total].to_numpy(dtype="float32"), device=device),
        torch.tensor(
            indexed[shares]
            .to_numpy(dtype="float32")
            .reshape(len(indexed), dimensions, degree),
            device=device,
        ),
    )


def _load_full_bernstein_parameters(tossups, data, dimensions, device):
    degree = sum(
        column.startswith("drop_share_") and column.endswith("_d1")
        for column in tossups.columns
    )
    return {
        **_double_relevance(tossups, data, dimensions, device),
        **_both_curves(
            lambda prefix: _aligned_bernstein_curve(
                tossups, data["tossup_ids"], prefix, dimensions, degree, device
            )
        ),
    }


def _load_polynomial_parameters(tossups, data, dimensions, device):
    degree = sum(
        column.startswith("drop_share_") and column.endswith("_d1")
        for column in tossups.columns
    )
    start, total_drop, shares = _aligned_bernstein_curve(
        tossups, data["tossup_ids"], "", dimensions, degree, device
    )
    return {
        "r": _tossup_matrix(tossups, data, "r", dimensions, device),
        "start_difficulty": start,
        "total_drop": total_drop,
        "drop_proportions": shares,
    }


def _load_double_sigmoid_parameters(tossups, data, dimensions, device):
    return {
        **_double_relevance(tossups, data, dimensions, device),
        **{
            f"{name}_{suffix}": _tossup_matrix(
                tossups, data, f"{prefix}{name}", dimensions, device
            )
            for prefix, suffix in (("", "correct"), ("hazard_", "hazard"))
            for name in ("beta", "gamma", "mu")
        },
    }


def _load_multidim_parameters(tossups, data, dimensions, device):
    return {
        name: _tossup_matrix(tossups, data, name, dimensions, device)
        for name in ("r", "beta", "gamma", "mu")
    }


@dataclass(frozen=True)
class TossupSchema:
    """How one saved Stage-1 family is loaded, replayed, and written back.

    The flags say which optional arguments the family's replay functions take.
    Bernstein curves carry their shape in the saved parameters, so only the
    sigmoid families need ``--difficulty-link``.
    """

    load: Callable
    model: object
    save: Callable
    calibration_aware: bool = False
    link_aware: bool = False
    perceived_players: bool = False
    sliced_perceived_players: bool = False
    scalar_perception: bool = False


TOSSUP_SCHEMAS = {
    PERCEIVED_LOGIT_BERNSTEIN: TossupSchema(
        _load_polynomial_parameters,
        perceived_logit_bernstein_model,
        save_perceived_logit_parameters,
        scalar_perception=True,
    ),
    PERCEIVED_DIFFICULTY_BERNSTEIN: TossupSchema(
        _load_polynomial_parameters,
        perceived_difficulty_bernstein_model,
        save_perceived_parameters,
        perceived_players=True,
    ),
    PERCEIVED_DIFFICULTY_SLICED_BERNSTEIN: TossupSchema(
        _load_polynomial_parameters,
        perceived_difficulty_bernstein_model,
        save_perceived_parameters,
        sliced_perceived_players=True,
    ),
    FULL_BERNSTEIN: TossupSchema(
        _load_full_bernstein_parameters,
        full_bernstein_model,
        save_full_bernstein_parameters,
        calibration_aware=True,
    ),
    DOUBLE_SIGMOID: TossupSchema(
        _load_double_sigmoid_parameters,
        double_sigmoid_model,
        save_double_sigmoid_parameters,
        calibration_aware=True,
        link_aware=True,
    ),
    MULTIDIM: TossupSchema(
        _load_multidim_parameters,
        multidim_model,
        save_multidim_parameters,
        calibration_aware=True,
        link_aware=True,
    ),
}


# Archived families are still detected so their saved fits fail clearly instead
# of being misread as the multidim default.
ARCHIVED_SCHEMAS = {
    POLYNOMIAL_BERNSTEIN: "archive/polynomial_compirt",
    LINEAR_SPLINE: "archive/dd_linear_spline",
}


def _tossup_schema(schema):
    """Resolve a replay family, rejecting schemas whose package was archived."""
    if schema in ARCHIVED_SCHEMAS:
        raise ValueError(
            f"{schema} replay is no longer supported; its model package was "
            f"moved to {ARCHIVED_SCHEMAS[schema]}"
        )
    return TOSSUP_SCHEMAS[schema]


def _load_tossup_posterior(players, tossups, data, dimensions, device, schema):
    """Assemble the shared player parameters plus one family's item parameters."""
    posterior = {
        "theta": _aligned_matrix(
            players,
            "player_id",
            data["player_ids"],
            _numbered_columns(players, "theta", dimensions),
            device,
        ),
    }
    family = _tossup_schema(schema)
    if family.scalar_perception:
        posterior.update(
            {
                name: _aligned_vector(
                    players, "player_id", data["player_ids"], name, device
                )
                for name in ("alpha", "beta")
            }
        )
    elif family.sliced_perceived_players:
        dimension_range = range(1, dimensions + 1)
        for name in ("alpha", "beta"):
            posterior[name] = torch.stack(
                [
                    _aligned_matrix(
                        players,
                        "player_id",
                        data["player_ids"],
                        [
                            f"{name}_{slice_name}_{dimension}"
                            for dimension in dimension_range
                        ],
                        device,
                    )
                    for slice_name in ("first", "middle", "last")
                ],
                dim=1,
            )
    elif family.perceived_players:
        posterior.update(
            {
                name: _aligned_matrix(
                    players,
                    "player_id",
                    data["player_ids"],
                    _numbered_columns(players, name, dimensions),
                    device,
                )
                for name in ("alpha", "beta")
            }
        )
    else:
        posterior["c"] = _aligned_vector(
            players, "player_id", data["player_ids"], "c", device
        )
        if schema == FULL_BERNSTEIN and "a" in players.columns:
            posterior["a"] = _aligned_vector(
                players, "player_id", data["player_ids"], "a", device
            )
    posterior.update(family.load(tossups, data, dimensions, device))
    return posterior


def _load_terminal_intercepts(summary_path: Path, device):
    """Return a fit's saved final-cell intercepts, if it has them.

    The double-difficulty families give position 'T_j' its own correctness and
    hazard intercept. Both are global scalars, so they live in the training
    'summary.json' rather than in 'tossups.csv'. A fit made without them simply
    has no keys and the replay stays on the old path.
    """
    if not summary_path.exists():
        return {}
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    if "end_correct" not in summary or "end_hazard" not in summary:
        return {}
    return {
        name: torch.tensor(float(summary[name]), device=device)
        for name in ("end_correct", "end_hazard")
    }


def _load_calibration(summary_path: Path, device):
    """Return Platt scale/bias tensors from a stage summary, or ``None``."""
    if not summary_path.exists():
        return None
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    if "correctness_bias" not in summary:
        return None
    return (
        (
            torch.tensor(float(summary["correctness_scale"]), device=device)
            if "correctness_scale" in summary
            else None
        ),
        torch.tensor(float(summary["correctness_bias"]), device=device),
    )


# --- coverage guards ----------------------------------------------------------


def _drop_uncovered_tossup_events(observations, known_players, known_tossups, on_missing):
    """Drop whole events whose tossup or any rostered player lacks a train fit.

    Single rows are never dropped: an event's survival, first-buzz timing, and
    joint score aggregate over its full roster, so a partial roster would
    corrupt them.
    """
    tossup_ok = observations["tossup_id"].astype(str).isin(known_tossups)
    player_ok = observations["player_id"].astype(str).isin(known_players)
    bad_events = set(observations.loc[~(tossup_ok & player_ok), "event_id"])
    info = {
        "dropped_events": len(bad_events),
        "missing_tossups": sorted(
            set(observations.loc[~tossup_ok, "tossup_id"].astype(str))
        ),
        "missing_players": sorted(
            set(observations.loc[~player_ok, "player_id"].astype(str))
        ),
    }
    if bad_events:
        message = (
            f"{len(bad_events)} test events reference entities with no training "
            f"fit ({len(info['missing_tossups'])} tossups, "
            f"{len(info['missing_players'])} players)"
        )
        if on_missing == "error":
            raise SystemExit(message)
        print(f"Dropping {message}")
    kept = observations[~observations["event_id"].isin(bad_events)].reset_index(drop=True)
    return kept, info


def _drop_uncovered_bonus_responses(observations, known_parts, on_missing):
    """Drop whole responses whose any part lacks a train fit."""
    part_ok = observations["bonus_part_id"].astype(str).isin(known_parts)
    bad_responses = set(observations.loc[~part_ok, "response_id"])
    info = {
        "dropped_responses": len(bad_responses),
        "missing_parts": sorted(
            set(observations.loc[~part_ok, "bonus_part_id"].astype(str))
        ),
    }
    if bad_responses:
        message = (
            f"{len(bad_responses)} test bonus responses reference parts with no "
            f"training fit ({len(info['missing_parts'])} parts)"
        )
        if on_missing == "error":
            raise SystemExit(message)
        print(f"Dropping {message}")
    kept = observations[~observations["response_id"].isin(bad_responses)].reset_index(
        drop=True
    )
    return kept, info


# --- frozen tossup stage ------------------------------------------------------


def frozen_predict_tossups(args) -> dict:
    """Replay Stage-1 tossup predictions for the test split at train medians."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    train_pyr = Path(args.train_pyramidal)
    players = pd.read_csv(train_pyr / "players.csv")
    tossups = pd.read_csv(train_pyr / "tossups.csv")
    train_dimensions = _theta_dimensions(players)
    if train_dimensions != args.dimensions:
        raise ValueError(
            f"--dimensions {args.dimensions} but training players.csv has "
            f"{train_dimensions} theta columns; rerun with matching --dimensions"
        )

    tables = filter_tournament(
        load_hf_tables(args.data_dir, args.split), args.tournament
    )
    observations = build_tossup_observations(
        tables, include_bounceback=args.include_bounceback
    )
    if observations.empty:
        raise ValueError("No tossup observations matched the requested data selection")
    observations, drop_info = _drop_uncovered_tossup_events(
        observations,
        set(players["player_id"].astype(str)),
        set(tossups["tossup_id"].astype(str)),
        args.on_missing,
    )
    if observations.empty:
        raise ValueError("Every test event was dropped for missing training fits")

    data = tossup_tensors(observations, args.device)
    print(
        f"Rows: {len(observations):,}  "
        f"Players: {len(data['player_ids']):,}  "
        f"Tossups: {len(data['tossup_ids']):,}"
    )

    schema = detect_tossup_parameter_schema(tossups, players)
    family = _tossup_schema(schema)
    if args.calibrate_correctness and not family.calibration_aware:
        raise ValueError(f"{schema} does not support correctness calibration")
    posterior = _load_tossup_posterior(
        players, tossups, data, args.dimensions, args.device, schema
    )
    # Terminal-cell intercepts are global, so they live in the training summary.
    # A family or fit without them contributes no keys and replays unchanged.
    posterior.update(
        _load_terminal_intercepts(train_pyr / "summary.json", args.device)
    )
    calibrate_scale = True
    if args.calibrate_correctness:
        calibration = _load_calibration(train_pyr / "summary.json", args.device)
        if calibration is None:
            raise ValueError(
                "--calibrate-correctness set but training summary.json has no "
                "correctness_bias"
            )
        scale, posterior["correctness_bias"] = calibration
        calibrate_scale = scale is not None
        if calibrate_scale:
            posterior["correctness_scale"] = scale

    # Passed by keyword: the families order these differently.
    row_kwargs = {}
    if family.calibration_aware:
        row_kwargs.update(
            calibrate_correctness=args.calibrate_correctness,
            calibrate_scale=calibrate_scale,
        )
    timing_kwargs = {"link": args.difficulty_link} if family.link_aware else {}
    correct, hazard, survival = family.model.posterior_row_predictions(
        data, posterior, **row_kwargs, **timing_kwargs
    )
    buzz_expected = family.model.expected_first_buzz_positions(
        data, posterior, **timing_kwargs
    )
    family.save(args.output_dir, data, posterior)
    save_tossup_predictions(
        args.output_dir,
        observations,
        correct,
        hazard,
        survival,
        buzz_expected=buzz_expected,
    )
    summary = _stage_summary(train_pyr / "summary.json", args, data, drop_info)
    summary["parameter_schema"] = schema
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    return summary


def _stage_summary(train_summary_path, args, data, drop_info) -> dict:
    """Carry the training pyramidal summary forward with frozen-run metadata."""
    summary = {}
    if train_summary_path.exists():
        summary = json.loads(train_summary_path.read_text(encoding="utf-8"))
    summary.update(
        {
            "frozen_predict": True,
            "split": args.split,
            "tournament": args.tournament or "",
            "dimensions": args.dimensions,
            "difficulty_link": args.difficulty_link,
            "calibrate_correctness": args.calibrate_correctness,
            "players": len(data["player_ids"]),
            "tossups": len(data["tossup_ids"]),
            "events": len(data["event_ids"]),
        }
    )
    summary.update(drop_info)
    return summary


# --- frozen bonus stage -------------------------------------------------------


def frozen_predict_bonuses(args) -> dict:
    """Replay Stage-2 bonus predictions for the test split at train medians."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    train_pyr = Path(args.train_pyramidal)
    train_bonus = Path(args.train_compositional)

    summary_path = train_bonus / "summary.json"
    training_summary = json.loads(summary_path.read_text()) if summary_path.exists() else {}
    # Replay the model the fit used. Summaries written before an option existed
    # used its default.
    bonus_difficulty = training_summary.get("bonus_difficulty", "scalar")
    bonus_aggregation = training_summary.get("bonus_aggregation", "lse")
    synergy_form = training_summary.get("synergy_form", "dot")
    synergy_link = training_summary.get("synergy_link", "additive")
    for setting in ("use_synergy", "calibrate_correctness"):
        if setting in training_summary and bool(training_summary[setting]) != getattr(args, setting):
            raise ValueError(
                f"Replay {setting}={getattr(args, setting)} disagrees with the "
                f"saved bonus fit ({training_summary[setting]}): {summary_path}"
            )
    validate_bonus_settings(
        bonus_aggregation,
        bonus_difficulty,
        use_synergy=args.use_synergy,
        calibrate_correctness=args.calibrate_correctness,
        synergy_form=synergy_form,
        synergy_link=synergy_link,
    )

    player_ids, theta = load_player_skills(train_pyr / "players.csv", args.device)
    tables = filter_tournament(
        load_hf_tables(args.data_dir, args.split), args.tournament
    )
    observations = build_bonus_part_observations(tables)
    if observations.empty:
        raise ValueError("No bonus observations matched the requested data selection")

    known_players = set(player_ids)
    known_roster = [
        bool(roster) and all(str(player) in known_players for player in roster)
        for roster in observations["player_ids"]
    ]
    unknown_roster = int(len(observations) - sum(known_roster))
    if unknown_roster and args.on_missing == "error":
        raise ValueError(f"{unknown_roster} bonus part rows have empty or uncovered rosters")
    uncovered_responses = set(observations.loc[np.logical_not(known_roster), "response_id"])
    observations = observations[
        ~observations["response_id"].isin(uncovered_responses)
    ].reset_index(drop=True)

    bonus_parts = pd.read_csv(train_bonus / "bonus_parts.csv")
    known_parts = set(bonus_parts["bonus_part_id"].astype(str))
    observations, drop_info = _drop_uncovered_bonus_responses(
        observations, known_parts, args.on_missing
    )
    drop_info["dropped_rows_unknown_roster"] = unknown_roster
    drop_info["dropped_responses_unknown_roster"] = len(uncovered_responses)
    if observations.empty:
        raise ValueError("Every test bonus response was dropped for missing training fits")

    data = bonus_tensors(observations, player_ids, args.device)
    print(f"Bonus part rows: {len(observations):,}  Parts: {len(data['part_ids']):,}")

    dimensions = theta.shape[1]
    weight_site = part_weight_site(bonus_difficulty)
    posterior = {
        weight_site: _aligned_matrix(
            bonus_parts,
            "bonus_part_id",
            data["part_ids"],
            _numbered_columns(bonus_parts, weight_site, dimensions),
            args.device,
        ),
    }
    # Only LSE aggregation saves a temperature.
    if bonus_aggregation == "lse":
        posterior["tau"] = torch.tensor(
            float((train_bonus / "tau.txt").read_text().strip()), device=args.device
        )
    if bonus_difficulty == "multidim":
        posterior["beta"] = _aligned_matrix(
            bonus_parts, "bonus_part_id", data["part_ids"],
            _numbered_columns(bonus_parts, "beta", dimensions), args.device,
        )
    else:
        posterior["beta"] = _aligned_vector(
            bonus_parts, "bonus_part_id", data["part_ids"], "beta", args.device
        )
    if args.use_synergy:
        profiles = pd.read_csv(train_bonus / "player_synergy_profiles.csv", dtype={"player_id": str})
        synergy_dimensions = sum(
            1
            for column in profiles.columns
            if column.startswith("psi_") and column.removeprefix("psi_").isdigit()
        )
        if not synergy_dimensions or profiles["player_id"].astype(str).duplicated().any():
            raise ValueError(f"Invalid synergy profiles in {train_bonus}")
        # Unused players may be absent; every evaluated roster needs fitted psi.
        indexed = profiles.set_index(profiles["player_id"].astype(str))
        active = {str(player) for roster in observations["player_ids"] for player in roster}
        missing = active - set(indexed.index)
        if missing:
            raise ValueError(f"Missing fitted synergy profiles for {len(missing)} evaluated players")
        present = [pid for pid in player_ids if pid in indexed.index]
        has_phi = any(
            column.startswith("phi_") and column.removeprefix("phi_").isdigit()
            for column in profiles
        )
        if has_phi != (synergy_form == "phi-psi"):
            raise ValueError("Saved phi profiles disagree with summary synergy_form")
        for name in (("psi", "phi") if synergy_form == "phi-psi" else ("psi",)):
            columns = _numbered_columns(profiles, name, synergy_dimensions)
            values = torch.zeros((len(player_ids), synergy_dimensions), device=args.device)
            if present:
                aligned = indexed.loc[present, columns].to_numpy(dtype="float32")
                if not np.isfinite(aligned).all():
                    raise ValueError(f"Nonfinite synergy profiles in {train_bonus}")
                row_of = {pid: row for row, pid in enumerate(player_ids)}
                values[[row_of[pid] for pid in present]] = torch.tensor(
                    aligned, dtype=torch.float32, device=args.device
                )
            posterior[name] = values
    if args.calibrate_correctness:
        calibration = _load_calibration(train_bonus / "summary.json", args.device)
        if calibration is None:
            raise ValueError(
                "--calibrate-correctness set but training bonus summary.json has "
                "no correctness_scale/bias"
            )
        posterior["correctness_scale"], posterior["correctness_bias"] = calibration

    probabilities, aggregates, synergy = posterior_predictions(
        data, theta, posterior, args.use_synergy, args.calibrate_correctness,
        synergy_link=synergy_link, bonus_difficulty=bonus_difficulty,
        bonus_aggregation=bonus_aggregation,
    )
    save_bonus_predictions(
        args.output_dir, observations, probabilities, aggregates, synergy
    )
    summary = {
        "frozen_predict": True,
        "train_pyramidal": str(train_pyr.resolve()),
        "train_compositional": str(train_bonus.resolve()),
        "split": args.split,
        "tournament": args.tournament or "",
        "use_synergy": args.use_synergy,
        "synergy_form": synergy_form,
        "synergy_link": synergy_link,
        "bonus_difficulty": bonus_difficulty,
        "bonus_aggregation": bonus_aggregation,
        "calibrate_correctness": args.calibrate_correctness,
        "skill_dimensions": dimensions,
        "bonus_part_observations": len(observations),
        "bonus_parts": len(data["part_ids"]),
        "tau": float(posterior["tau"].detach().cpu()) if "tau" in posterior else None,
        **drop_info,
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    return summary


# --- CLI ----------------------------------------------------------------------


def _add_shared_args(parser):
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--train-pyramidal", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--calibrate-correctness", action="store_true")
    parser.add_argument(
        "--on-missing",
        choices=("drop", "error"),
        default="drop",
        help="test entity with no training fit: drop the whole event/response "
        "(default) or fail",
    )


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="stage", required=True)

    tossup = subparsers.add_parser("tossup", help="frozen Stage-1 tossup scoring")
    _add_shared_args(tossup)
    tossup.add_argument("--dimensions", type=int, required=True)
    tossup.add_argument(
        "--difficulty-link", choices=("sigmoid", "tanh"), default="sigmoid"
    )
    tossup.add_argument("--include-bounceback", action="store_true")

    bonus = subparsers.add_parser("bonus", help="frozen Stage-2 bonus scoring")
    _add_shared_args(bonus)
    bonus.add_argument("--train-compositional", type=Path, required=True)
    bonus.add_argument("--use-synergy", action="store_true")

    return parser.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)
    if args.stage == "tossup":
        frozen_predict_tossups(args)
    else:
        frozen_predict_bonuses(args)


if __name__ == "__main__":
    main()
