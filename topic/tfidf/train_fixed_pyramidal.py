"""Train the dedicated fixed-topic TF-IDF pyramidal experiment.

The trainer accepts every existing fixed topic-vector source (PLDA, LDA, or
category one-hots). Unlike the baseline topic trainer, cumulative TF-IDF is
always part of this isolated model and one nonnegative lambda is learned for
each topic coordinate.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from holdout.player_priors import attach_player_priors, player_tier_map
from tfidf.tfidf_features import attach_tfidf_prefix_scores
from topic.fixed.topic_compirt.topics import align_tossup_topic_weights
from topic.fixed.train_topic_pyramidal import save_topic_parameters
from topic.tfidf.outputs import lambda_mapping, save_adjustment_curves, save_lambdas
from topic.tfidf.pyramidal import (
    competing_risks_model,
    expected_first_buzz_positions,
    posterior_row_predictions,
    row_tfidf_prefix_scores,
)
from topic.utils.outputs import DEFAULT_TOPIC_VECTORS, REPO_ROOT
from utils.saving import (
    save_loss_plot,
    save_player_posterior,
    save_tossup_predictions,
    write_summary,
)
from utils.training import fit_svi, require_device


DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "topic-tfidf-pyramidal"
FORMULA = (
    "d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t); "
    "logit_ij(t) = sum_k r_jk * (theta_ik - d'_jk(t))"
)


def train_model(
    data,
    n_dimensions,
    n_steps=1000,
    lr=0.02,
    calibrate_correctness=False,
    prior_scale=1.0,
):
    """Fit the isolated fixed-topic TF-IDF competing-risks model."""
    return fit_svi(
        competing_risks_model,
        (data, n_dimensions, calibrate_correctness, prior_scale),
        n_steps,
        lr,
        return_guide=True,
    )


def run_experiment(args):
    """Run feature construction, fitting, replay, and dedicated output writing."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    tables = filter_tournament(
        load_hf_tables(args.data_dir, args.split), args.tournament
    )
    observations = build_tossup_observations(tables)
    if observations.empty:
        raise ValueError("No tossup observations matched the requested data selection")
    data = tossup_tensors(observations, args.device)
    tfidf_summary = attach_tfidf_prefix_scores(
        data, tables, normalize=not args.no_normalize_tfidf, device=args.device
    )

    topic_weight, topic_columns = align_tossup_topic_weights(
        data, args.topic_vectors, args.dimensions
    )
    data["topic_weight"] = topic_weight
    dimensions = len(topic_columns)
    print(
        f"Rows: {len(observations):,}  Players: {len(data['player_ids']):,}  "
        f"Tossups: {len(data['tossup_ids']):,}  Topic dimensions: {dimensions}  "
        f"IDF vocab: {tfidf_summary['vocabulary_size']:,}"
    )
    print(observations["z"].value_counts().to_string())

    tier_map = player_tier_map(tables)
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

    posterior, guide, losses = train_model(
        data,
        dimensions,
        args.steps,
        args.lr,
        args.calibrate_correctness,
        args.effect_prior_scale,
    )
    save_topic_parameters(args.output_dir, data, posterior)
    save_player_posterior(args.output_dir, data["player_ids"], guide, tier_map)
    save_lambdas(args.output_dir, topic_columns, posterior["topic_tfidf_lambdas"])
    save_adjustment_curves(
        args.output_dir,
        data,
        observations,
        data["topic_weight"],
        posterior["topic_tfidf_lambdas"],
    )
    save_loss_plot(
        args.output_dir, losses, "Topic-specific TF-IDF pyramidal IRT training loss"
    )

    correct, hazard, survival = posterior_row_predictions(
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
        extra_columns={"tfidf_prefix_score": row_tfidf_prefix_scores(data)},
    )

    summary = {
        "model": "topic-tfidf-pyramidal",
        "formula": FORMULA,
        "topic_vectors": str(args.topic_vectors),
        "topic_dimensions": dimensions,
        "topic_columns": topic_columns,
        "topic_tfidf_lambdas": lambda_mapping(
            topic_columns, posterior["topic_tfidf_lambdas"]
        ),
        "topic_tfidf_effect_prior_scale": args.effect_prior_scale,
        "tfidf_features": tfidf_summary,
        "tfidf_adjustment_curve": "topic_weighted_aggregate",
        "tournament": args.tournament or "",
        "dimensions": dimensions,
        "steps": args.steps,
        "lr": args.lr,
        "final_loss": losses[-1],
        "calibrate_correctness": args.calibrate_correctness,
        "players": len(data["player_ids"]),
        "tossups": len(data["tossup_ids"]),
        "events": len(data["event_ids"]),
        "predicted_buzz_positions": args.predict_buzz_positions,
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
    write_summary(args.output_dir, summary, posterior)
    return summary


def parse_args():
    """Parse options for the dedicated fixed-topic TF-IDF experiment."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--topic-vectors", type=Path, default=DEFAULT_TOPIC_VECTORS)
    parser.add_argument(
        "--dimensions",
        type=int,
        default=None,
        help="Latent skill dimensions; defaults to topic-vector column count.",
    )
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--predict-buzz-positions", action="store_true")
    parser.add_argument("--calibrate-correctness", action="store_true")
    parser.add_argument(
        "--effect-prior-scale",
        "--topic-tfidf-effect-prior-scale",
        dest="effect_prior_scale",
        type=float,
        default=1.0,
        help="HalfNormal prior scale for the per-topic TF-IDF lambda vector.",
    )
    parser.add_argument(
        "--no-normalize-tfidf",
        action="store_true",
        help="Use raw cumulative TF-IDF rather than normalized prefix mass.",
    )
    parser.add_argument("--train-posterior", type=Path)
    parser.add_argument(
        "--new-player-prior",
        choices=("tier", "flat"),
        default="tier",
        help="Prior for unseen players in a held-out transductive fit.",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    if args.dimensions is not None and args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    if args.effect_prior_scale <= 0:
        raise ValueError("--effect-prior-scale must be positive")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
