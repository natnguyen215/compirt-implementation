#!/usr/bin/env python3
"""Full-2024 CompIRT experiment wrapper.

'run_compirt_2024.sh' is a thin wrapper around this script. It validates the
dataset, checks model-ready data, then delegates to 'run_compirt.py' with
all-2024 defaults and both no-synergy and synergy variants enabled.
"""

from __future__ import annotations

import os
import shlex
import sys
from pathlib import Path

# Add the repository root to sys.path for direct script invocation.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from utils.run_logging import (
    env_default,
    env_unset_only,
    format_run_log_header,
    resolve_result_root,
    run_logged,
    tee_run_output,
    warn_env_knob_typos,
)

PYTHON = Path(os.environ.get("PYTHON", str(REPO_ROOT / ".venv" / "bin" / "python")))


def run(args: list[str]) -> None:
    """Print and run a child command."""
    print("+ " + shlex.join(args), flush=True)
    run_logged(args, cwd=REPO_ROOT)


def tournament_args(tournament: str) -> list[str]:
    return ["--tournament", tournament] if tournament else []


def main() -> None:
    """Apply full-2024 defaults, validate the data, and launch CompIRT."""
    # Resolve and export one configuration for validation and all model stages.
    os.environ["SPLIT"] = env_default("SPLIT", "year_2024")
    os.environ["TOURNAMENT"] = env_unset_only("TOURNAMENT", "")
    os.environ["ROOT"] = resolve_result_root(
        env_default("ROOT", "results/compirt/in_sample/baseline/cuda-all-2024"),
        "in_sample",
    )
    os.environ["PYRAMIDAL_STEPS"] = env_default("PYRAMIDAL_STEPS", "5000")
    os.environ["BONUS_STEPS"] = env_default("BONUS_STEPS", "3000")
    os.environ["DIMENSIONS"] = env_default("DIMENSIONS", "5")
    os.environ["SYNERGY_DIMENSIONS"] = env_default("SYNERGY_DIMENSIONS", "3")
    os.environ["LR"] = env_default("LR", "0.005")
    os.environ["SEED"] = env_default("SEED", "42")
    os.environ["RUN_SYNERGY"] = "1"
    os.environ["SAVE_SYNERGY_DETAILS"] = env_default("SAVE_SYNERGY_DETAILS", "1")
    os.environ["MPLCONFIGDIR"] = env_default(
        "MPLCONFIGDIR", "/tmp/matplotlib-compirt"
    )
    warn_env_knob_typos()
    # Capture validation and training output in the same run log.
    if os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(Path(os.environ["ROOT"]) / "run.log")

    split = os.environ["SPLIT"]
    tournament = os.environ["TOURNAMENT"]
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/common/run_compirt_2024.py",
                "ROOT": os.environ["ROOT"],
                "MODEL": "baseline",
                "SPLIT": split,
                "TOURNAMENT": tournament or "<all>",
                "DEVICE": "cuda",
                "GPU": os.environ.get("GPU", "0"),
                "DIMENSIONS": os.environ["DIMENSIONS"],
                "PYRAMIDAL_STEPS": os.environ["PYRAMIDAL_STEPS"],
                "BONUS_STEPS": os.environ["BONUS_STEPS"],
                "LR": os.environ["LR"],
                "SEED": os.environ["SEED"],
                "RUN_SYNERGY": os.environ["RUN_SYNERGY"],
                "SYNERGY_DIMENSIONS": os.environ["SYNERGY_DIMENSIONS"],
                "SAVE_SYNERGY_DETAILS": os.environ["SAVE_SYNERGY_DETAILS"],
                "MPLCONFIGDIR": os.environ["MPLCONFIGDIR"],
                "PYTHON": PYTHON,
            }
        ),
        flush=True,
    )

    # Validate the linked dataset and model-ready observations before fitting.
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
    # Delegate the actual two-stage fit and evaluation with the exported settings.
    run([str(PYTHON), "run_scripts/common/run_compirt.py"])


if __name__ == "__main__":
    main()
