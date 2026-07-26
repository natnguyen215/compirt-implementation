"""Train the second-stage CompIRT model for team bonus performance.

The trainer loads fitted 'theta' vectors from the pyramidal model, holds them
fixed, and learns how those individual skills combine for bonus parts.

'run_experiment' coordinates the complete workflow.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import pyro
import torch

from compirt_data import (
    DEFAULT_DATA_DIR,
    bonus_tensors,
    build_bonus_part_observations,
    filter_tournament,
    load_hf_tables,
)
from compositional_model import compositional_model, posterior_predictions
from compirt_eval.diagnostics.posterior_predictive import save_bonus_ppc
from utils.saving import (
    add_numbered_tensor_columns,
    save_bonus_predictions,
    save_loss_plot,
    save_synergy_outputs,
    tensor_values,
    write_summary,
)
from utils.posterior import add_posterior_output_args
from utils.training import fit_svi, require_device


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


def run_experiment(args):
    """Run the complete compositional bonus training and output pipeline."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)
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
    model_kwargs = {
        "data": data,
        "theta": theta,
        "use_synergy": args.use_synergy,
        "synergy_dimensions": args.synergy_dimensions,
        "calibrate_correctness": args.calibrate_correctness,
        "alpha_prior": args.alpha_prior,
    }
    posterior, guide, losses = fit_svi(
        compositional_model,
        model_kwargs=model_kwargs,
        n_steps=args.steps,
        lr=args.lr,
        posterior_output_dir=args.output_dir,
        posterior_draws=args.posterior_draws,
        posterior_seed=args.seed,
    )
    probabilities, aggregates, synergy = posterior_predictions(
        data, theta, posterior, args.use_synergy, args.calibrate_correctness
    )

    # One parameter row per unique bonus part.
    part_parameters = {
        "bonus_part_id": data["part_ids"],
        "beta": tensor_values(posterior["beta"]),
    }
    add_numbered_tensor_columns(part_parameters, "alpha", posterior["alpha"])
    pd.DataFrame(part_parameters).to_csv(
        args.output_dir / "bonus_parts.csv", index=False
    )
    (args.output_dir / "tau.txt").write_text(
        f"{float(posterior['tau'].detach().cpu()):.8f}\n", encoding="utf-8"
    )

    save_bonus_predictions(
        args.output_dir, observations, probabilities, aggregates, synergy
    )
    save_bonus_ppc(
        args.output_dir,
        observations,
        data,
        theta,
        guide,
        model_kwargs,
        draws=args.ppc_draws,
        max_responses=args.ppc_max_responses,
        seed=args.seed,
    )

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
        "split": args.split,
        "tournament": args.tournament or "",
        "steps": args.steps,
        "lr": args.lr,
        "seed": args.seed,
        "final_loss": losses[-1],
        "use_synergy": args.use_synergy,
        "synergy_dimensions": args.synergy_dimensions if args.use_synergy else 0,
        "saved_synergy_details": args.use_synergy and args.save_synergy_details,
        "calibrate_correctness": args.calibrate_correctness,
        "alpha_prior": args.alpha_prior,
        "skill_dimensions": theta.shape[1],
        "bonus_part_observations": len(observations),
        "bonus_parts": len(data["part_ids"]),
        "tau": float(posterior["tau"].detach().cpu()),
    }
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
    write_summary(args.output_dir, summary, posterior)
    return summary


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    add_posterior_output_args(parser)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--player-skills", type=Path, required=True)
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--use-synergy", action="store_true")
    parser.add_argument("--synergy-dimensions", type=int, default=1)
    parser.add_argument("--save-synergy-details", action="store_true")
    parser.add_argument("--calibrate-correctness", action="store_true")
    parser.add_argument("--ppc-draws", type=int, default=0)
    parser.add_argument("--ppc-max-responses", type=int, default=500)
    parser.add_argument(
        "--alpha-prior",
        choices=("normal", "gamma"),
        default="normal",
        help=(
            "Bonus-part discrimination prior. Use 'gamma' only when the fixed "
            "theta basis is already pinned positive (multidim pyramidal)."
        ),
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


if __name__ == "__main__":
    run_experiment(parse_args())
