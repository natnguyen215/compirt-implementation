"""Train Bernstein 332 with a scalar affine buzz-logit transform per player."""

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
from hazard_double_difficulty.perceived_logit_bernstein.pyramidal_model import (
    ALPHA_LOG_SCALE,
    DEFAULT_DROP_CONCENTRATION,
    DEFAULT_RELEVANCE_CONCENTRATION,
    MIN_DEGREE,
    SUPPORTED_DEGREES,
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
from utils.training import convergence_summary, fit_svi, require_device


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = (
    REPO_ROOT
    / "results"
    / "compirt"
    / "in_sample"
    / "double-difficulty"
    / "perceived-logit-positive-alpha-bernstein-332"
)
MODEL_NAME = "perceived-logit-bernstein-competing-risks"
PARAMETER_SCHEMA = "perceived-logit-bernstein"
FORMULA = (
    "correctness_ij(x) = sum_k r_jk * (theta_ik - d_jk(x)); "
    "hazard_ij(x) = alpha_i * correctness_ij(x) + beta_i"
)


def save_perceived_logit_parameters(output_dir, data, posterior):
    """Save scalar player transform parameters and the shared item curve."""
    players = {
        "player_id": data["player_ids"],
        "alpha": tensor_values(posterior["alpha"]),
        "beta": tensor_values(posterior["beta"]),
    }
    add_numbered_tensor_columns(players, "theta", posterior["theta"])
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

    posterior, _guide, losses = fit_svi(
        competing_risks_model,
        model_kwargs={
            "data": data,
            "n_dimensions": args.dimensions,
            "degree": args.degree,
            "relevance_concentration": args.relevance_concentration,
            "drop_concentration": args.drop_concentration,
        },
        n_steps=args.steps,
        lr=args.lr,
        posterior_output_dir=args.output_dir,
        posterior_draws=args.posterior_draws,
        posterior_seed=args.seed,
    )
    save_perceived_logit_parameters(args.output_dir, data, posterior)
    save_loss_plot(
        args.output_dir, losses, "Perceived-logit Bernstein CompIRT training loss"
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

    item_parameters = args.dimensions * args.degree + 2 * args.dimensions - 1
    summary = {
        "model": MODEL_NAME,
        "parameter_schema": PARAMETER_SCHEMA,
        "formula": FORMULA,
        "difficulty_family": "monotone_bernstein_polynomial",
        "difficulty_coupling": "shared_correctness_hazard",
        "relevance_coupling": "shared_simplex",
        "perception_multiplier": "player_scalar_alpha",
        "perception_intercept": "player_scalar_beta",
        "theta_prior": "Normal(0, 1) per dimension",
        "alpha_prior": f"LogNormal(0, {ALPHA_LOG_SCALE})",
        "alpha_constraint": "positive",
        "beta_prior": "Normal(0, 1)",
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
        "lr": args.lr,
        "seed": args.seed,
        **convergence_summary(losses),
        "players": len(data["player_ids"]),
        "tossups": len(data["tossup_ids"]),
        "events": len(data["event_ids"]),
        "effective_item_parameters": item_parameters,
        "effective_parameter_count": (
            len(data["player_ids"]) * (args.dimensions + 2)
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
        "--relevance-concentration",
        type=float,
        default=DEFAULT_RELEVANCE_CONCENTRATION,
    )
    parser.add_argument(
        "--drop-concentration", type=float, default=DEFAULT_DROP_CONCENTRATION
    )
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--include-bounceback", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args(argv)
    if args.dimensions < 1:
        parser.error("--dimensions must be at least 1")
    if args.steps < 1:
        parser.error("--steps must be at least 1")
    for name in ("relevance_concentration", "drop_concentration"):
        try:
            validate_concentration(getattr(args, name), name)
        except ValueError as error:
            parser.error(str(error))
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
