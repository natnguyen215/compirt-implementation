#!/usr/bin/env python3
"""Compare fitted conditional buzz accuracy with tournament PPG or PP20."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_eval.player_rankings import (
    ACTUAL_RANK_MODES,
    DEFAULT_DATABASE,
    evaluate_player_rankings,
)


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tournament", required=True, help="Tournament slug to compare")
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument(
        "--player-summary",
        type=Path,
        required=True,
        help="A fitted run's pyramidal player_buzz_summary.csv",
    )
    parser.add_argument(
        "--predictions",
        type=Path,
        required=True,
        help="The same run's pyramidal tossup_predictions.csv",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--actual-rank-mode",
        choices=ACTUAL_RANK_MODES,
        default="ppg",
        help="Real-ranking metric: public-standings PPG (default) or PP20",
    )
    parser.add_argument(
        "--min-games",
        type=int,
        default=1,
        help="Optional eligibility floor; public 2024 standings state no floor",
    )
    parser.add_argument(
        "--min-tuh",
        type=int,
        default=1,
        help="Optional eligibility floor; public 2024 standings state no floor",
    )
    parser.add_argument(
        "--min-game-tossups",
        type=int,
        default=1,
        help="Exclude incomplete games below this tossup count (default: include all)",
    )
    parser.add_argument("--actual-top", type=int, default=20)
    return parser.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)
    output_dir = evaluate_player_rankings(
        tournament=args.tournament,
        database=args.database,
        player_summary=args.player_summary,
        predictions=args.predictions,
        output_root=args.output_dir,
        actual_rank_mode=args.actual_rank_mode,
        min_games=args.min_games,
        min_tuh=args.min_tuh,
        min_game_tossups=args.min_game_tossups,
        actual_top=args.actual_top,
    )
    print(f"Wrote {output_dir / 'player_ranking_comparison.md'}")
    print(f"Wrote {output_dir / 'player_ranking_comparison.csv'}")


if __name__ == "__main__":
    main()
