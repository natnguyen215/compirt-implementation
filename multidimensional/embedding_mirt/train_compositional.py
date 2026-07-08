"""Train the embedding-relevance compositional bonus model.

This is the embedding-relevance counterpart to the root 'train_compositional.py'
and 'topic/fixed/train_topic_compositional.py'. Like those scripts, it does not
learn player skill from scratch: it loads the fixed 'theta' vectors from the
pyramidal stage, holds them fixed, and learns per-dimension bonus-part
difficulty. Each bonus's relevance vector 'r_b' is computed once, up front,
from its frozen embedding and the **frozen** projection ('r_projection.npz')
fit during pyramidal training -- this stage never retrains that projection, it
only reuses it, the same way it reuses 'theta'.

Start reading at 'run_experiment' near the bottom; it coordinates the full
load -> build -> train -> predict -> save workflow.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_data import (
    DEFAULT_DATA_DIR,
    bonus_tensors,
    build_bonus_part_observations,
    filter_tournament,
    load_hf_tables,
)
from multidimensional.embedding_mirt.compositional_model import (
    compositional_model,
    posterior_predictions,
)
from multidimensional.embedding_mirt.embeddings import (
    align_bonus_embeddings,
    center_embeddings,
    check_projection_shapes,
    load_projection_state,
)
from multidimensional.embedding_mirt.pyramidal_model import project_relevance
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


DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "embedding-compositional"
DEFAULT_EMBEDDINGS = (
    REPO_ROOT / "multidimensional" / "embedding_mirt" / "outputs" / "bonus_embeddings.npz"
)
FORMULA = "logit_rb = LSE_m(sum_k r_bk * theta_pmk; tau) - sum_k r_bk * beta_bk"


def train_model(
    data, theta, r, use_synergy, synergy_dimensions, n_steps, lr,
    calibrate_correctness=False,
):
    """Fit bonus-part parameters while 'theta' and 'r' are both fixed."""
    return fit_svi(
        compositional_model,
        (data, theta, r, use_synergy, synergy_dimensions, calibrate_correctness),
        n_steps,
        lr,
    )


def save_bonus_part_parameters(output_dir, data, r, posterior):
    """Write bonus-part parameters, including the frozen relevance 'r'."""
    part_parameters = {"bonus_part_id": data["part_ids"]}
    add_numbered_tensor_columns(part_parameters, "beta", posterior["beta"])
    add_numbered_tensor_columns(part_parameters, "r", r)
    pd.DataFrame(part_parameters).to_csv(output_dir / "bonus_parts.csv", index=False)


def run_experiment(args):
    """Run the complete embedding-relevance compositional pipeline."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)

    player_ids, theta = load_player_skills(args.player_skills, args.device)

    tables = filter_tournament(
        load_hf_tables(args.data_dir, args.split), args.tournament
    )
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

    data = bonus_tensors(observations, player_ids, args.device)
    # Frozen projection from the paired pyramidal run: this stage reuses the
    # embedding-to-r FFN exactly as fit on tossups, it does not learn its own.
    projection, embedding_mean = load_projection_state(args.projection, args.device)
    embedding = align_bonus_embeddings(data, args.embeddings)
    check_projection_shapes(
        projection,
        embedding,
        theta,
        projection_path=args.projection,
        embeddings_path=args.embeddings,
        player_skills_path=args.player_skills,
        embedding_mean=embedding_mean,
    )
    embedding = center_embeddings(embedding, embedding_mean)
    with torch.no_grad():
        r = project_relevance(embedding, projection)
    print(
        f"Bonus part rows: {len(observations):,}  "
        f"Parts: {len(data['part_ids']):,}  "
        f"Relevance dimensions: {r.shape[1]}"
    )

    posterior, losses = train_model(
        data, theta, r, args.use_synergy, args.synergy_dimensions, args.steps, args.lr,
        args.calibrate_correctness,
    )
    probabilities, aggregates, synergy = posterior_predictions(
        data, theta, r, posterior, args.use_synergy, args.calibrate_correctness
    )

    save_bonus_part_parameters(args.output_dir, data, r, posterior)
    (args.output_dir / "tau.txt").write_text(
        f"{float(posterior['tau'].detach().cpu()):.8f}\n", encoding="utf-8"
    )

    save_bonus_predictions(
        args.output_dir, observations, probabilities, aggregates, synergy
    )

    save_loss_plot(
        args.output_dir, losses, "Embedding-relevance compositional IRT training loss"
    )
    if args.use_synergy and args.save_synergy_details:
        save_synergy_outputs(
            args.output_dir,
            player_ids,
            observations,
            posterior,
            tensor_values(synergy),
        )

    summary = {
        "model": "embedding-relevance-compositional",
        "formula": FORMULA,
        "embeddings": str(args.embeddings),
        "projection": str(args.projection),
        "projection_kind": projection["kind"],
        "centered_embeddings": embedding_mean is not None,
        "tournament": args.tournament or "",
        "steps": args.steps,
        "final_loss": losses[-1],
        "use_synergy": args.use_synergy,
        "synergy_dimensions": args.synergy_dimensions if args.use_synergy else 0,
        "saved_synergy_details": args.use_synergy and args.save_synergy_details,
        "calibrate_correctness": args.calibrate_correctness,
        "skill_dimensions": theta.shape[1],
        "bonus_part_observations": len(observations),
        "bonus_parts": len(data["part_ids"]),
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
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--embeddings", type=Path, default=DEFAULT_EMBEDDINGS)
    parser.add_argument(
        "--projection",
        type=Path,
        required=True,
        help="r_projection.npz saved by the paired train_pyramidal.py run",
    )
    parser.add_argument("--player-skills", type=Path, required=True)
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.02)
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
