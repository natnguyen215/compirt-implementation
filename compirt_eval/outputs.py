"""Output-path helpers for evaluation reports."""

from __future__ import annotations

from pathlib import Path


GRAPHS_DIR = "graphs"
CSVS_DIR = "csvs"


def evaluation_output_dirs(output_dir: Path) -> tuple[Path, Path]:
    """Return the graph and CSV subdirectories for an evaluation output root."""
    graphs_dir = output_dir / GRAPHS_DIR
    csvs_dir = output_dir / CSVS_DIR
    graphs_dir.mkdir(parents=True, exist_ok=True)
    csvs_dir.mkdir(parents=True, exist_ok=True)
    return graphs_dir, csvs_dir


def metrics_path(evaluation_dir: Path, filename: str) -> Path:
    """Return the preferred metrics CSV path, falling back to the legacy flat file."""
    nested = evaluation_dir / CSVS_DIR / filename
    if nested.exists():
        return nested
    return evaluation_dir / filename


def graph_path(output_dir: Path, filename: str) -> Path:
    """Return a graph artifact path under 'graphs/'."""
    if output_dir.name == GRAPHS_DIR:
        path = output_dir / filename
    else:
        path = output_dir / GRAPHS_DIR / filename
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
