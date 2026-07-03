"""Train the second-stage CompIRT model for team bonus performance.

Unlike pyramidal training, this file does not learn player skill from scratch.
It loads fitted 'theta' vectors from the pyramidal model, holds them fixed,
and learns how those individual skills combine for bonus parts.

Start reading at 'run_experiment' to see the complete workflow.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyro
import torch
from pyro.infer import SVI, Trace_ELBO
from pyro.infer.autoguide import AutoNormal
from pyro.optim import ClippedAdam

from compirt_data import (
    DEFAULT_DATA_DIR,
    bonus_tensors,
    build_bonus_part_observations,
    filter_tournament,
    load_hf_tables,
)
from compositional_model import compositional_model, posterior_predictions
from utils.saving import save_loss_plot, save_synergy_outputs, tensor_values


ROOT = Path(__file__).parent
DEFAULT_OUTPUT_DIR = ROOT / "results" / "compirt" / "compositional"


def load_player_skills(path, device):
    """Load player IDs and fixed theta vectors from pyramidal 'players.csv'."""
    players = pd.read_csv(path)
    # Sort by numeric suffix so theta_10 follows theta_9, not theta_1.
    theta_columns = sorted(
        (
            c
            for c in players
            if c.startswith("theta_") and c.removeprefix("theta_").isdigit()
        ),
        key=lambda c: int(c.removeprefix("theta_")),
    )
    expected = [f"theta_{i}" for i in range(1, len(theta_columns) + 1)]
    if not theta_columns or theta_columns != expected:
        raise ValueError(
            f"Expected contiguous theta_1.. columns in {path}, got {theta_columns}"
        )
    theta = torch.tensor(
        players[theta_columns].to_numpy(), dtype=torch.float32, device=device
    )
    return players["player_id"].astype(str).tolist(), theta


def train_model(
    data, theta, use_synergy, synergy_dimensions, n_steps, lr, calibrate_correctness=False
):
    """Fit bonus-part parameters while treating 'theta' as fixed input."""
    pyro.clear_param_store()
    # The guide only learns alpha, beta, tau, and optional psi.
    guide = AutoNormal(compositional_model)
    svi = SVI(compositional_model, guide, ClippedAdam({"lr": lr}), loss=Trace_ELBO())
    losses = []
    for step in range(n_steps):
        loss = svi.step(
            data, theta, use_synergy, synergy_dimensions, calibrate_correctness
        )
        losses.append(float(loss))
        if step % 100 == 0:
            print(f"step {step:4d}  ELBO loss: {loss:,.1f}")
    return guide.median(
        data, theta, use_synergy, synergy_dimensions, calibrate_correctness
    ), losses


def expected_bonus_points(part_probabilities):
    """Convert three part-correct probabilities into expected bonus points."""
    return 10 * part_probabilities.sum()


def run_experiment(args):
    """Run the complete compositional bonus training and output pipeline."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.device == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested, but no CUDA device is available")
    # Load and freeze player skills from tossups, then build bonus-part rows.
    player_ids, theta = load_player_skills(args.player_skills, args.device)
    tables = filter_tournament(
        load_hf_tables(args.data_dir, args.split), args.tournament
    )
    observations = build_bonus_part_observations(tables)
    if observations.empty:
        raise ValueError("No bonus observations matched the requested data selection")
    # Every roster member needs a fitted theta; drop the whole observation if
    # any member is unknown rather than silently changing the team.
    known_players = set(player_ids)
    known_roster = [
        bool(roster) and all(player in known_players for player in roster)
        for roster in observations["player_ids"]
    ]
    observations = observations[known_roster].reset_index(drop=True)
    if observations.empty:
        raise ValueError(
            "No bonus observations have fitted tossup skills for the full roster"
        )
    # Pad rosters using the same player order as the fixed theta matrix, fit,
    # then produce fitted values for every observation.
    data = bonus_tensors(observations, player_ids, args.device)
    print(
        f"Bonus part rows: {len(observations):,}  "
        f"Parts: {len(data['part_ids']):,}"
    )
    posterior, losses = train_model(
        data,
        theta,
        args.use_synergy,
        args.synergy_dimensions,
        args.steps,
        args.lr,
        args.calibrate_correctness,
    )
    probabilities, aggregates, synergy = posterior_predictions(
        data, theta, posterior, args.use_synergy, args.calibrate_correctness
    )

    # One parameter row per unique bonus part.
    part_parameters = {
        "bonus_part_id": data["part_ids"],
        "beta": tensor_values(posterior["beta"]),
    }
    for dimension in range(posterior["alpha"].shape[1]):
        part_parameters[f"alpha_{dimension + 1}"] = tensor_values(
            posterior["alpha"][:, dimension]
        )
    pd.DataFrame(part_parameters).to_csv(
        args.output_dir / "bonus_parts.csv", index=False
    )
    (args.output_dir / "tau.txt").write_text(
        f"{float(posterior['tau'].detach().cpu()):.8f}\n", encoding="utf-8"
    )

    predictions = observations.copy()
    predictions["predicted_correct"] = tensor_values(probabilities)
    predictions["aggregate"] = tensor_values(aggregates)
    predictions["synergy_contribution"] = tensor_values(synergy)
    predictions.to_csv(args.output_dir / "bonus_part_predictions.csv", index=False)
    # Expected points equal 10 times the sum of the three part probabilities.
    team_predictions = predictions.groupby("response_id", as_index=False).agg(
        game_id=("game_id", "first"),
        team_id=("team_id", "first"),
        total_points=("total_points", "first"),
        predicted_points=("predicted_correct", expected_bonus_points),
    )
    team_predictions.to_csv(args.output_dir / "team_predictions.csv", index=False)

    save_loss_plot(args.output_dir, losses, "Compositional IRT training loss")
    if args.use_synergy and args.save_synergy_details:
        save_synergy_outputs(
            args.output_dir,
            player_ids,
            observations,
            posterior,
            tensor_values(synergy),
        )

    summary = {
        "tournament": args.tournament or "",
        "steps": args.steps,
        "final_loss": losses[-1],
        "use_synergy": args.use_synergy,
        "synergy_dimensions": args.synergy_dimensions if args.use_synergy else 0,
        "saved_synergy_details": args.use_synergy and args.save_synergy_details,
        "calibrate_correctness": args.calibrate_correctness,
        "skill_dimensions": theta.shape[1],
        "bonus_part_observations": len(observations),
        "bonus_parts": len(data["part_ids"]),
        "tau": float(posterior["tau"].detach().cpu()),
    }
    if args.calibrate_correctness and "correctness_scale" in posterior:
        summary["correctness_scale"] = float(
            posterior["correctness_scale"].detach().cpu()
        )
        summary["correctness_bias"] = float(
            posterior["correctness_bias"].detach().cpu()
        )
    if args.use_synergy:
        synergy_array = tensor_values(synergy)
        summary.update(
            {
                "mean_synergy_contribution": float(synergy_array.mean()),
                "median_synergy_contribution": float(np.median(synergy_array)),
                "negative_synergy_fraction": float((synergy_array < 0).mean()),
                "positive_synergy_fraction": float((synergy_array > 0).mean()),
            }
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
    parser.add_argument("--player-skills", type=Path, required=True)
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--use-synergy", action="store_true")
    parser.add_argument("--synergy-dimensions", type=int, default=1)
    parser.add_argument("--save-synergy-details", action="store_true")
    parser.add_argument("--calibrate-correctness", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


if __name__ == "__main__":
    run_experiment(parse_args())
