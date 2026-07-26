"""Train the embedding-relevance CompIRT tossup model.

The trainer attaches each tossup's frozen Qwen3 embedding, projects it into the
relevance vector 'r', and saves the fitted projection as 'r_projection.npz' for
the bonus stage.

'run_experiment' coordinates the load -> build -> tensors -> train -> predict ->
save workflow.
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
from multidimensional.embedding_mirt.embeddings import (
    align_tossup_embeddings,
    center_embeddings,
    save_projection,
)
from multidimensional.embedding_mirt.pyramidal_model import (
    DEFAULT_PROJECTION_HIDDEN_DIM,
    competing_risks_model,
    expected_first_buzz_positions,
    fitted_projection,
    posterior_row_predictions,
    project_relevance,
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


DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "embedding-pyramidal"
DEFAULT_EMBEDDINGS = (
    REPO_ROOT / "multidimensional" / "embedding_mirt" / "outputs" / "tossup_embeddings.npz"
)
FORMULA = (
    "logit_ij(t) = sum_k r_jk * (theta_ik - d_jk(t)), "
    "r_j = softmax(W2 gelu(W1 @ (e_j - mean_e) + b1) + b2)"
)


def save_embedding_parameters(output_dir, data, posterior):
    """Write player and tossup parameters, including the fitted relevance 'r'."""
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


def fit_embedding_model(
    data,
    *,
    n_dimensions=5,
    n_steps=1000,
    lr=0.02,
    calibrate_correctness=False,
    projection_hidden_dim=DEFAULT_PROJECTION_HIDDEN_DIM,
    posterior_output_dir=None,
    posterior_draws=0,
    posterior_seed=42,
):
    """Fit the model and return posterior medians (plus fitted 'r'), guide, and losses."""
    data["projection_hidden_dim"] = projection_hidden_dim
    posterior, guide, losses = fit_svi(
        competing_risks_model,
        model_kwargs={
            "data": data,
            "n_dimensions": n_dimensions,
            "calibrate_correctness": calibrate_correctness,
        },
        n_steps=n_steps,
        lr=lr,
        posterior_output_dir=posterior_output_dir,
        posterior_draws=posterior_draws,
        posterior_seed=posterior_seed,
    )
    # Read the point-estimated FFN from the parameter store and use it to derive
    # deterministic relevance vectors.
    projection = fitted_projection()
    posterior["r"] = project_relevance(data["embedding"], projection)
    return posterior, guide, losses, projection


def run_experiment(args):
    """Run the complete embedding-relevance training pipeline."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)

    # Build tossup tensors, align cached embeddings, and center them using the
    # mean that will be saved with the fitted projection.
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    observations = build_tossup_observations(tables)
    if observations.empty:
        raise ValueError("No tossup observations matched the requested data selection")
    data = tossup_tensors(observations, args.device)
    data["embedding"] = align_tossup_embeddings(data, args.embeddings)
    embedding_mean = data["embedding"].mean(dim=0)
    data["embedding"] = center_embeddings(data["embedding"], embedding_mean)
    print(
        f"Rows: {len(observations):,}  "
        f"Players: {len(data['player_ids']):,}  "
        f"Tossups: {len(data['tossup_ids']):,}  "
        f"Embedding dim: {data['embedding'].shape[1]:,}"
    )
    print(observations["z"].value_counts().to_string())

    # Attach held-out player priors when replaying from a training posterior.
    tier_map = player_tier_map(tables)
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

    # Fit player/tossup parameters and the embedding-to-relevance projection.
    posterior, guide, losses, projection = fit_embedding_model(
        data,
        n_dimensions=args.dimensions,
        n_steps=args.steps,
        lr=args.lr,
        calibrate_correctness=args.calibrate_correctness,
        projection_hidden_dim=args.projection_hidden_dim,
        posterior_output_dir=args.output_dir,
        posterior_draws=args.posterior_draws,
        posterior_seed=args.seed,
    )

    # Save fitted parameters, the centered projection, and training diagnostics.
    save_embedding_parameters(args.output_dir, data, posterior)
    save_projection(
        args.output_dir / "r_projection.npz",
        projection,
        embedding_mean=embedding_mean,
    )
    save_player_posterior(args.output_dir, data["player_ids"], guide, tier_map)
    save_loss_plot(
        args.output_dir, losses, "Embedding-relevance IRT training loss"
    )

    # Replay row and event predictions at the fitted posterior medians.
    correct, hazard, survival = posterior_row_predictions(
        data, posterior, args.calibrate_correctness
    )
    buzz_expected = expected_first_buzz_positions(data, posterior)
    save_tossup_predictions(
        args.output_dir, observations, correct, hazard, survival, buzz_expected=buzz_expected
    )

    # Record the inputs, fit settings, and realized dataset sizes.
    summary = {
        "model": "embedding-relevance-competing-risks",
        "formula": FORMULA,
        "embeddings": str(args.embeddings),
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "projection": "ffn",
        "projection_hidden_dim": args.projection_hidden_dim,
        "centered_embeddings": True,
        "embedding_mean_norm": float(embedding_mean.norm().detach().cpu()),
        "steps": args.steps,
        "lr": args.lr,
        "seed": args.seed,
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
    parser.add_argument("--embeddings", type=Path, default=DEFAULT_EMBEDDINGS)
    parser.add_argument("--dimensions", type=int, default=5)
    parser.add_argument(
        "--projection-hidden-dim",
        type=int,
        default=DEFAULT_PROJECTION_HIDDEN_DIM,
        help="Hidden width for the embedding-to-r FFN projection",
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
    if args.projection_hidden_dim < 1:
        raise ValueError("--projection-hidden-dim must be at least 1")
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
