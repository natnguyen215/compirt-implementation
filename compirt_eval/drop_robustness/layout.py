"""Stable result-layout helpers for random and targeted drop studies."""

from __future__ import annotations

from pathlib import Path


def fraction_label(fraction: float) -> str:
    return f"{fraction:g}"


def droplist_path(root: Path, fraction: float, replicate: int) -> Path:
    return (
        root
        / "droplists"
        / f"frac_{fraction_label(fraction)}"
        / f"rep_{replicate}.txt"
    )


def cell_dir(root: Path, model: str, fraction: float, replicate: int) -> Path:
    return (
        root
        / model
        / f"frac_{fraction_label(fraction)}"
        / f"rep_{replicate}"
        / "pyramidal"
    )


def full_dir(root: Path, model: str) -> Path:
    return root / model / "full" / "pyramidal"


def noise_dir(root: Path, model: str, seed: int) -> Path:
    return root / model / "noisefloor" / f"seed_{seed}" / "pyramidal"


def pair_label(direction: str, player_id: str) -> str:
    return f"{direction}_{player_id}"


def targeted_droplist_dir(root: Path, direction: str, player_id: str) -> Path:
    return root / "droplists" / pair_label(direction, player_id)


def count_list_path(
    root: Path, direction: str, player_id: str, count: int
) -> Path:
    return targeted_droplist_dir(root, direction, player_id) / f"n_{count}.txt"


def targeted_cell_dir(
    root: Path, model: str, direction: str, player_id: str, count: int
) -> Path:
    return root / model / pair_label(direction, player_id) / f"n_{count}" / "pyramidal"
