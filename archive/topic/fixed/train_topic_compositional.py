"""Train the topic-weighted compositional bonus model.

The trainer loads fixed 'theta' vectors from the pyramidal stage and learns
per-topic bonus-part difficulty. Each bonus part's fixed PLDA topic vector
weights member skill and part difficulty coordinates.

'run_experiment' coordinates the
load -> build -> train -> predict -> save workflow.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import pyro

from compirt_data import (
    DEFAULT_DATA_DIR,
    bonus_tensors,
    build_bonus_part_observations,
    filter_tournament,
    load_hf_tables,
)
from topic.fixed.topic_compirt.compositional import compositional_model, posterior_predictions
from topic.fixed.topic_compirt.topics import align_bonus_topic_weights
from topic.utils.outputs import DEFAULT_TOPIC_VECTORS, REPO_ROOT
from train_compositional import load_player_skills
from utils.saving import (
    add_numbered_tensor_columns,
    save_bonus_predictions,
    save_loss_plot,
    save_synergy_outputs,
    tensor_values,
    write_summary,
)
from utils.training import fit_svi, require_device
from utils.posterior import add_posterior_output_args


DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "topic-compositional"
FORMULA = "logit_rb = LSE_m(sum_k r_bk * theta_pmk; tau) - sum_k r_bk * beta_bk"


def save_bonus_part_parameters(output_dir, data, posterior):
    """Write bonus-part parameters, including fixed topic weights."""
    part_parameters = {"bonus_part_id": data["part_ids"]}
    add_numbered_tensor_columns(part_parameters, "beta", posterior["beta"])
    add_numbered_tensor_columns(part_parameters, "topic_weight", data["topic_weight"])
    pd.DataFrame(part_parameters).to_csv(output_dir / "bonus_parts.csv", index=False)


def run_experiment(args):
    """Run the complete topic-weighted compositional pipeline."""
    # Set up the output directory and validate the requested device.
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)

    # Load the fixed player skills (theta) learned by the pyramidal stage.
    player_ids, theta = load_player_skills(args.player_skills, args.device)

    # Prepare bonus-part observations, keeping only rows with a fully-known roster.
    tables = filter_tournament(
        load_hf_tables(args.data_dir, args.split), args.tournament
    )
    observations = build_bonus_part_observations(tables)
    if observations.empty:
        raise ValueError("No bonus observations matched the requested data selection")
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

    # Build training tensors and attach the fixed topic-weight vectors.
    data = bonus_tensors(observations, player_ids, args.device)
    topic_weight, topic_columns = align_bonus_topic_weights(
        data, args.topic_vectors, theta.shape[1]
    )
    data["topic_weight"] = topic_weight
    print(
        f"Bonus part rows: {len(observations):,}  "
        f"Parts: {len(data['part_ids']):,}  "
        f"Topic dimensions: {len(topic_columns)}"
    )

    # Train the topic-weighted bonus-part parameters (theta stays fixed).
    posterior, _guide, losses = fit_svi(
        compositional_model,
        model_kwargs={
            "data": data,
            "theta": theta,
            "use_synergy": args.use_synergy,
            "synergy_dimensions": args.synergy_dimensions,
            "calibrate_correctness": args.calibrate_correctness,
        },
        n_steps=args.steps,
        lr=args.lr,
        posterior_output_dir=args.output_dir,
        posterior_draws=args.posterior_draws,
        posterior_seed=args.seed,
    )
    # Replay predictions at the fitted posterior medians.
    probabilities, aggregates, synergy = posterior_predictions(
        data, theta, posterior, args.use_synergy, args.calibrate_correctness
    )

    # Save the fitted bonus-part parameters and the tau aggregation scale.
    save_bonus_part_parameters(args.output_dir, data, posterior)
    (args.output_dir / "tau.txt").write_text(
        f"{float(posterior['tau'].detach().cpu()):.8f}\n", encoding="utf-8"
    )

    # Save per-part predictions, then aggregate to expected per-team bonus points.
    save_bonus_predictions(
        args.output_dir, observations, probabilities, aggregates, synergy
    )

    # Save the training-loss plot, plus optional per-player synergy details.
    save_loss_plot(
        args.output_dir, losses, "Topic-weighted compositional IRT training loss"
    )
    if args.use_synergy and args.save_synergy_details:
        save_synergy_outputs(
            args.output_dir,
            player_ids,
            observations,
            posterior,
            tensor_values(synergy),
        )

    # Build the run summary (with synergy stats when synergy is enabled).
    summary = {
        "model": "topic-weighted-compositional",
        "formula": FORMULA,
        "topic_vectors": str(args.topic_vectors),
        "topic_dimensions": len(topic_columns),
        "topic_columns": topic_columns,
        "tournament": args.tournament or "",
        "steps": args.steps,
        "lr": args.lr,
        "seed": args.seed,
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
    # Save the run summary to disk and return it to the caller.
    write_summary(args.output_dir, summary, posterior)
    return summary


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    add_posterior_output_args(parser)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--topic-vectors", type=Path, default=DEFAULT_TOPIC_VECTORS)
    parser.add_argument("--player-skills", type=Path, required=True)
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--use-synergy", action="store_true")
    parser.add_argument("--synergy-dimensions", type=int, default=1)
    parser.add_argument("--save-synergy-details", action="store_true")
    parser.add_argument(
        "--calibrate-correctness",
        action="store_true",
        help="Add a learned global scale+bias (Platt scaling) to the bonus-part logit",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    if args.synergy_dimensions < 1:
        raise ValueError("--synergy-dimensions must be at least 1")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
