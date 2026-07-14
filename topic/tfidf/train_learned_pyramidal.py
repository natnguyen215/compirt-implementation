"""Train the dedicated learned-topic TF-IDF pyramidal experiment.

The model learns Dirichlet document topic proportions jointly with the
topic-specific TF-IDF competing-risks likelihood. It mirrors the learned-topic
workflow's data and held-out conventions, while keeping this Stage 1 variant
and its outputs independent from ordinary learned-topic runs.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pyro
import torch

from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from holdout.player_priors import attach_player_priors, player_tier_map
from tfidf.tfidf_features import attach_tfidf_prefix_scores
from topic.learned.bow import bow_tensor, build_vocabulary
# The learned-topic writers read the fitted "topic_word_logits" Pyro param, so
# they persist this run's topics/vocabulary/document vectors unchanged.
from topic.learned.train_joint_pyramidal import (
    build_corpus,
    save_parameters,
    write_document_vectors,
    write_topic_model,
    write_topics,
)
from topic.tfidf.joint_pyramidal import joint_model
from topic.tfidf.outputs import lambda_mapping, save_adjustment_curves, save_lambdas
from topic.tfidf.pyramidal import (
    expected_first_buzz_positions,
    posterior_row_predictions,
    row_tfidf_prefix_scores,
)
from topic.utils.outputs import DEFAULT_DATABASE, latent_topic_columns
from utils.saving import (
    save_loss_plot,
    save_player_posterior,
    save_tossup_predictions,
    write_summary,
)
from utils.training import fit_svi, require_device


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "joint-slda-tfidf"
FORMULA = (
    "d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t); "
    "logit_ij(t) = sum_k r_jk * (theta_ik - d'_jk(t)), "
    "r_j = theta_doc_j (Dirichlet)"
)


def run_experiment(args):
    """Run the complete learned-topic TF-IDF experiment and save its artifacts."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)
    tables = filter_tournament(
        load_hf_tables(args.data_dir, args.split), args.tournament
    )
    observations = build_tossup_observations(tables)
    if observations.empty:
        raise ValueError("No tossup observations matched the requested data selection")
    data = tossup_tensors(observations, args.device)
    n_tossups = len(data["tossup_ids"])
    tfidf_summary = attach_tfidf_prefix_scores(
        data, tables, normalize=not args.no_normalize_tfidf, device=args.device
    )

    documents, documents_by_id, combined_ids, bonus_ids = build_corpus(
        args.database, data["tossup_ids"], tables["bonuses"]["bonus_id"]
    )
    frozen_topic_word = None
    if args.train_posterior and args.train_topic_model:
        vocabulary = json.loads(
            (args.train_topic_model / "vocabulary.json").read_text(encoding="utf-8")
        )
        vocabulary_index = {word: index for index, word in enumerate(vocabulary)}
        frozen_topic_word = torch.tensor(
            np.load(args.train_topic_model / "topic_word_matrix.npy"),
            dtype=torch.float32,
            device=args.device,
        )
    else:
        vocabulary, vocabulary_index = build_vocabulary(
            documents,
            vocab_size=args.vocab_size,
            min_df=args.min_df,
            rm_top=args.rm_top,
        )
    data["bow"] = bow_tensor(
        documents, vocabulary_index, combined_ids, device=args.device
    )
    if frozen_topic_word is not None:
        data["fixed_topic_word"] = frozen_topic_word
    print(
        f"Rows: {len(observations):,}  Players: {len(data['player_ids']):,}  "
        f"Tossups: {n_tossups:,}  Bonuses: {len(bonus_ids):,}  "
        f"Vocab: {len(vocabulary):,}  Topics: {args.dimensions}  "
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
            n_dimensions=args.dimensions,
            tier_map=tier_map,
        )
        print(f"Held-out player priors: {prior_summary}")

    model_args = (
        data,
        args.dimensions,
        len(vocabulary),
        args.bow_weight,
        args.topic_concentration,
        args.calibrate_correctness,
        args.effect_prior_scale,
    )
    posterior, guide, losses = fit_svi(
        joint_model, model_args, args.steps, args.lr, return_guide=True
    )
    theta_doc = posterior["theta_doc"]
    data["topic_weight"] = theta_doc[:n_tossups]
    document_weights = theta_doc.detach().cpu()
    topic_columns = latent_topic_columns(args.dimensions)

    save_parameters(args.output_dir, data, posterior)
    save_player_posterior(args.output_dir, data["player_ids"], guide, tier_map)
    save_lambdas(args.output_dir, topic_columns, posterior["topic_tfidf_lambdas"])
    save_adjustment_curves(
        args.output_dir,
        data,
        observations,
        data["topic_weight"],
        posterior["topic_tfidf_lambdas"],
    )
    if frozen_topic_word is None:
        write_topics(args.output_dir, vocabulary, args.top_n)
        write_topic_model(args.output_dir, vocabulary)
    write_document_vectors(
        args.output_dir,
        documents_by_id,
        combined_ids,
        document_weights,
        args.dimensions,
    )
    save_loss_plot(
        args.output_dir,
        losses,
        "Joint supervised-LDA + topic-specific TF-IDF pyramidal training loss",
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
        "model": "joint-slda-topic-tfidf-pyramidal",
        "formula": FORMULA,
        "split": args.split,
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "vocab_size": len(vocabulary),
        "vocab_size_limit": args.vocab_size,
        "min_df": args.min_df,
        "rm_top": args.rm_top,
        "bow_weight": args.bow_weight,
        "topic_concentration": args.topic_concentration,
        "topic_tfidf_lambdas": lambda_mapping(
            topic_columns, posterior["topic_tfidf_lambdas"]
        ),
        "topic_tfidf_effect_prior_scale": args.effect_prior_scale,
        "tfidf_features": tfidf_summary,
        "tfidf_adjustment_curve": "topic_weighted_aggregate",
        "steps": args.steps,
        "lr": args.lr,
        "seed": args.seed,
        "new_player_prior": args.new_player_prior if args.train_posterior else "",
        "final_loss": losses[-1],
        "calibrate_correctness": args.calibrate_correctness,
        "players": len(data["player_ids"]),
        "tossups": n_tossups,
        "bonuses": len(bonus_ids),
        "events": len(data["event_ids"]),
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
    write_summary(args.output_dir, summary, posterior)
    return summary


def parse_args():
    """Parse options for the dedicated learned-topic TF-IDF experiment."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--dimensions", type=int, default=5)
    parser.add_argument("--vocab-size", type=int, default=2000)
    parser.add_argument("--min-df", type=int, default=2)
    parser.add_argument("--rm-top", type=int, default=20)
    parser.add_argument("--topic-concentration", type=float, default=1.0)
    parser.add_argument("--bow-weight", type=float, default=1.0)
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--top-n", type=int, default=15)
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
    parser.add_argument("--no-normalize-tfidf", action="store_true")
    parser.add_argument("--train-posterior", type=Path)
    parser.add_argument("--train-topic-model", type=Path)
    parser.add_argument("--new-player-prior", choices=("tier", "flat"), default="tier")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    if args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    if args.effect_prior_scale <= 0:
        raise ValueError("--effect-prior-scale must be positive")
    if args.train_posterior and not args.train_topic_model:
        raise ValueError(
            "--train-posterior requires --train-topic-model so the held-out pass "
            "reuses the trained topics and vocabulary"
        )
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
