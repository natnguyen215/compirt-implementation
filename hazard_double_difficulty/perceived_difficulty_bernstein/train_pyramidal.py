"""Train the shared-difficulty player-perception Bernstein model."""

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
    tossup_tensors,
)
from hazard_double_difficulty.perceived_difficulty_bernstein.pyramidal_model import (
    DEFAULT_DROP_CONCENTRATION,
    DEFAULT_RELEVANCE_CONCENTRATION,
    ALPHA_PRIOR_LOGNORMAL,
    ALPHA_LOG_SCALE,
    MIN_DEGREE,
    PERCEPTION_SLICE_NAMES,
    SUPPORTED_DEGREES,
    SUPPORTED_ALPHA_PRIORS,
    SUPPORTED_PERCEPTION_SLICES,
    TOTAL_DROP_LOG_SCALE,
    competing_risks_model,
    expected_first_buzz_positions,
    posterior_row_predictions,
    validate_concentration,
)
from utils.posterior import add_posterior_output_args
from utils.saving import (
    add_numbered_tensor_columns,
    save_loss_plot,
    save_tossup_predictions,
    tensor_values,
    write_summary,
)
from utils.training import (
    convergence_summary,
    fit_svi,
    fit_svi_alternating,
    require_device,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = (
    REPO_ROOT
    / "results"
    / "compirt"
    / "in_sample"
    / "double-difficulty"
    / "perceived-difficulty-positive-alpha-bernstein-332"
)
SLICED_DEFAULT_OUTPUT_DIR = (
    REPO_ROOT
    / "results"
    / "compirt"
    / "in_sample"
    / "double-difficulty"
    / "perceived-difficulty-three-slice-positive-alpha-bernstein-332"
)
MODEL_NAME = "perceived-difficulty-bernstein-competing-risks"
PARAMETER_SCHEMA = "perceived-difficulty-bernstein"
SLICED_MODEL_NAME = "perceived-difficulty-sliced-bernstein-competing-risks"
SLICED_PARAMETER_SCHEMA = "perceived-difficulty-sliced-bernstein"
JOINT_OPTIMIZATION = "joint"
ALTERNATING_PLAYER_OPTIMIZATION = "alternating-theta-perception"
FORMULA = (
    "correctness_ij(x) = sum_k r_jk * (theta_ik - d_jk(x)); "
    "hazard_ij(x) = sum_k r_jk * "
    "(theta_ik - alpha_ik * d_jk(x) + beta_ik)"
)
SLICED_FORMULA = (
    "correctness_ij(x) = sum_k r_jk * (theta_ik - d_jk(x)); "
    "hazard_ij(x) = sum_k r_jk * "
    "(theta_ik - alpha_i,s(x),k * d_jk(x) + beta_i,s(x),k)"
)


def save_perceived_parameters(output_dir, data, posterior):
    """Save player perception vectors and the one shared item curve."""
    players = {"player_id": data["player_ids"]}
    add_numbered_tensor_columns(players, "theta", posterior["theta"])
    alpha = tensor_values(posterior["alpha"])
    beta = tensor_values(posterior["beta"])
    if alpha.shape != beta.shape:
        raise ValueError("alpha and beta perception shapes must match")
    if alpha.ndim == 2:
        add_numbered_tensor_columns(players, "alpha", posterior["alpha"])
        add_numbered_tensor_columns(players, "beta", posterior["beta"])
    elif alpha.ndim == 3 and alpha.shape[1] == len(PERCEPTION_SLICE_NAMES):
        for slice_index, slice_name in enumerate(PERCEPTION_SLICE_NAMES):
            for dimension in range(alpha.shape[2]):
                suffix = f"{slice_name}_{dimension + 1}"
                players[f"alpha_{suffix}"] = alpha[:, slice_index, dimension]
                players[f"beta_{suffix}"] = beta[:, slice_index, dimension]
    else:
        raise ValueError(
            "Perception parameters must have shape (players, dimensions) or "
            f"(players, 3, dimensions), got {alpha.shape}"
        )
    player_frame = pd.DataFrame(players)
    player_frame["theta_norm"] = np.linalg.norm(
        player_frame.filter(regex=r"^theta_\d+$").to_numpy(), axis=1
    )
    player_frame.to_csv(output_dir / "players.csv", index=False)

    tossups = {"tossup_id": data["tossup_ids"]}
    add_numbered_tensor_columns(tossups, "r", posterior["r"])
    start = tensor_values(posterior["start_difficulty"])
    total = tensor_values(posterior["total_drop"])
    shares = tensor_values(posterior["drop_proportions"])
    for dimension in range(start.shape[1]):
        suffix = f"d{dimension + 1}"
        tossups[f"start_difficulty_{suffix}"] = start[:, dimension]
        tossups[f"end_difficulty_{suffix}"] = (
            start[:, dimension] - total[:, dimension]
        )
        tossups[f"total_drop_{suffix}"] = total[:, dimension]
        for share in range(shares.shape[2]):
            tossups[f"drop_share_{share + 1}_{suffix}"] = shares[
                :, dimension, share
            ]
    pd.DataFrame(tossups).to_csv(output_dir / "tossups.csv", index=False)


def run_experiment(args, *, tables=None):
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
    data = tossup_tensors(observations, args.device)
    print(
        f"Rows: {len(observations):,}  Players: {len(data['player_ids']):,}  "
        f"Tossups: {len(data['tossup_ids']):,}"
    )
    print(observations["z"].value_counts().to_string())

    model_kwargs = {
        "data": data,
        "n_dimensions": args.dimensions,
        "degree": args.degree,
        "relevance_concentration": args.relevance_concentration,
        "drop_concentration": args.drop_concentration,
        "perception_slices": args.perception_slices,
        "alpha_prior": args.alpha_prior,
    }
    fit_kwargs = {
        "model_kwargs": model_kwargs,
        "n_steps": args.steps,
        "lr": args.lr,
        "posterior_output_dir": args.output_dir,
        "posterior_draws": args.posterior_draws,
        "posterior_seed": args.seed,
    }
    if args.alternate_player_steps:
        posterior, _guide, losses = fit_svi_alternating(
            competing_risks_model,
            frozen_site_cycle=(("alpha", "beta"), ("theta",)),
            **fit_kwargs,
        )
    else:
        posterior, _guide, losses = fit_svi(
            competing_risks_model,
            **fit_kwargs,
        )
    save_perceived_parameters(args.output_dir, data, posterior)
    save_loss_plot(
        args.output_dir, losses, "Perceived Bernstein CompIRT training loss"
    )
    correct, hazard, survival = posterior_row_predictions(data, posterior)
    save_tossup_predictions(
        args.output_dir,
        observations,
        correct,
        hazard,
        survival,
        buzz_expected=expected_first_buzz_positions(data, posterior),
    )

    item_parameters = (
        args.dimensions * args.degree + 2 * args.dimensions - 1
    )
    sliced = args.perception_slices == len(PERCEPTION_SLICE_NAMES)
    player_parameters = args.dimensions * (1 + 2 * args.perception_slices)
    summary = {
        "model": SLICED_MODEL_NAME if sliced else MODEL_NAME,
        "parameter_schema": SLICED_PARAMETER_SCHEMA if sliced else PARAMETER_SCHEMA,
        "formula": SLICED_FORMULA if sliced else FORMULA,
        "difficulty_family": "monotone_bernstein_polynomial",
        "difficulty_coupling": "shared_correctness_hazard",
        "relevance_coupling": "shared_simplex",
        "perception_multiplier": (
            "player_slice_dimension_alpha" if sliced else "player_dimension_alpha"
        ),
        "perception_intercept": (
            "player_slice_dimension_beta" if sliced else "player_dimension_beta"
        ),
        "perception_slices": args.perception_slices,
        "perception_slice_names": (
            list(PERCEPTION_SLICE_NAMES) if sliced else ["all"]
        ),
        "perception_slice_boundaries": (
            [1.0 / 3.0, 2.0 / 3.0] if sliced else []
        ),
        "theta_prior": "Normal(0, 1) per dimension",
        "alpha_prior": {
            "lognormal": f"LogNormal(0, {ALPHA_LOG_SCALE})",
            "normal-zero": "Normal(0, 1)",
            "normal-one": "Normal(1, 1)",
        }[args.alpha_prior],
        "alpha_prior_sharing": (
            "independent_per_player_slice_dimension"
            if sliced
            else "independent_per_player_dimension"
        ),
        "alpha_constraint": (
            "positive" if args.alpha_prior == ALPHA_PRIOR_LOGNORMAL else "unconstrained"
        ),
        "beta_prior": "Normal(0, 1)",
        "beta_prior_sharing": (
            "independent_per_player_slice_dimension"
            if sliced
            else "independent_per_player_dimension"
        ),
        "relevance_prior": f"Dirichlet({args.relevance_concentration})",
        "polynomial_degree": args.degree,
        "polynomial_basis": "strictly-decreasing-bernstein",
        "relevance_concentration": args.relevance_concentration,
        "drop_concentration": args.drop_concentration,
        "start_difficulty_prior": "Normal(0, 1) per dimension",
        "total_drop_prior": f"LogNormal(0, {TOTAL_DROP_LOG_SCALE})",
        "drop_share_prior": f"Dirichlet({args.drop_concentration}) per dimension",
        "split": args.split,
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "steps": args.steps,
        "optimization_schedule": (
            ALTERNATING_PLAYER_OPTIMIZATION
            if args.alternate_player_steps
            else JOINT_OPTIMIZATION
        ),
        "alternating_step_cycle": (
            [
                {
                    "step_modulo": 0,
                    "train_player_sites": ["theta"],
                    "frozen_player_sites": ["alpha", "beta"],
                },
                {
                    "step_modulo": 1,
                    "train_player_sites": ["alpha", "beta"],
                    "frozen_player_sites": ["theta"],
                },
            ]
            if args.alternate_player_steps
            else []
        ),
        "other_parameter_schedule": "trainable_every_step",
        "always_trainable_sites": [
            "r",
            "start_difficulty",
            "total_drop",
            "drop_proportions",
        ],
        "lr": args.lr,
        "seed": args.seed,
        **convergence_summary(losses),
        "players": len(data["player_ids"]),
        "tossups": len(data["tossup_ids"]),
        "events": len(data["event_ids"]),
        "effective_item_parameters": item_parameters,
        "effective_parameter_count": (
            len(data["player_ids"]) * player_parameters
            + len(data["tossup_ids"]) * item_parameters
        ),
        "terminal_intercepts": False,
        "terminal_no_buzz_survival": "tokens_1_through_T",
        "include_bounceback": args.include_bounceback,
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
    write_summary(args.output_dir, summary, posterior)
    return summary


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    add_posterior_output_args(parser)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument(
        "--degree", type=int, choices=SUPPORTED_DEGREES, default=MIN_DEGREE
    )
    parser.add_argument("--dimensions", type=int, default=3)
    parser.add_argument(
        "--alpha-prior",
        choices=SUPPORTED_ALPHA_PRIORS,
        default=ALPHA_PRIOR_LOGNORMAL,
        help=(
            "player alpha prior: positive LogNormal(0,1), unconstrained "
            "Normal(0,1), or unconstrained Normal(1,1)"
        ),
    )
    parser.add_argument(
        "--perception-slices",
        type=int,
        choices=SUPPORTED_PERCEPTION_SLICES,
        default=1,
        help="player alpha/beta position slices (default: 1; experiment: 3)",
    )
    parser.add_argument(
        "--relevance-concentration",
        type=float,
        default=DEFAULT_RELEVANCE_CONCENTRATION,
    )
    parser.add_argument(
        "--drop-concentration", type=float, default=DEFAULT_DROP_CONCENTRATION
    )
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument(
        "--alternate-player-steps",
        action="store_true",
        help=(
            "for three-slice perception, alternate theta-only and "
            "alpha/beta-only player updates; all item sites update every step"
        ),
    )
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--include-bounceback", action="store_true")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args(argv)
    if args.output_dir is None:
        args.output_dir = (
            SLICED_DEFAULT_OUTPUT_DIR
            if args.perception_slices == len(PERCEPTION_SLICE_NAMES)
            else DEFAULT_OUTPUT_DIR
        )
    if args.dimensions < 1:
        parser.error("--dimensions must be at least 1")
    if args.steps < 1:
        parser.error("--steps must be at least 1")
    if args.alternate_player_steps and args.perception_slices != 3:
        parser.error("--alternate-player-steps requires --perception-slices 3")
    for name in ("relevance_concentration", "drop_concentration"):
        try:
            validate_concentration(getattr(args, name), name)
        except ValueError as error:
            parser.error(str(error))
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
