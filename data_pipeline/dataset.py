"""Build the linked quizbowl IRT dataset from the raw SQLite export.

Start reading at 'build_dataset_directory' -- the single public entry point
used by 'build.py'. It wraps the two steps below in an all-or-nothing write:

1. 'build_records' reads the raw SQLite database (schema documented in
   'data_pipeline.schema') and reshapes it into the nine linked in-memory
   tables described there, resolving readable IDs ('data_pipeline.identity')
   and cleaning question text ('data_pipeline.text_cleaning') along the way.
2. 'write_datasets' / 'write_response_matrix' save those tables to disk as
   HuggingFace 'DatasetDict's plus a wide player-by-tossup CSV matrix.

The trickiest part of step 1 is that the source database only records the
single first buzz per tossup and the *final* per-team bonus score, but the
output tables need to look like a complete play-by-play: every rostered
player gets a correctness label for every tossup their team saw
('irt_responses'), and every buzz/bonus response is annotated with the
score *at that moment* ('team_score' / 'opponent_score') rather than only
the final score. Both are reconstructed here by walking each game's events in
order.
"""

from __future__ import annotations

import json
import re
import shutil
import sqlite3
import uuid
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
from datasets import Dataset, DatasetDict

from data_pipeline.identity import (
    assign_unique_team_ids,
    deduplicate_bonus_parts,
    group_players_by_slug,
    order_buzzes,
)
from data_pipeline.schema import REQUIRED_TABLES, TABLE_FEATURES
from data_pipeline.text_cleaning import sanitize_html, sentence_boundaries, strip_leading_moderator_note


@dataclass
class BuiltRecords:
    """In-memory result of 'build_records', before anything hits disk."""

    # Table name -> list of row dicts. Rows still carry private "_"-prefixed
    # fields (e.g. "_year") used only to build year splits; see _public_record.
    tables: dict[str, list[dict[str, Any]]]
    # Row counts, source integrity check, and any repairs build_records made
    # (team ID collisions, duplicate bonus-part scores) -- written alongside
    # the dataset as build_report.json.
    build_report: dict[str, Any]
    # Slug/name conflicts and other identity ambiguities worth a human's
    # attention, but not severe enough to fail the build outright.
    identity_report: dict[str, Any]


def _dict_rows(connection: sqlite3.Connection, query: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    """Run a query and return each row as a plain dict (requires Row factory set)."""
    return [dict(row) for row in connection.execute(query, params)]


def preflight_database(db_path: Path) -> dict[str, Any]:
    """Check the source database is readable and has the tables the build needs.

    Raises if the SQLite integrity check fails or a required table is
    missing, so a corrupt or partial export fails fast instead of producing a
    silently incomplete dataset.
    """
    if not db_path.is_file():
        raise FileNotFoundError(f"Database not found: {db_path}")
    connection = sqlite3.connect(f"file:{db_path.resolve().as_posix()}?mode=ro", uri=True)
    try:
        integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
        if integrity != "ok":
            raise ValueError(f"SQLite integrity check failed: {integrity}")
        present = {
            row[0]
            for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")
        }
        missing = sorted(REQUIRED_TABLES - present)
        if missing:
            raise ValueError(f"Database is missing required tables: {', '.join(missing)}")
        counts = {
            table: int(connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])
            for table in sorted(REQUIRED_TABLES)
        }
        return {"integrity_check": integrity, "source_table_counts": counts}
    finally:
        connection.close()


def build_records(db_path: Path) -> BuiltRecords:
    """Read the source database and build the nine linked output tables.

    This function is long because it mirrors the source schema's join
    structure one table at a time, in dependency order (tournaments -> teams
    -> players -> tossups/bonuses -> games -> buzzes/bonus responses ->
    derived irt_responses), reusing each stage's readable IDs and lookups in
    the next. See the module docstring for why buzzes/responses need a
    running score reconstruction rather than a single query.
    """
    preflight = preflight_database(db_path)
    connection = sqlite3.connect(f"file:{db_path.resolve().as_posix()}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        # --- Tournaments -----------------------------------------------
        tournament_rows = _dict_rows(
            connection,
            """
            SELECT t.*, qs.slug AS event_slug, qse.slug AS edition_slug,
                   qs.name AS event_name,
                   COUNT(DISTINCT r.packet_id) AS num_packets
            FROM tournament t
            JOIN question_set_edition qse ON qse.id = t.question_set_edition_id
            JOIN question_set qs ON qs.id = qse.question_set_id
            LEFT JOIN round r ON r.tournament_id = t.id
            GROUP BY t.id
            ORDER BY t.id
            """,
        )
        tournaments = [
            {
                "tournament_id": row["slug"],
                "name": row["name"] or "",
                # e.g. "acf-regionals" -> tier "regionals"; the event slug's
                # last hyphen-delimited segment is the difficulty tier.
                "tier": str(row["event_slug"]).split("-")[-1],
                "year": int(str(row["start_date"])[:4]),
                "num_packets": int(row["num_packets"]),
                # Tossups/bonuses are shared across a question set's mirror
                # tournaments, so they're keyed by this event+edition ID
                # rather than by any single tournament_id.
                "question_set_event_id": f"{row['event_slug']}::{row['edition_slug']}",
                "level": row["level"] or "",
                "location": row["location"] or "",
                "start_date": str(row["start_date"]),
                "end_date": str(row["end_date"]),
                "_year": int(str(row["start_date"])[:4]),
            }
            for row in tournament_rows
        ]

        # --- Teams -------------------------------------------------------
        team_rows = _dict_rows(
            connection,
            """
            SELECT tm.*, t.slug AS tournament_slug, t.start_date
            FROM team tm JOIN tournament t ON t.id = tm.tournament_id
            ORDER BY tm.id
            """,
        )
        team_id_by_db_id, team_collisions = assign_unique_team_ids(team_rows)

        # --- Players -------------------------------------------------------
        player_rows = _dict_rows(
            connection,
            """
            SELECT p.*, tm.slug AS team_slug, t.slug AS tournament_slug,
                   t.start_date
            FROM player p
            JOIN team tm ON tm.id = p.team_id
            JOIN tournament t ON t.id = tm.tournament_id
            ORDER BY p.id
            """,
        )
        player_id_by_db_id, players = group_players_by_slug(player_rows)
        # Roster membership is derived from the player rows themselves
        # (each carries the team it was rostered on), deduplicated per team.
        roster_by_team_db_id: dict[int, list[str]] = defaultdict(list)
        for row in player_rows:
            roster_by_team_db_id[int(row["team_id"])].append(player_id_by_db_id[int(row["id"])])
        teams = [
            {
                "team_id": team_id_by_db_id[int(row["id"])],
                "tournament_id": row["tournament_slug"],
                "team_name": row["name"] or "",
                "player_ids": sorted(set(roster_by_team_db_id[int(row["id"])])),
                "_year": int(str(row["start_date"])[:4]),
            }
            for row in team_rows
        ]

        # --- Tossups -------------------------------------------------------
        tossup_rows = _dict_rows(
            connection,
            """
            SELECT pq.packet_id, pq.question_number, qse.date AS event_date,
                   qs.slug AS event_slug, qse.slug AS edition_slug,
                   q.category, q.subcategory,
                   tu.id AS tossup_db_id, tu.question, tu.answer
            FROM packet_question pq
            JOIN packet p ON p.id = pq.packet_id
            JOIN question_set_edition qse ON qse.id = p.question_set_edition_id
            JOIN question_set qs ON qs.id = qse.question_set_id
            JOIN question q ON q.id = pq.question_id
            JOIN tossup tu ON tu.question_id = q.id
            ORDER BY pq.packet_id, pq.question_number
            """,
        )
        # Two lookups are built from this query's rows:
        # - tossup_entity_by_db_id: one clean tossup record per underlying
        #   tossup, built once even if it's reused across packet positions.
        # - tossup_lookup: keyed by (packet, source tossup db id), used below
        #   to resolve each buzz's tossup without re-parsing question text.
        tossup_lookup: dict[tuple[int, int], dict[str, Any]] = {}
        tossup_entity_by_db_id: dict[int, dict[str, Any]] = {}
        tossups: list[dict[str, Any]] = []
        moderator_note_count = 0
        for row in tossup_rows:
            tossup_db_id = int(row["tossup_db_id"])
            if tossup_db_id not in tossup_entity_by_db_id:
                clean_question, moderator_offset = strip_leading_moderator_note(row["question"])
                tokens = clean_question.split()
                event_id = f"{row['event_slug']}::{row['edition_slug']}"
                tossup_id = f"{event_id}::p{row['packet_id']}::q{row['question_number']}"
                entity = {
                    "tossup_id": tossup_id,
                    "question_set_event_id": event_id,
                    "packet": int(row["packet_id"]),
                    "question_num": int(row["question_number"]),
                    "category": row["category"] or "",
                    "subcategory": row["subcategory"] or "",
                    "answer": row["answer"] or "",
                    "tokens": tokens,
                    "sentence_boundaries": sentence_boundaries(tokens),
                    "question": clean_question,
                    "_year": int(str(row["event_date"])[:4]),
                    # Kept so buzz token positions (recorded against the raw,
                    # note-included text) can be shifted back into the
                    # cleaned token stream; see the buzz loop below.
                    "_moderator_offset": moderator_offset,
                }
                tossup_entity_by_db_id[tossup_db_id] = entity
                tossups.append(entity)
                moderator_note_count += moderator_offset > 0
            entity = tossup_entity_by_db_id[tossup_db_id]
            tossup_lookup[(int(row["packet_id"]), int(row["tossup_db_id"]))] = {
                "tossup_id": entity["tossup_id"],
                "question_number": int(row["question_number"]),
                "moderator_offset": entity["_moderator_offset"],
                "num_tokens_total": len(entity["tokens"]),
            }

        # --- Bonuses -------------------------------------------------------
        bonus_rows = _dict_rows(
            connection,
            """
            SELECT pq.packet_id, pq.question_number, qse.date AS event_date,
                   qs.slug AS event_slug, qse.slug AS edition_slug,
                   q.category, q.subcategory,
                   b.id AS bonus_db_id, b.leadin_sanitized,
                   bp.part_number, bp.part_sanitized, bp.answer, bp.difficulty_modifier
            FROM packet_question pq
            JOIN packet p ON p.id = pq.packet_id
            JOIN question_set_edition qse ON qse.id = p.question_set_edition_id
            JOIN question_set qs ON qs.id = qse.question_set_id
            JOIN question q ON q.id = pq.question_id
            JOIN bonus b ON b.question_id = q.id
            JOIN bonus_part bp ON bp.bonus_id = b.id
            ORDER BY pq.packet_id, pq.question_number, bp.part_number
            """,
        )
        # This query returns one row per bonus *part* (three per bonus), so
        # rows are grouped back into one bonus record with a 3-element parts list.
        bonus_grouped: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
        for row in bonus_rows:
            bonus_grouped[(int(row["packet_id"]), int(row["bonus_db_id"]))].append(row)
        bonus_lookup: dict[tuple[int, int], dict[str, Any]] = {}
        bonuses: list[dict[str, Any]] = []
        difficulty_map = {"e": "easy", "m": "medium", "h": "hard"}
        for key, group in sorted(bonus_grouped.items()):
            first = group[0]
            event_id = f"{first['event_slug']}::{first['edition_slug']}"
            bonus_id = f"{event_id}::p{first['packet_id']}::b{first['question_number']}"
            parts = [
                {
                    "text": sanitize_html(row["part_sanitized"]),
                    "answer": row["answer"] or "",
                    "difficulty": difficulty_map.get(
                        str(row["difficulty_modifier"] or "").lower(),
                        str(row["difficulty_modifier"] or ""),
                    ),
                }
                for row in sorted(group, key=lambda row: int(row["part_number"]))
            ]
            bonuses.append(
                {
                    "bonus_id": bonus_id,
                    "question_set_event_id": event_id,
                    "packet": int(first["packet_id"]),
                    "question_num": int(first["question_number"]),
                    "category": first["category"] or "",
                    "subcategory": first["subcategory"] or "",
                    "leadin": sanitize_html(first["leadin_sanitized"]),
                    "parts": parts,
                    "_year": int(str(first["event_date"])[:4]),
                }
            )
            bonus_lookup[key] = {
                "bonus_id": bonus_id,
                "question_number": int(first["question_number"]),
            }

        # --- Games -------------------------------------------------------
        game_rows = _dict_rows(
            connection,
            """
            SELECT g.*, r.number AS round_number, r.packet_id, r.tournament_id,
                   t.slug AS tournament_slug, t.start_date
            FROM game g
            JOIN round r ON r.id = g.round_id
            JOIN tournament t ON t.id = r.tournament_id
            ORDER BY g.id
            """,
        )
        # game_info stays keyed by source db ID (not yet the readable
        # game_id) because buzzes/bonus responses below join against it by
        # db ID first, then look up team_ids/readable game_id from it.
        game_info: dict[int, dict[str, Any]] = {}
        for row in game_rows:
            game_info[int(row["id"])] = {
                **row,
                "game_id": f"{row['tournament_slug']}::game-{row['id']}",
                "team_ids": [
                    team_id_by_db_id[int(row["team_one_id"])],
                    team_id_by_db_id[int(row["team_two_id"])],
                ],
                "year": int(str(row["start_date"])[:4]),
            }

        # --- Buzzes (joined to their tossup, grouped by game) --------------
        buzz_rows = _dict_rows(connection, "SELECT * FROM buzz ORDER BY game_id, buzz_position, id")
        buzzes_by_game: dict[int, list[dict[str, Any]]] = defaultdict(list)
        beyond_token_count = 0
        for row in buzz_rows:
            game = game_info[int(row["game_id"])]
            tossup = tossup_lookup[(int(game["packet_id"]), int(row["tossup_id"]))]
            buzzes_by_game[int(row["game_id"])].append(
                {
                    **row,
                    "question_number": int(tossup["question_number"]),
                    "tossup_entity": tossup,
                }
            )
        player_source_by_id = {int(row["id"]): row for row in player_rows}

        # --- Bonus responses (joined, deduplicated, grouped by game) -------
        direct_rows = _dict_rows(
            connection,
            """
            SELECT d.*, bp.bonus_id, bp.part_number
            FROM bonus_part_direct d
            JOIN bonus_part bp ON bp.id = d.bonus_part_id
            ORDER BY d.game_id, d.id
            """,
        )
        selected_direct, bonus_repairs = deduplicate_bonus_parts(direct_rows)
        # Reassembled into one row per (game, team, bonus): 3 per-part score
        # rows become the 'parts' list a single bonus_responses row needs.
        responses_by_game: dict[int, dict[tuple[int, int], list[dict[str, Any]]]] = defaultdict(
            lambda: defaultdict(list)
        )
        for row in selected_direct:
            responses_by_game[int(row["game_id"])][
                (int(row["team_id"]), int(row["bonus_id"]))
            ].append(row)

        # --- Replay each game's events in order to reconstruct running
        # score and derive tossup_buzzes / bonus_responses / games ----------
        #
        # The source database stores each buzz's/response's *value*, not the
        # score at that point in the game, and only the game's *final*
        # score. So each game's tossup and bonus events (grouped by the
        # packet question number they belong to) are replayed in order,
        # accumulating team_score/opponent_score as we go. The same replayed
        # totals also reconstruct each game's final_scores, which is checked
        # against the source in validate.py.
        tossup_buzzes: list[dict[str, Any]] = []
        bonus_responses: list[dict[str, Any]] = []
        games: list[dict[str, Any]] = []
        missing_earners: list[dict[str, Any]] = []
        for game_db_id, game in sorted(game_info.items()):
            scores = {int(game["team_one_id"]): 0, int(game["team_two_id"]): 0}
            events_by_question: dict[int, dict[str, Any]] = defaultdict(
                lambda: {"buzzes": [], "responses": []}
            )
            for buzz in buzzes_by_game.get(game_db_id, []):
                events_by_question[int(buzz["question_number"])]["buzzes"].append(buzz)
            for (team_db_id, bonus_db_id), part_rows in responses_by_game.get(game_db_id, {}).items():
                bonus = bonus_lookup[(int(game["packet_id"]), bonus_db_id)]
                events_by_question[int(bonus["question_number"])]["responses"].append(
                    {
                        "team_db_id": team_db_id,
                        "bonus_db_id": bonus_db_id,
                        "bonus_id": bonus["bonus_id"],
                        "parts": sorted(part_rows, key=lambda row: int(row["part_number"])),
                    }
                )

            for question_number in sorted(events_by_question):
                event = events_by_question[question_number]
                # Players who scored a positive-value buzz on this question,
                # by team -- used just below to attribute bonus points to
                # whichever single player earned the team's bonus chance.
                positive_by_team: dict[int, list[str]] = defaultdict(list)
                for buzz in order_buzzes(event["buzzes"]):
                    source_player = player_source_by_id[int(buzz["player_id"])]
                    team_db_id = int(source_player["team_id"])
                    opponent_db_id = (
                        int(game["team_two_id"]) if team_db_id == int(game["team_one_id"]) else int(game["team_one_id"])
                    )
                    tossup_entity = buzz["tossup_entity"]
                    # Buzz positions are recorded against the raw (possibly
                    # moderator-note-prefixed) token stream; shift back into
                    # the cleaned token stream the tossup record actually
                    # stores, clamped to zero so a buzz inside a stripped
                    # note doesn't go negative.
                    token_position = max(0, int(buzz["buzz_position"]) - int(tossup_entity["moderator_offset"]))
                    beyond_token_count += token_position > int(tossup_entity["num_tokens_total"])
                    player_id = player_id_by_db_id[int(buzz["player_id"])]
                    tossup_buzzes.append(
                        {
                            "buzz_id": f"{game['game_id']}::buzz-{buzz['id']}",
                            "tossup_id": tossup_entity["tossup_id"],
                            "game_id": game["game_id"],
                            "player_id": player_id,
                            "team_id": team_id_by_db_id[team_db_id],
                            "token_position": token_position,
                            "num_tokens_total": int(tossup_entity["num_tokens_total"]),
                            "correct": int(buzz["value"]) > 0,
                            # Score *before* this buzz's points are applied,
                            # i.e. the score the player actually buzzed at.
                            "team_score": scores[team_db_id],
                            "opponent_score": scores[opponent_db_id],
                            "question_number_in_game": question_number,
                            "value": int(buzz["value"]),
                            "_year": game["year"],
                        }
                    )
                    scores[team_db_id] += int(buzz["value"])
                    if int(buzz["value"]) > 0:
                        positive_by_team[team_db_id].append(player_id)

                for response in sorted(
                    event["responses"],
                    key=lambda row: (
                        team_id_by_db_id[int(row["team_db_id"])],
                        row["bonus_id"],
                    ),
                ):
                    team_db_id = int(response["team_db_id"])
                    opponent_db_id = (
                        int(game["team_two_id"]) if team_db_id == int(game["team_one_id"]) else int(game["team_one_id"])
                    )
                    # A bonus is only attributed to a single earning player
                    # when exactly one teammate got the tossup right; ties
                    # (multiple positive buzzes, which shouldn't normally
                    # happen within a team) are left unattributed and flagged.
                    earners = positive_by_team.get(team_db_id, [])
                    earning_player_id = earners[0] if len(earners) == 1 else ""
                    if not earning_player_id:
                        missing_earners.append(
                            {
                                "type": "missing_earning_player",
                                "game_id": game["game_id"],
                                "team_id": team_id_by_db_id[team_db_id],
                                "bonus_id": response["bonus_id"],
                                "question_number_in_game": question_number,
                            }
                        )
                    parts_correct = [int(row["value"]) > 0 for row in response["parts"]]
                    total_points = sum(int(row["value"]) for row in response["parts"])
                    bonus_responses.append(
                        {
                            "response_id": f"{game['game_id']}::{team_id_by_db_id[team_db_id]}::{response['bonus_id']}",
                            "bonus_id": response["bonus_id"],
                            "game_id": game["game_id"],
                            "team_id": team_id_by_db_id[team_db_id],
                            "earning_player_id": earning_player_id,
                            "parts_correct": parts_correct,
                            "total_points": total_points,
                            # Score before this bonus attempt's points, mirroring
                            # tossup_buzzes' team_score/opponent_score semantics.
                            "team_score": scores[team_db_id],
                            "opponent_score": scores[opponent_db_id],
                            "question_number_in_game": question_number,
                            "_year": game["year"],
                        }
                    )
                    scores[team_db_id] += total_points

            games.append(
                {
                    "game_id": game["game_id"],
                    "tournament_id": game["tournament_slug"],
                    "round": f"round{game['round_number']}",
                    "packet_id": int(game["packet_id"]),
                    "team_ids": game["team_ids"],
                    # Final scores come from the same replay, so they are
                    # guaranteed consistent with every buzz/response's
                    # running score above (checked independently in validate.py).
                    "final_scores": [
                        scores[int(game["team_one_id"])],
                        scores[int(game["team_two_id"])],
                    ],
                    "tossups_read": int(game["tossups_read"]),
                    "_year": game["year"],
                }
            )

        # --- Identity review warnings (informational, non-fatal) -----------
        # Two different-but-related risks in the raw player slugs, surfaced
        # for a human to review rather than failing the build:
        name_conflicts = []
        names_by_slug: dict[str, set[str]] = defaultdict(set)
        for row in player_rows:
            names_by_slug[row["slug"]].add(str(row["name"]).strip().casefold())
        for slug, names in sorted(names_by_slug.items()):
            if len(names) > 1:
                # Same raw slug used by rows with different display names --
                # possibly two different people sharing one slug.
                name_conflicts.append(
                    {"type": "raw_slug_name_conflict", "raw_slug": slug, "normalized_names": sorted(names)}
                )

        suffix_groups: dict[str, set[str]] = defaultdict(set)
        for row in player_rows:
            base = re.sub(r"-\d+$", "", row["slug"])
            suffix_groups[base].add(row["slug"])
        suffix_warnings = [
            {"type": "ambiguous_suffixed_slug_group", "base_slug": base, "raw_slugs": sorted(slugs)}
            for base, slugs in sorted(suffix_groups.items())
            if len(slugs) > 1
            # e.g. "john-smith" and "john-smith-2" both present -- the "-2"
            # suffix usually disambiguates two different people, but could
            # also just be an unrelated slug that happens to end in a digit.
        ]

        # --- Derived irt_responses: one binary label per (player, tossup) --
        # Every player rostered on either team for a tossup gets a label:
        # 1 if *that* player is the one who buzzed correctly, 0 otherwise
        # (including teammates who never buzzed at all). This is what makes
        # irt_responses a full response matrix rather than just the buzzers.
        roster_by_team_id = {row["team_id"]: row["player_ids"] for row in teams}
        game_by_id = {row["game_id"]: row for row in games}
        tossup_year = {row["tossup_id"]: row["_year"] for row in tossups}
        evidence: dict[tuple[str, str], dict[str, Any]] = {}
        correct_pairs = {
            (row["player_id"], row["tossup_id"])
            for row in tossup_buzzes
            if row["correct"]
        }
        for game_id, tossup_id in {
            (row["game_id"], row["tossup_id"]) for row in tossup_buzzes
        }:
            game = game_by_id[game_id]
            for team_id in game["team_ids"]:
                for player_id in roster_by_team_id[team_id]:
                    key = (player_id, tossup_id)
                    evidence[key] = {
                        "response_id": f"{player_id}::{tossup_id}",
                        "player_id": player_id,
                        "tossup_id": tossup_id,
                        "response": int(key in correct_pairs),
                        "_year": tossup_year[tossup_id],
                    }
        irt_responses = [evidence[key] for key in sorted(evidence)]

        tables = {
            "tournaments": tournaments,
            "players": players,
            "teams": teams,
            "games": games,
            "tossups": tossups,
            "bonuses": bonuses,
            "tossup_buzzes": tossup_buzzes,
            "bonus_responses": bonus_responses,
            "irt_responses": irt_responses,
        }
        build_report = {
            **preflight,
            "output_counts": {name: len(rows) for name, rows in tables.items()},
            "repair_summary": {
                "team_id_collisions": len(team_collisions),
                "duplicate_bonus_part_score_keys": len(bonus_repairs),
                "conflicting_duplicate_bonus_part_score_keys": sum(
                    len(set(repair["source_values"])) > 1 for repair in bonus_repairs
                ),
            },
            "repairs": {
                "team_id_collisions": team_collisions,
                "duplicate_bonus_part_scores": bonus_repairs,
            },
            "warnings": {
                "packet_positions_without_bonus": len(tossups) - len(bonuses),
                "tossups_with_removed_moderator_note": moderator_note_count,
                "buzzes_beyond_sanitized_token_count": beyond_token_count,
                "bonus_responses_without_earning_player": len(missing_earners),
            },
        }
        identity_report = {
            "warnings": name_conflicts + suffix_warnings + missing_earners,
            "summary": {
                "players_grouped_by_raw_slug": len(players),
                "raw_player_rows": len(player_rows),
                "raw_player_slugs": len({row["slug"] for row in player_rows}),
                "raw_slug_name_conflicts": len(name_conflicts),
                "ambiguous_suffixed_slug_groups": len(suffix_warnings),
                "missing_earning_players": len(missing_earners),
            },
        }
        return BuiltRecords(tables=tables, build_report=build_report, identity_report=identity_report)
    finally:
        connection.close()


def _public_record(row: dict[str, Any]) -> dict[str, Any]:
    """Drop internal "_"-prefixed bookkeeping fields (e.g. "_year") before saving."""
    return {key: value for key, value in row.items() if not key.startswith("_")}


def write_datasets(records: BuiltRecords, output_dir: Path) -> None:
    """Save every table as a HuggingFace 'DatasetDict' with year splits.

    Each table gets an '"all"' split plus a '"year_2024"' / '"year_2025"'
    split. Membership in a year split uses each row's private '_year'
    (most rows) or '_years' (players, who can span multiple years) field,
    which is stripped from the row before it's written ('_public_record').
    """
    output_dir.mkdir(parents=True, exist_ok=False)
    for table_name, rows in records.tables.items():
        features = TABLE_FEATURES[table_name]
        all_rows = [_public_record(row) for row in rows]
        splits: dict[str, Dataset] = {"all": Dataset.from_list(all_rows, features=features)}
        for year in (2024, 2025):
            year_rows = [
                _public_record(row)
                for row in rows
                if row.get("_year") == year or year in row.get("_years", [])
            ]
            splits[f"year_{year}"] = Dataset.from_list(year_rows, features=features)
        DatasetDict(splits).save_to_disk(str(output_dir / table_name))

    (output_dir / "build_report.json").write_text(
        json.dumps(records.build_report, indent=2, sort_keys=True), encoding="utf-8"
    )
    (output_dir / "identity_review_report.json").write_text(
        json.dumps(records.identity_report, indent=2, sort_keys=True, ensure_ascii=False),
        encoding="utf-8",
    )


def write_response_matrix(records: BuiltRecords, output_path: Path) -> None:
    """Write the wide player-by-tossup matrix derived from irt_responses."""
    matrix = (
        pd.DataFrame(records.tables["irt_responses"])
        .pivot(index="player_id", columns="tossup_id", values="response")
        .sort_index()
        .sort_index(axis=1)
    )
    matrix.index.name = "player_slug"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    matrix.to_csv(output_path)


def build_dataset_directory(
    db_path: Path,
    output_dir: Path,
    response_matrix_path: Path,
    overwrite: bool = False,
) -> dict[str, Any]:
    """Build, validate, then atomically publish the dataset and response matrix.

    The dataset is written to a temporary sibling directory first and only
    'validate_dataset'-checked and moved into place at the end, so a failed
    or interrupted build never leaves 'output_dir' in a half-written state.
    """
    # Imported lazily: validate.py imports schema constants from this module.
    from data_pipeline.validate import validate_dataset

    existing = [path for path in (output_dir, response_matrix_path) if path.exists()]
    if existing and not overwrite:
        raise FileExistsError(
            f"Output already exists: {', '.join(str(path) for path in existing)}; "
            "pass --overwrite to replace it"
        )
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    temp_dir = output_dir.parent / f".{output_dir.name}.tmp-{uuid.uuid4().hex}"
    temp_matrix = response_matrix_path.parent / (
        f".{response_matrix_path.name}.tmp-{uuid.uuid4().hex}"
    )
    records = build_records(db_path)
    try:
        write_datasets(records, temp_dir)
        write_response_matrix(records, temp_matrix)
        # Validate the freshly written temp copy (not the old published
        # copy) before anything replaces the real output.
        validation = validate_dataset(temp_dir, db_path, temp_matrix)
        records.build_report["validation"] = validation
        (temp_dir / "build_report.json").write_text(
            json.dumps(records.build_report, indent=2, sort_keys=True), encoding="utf-8"
        )
        if output_dir.exists():
            shutil.rmtree(output_dir)
        shutil.move(str(temp_dir), str(output_dir))
        if response_matrix_path.exists():
            response_matrix_path.unlink()
        shutil.move(str(temp_matrix), str(response_matrix_path))
        return records.build_report
    finally:
        # Only reached on failure -- the successful path already moved these.
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        if temp_matrix.exists():
            temp_matrix.unlink()
