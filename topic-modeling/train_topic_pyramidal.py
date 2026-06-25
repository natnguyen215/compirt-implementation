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
import json
from pathlib import Path

import numpy as np
import pandas as pd
import torch


from topic_compirt.common import (  # noqa: E402
    DEFAULT_TOPIC_VECTORS,
    REPO_ROOT,
    add_numbered_tensor_columns,
    add_repo_root_to_path,
    fit_svi,
    tensor_values,
)


add_repo_root_to_path()

from compirt_data import (  # noqa: E402
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from topic_compirt.pyramidal import (  # noqa: E402
    competing_risks_model,
    expected_first_buzz_positions,
    posterior_row_predictions,
)
from topic_compirt.topics import align_tossup_topic_weights  # noqa: E402
from utils.saving import save_loss_plot, save_player_rankings  # noqa: E402


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
    if args.device == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested, but no CUDA device is available")

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

    # Train the topic-weighted competing-risks model.
    posterior, losses = train_model(
        data, dimensions, args.steps, args.lr, args.calibrate_correctness
    )

    # Save fitted player/tossup parameters and the training-loss plot.
    save_topic_parameters(args.output_dir, data, posterior)
    save_loss_plot(args.output_dir, losses, "Topic-weighted pyramidal IRT training loss")

    # Replay per-row predictions at the fitted medians and save them with rankings.
    predictions = observations.copy()
    correct, hazard, survival = posterior_row_predictions(
        data, posterior, args.calibrate_correctness
    )
    predictions["predicted_correct"] = tensor_values(correct)
    predictions["predicted_hazard"] = tensor_values(hazard)
    predictions["predicted_survival"] = tensor_values(survival)
    predictions.to_csv(args.output_dir / "tossup_predictions.csv", index=False)
    save_player_rankings(args.output_dir, predictions)

    # Optionally simulate and save expected first-buzz positions per event.
    if args.predict_buzz_positions:
        expected = expected_first_buzz_positions(data, posterior)
        buzz_events = predictions[predictions["z"] == "BUZZ"][
            ["event_id", "relative_position"]
        ].rename(columns={"relative_position": "observed_relative_position"})
        buzz_events["predicted_relative_position"] = buzz_events["event_id"].map(
            expected
        )
        buzz_events.to_csv(args.output_dir / "buzz_event_predictions.csv", index=False)

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
    if args.calibrate_correctness and "correctness_scale" in posterior:
        summary["correctness_scale"] = float(
            posterior["correctness_scale"].detach().cpu()
        )
        summary["correctness_bias"] = float(
            posterior["correctness_bias"].detach().cpu()
        )
    # Save the run summary to disk and return it to the caller.
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
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
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    if args.dimensions is not None and args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
