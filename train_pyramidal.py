"""Train the CompIRT pyramidal tossup model and save reusable result files.

Start reading at 'run_experiment' near the bottom. It coordinates the full
workflow:

    load tables -> build observations -> make tensors -> train model
        -> calculate predictions -> save CSV files, plots, and summary

The smaller functions above it each implement one step of that workflow.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pyro

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
    save_tossup_predictions,
    write_summary,
)
from compirt_eval.drop_robustness.perturbations import (
    drop_tossup_events,
    load_event_drop_list,
)
from utils.posterior import add_posterior_output_args
from utils.training import fit_svi, require_device
from holdout.player_priors import attach_player_priors, player_tier_map


ROOT = Path(__file__).parent
DEFAULT_OUTPUT_DIR = ROOT / "results" / "compirt" / "pyramidal"


def run_experiment(args):
    """Run the complete pyramidal training and output pipeline."""
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
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
    model_kwargs = {
        "data": data,
        "n_dimensions": args.dimensions,
        "calibrate_correctness": args.calibrate_correctness,
    }
    posterior, guide, losses = fit_svi(
        competing_risks_model,
        model_kwargs=model_kwargs,
        n_steps=args.steps,
        lr=args.lr,
        posterior_output_dir=output_dir,
        posterior_draws=args.posterior_draws,
        posterior_seed=args.seed,
    )

    save_parameters(output_dir, data, posterior)
    # Save the full theta/c posterior (loc + scale) plus each player's tier so a
    # later held-out run can rebuild returning-player and tier-conditioned priors.
    save_player_posterior(output_dir, data["player_ids"], guide, tier_map)
    save_loss_plot(output_dir, losses, "Pyramidal IRT training loss")
    # Attach fitted predictions back onto the readable observation rows.
    correct, hazard, survival = posterior_row_predictions(
        data, posterior, args.calibrate_correctness
    )
    # One expected first-buzz position per event from the row-level hazards.
    buzz_expected = expected_first_buzz_positions(data, posterior)
    save_tossup_predictions(
        output_dir, observations, correct, hazard, survival, buzz_expected=buzz_expected
    )

    # summary.json records run configuration and dataset size at a glance.
    summary = {
        "model": "competing-risks",
        "split": args.split,
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "steps": args.steps,
        "lr": args.lr,
        "seed": args.seed,
        "final_loss": losses[-1],
        "players": len(data["player_ids"]),
        "tossups": len(data["tossup_ids"]),
        "events": len(data["event_ids"]),
        "calibrate_correctness": args.calibrate_correctness,
        "include_bounceback": args.include_bounceback,
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
    if drop_info is not None:
        summary["drop_events_file"] = str(args.drop_events)
        summary.update(drop_info)
    write_summary(output_dir, summary, posterior)
    return summary


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    add_posterior_output_args(parser)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--dimensions", type=int, default=1)
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--calibrate-correctness", action="store_true")
    parser.add_argument(
        "--include-bounceback",
        action="store_true",
        help="model the opposing team's post-neg continuation as a phase-1 "
        "risk set (paper Section 3.1 / Appendix A); off by default so runs are "
        "unchanged unless requested",
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
    parser.add_argument(
        "--drop-events",
        type=Path,
        help="text file of event_ids (one per line) to exclude before fitting; "
        "used by the data-dropping robustness study",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


if __name__ == "__main__":
    run_experiment(parse_args())
