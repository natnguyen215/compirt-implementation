"""Jointly train topic-gated CompIRT bonus topics (sLDA-style) with the compositional model.

This is the bonus-stage counterpart to 'train_joint_pyramidal'. The pyramidal
stage first learns player skills 'theta' and the topic-word matrix 'topic_word';
this stage freezes both and re-learns each bonus's Dirichlet topic proportions
'theta_doc' inside one SVI, so the bonus's part-correctness outcomes (not just
its words) reshape its place in topic space (sLDA-style supervision for bonuses).
It is supervised-LDA in spirit, not the canonical Blei-McAuliffe form: 'r_b' =
'theta_doc' doubles as the compositional weight rather than feeding a separate
response regression. The objective is the topic-weighted bonus-part log-likelihood
plus the ('--bow-weight' scaled) LDA word likelihood with 'topic_word' held fixed.

Outputs match the topic-compositional stage ('bonus_parts.csv', 'tau.txt',
'bonus_part_predictions.csv', 'team_predictions.csv', 'summary.json', loss
plot) plus a 'document_latent_vectors.csv' of the learned bonus topic weights,
so the downstream evaluation and profiling stages reuse it.

Start reading at 'run_experiment' near the bottom; it coordinates the full
load -> build -> train -> predict -> save workflow.
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

from topic.learned.bow import bow_tensor
from topic.learned.joint_compositional import (
    joint_compositional_model,
    joint_posterior_predictions,
)

from compirt_data import (
    DEFAULT_DATA_DIR,
    bonus_tensors,
    build_bonus_part_observations,
    filter_tournament,
    load_hf_tables,
)
from topic.fixed.topic_compirt.topics import bonus_id_from_part_id
from topic.utils.corpus import load_documents
from topic.utils.outputs import (
    DEFAULT_DATABASE,
    DOCUMENT_VECTOR_FILENAME,
    document_vector_fieldnames,
    document_vector_row,
)
from train_compositional import load_player_skills
from utils.saving import (
    add_numbered_tensor_columns,
    save_bonus_predictions,
    save_loss_plot,
    save_synergy_outputs,
    tensor_values,
    write_summary,
)
from utils.training import fit_svi, require_device


REPO_ROOT = Path(__file__).resolve().parents[2]


DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "joint-slda-compositional"
FORMULA = (
    "logit_rb = LSE_m(sum_k r_bk * theta_pmk; tau) "
    "- sum_k r_bk * difficulty_beta_bk,  r_b = theta_doc_b (Dirichlet, sLDA)"
)


def build_part_doc_index(part_ids):
    """Map bonus parts to shared bonus-document rows.

    Returns '(ordered_bonus_ids, part_doc_index)': 'ordered_bonus_ids' lists
    each distinct base bonus id in first-appearance order (the document order of
    'theta_doc'), and 'part_doc_index[i]' is the document row of the bonus
    that 'part_ids[i]' belongs to. All three parts of a bonus share one row.
    """
    ordered_bonus_ids: list[str] = []
    row_of: dict[str, int] = {}
    part_doc_index: list[int] = []
    for part_id in part_ids:
        base = bonus_id_from_part_id(part_id)
        if base not in row_of:
            row_of[base] = len(ordered_bonus_ids)
            ordered_bonus_ids.append(base)
        part_doc_index.append(row_of[base])
    return ordered_bonus_ids, part_doc_index


def load_topic_model(topic_model_dir, device):
    """Load the fixed topic-word matrix and vocabulary from the pyramidal stage."""
    matrix_path = topic_model_dir / "topic_word_matrix.npy"
    vocab_path = topic_model_dir / "vocabulary.json"
    if not matrix_path.exists() or not vocab_path.exists():
        raise FileNotFoundError(
            f"{topic_model_dir} must contain topic_word_matrix.npy and "
            "vocabulary.json (re-run train_joint_pyramidal to export them)"
        )
    topic_word_matrix = np.load(matrix_path)
    vocabulary = json.loads(vocab_path.read_text(encoding="utf-8"))
    if topic_word_matrix.shape[1] != len(vocabulary):
        raise ValueError(
            f"topic_word_matrix has {topic_word_matrix.shape[1]} columns but vocabulary has "
            f"{len(vocabulary)} words"
        )
    topic_word = torch.tensor(topic_word_matrix, dtype=torch.float32, device=device)
    vocabulary_index = {word: index for index, word in enumerate(vocabulary)}
    return topic_word, vocabulary, vocabulary_index


def save_bonus_part_parameters(output_dir, data, posterior, part_topic_weight):
    """Write bonus-part parameters, including the learned per-bonus topic weights."""
    part_parameters = {"bonus_part_id": data["part_ids"]}
    # This is CompIRT difficulty_beta, not LDA beta/topic_word. The column prefix
    # stays "beta" because topic_compirt evaluation already consumes beta_*.
    add_numbered_tensor_columns(part_parameters, "beta", posterior["beta"])
    add_numbered_tensor_columns(part_parameters, "topic_weight", part_topic_weight)
    pd.DataFrame(part_parameters).to_csv(output_dir / "bonus_parts.csv", index=False)


def write_document_vectors(output_dir, documents_by_id, ordered_ids, weights, dimensions):
    """Write the standard topic-vector CSV from aligned ids and learned weights."""
    path = output_dir / DOCUMENT_VECTOR_FILENAME
    with path.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=document_vector_fieldnames(dimensions))
        writer.writeheader()
        for identifier, vector in zip(ordered_ids, weights):
            writer.writerow(document_vector_row(documents_by_id[identifier], vector.tolist()))


def run_experiment(args):
    """Run the complete joint supervised-LDA + compositional bonus pipeline."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)

    # Fixed inputs from the pyramidal stage: player skills and the topic axes.
    player_ids, theta = load_player_skills(args.player_skills, args.device)
    topic_word, vocabulary, vocabulary_index = load_topic_model(
        args.topic_model_dir, args.device
    )
    dimensions = theta.shape[1]
    if topic_word.shape[0] != dimensions:
        raise ValueError(
            f"theta has {dimensions} skill dimensions but topic_word_matrix has "
            f"{topic_word.shape[0]} topics; they must match"
        )

    # Bonus-part observations, keeping only rows with a fully-known roster.
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    observations = build_bonus_part_observations(tables)
    if observations.empty:
        raise ValueError("No bonus observations matched the requested data selection")
    known_players = set(player_ids)
    known_roster = [
        bool(roster) and all(player in known_players for player in roster)
        for roster in observations["player_ids"]
    ]
    observations = observations[known_roster].reset_index(drop=True)
    if observations.empty:
        raise ValueError(
            "No bonus observations have fitted tossup skills for the full roster"
        )

    # Training tensors, plus the bonus corpus / bag-of-words (fixed vocabulary).
    data = bonus_tensors(observations, player_ids, args.device)
    ordered_bonus_ids, part_doc_index = build_part_doc_index(data["part_ids"])
    documents = load_documents(args.database, "bonuses")
    documents_by_id = {str(doc["document_id"]): doc for doc in documents}
    data["part_doc_index"] = torch.tensor(
        part_doc_index, dtype=torch.long, device=args.device
    )
    data["bonus_bow"] = bow_tensor(
        documents, vocabulary_index, ordered_bonus_ids, device=args.device
    )
    print(
        f"Bonus part rows: {len(observations):,}  "
        f"Parts: {len(data['part_ids']):,}  Bonuses: {len(ordered_bonus_ids):,}  "
        f"Vocab: {len(vocabulary):,}  Topics: {dimensions}"
    )

    # Joint SVI: one AutoNormal guide covers theta_doc + bonus-part parameters.
    # The topic dimension is read from theta inside the model.
    model_args = (
        data, theta, topic_word, args.bow_weight,
        args.topic_concentration, args.use_synergy, args.synergy_dimensions,
        args.calibrate_correctness,
    )
    posterior, losses = fit_svi(joint_compositional_model, model_args, args.steps, args.lr)

    # Learned per-bonus topic weights, then the per-part view (parts share a bonus).
    document_weights = posterior["theta_doc"].detach().cpu()
    part_topic_weight = posterior["theta_doc"][data["part_doc_index"]]

    # Replay predictions at the fitted posterior medians.
    probabilities, aggregates, synergy = joint_posterior_predictions(
        data, theta, posterior, args.use_synergy, args.calibrate_correctness
    )

    # Save the fitted bonus-part parameters, learned topics, and tau.
    save_bonus_part_parameters(args.output_dir, data, posterior, part_topic_weight)
    write_document_vectors(
        args.output_dir, documents_by_id, ordered_bonus_ids, document_weights, dimensions
    )
    (args.output_dir / "tau.txt").write_text(
        f"{float(posterior['tau'].detach().cpu()):.8f}\n", encoding="utf-8"
    )

    # Save per-part predictions, then aggregate to expected per-team bonus points.
    save_bonus_predictions(
        args.output_dir, observations, probabilities, aggregates, synergy
    )

    save_loss_plot(
        args.output_dir, losses, "Joint supervised-LDA + compositional training loss"
    )
    if args.use_synergy and args.save_synergy_details:
        save_synergy_outputs(
            args.output_dir, player_ids, observations, posterior, tensor_values(synergy)
        )

    summary = {
        "model": "joint-slda-compositional",
        "formula": FORMULA,
        "topic_model_dir": str(args.topic_model_dir),
        "player_skills": str(args.player_skills),
        "split": args.split,
        "tournament": args.tournament or "",
        "skill_dimensions": dimensions,
        "vocab_size": len(vocabulary),
        "bow_weight": args.bow_weight,
        "topic_concentration": args.topic_concentration,
        "steps": args.steps,
        "lr": args.lr,
        "final_loss": losses[-1],
        "use_synergy": args.use_synergy,
        "synergy_dimensions": args.synergy_dimensions if args.use_synergy else 0,
        "saved_synergy_details": args.use_synergy and args.save_synergy_details,
        "calibrate_correctness": args.calibrate_correctness,
        "bonus_part_observations": len(observations),
        "bonus_parts": len(data["part_ids"]),
        "bonuses": len(ordered_bonus_ids),
        "tau": float(posterior["tau"].detach().cpu()),
    }
    if args.use_synergy:
        synergy_array = tensor_values(synergy)
        summary.update(
            {
                "mean_synergy_contribution": float(synergy_array.mean()),
                "median_synergy_contribution": float(np.median(synergy_array)),
                "negative_synergy_fraction": float((synergy_array < 0).mean()),
                "positive_synergy_fraction": float((synergy_array > 0).mean()),
            }
        )
    write_summary(args.output_dir, summary, posterior)
    return summary


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--player-skills", type=Path, required=True)
    parser.add_argument(
        "--topic-model-dir",
        type=Path,
        required=True,
        help="Pyramidal-stage output dir holding topic_word_matrix.npy + vocabulary.json",
    )
    parser.add_argument(
        "--bow-weight",
        type=float,
        default=1.0,
        help="Scale on the LDA word likelihood vs. the bonus-part likelihood.",
    )
    parser.add_argument(
        "--topic-concentration",
        type=float,
        default=1.0,
        help="Dirichlet alpha for theta_doc; lower (<1) gives sparser topic mixes.",
    )
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--use-synergy", action="store_true")
    parser.add_argument("--synergy-dimensions", type=int, default=1)
    parser.add_argument("--save-synergy-details", action="store_true")
    parser.add_argument(
        "--calibrate-correctness",
        action="store_true",
        help="Add a learned global scale+bias (Platt scaling) to the bonus-part logit",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    if args.steps < 1:
        raise ValueError("--steps must be at least 1")
    if args.synergy_dimensions < 1:
        raise ValueError("--synergy-dimensions must be at least 1")
    return args


if __name__ == "__main__":
    run_experiment(parse_args())
