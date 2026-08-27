"""Train the multidimensional-difficulty CompIRT tossup model.

The trainer fits 'multidimensional.multidim_mirt.pyramidal_model' and saves
vector-valued tossup difficulty parameters:

    r_1..K, beta_1..K, gamma_1..K, mu_1..K

The relevance weight is saved in 'r_1..K'.

'run_experiment' coordinates the load -> build -> tensors -> train -> predict ->
save workflow. The saved 'players.csv' is compatible with
'train_compositional.py'.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pyro

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from compirt_eval.diagnostics.posterior_predictive import save_pyramidal_ppc
from holdout.player_priors import attach_player_priors, player_tier_map
from multidimensional.multidim_mirt.pyramidal_model import (
    competing_risks_model,
    expected_first_buzz_positions,
    posterior_row_predictions,
)
from compirt_eval.drop_robustness.perturbations import (
    drop_tossup_events,
    load_event_drop_list,
)
from utils.saving import (
    add_numbered_tensor_columns,
    save_loss_plot,
    save_player_posterior,
    save_tossup_predictions,
    tensor_values,
    write_summary,
)
from utils.training import fit_svi, require_device
from utils.posterior import add_posterior_output_args


DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "multidim-pyramidal"
FORMULA = "logit_ij(t) = sum_k r_jk * (theta_ik - d_jk(t))"


def save_multidim_parameters(output_dir, data, posterior):
    """Write player and vector-valued tossup parameters to CSV files."""
    players = {
        "player_id": data["player_ids"],
        "c": tensor_values(posterior["c"]),
    }
    add_numbered_tensor_columns(players, "theta", posterior["theta"])
    player_df = pd.DataFrame(players)
    player_df["theta_norm"] = np.linalg.norm(
        player_df.filter(like="theta_").to_numpy(), axis=1
    )
    player_df.to_csv(output_dir / "players.csv", index=False)

    tossups = {"tossup_id": data["tossup_ids"]}
    add_numbered_tensor_columns(tossups, "r", posterior["r"])
    add_numbered_tensor_columns(tossups, "beta", posterior["beta"])
    add_numbered_tensor_columns(tossups, "gamma", posterior["gamma"])
    add_numbered_tensor_columns(tossups, "mu", posterior["mu"])
    pd.DataFrame(tossups).to_csv(output_dir / "tossups.csv", index=False)


def run_experiment(args):
    """Run the complete multidimensional-difficulty training pipeline."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)

    # Load tables -> build BUZZ/CENSORED/NO-BUZZ rows -> index into tensors.
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    observations = build_tossup_observations(
        tables, include_bounceback=args.include_bounceback
    )
    if observations.empty:
        raise ValueError("No tossup observations matched the requested data selection")
    # Robustness studies pass a drop list to refit without the listed events.
    drop_info = None
    if args.drop_events:
        observations, drop_info = drop_tossup_events(
            observations, load_event_drop_list(args.drop_events)
        )
        print(f"Dropped events: {drop_info}")
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
            "calibrate_correctness": args.calibrate_correctness,
            "calibrate_scale": not args.calibration_no_scale,
            "link": args.difficulty_link,
        },
        n_steps=args.steps,
        lr=args.lr,
        posterior_output_dir=args.output_dir,
        posterior_draws=args.posterior_draws,
        posterior_seed=args.seed,
    )

    save_multidim_parameters(args.output_dir, data, posterior)
    # Save the full theta/c posterior plus tiers so a later held-out run can
    # rebuild returning-player and tier-conditioned priors.
    save_player_posterior(args.output_dir, data["player_ids"], guide, tier_map)
    save_loss_plot(
        args.output_dir, losses, "Multidimensional-difficulty IRT training loss"
    )

    # Attach fitted predictions back onto the readable observation rows.
    correct, hazard, survival = posterior_row_predictions(
        data,
        posterior,
        args.calibrate_correctness,
        args.difficulty_link,
        calibrate_scale=not args.calibration_no_scale,
    )
    buzz_expected = expected_first_buzz_positions(
        data, posterior, args.difficulty_link
    )
    save_tossup_predictions(
        args.output_dir, observations, correct, hazard, survival, buzz_expected=buzz_expected
    )
    save_pyramidal_ppc(
        args.output_dir,
        observations,
        data,
        guide,
        {
            "data": data,
            "n_dimensions": args.dimensions,
            "calibrate_correctness": args.calibrate_correctness,
            "calibrate_scale": not args.calibration_no_scale,
            "link": args.difficulty_link,
        },
        draws=args.ppc_draws,
        max_events=args.ppc_max_events,
        seed=args.seed,
    )

    summary = {
        "model": "multidimensional-difficulty-competing-risks",
        "formula": FORMULA,
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "difficulty_link": args.difficulty_link,
        "seed": args.seed,
        "steps": args.steps,
        "final_loss": losses[-1],
        "players": len(data["player_ids"]),
        "tossups": len(data["tossup_ids"]),
        "events": len(data["event_ids"]),
        "calibrate_correctness": args.calibrate_correctness,
        "calibration_no_scale": args.calibration_no_scale,
        "include_bounceback": args.include_bounceback,
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
    if drop_info is not None:
        summary["drop_events_file"] = str(args.drop_events)
        summary.update(drop_info)
    write_summary(args.output_dir, summary, posterior)
    return summary


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    add_posterior_output_args(parser)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--dimensions", type=int, default=1)
    parser.add_argument(
        "--difficulty-link",
        choices=("sigmoid", "tanh"),
        default="sigmoid",
        help="link inside d_jk(t); tanh lets difficulty go negative late",
    )
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--calibrate-correctness", action="store_true")
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
        "risk set (paper Section 3.1 / Appendix A); off by default so runs are "
        "unchanged unless requested",
    )
    parser.add_argument("--ppc-draws", type=int, default=0)
    parser.add_argument("--ppc-max-events", type=int, default=500)
    parser.add_argument(
        "--train-posterior",
        type=Path,
        help="player_posterior.csv from a training run; enables held-out priors",
    )
    parser.add_argument(
        "--new-player-prior",
        choices=("tier", "flat"),
        default="tier",
        help="prior for players unseen in training",
    )
    parser.add_argument(
        "--drop-events",
        type=Path,
        help="text file of event_ids (one per line) to exclude before fitting; "
        "used by the data-dropping robustness study",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    if args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
