"""Train the biased-tanh multidimensional-difficulty CompIRT tossup model.

The trainer fits 'multidimensional.multidim_mirt.pyramidal_model_tanhbias',
whose difficulty curve is

    d_jk(t) = tanh(gamma_jk * (mu_jk - t / T_j) + bias_jk) * scale

The learned tanh shift 'bias' and fixed amplitude 'scale' (default 5.0,
'--difficulty-scale') produce these saved parameters:

    r_1..K, bias_1..K, gamma_1..K, mu_1..K

'run_experiment' coordinates the load -> build -> tensors -> train -> predict ->
save workflow. The saved 'players.csv' is compatible with
'train_compositional.py'.

The 'compirt_eval' evaluator recognizes this model from 'summary.json'
and replays its saved 'bias_*' curves with the recorded fixed difficulty scale.
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
from holdout.player_priors import attach_player_priors, player_tier_map
from multidimensional.multidim_mirt.pyramidal_model_tanhbias import (
    DEFAULT_SCALE,
    competing_risks_model,
    expected_first_buzz_positions,
    posterior_row_predictions,
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


DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "multidim-tanhbias-pyramidal"
FORMULA = (
    "logit_ij(t) = sum_k r_jk * "
    "(theta_ik - tanh(gamma_jk * (mu_jk - t / T_j) + bias_jk) * scale)"
)


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
    add_numbered_tensor_columns(tossups, "bias", posterior["bias"])
    add_numbered_tensor_columns(tossups, "gamma", posterior["gamma"])
    add_numbered_tensor_columns(tossups, "mu", posterior["mu"])
    pd.DataFrame(tossups).to_csv(output_dir / "tossups.csv", index=False)


def run_experiment(args):
    """Run the complete biased-tanh multidim training pipeline."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)

    # Load tables -> build BUZZ/CENSORED/NO-BUZZ rows -> index into tensors.
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    observations = build_tossup_observations(tables)
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
            "calibrate_correctness": args.calibrate_correctness,
            "scale": args.difficulty_scale,
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
        args.output_dir, losses, "Biased-tanh multidim IRT training loss"
    )

    # Attach fitted predictions back onto the readable observation rows.
    correct, hazard, survival = posterior_row_predictions(
        data, posterior, args.calibrate_correctness, args.difficulty_scale
    )
    buzz_expected = expected_first_buzz_positions(
        data, posterior, args.difficulty_scale
    )
    save_tossup_predictions(
        args.output_dir, observations, correct, hazard, survival, buzz_expected=buzz_expected
    )

    summary = {
        "model": "multidim-tanhbias-competing-risks",
        "formula": FORMULA,
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "difficulty_scale": args.difficulty_scale,
        "seed": args.seed,
        "steps": args.steps,
        "final_loss": losses[-1],
        "players": len(data["player_ids"]),
        "tossups": len(data["tossup_ids"]),
        "events": len(data["event_ids"]),
        "calibrate_correctness": args.calibrate_correctness,
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
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
        "--difficulty-scale",
        type=float,
        default=DEFAULT_SCALE,
        help="fixed amplitude of the biased-tanh difficulty curve d_jk(t)",
    )
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--calibrate-correctness", action="store_true")
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
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    if args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    if args.difficulty_scale <= 0:
        raise ValueError("--difficulty-scale must be positive")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
