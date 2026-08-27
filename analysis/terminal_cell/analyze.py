"""Measure the discrete-time team first-buzz hazard near the end of a tossup.

The pyramidal families model a tossup as a discrete-time survival process over
token positions and give every position the same kind of cell. That is not what
the data look like: positions '1 .. T_j - 1' are single tokens read aloud, but
position 'T_j' also absorbs the whole post-reading buzz window, so its cell
covers much more real time than any other. This script reports the empirical
team hazard indexed by tokens remaining, which is the evidence behind the
double-difficulty families' terminal-cell intercepts (see
'docs/terminal-cell.md').

Reproduce with::

    .venv/bin/python -m analysis.terminal_cell.analyze --split year_2024
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from compirt_data import build_tossup_observations, filter_tournament, load_hf_tables


OUTPUT_DIR = Path(__file__).resolve().parent / "data"


def event_frame(observations):
    """Collapse observation rows to one row per game-tossup event."""
    events = observations.groupby("event_id").agg(
        tossup_id=("tossup_id", "first"),
        tournament_id=("tournament_id", "first"),
        T_j=("T_j", "first"),
    )
    buzz = observations[observations["z"] == "BUZZ"].set_index("event_id")
    events["t_star"] = buzz["t_star"].reindex(events.index)
    events["dead"] = events["t_star"].isna()
    events["tokens_remaining"] = events["T_j"] - events["t_star"]
    return events


def hazard_by_tokens_remaining(events, horizon=15):
    """Return the team hazard for each of the last 'horizon' cells.

    A cell's risk set is every event that survived to it: the dead tossups plus
    the events whose buzz came at or after it.
    """
    rows = []
    for remaining in range(horizon):
        at_risk = events["dead"] | (events["tokens_remaining"] <= remaining)
        fired = ~events["dead"] & (events["tokens_remaining"] == remaining)
        rows.append(
            {
                "tokens_remaining": remaining,
                "at_risk": int(at_risk.sum()),
                "buzzes": int(fired.sum()),
                "team_hazard": float(fired.sum() / max(int(at_risk.sum()), 1)),
            }
        )
    return pd.DataFrame(rows)


def hazard_by_relative_position(events, bins=20):
    """Return the same hazard binned on the relative-position grid instead."""
    relative = np.where(
        events["dead"], np.inf, events["t_star"] / events["T_j"]
    )
    edges = np.linspace(0.0, 1.0, bins + 1)
    rows = []
    for low, high in zip(edges[:-1], edges[1:]):
        at_risk = int((relative >= low).sum())
        fired = int(((relative >= low) & (relative < high + 1e-9)).sum())
        rows.append(
            {
                "relative_position": float(high),
                "at_risk": at_risk,
                "buzzes": fired,
                "team_hazard": fired / max(at_risk, 1),
            }
        )
    return pd.DataFrame(rows)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--split", default="year_2024")
    parser.add_argument("--tournament")
    parser.add_argument("--horizon", type=int, default=15)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    args = parser.parse_args(argv)

    tables = filter_tournament(load_hf_tables(split=args.split), args.tournament)
    events = event_frame(build_tossup_observations(tables))
    args.output_dir.mkdir(parents=True, exist_ok=True)

    by_token = hazard_by_tokens_remaining(events, args.horizon)
    by_position = hazard_by_relative_position(events)
    by_token.to_csv(args.output_dir / "hazard_by_tokens_remaining.csv", index=False)
    by_position.to_csv(
        args.output_dir / "hazard_by_relative_position.csv", index=False
    )

    print(f"split={args.split} tournament={args.tournament or 'all'}")
    print(f"events={len(events):,}  dead rate={events['dead'].mean():.4f}")
    print("\nteam hazard by tokens remaining")
    print(by_token.to_string(index=False))
    final = by_token.iloc[0]["team_hazard"]
    penultimate = by_token.iloc[1]["team_hazard"]
    print(
        f"\nfinal cell hazard {final:.4f} is {final / max(penultimate, 1e-9):.1f}x "
        f"the cell one token earlier ({penultimate:.4f})"
    )


if __name__ == "__main__":
    main()
