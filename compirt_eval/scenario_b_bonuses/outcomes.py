"""Team bonus-only PPG and game margins, conditional on recorded bonuses."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def bonus_team_outcomes(parts, official_games, recorded_responses):
    """Pool complete games before scoring team PPG and tournament rankings.

    Expected points are ten times summed part probabilities. Game metadata
    supplies both teams and the denominator, including zero-bonus games.
    Return scalar metrics, team-game totals, team PPG, tournament metrics,
    and one signed bonus margin per game.
    """
    if official_games["game_id"].duplicated().any():
        raise ValueError("Duplicate games; pool each held-out game only once")
    if parts.duplicated(["response_id", "part_index"]).any():
        raise ValueError("Duplicate bonus parts; pool each held-out prediction only once")
    if not np.isfinite(parts["predicted_correct"]).all() or not parts["predicted_correct"].between(0, 1).all():
        raise ValueError("Invalid bonus probabilities")
    if not parts["correct"].isin([0, 1]).all():
        raise ValueError("Invalid bonus labels")

    pair_rows = []
    for game in official_games.itertuples(index=False):
        teams = sorted(set(game.team_ids))
        if len(teams) != 2:
            raise ValueError(f"Expected two distinct teams for game {game.game_id}")
        pair_rows.append({"tournament_id": game.tournament_id, "game_id": game.game_id,
                          "team_a": teams[0], "team_b": teams[1]})
    pairs = pd.DataFrame(pair_rows, columns=["tournament_id", "game_id", "team_a", "team_b"])
    keys = ["tournament_id", "game_id", "team_id"]
    participants = pd.concat([
        pairs[["tournament_id", "game_id", side]].rename(columns={side: "team_id"})
        for side in ("team_a", "team_b")
    ], ignore_index=True)
    game_ids = set(official_games["game_id"])
    if not set(parts["game_id"]) <= game_ids:
        raise ValueError("Bonus predictions contain games absent from game metadata")
    identities = parts[keys].drop_duplicates().merge(participants, on=keys, how="left", indicator=True)
    if identities["_merge"].ne("both").any():
        raise ValueError("Bonus prediction team or tournament disagrees with game metadata")

    recorded = recorded_responses[recorded_responses["game_id"].isin(game_ids)]
    official = recorded.set_index("response_id")
    if not official.index.is_unique:
        raise ValueError("Duplicate recorded bonus responses")
    expected = recorded.groupby("game_id")["response_id"].agg(set).to_dict()
    actual = parts.groupby("game_id")["response_id"].agg(set).to_dict()
    incomplete = {game for game in game_ids if expected.get(game, set()) != actual.get(game, set())}
    complete = parts.groupby("response_id")["part_index"].agg(lambda values: set(values) == {0, 1, 2})
    incomplete.update(parts.loc[~parts["response_id"].map(complete).astype(bool), "game_id"])
    responses = parts.groupby("response_id", as_index=False).agg(
        tournament_id=("tournament_id", "first"), game_id=("game_id", "first"),
        team_id=("team_id", "first"), observed_bonus_points=("correct", "sum"),
        predicted_bonus_points=("predicted_correct", "sum"),
    )
    points = ["observed_bonus_points", "predicted_bonus_points"]
    responses[points] *= 10
    # A response cannot mix identities across its parts, even when both teams
    # happen to be valid participants in the game.
    mixed = parts.groupby("response_id")[keys].nunique().gt(1).any(axis=1)
    if mixed.any():
        raise ValueError("Inconsistent bonus response identity across parts")
    responses = responses[~responses["game_id"].isin(incomplete)]
    source = official.reindex(responses["response_id"])
    if (responses["game_id"].to_numpy() != source["game_id"].to_numpy()).any() or (
        responses["team_id"].to_numpy() != source["team_id"].to_numpy()
    ).any() or (responses["observed_bonus_points"].to_numpy() != source["total_points"].to_numpy()).any():
        raise ValueError("Bonus prediction disagrees with recorded response identity or score")

    participants = participants[~participants["game_id"].isin(incomplete)]
    games = participants.merge(responses.groupby(keys, as_index=False)[points].sum(),
                               on=keys, how="left", validate="one_to_one")
    games[points] = games[points].fillna(0.0)
    leaderboard = games.groupby(["tournament_id", "team_id"], as_index=False).agg(
        games=("game_id", "nunique"), observed_bonus_points=("observed_bonus_points", "sum"),
        predicted_bonus_points=("predicted_bonus_points", "sum"),
    )
    leaderboard["observed_bonus_ppg"] = leaderboard["observed_bonus_points"] / leaderboard["games"]
    leaderboard["predicted_bonus_ppg"] = leaderboard["predicted_bonus_points"] / leaderboard["games"]
    leaderboard["absolute_error"] = (leaderboard["predicted_bonus_ppg"] - leaderboard["observed_bonus_ppg"]).abs()

    margins = pairs[~pairs["game_id"].isin(incomplete)].copy()
    for side in ("a", "b"):
        margins = margins.merge(
            games.rename(columns={"team_id": f"team_{side}", **{p: f"{p}_{side}" for p in points}}),
            on=["tournament_id", "game_id", f"team_{side}"], validate="one_to_one",
        )
    for kind in ("observed", "predicted"):
        margins[f"{kind}_bonus_margin"] = margins[f"{kind}_bonus_points_a"] - margins[f"{kind}_bonus_points_b"]
    margins["absolute_bonus_margin_error"] = (margins["predicted_bonus_margin"] - margins["observed_bonus_margin"]).abs()

    rows = []
    for tournament_id, group in leaderboard.groupby("tournament_id", sort=True):
        observed, predicted = group["observed_bonus_ppg"], group["predicted_bonus_ppg"]
        rho = observed.corr(predicted, method="spearman") if observed.nunique() > 1 and predicted.nunique() > 1 else np.nan
        tournament_games = margins[margins["tournament_id"] == tournament_id]
        rows.append({"tournament_id": tournament_id, "teams": len(group),
                     "games": len(tournament_games),
                     "bonus_ppg_mae": float(group["absolute_error"].mean()),
                     "bonus_ppg_spearman": rho,
                     "bonus_game_margin_mae": float(tournament_games["absolute_bonus_margin_error"].mean())})
    tournaments = pd.DataFrame(rows, columns=["tournament_id", "teams", "games", "bonus_ppg_mae",
                                              "bonus_ppg_spearman", "bonus_game_margin_mae"])
    summary = {
        "tournament_team_bonus_ppg_mae": float(tournaments["bonus_ppg_mae"].mean()),
        "tournament_team_bonus_ppg_spearman": float(tournaments["bonus_ppg_spearman"].mean()),
        "bonus_ppg_tournaments": len(tournaments),
        "bonus_ppg_spearman_tournaments": int(tournaments["bonus_ppg_spearman"].notna().sum()),
        "bonus_ppg_incomplete_games": len(incomplete),
        "bonus_ppg_games": len(margins),
        "bonus_game_margin_mae": float(margins["absolute_bonus_margin_error"].mean()),
        "bonus_game_margin_mae_games": len(margins),
    }
    return summary, games, leaderboard, tournaments, margins


def write_bonus_outcomes(parts, tables, output_dir):
    """Write team PPG and margin artifacts for the games selected by the caller."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    summary, games, leaderboard, tournaments, margins = bonus_team_outcomes(
        parts, tables["games"], tables["bonus_responses"]
    )
    for name, frame in (("bonus_team_game_predictions", games),
                        ("bonus_team_ppg_leaderboard", leaderboard),
                        ("bonus_team_ranking_metrics", tournaments),
                        ("bonus_game_margin_predictions", margins)):
        frame.to_csv(output_dir / f"{name}.csv", index=False)
    return summary
