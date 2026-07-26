"""Resolve stable, readable entity IDs from the raw source database rows.

The source SQLite database identifies teams, players, and bonus-part scores
with auto-increment integer primary keys that are meaningless across
tournaments and occasionally collide or duplicate. Each function here
reconciles a batch of raw source rows and returns:

* a mapping from source integer ID to the readable string ID used in the
  output tables, and
* a list of "repair" records describing any collision it had to resolve, so
  'build_records' can surface them in the build report for manual review.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Iterable


def assign_unique_team_ids(
    team_rows: Iterable[dict[str, Any]],
) -> tuple[dict[int, str], list[dict[str, Any]]]:
    """Assign readable 'tournament::team-slug' IDs, disambiguating collisions.

    Team slugs are normally unique within a tournament, so the readable ID is
    just 'f"{tournament_slug}::{slug}"'. When two source team rows share
    both fields (a re-registration or data-entry duplicate), each colliding
    row instead gets a '::db-<source_id>' suffix appended so IDs stay unique,
    and the collision is recorded for the build report.
    """
    rows = list(team_rows)
    by_base: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_base[f"{row['tournament_slug']}::{row['slug']}"].append(row)

    team_ids: dict[int, str] = {}
    collisions: list[dict[str, Any]] = []
    for base, group in sorted(by_base.items()):
        if len(group) == 1:
            team_ids[int(group[0]["id"])] = base
            continue
        collision = {"base_team_id": base, "source_team_ids": sorted(int(row["id"]) for row in group)}
        collisions.append(collision)
        for row in group:
            team_ids[int(row["id"])] = f"{base}::db-{row['id']}"
    return team_ids, collisions


def group_players_by_slug(
    player_rows: Iterable[dict[str, Any]],
) -> tuple[dict[int, str], list[dict[str, Any]]]:
    """Group source player rows using their raw player slug as the player ID.

    A player has one source row per team they were rostered on, so the same
    person can appear many times across tournaments/years. This collapses
    every row sharing a raw 'slug' into a single 'players' record (name
    taken from their earliest appearance, source refs listing every
    team/tournament they were seen on), and returns a source-row-ID -> player
    ID map so other tables can reference the collapsed player.

    Note: slug collisions between two different real people are not resolved
    here -- that risk is instead surfaced separately in 'build_records' via
    the identity review report's slug/name-conflict warnings.
    """
    assigned: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in player_rows:
        assigned[str(row["slug"])].append(row)

    player_id_by_db_id: dict[int, str] = {}
    records: list[dict[str, Any]] = []
    for player_id, group in sorted(assigned.items()):
        # Earliest appearance (by tournament start date) sets the display
        # name and first-seen tournament; ties break deterministically on
        # tournament/team slug and finally source row ID.
        ordered = sorted(
            group,
            key=lambda row: (
                row["start_date"],
                row["tournament_slug"],
                row["team_slug"],
                int(row["id"]),
            ),
        )
        for row in ordered:
            player_id_by_db_id[int(row["id"])] = player_id
        records.append(
            {
                "player_id": player_id,
                "name": ordered[0]["name"],
                "first_seen_tournament": ordered[0]["tournament_slug"],
                "tournaments_played": list(dict.fromkeys(row["tournament_slug"] for row in ordered)),
                "source_slugs": sorted(set(row["slug"] for row in ordered)),
                "source_player_refs": [
                    f"{row['tournament_slug']}::{row['team_slug']}::{row['slug']}" for row in ordered
                ],
                # Internal field (stripped before writing): every year this
                # player appears in, used to place them in year splits even
                # though a player has no single "_year" of their own.
                "_years": sorted(set(int(row["start_date"][:4]) for row in ordered)),
            }
        )
    return player_id_by_db_id, records


def deduplicate_bonus_parts(
    rows: Iterable[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Keep one score per (game, team, bonus part), preferring the latest entry.

    The source 'bonus_part_direct' table occasionally has more than one
    scoring row for the same team's attempt at the same bonus part -- usually
    a moderator's score correction re-entered later. The row with the highest
    source ID (assumed most recently inserted) is kept; every other row in
    that group is dropped and recorded as a repair, flagging whether the
    dropped scores actually disagreed with the kept one.
    """
    grouped: dict[tuple[int, int, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(int(row["game_id"]), int(row["team_id"]), int(row["bonus_part_id"]))].append(row)

    selected: list[dict[str, Any]] = []
    repairs: list[dict[str, Any]] = []
    for key, group in sorted(grouped.items()):
        ordered = sorted(group, key=lambda row: int(row["id"]))
        selected.append(ordered[-1])
        if len(ordered) > 1:
            repairs.append(
                {
                    "type": "duplicate_bonus_part_score",
                    "game_db_id": key[0],
                    "team_db_id": key[1],
                    "bonus_part_db_id": key[2],
                    "source_row_ids": [int(row["id"]) for row in ordered],
                    "source_values": [int(row["value"]) for row in ordered],
                    "selected_row_id": int(ordered[-1]["id"]),
                    "selected_value": int(ordered[-1]["value"]),
                }
            )
    return selected, repairs


def order_buzzes(rows: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Order one tossup event's buzzes by token position, then source ID.

    Token position is the primary ordering (earlier buzz = happened first);
    source ID is only a tiebreaker for same-position rows, keeping the order
    deterministic when the source data doesn't otherwise distinguish them.
    """
    return sorted(rows, key=lambda row: (int(row["buzz_position"]), int(row["id"])))
