#!/usr/bin/env python3
"""Run CompIRT on the final 20 percent of rounds in every tournament.

This is a thin configuration layer over ``run_compirt_holdout.py``.  It trains
on all earlier rounds in ``BASE_SPLIT`` and sends all games from each
tournament's final ``ROUND_HOLDOUT_FRACTION`` of numbered rounds to the existing
transductive held-out pass.

Environment variables:

* ``BASE_SPLIT`` (default ``all``)
* ``ROUND_HOLDOUT_FRACTION`` (default ``0.2``)
* every variable accepted by ``run_compirt_holdout.py`` (``MODEL``, ``ROOT``,
  ``TOURNAMENT``, training settings, and so on)

``TRAIN_SPLIT`` and ``TEST_SPLIT`` are derived by this wrapper and may not be
set directly.  This preserves whole-round boundaries and makes the split
reproducible across every model family that uses the shared data loader.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# Support both ``python -m`` and direct ``python run_scripts/...py`` execution.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from holdout.round_splits import round_holdout_split_name
from run_scripts.common import run_compirt_holdout


def configure_round_holdout() -> tuple[str, str]:
    """Set the existing runner's train/test split names and return them."""
    if "TRAIN_SPLIT" in os.environ or "TEST_SPLIT" in os.environ:
        raise SystemExit(
            "run_compirt_round_holdout derives TRAIN_SPLIT and TEST_SPLIT; "
            "use BASE_SPLIT and ROUND_HOLDOUT_FRACTION instead"
        )
    base_split = os.environ.get("BASE_SPLIT", "all")
    raw_fraction = os.environ.get("ROUND_HOLDOUT_FRACTION", "0.2")
    try:
        fraction = float(raw_fraction)
        train_split = round_holdout_split_name(base_split, "train", fraction)
        test_split = round_holdout_split_name(base_split, "test", fraction)
    except ValueError as error:
        raise SystemExit(str(error)) from error

    os.environ["TRAIN_SPLIT"] = train_split
    os.environ["TEST_SPLIT"] = test_split
    model = os.environ.get("MODEL", "baseline")
    os.environ.setdefault(
        "ROOT", f"results/compirt/holdout/common/final-round-fraction/{model}"
    )
    return train_split, test_split


def main() -> None:
    configure_round_holdout()
    run_compirt_holdout.main()


if __name__ == "__main__":
    main()
