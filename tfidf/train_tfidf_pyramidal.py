"""Train one of the isolated TF-IDF-aware pyramidal tossup variants.

This mirrors the root 'train_pyramidal.py' but attaches precomputed TF-IDF clue
features to the tensor dict and fits 'tfidf.pyramidal_tfidf_model'. The root
baseline model remains untouched.

Start reading at 'run_experiment' near the bottom; it coordinates the same
load -> build -> tensors -> train -> predict -> save workflow as the root
script, plus the TF-IDF feature attachment and the 'cumulative-difficulty'
adjustment-curve export. The saved 'players.csv' remains compatible with the
root 'train_compositional.py'.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pyro

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from tfidf.pyramidal_tfidf_model import (
    CUMULATIVE_DIFFICULTY,
    HAZARD_SPIKE,
    REPLACE_POSITION,
    TFIDF_VARIANTS,
    competing_risks_model,
    expected_first_buzz_positions,
    posterior_row_predictions,
    uses_tfidf_effect,
)
from tfidf.tfidf_features import attach_tfidf_prefix_scores
from utils.saving import (
    save_loss_plot,
    save_parameters,
    save_player_posterior,
    save_tossup_predictions,
    write_summary,
)
from utils.training import fit_svi, require_device
from holdout.player_priors import attach_player_priors, player_tier_map


DEFAULT_OUTPUT_PARENT = REPO_ROOT / "results" / "compirt"
FORMULAS = {
    REPLACE_POSITION: (
        "d_j(t) = beta_j * sigmoid(gamma_j * (mu_j - tfidf_prefix_j(t))); "
        "hazard_ij(t) = theta_i^T alpha_j - d_j(t) - c_i"
    ),
    CUMULATIVE_DIFFICULTY: (
        "d'_j(t) = d_j(t) - lambda_tfidf * tfidf_prefix_j(t); "
        "hazard_ij(t) = theta_i^T alpha_j - d'_j(t) - c_i"
    ),
    HAZARD_SPIKE: (
        "correctness_ij(t) = theta_i^T alpha_j - d_j(t); "
        "hazard_ij(t) = correctness_ij(t) - c_i + eta_tfidf * tfidf(w_j,t)"
    ),
}


def default_output_dir(tfidf_variant: str) -> Path:
    """Return a variant-specific default output directory."""
    return DEFAULT_OUTPUT_PARENT / f"tfidf-{tfidf_variant}-pyramidal"


def save_tfidf_adjustment_curves(
    output_dir,
    data,
    observations,
    posterior,
    tfidf_variant,
    n_points=201,
):
    """Persist signed per-tossup difficulty deltas for 'cumulative-difficulty'.

    For 'cumulative-difficulty' the effective difficulty is:

        d'_j(t) = d_j(t) - lambda_tfidf * p_j(t)

    The saved adjustment is therefore negative. Evaluators add it to the base
    difficulty curve to replay the effective curve. The other variants change
    no difficulty term ('hazard-spike') or need no delta ('replace-position'),
    so nothing is written for them.
    """
    if tfidf_variant != CUMULATIVE_DIFFICULTY:
        return

    lambda_tfidf = float(posterior["tfidf_clue_effect"].detach().cpu())
    prefix = data["tfidf_prefix"].detach().cpu().numpy()
    tossup_T = observations.groupby("tossup_id")["T_j"].first()
    grid = np.linspace(0.0, 1.0, n_points)
    values = np.zeros((len(data["tossup_ids"]), n_points))
    for index, tossup_id in enumerate(data["tossup_ids"]):
        T = int(tossup_T[tossup_id])
        token = np.clip(np.rint(grid * T).astype(int), 1, min(T, prefix.shape[1]))
        values[index] = -lambda_tfidf * prefix[index, token - 1]
    frame = pd.DataFrame(
        values, columns=[f"adjustment_{point:03d}" for point in range(n_points)]
    )
    frame.insert(0, "tossup_id", data["tossup_ids"])
    frame.to_csv(output_dir / "tfidf_adjustment_curves.csv", index=False)


def train_model(
    data,
    n_dimensions=1,
    n_steps=1000,
    lr=0.02,
    calibrate_correctness=False,
    tfidf_effect_prior_scale=1.0,
    tfidf_variant=REPLACE_POSITION,
):
    """Fit the selected TF-IDF competing-risks model."""
    return fit_svi(
        competing_risks_model,
        (
            data,
            n_dimensions,
            calibrate_correctness,
            tfidf_effect_prior_scale,
            tfidf_variant,
        ),
        n_steps,
        lr,
        return_guide=True,
    )


def run_experiment(args):
    """Run the full isolated TF-IDF pyramidal pipeline."""
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
        f"Variant: {args.tfidf_variant}  "
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

    posterior, guide, losses = train_model(
        data,
        args.dimensions,
        args.steps,
        args.lr,
        args.calibrate_correctness,
        args.tfidf_effect_prior_scale,
        args.tfidf_variant,
    )

    save_parameters(args.output_dir, data, posterior)
    # Save the full theta/c posterior plus tiers so a later held-out run can
    # rebuild returning-player and tier-conditioned priors.
    save_player_posterior(args.output_dir, data["player_ids"], guide, tier_map)
    save_tfidf_adjustment_curves(
        args.output_dir, data, observations, posterior, args.tfidf_variant
    )
    save_loss_plot(
        args.output_dir,
        losses,
        f"TF-IDF {args.tfidf_variant} pyramidal training loss",
    )

    # Attach fitted predictions back onto the readable observation rows; the
    # TF-IDF scores at each row's 't_star' ride along as diagnostics.
    correct, hazard, survival, prefix_score, token_score = posterior_row_predictions(
        data, posterior, args.calibrate_correctness, args.tfidf_variant
    )
    buzz_expected = (
        expected_first_buzz_positions(data, posterior, args.tfidf_variant)
        if args.predict_buzz_positions
        else None
    )
    extra_columns = {"tfidf_prefix_score": prefix_score}
    if args.tfidf_variant == HAZARD_SPIKE:
        extra_columns["tfidf_token_score"] = token_score
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
        "model": f"tfidf-{args.tfidf_variant}-pyramidal",
        "tfidf_variant": args.tfidf_variant,
        "formula": FORMULAS[args.tfidf_variant],
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
        "predicted_buzz_positions": args.predict_buzz_positions,
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
    if args.train_posterior:
        summary["train_posterior"] = str(args.train_posterior)
        summary["new_player_prior"] = args.new_player_prior
        summary["heldout_prior_summary"] = prior_summary
    if uses_tfidf_effect(args.tfidf_variant):
        summary["tfidf_effect_prior_scale"] = args.tfidf_effect_prior_scale
    if args.tfidf_variant == CUMULATIVE_DIFFICULTY:
        summary["tfidf_clue_effect"] = float(
            posterior["tfidf_clue_effect"].detach().cpu()
        )
    if args.tfidf_variant == HAZARD_SPIKE:
        summary["tfidf_hazard_effect"] = float(
            posterior["tfidf_hazard_effect"].detach().cpu()
        )
    write_summary(args.output_dir, summary, posterior)
    return summary


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--dimensions", type=int, default=1)
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--predict-buzz-positions", action="store_true")
    parser.add_argument("--calibrate-correctness", action="store_true")
    parser.add_argument(
        "--tfidf-variant",
        choices=TFIDF_VARIANTS,
        default=REPLACE_POSITION,
        help="Which requested TF-IDF formulation to train",
    )
    parser.add_argument(
        "--tfidf-effect-prior-scale",
        type=float,
        default=1.0,
        help="HalfNormal prior scale for cumulative/hazard TF-IDF effects",
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
        args.output_dir = default_output_dir(args.tfidf_variant)
    if args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    if args.tfidf_effect_prior_scale <= 0:
        raise ValueError("--tfidf-effect-prior-scale must be positive")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
