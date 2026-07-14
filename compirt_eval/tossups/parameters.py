"""Read and reconstruct fitted pyramidal parameters from saved CSVs.

Stage 1 training ('train_pyramidal.py') can save tossup difficulty either
as a single scalar curve ('beta'/'gamma'/'mu' columns, one per tossup)
or, for vector-weighted fits, as one curve per skill dimension
('beta_1'/'gamma_1'/'mu_1', 'beta_2'/... alongside a matching
'alpha_1'/'alpha_2'/... discrimination vector or embedding-run
'r_1'/'r_2'/... relevance vector). Every other tossup
evaluation module needs to read whichever form is present and, for the
multidimensional case, combine the per-dimension curves into the single
weighted effective difficulty the model actually uses (Eq. 3-4). This
module is the shared place that knows how to do both.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from compirt_eval.figures import numeric_columns
from compirt_eval.metrics import difficulty_curve


def _numbered_labels(frame, prefix):
    """Return numbered labels from either a DataFrame's columns or a Series index."""
    labels = frame.index if isinstance(frame, pd.Series) else frame.columns
    return sorted(
        (
            label
            for label in labels
            if isinstance(label, str)
            and label.startswith(prefix)
            and label.removeprefix(prefix).isdigit()
        ),
        key=lambda label: int(label.removeprefix(prefix)),
    )


def _discrimination_columns(frame):
    """Return vector-weight columns, accepting either alpha_* or embedding r_*."""
    alpha_columns = _numbered_labels(frame, "alpha_")
    relevance_columns = _numbered_labels(frame, "r_")
    if alpha_columns and relevance_columns:
        raise ValueError("Saved vector weights must use either alpha_* or r_*, not both")
    return alpha_columns or relevance_columns


def _vector_weight_name(columns):
    """Return the saved coordinate name for labels and derived norm columns."""
    if columns and columns[0].startswith("r_"):
        return "r"
    return "alpha"


def _parameter_columns(frame):
    """Return saved numbered tossup parameter columns in dimension order."""
    return {
        "alpha": _discrimination_columns(frame),
        "beta": _numbered_labels(frame, "beta_"),
        "gamma": _numbered_labels(frame, "gamma_"),
        "mu": _numbered_labels(frame, "mu_"),
    }


def _validate_multidim_dimensions(
    theta_columns, alpha_columns, beta_columns, gamma_columns, mu_columns
):
    """Validate that saved multidimensional-difficulty columns line up."""
    dimensions = {
        len(theta_columns),
        len(alpha_columns),
        len(beta_columns),
        len(gamma_columns),
        len(mu_columns),
    }
    if not theta_columns or len(dimensions) != 1:
        raise ValueError(
            "Saved theta, alpha, beta, gamma, and mu dimensions must be present and match"
        )


def _validate_tossup_multidim_dimensions(
    alpha_columns,
    beta_columns,
    gamma_columns,
    mu_columns,
):
    """Validate vector tossup parameters when player theta is not needed."""
    dimensions = {
        len(alpha_columns),
        len(beta_columns),
        len(gamma_columns),
        len(mu_columns),
    }
    if not alpha_columns or len(dimensions) != 1:
        raise ValueError(
            "Saved alpha, beta, gamma, and mu dimensions must be present and match"
        )


def _positive_log_series(frame, columns):
    """Return log10 values for positive-valued numbered columns."""
    series = {}
    for column in columns:
        positive = frame.loc[frame[column] > 0, column]
        series[f"log10_{column}"] = np.log10(positive)
    return series


def _multidim_effective_difficulty(tossup, positions, link="sigmoid"):
    """Return sum_k alpha_jk * d_jk(t) from saved vector difficulty columns."""
    columns = _parameter_columns(tossup)
    _validate_tossup_multidim_dimensions(
        columns["alpha"],
        columns["beta"],
        columns["gamma"],
        columns["mu"],
    )
    alpha = tossup[columns["alpha"]].to_numpy(dtype=float)
    per_dimension = difficulty_curve(
        tossup[columns["beta"]].to_numpy(dtype=float)[:, None],
        tossup[columns["gamma"]].to_numpy(dtype=float)[:, None],
        tossup[columns["mu"]].to_numpy(dtype=float)[:, None],
        np.asarray(positions, dtype=float)[None, :],
        link,
    )
    return alpha @ per_dimension


def _multidim_difficulty_components(tossup, columns, positions, link="sigmoid"):
    """Return per-dimension difficulty curves and the alpha-weighted aggregate."""
    beta = tossup[columns["beta"]].to_numpy(dtype=float)
    gamma = tossup[columns["gamma"]].to_numpy(dtype=float)
    mu = tossup[columns["mu"]].to_numpy(dtype=float)
    alpha = tossup[columns["alpha"]].to_numpy(dtype=float)
    positions = np.asarray(positions, dtype=float)
    per_dimension = difficulty_curve(
        beta[:, None],
        gamma[:, None],
        mu[:, None],
        positions[None, :],
        link,
    )
    return per_dimension, alpha @ per_dimension


def load_difficulty_link(results_dir):
    """Return the difficulty-curve link a training run used.

    Trainers that support the opt-in tanh link record 'difficulty_link' in
    their 'summary.json'; every run without the key (all older runs and every
    other family) used the sigmoid link.
    """
    path = Path(results_dir) / "summary.json"
    if not path.exists():
        return "sigmoid"
    summary = json.loads(path.read_text(encoding="utf-8"))
    return summary.get("difficulty_link", "sigmoid")


def load_difficulty_adjustment_curves(results_dir):
    """Load optional saved effective-difficulty adjustments, if the run has them.

    TF-IDF cumulative-difficulty runs save 'tfidf_adjustment_curves.csv': one row
    per tossup with the signed text-conditioned difficulty delta sampled on an
    evenly spaced relative-position grid. The evaluator adds that delta to the
    base curve to draw 'd'_j(r) = d_j(r) + delta_j(r)' without recomputing text
    features. Returns 'None' when the run has no such file, otherwise
    '(values_by_tossup, grid)'.
    """
    path = Path(results_dir) / "tfidf_adjustment_curves.csv"
    if not path.exists():
        return None
    frame = pd.read_csv(path, dtype={"tossup_id": str}).set_index("tossup_id")
    columns = [
        column for column in frame.columns if column.startswith("adjustment_")
    ]
    if len(columns) < 2:
        return None
    grid = np.linspace(0.0, 1.0, len(columns))
    values = {
        tossup_id: row[columns].to_numpy(dtype=float)
        for tossup_id, row in frame.iterrows()
    }
    return values, grid


def difficulty_adjustment_at(adjustments, tossup_id, positions):
    """Interpolate one tossup's saved adjustment onto arbitrary positions."""
    if adjustments is None:
        return None
    values, grid = adjustments
    curve = values.get(str(tossup_id))
    if curve is None:
        return None
    return np.interp(np.asarray(positions, dtype=float), grid, curve)


def _saved_difficulty_curve(tossup, positions, link="sigmoid"):
    """Return scalar or alpha-weighted multidimensional difficulty, if present."""
    if {"beta", "gamma", "mu"}.issubset(tossup.index):
        return difficulty_curve(
            float(tossup["beta"]),
            float(tossup["gamma"]),
            float(tossup["mu"]),
            positions,
            link,
        )
    columns = _parameter_columns(tossup)
    if all(columns[name] for name in ("alpha", "beta", "gamma", "mu")):
        return _multidim_effective_difficulty(tossup, positions, link)
    return None


def _saved_effective_mu(tossup):
    """Return a scalar inflection marker for timing plots, if available."""
    if "mu" in tossup.index:
        return float(tossup["mu"])
    columns = _parameter_columns(tossup)
    if not columns["alpha"] or len(columns["alpha"]) != len(columns["mu"]):
        return None
    alpha = np.abs(tossup[columns["alpha"]].to_numpy(dtype=float))
    mu = tossup[columns["mu"]].to_numpy(dtype=float)
    if alpha.sum() > 0:
        return float(np.dot(alpha / alpha.sum(), mu))
    return float(mu.mean())


def _supports_first_buzz_reconstruction(players, tossups):
    """Return whether saved files have enough parameters for timing replay."""
    theta_columns = numeric_columns(players, "theta_")
    columns = _parameter_columns(tossups)
    alpha_columns = columns["alpha"]
    if not theta_columns or len(theta_columns) != len(alpha_columns):
        return False
    if {"beta", "gamma", "mu"}.issubset(tossups.columns):
        return True
    try:
        _validate_tossup_multidim_dimensions(
            alpha_columns,
            columns["beta"],
            columns["gamma"],
            columns["mu"],
        )
    except ValueError:
        return False
    return True
