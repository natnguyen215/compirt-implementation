"""Read and reconstruct fitted pyramidal parameters from saved CSVs.

Stage 1 training ('train_pyramidal.py') can save tossup difficulty either
as a single scalar curve ('beta'/'gamma'/'mu' columns, one per tossup)
or, for vector-weighted fits, as one curve per skill dimension
('beta_1'/'gamma_1'/'mu_1', 'beta_2'/... alongside a matching
'alpha_1'/'alpha_2'/... discrimination vector or
'r_1'/'r_2'/... relevance vector). Polynomial-ridge fits instead save raw-power
coefficients as 'poly_coef_p<power>_d<dimension>' beside the same relevance
vector. Monotone Bernstein-polynomial fits instead save start/end difficulty,
positive total drop, and positive drop shares per dimension. Every other tossup
evaluation module needs to read whichever form is present and, for the
multidimensional case, combine the per-dimension curves into the single
weighted effective difficulty the model actually uses (Eq. 3-4). This
module is the shared place that knows how to do both.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

import numpy as np
import pandas as pd

from compirt_eval.common.figures import numeric_columns, vector_weight_columns


POLYNOMIAL_COEFFICIENT = re.compile(r"^poly_coef_p(\d+)_d(\d+)$")
MONOTONE_START = re.compile(r"^start_difficulty_d(\d+)$")
MONOTONE_END = re.compile(r"^end_difficulty_d(\d+)$")
MONOTONE_TOTAL_DROP = re.compile(r"^total_drop_d(\d+)$")
MONOTONE_DROP_SHARE = re.compile(r"^drop_share_(\d+)_d(\d+)$")
SCALAR_MONOTONE_DROP_SHARE = re.compile(r"^drop_share_(\d+)$")
SPLINE_KNOT_X = re.compile(r"^spline_knot_x_(\d+)$")
SPLINE_Y = re.compile(r"^spline_y_(\d+)_d(\d+)$")
PERCEPTION_SLICE_NAMES = ("first", "middle", "last")


def sliced_perception_columns(frame, parameter):
    """Return first/middle/last numbered player columns for one parameter."""
    groups = [
        numeric_columns(frame, f"{parameter}_{slice_name}_")
        for slice_name in PERCEPTION_SLICE_NAMES
    ]
    if not any(groups):
        return []
    dimensions = {len(columns) for columns in groups}
    if 0 in dimensions or len(dimensions) != 1:
        raise ValueError(
            f"Sliced {parameter} columns must be present and dimension-matched "
            "for first, middle, and last"
        )
    return groups


def perception_slice_indices(relative_position):
    """Map relative positions to first/middle/last slice indexes."""
    relative_position = np.asarray(relative_position, dtype=float)
    return np.where(
        relative_position < (1.0 / 3.0),
        0,
        np.where(relative_position < (2.0 / 3.0), 1, 2),
    )


def difficulty_curve(beta, gamma, mu, positions, link="sigmoid"):
    """Evaluate a saved pyramidal difficulty curve at relative positions.

    This NumPy replay of the model's Eq. 3 supports the standard sigmoid and
    opt-in tanh links recorded in a run's ``summary.json``.
    """
    argument = np.clip(gamma * (mu - positions), -60, 60)
    if link == "tanh":
        return beta * np.tanh(argument)
    if link != "sigmoid":
        raise ValueError(f"Unknown difficulty link {link!r}")
    return beta / (1.0 + np.exp(-argument))


def _parameter_columns(frame, parameter_prefix=""):
    """Return one saved difficulty family's columns in dimension order.

    ``parameter_prefix=""`` reads the canonical correctness curve. Double-
    difficulty runs additionally save the timing curve under ``"hazard_"``.
    Independent-relevance double-difficulty runs save hazard weights under
    ``hazard_r_*``. Older shared-relevance runs fall back to canonical weights.
    """
    prefixed_weights = (
        numeric_columns(frame, f"{parameter_prefix}r_") if parameter_prefix else []
    )
    return {
        "alpha": prefixed_weights or vector_weight_columns(frame),
        "beta": numeric_columns(frame, f"{parameter_prefix}beta_"),
        "bias": numeric_columns(frame, f"{parameter_prefix}bias_"),
        "gamma": numeric_columns(frame, f"{parameter_prefix}gamma_"),
        "mu": numeric_columns(frame, f"{parameter_prefix}mu_"),
        "polynomial": _polynomial_columns(frame, parameter_prefix),
        "monotone": _monotone_polynomial_columns(frame, parameter_prefix),
        "scalar_monotone": _scalar_monotone_columns(frame, parameter_prefix),
        "spline": _linear_spline_columns(frame, parameter_prefix),
    }


def _family_label(label, parameter_prefix):
    """Return a curve-family-local label or ``None`` for another family."""
    if not isinstance(label, str):
        return None
    if not parameter_prefix:
        return label
    if not label.startswith(parameter_prefix):
        return None
    return label.removeprefix(parameter_prefix)


def _scalar_monotone_columns(frame, parameter_prefix=""):
    """Return the scalar Bernstein schema."""
    labels = frame.index if isinstance(frame, pd.Series) else frame.columns
    result = {
        "start": f"{parameter_prefix}start_difficulty",
        "end": f"{parameter_prefix}end_difficulty",
        "total": f"{parameter_prefix}total_drop",
    }
    if not set(result.values()).issubset(labels):
        return {}
    shares = []
    for label in labels:
        local = _family_label(label, parameter_prefix)
        match = SCALAR_MONOTONE_DROP_SHARE.fullmatch(local or "")
        if match:
            shares.append((int(match.group(1)), label))
    shares.sort()
    if not shares or [number for number, _ in shares] != list(
        range(1, len(shares) + 1)
    ):
        raise ValueError("Scalar Bernstein drop shares must be contiguous from 1")
    result["shares"] = [label for _, label in shares]
    return result


def _linear_spline_columns(frame, parameter_prefix=""):
    """Return fixed knot positions and branch-local landmark columns."""
    labels = frame.index if isinstance(frame, pd.Series) else frame.columns
    positions = {}
    values: dict[int, dict[int, str]] = {}
    for label in labels:
        if isinstance(label, str):
            match = SPLINE_KNOT_X.fullmatch(label)
            if match:
                positions[int(match.group(1))] = label
        local = _family_label(label, parameter_prefix)
        match = SPLINE_Y.fullmatch(local or "")
        if match:
            knot, dimension = map(int, match.groups())
            values.setdefault(dimension, {})[knot] = label
    if not values:
        return {}
    knot_numbers = list(range(max(positions) + 1)) if positions else []
    dimensions = sorted(values)
    if (
        not knot_numbers
        or sorted(positions) != knot_numbers
        or dimensions != list(range(1, len(dimensions) + 1))
    ):
        raise ValueError("Spline knots and dimensions must be contiguous")
    for dimension in dimensions:
        if sorted(values[dimension]) != knot_numbers:
            raise ValueError("Spline landmark indices must match knot positions")
    return {
        "x": [positions[knot] for knot in knot_numbers],
        "y": [
            [values[dimension][knot] for knot in knot_numbers]
            for dimension in dimensions
        ],
    }


def _polynomial_columns(frame, parameter_prefix=""):
    """Return polynomial coefficient labels grouped by dimension then power.

    The saved schema is ``poly_coef_p<power>_d<dimension>``. Every dimension
    must contain the same contiguous powers beginning at zero.
    """
    labels = frame.index if isinstance(frame, pd.Series) else frame.columns
    grouped: dict[int, dict[int, str]] = {}
    for label in labels:
        local_label = _family_label(label, parameter_prefix)
        if local_label is None:
            continue
        match = POLYNOMIAL_COEFFICIENT.fullmatch(local_label)
        if match is None:
            continue
        power, dimension = map(int, match.groups())
        grouped.setdefault(dimension, {})[power] = label
    if not grouped:
        return []
    dimensions = sorted(grouped)
    if dimensions != list(range(1, len(dimensions) + 1)):
        raise ValueError("Polynomial coefficient dimensions must be contiguous from 1")
    expected_powers = list(range(max(grouped[dimensions[0]]) + 1))
    if len(expected_powers) < 2:
        raise ValueError("Polynomial coefficients must include an intercept and a slope")
    columns = []
    for dimension in dimensions:
        powers = sorted(grouped[dimension])
        if powers != expected_powers:
            raise ValueError(
                "Polynomial coefficient powers must be contiguous and match across dimensions"
            )
        columns.append([grouped[dimension][power] for power in powers])
    return columns


def _monotone_polynomial_columns(frame, parameter_prefix=""):
    """Return the interpretable monotone-polynomial column schema."""
    labels = frame.index if isinstance(frame, pd.Series) else frame.columns
    start, end, total = {}, {}, {}
    shares: dict[int, dict[int, str]] = {}
    for label in labels:
        local_label = _family_label(label, parameter_prefix)
        if local_label is None:
            continue
        match = MONOTONE_START.fullmatch(local_label)
        if match:
            start[int(match.group(1))] = label
            continue
        match = MONOTONE_END.fullmatch(local_label)
        if match:
            end[int(match.group(1))] = label
            continue
        match = MONOTONE_TOTAL_DROP.fullmatch(local_label)
        if match:
            total[int(match.group(1))] = label
            continue
        match = MONOTONE_DROP_SHARE.fullmatch(local_label)
        if match:
            share, dimension = map(int, match.groups())
            shares.setdefault(dimension, {})[share] = label
    if not (start or end or total or shares):
        return {}
    dimensions = sorted(start)
    expected_dimensions = list(range(1, len(dimensions) + 1))
    if (
        dimensions != expected_dimensions
        or sorted(end) != dimensions
        or sorted(total) != dimensions
        or sorted(shares) != dimensions
    ):
        raise ValueError(
            "Monotone polynomial start/end/drop dimensions must be contiguous and match"
        )
    expected_shares = list(range(1, max(shares[dimensions[0]]) + 1))
    if len(expected_shares) < 1:
        raise ValueError("Monotone polynomial must contain at least one drop share")
    share_columns = []
    for dimension in dimensions:
        if sorted(shares[dimension]) != expected_shares:
            raise ValueError(
                "Monotone polynomial drop shares must be contiguous and match "
                "across dimensions"
            )
        share_columns.append(
            [shares[dimension][share] for share in expected_shares]
        )
    return {
        "start": [start[dimension] for dimension in dimensions],
        "end": [end[dimension] for dimension in dimensions],
        "total": [total[dimension] for dimension in dimensions],
        "shares": share_columns,
    }


def _difficulty_parameter_columns(columns, link):
    """Return the learned curve-coordinate columns for one difficulty family."""
    name = "bias" if link == "biased_tanh" else "beta"
    return columns[name]


def _evaluate_difficulty_curve(parameter, gamma, mu, positions, link, scale=1.0):
    """Evaluate either the standard beta-link curve or the biased-tanh curve."""
    if link == "biased_tanh":
        return scale * np.tanh(gamma * (mu - positions) + parameter)
    return difficulty_curve(parameter, gamma, mu, positions, link)


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


def _validate_polynomial_dimensions(
    alpha_columns,
    polynomial_columns,
    theta_columns=None,
):
    """Validate relevance, optional skill, and polynomial dimension counts."""
    dimensions = {len(alpha_columns), len(polynomial_columns)}
    if theta_columns is not None:
        dimensions.add(len(theta_columns))
    if not alpha_columns or not polynomial_columns or len(dimensions) != 1:
        raise ValueError(
            "Saved theta/relevance and polynomial coefficient dimensions "
            "must be present and match"
        )


def _validate_monotone_dimensions(
    alpha_columns,
    monotone_columns,
    theta_columns=None,
):
    """Validate relevance, optional skill, and monotone curve dimensions."""
    if not monotone_columns:
        raise ValueError("Saved monotone polynomial parameters are missing")
    dimensions = {
        len(alpha_columns),
        len(monotone_columns["start"]),
        len(monotone_columns["end"]),
        len(monotone_columns["total"]),
        len(monotone_columns["shares"]),
    }
    if theta_columns is not None:
        dimensions.add(len(theta_columns))
    if not alpha_columns or len(dimensions) != 1:
        raise ValueError(
            "Saved theta/relevance and monotone polynomial dimensions "
            "must be present and match"
        )


def _validate_spline_dimensions(alpha_columns, spline_columns, theta_columns=None):
    """Validate relevance, optional skill, and linear-spline dimensions."""
    if not spline_columns:
        raise ValueError("Saved linear-spline parameters are missing")
    dimensions = {len(alpha_columns), len(spline_columns["y"])}
    if theta_columns is not None:
        dimensions.add(len(theta_columns))
    if not alpha_columns or len(dimensions) != 1:
        raise ValueError(
            "Saved theta/relevance and linear-spline dimensions must match"
        )


def _positive_log_series(frame, columns):
    """Return log10 values for positive-valued numbered columns."""
    return {
        f"log10_{column}": np.log10(frame.loc[frame[column] > 0, column])
        for column in columns
    }


def _multidim_difficulty_components(
    tossup, columns, positions, link="sigmoid", difficulty_scale=1.0
):
    """Return per-dimension difficulty curves and the alpha-weighted aggregate."""
    parameter_columns = _difficulty_parameter_columns(columns, link)
    parameter = tossup[parameter_columns].to_numpy(dtype=float)
    gamma = tossup[columns["gamma"]].to_numpy(dtype=float)
    mu = tossup[columns["mu"]].to_numpy(dtype=float)
    alpha = tossup[columns["alpha"]].to_numpy(dtype=float)
    positions = np.asarray(positions, dtype=float)
    per_dimension = _evaluate_difficulty_curve(
        parameter[:, None],
        gamma[:, None],
        mu[:, None],
        positions[None, :],
        link,
        difficulty_scale,
    )
    return per_dimension, alpha @ per_dimension


def _polynomial_difficulty_components(tossup, columns, positions):
    """Return raw-power polynomial curves and their relevance-weighted sum."""
    _validate_polynomial_dimensions(columns["alpha"], columns["polynomial"])
    coefficients = tossup[
        [label for dimension in columns["polynomial"] for label in dimension]
    ].to_numpy(dtype=float).reshape(
        len(columns["polynomial"]), len(columns["polynomial"][0])
    )
    positions = np.asarray(positions, dtype=float)
    powers = positions[None, :] ** np.arange(coefficients.shape[1])[:, None]
    per_dimension = coefficients @ powers
    alpha = tossup[columns["alpha"]].to_numpy(dtype=float)
    return per_dimension, alpha @ per_dimension


def _monotone_difficulty_components(tossup, columns, positions):
    """Return Bernstein curves and relevance-weighted effective difficulty."""
    monotone = columns["monotone"]
    _validate_monotone_dimensions(columns["alpha"], monotone)
    start = tossup[monotone["start"]].to_numpy(dtype=float)
    total = tossup[monotone["total"]].to_numpy(dtype=float)
    shares = tossup[
        [label for dimension in monotone["shares"] for label in dimension]
    ].to_numpy(dtype=float).reshape(
        len(monotone["shares"]), len(monotone["shares"][0])
    )
    controls = np.concatenate(
        [
            start[:, None],
            start[:, None] - np.cumsum(total[:, None] * shares, axis=1),
        ],
        axis=1,
    )
    degree = shares.shape[1]
    positions = np.asarray(positions, dtype=float)
    basis = np.stack(
        [
            math.comb(degree, power)
            * positions**power
            * (1.0 - positions) ** (degree - power)
            for power in range(degree + 1)
        ]
    )
    per_dimension = controls @ basis
    alpha = tossup[columns["alpha"]].to_numpy(dtype=float)
    return per_dimension, alpha @ per_dimension


def _scalar_monotone_difficulty(tossup, columns, positions):
    """Evaluate a scalar Bernstein curve."""
    monotone = columns["scalar_monotone"]
    start = float(tossup[monotone["start"]])
    total = float(tossup[monotone["total"]])
    shares = tossup[monotone["shares"]].to_numpy(dtype=float)
    controls = np.concatenate(([start], start - np.cumsum(total * shares)))
    degree = len(shares)
    positions = np.asarray(positions, dtype=float)
    basis = np.stack(
        [
            math.comb(degree, power)
            * positions**power
            * (1.0 - positions) ** (degree - power)
            for power in range(degree + 1)
        ]
    )
    return controls @ basis


def _linear_spline_difficulty_components(tossup, columns, positions):
    """Return per-dimension linear splines and their relevance-weighted sum."""
    spline = columns["spline"]
    _validate_spline_dimensions(columns["alpha"], spline)
    knot_x = tossup[spline["x"]].to_numpy(dtype=float)
    valid = np.isfinite(knot_x)
    knot_x = knot_x[valid]
    if len(knot_x) < 2:
        raise ValueError("A saved linear spline must contain at least two knots")
    per_dimension = np.asarray(
        [
            np.interp(
                np.asarray(positions, dtype=float),
                knot_x,
                tossup[dimension].to_numpy(dtype=float)[valid],
            )
            for dimension in spline["y"]
        ]
    )
    alpha = tossup[columns["alpha"]].to_numpy(dtype=float)
    return per_dimension, alpha @ per_dimension


def _saved_difficulty_components(
    tossup,
    positions,
    link="sigmoid",
    difficulty_scale=1.0,
    parameter_prefix="",
):
    """Return one family's per-dimension and effective saved curves."""
    columns = _parameter_columns(tossup, parameter_prefix)
    if columns["spline"]:
        return _linear_spline_difficulty_components(tossup, columns, positions)
    if columns["monotone"]:
        return _monotone_difficulty_components(tossup, columns, positions)
    if columns["polynomial"]:
        return _polynomial_difficulty_components(tossup, columns, positions)
    if (
        columns["alpha"]
        and _difficulty_parameter_columns(columns, link)
        and columns["gamma"]
        and columns["mu"]
    ):
        return _multidim_difficulty_components(
            tossup, columns, positions, link, difficulty_scale
        )
    return None


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
    if summary.get("model") == "multidim-tanhbias-competing-risks":
        return "biased_tanh"
    return summary.get("difficulty_link", "sigmoid")


def load_difficulty_scale(results_dir):
    """Return the fixed amplitude used by a biased-tanh training run."""
    path = Path(results_dir) / "summary.json"
    if not path.exists():
        return 1.0
    summary = json.loads(path.read_text(encoding="utf-8"))
    return float(summary.get("difficulty_scale", 1.0))


def load_terminal_intercepts(results_dir):
    """Return a run's '(correctness, hazard)' final-cell intercepts.

    The double-difficulty families give position 'T_j' its own intercept
    because that cell also covers the post-reading buzz window. The two scalars
    are global, so they are recorded in 'summary.json' rather than in
    'tossups.csv'. Runs without them (every other family, and fits made before
    the terminal cell existed) get '(0.0, 0.0)', which is a no-op.
    """
    path = Path(results_dir) / "summary.json"
    if not path.exists():
        return 0.0, 0.0
    summary = json.loads(path.read_text(encoding="utf-8"))
    return (
        float(summary.get("end_correct", 0.0)),
        float(summary.get("end_hazard", 0.0)),
    )


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


def _saved_difficulty_curve(
    tossup,
    positions,
    link="sigmoid",
    difficulty_scale=1.0,
    parameter_prefix="",
):
    """Return one saved scalar or weighted multidimensional difficulty curve."""
    scalar_columns = {
        name: f"{parameter_prefix}{name}" for name in ("beta", "gamma", "mu")
    }
    if set(scalar_columns.values()).issubset(tossup.index):
        return difficulty_curve(
            float(tossup[scalar_columns["beta"]]),
            float(tossup[scalar_columns["gamma"]]),
            float(tossup[scalar_columns["mu"]]),
            positions,
            link,
        )
    columns = _parameter_columns(tossup, parameter_prefix)
    if columns["scalar_monotone"]:
        return _scalar_monotone_difficulty(tossup, columns, positions)
    components = _saved_difficulty_components(
        tossup, positions, link, difficulty_scale, parameter_prefix
    )
    return None if components is None else components[1]


def _saved_effective_mu(tossup, parameter_prefix=""):
    """Return a scalar inflection marker for timing plots, if available."""
    scalar_mu = f"{parameter_prefix}mu"
    if scalar_mu in tossup.index:
        return float(tossup[scalar_mu])
    columns = _parameter_columns(tossup, parameter_prefix)
    # Polynomial and Bernstein curves have no transition-location parameter.
    if (
        columns["spline"]
        or columns["monotone"]
        or columns["polynomial"]
        or columns["scalar_monotone"]
    ):
        return None
    if not columns["alpha"] or len(columns["alpha"]) != len(columns["mu"]):
        return None
    alpha = np.abs(tossup[columns["alpha"]].to_numpy(dtype=float))
    mu = tossup[columns["mu"]].to_numpy(dtype=float)
    if alpha.sum() > 0:
        return float(np.dot(alpha / alpha.sum(), mu))
    return float(mu.mean())


def _has_saved_difficulty(frame, parameter_prefix=""):
    """Return whether ``frame`` contains a complete curve under ``parameter_prefix``."""
    labels = frame.index if isinstance(frame, pd.Series) else frame.columns
    scalar = {
        f"{parameter_prefix}beta",
        f"{parameter_prefix}gamma",
        f"{parameter_prefix}mu",
    }
    if scalar.issubset(labels):
        return True
    columns = _parameter_columns(frame, parameter_prefix)
    if (
        columns["spline"]
        or columns["monotone"]
        or columns["polynomial"]
        or columns["scalar_monotone"]
    ):
        return True
    return bool(
        columns["alpha"]
        and columns["beta"]
        and columns["gamma"]
        and columns["mu"]
    )


def _buzz_parameter_prefix(tossups):
    """Return the saved family that must drive buzz timing and survival."""
    return "hazard_" if _has_saved_difficulty(tossups, "hazard_") else ""


def _supports_first_buzz_reconstruction(players, tossups, parameter_prefix=None):
    """Return whether saved files have enough parameters for timing replay."""
    if parameter_prefix is None:
        parameter_prefix = _buzz_parameter_prefix(tossups)
    theta_columns = numeric_columns(players, "theta_")
    columns = _parameter_columns(tossups, parameter_prefix)
    alpha_columns = columns["alpha"]
    if not theta_columns or len(theta_columns) != len(alpha_columns):
        return False
    try:
        if columns["spline"]:
            _validate_spline_dimensions(
                alpha_columns, columns["spline"], theta_columns
            )
        elif columns["monotone"]:
            _validate_monotone_dimensions(
                alpha_columns, columns["monotone"], theta_columns
            )
        elif columns["polynomial"]:
            _validate_polynomial_dimensions(
                alpha_columns, columns["polynomial"], theta_columns
            )
        elif not columns["scalar_monotone"] and not {
            f"{parameter_prefix}beta",
            f"{parameter_prefix}gamma",
            f"{parameter_prefix}mu",
        }.issubset(tossups.columns):
            _validate_tossup_multidim_dimensions(
                alpha_columns, columns["beta"], columns["gamma"], columns["mu"]
            )
    except ValueError:
        return False
    return True
