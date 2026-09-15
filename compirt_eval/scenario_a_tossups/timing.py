"""Compare fitted and empirical first-buzz timing for representative tossups."""

from __future__ import annotations

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.common.figures import short_id
from compirt_eval.common.report_paths import csv_path, graph_path
from compirt_eval.scenario_a_tossups.difficulty import selected_tossups
from compirt_eval.scenario_a_tossups.parameters import _saved_effective_mu
from compirt_eval.scenario_a_tossups.reconstruction import (
    _load_timing_evaluation_inputs,
    conditional_expected_buzz_position,
    event_first_buzz_components,
    first_buzz_distribution,
)
from compirt_eval.scenario_a_tossups.survival import (
    evaluate_survival_and_first_buzzer,
)


__all__ = [
    "buzz_density_fit_plot",
    "conditional_expected_buzz_position",
    "evaluate_survival_and_first_buzzer",
    "event_first_buzz_components",
    "first_buzz_distribution",
]


def _aggregate_buzz_timing(
    predictions,
    players,
    tossups,
    tossup_id,
    n_bins,
    adjustments=None,
    link="sigmoid",
    buzz_parameter_prefix=None,
    difficulty_scale=1.0,
    terminal_intercepts=(0.0, 0.0),
):
    """Average fitted and empirical first-buzz mass over one tossup's events.

    Walks every event for 'tossup_id', sums the model's fitted first-buzz mass
    (from 'first_buzz_distribution') against the single observed buzz bin, then
    normalizes by the event count. Returns the per-event mass arrays, both dead
    rates, or 'None' when no usable event is found (so the caller can blank
    that subplot).
    """
    predicted = np.zeros(n_bins)
    observed = np.zeros(n_bins)
    predicted_dead = 0.0
    observed_dead = 0
    event_count = 0
    tossup_events = predictions[predictions["tossup_id"] == tossup_id]
    for _, event in tossup_events.groupby("event_id"):
        if not set(event["player_id"]).issubset(players.index):
            continue
        fitted_mass, fitted_dead = first_buzz_distribution(
            event,
            players,
            tossups,
            n_bins,
            adjustments,
            link,
            buzz_parameter_prefix,
            difficulty_scale,
            terminal_intercepts,
        )
        predicted += fitted_mass
        predicted_dead += fitted_dead
        buzz = event[event["z"] == "BUZZ"]
        if buzz.empty:
            observed_dead += 1
        else:
            index = min(
                int(float(buzz["relative_position"].iloc[0]) * n_bins),
                n_bins - 1,
            )
            observed[index] += 1
        event_count += 1
    if event_count == 0:
        return None
    predicted /= event_count
    predicted_dead /= event_count
    observed /= event_count
    observed_dead_rate = observed_dead / event_count
    return {
        "event_count": event_count,
        "predicted": predicted,
        "observed": observed,
        "predicted_dead": predicted_dead,
        "observed_dead_rate": observed_dead_rate,
    }


def buzz_density_fit_plot(results_dir, output_dir, n_bins=12):
    """Compare empirical and fitted first-buzz timing for representative tossups."""
    inputs = _load_timing_evaluation_inputs(results_dir)
    if inputs is None:
        return

    selected = [
        tossup_id
        for tossup_id in selected_tossups(inputs.predictions)
        if tossup_id in inputs.tossups.index
    ]
    if not selected:
        return
    columns = 2
    rows = math.ceil(len(selected) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(12, 3.8 * rows), squeeze=False)
    centers = (np.arange(n_bins) + 0.5) / n_bins
    summaries = []
    for ax, tossup_id in zip(axes.flat, selected):
        timing = _aggregate_buzz_timing(
            inputs.predictions,
            inputs.players,
            inputs.tossups,
            tossup_id,
            n_bins,
            inputs.adjustments,
            inputs.link,
            inputs.buzz_parameter_prefix,
            inputs.difficulty_scale,
            inputs.terminal_intercepts,
        )
        if timing is None:
            ax.set_visible(False)
            continue
        event_count = timing["event_count"]
        predicted = timing["predicted"]
        observed = timing["observed"]
        predicted_dead = timing["predicted_dead"]
        observed_dead_rate = timing["observed_dead_rate"]
        summaries.append(
            {
                "tossup_id": tossup_id,
                "events": event_count,
                "observed_dead_rate": observed_dead_rate,
                "predicted_dead_rate": predicted_dead,
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
        mu = _saved_effective_mu(
            inputs.tossups.loc[tossup_id],
            inputs.buzz_parameter_prefix,
        )
        if mu is not None:
            ax.axvline(
                mu,
                color="tab:green",
                linestyle="--",
                linewidth=1.5,
                label=f"Hazard difficulty inflection ($\\mu$={mu:.2f})",
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
            f"dead: observed={observed_dead_rate:.2f}, predicted={predicted_dead:.2f}",
            transform=ax.transAxes,
            va="top",
            fontsize=8,
        )
        ax.grid(alpha=0.2)
        ax.legend(fontsize=7, loc="upper right")
    for ax in axes.flat[len(selected):]:
        ax.set_visible(False)
    fig.suptitle("Hazard-based predicted versus empirical first-buzz timing")
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, "tossup_buzz_density_fit.png", "tossup"), dpi=160)
    plt.close(fig)
    pd.DataFrame(summaries).to_csv(
        csv_path(output_dir, "tossup_buzz_density_metrics.csv"), index=False
    )
