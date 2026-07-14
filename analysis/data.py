"""Shared loaders for the baseline-ablation sweep's saved predictions.

Everything in `analysis/` reads the CSVs the sweep already wrote — nothing here
retrains. Frames are cached per process because several modules re-read the
same large prediction files.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

DEFAULT_SWEEP = Path("results/compirt/holdout/baseline-ablation")
DEFAULT_OUTPUT = Path("results/analysis")
# The sweep stores the no-synergy bonus branch under syn_0; its Stage-2 tables
# are the ones carrying `category`.
BONUS_BRANCH = "syn_0"

# The source data's category vocabulary is dirty; canonicalize before slicing,
# or the variants split their categories' sample.
CATEGORY_CANON = {
    "Pop Culture": "Popular Culture",
    "Any History": "History",
    "Painting &amp; Sculpture": "Fine Arts",
    "Painting/Sculpture": "Fine Arts",
    "Geography/Current Events": "Geography",
    "Current Events/Geography": "Current Events",
}

_CACHE: dict[tuple, pd.DataFrame] = {}


def base_parser(description):
    """Argument parser with the flags every analysis module shares."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--sweep-dir", type=Path, default=DEFAULT_SWEEP)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser


def holdout_dir(sweep_dir, dimension):
    return sweep_dir / f"dim_{dimension}" / "holdout"


def train_dir(sweep_dir, dimension):
    """The 2024 training leg — a disjoint season's fit, used as an exogenous
    source of player covariates."""
    return sweep_dir / f"dim_{dimension}" / "train"


def bonus_dir(sweep_dir, dimension):
    return holdout_dir(sweep_dir, dimension) / BONUS_BRANCH / "compositional"


def _read(path):
    """Read a CSV once per process; these files are large and re-read constantly."""
    key = str(path)
    if key not in _CACHE:
        _CACHE[key] = pd.read_csv(path)
    return _CACHE[key]


def discover_dimensions(sweep_dir):
    """Return the sweep's skill dimensions, ascending, that have holdout output."""
    dimensions = []
    for path in sorted(sweep_dir.glob("dim_*")):
        if (path / "holdout" / "pyramidal" / "tossup_predictions.csv").exists():
            dimensions.append(int(path.name.removeprefix("dim_")))
    return sorted(dimensions)


def require_dimensions(sweep_dir):
    dimensions = discover_dimensions(sweep_dir)
    if not dimensions:
        raise SystemExit(f"no dim_*/holdout tossup predictions under {sweep_dir}")
    assert_observed_columns_shared(sweep_dir, dimensions)
    return dimensions


def load_events(sweep_dir, dimension, leg="holdout"):
    """Every scored row for one dimension: buzzes, censored teammates, dead tossups."""
    base = holdout_dir(sweep_dir, dimension) if leg == "holdout" else train_dir(sweep_dir, dimension)
    return _read(base / "pyramidal" / "tossup_predictions.csv")


def load_buzzes(sweep_dir, dimension, leg="holdout"):
    """One leg's first-buzz rows, with buzz-position predictions attached.

    Only `z == "BUZZ"` rows carry an observed correctness outcome — the same
    filter `compirt_eval.tossups.evaluate_tossups` applies. The buzz-position
    predictions live in a separate file keyed by `event_id`.
    """
    key = ("buzzes", str(sweep_dir), dimension, leg)
    if key in _CACHE:
        return _CACHE[key]

    frame = load_events(sweep_dir, dimension, leg)
    buzzes = frame[frame["z"] == "BUZZ"]

    base = holdout_dir(sweep_dir, dimension) if leg == "holdout" else train_dir(sweep_dir, dimension)
    positions = base / "pyramidal" / "buzz_event_predictions.csv"
    if positions.exists():
        buzzes = buzzes.merge(_read(positions), on="event_id", how="left")

    _CACHE[key] = buzzes
    return buzzes


def load_players(sweep_dir, dimension, leg="holdout"):
    base = holdout_dir(sweep_dir, dimension) if leg == "holdout" else train_dir(sweep_dir, dimension)
    return _read(base / "pyramidal" / "players.csv")


def load_tossup_params(sweep_dir, dimension):
    return _read(holdout_dir(sweep_dir, dimension) / "pyramidal" / "tossups.csv")


def load_bonus_parts(sweep_dir, dimension):
    parts = _read(bonus_dir(sweep_dir, dimension) / "bonus_part_predictions.csv").copy()
    parts["category"] = parts["category"].replace(CATEGORY_CANON)
    return parts


def load_bonus_teams(sweep_dir, dimension):
    return _read(bonus_dir(sweep_dir, dimension) / "team_predictions.csv")


def load_tossup_categories(hf_root=Path("data/hf/quizbowl-irt")):
    """tossup_id -> canonical category, from the local HuggingFace tables.

    The tossup prediction CSVs carry only `tier`/`tournament_id`; category lives
    in the `tossups` table.
    """
    from datasets import load_from_disk

    tossups = load_from_disk(str(hf_root / "tossups"))["all"].to_pandas()
    categories = tossups.set_index("tossup_id")["category"].replace(CATEGORY_CANON)
    return categories.replace("", pd.NA)


def numbered_columns(frame, prefix):
    """Return `prefix_1..prefix_K` in ascending K order (the saved-CSV schema).

    The digit check matters: `players.csv` also carries `theta_norm`, which
    shares the `theta_` prefix but is a summary, not a coordinate.
    """
    columns = [
        c for c in frame.columns if c.startswith(f"{prefix}_") and c.rsplit("_", 1)[1].isdigit()
    ]
    return sorted(columns, key=lambda c: int(c.rsplit("_", 1)[1]))


def assert_observed_columns_shared(sweep_dir, dimensions):
    """The sweep's dimensions must describe the same held-out events.

    Difficulty buckets, fold assignments and category joins are derived once and
    applied to every dimension, which is only sound if the *observed* columns
    are identical across dimensions (the predictions of course differ).
    """
    reference = load_events(sweep_dir, dimensions[0])
    for dimension in dimensions[1:]:
        other = load_events(sweep_dir, dimension)
        for column in ("event_id", "y", "relative_position", "tossup_id", "player_id"):
            if not reference[column].equals(other[column]):
                raise SystemExit(
                    f"dim_{dimensions[0]} and dim_{dimension} disagree on observed column "
                    f"'{column}'; every shared slice definition would be misaligned"
                )
