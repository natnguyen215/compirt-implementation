"""Train the CompIRT pyramidal tossup model and save reusable result files.

Start reading at 'run_experiment' near the bottom. It coordinates the full
workflow:

    load tables -> build observations -> make tensors -> train model
        -> calculate predictions -> save CSV files, plots, and summary

The smaller functions above it each implement one step of that workflow.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pyro
import torch
from pyro.infer import SVI, Trace_ELBO
from pyro.infer.autoguide import AutoNormal
from pyro.optim import ClippedAdam

from pyramidal_model import (
    competing_risks_model,
    expected_first_buzz_positions,
    posterior_row_predictions,
)
from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from utils.saving import (
    save_loss_plot,
    save_parameters,
    save_player_posterior,
    save_player_rankings,
    tensor_values,
)
from holdout.player_priors import attach_player_priors, player_tier_map


ROOT = Path(__file__).parent
DEFAULT_OUTPUT_DIR = ROOT / "results" / "compirt" / "pyramidal"


def train_model(
    data,
    n_dimensions=1,
    n_steps=1000,
    lr=0.02,
    calibrate_correctness=False,
):
    """Fit the competing-risks model and return medians plus its loss curve."""
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
    # Collapse each posterior to its median for CSV output and prediction. The
    # guide is returned too so callers can save the full theta/c posterior.
    return (
        guide.median(data, n_dimensions, calibrate_correctness),
        guide,
        losses,
    )


def run_experiment(args):
    """Run the complete pyramidal training and output pipeline."""
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
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
    # Each player's tier is used both to build new-player priors (when running
    # held-out) and to label the saved posterior; compute it once and share it.
    tier_map = player_tier_map(tables)
    # Held-out evaluation: attach informative player priors (training posterior
    # for returning players, tier-conditioned for new players) before fitting.
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

    save_parameters(output_dir, data, posterior)
    # Save the full theta/c posterior (loc + scale) plus each player's tier so a
    # later held-out run can rebuild returning-player and tier-conditioned priors.
    save_player_posterior(output_dir, data["player_ids"], guide, tier_map)
    save_loss_plot(output_dir, losses, "Pyramidal IRT training loss")
    # Attach fitted predictions back onto the readable observation rows.
    predictions = observations.copy()
    correct, hazard, survival = posterior_row_predictions(
        data, posterior, args.calibrate_correctness
    )
    predictions["predicted_correct"] = tensor_values(correct)
    predictions["predicted_hazard"] = tensor_values(hazard)
    predictions["predicted_survival"] = tensor_values(survival)
    predictions.to_csv(output_dir / "tossup_predictions.csv", index=False)
    save_player_rankings(output_dir, predictions)

    if args.predict_buzz_positions:
        # One expected first-buzz position per event from the row-level hazards.
        expected = expected_first_buzz_positions(data, posterior)
        buzz_events = predictions[predictions["z"] == "BUZZ"][
            ["event_id", "relative_position"]
        ].rename(columns={"relative_position": "observed_relative_position"})
        buzz_events["predicted_relative_position"] = buzz_events["event_id"].map(
            expected
        )
        buzz_events.to_csv(output_dir / "buzz_event_predictions.csv", index=False)

    # summary.json records run configuration and dataset size at a glance.
    summary = {
        "model": "competing-risks",
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
    (output_dir / "summary.json").write_text(
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
    return parser.parse_args()


if __name__ == "__main__":
    run_experiment(parse_args())
