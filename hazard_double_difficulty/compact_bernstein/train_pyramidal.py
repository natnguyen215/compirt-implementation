"""Train compact scalar-curve double-Bernstein CompIRT.

The saved ``r_1..r_K`` columns are the effective positive discrimination vector
``a_j w_j``.  Saving the product preserves compatibility with the standard
CompIRT evaluator; frozen replay uniquely reconstructs ``a_j = sum_k r_jk`` and
``w_j = r_j / a_j``.
"""

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
from holdout.player_priors import attach_player_priors, player_tier_map
from hazard_double_difficulty.compact_bernstein.pyramidal_model import (
    DEFAULT_DROP_CONCENTRATION,
    MIN_DEGREE,
    SUPPORTED_DEGREES,
    competing_risks_model,
    expected_first_buzz_positions,
    posterior_row_predictions,
    validate_drop_concentration,
)
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


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = (
    REPO_ROOT / "results" / "compirt" / "in_sample" / "compact-double-bernstein"
)
MODEL_NAME = "compact-double-bernstein"


def _add_scalar_curve_columns(tossups, prefix, start, total, shares):
    tossups[f"{prefix}start_difficulty"] = start
    tossups[f"{prefix}end_difficulty"] = start - total
    tossups[f"{prefix}total_drop"] = total
    for index in range(shares.shape[1]):
        tossups[f"{prefix}drop_share_{index + 1}"] = shares[:, index]


def save_compact_parameters(output_dir, data, posterior):
    """Save compact parameters under evaluator- and frozen-replay-compatible names."""
    players = {
        "player_id": data["player_ids"],
        "c": tensor_values(posterior["c"]),
    }
    add_numbered_tensor_columns(players, "theta", posterior["theta"])
    player_frame = pd.DataFrame(players)
    player_frame["theta_norm"] = np.linalg.norm(
        player_frame.filter(like="theta_").to_numpy(), axis=1
    )
    player_frame.to_csv(output_dir / "players.csv", index=False)

    tossups = {"tossup_id": data["tossup_ids"]}
    effective_r = posterior["skill_weights"] * posterior["discrimination"].unsqueeze(-1)
    add_numbered_tensor_columns(tossups, "r", effective_r)
    tossups["discrimination"] = tensor_values(posterior["discrimination"])
    add_numbered_tensor_columns(tossups, "skill_weight", posterior["skill_weights"])
    for prefix, suffix in (("", "correct"), ("hazard_", "hazard")):
        _add_scalar_curve_columns(
            tossups,
            prefix,
            tensor_values(posterior[f"start_difficulty_{suffix}"]),
            tensor_values(posterior[f"total_drop_{suffix}"]),
            tensor_values(posterior[f"drop_proportions_{suffix}"]),
        )
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

    model_kwargs = {
        "data": data,
        "n_dimensions": args.dimensions,
        "degree": args.degree,
        "drop_concentration": args.drop_concentration,
        "learned_curve_locations": args.learn_curve_locations,
        "terminal_intercepts": args.terminal_intercepts,
    }
    posterior, guide, losses = fit_svi(
        competing_risks_model,
        model_kwargs=model_kwargs,
        n_steps=args.steps,
        lr=args.lr,
        posterior_output_dir=args.output_dir,
        posterior_draws=args.posterior_draws,
        posterior_seed=args.seed,
    )
    save_compact_parameters(args.output_dir, data, posterior)
    save_player_posterior(args.output_dir, data["player_ids"], guide, tier_map)
    save_loss_plot(args.output_dir, losses, "Compact double-Bernstein training loss")
    correct, hazard, survival = posterior_row_predictions(data, posterior)
    buzz_expected = expected_first_buzz_positions(data, posterior)
    save_tossup_predictions(
        args.output_dir,
        observations,
        correct,
        hazard,
        survival,
        buzz_expected=buzz_expected,
    )

    # Degree-p scalar curve has p+1 effective parameters: start, total, and
    # p-1 free simplex shares.  The shared skill direction contributes K-1 and
    # discrimination contributes one.
    effective_item_parameters = args.dimensions + 2 * (args.degree + 1)
    global_parameters = 2 * int(args.learn_curve_locations) + 2 * int(
        args.terminal_intercepts
    )
    summary = {
        "model": MODEL_NAME,
        "formula": (
            "correctness=a_j*(w_j dot theta_i)-b_correct_j(x); "
            "hazard=a_j*(w_j dot theta_i)-b_hazard_j(x)-c_i"
        ),
        "difficulty_family": "scalar_monotone_bernstein_polynomial",
        "difficulty_coupling": "separate_correctness_hazard",
        "skill_weights": "simplex",
        "positive_discrimination": True,
        "polynomial_degree": args.degree,
        "drop_concentration": args.drop_concentration,
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
        "effective_item_parameters": effective_item_parameters,
        "global_parameters": global_parameters,
        "effective_parameter_count": (
            len(data["player_ids"]) * (args.dimensions + 1)
            + len(data["tossup_ids"]) * effective_item_parameters
            + global_parameters
        ),
        "learned_curve_locations": args.learn_curve_locations,
        "terminal_intercepts": args.terminal_intercepts,
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
    parser.add_argument("--degree", type=int, choices=SUPPORTED_DEGREES, default=MIN_DEGREE)
    parser.add_argument("--dimensions", type=int, default=3)
    parser.add_argument("--drop-concentration", type=float, default=DEFAULT_DROP_CONCENTRATION)
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--learn-curve-locations", action="store_true")
    parser.add_argument("--terminal-intercepts", action="store_true")
    parser.add_argument("--include-bounceback", action="store_true")
    parser.add_argument("--train-posterior", type=Path)
    parser.add_argument("--new-player-prior", choices=("tier", "flat"), default="tier")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args(argv)
    if args.dimensions < 1:
        parser.error("--dimensions must be at least 1")
    if args.steps < 1:
        parser.error("--steps must be at least 1")
    try:
        validate_drop_concentration(args.drop_concentration)
    except ValueError as error:
        parser.error(str(error))
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
