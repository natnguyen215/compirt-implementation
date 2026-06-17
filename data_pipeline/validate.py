#!/usr/bin/env python3
"""Validate the generated local quizbowl IRT Hugging Face dataset."""

from __future__ import annotations

import argparse
import json
import sqlite3
from collections import defaultdict
from pathlib import Path
from typing import Any

import pandas as pd
from datasets import DatasetDict, load_from_disk

from data_pipeline.dataset import PRIMARY_KEYS, TABLE_FEATURES


def _expected_year_ids(table_name: str, all_rows: list[dict[str, Any]], tables: dict[str, list[dict[str, Any]]]) -> dict[int, set[str]]:
    pk = PRIMARY_KEYS[table_name]
    tournament_year = {row["tournament_id"]: int(row["year"]) for row in tables["tournaments"]}
    game_year = {
        row["game_id"]: tournament_year[row["tournament_id"]] for row in tables["games"]
    }
    team_year = {
        row["team_id"]: tournament_year[row["tournament_id"]] for row in tables["teams"]
    }
    player_years: dict[str, set[int]] = defaultdict(set)
    for team in tables["teams"]:
        for player_id in team["player_ids"]:
            player_years[player_id].add(team_year[team["team_id"]])

    result = {2024: set(), 2025: set()}
    for row in all_rows:
        if table_name == "tournaments":
            years = {int(row["year"])}
        elif table_name == "players":
            years = player_years[row["player_id"]]
        elif table_name == "teams":
            years = {team_year[row["team_id"]]}
        elif table_name == "games":
            years = {game_year[row["game_id"]]}
        elif table_name in {"tossups", "bonuses"}:
            years = {int(row["question_set_event_id"][:4])}
        elif table_name == "irt_responses":
            years = {int(row["tossup_id"][:4])}
        else:
            years = {game_year[row["game_id"]]}
        for year in years:
            if year in result:
                result[year].add(row[pk])
    return result


def validate_dataset(
    data_dir: Path,
    db_path: Path | None = None,
    response_matrix_path: Path | None = None,
) -> dict[str, Any]:
    errors: list[str] = []
    tables: dict[str, list[dict[str, Any]]] = {}
    splits: dict[str, DatasetDict] = {}
    for table_name, expected_features in TABLE_FEATURES.items():
        table_path = data_dir / table_name
        if not table_path.is_dir():
            errors.append(f"Missing dataset directory: {table_path}")
            continue
        dataset = load_from_disk(str(table_path))
        splits[table_name] = dataset
        if set(dataset.keys()) != {"all", "year_2024", "year_2025"}:
            errors.append(f"{table_name}: unexpected splits {sorted(dataset.keys())}")
        for split_name in dataset:
            if dataset[split_name].features != expected_features:
                errors.append(f"{table_name}/{split_name}: feature schema mismatch")
        tables[table_name] = [dict(row) for row in dataset["all"]]

    if errors:
        raise ValueError("\n".join(errors))

    for table_name, rows in tables.items():
        pk = PRIMARY_KEYS[table_name]
        ids = [row[pk] for row in rows]
        if len(ids) != len(set(ids)):
            errors.append(f"{table_name}: duplicate primary IDs")
        expected_years = _expected_year_ids(table_name, rows, tables)
        for year, expected_ids in expected_years.items():
            actual_ids = set(splits[table_name][f"year_{year}"][pk])
            if actual_ids != expected_ids:
                errors.append(
                    f"{table_name}/year_{year}: expected {len(expected_ids)} IDs, found {len(actual_ids)}"
                )

    tournament_ids = {row["tournament_id"] for row in tables["tournaments"]}
    player_ids = {row["player_id"] for row in tables["players"]}
    team_ids = {row["team_id"] for row in tables["teams"]}
    game_ids = {row["game_id"] for row in tables["games"]}
    tossup_ids = {row["tossup_id"] for row in tables["tossups"]}
    bonus_ids = {row["bonus_id"] for row in tables["bonuses"]}

    for team in tables["teams"]:
        if team["tournament_id"] not in tournament_ids:
            errors.append(f"teams: missing tournament {team['tournament_id']}")
        if not set(team["player_ids"]) <= player_ids:
            errors.append(f"teams: missing player reference on {team['team_id']}")
    for game in tables["games"]:
        if game["tournament_id"] not in tournament_ids or not set(game["team_ids"]) <= team_ids:
            errors.append(f"games: broken reference on {game['game_id']}")
    for buzz in tables["tossup_buzzes"]:
        if (
            buzz["game_id"] not in game_ids
            or buzz["team_id"] not in team_ids
            or buzz["player_id"] not in player_ids
            or buzz["tossup_id"] not in tossup_ids
        ):
            errors.append(f"tossup_buzzes: broken reference on {buzz['buzz_id']}")
    for response in tables["bonus_responses"]:
        if (
            response["game_id"] not in game_ids
            or response["team_id"] not in team_ids
            or response["bonus_id"] not in bonus_ids
            or (response["earning_player_id"] and response["earning_player_id"] not in player_ids)
        ):
            errors.append(f"bonus_responses: broken reference on {response['response_id']}")
        if len(response["parts_correct"]) != 3:
            errors.append(f"bonus_responses: response does not have three parts: {response['response_id']}")
    for bonus in tables["bonuses"]:
        if len(bonus["parts"]) != 3:
            errors.append(f"bonuses: bonus does not have three parts: {bonus['bonus_id']}")
    for response in tables["irt_responses"]:
        if response["player_id"] not in player_ids or response["tossup_id"] not in tossup_ids:
            errors.append(f"irt_responses: broken reference on {response['response_id']}")
        if int(response["response"]) not in {0, 1}:
            errors.append(f"irt_responses: non-binary response on {response['response_id']}")

    actual_irt = {
        (row["player_id"], row["tossup_id"]): int(row["response"])
        for row in tables["irt_responses"]
    }
    roster_by_team = {row["team_id"]: row["player_ids"] for row in tables["teams"]}
    game_by_id = {row["game_id"]: row for row in tables["games"]}
    correct_pairs = {
        (row["player_id"], row["tossup_id"])
        for row in tables["tossup_buzzes"]
        if row["correct"]
    }
    expected_irt: dict[tuple[str, str], int] = {}
    for game_id_value, tossup_id_value in {
        (row["game_id"], row["tossup_id"]) for row in tables["tossup_buzzes"]
    }:
        for team_id in game_by_id[game_id_value]["team_ids"]:
            for player_id in roster_by_team[team_id]:
                key = (player_id, tossup_id_value)
                expected_irt[key] = int(key in correct_pairs)
    if actual_irt != expected_irt:
        errors.append(
            f"irt_responses: expected {len(expected_irt)} derived observations, "
            f"found {len(actual_irt)}"
        )

    buzzes_by_game: dict[str, list[dict[str, Any]]] = defaultdict(list)
    responses_by_game: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for buzz in tables["tossup_buzzes"]:
        buzzes_by_game[buzz["game_id"]].append(buzz)
    for response in tables["bonus_responses"]:
        responses_by_game[response["game_id"]].append(response)
    for game in tables["games"]:
        scores = {team_id: 0 for team_id in game["team_ids"]}
        events: dict[int, dict[str, list[dict[str, Any]]]] = defaultdict(
            lambda: {"buzzes": [], "responses": []}
        )
        for buzz in buzzes_by_game[game["game_id"]]:
            events[int(buzz["question_number_in_game"])]["buzzes"].append(buzz)
        for response in responses_by_game[game["game_id"]]:
            events[int(response["question_number_in_game"])]["responses"].append(response)

        for question_number in sorted(events):
            for buzz in sorted(
                events[question_number]["buzzes"],
                key=lambda row: (int(row["token_position"]), int(row["buzz_id"].rsplit("-", 1)[1])),
            ):
                opponent_id = next(team_id for team_id in game["team_ids"] if team_id != buzz["team_id"])
                if buzz["team_score"] != scores[buzz["team_id"]] or buzz["opponent_score"] != scores[opponent_id]:
                    errors.append(f"tossup_buzzes: score timeline mismatch on {buzz['buzz_id']}")
                scores[buzz["team_id"]] += int(buzz["value"])
            for response in sorted(
                events[question_number]["responses"],
                key=lambda row: (row["team_id"], row["bonus_id"]),
            ):
                opponent_id = next(team_id for team_id in game["team_ids"] if team_id != response["team_id"])
                if (
                    response["team_score"] != scores[response["team_id"]]
                    or response["opponent_score"] != scores[opponent_id]
                ):
                    errors.append(f"bonus_responses: score timeline mismatch on {response['response_id']}")
                scores[response["team_id"]] += int(response["total_points"])

        reconstructed = [scores[team_id] for team_id in game["team_ids"]]
        if reconstructed != game["final_scores"]:
            errors.append(f"games: final score mismatch on {game['game_id']}")

    if db_path is not None:
        connection = sqlite3.connect(f"file:{db_path.resolve().as_posix()}?mode=ro", uri=True)
        try:
            expected_counts = {
                "tournaments": connection.execute("SELECT COUNT(*) FROM tournament").fetchone()[0],
                "teams": connection.execute("SELECT COUNT(*) FROM team").fetchone()[0],
                "players": connection.execute("SELECT COUNT(DISTINCT slug) FROM player").fetchone()[0],
                "games": connection.execute("SELECT COUNT(*) FROM game").fetchone()[0],
                "tossups": connection.execute(
                    "SELECT COUNT(*) FROM tossup"
                ).fetchone()[0],
                "bonuses": connection.execute(
                    "SELECT COUNT(DISTINCT pq.packet_id || ':' || pq.question_number) "
                    "FROM packet_question pq JOIN bonus b ON b.question_id=pq.question_id"
                ).fetchone()[0],
                "tossup_buzzes": connection.execute("SELECT COUNT(*) FROM buzz").fetchone()[0],
                "bonus_responses": connection.execute(
                    "SELECT COUNT(*) FROM ("
                    "SELECT d.game_id,d.team_id,bp.bonus_id FROM bonus_part_direct d "
                    "JOIN bonus_part bp ON bp.id=d.bonus_part_id "
                    "GROUP BY d.game_id,d.team_id,bp.bonus_id)"
                ).fetchone()[0],
            }
            for table_name, expected in expected_counts.items():
                if len(tables[table_name]) != expected:
                    errors.append(
                        f"{table_name}: expected {expected} source-derived rows, found {len(tables[table_name])}"
                    )
        finally:
            connection.close()

    if response_matrix_path is not None:
        actual_matrix = pd.read_csv(response_matrix_path, index_col=0)
        actual_matrix.columns = actual_matrix.columns.astype(str)
        expected_matrix = (
            pd.DataFrame(tables["irt_responses"])
            .pivot(index="player_id", columns="tossup_id", values="response")
            .sort_index()
            .sort_index(axis=1)
        )
        actual_matrix = actual_matrix.sort_index().sort_index(axis=1)
        try:
            pd.testing.assert_frame_equal(
                actual_matrix,
                expected_matrix,
                check_dtype=False,
                check_names=False,
            )
        except AssertionError as error:
            errors.append(f"response_matrix.csv does not match irt_responses: {error}")

    if errors:
        preview = "\n".join(errors[:50])
        extra = "" if len(errors) <= 50 else f"\n... and {len(errors) - 50} more errors"
        raise ValueError(preview + extra)
    return {
        "status": "ok",
        "counts": {name: len(rows) for name, rows in tables.items()},
        "checks": [
            "schemas",
            "primary_ids",
            "year_splits",
            "foreign_keys",
            "three_part_bonuses",
            "intermediate_score_timelines",
            "reconstructed_final_scores",
            "source_counts" if db_path is not None else "source_counts_skipped",
            "irt_response_derivation",
            "response_matrix" if response_matrix_path is not None else "response_matrix_skipped",
        ],
    }


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-path", type=Path, default=ROOT / "data" / "database.db")
    parser.add_argument(
        "--data-dir", type=Path, default=ROOT / "data" / "hf" / "quizbowl-irt"
    )
    parser.add_argument(
        "--response-matrix",
        type=Path,
        default=ROOT / "data" / "response_matrix.csv",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = validate_dataset(
        data_dir=args.data_dir.expanduser(),
        db_path=args.db_path.expanduser(),
        response_matrix_path=args.response_matrix.expanduser(),
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
