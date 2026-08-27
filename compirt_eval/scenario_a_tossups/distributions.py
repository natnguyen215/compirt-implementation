"""Plot fitted pyramidal player/tossup parameter distributions.

Renders density panels for every fitted Stage 1 parameter (player skill
'theta'/confidence 'c', tossup discrimination 'alpha'/difficulty 'beta' or
biased-tanh 'bias', plus 'gamma'/'mu', polynomial raw-power coefficients, or
monotone-polynomial start/end/drop parameters) and a percentile-band view of
the learned difficulty curves themselves, and writes a matching numeric
summary CSV.
'pyramidal_parameter_distribution_plots' is the entry point, called from
'evaluate_tossups'.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.common.figures import (
    density_panel_spec,
    distribution_dashboard,
    distribution_summary,
    numeric_columns,
    vector_weight_name,
)
from compirt_eval.common.report_paths import csv_path, graph_path
from compirt_eval.scenario_a_tossups.parameters import (
    PERCEPTION_SLICE_NAMES,
    _has_saved_difficulty,
    _parameter_columns,
    _positive_log_series,
    _saved_difficulty_curve,
    difficulty_adjustment_at,
    load_difficulty_adjustment_curves,
    load_difficulty_link,
    load_difficulty_scale,
    sliced_perception_columns,
)


def _pyramidal_player_panels(players, theta_columns):
    """Build density panels for skill and either threshold or perception."""
    panels = []
    if "c" in players:
        panels.append(
            density_panel_spec(
                players["c"], "Confidence threshold", "c", zero_line=True
            )
        )
    if theta_columns:
        panels.append(
            density_panel_spec(
                players[theta_columns], "Skill coordinates", "theta", zero_line=True
            )
        )
    alpha_columns = numeric_columns(players, "alpha_")
    beta_columns = numeric_columns(players, "beta_")
    sliced_alpha_columns = sliced_perception_columns(players, "alpha")
    sliced_beta_columns = sliced_perception_columns(players, "beta")
    if alpha_columns:
        panels.append(
            density_panel_spec(
                players[alpha_columns],
                "Difficulty perception multipliers",
                "alpha",
                zero_line=True,
            )
        )
    if beta_columns:
        panels.append(
            density_panel_spec(
                players[beta_columns],
                "Buzz intercepts",
                "beta",
                zero_line=True,
            )
        )
    for slice_name, slice_alpha, slice_beta in zip(
        PERCEPTION_SLICE_NAMES,
        sliced_alpha_columns,
        sliced_beta_columns,
    ):
        panels.append(
            density_panel_spec(
                players[slice_alpha],
                f"Difficulty perception multipliers ({slice_name} third)",
                f"alpha_{slice_name}",
                zero_line=True,
            )
        )
        panels.append(
            density_panel_spec(
                players[slice_beta],
                f"Buzz intercepts ({slice_name} third)",
                f"beta_{slice_name}",
                zero_line=True,
            )
        )
    if "alpha" in players:
        panels.append(
            density_panel_spec(
                players["alpha"],
                "Correctness-logit buzz multipliers",
                "alpha",
                zero_line=True,
            )
        )
    if "beta" in players:
        panels.append(
            density_panel_spec(
                players["beta"],
                "Buzz-logit intercepts",
                "beta",
                zero_line=True,
            )
        )
    if "theta_norm" in players:
        panels.append(
            density_panel_spec(
                players["theta_norm"],
                "Skill magnitude",
                "theta norm",
                bounds=(0, None),
            )
        )
    return panels


def _pyramidal_tossup_panels(
    tossups,
    alpha_columns,
    parameter_prefix="",
    include_weights=True,
):
    """Build density panels for fitted tossup difficulty and weight parameters."""
    panels = []
    columns = _parameter_columns(tossups, parameter_prefix)
    title_prefix = "Hazard " if parameter_prefix else ""
    weight_name = vector_weight_name(alpha_columns)
    norm_column = f"{weight_name}_norm"
    for column, title, xlabel, zero_line in (
        (f"{parameter_prefix}beta", "Difficulty amplitude", "beta", True),
        (
            f"{parameter_prefix}mu",
            "Difficulty transition location",
            "relative position mu",
            False,
        ),
    ):
        if column in tossups:
            panels.append(
                density_panel_spec(
                    tossups[column],
                    f"{title_prefix}{title}",
                    xlabel,
                    zero_line=zero_line,
                    bounds=(0, 1) if column == f"{parameter_prefix}mu" else None,
                )
            )
    scalar_gamma = f"{parameter_prefix}gamma"
    if scalar_gamma in tossups:
        # gamma is positive and heavy-tailed, so plot it on a log10 axis between
        # the amplitude and location panels.
        positive_gamma = tossups.loc[tossups[scalar_gamma] > 0, scalar_gamma]
        panels.insert(
            1,
            density_panel_spec(
                {f"log10_{scalar_gamma}": np.log10(positive_gamma)},
                f"{title_prefix}difficulty transition sharpness",
                "log10(gamma)",
                zero_line=True,
            ),
        )
    for key, title, xlabel, zero_line, bounds in (
        ("beta", "difficulty amplitudes", "beta", True, None),
        ("bias", "biased-tanh difficulty shifts", "bias", True, None),
        ("gamma", "difficulty transition sharpness", "log10(gamma)", True, None),
        ("mu", "difficulty transition locations", "relative position mu", False, (0, 1)),
    ):
        if not columns[key]:
            continue
        # Per-dimension gamma is positive and heavy-tailed, so it too goes on a
        # log10 axis rather than plotting raw.
        series = (
            _positive_log_series(tossups, columns["gamma"])
            if key == "gamma"
            else tossups[columns[key]]
        )
        panels.append(
            density_panel_spec(
                series,
                f"{title_prefix}{title}",
                xlabel,
                zero_line=zero_line,
                bounds=bounds,
            )
        )
    if columns["polynomial"]:
        for power in range(len(columns["polynomial"][0])):
            panels.append(
                density_panel_spec(
                    tossups[[per_dimension[power] for per_dimension in columns["polynomial"]]],
                    f"{title_prefix}polynomial coefficients for x^{power}",
                    f"raw coefficient c{power}",
                    zero_line=True,
                )
            )
    if columns["monotone"]:
        monotone = columns["monotone"]
        for key, title, xlabel, bounds in (
            ("start", "Starting difficulty", "difficulty at x=0", None),
            ("end", "Ending difficulty", "difficulty at x=1", None),
            ("total", "Total difficulty drop", "start minus end", (0, None)),
        ):
            panels.append(
                density_panel_spec(
                    tossups[monotone[key]],
                    f"{title_prefix}{title}",
                    xlabel,
                    zero_line=key != "total",
                    bounds=bounds,
                )
            )
        for share in range(len(monotone["shares"][0])):
            panels.append(
                density_panel_spec(
                    tossups[
                        [
                            per_dimension[share]
                            for per_dimension in monotone["shares"]
                        ]
                    ],
                    f"{title_prefix}difficulty drop share {share + 1}",
                    "proportion of total drop",
                    bounds=(0, 1),
                )
            )
    if columns["spline"]:
        panels.append(
            density_panel_spec(
                tossups[
                    [
                        landmark
                        for dimension in columns["spline"]["y"]
                        for landmark in dimension
                    ]
                ],
                f"{title_prefix}linear-spline landmarks",
                "difficulty landmark y",
                zero_line=True,
            )
        )
    if alpha_columns and include_weights:
        role = "relevance" if weight_name == "r" else "discrimination"
        panels.append(
            density_panel_spec(
                tossups[alpha_columns],
                f"Tossup {role} coordinates",
                weight_name,
                zero_line=True,
            )
        )
        panels.append(
            density_panel_spec(
                tossups[norm_column],
                f"Tossup {role} magnitude",
                f"{weight_name} norm",
                bounds=(0, None),
            )
        )
    return panels


def _difficulty_curve_distribution_plot(
    tossups,
    output_dir,
    adjustments=None,
    link="sigmoid",
    difficulty_scale=1.0,
    parameter_prefix="",
    family_label="Correctness difficulty",
    filename="pyramidal_difficulty_curve_distribution.png",
    csv_filename="pyramidal_difficulty_curve_distribution.csv",
):
    """Plot percentile bands across every learned tossup difficulty curve (Eq. 3).

    'adjustments' (saved signed TF-IDF difficulty deltas) shifts each tossup's
    curve to the effective difficulty 'd'' the model actually used.
    """
    positions = np.linspace(0, 1, 150)
    curves = []
    for _, tossup in tossups.iterrows():
        curve = _saved_difficulty_curve(
            tossup,
            positions,
            link,
            difficulty_scale,
            parameter_prefix,
        )
        if curve is None:
            return
        curves.append(curve)
    if not curves:
        return
    curves = np.asarray(curves)
    columns = _parameter_columns(tossups, parameter_prefix)
    weight_name = vector_weight_name(columns["alpha"])
    label = (
        f"Median {weight_name}-weighted {family_label.lower()}"
        if columns["alpha"]
        else f"Median {family_label.lower()}"
    )
    ylabel = (
        f"Estimated {weight_name}-weighted {family_label.lower()}"
        if columns["alpha"]
        else f"Estimated {family_label.lower()}"
    )
    if adjustments is not None and "tossup_id" in tossups:
        for index, tossup_id in enumerate(tossups["tossup_id"].astype(str)):
            adjustment = difficulty_adjustment_at(adjustments, tossup_id, positions)
            if adjustment is not None:
                curves[index] = curves[index] + adjustment
        label = f"{label} (TF-IDF effective d')"
    percentiles = np.percentile(curves, [5, 25, 50, 75, 95], axis=0)
    pd.DataFrame(
        {
            "relative_position": positions,
            "p05": percentiles[0],
            "p25": percentiles[1],
            "p50": percentiles[2],
            "p75": percentiles[3],
            "p95": percentiles[4],
        }
    ).to_csv(csv_path(output_dir, csv_filename), index=False)
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.fill_between(
        positions,
        percentiles[0],
        percentiles[4],
        alpha=0.15,
        label="5th-95th percentile",
    )
    ax.fill_between(
        positions,
        percentiles[1],
        percentiles[3],
        alpha=0.3,
        label="25th-75th percentile",
    )
    ax.plot(positions, percentiles[2], linewidth=2, label=label)
    ax.set(
        title=f"Distribution of learned tossup {family_label.lower()} curves",
        xlabel="Relative question position",
        ylabel=ylabel,
        xlim=(0, 1),
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, filename, "tossup"), dpi=160)
    plt.close(fig)


def _flatten(nested):
    """Flatten the per-dimension columns used by saved curve schemas."""
    return [column for group in nested for column in group]


def _difficulty_summary_columns(columns, parameter_prefix=""):
    """Return every saved coordinate for one difficulty family."""
    result = [
        f"{parameter_prefix}{name}" for name in ("beta", "bias", "gamma", "mu")
    ]
    result.extend(
        column
        for name in ("beta", "bias", "gamma", "mu")
        for column in columns[name]
    )
    result.extend(_flatten(columns["polynomial"]))
    if columns["monotone"]:
        result.extend(
            [
                *columns["monotone"]["start"],
                *columns["monotone"]["end"],
                *columns["monotone"]["total"],
                *_flatten(columns["monotone"]["shares"]),
            ]
        )
    if columns["scalar_monotone"]:
        result.extend(
            [
                columns["scalar_monotone"]["start"],
                columns["scalar_monotone"]["end"],
                columns["scalar_monotone"]["total"],
                *columns["scalar_monotone"]["shares"],
            ]
        )
    if columns["spline"]:
        result.extend(_flatten(columns["spline"]["y"]))
    return result


def pyramidal_parameter_distribution_plots(results_dir, output_dir):
    """Plot fitted player and tossup parameter distributions.

    Reads the Stage 1 'players.csv' and 'tossups.csv' and writes player/tossup
    parameter panels, difficulty-curve bands and sampled percentile CSVs, plus
    a parameter summary. Double-difficulty runs receive parallel correctness
    and hazard outputs.
    """
    player_path = results_dir / "players.csv"
    tossup_path = results_dir / "tossups.csv"
    if not player_path.exists() or not tossup_path.exists():
        return
    players = pd.read_csv(player_path)
    tossups = pd.read_csv(tossup_path)
    theta_columns = numeric_columns(players, "theta_")
    tossup_columns = _parameter_columns(tossups)
    alpha_columns = tossup_columns["alpha"]
    weight_name = vector_weight_name(alpha_columns)
    norm_column = f"{weight_name}_norm"
    if "theta_norm" not in players and theta_columns:
        players["theta_norm"] = np.linalg.norm(
            players[theta_columns].to_numpy(dtype=float), axis=1
        )
    if alpha_columns:
        tossups[norm_column] = np.linalg.norm(
            tossups[alpha_columns].to_numpy(dtype=float), axis=1
        )

    player_panels = _pyramidal_player_panels(players, theta_columns)
    if player_panels:
        distribution_dashboard(
            player_panels,
            "Pyramidal player parameter distributions",
            graph_path(
                output_dir,
                "pyramidal_player_parameter_distributions.png",
                "parameters",
            ),
        )

    tossup_panels = _pyramidal_tossup_panels(tossups, alpha_columns)
    if tossup_panels:
        distribution_dashboard(
            tossup_panels,
            "Pyramidal tossup parameter distributions",
            graph_path(
                output_dir,
                "pyramidal_tossup_parameter_distributions.png",
                "parameters",
            ),
        )

    has_hazard_difficulty = _has_saved_difficulty(tossups, "hazard_")
    hazard_columns = _parameter_columns(tossups, "hazard_")
    if has_hazard_difficulty:
        hazard_panels = _pyramidal_tossup_panels(
            tossups,
            hazard_columns["alpha"],
            parameter_prefix="hazard_",
            include_weights=False,
        )
        if hazard_panels:
            distribution_dashboard(
                hazard_panels,
                "Pyramidal hazard difficulty parameter distributions",
                graph_path(
                    output_dir,
                    "pyramidal_hazard_parameter_distributions.png",
                    "parameters",
                ),
            )

    adjustments = load_difficulty_adjustment_curves(results_dir)
    link = load_difficulty_link(results_dir)
    difficulty_scale = load_difficulty_scale(results_dir)
    _difficulty_curve_distribution_plot(
        tossups,
        output_dir,
        adjustments,
        link,
        difficulty_scale,
    )
    if has_hazard_difficulty:
        _difficulty_curve_distribution_plot(
            tossups,
            output_dir,
            adjustments,
            link,
            difficulty_scale,
            parameter_prefix="hazard_",
            family_label="Hazard difficulty",
            filename="pyramidal_hazard_difficulty_curve_distribution.png",
            csv_filename="pyramidal_hazard_difficulty_curve_distribution.csv",
        )

    rows = []
    player_alpha_columns = numeric_columns(players, "alpha_")
    player_beta_columns = numeric_columns(players, "beta_")
    groups = [
        (
            "player",
            players,
            [
                "c",
                "alpha",
                "beta",
                *theta_columns,
                *player_alpha_columns,
                *player_beta_columns,
                "theta_norm",
            ],
        ),
        (
            "tossup",
            tossups,
            [
                *_difficulty_summary_columns(tossup_columns),
                *alpha_columns,
                norm_column,
            ],
        ),
    ]
    if has_hazard_difficulty:
        groups.append(
            (
                "tossup_hazard",
                tossups,
                [
                    *_difficulty_summary_columns(hazard_columns, "hazard_"),
                    *(
                        hazard_columns["alpha"]
                        if hazard_columns["alpha"] != alpha_columns
                        else []
                    ),
                ],
            )
        )
    for group, frame, columns in groups:
        for column in columns:
            if column in frame:
                summary = distribution_summary(group, column, frame[column])
                if summary:
                    rows.append(summary)
    pd.DataFrame(rows).to_csv(
        csv_path(output_dir, "pyramidal_parameter_distribution_summary.csv"), index=False
    )
