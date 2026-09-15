#!/usr/bin/env python3
"""Run the repository's publication-readiness checks without training models.

The default check covers every test suite, Pyflakes, tracked shell syntax, and
whitespace errors in the working-tree diff. Dataset validation is opt-in
because it requires the ignored local dataset.
"""

from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]

# Pytest collects both TestCase classes and bare test functions in tests/.
# Family suites use unittest with their own discovery roots and PYTHONPATH.
TEST_SUITES = [
    ("root tests", ["-m", "pytest", "-q", "tests"], None),
    (
        "double-difficulty tests",
        [
            "-m",
            "unittest",
            "discover",
            "-s",
            "hazard_double_difficulty/tests",
            "-t",
            ".",
            "-v",
        ],
        None,
    ),
    # The correctness studies keep their tests beside the code they check, and
    # mix TestCase classes with bare test functions, so they need pytest.
    ("correctness study tests", ["-m", "pytest", "-q", "analysis/correctness"], None),
]


def _run(label: str, command: list[str], environment: dict[str, str]) -> None:
    """Run one check and stop immediately if it fails."""
    print(f"\n[{label}]", flush=True)
    print("+ " + shlex.join(command), flush=True)
    subprocess.run(command, cwd=REPO_ROOT, env=environment, check=True)


def _repository_files(pattern: str) -> list[str]:
    """Return tracked and visible untracked files matching a Git pathspec."""
    result = subprocess.run(
        [
            "git",
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "--",
            pattern,
        ],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    # A dirty tree may contain tracked deletions; tools should see only files
    # that are present in the working tree being checked. Code kept beside
    # results and in archive/ is a record, not maintained source.
    return [
        path
        for path in result.stdout.splitlines()
        if (REPO_ROOT / path).is_file()
        and not path.startswith(("results/", "archive/"))
    ]


def _check_shell_scripts(environment: dict[str, str]) -> None:
    """Parse every tracked or visible untracked shell script."""
    scripts = _repository_files("*.sh")
    print(f"\n[shell syntax: {len(scripts)} files]", flush=True)
    for script in scripts:
        subprocess.run(
            ["bash", "-n", script], cwd=REPO_ROOT, env=environment, check=True
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--include-data-validation",
        action="store_true",
        help="also validate the ignored local generated dataset",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-compirt")

    # Preserve the virtual-environment executable symlink so the environment's
    # packages remain available.
    python = sys.executable
    for label, arguments, pythonpath in TEST_SUITES:
        suite_environment = environment.copy()
        if pythonpath is not None:
            suite_environment["PYTHONPATH"] = pythonpath
        _run(label, [python, "-B", *arguments], suite_environment)

    python_files = _repository_files("*.py")
    _run(
        f"Pyflakes: {len(python_files)} files",
        [python, "-B", "-m", "pyflakes", *python_files],
        environment,
    )
    _check_shell_scripts(environment)
    # Preserve result logs byte-for-byte as experiment artifacts. Apply the
    # publication gate to editable source, documentation, and configuration.
    _run(
        "source/document working-tree whitespace",
        ["git", "diff", "--check", "--", ".", ":(exclude)results/**"],
        environment,
    )

    if args.include_data_validation:
        _run(
            "generated dataset validation",
            [python, "-B", "-m", "data_pipeline.validate"],
            environment,
        )

    print("\nRepository checks passed.", flush=True)


if __name__ == "__main__":
    main()
