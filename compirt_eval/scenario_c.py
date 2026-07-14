"""Shared data and evaluation logic for paper Scenario C.

The functions in this module are deliberately model-agnostic.  They classify
saved bonus observations by training-time roster observability, audit lineup
and team-label provenance, and evaluate already-produced probabilities.  The
Pyro model that fits new test items lives in :mod:`scenario_c_model`.
"""

from __future__ import annotations

import json
import math
import re
from collections import defaultdict, deque
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error

from compirt_eval.metrics import classification_metrics


SCENARIOS = ("ALL", "C1", "C2", "C3", "C4")
PRIMARY_METRICS = (
    "auc",
    "log_loss",
    "ece",
    "accuracy",
    "exact_acc",
    "exact_score_accuracy",
    "per_bonus_points_mae",
    "ppb_mae",
)


def canonical_roster(player_ids) -> tuple[str, ...]:
    """Return an order-independent roster key, rejecting empty rosters."""
    roster = tuple(sorted({str(player_id) for player_id in player_ids if str(player_id)}))
    if not roster:
        raise ValueError("Scenario C cannot classify an empty lineup")
    return roster


def roster_key(player_ids) -> str:
    """Return the readable serialized form used in CSV artifacts."""
    return "|".join(canonical_roster(player_ids))


def normalize_team_label(value) -> str:
    """Normalize a human team label for diagnostic cross-event comparisons."""
    return " ".join(re.findall(r"[a-z0-9]+", str(value).casefold()))


def validate_historical_prediction_ids(no_synergy_path: Path, synergy_path: Path):
    """Return exact eligible observation/response IDs after branch validation."""
    left = pd.read_csv(no_synergy_path, usecols=["observation_id", "response_id"])
    right = pd.read_csv(synergy_path, usecols=["observation_id", "response_id"])
    left_pairs = set(
        zip(left["observation_id"].astype(str), left["response_id"].astype(str))
    )
    right_pairs = set(
        zip(right["observation_id"].astype(str), right["response_id"].astype(str))
    )
    left_ids = {observation_id for observation_id, _ in left_pairs}
    right_ids = {observation_id for observation_id, _ in right_pairs}
    if left_pairs != right_pairs:
        only_left = sorted(left_ids - right_ids)[:5]
        only_right = sorted(right_ids - left_ids)[:5]
        raise ValueError(
            "Historical Scenario C branches consumed different observation/response "
            "pairs: "
            f"no-synergy-only={only_left}, synergy-only={only_right}"
        )
    return left_ids, sorted({response_id for _, response_id in left_pairs})


def add_lineup_metadata(observations, tables, lineups):
    """Attach the authoritative ``LineupIndex`` record to every bonus-part row."""
    result = observations.copy()
    question_number = tables["bonuses"].set_index("bonus_id")["question_num"].to_dict()
    team_name = tables["teams"].set_index("team_id")["team_name"].to_dict()
    records = {}
    for response in result[["response_id", "game_id", "team_id", "bonus_id"]].drop_duplicates().itertuples(index=False):
        qnum = int(question_number[response.bonus_id])
        record = lineups.record_for(response.game_id, response.team_id, qnum)
        if record is None:
            raise ValueError(
                "Missing lineup metadata for "
                f"game={response.game_id}, team={response.team_id}, bonus={response.bonus_id}"
            )
        records[response.response_id] = record

    result["lineup_segment"] = result["response_id"].map(
        lambda value: records[value].segment
    )
    result["registered_roster_size"] = result["response_id"].map(
        lambda value: records[value].roster_size
    )
    result["inferred_lineup_size"] = result["response_id"].map(
        lambda value: records[value].lineup_size
    )
    result["distinct_game_buzzers"] = result["response_id"].map(
        lambda value: records[value].distinct_game_buzzers
    )
    result["lineup_confidence"] = result["response_id"].map(
        lambda value: records[value].confidence
    )
    result["lineup_resolution_rule"] = result["response_id"].map(
        lambda value: records[value].resolution_rule
    )
    result["lineup_has_game_buzz_evidence"] = result["distinct_game_buzzers"] > 0
    result["lineup_is_full_roster_fallback"] = (
        result["lineup_resolution_rule"] == "whole_game_no_evidence"
    )
    result["team_name"] = result["team_id"].map(team_name).fillna("")
    result["team_label_key"] = result["team_name"].map(normalize_team_label)
    result["roster_key"] = result["player_ids"].map(roster_key)
    result["roster_size"] = result["player_ids"].map(lambda value: len(canonical_roster(value)))
    return result


def _connected_components(players, pairs):
    adjacency = {player: set() for player in players}
    for left, right in pairs:
        adjacency.setdefault(left, set()).add(right)
        adjacency.setdefault(right, set()).add(left)
    component = {}
    sizes = []
    for player in adjacency:
        if player in component:
            continue
        index = len(sizes)
        queue = deque([player])
        size = 0
        while queue:
            current = queue.popleft()
            if current in component:
                continue
            component[current] = index
            size += 1
            queue.extend(adjacency[current] - component.keys())
        sizes.append(size)
    return component, sizes, adjacency


def build_training_context(training_parts, theta_known):
    """Summarize the exact Stage-2 observations used to define familiarity."""
    responses = training_parts.drop_duplicates("response_id").copy()
    responses["canonical_roster"] = responses["player_ids"].map(canonical_roster)
    rosters = set(responses["canonical_roster"])
    psi_informed = {player for roster in rosters for player in roster}
    pairs = {
        pair
        for roster in rosters
        for pair in combinations(roster, 2)
    }
    labels_by_player = defaultdict(set)
    training_labels = set()
    for row in responses.itertuples(index=False):
        label = row.team_label_key
        if label:
            training_labels.add(label)
            for player in row.canonical_roster:
                labels_by_player[player].add(label)
    component, component_sizes, adjacency = _connected_components(psi_informed, pairs)
    distinct_rosters_by_player = defaultdict(set)
    for roster in rosters:
        for player in roster:
            distinct_rosters_by_player[player].add(roster)
    return {
        "theta_known": set(map(str, theta_known)),
        "psi_informed": psi_informed,
        "rosters": rosters,
        "pairs": pairs,
        "training_labels": training_labels,
        "labels_by_player": labels_by_player,
        "component": component,
        "component_sizes": component_sizes,
        "adjacency": adjacency,
        "distinct_rosters_by_player": distinct_rosters_by_player,
    }


def classify_observations(test_parts, context):
    """Attach C1--C4 labels and provenance using one row per response internally."""
    responses = test_parts.drop_duplicates("response_id").copy()
    theta_known = context["theta_known"]
    psi_informed = context["psi_informed"]

    rows = []
    for row in responses.itertuples(index=False):
        roster = canonical_roster(row.player_ids)
        theta_count = sum(player in theta_known for player in roster)
        psi_count = sum(player in psi_informed for player in roster)
        size = len(roster)
        exact = roster in context["rosters"]
        if exact and theta_count == size:
            scenario = "C1"
        elif theta_count == size:
            scenario = "C2"
        elif theta_count:
            scenario = "C3"
        else:
            scenario = "C4"

        roster_pairs = list(combinations(roster, 2))
        seen_pairs = sum(pair in context["pairs"] for pair in roster_pairs)
        pair_fraction = seen_pairs / len(roster_pairs) if roster_pairs else math.nan
        label_sets = [context["labels_by_player"].get(player, set()) for player in roster]
        shared_labels = set.intersection(*map(set, label_sets)) if label_sets else set()
        component_ids = {
            context["component"][player]
            for player in roster
            if player in context["component"]
        }
        same_component = len(component_ids) == 1 and psi_count == size
        if scenario == "C2":
            if row.team_label_key and row.team_label_key in context["training_labels"]:
                provenance = "same_team_label_variant"
            else:
                provenance = "cross_team_recombination_candidate"
        else:
            provenance = "not_c2"

        rows.append(
            {
                "response_id": row.response_id,
                "scenario": scenario,
                "theta_known_member_count": theta_count,
                "theta_known_member_fraction": theta_count / size,
                "psi_informed_member_count": psi_count,
                "psi_informed_member_fraction": psi_count / size,
                "unknown_member_count": size - theta_count,
                "unknown_member_fraction": (size - theta_count) / size,
                "exact_training_roster": exact,
                "training_pair_fraction": pair_fraction,
                "all_members_shared_training_team_label": bool(shared_labels),
                "test_team_label_seen_in_training": bool(
                    row.team_label_key
                    and row.team_label_key in context["training_labels"]
                ),
                "all_members_same_training_component": same_component,
                "c2_provenance": provenance,
            }
        )
    labels = pd.DataFrame(rows)
    return test_parts.merge(labels, on="response_id", how="left", validate="many_to_one")


def composition_graph_summary(context, lineup_scope):
    """Return the paper's basic training co-roster graph diagnostics."""
    degrees = [len(neighbors) for neighbors in context["adjacency"].values()]
    sizes = context["component_sizes"]
    return {
        "lineup_scope": lineup_scope,
        "players": len(context["adjacency"]),
        "edges": len(context["pairs"]),
        "connected_components": len(sizes),
        "largest_component_fraction": max(sizes, default=0) / max(1, sum(sizes)),
        "mean_degree": float(np.mean(degrees)) if degrees else 0.0,
        "median_degree": float(np.median(degrees)) if degrees else 0.0,
        "players_on_multiple_rosters": sum(
            len(rosters) > 1 for rosters in context["distinct_rosters_by_player"].values()
        ),
    }


def _team_predictions(parts):
    """Collapse three part rows to one bonus response while retaining provenance."""
    return parts.groupby("response_id", as_index=False).agg(
        game_id=("game_id", "first"),
        team_id=("team_id", "first"),
        tournament_id=("tournament_id", "first"),
        tier=("tier", "first"),
        scenario=("scenario", "first"),
        total_points=("total_points", "first"),
        predicted_points=("predicted_correct", lambda values: float(10.0 * values.sum())),
    )


def scenario_metrics(all_parts, scenario):
    """Compute bonus metrics, excluding mixed-scenario game-teams from PPB only."""
    parts = all_parts if scenario == "ALL" else all_parts[all_parts["scenario"] == scenario]
    if parts.empty:
        return {metric: math.nan for metric in PRIMARY_METRICS} | {
            "parts": 0,
            "responses": 0,
            "games": 0,
            "game_teams": 0,
            "ppb_excluded_mixed_game_teams": 0,
        }
    metrics = classification_metrics(parts["correct"], parts["predicted_correct"])
    matches = (parts["predicted_correct"] >= 0.5) == parts["correct"].astype(bool)
    exact = pd.DataFrame({"response_id": parts["response_id"], "match": matches}).groupby(
        "response_id"
    ).agg(all_match=("match", "all"), count=("match", "size"))
    metrics["exact_acc"] = float((exact["all_match"] & (exact["count"] == 3)).mean())
    predicted_scores = parts.assign(
        _predicted_part_points=(parts["predicted_correct"] >= 0.5).astype(int) * 10
    ).groupby("response_id", as_index=False).agg(
        predicted_score=("_predicted_part_points", "sum"),
        observed_score=("total_points", "first"),
    )
    metrics["exact_score_accuracy"] = float(
        (predicted_scores["predicted_score"] == predicted_scores["observed_score"]).mean()
    )
    teams = _team_predictions(parts)
    metrics["per_bonus_points_mae"] = mean_absolute_error(
        teams["total_points"], teams["predicted_points"]
    )

    excluded = 0
    if scenario != "ALL":
        response_scenarios = all_parts.drop_duplicates("response_id")
        homogeneity = response_scenarios.groupby(["game_id", "team_id"])["scenario"].nunique()
        homogeneous_keys = set(homogeneity[homogeneity == 1].index)
        keep = [
            (game_id, team_id) in homogeneous_keys
            for game_id, team_id in zip(teams["game_id"], teams["team_id"])
        ]
        excluded = len(set(zip(teams["game_id"], teams["team_id"]))) - len(
            set(zip(teams.loc[keep, "game_id"], teams.loc[keep, "team_id"]))
        )
        teams = teams[keep]
    if teams.empty:
        metrics["ppb_mae"] = math.nan
    else:
        ppb = teams.groupby(["game_id", "team_id"], as_index=False).agg(
            observed=("total_points", "mean"), predicted=("predicted_points", "mean")
        )
        metrics["ppb_mae"] = mean_absolute_error(ppb["observed"], ppb["predicted"])
    metrics.update(
        {
            "parts": len(parts),
            "responses": parts["response_id"].nunique(),
            "games": parts["game_id"].nunique(),
            "game_teams": parts[["game_id", "team_id"]].drop_duplicates().shape[0],
            "ppb_excluded_mixed_game_teams": excluded,
        }
    )
    return metrics


def scenario_count_table(parts, lineup_scope):
    """Build the report's first, interpretation-critical sample-size table."""
    rows = []
    for scenario in SCENARIOS:
        selected = parts if scenario == "ALL" else parts[parts["scenario"] == scenario]
        responses = selected.drop_duplicates("response_id")
        rows.append(
            {
                "lineup_scope": lineup_scope,
                "scenario": scenario,
                "games": responses["game_id"].nunique(),
                "game_teams": responses[["game_id", "team_id"]].drop_duplicates().shape[0],
                "lineup_segments": responses[["game_id", "team_id", "lineup_segment"]].drop_duplicates().shape[0],
                "distinct_rosters": responses["roster_key"].nunique(),
                "responses": len(responses),
                "parts": len(selected),
                "roster_sizes": json.dumps(responses["roster_size"].value_counts().sort_index().to_dict()),
                "mean_theta_known_fraction": responses["theta_known_member_fraction"].mean(),
                "mean_psi_informed_fraction": responses["psi_informed_member_fraction"].mean(),
                "zero_evidence_responses": int((~responses["lineup_has_game_buzz_evidence"]).sum()),
                "full_roster_fallback_responses": int(responses["lineup_is_full_roster_fallback"].sum()),
                "cross_team_c2_responses": int((responses["c2_provenance"] == "cross_team_recombination_candidate").sum()),
                "cross_team_c2_games": responses.loc[
                    responses["c2_provenance"] == "cross_team_recombination_candidate",
                    "game_id",
                ].nunique(),
            }
        )
    return pd.DataFrame(rows)


def model_difference_rows(no_synergy, synergy, scenario):
    """Return paired point differences on identical Scenario C observations."""
    keys = ["observation_id", "scenario", "game_id", "tournament_id"]
    left_keys = no_synergy[keys].sort_values("observation_id").reset_index(drop=True)
    right_keys = synergy[keys].sort_values("observation_id").reset_index(drop=True)
    if not left_keys.equals(right_keys):
        raise ValueError(
            "Scenario C model branches do not contain identical prediction rows"
        )
    left = scenario_metrics(no_synergy, scenario)
    right = scenario_metrics(synergy, scenario)
    return [
        {
            "scenario": scenario,
            "metric": metric,
            "no_synergy": left.get(metric, math.nan),
            "synergy": right.get(metric, math.nan),
            "synergy_minus_no_synergy": right.get(metric, math.nan)
            - left.get(metric, math.nan),
        }
        for metric in PRIMARY_METRICS
    ]
