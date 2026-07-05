"""Train the isolated TF-IDF clue-adjusted baseline pyramidal model.

This mirrors the root 'train_pyramidal.py' workflow but attaches precomputed
TF-IDF clue features to the tensor dict and fits 'tfidf.pyramidal_tfidf_model'.
Start reading at 'run_experiment' near the bottom; it coordinates the full
pipeline:

    load tables -> build observations -> make tensors -> attach TF-IDF features
        -> train model -> compute predictions -> save CSVs, plots, and summary
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import pyro

from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from tfidf.pyramidal_tfidf_model import (
    competing_risks_model,
    expected_first_buzz_positions,
    posterior_row_predictions,
)
from tfidf.tfidf_features import attach_tfidf_prefix_scores
from utils.saving import (
    save_loss_plot,
    save_parameters,
    save_tossup_predictions,
    write_summary,
)
from utils.training import fit_svi, require_device


REPO_ROOT = Path(__file__).resolve().parents[1]


DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "tfidf-baseline-pyramidal"
FORMULA = (
    "logit_ij(t) = theta_i^T alpha_j - d_j(t) + lambda_tfidf * tfidf_prefix_j(t)"
)


def save_tfidf_adjustment_curves(output_dir, data, observations, posterior, n_points=201):
    """Persist per-tossup TF-IDF difficulty adjustments on a relative-position grid.

    The shared evaluator reconstructs difficulty curves from saved CSVs only,
    so it cannot recompute text features. This file lets it draw the effective
    difficulty 'd'_j(r) = d_j(r) - A_j(r)' the model actually used.
    """
    lambda_tfidf = float(posterior["tfidf_clue_effect"].detach().cpu())
    prefix = data["tfidf_prefix"].detach().cpu().numpy()
    tossup_T = observations.groupby("tossup_id")["T_j"].first()
    grid = np.linspace(0.0, 1.0, n_points)
    values = np.zeros((len(data["tossup_ids"]), n_points))
    for index, tossup_id in enumerate(data["tossup_ids"]):
        T = int(tossup_T[tossup_id])
        token = np.clip(np.rint(grid * T).astype(int), 1, min(T, prefix.shape[1]))
        values[index] = lambda_tfidf * prefix[index, token - 1]
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
):
    """Fit the TF-IDF clue-adjusted competing-risks model, return medians + loss."""
    return fit_svi(
        competing_risks_model,
        (data, n_dimensions, calibrate_correctness, tfidf_effect_prior_scale),
        n_steps,
        lr,
    )


def run_experiment(args):
    """Run the full isolated TF-IDF baseline pyramidal pipeline."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)

    # Load tables -> build BUZZ/CENSORED/NO-BUZZ rows -> index into tensors.
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    observations = build_tossup_observations(tables)
    if observations.empty:
        raise ValueError("No tossup observations matched the requested data selection")
    data = tossup_tensors(observations, args.device)
    # Compute TF-IDF clue features from tossup text and attach them onto 'data'.
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
        f"TF-IDF vocab: {tfidf_summary['vocabulary_size']:,}"
    )
    print(observations["z"].value_counts().to_string())

    posterior, losses = train_model(
        data,
        args.dimensions,
        args.steps,
        args.lr,
        args.calibrate_correctness,
        args.tfidf_effect_prior_scale,
    )

    save_parameters(args.output_dir, data, posterior)
    # Persist the effective-difficulty adjustment so the shared evaluator can
    # redraw d'(t) without recomputing text features.
    save_tfidf_adjustment_curves(args.output_dir, data, observations, posterior)
    save_loss_plot(args.output_dir, losses, "TF-IDF baseline pyramidal training loss")

    # Attach fitted predictions and TF-IDF features onto the observation rows.
    correct, hazard, survival, tfidf_score = posterior_row_predictions(
        data, posterior, args.calibrate_correctness
    )
    buzz_expected = (
        expected_first_buzz_positions(data, posterior)
        if args.predict_buzz_positions
        else None
    )
    save_tossup_predictions(
        args.output_dir,
        observations,
        correct,
        hazard,
        survival,
        buzz_expected=buzz_expected,
        extra_columns={"tfidf_prefix_score": tfidf_score},
    )

    summary = {
        "model": "tfidf-baseline-pyramidal",
        "formula": FORMULA,
        "split": args.split,
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "steps": args.steps,
        "lr": args.lr,
        "seed": args.seed,
        "final_loss": losses[-1],
        "calibrate_correctness": args.calibrate_correctness,
        "tfidf_effect_prior_scale": args.tfidf_effect_prior_scale,
        "tfidf_clue_effect": float(
            posterior["tfidf_clue_effect"].detach().cpu()
        ),
        "tfidf_features": tfidf_summary,
        "players": len(data["player_ids"]),
        "tossups": len(data["tossup_ids"]),
        "events": len(data["event_ids"]),
        "predicted_buzz_positions": args.predict_buzz_positions,
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
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
        "--tfidf-effect-prior-scale",
        type=float,
        default=1.0,
        help="HalfNormal prior scale for learned nonnegative TF-IDF effects",
    )
    parser.add_argument(
        "--no-normalize-tfidf",
        action="store_true",
        help="Use raw cumulative TF-IDF mass instead of scaling each tossup to end at 1",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    if args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    if args.tfidf_effect_prior_scale <= 0:
        raise ValueError("--tfidf-effect-prior-scale must be positive")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
