"""Train the multidimensional-difficulty CompIRT tossup model.

This mirrors the root 'train_pyramidal.py' but imports
'multidim_mirt.pyramidal_model' and saves vector-valued tossup difficulty
parameters:

    alpha_1..K, beta_1..K, gamma_1..K, mu_1..K

Start reading at 'run_experiment' near the bottom; it coordinates the same
load -> build -> tensors -> train -> predict -> save workflow as the root
script. The saved 'players.csv' remains compatible with 'train_compositional.py'.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pyro
import torch
from pyro.infer import SVI, Trace_ELBO
from pyro.infer.autoguide import AutoNormal
from pyro.optim import ClippedAdam

REPO_ROOT = Path(__file__).resolve().parent.parent
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
from multidim_mirt.pyramidal_model import (
    competing_risks_model,
    expected_first_buzz_positions,
    posterior_row_predictions,
)
from utils.saving import (
    save_loss_plot,
    save_player_posterior,
    save_player_rankings,
    tensor_values,
)


DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "multidim-pyramidal"
FORMULA = "logit_ij(t) = sum_k alpha_jk * (theta_ik - d_jk(t))"


def add_numbered_tensor_columns(frame, prefix, tensor):
    """Add one DataFrame-ready column per tensor coordinate (e.g. alpha_1..K)."""
    values = tensor_values(tensor)
    if values.ndim != 2:
        raise ValueError(f"Expected {prefix} to be a matrix, got shape {values.shape}")
    for dimension in range(values.shape[1]):
        frame[f"{prefix}_{dimension + 1}"] = values[:, dimension]


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
    add_numbered_tensor_columns(tossups, "alpha", posterior["alpha"])
    add_numbered_tensor_columns(tossups, "beta", posterior["beta"])
    add_numbered_tensor_columns(tossups, "gamma", posterior["gamma"])
    add_numbered_tensor_columns(tossups, "mu", posterior["mu"])
    pd.DataFrame(tossups).to_csv(output_dir / "tossups.csv", index=False)


def train_model(
    data,
    n_dimensions=1,
    n_steps=1000,
    lr=0.02,
    calibrate_correctness=False,
):
    """Fit the model and return posterior medians, guide, and loss curve."""
    # Clear the global param store so a previous run cannot leak in.
    pyro.clear_param_store()
    guide = AutoNormal(competing_risks_model)
    svi = SVI(
        competing_risks_model, guide, ClippedAdam({"lr": lr}), loss=Trace_ELBO()
    )
    losses = []
    for step in range(n_steps):
        loss = svi.step(data, n_dimensions, calibrate_correctness)
        losses.append(float(loss))
        if step % 100 == 0:
            print(f"step {step:4d}  ELBO loss: {loss:,.1f}")
    # Collapse each posterior to its median for CSV output and prediction; the
    # guide is returned too so callers can save the full theta/c posterior.
    return (
        guide.median(data, n_dimensions, calibrate_correctness),
        guide,
        losses,
    )


def run_experiment(args):
    """Run the complete multidimensional-difficulty training pipeline."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.device == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested, but no CUDA device is available")

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

    posterior, guide, losses = train_model(
        data,
        args.dimensions,
        args.steps,
        args.lr,
        args.calibrate_correctness,
    )

    save_multidim_parameters(args.output_dir, data, posterior)
    # Save the full theta/c posterior plus tiers so a later held-out run can
    # rebuild returning-player and tier-conditioned priors.
    save_player_posterior(args.output_dir, data["player_ids"], guide, tier_map)
    save_loss_plot(
        args.output_dir, losses, "Multidimensional-difficulty IRT training loss"
    )

    # Attach fitted predictions back onto the readable observation rows.
    predictions = observations.copy()
    correct, hazard, survival = posterior_row_predictions(
        data, posterior, args.calibrate_correctness
    )
    predictions["predicted_correct"] = tensor_values(correct)
    predictions["predicted_hazard"] = tensor_values(hazard)
    predictions["predicted_survival"] = tensor_values(survival)
    predictions.to_csv(args.output_dir / "tossup_predictions.csv", index=False)
    save_player_rankings(args.output_dir, predictions)

    if args.predict_buzz_positions:
        expected = expected_first_buzz_positions(data, posterior)
        buzz_events = predictions[predictions["z"] == "BUZZ"][
            ["event_id", "relative_position"]
        ].rename(columns={"relative_position": "observed_relative_position"})
        buzz_events["predicted_relative_position"] = buzz_events["event_id"].map(
            expected
        )
        buzz_events.to_csv(args.output_dir / "buzz_event_predictions.csv", index=False)

    summary = {
        "model": "multidimensional-difficulty-competing-risks",
        "formula": FORMULA,
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "steps": args.steps,
        "final_loss": losses[-1],
        "players": len(data["player_ids"]),
        "tossups": len(data["tossup_ids"]),
        "events": len(data["event_ids"]),
        "predicted_buzz_positions": args.predict_buzz_positions,
        "calibrate_correctness": args.calibrate_correctness,
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
    if args.calibrate_correctness and "correctness_scale" in posterior:
        summary["correctness_scale"] = float(
            posterior["correctness_scale"].detach().cpu()
        )
        summary["correctness_bias"] = float(
            posterior["correctness_bias"].detach().cpu()
        )
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    return summary


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--dimensions", type=int, default=1)
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--predict-buzz-positions", action="store_true")
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
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
