"""Output helpers shared by the CompIRT training scripts.

These functions convert fitted tensors to arrays and write the result files
(CSV parameter tables, per-row predictions, the run summary, and the loss plot).
Model definitions and each script's 'run_experiment' orchestration still live in
the individual training scripts; the shared device check and SVI loop live in
'utils.training'.
"""

from __future__ import annotations

import json
from itertools import combinations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def tensor_values(tensor):
    """Return a tensor as a NumPy array for CSV output."""
    return tensor.detach().cpu().numpy()


def add_numbered_tensor_columns(target, prefix, tensor):
    """Add one numbered column per tensor coordinate (e.g. alpha_1..K).

    'target' may be a dict or a DataFrame; either accepts 'target[name] = column'
    the same way. Used to flatten vector-valued player/tossup/bonus parameters
    into readable CSV columns.
    """
    values = tensor_values(tensor)
    if values.ndim != 2:
        raise ValueError(f"Expected {prefix} to be a matrix, got shape {values.shape}")
    for dimension in range(values.shape[1]):
        target[f"{prefix}_{dimension + 1}"] = values[:, dimension]


def save_loss_plot(output_dir, losses, title):
    """Plot ELBO loss over optimization steps to inspect convergence."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(losses)
    ax.set(title=title, xlabel="SVI step", ylabel="ELBO loss")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(output_dir / "loss_curve.png", dpi=160)
    plt.close(fig)


def save_parameters(output_dir, data, posterior):
    """Write fitted player and tossup latent parameters to readable CSV files."""
    # data["player_ids"] shares row order with posterior["theta"]/["c"].
    players = {
        "player_id": data["player_ids"],
        "c": tensor_values(posterior["c"]),
    }
    for dimension in range(posterior["theta"].shape[1]):
        players[f"theta_{dimension + 1}"] = tensor_values(
            posterior["theta"][:, dimension]
        )
    player_df = pd.DataFrame(players)
    # theta_norm is a convenience summary of overall skill magnitude.
    player_df["theta_norm"] = np.linalg.norm(
        player_df.filter(like="theta_").to_numpy(), axis=1
    )
    player_df.to_csv(output_dir / "players.csv", index=False)

    tossups = {
        "tossup_id": data["tossup_ids"],
        "beta": tensor_values(posterior["beta"]),
        "gamma": tensor_values(posterior["gamma"]),
        "mu": tensor_values(posterior["mu"]),
    }
    for dimension in range(posterior["alpha"].shape[1]):
        tossups[f"alpha_{dimension + 1}"] = tensor_values(
            posterior["alpha"][:, dimension]
        )
    pd.DataFrame(tossups).to_csv(output_dir / "tossups.csv", index=False)


def player_posterior_frame(player_ids, guide, tier_map=None):
    """Extract per-player theta/c variational posterior (loc + scale).

    The held-out evaluation reuses the training posterior as the prior on
    returning players (paper Section 4.2 / Appendix B): for an 'AutoNormal'
    guide the per-site loc is the posterior mean and the scale is its standard
    deviation, so saving both lets a later run reconstruct N(loc, scale) priors.
    'tier_map' (player_id -> tier) is recorded so a later run can build the
    tier-conditioned prior for new players from this training set.
    """
    # '_get_loc_and_scale' is AutoNormal's per-site accessor (private but stable
    # across Pyro 1.x); it returns the mean-field loc and constrained scale.
    theta_loc, theta_scale = guide._get_loc_and_scale("theta")
    c_loc, c_scale = guide._get_loc_and_scale("c")
    theta_loc = tensor_values(theta_loc)
    theta_scale = tensor_values(theta_scale)
    frame = {"player_id": player_ids}
    for dimension in range(theta_loc.shape[1]):
        frame[f"theta_{dimension + 1}_loc"] = theta_loc[:, dimension]
        frame[f"theta_{dimension + 1}_scale"] = theta_scale[:, dimension]
    frame["c_loc"] = tensor_values(c_loc)
    frame["c_scale"] = tensor_values(c_scale)
    if tier_map is not None:
        frame["tier"] = [tier_map.get(str(player_id)) for player_id in player_ids]
    return pd.DataFrame(frame)


def save_player_posterior(output_dir, player_ids, guide, tier_map=None):
    """Write the per-player theta/c posterior (loc + scale) for held-out priors."""
    player_posterior_frame(player_ids, guide, tier_map).to_csv(
        output_dir / "player_posterior.csv", index=False
    )


def save_player_buzz_summary(output_dir, predictions):
    """Save per-player observed and fitted correctness over observed buzzes.

    This is a descriptive per-player calibration diagnostic, not a skill
    ranking: 'fitted_correctness' averages P(correct | the player buzzed where
    they did), so it is conditioned on each player's own shot selection.
    Cautious late buzzers score high and aggressive early buzzers score low
    regardless of theta, and buzz volume never enters. For a PPG-comparable
    model quantity use a competing-risks expected-points summary instead
    (see 'compirt_eval.noise_floor').
    """
    summary = (
        predictions[predictions["z"] == "BUZZ"]
        .groupby("player_id", as_index=False)
        .agg(
            buzzes=("y", "size"),
            observed_correctness=("y", "mean"),
            fitted_correctness=("predicted_correct", "mean"),
            average_relative_position=("relative_position", "mean"),
        )
        .sort_values("buzzes", ascending=False)
    )
    summary.to_csv(output_dir / "player_buzz_summary.csv", index=False)


def save_tossup_predictions(
    output_dir,
    observations,
    correct,
    hazard,
    survival,
    *,
    buzz_expected,
    extra_columns=None,
):
    """Attach fitted tossup predictions to the observation rows and save them.

    Writes 'tossup_predictions.csv' (the fitted correctness/hazard/survival for
    every row), the derived 'player_buzz_summary.csv', and
    'buzz_event_predictions.csv' from the required event_id -> expected
    relative position mapping.
    'extra_columns' maps extra column names to
    tensors for model-specific outputs (e.g. the TF-IDF baseline's prefix
    score). Returns the predictions frame for any further per-run use.
    """
    predictions = observations.copy()
    predictions["predicted_correct"] = tensor_values(correct)
    predictions["predicted_hazard"] = tensor_values(hazard)
    predictions["predicted_survival"] = tensor_values(survival)
    for name, column in (extra_columns or {}).items():
        predictions[name] = tensor_values(column)
    predictions.to_csv(output_dir / "tossup_predictions.csv", index=False)
    save_player_buzz_summary(output_dir, predictions)

    buzz_events = predictions[predictions["z"] == "BUZZ"][
        ["event_id", "relative_position"]
    ].rename(columns={"relative_position": "observed_relative_position"})
    buzz_events["predicted_relative_position"] = buzz_events["event_id"].map(
        buzz_expected
    )
    buzz_events.to_csv(output_dir / "buzz_event_predictions.csv", index=False)
    return predictions


def expected_bonus_points(part_probabilities):
    """Convert three part-correct probabilities into expected bonus points."""
    return 10 * part_probabilities.sum()


def save_bonus_predictions(output_dir, observations, probabilities, aggregates, synergy):
    """Attach fitted bonus-part predictions to the rows and save them.

    Writes 'bonus_part_predictions.csv' (per part) and 'team_predictions.csv'
    (expected points per bonus response, ten times the summed part
    probabilities). Returns the per-part predictions frame.
    """
    predictions = observations.copy()
    predictions["predicted_correct"] = tensor_values(probabilities)
    predictions["aggregate"] = tensor_values(aggregates)
    predictions["synergy_contribution"] = tensor_values(synergy)
    predictions.to_csv(output_dir / "bonus_part_predictions.csv", index=False)

    team_predictions = predictions.groupby("response_id", as_index=False).agg(
        game_id=("game_id", "first"),
        team_id=("team_id", "first"),
        total_points=("total_points", "first"),
        predicted_points=("predicted_correct", expected_bonus_points),
    )
    team_predictions.to_csv(output_dir / "team_predictions.csv", index=False)
    return predictions


def write_summary(output_dir, summary, posterior):
    """Append learned calibration parameters (if any) and write 'summary.json'.

    Each training script builds its own 'summary' dict of run configuration and
    dataset sizes, then calls this to record the optional Platt-scaling
    parameters ('correctness_scale'/'correctness_bias', present only when a run
    used '--calibrate-correctness') and write the file.
    """
    if "correctness_scale" in posterior:
        summary["correctness_scale"] = float(posterior["correctness_scale"].detach().cpu())
        summary["correctness_bias"] = float(posterior["correctness_bias"].detach().cpu())
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )


def save_synergy_outputs(output_dir, player_ids, observations, posterior, synergy_values):
    """Save optional detailed synergy profiles and observed teammate pairs."""
    # psi acts like an embedding: pair dot products matter, not the coordinates.
    profiles = {"player_id": player_ids}
    for dimension in range(posterior["psi"].shape[1]):
        profiles[f"psi_{dimension + 1}"] = tensor_values(
            posterior["psi"][:, dimension]
        )
    pd.DataFrame(profiles).to_csv(output_dir / "player_synergy_profiles.csv", index=False)

    psi = tensor_values(posterior["psi"])
    # Export only observed teammate pairs; all pairs would grow quadratically.
    player_index = {player_id: index for index, player_id in enumerate(player_ids)}
    observed_pairs = set()
    for roster in observations["player_ids"]:
        known = sorted(player_id for player_id in roster if player_id in player_index)
        observed_pairs.update(combinations(known, 2))

    pairs = []
    for player_1, player_2 in observed_pairs:
        left = player_index[player_1]
        right = player_index[player_2]
        pairs.append(
            {
                "player_1": player_1,
                "player_2": player_2,
                "synergy_score": float(np.dot(psi[left], psi[right])),
            }
        )
    pair_df = pd.DataFrame(
        pairs, columns=["player_1", "player_2", "synergy_score"]
    ).sort_values("synergy_score", ascending=False)
    pair_df.to_csv(output_dir / "pairwise_synergy_scores.csv", index=False)
    # All three part rows from one bonus response have the same roster and
    # therefore the same synergy contribution. Keep one row per response.
    team = observations[["response_id", "team_id", "player_ids"]].assign(
        synergy_contribution=synergy_values
    )
    team["roster_size"] = team["player_ids"].apply(len)
    team["pair_count"] = team["roster_size"] * (team["roster_size"] - 1) // 2
    team["synergy_per_pair"] = team["synergy_contribution"] / team[
        "pair_count"
    ].replace(0, np.nan)
    team.drop_duplicates("response_id").to_csv(
        output_dir / "team_synergy_contributions.csv", index=False
    )
