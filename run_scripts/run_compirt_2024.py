#!/usr/bin/env python3
"""Full-2024 CompIRT experiment wrapper.

Python equivalent of ``run_compirt_2024.sh``. It validates the dataset,
checks model-ready data, then delegates to ``run_compirt.py`` with all-2024
defaults and both no-synergy and synergy variants enabled.
"""

from __future__ import annotations

import os
import shlex
import subprocess
from pathlib import Path


# This script lives in run_scripts/, so the repo root is one directory up.
REPO_ROOT = Path(__file__).resolve().parent.parent
PYTHON = REPO_ROOT / ".venv" / "bin" / "python"


def env_default(name: str, default: str) -> str:
    """Return an environment value, treating unset or empty as missing."""
    value = os.environ.get(name)
    return default if value in (None, "") else value


def env_default_unset_only(name: str, default: str) -> str:
    """Return an environment value, treating only unset as missing."""
    return os.environ.get(name, default)


def run(args: list[str]) -> None:
    """Print and run a child command."""
    print("+ " + shlex.join(args), flush=True)
    subprocess.run(args, cwd=REPO_ROOT, check=True)


def tournament_args(tournament: str) -> list[str]:
    return ["--tournament", tournament] if tournament else []


def main() -> None:
    os.environ["SPLIT"] = env_default("SPLIT", "year_2024")
    os.environ["TOURNAMENT"] = env_default_unset_only("TOURNAMENT", "")
    os.environ["ROOT"] = env_default("ROOT", "results/compirt/cuda-all-2024")
    os.environ["PYRAMIDAL_STEPS"] = env_default("PYRAMIDAL_STEPS", "5000")
    os.environ["BONUS_STEPS"] = env_default("BONUS_STEPS", "3000")
    os.environ["DIMENSIONS"] = env_default("DIMENSIONS", "5")
    os.environ["SYNERGY_DIMENSIONS"] = env_default("SYNERGY_DIMENSIONS", "3")
    os.environ["LR"] = env_default("LR", "0.005")
    os.environ["PREDICT_BUZZ_POSITIONS"] = env_default("PREDICT_BUZZ_POSITIONS", "1")
    os.environ["RUN_SYNERGY"] = "1"
    os.environ["SAVE_SYNERGY_DETAILS"] = env_default("SAVE_SYNERGY_DETAILS", "1")
    os.environ["MPLCONFIGDIR"] = env_default(
        "MPLCONFIGDIR", "/tmp/matplotlib-compirt"
    )

    split = os.environ["SPLIT"]
    tournament = os.environ["TOURNAMENT"]

    run([str(PYTHON), "-m", "data_pipeline.validate"])
    run(
        [
            str(PYTHON),
            "compirt_data.py",
            "--split",
            split,
            *tournament_args(tournament),
        ]
    )
    run([str(PYTHON), "run_scripts/run_compirt.py"])


if __name__ == "__main__":
    main()
