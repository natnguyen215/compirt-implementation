"""Output-path helpers for evaluation reports."""

from __future__ import annotations

from pathlib import Path


GRAPHS_DIR = "graphs"
CSVS_DIR = "csvs"

# Themed subdirectories the standard evaluators sort their figures into.
GRAPH_GROUPS = ("tossup", "bonus", "match", "parameters", "diagnostics")


def evaluation_output_dirs(output_dir: Path) -> tuple[Path, Path]:
    """Return the graph and CSV subdirectories for an evaluation output root."""
    graphs_dir = output_dir / GRAPHS_DIR
    csvs_dir = output_dir / CSVS_DIR
    graphs_dir.mkdir(parents=True, exist_ok=True)
    csvs_dir.mkdir(parents=True, exist_ok=True)
    return graphs_dir, csvs_dir


def metrics_path(evaluation_dir: Path, filename: str) -> Path:
    """Return the metrics CSV path from a nested or flat evaluation layout."""
    nested = evaluation_dir / CSVS_DIR / filename
    if nested.exists():
        return nested
    return evaluation_dir / filename


def graph_path(output_dir: Path, filename: str, group: str | None = None) -> Path:
    """Return a graph artifact path under 'graphs/', optionally themed.

    The standard evaluators pass a 'GRAPH_GROUPS' name so a run's figures land
    in 'graphs/<group>/' sorted by scenario. Standalone runners (ablation
    sweeps, drop robustness, Scenario C) omit it and keep the flat 'graphs/'
    layout their artifact maps document.
    """
    if group is not None and group not in GRAPH_GROUPS:
        raise ValueError(f"unknown graph group: {group!r}")
    base = output_dir if output_dir.name == GRAPHS_DIR else output_dir / GRAPHS_DIR
    path = base / group / filename if group else base / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def csv_path(output_dir: Path, filename: str) -> Path:
    """Return a CSV artifact path under 'csvs/'."""
    if output_dir.name == CSVS_DIR:
        path = output_dir / filename
    else:
        path = output_dir / CSVS_DIR / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
