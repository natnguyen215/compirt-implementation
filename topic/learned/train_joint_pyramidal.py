"""Jointly train topic-gated CompIRT topics (sLDA-style) with the pyramidal model.

This replaces the fixed-CSV topic weights of 'topic/fixed/train_topic_pyramidal'
with a Dirichlet topic model trained *inside* the same SVI: each tossup's topic
proportions 'theta_doc' gate the competing-risks likelihood, so buzz/answer
outcomes propagate into the topics. It is supervised-LDA in spirit, not the
canonical Blei-McAuliffe form -- 'r_j' = 'theta_doc' doubles as the IRT weight
rather than feeding a separate response regression. Bonuses are included as
word-only documents sharing the topic-word matrix, so their vectors come out of
the same fit for the downstream compositional stage. The objective is the topic-
weighted competing-risks log-likelihood plus the ('--bow-weight' scaled) LDA
word likelihood.

Outputs match the topic-pyramidal stage ('players.csv', 'tossups.csv',
'tossup_predictions.csv', 'summary.json', loss plot) plus a
'document_latent_vectors.csv' of the learned topic weights for tossups and
bonuses, so the downstream compositional and evaluation stages reuse it.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyro
import torch

from topic.learned.bow import bow_tensor, build_vocabulary
from topic.learned.joint_pyramidal import joint_model, topic_word_distributions

from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
    tossup_tensors,
)
from topic.fixed.topic_compirt.common import (
    add_numbered_tensor_columns,
    fit_svi,
    tensor_values,
)
from topic.fixed.topic_compirt.pyramidal import (
    expected_first_buzz_positions,
    posterior_row_predictions,
)
from topic.utils.corpus import load_documents
from topic.utils.outputs import (
    DEFAULT_DATABASE,
    DOCUMENT_VECTOR_FILENAME,
    document_vector_fieldnames,
    document_vector_row,
)
from utils.saving import (
    save_loss_plot,
    save_player_posterior,
    save_player_rankings,
)
from holdout.player_priors import attach_player_priors, player_tier_map


REPO_ROOT = Path(__file__).resolve().parents[2]


DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "joint-slda"
FORMULA = "logit_ij(t) = sum_k r_jk * (theta_ik - d_jk(t)),  r_j = theta_doc_j (Dirichlet)"


def build_corpus(database, tossup_ids, bonus_ids):
    """Return (documents_by_id, combined_ids, bonus_ids) ordered tossups-first.

    'combined_ids' is the model's document order: every observed tossup (in
    'tossup_ids' order) followed by every selected bonus. Filtering to these IDs
    keeps a 2024 training run from learning vocabulary/topics from 2025 text.
    """
    documents = load_documents(database, "both")
    documents_by_id = {str(doc["document_id"]): doc for doc in documents}
    combined_ids = [str(value) for value in tossup_ids] + [
        str(value) for value in bonus_ids
    ]
    missing = [
        identifier for identifier in combined_ids if identifier not in documents_by_id
    ]
    if missing:
        raise ValueError(f"No text document for ids: {', '.join(missing[:5])}")
    documents = [documents_by_id[identifier] for identifier in combined_ids]
    return (
        documents,
        {str(doc["document_id"]): doc for doc in documents},
        combined_ids,
        [str(value) for value in bonus_ids],
    )


def save_parameters(output_dir, data, posterior):
    """Write player and tossup parameter tables, including learned topic weights."""
    players = {"player_id": data["player_ids"], "c": tensor_values(posterior["c"])}
    add_numbered_tensor_columns(players, "theta", posterior["theta"])
    player_df = pd.DataFrame(players)
    player_df["theta_norm"] = np.linalg.norm(
        player_df.filter(like="theta_").to_numpy(), axis=1
    )
    player_df.to_csv(output_dir / "players.csv", index=False)

    tossups = {"tossup_id": data["tossup_ids"]}
    # This is CompIRT difficulty_beta, not LDA beta/topic_word. The column prefix
    # stays "beta" because topic_compirt evaluation already consumes beta_*.
    add_numbered_tensor_columns(tossups, "beta", posterior["beta"])
    add_numbered_tensor_columns(tossups, "gamma", posterior["gamma"])
    add_numbered_tensor_columns(tossups, "mu", posterior["mu"])
    add_numbered_tensor_columns(tossups, "topic_weight", data["topic_weight"])
    pd.DataFrame(tossups).to_csv(output_dir / "tossups.csv", index=False)


def write_topics(output_dir, vocabulary, top_n):
    """Write 'topics.csv': the top words per topic from the fitted topic-word matrix."""
    weights = topic_word_distributions().cpu()
    with (output_dir / "topics.csv").open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["topic_id", "label", "top_words"])
        writer.writeheader()
        for topic_id in range(weights.shape[0]):
            top = torch.topk(weights[topic_id], min(top_n, len(vocabulary))).indices
            words = [vocabulary[index] for index in top.tolist()]
            writer.writerow(
                {
                    "topic_id": topic_id,
                    "label": f"latent_topic_{topic_id:02d}",
                    "top_words": " ".join(words),
                }
            )


def write_topic_model(output_dir, vocabulary):
    """Persist the fitted topic_word matrix and vocabulary for the bonus stage.

    The learned-compositional stage ('train_joint_compositional') freezes these
    so its bonus topic proportions live in the same axes as the player skills.
    """
    np.save(output_dir / "topic_word_matrix.npy", topic_word_distributions().cpu().numpy())
    (output_dir / "vocabulary.json").write_text(
        json.dumps(list(vocabulary)), encoding="utf-8"
    )


def write_document_vectors(output_dir, documents_by_id, ordered_ids, weights, dimensions):
    """Write the standard topic-vector CSV from aligned ids and topic weights."""
    path = output_dir / DOCUMENT_VECTOR_FILENAME
    with path.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=document_vector_fieldnames(dimensions))
        writer.writeheader()
        for identifier, vector in zip(ordered_ids, weights):
            writer.writerow(document_vector_row(documents_by_id[identifier], vector.tolist()))


def run_experiment(args):
    """Run the complete joint supervised-LDA + pyramidal pipeline."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.device == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested, but no CUDA device is available")
    pyro.set_rng_seed(args.seed)

    # Tossup observations and training tensors.
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    observations = build_tossup_observations(tables)
    if observations.empty:
        raise ValueError("No tossup observations matched the requested data selection")
    data = tossup_tensors(observations, args.device)
    n_tossups = len(data["tossup_ids"])

    # Build the document corpus (tossups first), vocabulary, and bag-of-words.
    documents, documents_by_id, combined_ids, bonus_ids = build_corpus(
        args.database, data["tossup_ids"], tables["bonuses"]["bonus_id"]
    )
    # Held-out evaluation reuses the training run's frozen topic-word matrix so
    # 2025 documents are scored against trained topics; that requires the training
    # vocabulary (same column order) rather than a freshly built one.
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
            documents, vocab_size=args.vocab_size, min_df=args.min_df, rm_top=args.rm_top
        )
    data["bow"] = bow_tensor(documents, vocabulary_index, combined_ids, device=args.device)
    if frozen_topic_word is not None:
        data["fixed_topic_word"] = frozen_topic_word
    print(
        f"Rows: {len(observations):,}  Players: {len(data['player_ids']):,}  "
        f"Tossups: {n_tossups:,}  Bonuses: {len(bonus_ids):,}  "
        f"Vocab: {len(vocabulary):,}  Topics: {args.dimensions}"
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
            n_dimensions=args.dimensions,
            tier_map=tier_map,
        )
        print(f"Held-out player priors: {prior_summary}")

    # Joint SVI: one AutoNormal guide covers every latent (incl. theta_doc).
    model_args = (
        data, args.dimensions, len(vocabulary), args.bow_weight,
        args.topic_concentration, args.calibrate_correctness,
    )
    posterior, guide, losses = fit_svi(
        joint_model, model_args, args.steps, args.lr, return_guide=True
    )

    # Split the document topic proportions into tossup and bonus weights.
    theta_doc = posterior["theta_doc"]
    data["topic_weight"] = theta_doc[:n_tossups]
    document_weights = theta_doc.detach().cpu()

    save_parameters(args.output_dir, data, posterior)
    save_player_posterior(args.output_dir, data["player_ids"], guide, tier_map)
    # The topic-word matrix is only re-learned on a from-scratch run; a held-out
    # pass reuses the frozen training matrix, so there is nothing new to persist.
    if frozen_topic_word is None:
        write_topics(args.output_dir, vocabulary, args.top_n)
        write_topic_model(args.output_dir, vocabulary)
    write_document_vectors(
        args.output_dir, documents_by_id, combined_ids, document_weights, args.dimensions
    )
    save_loss_plot(args.output_dir, losses, "Joint supervised-LDA + pyramidal training loss")

    # Replay per-row predictions at the fitted medians.
    predictions = observations.copy()
    correct, hazard, survival = posterior_row_predictions(
        data, posterior, args.calibrate_correctness
    )
    predictions["predicted_correct"] = tensor_values(correct)
    predictions["predicted_hazard"] = tensor_values(hazard)
    predictions["predicted_survival"] = tensor_values(survival)
    predictions.to_csv(args.output_dir / "tossup_predictions.csv", index=False)
    save_player_rankings(args.output_dir, predictions)

    if args.predict_buzz_positions:
        expected = expected_first_buzz_positions(data, posterior)
        buzz_events = predictions[predictions["z"] == "BUZZ"][
            ["event_id", "relative_position"]
        ].rename(columns={"relative_position": "observed_relative_position"})
        buzz_events["predicted_relative_position"] = buzz_events["event_id"].map(expected)
        buzz_events.to_csv(args.output_dir / "buzz_event_predictions.csv", index=False)

    summary = {
        "model": "joint-slda-pyramidal",
        "formula": FORMULA,
        "split": args.split,
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "vocab_size": len(vocabulary),
        "bow_weight": args.bow_weight,
        "topic_concentration": args.topic_concentration,
        "steps": args.steps,
        "lr": args.lr,
        "final_loss": losses[-1],
        "calibrate_correctness": args.calibrate_correctness,
        "players": len(data["player_ids"]),
        "tossups": n_tossups,
        "bonuses": len(bonus_ids),
        "events": len(data["event_ids"]),
        "observation_counts": observations["z"].value_counts().to_dict(),
    }
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--dimensions", type=int, default=5, help="Topics == IRT skill dims.")
    parser.add_argument("--vocab-size", type=int, default=2000)
    parser.add_argument("--min-df", type=int, default=2)
    parser.add_argument("--rm-top", type=int, default=20)
    parser.add_argument(
        "--topic-concentration",
        type=float,
        default=1.0,
        help="Dirichlet alpha for theta_doc; lower (<1) gives sparser topic mixes.",
    )
    parser.add_argument(
        "--bow-weight",
        type=float,
        default=1.0,
        help="Scale on the LDA word likelihood vs. the IRT competing-risks factor.",
    )
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--top-n", type=int, default=15)
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
        "--train-topic-model",
        type=Path,
        help="training run output dir holding topic_word_matrix.npy + "
        "vocabulary.json to freeze for the held-out pass",
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
    if args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    if args.train_posterior and not args.train_topic_model:
        raise ValueError(
            "--train-posterior requires --train-topic-model so the held-out pass "
            "reuses the trained topics/vocabulary"
        )
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
