"""Train the isolated topic-weighted pyramidal tossup model.

This is the topic-weighted counterpart to the root 'train_pyramidal.py'. It
learns player skills 'theta' and per-topic tossup difficulty curves. The fixed
PLDA topic vector weights the skill-minus-difficulty gap for each tossup.

Start reading at 'run_experiment' near the bottom. It coordinates the full
workflow:

    load tables -> build observations -> make tensors -> attach topic weights
        -> train model -> calculate predictions -> save CSV files, plots, summary
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from topic.fixed.topic_compirt.pyramidal import (
    competing_risks_model,
    expected_first_buzz_positions,
    posterior_row_predictions,
)
from topic.fixed.topic_compirt.topics import align_tossup_topic_weights
from topic.utils.outputs import DEFAULT_TOPIC_VECTORS, REPO_ROOT
from utils.saving import (
    add_numbered_tensor_columns,
    save_loss_plot,
    save_player_posterior,
    save_tossup_predictions,
    tensor_values,
    write_summary,
)
from utils.training import fit_svi, require_device
from holdout.player_priors import attach_player_priors, player_tier_map


DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "topic-pyramidal"
FORMULA = "logit_ij(t) = sum_k r_jk * (theta_ik - d_jk(t))"


def train_model(
    data, n_dimensions, n_steps=1000, lr=0.02, calibrate_correctness=False
):
    """Fit the topic-weighted competing-risks model."""
    return fit_svi(
        competing_risks_model,
        (data, n_dimensions, calibrate_correctness),
        n_steps,
        lr,
        return_guide=True,
    )


def save_topic_parameters(output_dir, data, posterior):
    """Write player and tossup parameters, including fixed topic weights."""
    # Players table: confidence c, theta dimensions, and the theta vector norm.
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

    # Tossups table: per-topic difficulty params plus the fixed topic weights.
    tossups = {"tossup_id": data["tossup_ids"]}
    add_numbered_tensor_columns(tossups, "beta", posterior["beta"])
    add_numbered_tensor_columns(tossups, "gamma", posterior["gamma"])
    add_numbered_tensor_columns(tossups, "mu", posterior["mu"])
    add_numbered_tensor_columns(tossups, "topic_weight", data["topic_weight"])
    pd.DataFrame(tossups).to_csv(output_dir / "tossups.csv", index=False)


def run_experiment(args):
    """Run the complete isolated topic-weighted pyramidal pipeline."""
    # Set up the output directory and validate the requested device.
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)

    # Prepare tossup observations and build the training tensors.
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    observations = build_tossup_observations(tables)
    if observations.empty:
        raise ValueError("No tossup observations matched the requested data selection")
    data = tossup_tensors(observations, args.device)

    # Attach the fixed topic-weight vectors; default dimensions to the topic count.
    topic_weight, topic_columns = align_tossup_topic_weights(
        data, args.topic_vectors, args.dimensions
    )
    data["topic_weight"] = topic_weight
    dimensions = len(topic_columns)
    print(
        f"Rows: {len(observations):,}  "
        f"Players: {len(data['player_ids']):,}  "
        f"Tossups: {len(data['tossup_ids']):,}  "
        f"Topic dimensions: {dimensions}"
    )
    print(observations["z"].value_counts().to_string())

    # Player tiers feed both new-player priors and the saved posterior label;
    # compute once and share.
    tier_map = player_tier_map(tables)
    # Held-out evaluation: attach informative player priors before fitting.
    if args.train_posterior:
        prior_summary = attach_player_priors(
            data,
            tables,
            args.train_posterior,
            args.new_player_prior,
            args.device,
            n_dimensions=dimensions,
            tier_map=tier_map,
        )
        print(f"Held-out player priors: {prior_summary}")

    # Train the topic-weighted competing-risks model.
    posterior, guide, losses = train_model(
        data, dimensions, args.steps, args.lr, args.calibrate_correctness
    )

    # Save fitted player/tossup parameters and the training-loss plot.
    save_topic_parameters(args.output_dir, data, posterior)
    save_player_posterior(args.output_dir, data["player_ids"], guide, tier_map)
    save_loss_plot(args.output_dir, losses, "Topic-weighted pyramidal IRT training loss")

    # Replay per-row predictions at the fitted medians and save them with rankings.
    correct, hazard, survival = posterior_row_predictions(
        data, posterior, args.calibrate_correctness
    )
    buzz_expected = (
        expected_first_buzz_positions(data, posterior)
        if args.predict_buzz_positions
        else None
    )
    save_tossup_predictions(
        args.output_dir, observations, correct, hazard, survival, buzz_expected=buzz_expected
    )

    # Build the run summary.
    summary = {
        "model": "topic-weighted-pyramidal",
        "formula": FORMULA,
        "topic_vectors": str(args.topic_vectors),
        "topic_dimensions": dimensions,
        "topic_columns": topic_columns,
        "tournament": args.tournament or "",
        "dimensions": dimensions,
        "steps": args.steps,
        "final_loss": losses[-1],
        "calibrate_correctness": args.calibrate_correctness,
        "players": len(data["player_ids"]),
        "tossups": len(data["tossup_ids"]),
        "events": len(data["event_ids"]),
        "predicted_buzz_positions": args.predict_buzz_positions,
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
    # Save the run summary to disk and return it to the caller.
    write_summary(args.output_dir, summary, posterior)
    return summary


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--topic-vectors", type=Path, default=DEFAULT_TOPIC_VECTORS)
    parser.add_argument(
        "--dimensions",
        type=int,
        default=None,
        help="Latent skill dimensions. Defaults to topic-vector column count.",
    )
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--predict-buzz-positions", action="store_true")
    parser.add_argument(
        "--calibrate-correctness",
        action="store_true",
        help="Add a learned global scale+bias (Platt scaling) to the correctness logit",
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
        help="prior for players unseen in training: tier-conditioned (paper "
        "default) or flat N(0, I) (ablation)",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    if args.dimensions is not None and args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
