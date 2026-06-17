"""Output helpers shared by the CompIRT training scripts.

These functions only convert fitted tensors to arrays and write result files
(CSV summaries and the loss plot). Model definitions, the SVI training loop, and
the per-script ``run_experiment`` orchestration deliberately live in the
individual training scripts, not here.
"""

from __future__ import annotations

from itertools import combinations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def tensor_values(tensor):
    """Return a tensor as a NumPy array for CSV output."""
    return tensor.detach().cpu().numpy()


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


def save_player_rankings(output_dir, predictions):
    """Save a descriptive ranking based on fitted correctness of observed buzzes.

    This is not a pure ranking of theta: it summarizes the probabilities for
    the particular tossups and buzz positions each player actually encountered.
    """
    ranking = (
        predictions[predictions["z"] == "BUZZ"]
        .groupby("player_id", as_index=False)
        .agg(
            buzzes=("y", "size"),
            observed_correctness=("y", "mean"),
            fitted_correctness=("predicted_correct", "mean"),
            average_relative_position=("relative_position", "mean"),
        )
        .sort_values(["fitted_correctness", "buzzes"], ascending=False)
    )
    ranking.to_csv(output_dir / "top_players.csv", index=False)


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
