#!/usr/bin/env python3
"""Simulate randomized teams and packets from completed CompIRT fits."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_data import DEFAULT_DATA_DIR
from compirt_eval.imaginary_tournament import (
    load_tournament_inputs,
    simulate_imaginary_tournament,
    write_outputs,
)


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pyramidal-results", type=Path, required=True)
    parser.add_argument("--compositional-results", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="year_2024")
    parser.add_argument("--games", type=int, default=1000)
    parser.add_argument("--players-per-team", type=int, default=4)
    parser.add_argument("--tossups-per-game", type=int, default=20)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)
    inputs = load_tournament_inputs(
        args.pyramidal_results,
        args.compositional_results,
        args.data_dir,
        args.split,
    )
    players, games, summary = simulate_imaginary_tournament(
        inputs,
        games=args.games,
        players_per_team=args.players_per_team,
        tossups_per_game=args.tossups_per_game,
        seed=args.seed,
    )
    write_outputs(args.output_dir, players, games, summary)
    print("\nTop 20 by simulated PPG")
    print(
        players[["rank", "player_id", "games", "tossup_points", "ppg", "pp20"]]
        .head(20)
        .to_string(index=False, float_format=lambda value: f"{value:.3f}")
    )
    print(f"\nAggregate tournament PPG: {summary['aggregate_ppg']:.3f}")
    print(f"Wrote outputs to {args.output_dir}")


if __name__ == "__main__":
    main()
