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

The active model family is ``multidim`` (per-dimension tossup difficulty).

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
from pathlib import Path

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
from compositional_model import posterior_predictions
from multidimensional.multidim_mirt.pyramidal_model import (
    expected_first_buzz_positions,
    posterior_row_predictions,
)
from train_compositional import load_player_skills
from multidimensional.multidim_mirt.train_pyramidal import save_multidim_parameters
from utils.saving import save_bonus_predictions, save_tossup_predictions
from utils.training import require_device


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


def _load_calibration(summary_path: Path, device):
    """Return Platt scale/bias tensors from a stage summary, or ``None``."""
    if not summary_path.exists():
        return None
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    if "correctness_scale" not in summary:
        return None
    return (
        torch.tensor(float(summary["correctness_scale"]), device=device),
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

    theta_cols = _numbered_columns(players, "theta", args.dimensions)
    posterior = {
        "theta": _aligned_matrix(
            players, "player_id", data["player_ids"], theta_cols, args.device
        ),
        "c": _aligned_vector(
            players, "player_id", data["player_ids"], "c", args.device
        ),
    }
    for prefix in ("r", "beta", "gamma", "mu"):
        posterior[prefix] = _aligned_matrix(
            tossups,
            "tossup_id",
            data["tossup_ids"],
            _numbered_columns(tossups, prefix, args.dimensions),
            args.device,
        )
    if args.calibrate_correctness:
        calibration = _load_calibration(train_pyr / "summary.json", args.device)
        if calibration is None:
            raise ValueError(
                "--calibrate-correctness set but training summary.json has no "
                "correctness_scale/bias"
            )
        posterior["correctness_scale"], posterior["correctness_bias"] = calibration

    correct, hazard, survival = posterior_row_predictions(
        data, posterior, args.calibrate_correctness, args.difficulty_link
    )
    buzz_expected = expected_first_buzz_positions(data, posterior, args.difficulty_link)

    save_multidim_parameters(args.output_dir, data, posterior)
    save_tossup_predictions(
        args.output_dir,
        observations,
        correct,
        hazard,
        survival,
        buzz_expected=buzz_expected,
    )
    summary = _stage_summary(train_pyr / "summary.json", args, data, drop_info)
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
    observations = observations[known_roster].reset_index(drop=True)

    bonus_parts = pd.read_csv(train_bonus / "bonus_parts.csv")
    known_parts = set(bonus_parts["bonus_part_id"].astype(str))
    observations, drop_info = _drop_uncovered_bonus_responses(
        observations, known_parts, args.on_missing
    )
    drop_info["dropped_rows_unknown_roster"] = unknown_roster
    if observations.empty:
        raise ValueError("Every test bonus response was dropped for missing training fits")

    data = bonus_tensors(observations, player_ids, args.device)
    print(f"Bonus part rows: {len(observations):,}  Parts: {len(data['part_ids']):,}")

    dimensions = theta.shape[1]
    posterior = {
        "alpha": _aligned_matrix(
            bonus_parts,
            "bonus_part_id",
            data["part_ids"],
            _numbered_columns(bonus_parts, "alpha", dimensions),
            args.device,
        ),
        "beta": _aligned_vector(
            bonus_parts, "bonus_part_id", data["part_ids"], "beta", args.device
        ),
        "tau": torch.tensor(
            float((train_bonus / "tau.txt").read_text().strip()), device=args.device
        ),
    }
    if args.use_synergy:
        profiles = pd.read_csv(train_bonus / "player_synergy_profiles.csv")
        synergy_dimensions = sum(
            1
            for column in profiles.columns
            if column.startswith("psi_") and column.removeprefix("psi_").isdigit()
        )
        psi_columns = _numbered_columns(profiles, "psi", synergy_dimensions)
        # Align to the frozen theta player order; players absent from the saved
        # synergy profiles fall back to a zero (no-synergy) profile.
        indexed = profiles.set_index(profiles["player_id"].astype(str))
        present = [pid for pid in player_ids if pid in indexed.index]
        psi = torch.zeros((len(player_ids), synergy_dimensions), device=args.device)
        if present:
            aligned = indexed.loc[present, psi_columns].to_numpy(dtype="float32")
            row_of = {pid: row for row, pid in enumerate(player_ids)}
            psi[[row_of[pid] for pid in present]] = torch.tensor(
                aligned, dtype=torch.float32, device=args.device
            )
        posterior["psi"] = psi
    if args.calibrate_correctness:
        calibration = _load_calibration(train_bonus / "summary.json", args.device)
        if calibration is None:
            raise ValueError(
                "--calibrate-correctness set but training bonus summary.json has "
                "no correctness_scale/bias"
            )
        posterior["correctness_scale"], posterior["correctness_bias"] = calibration

    probabilities, aggregates, synergy = posterior_predictions(
        data, theta, posterior, args.use_synergy, args.calibrate_correctness
    )
    save_bonus_predictions(
        args.output_dir, observations, probabilities, aggregates, synergy
    )
    summary = {
        "frozen_predict": True,
        "split": args.split,
        "tournament": args.tournament or "",
        "use_synergy": args.use_synergy,
        "calibrate_correctness": args.calibrate_correctness,
        "skill_dimensions": dimensions,
        "bonus_part_observations": len(observations),
        "bonus_parts": len(data["part_ids"]),
        "tau": float(posterior["tau"].detach().cpu()),
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
