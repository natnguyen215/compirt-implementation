"""Train clue-aligned linear-spline double-difficulty CompIRT."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import pyro

from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
)
from dd_linear_spline.clues import build_spline_tensors
from dd_linear_spline.pyramidal_model import (
    competing_risks_model,
    expected_first_buzz_positions,
    materialize_spline_landmarks,
    posterior_row_predictions,
)
from holdout.player_priors import attach_player_priors, player_tier_map
from utils.posterior import add_posterior_output_args
from utils.saving import (
    add_numbered_tensor_columns,
    save_loss_plot,
    save_player_posterior,
    save_tossup_predictions,
    tensor_values,
    write_summary,
)
from utils.training import convergence_summary, fit_svi, require_device


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = (
    REPO_ROOT / "results" / "compirt" / "in_sample" / "dd-linear-spline-pyramidal"
)
MODEL_NAME = "dd-linear-spline"


def _padded_landmarks(data, values):
    """Return ``(tossups, max_knots, dimensions)`` landmark values with NaNs."""
    values = tensor_values(values)
    counts = data["spline_knot_counts"].detach().cpu().numpy()
    indices = data["spline_knot_indices"].detach().cpu().numpy()
    padded = np.full(
        (len(data["tossup_ids"]), indices.shape[1], values.shape[1]),
        np.nan,
        dtype=float,
    )
    for tossup, count in enumerate(counts):
        padded[tossup, :count] = values[indices[tossup, :count]]
    return padded


def save_spline_parameters(output_dir, data, posterior):
    """Save standard player parameters and wide, variable-length spline columns."""
    players = {"player_id": data["player_ids"], "c": tensor_values(posterior["c"])}
    add_numbered_tensor_columns(players, "theta", posterior["theta"])
    player_frame = pd.DataFrame(players)
    player_frame["theta_norm"] = np.linalg.norm(
        player_frame.filter(like="theta_").to_numpy(), axis=1
    )
    player_frame.to_csv(output_dir / "players.csv", index=False)

    correct_y = _padded_landmarks(data, posterior["spline_y_correct"])
    hazard_y = _padded_landmarks(data, posterior["spline_y_hazard"])
    knot_x = data["spline_knot_positions"].detach().cpu().numpy().astype(float)
    counts = data["spline_knot_counts"].detach().cpu().numpy()
    tossups = {
        "tossup_id": data["tossup_ids"],
        "clue_count": counts - 1,
    }
    add_numbered_tensor_columns(tossups, "r", posterior["r_correct"])
    add_numbered_tensor_columns(tossups, "hazard_r", posterior["r_hazard"])
    for knot in range(knot_x.shape[1]):
        valid = knot < counts
        tossups[f"spline_knot_x_{knot}"] = np.where(
            valid, knot_x[:, knot], np.nan
        )
        for dimension in range(correct_y.shape[2]):
            suffix = f"{knot}_d{dimension + 1}"
            tossups[f"spline_y_{suffix}"] = correct_y[:, knot, dimension]
            tossups[f"hazard_spline_y_{suffix}"] = hazard_y[:, knot, dimension]
    pd.DataFrame(tossups).to_csv(output_dir / "tossups.csv", index=False)


def run_experiment(args, *, tables=None, monotone_decreasing=False):
    """Run load, spline construction, fitting, prediction, and saving."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)
    if tables is None:
        tables = load_hf_tables(args.data_dir, args.split)
    tables = filter_tournament(tables, args.tournament)
    observations = build_tossup_observations(
        tables, include_bounceback=args.include_bounceback
    )
    if observations.empty:
        raise ValueError("No tossup observations matched the requested data selection")
    data = build_spline_tensors(observations, tables["tossups"], args.device)
    print(
        f"Rows: {len(observations):,}  "
        f"Players: {len(data['player_ids']):,}  "
        f"Tossups: {len(data['tossup_ids']):,}  "
        f"Knots: {data['n_spline_knots']:,}"
    )

    tier_map = player_tier_map(tables)
    if args.train_posterior:
        prior_summary = attach_player_priors(
            data,
            tables,
            args.train_posterior,
            args.new_player_prior,
            args.device,
            n_dimensions=args.dimensions,
            tier_map=tier_map,
        )
        print(f"Held-out player priors: {prior_summary}")

    posterior, guide, losses = fit_svi(
        competing_risks_model,
        model_kwargs={
            "data": data,
            "n_dimensions": args.dimensions,
            "calibrate_correctness": args.calibrate_correctness,
            "calibrate_scale": not args.calibration_no_scale,
            "monotone_decreasing": monotone_decreasing,
            "terminal_intercepts": args.terminal_intercepts,
        },
        n_steps=args.steps,
        lr=args.lr,
        posterior_output_dir=args.output_dir,
        posterior_draws=args.posterior_draws,
        posterior_seed=args.seed,
    )
    posterior = materialize_spline_landmarks(data, posterior)
    save_spline_parameters(args.output_dir, data, posterior)
    save_player_posterior(args.output_dir, data["player_ids"], guide, tier_map)
    save_loss_plot(
        args.output_dir, losses, "Linear-spline double-difficulty training loss"
    )
    correct, hazard, survival = posterior_row_predictions(
        data,
        posterior,
        args.calibrate_correctness,
        calibrate_scale=not args.calibration_no_scale,
    )
    save_tossup_predictions(
        args.output_dir,
        observations,
        correct,
        hazard,
        survival,
        buzz_expected=expected_first_buzz_positions(data, posterior),
    )

    knot_counts = data["spline_knot_counts"].detach().cpu().numpy()
    calibration_parameters = (
        0
        if not args.calibrate_correctness
        else (1 if args.calibration_no_scale else 2)
    )
    effective_count = (
        len(data["player_ids"]) * (args.dimensions + 1)
        + len(data["tossup_ids"]) * 2 * args.dimensions
        + data["n_spline_knots"] * 2 * args.dimensions
        + calibration_parameters
    )
    summary = {
        "model": (
            "dd-monotone-linear-spline" if monotone_decreasing else MODEL_NAME
        ),
        "formula": (
            "correctness=sum_k r_correct_jk*(theta_ik-d_correct_jk(x)); "
            "hazard=sum_k r_hazard_jk*(theta_ik-d_hazard_jk(x))-c_i"
        ),
        "difficulty_family": (
            "clue_aligned_monotone_decreasing_linear_spline"
            if monotone_decreasing
            else "clue_aligned_linear_spline"
        ),
        "difficulty_coupling": "separate_correctness_hazard",
        "relevance_coupling": "separate_correctness_hazard",
        "clue_segmentation": "protected_sentence_v1",
        "landmark_prior": (
            "start=Normal(0, 1); successive_drop=HalfNormal(0.5)"
            if monotone_decreasing
            else "Normal(0, 1)"
        ),
        "monotone_decreasing": monotone_decreasing,
        "split": args.split,
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "steps": args.steps,
        "lr": args.lr,
        "seed": args.seed,
        "players": len(data["player_ids"]),
        "tossups": len(data["tossup_ids"]),
        "events": len(data["event_ids"]),
        "spline_knots": int(data["n_spline_knots"]),
        "min_knots_per_tossup": int(knot_counts.min()),
        "median_knots_per_tossup": float(np.median(knot_counts)),
        "max_knots_per_tossup": int(knot_counts.max()),
        "effective_parameter_count": int(effective_count),
        "calibrate_correctness": args.calibrate_correctness,
        "calibration_no_scale": args.calibration_no_scale,
        "include_bounceback": args.include_bounceback,
        "terminal_intercepts": args.terminal_intercepts,
        "terminal_no_buzz_survival": "tokens_1_through_T",
        "observation_counts": observations["z"].value_counts().to_dict(),
        **convergence_summary(losses),
    }
    write_summary(args.output_dir, summary, posterior)
    return summary


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    add_posterior_output_args(parser)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--dimensions", type=int, default=1)
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--calibrate-correctness", action="store_true")
    parser.add_argument("--calibration-no-scale", action="store_true")
    parser.add_argument("--include-bounceback", action="store_true")
    parser.add_argument(
        "--no-terminal-intercepts",
        dest="terminal_intercepts",
        action="store_false",
        help="drop the final-cell correctness/hazard intercepts (pre-2026-08 "
        "behaviour; only for the terminal-cell ablation)",
    )
    parser.add_argument("--train-posterior", type=Path)
    parser.add_argument(
        "--new-player-prior", choices=("tier", "flat"), default="tier"
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args(argv)
    if args.dimensions < 1:
        parser.error("--dimensions must be at least 1")
    if args.steps < 1:
        parser.error("--steps must be at least 1")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
