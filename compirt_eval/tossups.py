"""Scenario A: tossup first-buzz evaluation.

Correctness calibration, fitted-versus-empirical buzz timing,
difficulty curves over observed buzz locations, and the fitted
pyramidal player/tossup parameter distributions. ``evaluate_tossups``
is the entry point.
"""

from __future__ import annotations

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    median_absolute_error,
)

from compirt_eval.metrics import calibration_table, classification_metrics, difficulty_curve, inverse_logit
from compirt_eval.figures import distribution_dashboard, distribution_summary, numeric_columns, reliability_plot, short_id


def stratified_tossup_reliability_plot(buzz, output_dir):
    """Plot tossup calibration separately for early, middle, and late buzzes."""
    labels = ["Early third", "Middle third", "Late third"]
    buzz = buzz.copy()
    buzz["position_group"] = pd.cut(
        buzz["relative_position"],
        bins=[0.0, 1 / 3, 2 / 3, 1.0],
        labels=labels,
        include_lowest=True,
    )
    rows = []
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.plot([0, 1], [0, 1], "--", color="0.5", label="Perfect calibration")
    for label in labels:
        group = buzz[buzz["position_group"] == label]
        if group.empty:
            continue
        metrics = classification_metrics(group["y"], group["predicted_correct"])
        rows.append({"position_group": label, "observations": len(group), **metrics})
        calibration = calibration_table(group["y"], group["predicted_correct"], n_bins=8)
        ax.plot(
            calibration["predicted"],
            calibration["observed"],
            "o-",
            label=f"{label} (n={len(group):,}, ECE={metrics['ece']:.3f})",
        )
    ax.set(
        title="Tossup reliability by buzz position",
        xlabel="Predicted probability",
        ylabel="Observed correctness",
        xlim=(0, 1),
        ylim=(0, 1),
    )
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(output_dir / "tossup_reliability_by_buzz_position.png", dpi=160)
    plt.close(fig)
    pd.DataFrame(rows).to_csv(output_dir / "tossup_metrics_by_buzz_position.csv", index=False)


def _pyramidal_player_panels(players, theta_columns):
    """Build the density panels for fitted player parameters (c, theta)."""
    panels = []
    if "c" in players:
        panels.append(
            {
                "series": {"c": players["c"]},
                "title": "Confidence threshold",
                "xlabel": "c",
                "zero_line": True,
                "bounds": None,
            }
        )
    if theta_columns:
        panels.append(
            {
                "series": {column: players[column] for column in theta_columns},
                "title": "Skill coordinates",
                "xlabel": "theta",
                "zero_line": True,
                "bounds": None,
            }
        )
    if "theta_norm" in players:
        panels.append(
            {
                "series": {"theta_norm": players["theta_norm"]},
                "title": "Skill magnitude",
                "xlabel": "theta norm",
                "zero_line": False,
                "bounds": (0, None),
            }
        )
    return panels


def _pyramidal_tossup_panels(tossups, alpha_columns):
    """Build the density panels for fitted tossup parameters (beta, gamma, mu, alpha)."""
    panels = []
    for column, title, xlabel, zero_line in (
        ("beta", "Difficulty amplitude", "beta", True),
        ("mu", "Difficulty transition location", "relative position mu", False),
    ):
        if column in tossups:
            panels.append(
                {
                    "series": {column: tossups[column]},
                    "title": title,
                    "xlabel": xlabel,
                    "zero_line": zero_line,
                    "bounds": (0, 1) if column == "mu" else None,
                }
            )
    if "gamma" in tossups:
        # gamma is positive and heavy-tailed, so plot it on a log10 axis between
        # the amplitude and location panels.
        positive_gamma = tossups.loc[tossups["gamma"] > 0, "gamma"]
        panels.insert(
            1,
            {
                "series": {"log10_gamma": np.log10(positive_gamma)},
                "title": "Difficulty transition sharpness",
                "xlabel": "log10(gamma)",
                "zero_line": True,
                "bounds": None,
            },
        )
    if alpha_columns:
        panels.append(
            {
                "series": {column: tossups[column] for column in alpha_columns},
                "title": "Tossup discrimination coordinates",
                "xlabel": "alpha",
                "zero_line": True,
                "bounds": None,
            }
        )
        panels.append(
            {
                "series": {"alpha_norm": tossups["alpha_norm"]},
                "title": "Tossup discrimination magnitude",
                "xlabel": "alpha norm",
                "zero_line": False,
                "bounds": (0, None),
            }
        )
    return panels


def _difficulty_curve_distribution_plot(tossups, output_dir):
    """Plot percentile bands across every learned tossup difficulty curve (Eq. 3)."""
    if not {"beta", "gamma", "mu"}.issubset(tossups):
        return
    positions = np.linspace(0, 1, 150)
    curves = difficulty_curve(
        tossups["beta"].to_numpy()[:, None],
        tossups["gamma"].to_numpy()[:, None],
        tossups["mu"].to_numpy()[:, None],
        positions[None, :],
    )
    percentiles = np.percentile(curves, [5, 25, 50, 75, 95], axis=0)
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
    ax.plot(positions, percentiles[2], linewidth=2, label="Median difficulty")
    ax.set(
        title="Distribution of learned tossup difficulty curves",
        xlabel="Relative question position",
        ylabel="Estimated difficulty",
        xlim=(0, 1),
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "pyramidal_difficulty_curve_distribution.png", dpi=160)
    plt.close(fig)


def pyramidal_parameter_distribution_plots(results_dir, output_dir):
    """Plot fitted player and tossup parameter distributions.

    Reads the Stage 1 ``players.csv`` and ``tossups.csv`` and writes three
    figures (player panels, tossup panels, difficulty-curve bands) and a summary
    CSV. Panel construction is delegated to the ``_pyramidal_*`` helpers above.
    """
    player_path = results_dir / "players.csv"
    tossup_path = results_dir / "tossups.csv"
    if not player_path.exists() or not tossup_path.exists():
        return
    players = pd.read_csv(player_path)
    tossups = pd.read_csv(tossup_path)
    theta_columns = numeric_columns(players, "theta_")
    alpha_columns = numeric_columns(tossups, "alpha_")
    if "theta_norm" not in players and theta_columns:
        players["theta_norm"] = np.linalg.norm(
            players[theta_columns].to_numpy(dtype=float), axis=1
        )
    if alpha_columns:
        tossups["alpha_norm"] = np.linalg.norm(
            tossups[alpha_columns].to_numpy(dtype=float), axis=1
        )

    player_panels = _pyramidal_player_panels(players, theta_columns)
    if player_panels:
        distribution_dashboard(
            player_panels,
            "Pyramidal player parameter distributions",
            output_dir / "pyramidal_player_parameter_distributions.png",
        )

    tossup_panels = _pyramidal_tossup_panels(tossups, alpha_columns)
    if tossup_panels:
        distribution_dashboard(
            tossup_panels,
            "Pyramidal tossup parameter distributions",
            output_dir / "pyramidal_tossup_parameter_distributions.png",
        )

    _difficulty_curve_distribution_plot(tossups, output_dir)

    rows = []
    for group, frame, columns in (
        ("player", players, ["c", *theta_columns, "theta_norm"]),
        ("tossup", tossups, ["beta", "gamma", "mu", *alpha_columns, "alpha_norm"]),
    ):
        for column in columns:
            if column in frame:
                summary = distribution_summary(group, column, frame[column])
                if summary:
                    rows.append(summary)
    pd.DataFrame(rows).to_csv(
        output_dir / "pyramidal_parameter_distribution_summary.csv", index=False
    )


def tossup_observation_summary(predictions):
    """Summarize event frequency and empirical buzz timing by tossup."""
    summary = (
        predictions.assign(is_buzz=predictions["z"] == "BUZZ")
        .groupby("tossup_id")
        .agg(
            events=("event_id", "nunique"),
            buzzes=("is_buzz", "sum"),
        )
    )
    mean_position = (
        predictions[predictions["z"] == "BUZZ"]
        .groupby("tossup_id")["relative_position"]
        .mean()
        .rename("mean_buzz_position")
    )
    return summary.join(mean_position)


def evenly_spaced_ids(frame, sort_column, count=6):
    """Select IDs across the range of a diagnostic variable."""
    if frame.empty:
        return []
    frame = frame.sort_values(sort_column)
    if len(frame) <= count:
        return frame.index.tolist()
    positions = np.linspace(0, len(frame) - 1, count).round().astype(int)
    return frame.iloc[np.unique(positions)].index.tolist()


def selected_tossups(predictions, count=6):
    """Choose frequently observed tossups across the empirical timing range."""
    summary = tossup_observation_summary(predictions)
    minimum_events = summary["events"].quantile(0.75)
    frequent = summary[summary["events"] >= minimum_events].copy()
    frequent["mean_buzz_position"] = frequent["mean_buzz_position"].fillna(1.0)
    return evenly_spaced_ids(frequent, "mean_buzz_position", count)


def difficulty_plot(results_dir, output_dir):
    """Plot learned difficulty curves over empirical first-buzz locations."""
    parameters = pd.read_csv(results_dir / "tossups.csv").set_index("tossup_id")
    predictions = pd.read_csv(results_dir / "tossup_predictions.csv")
    selected = [
        tossup_id
        for tossup_id in selected_tossups(predictions)
        if tossup_id in parameters.index
    ]
    positions = np.linspace(0.0, 1.0, 100)

    if not selected:
        return
    columns = 2
    rows = math.ceil(len(selected) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(12, 3.7 * rows), squeeze=False)
    for ax, tossup_id in zip(axes.flat, selected):
        row = parameters.loc[tossup_id]
        difficulty = difficulty_curve(row["beta"], row["gamma"], row["mu"], positions)
        buzz_positions = predictions.loc[
            (predictions["tossup_id"] == tossup_id) & (predictions["z"] == "BUZZ"),
            "relative_position",
        ]
        ax.hist(
            buzz_positions,
            bins=np.linspace(0, 1, 11),
            color="tab:orange",
            alpha=0.25,
            label=f"Observed buzzes (n={len(buzz_positions)})",
        )
        curve_ax = ax.twinx()
        curve_ax.plot(
            positions,
            difficulty,
            color="tab:blue",
            linewidth=2,
            label="Difficulty",
        )
        ax.set(
            title=short_id(tossup_id),
            xlabel="Relative position",
            ylabel="Buzz count",
            xlim=(0, 1),
        )
        curve_ax.set_ylabel("Estimated difficulty")
        ax.grid(alpha=0.2)
        handles, labels = ax.get_legend_handles_labels()
        curve_handles, curve_labels = curve_ax.get_legend_handles_labels()
        ax.legend(
            handles + curve_handles,
            labels + curve_labels,
            fontsize=7,
            loc="upper right",
        )
    for ax in axes.flat[len(selected):]:
        ax.set_visible(False)
    fig.suptitle("Estimated tossup difficulty and empirical buzz locations")
    fig.tight_layout()
    fig.savefig(output_dir / "tossup_difficulty_curves.png", dpi=160)
    plt.close(fig)


def first_buzz_distribution(event, players, tossups, n_bins=12):
    """Reconstruct team first-buzz mass from saved posterior median parameters.

    This mirrors the model's competing-risks timing (Eq. 5 hazard and Eq. 6
    survival) outside Pyro: it walks every token, combines the roster's
    independent no-buzz probabilities into a team hazard, and returns how much
    first-buzz probability falls in each of ``n_bins`` relative-position bins,
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
    difficulty = difficulty_curve(
        float(tossup["beta"]),
        float(tossup["gamma"]),
        float(tossup["mu"]),
        relative,
    )
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


def _aggregate_buzz_timing(predictions, players, tossups, tossup_id, n_bins):
    """Average fitted and empirical first-buzz mass over one tossup's events.

    Walks every event for ``tossup_id``, sums the model's fitted first-buzz mass
    (from ``first_buzz_distribution``) against the single observed buzz bin, then
    normalizes by the event count. Returns the per-event mass arrays, both dead
    rates, and the total-variation distance, or ``None`` when no usable event is
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
        fitted_mass, fitted_dead = first_buzz_distribution(event, players, tossups, n_bins)
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

    selected = [item for item in selected_tossups(predictions) if item in tossups.index]
    if not selected:
        return
    columns = 2
    rows = math.ceil(len(selected) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(12, 3.8 * rows), squeeze=False)
    centers = (np.arange(n_bins) + 0.5) / n_bins
    summaries = []
    for ax, tossup_id in zip(axes.flat, selected):
        timing = _aggregate_buzz_timing(predictions, players, tossups, tossup_id, n_bins)
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
        mu = float(tossups.loc[tossup_id, "mu"])
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
    fig.savefig(output_dir / "tossup_buzz_density_fit.png", dpi=160)
    plt.close(fig)
    pd.DataFrame(summaries).to_csv(output_dir / "tossup_buzz_density_metrics.csv", index=False)


def player_skill_stability_plot(primary_dir, comparison_dir, output_dir):
    """Compare player skill magnitude and rank across two fitted pyramidal runs."""
    left = pd.read_csv(primary_dir / "players.csv", dtype={"player_id": str})
    right = pd.read_csv(comparison_dir / "players.csv", dtype={"player_id": str})
    for frame in (left, right):
        if "theta_norm" not in frame:
            frame["theta_norm"] = np.linalg.norm(
                frame[numeric_columns(frame, "theta_")].to_numpy(dtype=float), axis=1
            )
    comparison = left[["player_id", "theta_norm"]].merge(
        right[["player_id", "theta_norm"]],
        on="player_id",
        suffixes=("_primary", "_comparison"),
    )
    if comparison.empty:
        return
    comparison["rank_primary"] = comparison["theta_norm_primary"].rank(ascending=False)
    comparison["rank_comparison"] = comparison["theta_norm_comparison"].rank(ascending=False)
    comparison["absolute_rank_change"] = (
        comparison["rank_comparison"] - comparison["rank_primary"]
    ).abs()
    comparison.to_csv(output_dir / "player_skill_stability.csv", index=False)

    fig, (skill_ax, rank_ax) = plt.subplots(1, 2, figsize=(12, 5.5))
    skill_ax.scatter(
        comparison["theta_norm_primary"],
        comparison["theta_norm_comparison"],
        alpha=0.5,
    )
    skill_limit = max(
        comparison["theta_norm_primary"].max(),
        comparison["theta_norm_comparison"].max(),
    )
    skill_ax.plot([0, skill_limit], [0, skill_limit], "--", color="0.5")
    skill_ax.set(
        title="Skill magnitude stability",
        xlabel=primary_dir.name,
        ylabel=comparison_dir.name,
    )
    rank_ax.scatter(comparison["rank_primary"], comparison["rank_comparison"], alpha=0.5)
    rank_limit = max(comparison["rank_primary"].max(), comparison["rank_comparison"].max())
    rank_ax.plot([1, rank_limit], [1, rank_limit], "--", color="0.5")
    rank_ax.invert_xaxis()
    rank_ax.invert_yaxis()
    rank_ax.set(
        title="Player rank stability",
        xlabel=primary_dir.name,
        ylabel=comparison_dir.name,
    )
    for _, row in comparison.nlargest(min(8, len(comparison)), "absolute_rank_change").iterrows():
        rank_ax.annotate(
            short_id(row["player_id"], 18),
            (row["rank_primary"], row["rank_comparison"]),
            fontsize=7,
        )
    for ax in (skill_ax, rank_ax):
        ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(output_dir / "player_skill_stability.png", dpi=160)
    plt.close(fig)


def evaluate_tossups(results_dir, output_dir):
    """Evaluate first-buzz correctness and expected first-buzz position."""
    buzz = pd.read_csv(results_dir / "tossup_predictions.csv")
    # Only actual buzzers have an observed correctness outcome.
    buzz = buzz[buzz["z"] == "BUZZ"]
    metrics = classification_metrics(buzz["y"], buzz["predicted_correct"])
    if not buzz.empty:
        reliability_plot(
            buzz["y"],
            buzz["predicted_correct"],
            "Tossup correctness reliability",
            output_dir / "tossup_reliability.png",
        )
        stratified_tossup_reliability_plot(buzz, output_dir)
    difficulty_plot(results_dir, output_dir)
    buzz_density_fit_plot(results_dir, output_dir)
    pyramidal_parameter_distribution_plots(results_dir, output_dir)

    position_path = results_dir / "buzz_event_predictions.csv"
    if position_path.exists():
        # Position predictions already contain one row per first-buzz event.
        events = pd.read_csv(position_path)
        metrics.update(
            {
                "buzz_position_mae": mean_absolute_error(
                    events["observed_relative_position"],
                    events["predicted_relative_position"],
                ),
                "buzz_position_median_absolute_error": median_absolute_error(
                    events["observed_relative_position"],
                    events["predicted_relative_position"],
                ),
            }
        )
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.scatter(
            events["observed_relative_position"],
            events["predicted_relative_position"],
            alpha=0.25,
        )
        ax.plot([0, 1], [0, 1], "--", color="0.5")
        ax.set(
            title="Observed versus predicted buzz position",
            xlabel="Observed",
            ylabel="Predicted",
            xlim=(0, 1),
            ylim=(0, 1),
        )
        ax.grid(alpha=0.25)
        fig.tight_layout()
        fig.savefig(output_dir / "tossup_position_predictions.png", dpi=160)
        plt.close(fig)
    return metrics
