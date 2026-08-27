"""Regenerate buzz_event_predictions.csv from saved Stage 1 posterior medians.

The script reconstructs E[t | a buzz occurs] from a run's saved 'players.csv'
and 'tossups.csv' posterior medians, then rewrites
'buzz_event_predictions.csv'. Re-run 'evaluate_compirt.py' afterwards to
refresh 'buzz_position_mae'. Use it when a saved prediction file contains
unconditional expected positions and retraining is unnecessary.

It supports every run the evaluator's timing replay supports: the baseline
scalar schema, the multidim/embedding vector schema (including the recorded
tanh link), and TF-IDF runs via their saved adjustment curves. Topic-weighted
runs save a different difficulty schema and are refused.

Usage (from the repo root):

    .venv/bin/python run_scripts/common/replay_buzz_positions.py \\
        --results-dir results/compirt/holdout/baseline/all-2024/holdout/pyramidal
    # add --output <path> to choose a separate destination
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_eval.scenario_a_tossups.parameters import (
    _supports_first_buzz_reconstruction,
    load_difficulty_adjustment_curves,
    load_difficulty_link,
    load_difficulty_scale,
)
from compirt_eval.scenario_a_tossups.timing import conditional_expected_buzz_position


def replay_run(results_dir: Path, output_path: Path) -> pd.DataFrame:
    """Rewrite one run's buzz-event predictions from its saved parameters."""
    players = pd.read_csv(
        results_dir / "players.csv", dtype={"player_id": str}
    ).set_index("player_id")
    tossups = pd.read_csv(
        results_dir / "tossups.csv", dtype={"tossup_id": str}
    ).set_index("tossup_id")
    predictions = pd.read_csv(
        results_dir / "tossup_predictions.csv",
        dtype={"player_id": str, "tossup_id": str},
    )
    if "c" not in players or not _supports_first_buzz_reconstruction(players, tossups):
        raise SystemExit(
            f"{results_dir} does not save the standard scalar or vector "
            "difficulty schema needed for timing replay (topic-weighted runs "
            "are not supported); refit instead."
        )
    adjustments = load_difficulty_adjustment_curves(results_dir)
    link = load_difficulty_link(results_dir)
    difficulty_scale = load_difficulty_scale(results_dir)

    rows = []
    skipped = 0
    for event_id, event in predictions.groupby("event_id"):
        buzz = event[event["z"] == "BUZZ"]
        if buzz.empty:
            # buzz_event_predictions.csv only ever contained buzzed events.
            continue
        if not set(event["player_id"]).issubset(players.index):
            skipped += 1
            continue
        rows.append(
            {
                "event_id": event_id,
                "observed_relative_position": float(
                    buzz["relative_position"].iloc[0]
                ),
                "predicted_relative_position": conditional_expected_buzz_position(
                    event,
                    players,
                    tossups,
                    adjustments,
                    link,
                    difficulty_scale=difficulty_scale,
                ),
            }
        )
    if skipped:
        print(f"Skipped {skipped} events with players missing from players.csv")

    frame = pd.DataFrame(rows)
    error = (
        frame["observed_relative_position"] - frame["predicted_relative_position"]
    ).abs()
    previous_path = results_dir / "buzz_event_predictions.csv"
    if previous_path.exists():
        previous = pd.read_csv(previous_path)
        previous_error = (
            previous["observed_relative_position"]
            - previous["predicted_relative_position"]
        ).abs()
        print(
            f"Previous file: {len(previous)} events, MAE {previous_error.mean():.4f}, "
            f"mean signed (pred - obs) "
            f"{(previous['predicted_relative_position'] - previous['observed_relative_position']).mean():+.4f}"
        )
    print(
        f"Replayed:      {len(frame)} events, MAE {error.mean():.4f}, "
        f"mean signed (pred - obs) "
        f"{(frame['predicted_relative_position'] - frame['observed_relative_position']).mean():+.4f}"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_path, index=False)
    print(f"Wrote {output_path}")
    return frame


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--results-dir",
        type=Path,
        required=True,
        help="A Stage 1 output directory (contains players.csv/tossups.csv)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Where to write; defaults to the run's buzz_event_predictions.csv",
    )
    args = parser.parse_args()
    output = args.output or args.results_dir / "buzz_event_predictions.csv"
    replay_run(args.results_dir, output)


if __name__ == "__main__":
    main()
