"""Train the monotone Bernstein double-difficulty CompIRT tossup model.

The trainer fits 'hazard_double_difficulty.bernstein.pyramidal_model', which
learns one strictly-decreasing Bernstein difficulty curve for correctness and a
second, independent one for the buzz hazard. Both are saved in their
interpretable form rather than as raw Bernstein control values:

    r_1..K, hazard_r_1..K,
    start_difficulty_dK, end_difficulty_dK, total_drop_dK, drop_share_M_dK
        (correctness curve)
    hazard_start_difficulty_dK, hazard_end_difficulty_dK, hazard_total_drop_dK,
    hazard_drop_share_M_dK
        (hazard curve)

The correctness curve keeps the canonical parent column names so 'compirt_eval'
reads it as *the* difficulty curve — which is the right one for answer-difficulty
plots. See this package's README for the timing-replay caveat that follows.

'run_experiment' coordinates the load -> build -> tensors -> train -> predict ->
save workflow. The saved 'players.csv' is compatible with
'train_compositional.py'.
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
from hazard_double_difficulty.bernstein.pyramidal_model import (
    CURVE_LOCATION_PRIOR_SCALE,
    CURVE_START_PRIOR_SCALE,
    DEFAULT_DROP_CONCENTRATION,
    DEFAULT_RELEVANCE_PRIOR,
    MIN_DEGREE,
    SUPPORTED_DEGREES,
    SUPPORTED_RELEVANCE_PRIORS,
    TOTAL_DROP_LOG_SCALE,
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
    REPO_ROOT / "results" / "compirt" / "in_sample" / "dd-bernstein-pyramidal"
)
MODEL_NAME = "bernstein-double-difficulty-competing-risks"
FORMULA = (
    "correctness_ij(x) = sum_k r_correct_jk * (theta_ik - d_correct_jk(x)); "
    "hazard_ij(x) = sum_k r_hazard_jk * (theta_ik - d_hazard_jk(x)) - c_i"
)
BASIS_NAME = "strictly-decreasing-bernstein"


def add_curve_columns(tossups, prefix, start, total_drop, shares):
    """Add one curve's start/end/total-drop/share columns under 'prefix'.

    'prefix' is empty for the correctness curve, which therefore keeps the parent
    family's canonical column names.
    """
    for dimension in range(start.shape[1]):
        suffix = f"d{dimension + 1}"
        tossups[f"{prefix}start_difficulty_{suffix}"] = start[:, dimension]
        tossups[f"{prefix}end_difficulty_{suffix}"] = (
            start[:, dimension] - total_drop[:, dimension]
        )
        tossups[f"{prefix}total_drop_{suffix}"] = total_drop[:, dimension]
        for share in range(shares.shape[2]):
            tossups[f"{prefix}drop_share_{share + 1}_{suffix}"] = (
                shares[:, dimension, share]
            )


def save_double_difficulty_parameters(output_dir, data, posterior):
    """Write Stage-2-compatible player parameters and both fitted curves.

    The curves are saved as start/end/total-drop/shares rather than as Bernstein
    control values, so 'compirt_eval' can replay them and a reader can see what
    each number means without reconstructing the basis. The hazard curve is
    prefixed, which the evaluation column regexes ignore rather than mis-parse.
    """
    players = {
        "player_id": data["player_ids"],
        "c": tensor_values(posterior["c"]),
    }
    if "a" in posterior:
        players["a"] = tensor_values(posterior["a"])
    add_numbered_tensor_columns(players, "theta", posterior["theta"])
    player_frame = pd.DataFrame(players)
    player_frame["theta_norm"] = np.linalg.norm(
        player_frame.filter(like="theta_").to_numpy(), axis=1
    )
    player_frame.to_csv(output_dir / "players.csv", index=False)

    tossups = {"tossup_id": data["tossup_ids"]}
    add_numbered_tensor_columns(tossups, "r", posterior["r_correct"])
    add_numbered_tensor_columns(tossups, "hazard_r", posterior["r_hazard"])
    for prefix, suffix in (("", "correct"), ("hazard_", "hazard")):
        add_curve_columns(
            tossups,
            prefix,
            tensor_values(posterior[f"start_difficulty_{suffix}"]),
            tensor_values(posterior[f"total_drop_{suffix}"]),
            tensor_values(posterior[f"drop_proportions_{suffix}"]),
        )
    pd.DataFrame(tossups).to_csv(output_dir / "tossups.csv", index=False)


def run_experiment(args, *, tables=None):
    """Run the complete monotone double-difficulty training pipeline.

    'tables' injects already-built HuggingFace tables; the tests use it to run
    the whole pipeline on synthetic data.
    """
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)

    # Load tables -> build BUZZ/CENSORED/NO-BUZZ rows -> index into tensors.
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
        f"Rows: {len(observations):,}  "
        f"Players: {len(data['player_ids']):,}  "
        f"Tossups: {len(data['tossup_ids']):,}"
    )
    print(observations["z"].value_counts().to_string())

    # Each player's tier labels the saved posterior and builds new-player priors.
    tier_map = player_tier_map(tables)
    # Held-out evaluation: attach informative player priors before fitting.
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
            "degree": args.degree,
            "drop_concentration": args.drop_concentration,
            "calibrate_correctness": args.calibrate_correctness,
            "calibrate_scale": not args.calibration_no_scale,
            "terminal_intercepts": args.terminal_intercepts,
            "relevance_prior": args.relevance_prior,
            "learned_curve_locations": args.learn_curve_locations,
            "incorrect_weight": args.incorrect_weight,
            "player_neg_propensity": args.player_neg_propensity,
        },
        n_steps=args.steps,
        lr=args.lr,
        posterior_output_dir=args.output_dir,
        posterior_draws=args.posterior_draws,
        posterior_seed=args.seed,
    )

    save_double_difficulty_parameters(args.output_dir, data, posterior)
    # Save the full theta/c posterior plus tiers so a later held-out run can
    # rebuild returning-player and tier-conditioned priors.
    save_player_posterior(args.output_dir, data["player_ids"], guide, tier_map)
    save_loss_plot(
        args.output_dir, losses, "Bernstein double-difficulty CompIRT training loss"
    )

    # Attach fitted predictions back onto the readable observation rows.
    correct, hazard, survival = posterior_row_predictions(
        data,
        posterior,
        args.calibrate_correctness,
        calibrate_scale=not args.calibration_no_scale,
    )
    buzz_expected = expected_first_buzz_positions(data, posterior)
    save_tossup_predictions(
        args.output_dir,
        observations,
        correct,
        hazard,
        survival,
        buzz_expected=buzz_expected,
    )

    relevance_parameters = (
        2 * (args.dimensions - 1)
        if args.relevance_prior == "simplex"
        else 2 * args.dimensions
    )
    curve_parameters = 2 * args.dimensions * (args.degree + 1)
    effective_item_parameters = relevance_parameters + curve_parameters
    global_parameters = (
        2 * int(args.learn_curve_locations)
        + 2 * int(args.terminal_intercepts)
        + int(args.player_neg_propensity)
    )
    summary = {
        "model": MODEL_NAME,
        "formula": (
            FORMULA + "; correctness_ij(x) += a_i"
            if args.player_neg_propensity
            else FORMULA
        ),
        "difficulty_family": "monotone_bernstein_polynomial",
        "difficulty_coupling": "separate_correctness_hazard",
        "relevance_coupling": "separate_correctness_hazard",
        "relevance_prior": (
            f"Dirichlet(ones({args.dimensions}))"
            if args.relevance_prior == "simplex"
            else "Gamma(2, 2)"
        ),
        "relevance_prior_family": args.relevance_prior,
        "polynomial_degree": args.degree,
        "polynomial_basis": BASIS_NAME,
        "drop_concentration": args.drop_concentration,
        "total_drop_prior": f"LogNormal(0, {TOTAL_DROP_LOG_SCALE})",
        "learned_curve_locations": args.learn_curve_locations,
        "curve_location_prior": f"Normal(0, {CURVE_LOCATION_PRIOR_SCALE})",
        "curve_start_prior_scale": CURVE_START_PRIOR_SCALE,
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
        "calibrate_correctness": args.calibrate_correctness,
        "calibration_no_scale": args.calibration_no_scale,
        "effective_item_parameters": effective_item_parameters,
        "global_parameters": global_parameters,
        "effective_parameter_count": (
            len(data["player_ids"])
            * (args.dimensions + 1 + int(args.player_neg_propensity))
            + len(data["tossup_ids"])
            * effective_item_parameters
            + global_parameters
        ),
        "terminal_intercepts": args.terminal_intercepts,
        "terminal_no_buzz_survival": "tokens_1_through_T",
        "include_bounceback": args.include_bounceback,
        "incorrect_weight": args.incorrect_weight,
        "player_neg_propensity": args.player_neg_propensity,
        "player_neg_propensity_prior": (
            "a_scale ~ HalfNormal(1); a_i ~ Normal(0, a_scale)"
            if args.player_neg_propensity
            else "disabled"
        ),
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
    write_summary(args.output_dir, summary, posterior)
    return summary


def parse_args(argv=None):
    """Parse the double-difficulty Bernstein Stage-1 command line."""
    parser = argparse.ArgumentParser(description=__doc__)
    add_posterior_output_args(parser)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument(
        "--degree",
        type=int,
        choices=SUPPORTED_DEGREES,
        default=MIN_DEGREE,
        help="Bernstein degree, shared by the correctness and hazard curves",
    )
    parser.add_argument("--dimensions", type=int, default=1)
    parser.add_argument(
        "--relevance-prior",
        choices=SUPPORTED_RELEVANCE_PRIORS,
        default=DEFAULT_RELEVANCE_PRIOR,
        help="prior for each branch's independent tossup relevance vector; "
        "simplex uses Dirichlet(ones(dimensions))",
    )
    parser.add_argument(
        "--drop-concentration",
        type=float,
        default=DEFAULT_DROP_CONCENTRATION,
        help="symmetric Dirichlet concentration for the positive drop shares; "
        "shared by both curves so they have the same shape prior",
    )
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--calibrate-correctness", action="store_true")
    parser.add_argument(
        "--incorrect-weight",
        type=float,
        default=1.0,
        help="multiplicative loss weight for incorrect observed buzzes",
    )
    parser.add_argument(
        "--player-neg-propensity",
        action="store_true",
        help="add a hierarchical player correctness intercept: learned "
        "a_scale and a_i ~ Normal(0, a_scale)",
    )
    parser.add_argument(
        "--learn-curve-locations",
        action="store_true",
        help="learn separate global population locations for the correctness "
        "and hazard start-difficulty priors",
    )
    parser.add_argument(
        "--no-terminal-intercepts",
        dest="terminal_intercepts",
        action="store_false",
        help="drop the final-cell correctness/hazard intercepts (pre-2026-08 "
        "behaviour; only for the terminal-cell ablation)",
    )
    parser.add_argument(
        "--calibration-no-scale",
        action="store_true",
        help="with --calibrate-correctness, recalibrate with an additive bias "
        "only, keeping the multiplicative scale out of the correctness logit",
    )
    parser.add_argument(
        "--include-bounceback",
        action="store_true",
        help="model the opposing team's post-neg continuation as a phase-1 "
        "risk set (paper Section 3.1 / Appendix A); off by default",
    )
    parser.add_argument(
        "--train-posterior",
        type=Path,
        help="player_posterior.csv from a training run; enables the held-out "
        "transductive pass with informative player priors",
    )
    parser.add_argument(
        "--new-player-prior",
        choices=("tier", "flat"),
        default="tier",
        help="prior for players unseen in training: tier-conditioned or flat",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args(argv)
    if args.dimensions < 1:
        parser.error("--dimensions must be at least 1")
    if args.steps < 1:
        parser.error("--steps must be at least 1")
    if not np.isfinite(args.incorrect_weight) or args.incorrect_weight <= 0:
        parser.error("--incorrect-weight must be finite and greater than zero")
    try:
        validate_drop_concentration(args.drop_concentration)
    except ValueError as error:
        parser.error(str(error))
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
