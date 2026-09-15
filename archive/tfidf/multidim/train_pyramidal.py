"""Train the multidimensional cumulative TF-IDF pyramidal tossup model.

The trainer fits 'tfidf.multidim.pyramidal_model' and saves vector-valued tossup
difficulty parameters:

    r_1..K, beta_1..K, gamma_1..K, mu_1..K

'run_experiment' coordinates the load -> build -> tensors -> train -> predict ->
save workflow. The saved 'players.csv' is compatible with
'train_compositional.py'.
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
from tfidf.tfidf_features import attach_tfidf_prefix_scores
from tfidf.multidim.pyramidal_model import (
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


DEFAULT_OUTPUT_PARENT = REPO_ROOT / "results" / "compirt"
FORMULA = (
    "d'_jk(t) = d_jk(t) - lambda_tfidf * tfidf_prefix_j(t); "
    "hazard_ij(t) = sum_k r_jk * (theta_ik - d'_jk(t)) - c_i"
)


# Use the "cumulative-difficulty" segment in rendered result paths and reports.
DEFAULT_OUTPUT_DIR = DEFAULT_OUTPUT_PARENT / "tfidf-multidim-cumulative-difficulty-pyramidal"
MODEL_NAME = "tfidf-multidim-cumulative-difficulty-pyramidal"


def save_multidim_tfidf_parameters(output_dir, data, posterior):
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
    add_numbered_tensor_columns(tossups, "beta", posterior["beta"])
    add_numbered_tensor_columns(tossups, "gamma", posterior["gamma"])
    add_numbered_tensor_columns(tossups, "mu", posterior["mu"])
    pd.DataFrame(tossups).to_csv(output_dir / "tossups.csv", index=False)


def save_tfidf_adjustment_curves(output_dir, data, observations, posterior, n_points=201):
    """Persist signed aggregate cumulative TF-IDF difficulty deltas.

    The model applies '-lambda_tfidf * p_j(t)' inside every dimension before
    weighting by 'r'. The evaluator consumes a scalar aggregate curve, so
    the saved delta is '-lambda_tfidf * p_j(t) * sum_k r_jk'.
    """
    lambda_tfidf = float(posterior["tfidf_clue_effect"].detach().cpu())
    relevance_mass = posterior["r"].detach().cpu().sum(dim=1).numpy()
    prefix = data["tfidf_prefix"].detach().cpu().numpy()
    tossup_T = observations.groupby("tossup_id")["T_j"].first()
    grid = np.linspace(0.0, 1.0, n_points)
    values = np.zeros((len(data["tossup_ids"]), n_points))
    for index, tossup_id in enumerate(data["tossup_ids"]):
        T = int(tossup_T[tossup_id])
        token = np.clip(np.rint(grid * T).astype(int), 1, min(T, prefix.shape[1]))
        values[index] = -lambda_tfidf * prefix[index, token - 1] * relevance_mass[index]
    frame = pd.DataFrame(
        values, columns=[f"adjustment_{point:03d}" for point in range(n_points)]
    )
    frame.insert(0, "tossup_id", data["tossup_ids"])
    frame.to_csv(output_dir / "tfidf_adjustment_curves.csv", index=False)


def run_experiment(args):
    """Run the full multidimensional TF-IDF pyramidal pipeline."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)

    # Load tables -> build BUZZ/CENSORED/NO-BUZZ rows -> index into tensors,
    # then attach the precomputed TF-IDF prefix/token feature matrices.
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    observations = build_tossup_observations(tables)
    if observations.empty:
        raise ValueError("No tossup observations matched the requested data selection")
    data = tossup_tensors(observations, args.device)
    tfidf_summary = attach_tfidf_prefix_scores(
        data,
        tables,
        normalize=not args.no_normalize_tfidf,
        device=args.device,
    )

    print(
        f"Rows: {len(observations):,}  "
        f"Players: {len(data['player_ids']):,}  "
        f"Tossups: {len(data['tossup_ids']):,}  "
        f"Dimensions: {args.dimensions}  "
        f"IDF vocab: {tfidf_summary['vocabulary_size']:,}"
    )
    print(observations["z"].value_counts().to_string())

    # Each player's tier labels the saved posterior and builds new-player priors.
    tier_map = player_tier_map(tables)
    # Held-out evaluation: attach informative player priors before fitting.
    prior_summary = None
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
            "tfidf_effect_prior_scale": args.tfidf_effect_prior_scale,
        },
        n_steps=args.steps,
        lr=args.lr,
        posterior_output_dir=args.output_dir,
        posterior_draws=args.posterior_draws,
        posterior_seed=args.seed,
    )

    save_multidim_tfidf_parameters(args.output_dir, data, posterior)
    # Save the full theta/c posterior plus tiers so a later held-out run can
    # rebuild returning-player and tier-conditioned priors.
    save_player_posterior(
        args.output_dir, data["player_ids"], guide, tier_map
    )
    save_tfidf_adjustment_curves(args.output_dir, data, observations, posterior)
    save_loss_plot(
        args.output_dir,
        losses,
        "Multidim cumulative TF-IDF pyramidal training loss",
    )

    # Attach fitted predictions back onto the readable observation rows; the
    # TF-IDF scores at each row's 't_star' ride along as diagnostics.
    correct, hazard, survival, prefix_score = posterior_row_predictions(
        data, posterior, args.calibrate_correctness
    )
    buzz_expected = expected_first_buzz_positions(data, posterior)
    extra_columns = {"tfidf_prefix_score": prefix_score}
    save_tossup_predictions(
        args.output_dir,
        observations,
        correct,
        hazard,
        survival,
        buzz_expected=buzz_expected,
        extra_columns=extra_columns,
    )

    summary = {
        "model": MODEL_NAME,
        "formula": FORMULA,
        "split": args.split,
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "steps": args.steps,
        "lr": args.lr,
        "seed": args.seed,
        "final_loss": losses[-1],
        "calibrate_correctness": args.calibrate_correctness,
        "tfidf_features": tfidf_summary,
        "players": len(data["player_ids"]),
        "tossups": len(data["tossup_ids"]),
        "events": len(data["event_ids"]),
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
    if args.train_posterior:
        summary["train_posterior"] = str(args.train_posterior)
        summary["new_player_prior"] = args.new_player_prior
        summary["heldout_prior_summary"] = prior_summary
    summary["tfidf_effect_prior_scale"] = args.tfidf_effect_prior_scale
    summary["tfidf_clue_effect"] = float(
        posterior["tfidf_clue_effect"].detach().cpu()
    )
    summary["tfidf_adjustment_curve"] = "r_weighted_aggregate"
    write_summary(args.output_dir, summary, posterior)
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
        "--tfidf-effect-prior-scale",
        type=float,
        default=1.0,
        help="HalfNormal prior scale for the cumulative TF-IDF effect",
    )
    parser.add_argument(
        "--no-normalize-tfidf",
        action="store_true",
        help="Use raw cumulative TF-IDF mass instead of scaling each tossup to end at 1",
    )
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
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.output_dir is None:
        args.output_dir = DEFAULT_OUTPUT_DIR
    if args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    if args.tfidf_effect_prior_scale <= 0:
        raise ValueError("--tfidf-effect-prior-scale must be positive")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
