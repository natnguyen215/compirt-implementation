"""Compare fitted versus empirical first-buzz timing.

'first_buzz_distribution' reconstructs the model's competing-risks timing
(Eq. 5 hazard, Eq. 6 survival) for one event using only saved posterior
median parameters, outside of Pyro. 'buzz_density_fit_plot' averages that
reconstruction over every event of a representative sample of tossups and
compares it against the single empirical buzz each event actually produced,
as both a figure and a total-variation-distance summary CSV.
"""

from __future__ import annotations

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.figures import numeric_columns, short_id
from compirt_eval.metrics import difficulty_curve, inverse_logit
from compirt_eval.outputs import csv_path, graph_path
from compirt_eval.tossups.difficulty import selected_tossups
from compirt_eval.tossups.parameters import (
    _multidim_effective_difficulty,
    _parameter_columns,
    _saved_effective_mu,
    _supports_first_buzz_reconstruction,
    _validate_multidim_dimensions,
    difficulty_adjustment_at,
    load_difficulty_adjustment_curves,
)


def first_buzz_distribution(event, players, tossups, n_bins=12, adjustments=None):
    """Reconstruct team first-buzz mass from saved posterior median parameters.

    This mirrors the model's competing-risks timing (Eq. 5 hazard and Eq. 6
    survival) outside Pyro: it walks every token, combines the roster's
    independent no-buzz probabilities into a team hazard, and returns how much
    first-buzz probability falls in each of 'n_bins' relative-position bins,
    plus the dead-tossup (nobody buzzes) mass.
    """
    tossup_id = event["tossup_id"].iloc[0]
    tossup = tossups.loc[tossup_id]
    roster = players.loc[event["player_id"].astype(str)]
    theta_columns = numeric_columns(players, "theta_")
    alpha_columns = numeric_columns(tossups, "alpha_")
    if not theta_columns or len(theta_columns) != len(alpha_columns):
        raise ValueError("Saved theta and alpha dimensions must be present and match")

    total_tokens = int(event["T_j"].iloc[0])
    positions = np.arange(1, total_tokens + 1, dtype=float)
    relative = positions / total_tokens
    if {"beta", "gamma", "mu"}.issubset(tossup.index):
        difficulty = difficulty_curve(
            float(tossup["beta"]),
            float(tossup["gamma"]),
            float(tossup["mu"]),
            relative,
        )
    else:
        columns = _parameter_columns(tossups)
        _validate_multidim_dimensions(
            theta_columns,
            alpha_columns,
            columns["beta"],
            columns["gamma"],
            columns["mu"],
        )
        difficulty = _multidim_effective_difficulty(tossup, relative)
    adjustment = difficulty_adjustment_at(adjustments, tossup_id, relative)
    if adjustment is not None:
        # TF-IDF runs: replay the effective difficulty d' the model trained on.
        difficulty = difficulty - adjustment
    skill = (
        roster[theta_columns].to_numpy(dtype=float)
        @ tossup[alpha_columns].to_numpy(dtype=float)
    )
    logits = (
        skill[:, None]
        - difficulty[None, :]
        - roster["c"].to_numpy(dtype=float)[:, None]
    )
    hazard = inverse_logit(logits)
    team_hazard = 1.0 - np.prod(1.0 - hazard, axis=0)
    survival_before = np.concatenate(([1.0], np.cumprod(1.0 - team_hazard[:-1])))
    first_buzz_mass = survival_before * team_hazard
    dead_mass = float(np.prod(1.0 - team_hazard))

    bin_index = np.clip((relative * n_bins).astype(int), 0, n_bins - 1)
    binned_mass = np.zeros(n_bins)
    np.add.at(binned_mass, bin_index, first_buzz_mass)
    return binned_mass, dead_mass


def _aggregate_buzz_timing(predictions, players, tossups, tossup_id, n_bins, adjustments=None):
    """Average fitted and empirical first-buzz mass over one tossup's events.

    Walks every event for 'tossup_id', sums the model's fitted first-buzz mass
    (from 'first_buzz_distribution') against the single observed buzz bin, then
    normalizes by the event count. Returns the per-event mass arrays, both dead
    rates, and the total-variation distance, or 'None' when no usable event is
    found (so the caller can blank that subplot).
    """
    predicted = np.zeros(n_bins)
    observed = np.zeros(n_bins)
    predicted_dead = 0.0
    observed_dead = 0
    event_count = 0
    for _, event in predictions[predictions["tossup_id"] == tossup_id].groupby("event_id"):
        if not set(event["player_id"]).issubset(players.index):
            continue
        fitted_mass, fitted_dead = first_buzz_distribution(
            event, players, tossups, n_bins, adjustments
        )
        predicted += fitted_mass
        predicted_dead += fitted_dead
        buzz = event[event["z"] == "BUZZ"]
        if buzz.empty:
            observed_dead += 1
        else:
            index = min(int(float(buzz["relative_position"].iloc[0]) * n_bins), n_bins - 1)
            observed[index] += 1
        event_count += 1
    if event_count == 0:
        return None
    predicted /= event_count
    predicted_dead /= event_count
    observed /= event_count
    observed_dead_rate = observed_dead / event_count
    total_variation = 0.5 * (
        np.abs(predicted - observed).sum() + abs(predicted_dead - observed_dead_rate)
    )
    return {
        "event_count": event_count,
        "predicted": predicted,
        "observed": observed,
        "predicted_dead": predicted_dead,
        "observed_dead_rate": observed_dead_rate,
        "total_variation": total_variation,
    }


def buzz_density_fit_plot(results_dir, output_dir, n_bins=12):
    """Compare empirical and fitted first-buzz timing for representative tossups."""
    required = [
        results_dir / "players.csv",
        results_dir / "tossups.csv",
        results_dir / "tossup_predictions.csv",
    ]
    if not all(path.exists() for path in required):
        return
    players = pd.read_csv(required[0], dtype={"player_id": str}).set_index("player_id")
    tossups = pd.read_csv(required[1], dtype={"tossup_id": str}).set_index("tossup_id")
    predictions = pd.read_csv(required[2], dtype={"player_id": str, "tossup_id": str})
    if "c" not in players or predictions.empty:
        return
    if not _supports_first_buzz_reconstruction(players, tossups):
        return
    adjustments = load_difficulty_adjustment_curves(results_dir)

    selected = [item for item in selected_tossups(predictions) if item in tossups.index]
    if not selected:
        return
    columns = 2
    rows = math.ceil(len(selected) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(12, 3.8 * rows), squeeze=False)
    centers = (np.arange(n_bins) + 0.5) / n_bins
    summaries = []
    for ax, tossup_id in zip(axes.flat, selected):
        timing = _aggregate_buzz_timing(
            predictions, players, tossups, tossup_id, n_bins, adjustments
        )
        if timing is None:
            ax.set_visible(False)
            continue
        event_count = timing["event_count"]
        predicted = timing["predicted"]
        observed = timing["observed"]
        predicted_dead = timing["predicted_dead"]
        observed_dead_rate = timing["observed_dead_rate"]
        total_variation = timing["total_variation"]
        summaries.append(
            {
                "tossup_id": tossup_id,
                "events": event_count,
                "observed_dead_rate": observed_dead_rate,
                "predicted_dead_rate": predicted_dead,
                "timing_total_variation": total_variation,
            }
        )
        ax.bar(
            centers,
            observed,
            width=0.8 / n_bins,
            alpha=0.35,
            color="tab:orange",
            label="Empirical mass",
        )
        ax.plot(centers, predicted, "o-", color="tab:blue", label="Predicted mass")
        mu = _saved_effective_mu(tossups.loc[tossup_id])
        if mu is not None:
            ax.axvline(
                mu,
                color="tab:green",
                linestyle="--",
                linewidth=1.5,
                label=f"Difficulty inflection ($\\mu$={mu:.2f})",
            )
        ax.set(
            title=short_id(tossup_id),
            xlabel="Relative position",
            ylabel="Probability mass per event",
            xlim=(0, 1),
        )
        ax.text(
            0.02,
            0.98,
            f"events={event_count}\n"
            f"dead: observed={observed_dead_rate:.2f}, predicted={predicted_dead:.2f}\n"
            f"TV distance={total_variation:.2f}",
            transform=ax.transAxes,
            va="top",
            fontsize=8,
        )
        ax.grid(alpha=0.2)
        ax.legend(fontsize=7, loc="upper right")
    for ax in axes.flat[len(selected):]:
        ax.set_visible(False)
    fig.suptitle("Predicted versus empirical first-buzz timing")
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, "tossup_buzz_density_fit.png"), dpi=160)
    plt.close(fig)
    pd.DataFrame(summaries).to_csv(
        csv_path(output_dir, "tossup_buzz_density_metrics.csv"), index=False
    )
