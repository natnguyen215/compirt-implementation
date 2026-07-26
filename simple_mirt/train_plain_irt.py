"""Train the plain compensatory IRT comparator for the drop-robustness study.

This is the classical model the CompIRT paper extends (its Eq. 2):

    P(player i converts tossup j) = sigmoid(alpha_j^T theta_i - d_j)

It reuses 'simple_mirt/model.py' unchanged but is fed from the same tossup
observation frame as the CompIRT trainers (not the legacy SQLite response
matrix), so the identical '--drop-events' lists apply to every comparator.
A player has an observed cell for each tossup they were present for; the cell
is 1 only if they buzzed first and were correct — no buzz timing, censoring,
or competing risks.

Run as a module from the repo root:

    .venv/bin/python -m simple_mirt.train_plain_irt --split year_2024 ...
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd
import pyro
import torch

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_data import (
    DEFAULT_DATA_DIR,
    build_tossup_observations,
    filter_tournament,
    load_hf_tables,
)
from simple_mirt.model import model as plain_irt_model
from compirt_eval.drop_robustness.perturbations import (
    drop_tossup_events,
    load_event_drop_list,
)
from utils.posterior import add_posterior_output_args
from utils.saving import (
    add_numbered_tensor_columns,
    save_loss_plot,
    tensor_values,
    write_summary,
)
from utils.training import fit_svi, require_device

DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "compirt" / "plain-irt"


def response_matrix_from_observations(observations):
    """Build the player x tossup convert/no-convert matrix from event rows.

    Returns (responses, mask, player_ids, tossup_ids): a cell is observed
    (mask True) when the player was present for that tossup's event, and 1.0
    only when that player's BUZZ row was correct. Duplicate (player, tossup)
    pairs — a player hearing the same tossup twice — collapse to one cell
    that is 1.0 if any hearing converted.
    """
    player_ids = sorted(observations["player_id"].unique())
    tossup_ids = sorted(observations["tossup_id"].unique())
    player_index = {player_id: i for i, player_id in enumerate(player_ids)}
    tossup_index = {tossup_id: j for j, tossup_id in enumerate(tossup_ids)}

    responses = torch.zeros((len(player_ids), len(tossup_ids)))
    mask = torch.zeros((len(player_ids), len(tossup_ids)), dtype=torch.bool)

    present = observations[["player_id", "tossup_id"]].drop_duplicates()
    rows = torch.tensor(present["player_id"].map(player_index).to_numpy(dtype="int64"))
    cols = torch.tensor(present["tossup_id"].map(tossup_index).to_numpy(dtype="int64"))
    mask[rows, cols] = True

    converted = observations[
        (observations["z"] == "BUZZ") & (observations["y"] == 1)
    ][["player_id", "tossup_id"]].drop_duplicates()
    rows = torch.tensor(converted["player_id"].map(player_index).to_numpy(dtype="int64"))
    cols = torch.tensor(converted["tossup_id"].map(tossup_index).to_numpy(dtype="int64"))
    responses[rows, cols] = 1.0
    return responses, mask, player_ids, tossup_ids


def run_experiment(args):
    """Load observations, fit the plain IRT model, and save parameter CSVs."""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    require_device(args.device)
    pyro.set_rng_seed(args.seed)

    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    observations = build_tossup_observations(tables)
    if observations.empty:
        raise ValueError("No tossup observations matched the requested data selection")
    # Robustness studies pass a drop list to refit without the listed events.
    drop_info = None
    if args.drop_events:
        observations, drop_info = drop_tossup_events(
            observations, load_event_drop_list(args.drop_events)
        )
        print(f"Dropped events: {drop_info}")

    responses, mask, player_ids, tossup_ids = response_matrix_from_observations(
        observations
    )
    responses = responses.to(args.device)
    mask = mask.to(args.device)
    print(
        f"Players: {len(player_ids):,}  Tossups: {len(tossup_ids):,}  "
        f"Observed cells: {int(mask.sum()):,}"
    )

    posterior, _, losses = fit_svi(
        plain_irt_model,
        model_kwargs={
            "responses": responses,
            "mask": mask,
            "n_dimensions": args.dimensions,
        },
        n_steps=args.steps,
        lr=args.lr,
        posterior_output_dir=args.output_dir,
        posterior_draws=args.posterior_draws,
        posterior_seed=args.seed,
    )

    players = {"player_id": player_ids}
    add_numbered_tensor_columns(players, "theta", posterior["theta"])
    pd.DataFrame(players).to_csv(args.output_dir / "players.csv", index=False)

    questions = {"tossup_id": tossup_ids, "d": tensor_values(posterior["d"])}
    add_numbered_tensor_columns(questions, "alpha", posterior["alpha"])
    pd.DataFrame(questions).to_csv(args.output_dir / "questions.csv", index=False)

    save_loss_plot(args.output_dir, losses, "Plain IRT training loss")

    summary = {
        "model": "plain-irt",
        "formula": "P(convert) = sigmoid(alpha_j^T theta_i - d_j)",
        "split": args.split,
        "tournament": args.tournament or "",
        "dimensions": args.dimensions,
        "steps": args.steps,
        "lr": args.lr,
        "seed": args.seed,
        "final_loss": losses[-1],
        "players": len(player_ids),
        "tossups": len(tossup_ids),
        "observed_cells": int(mask.sum()),
    }
    if drop_info is not None:
        summary["drop_events_file"] = str(args.drop_events)
        summary.update(drop_info)
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
    parser.add_argument(
        "--drop-events",
        type=Path,
        help="text file of event_ids (one per line) to exclude before fitting; "
        "used by the data-dropping robustness study",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    add_posterior_output_args(parser)
    return parser.parse_args()


if __name__ == "__main__":
    run_experiment(parse_args())
