"""Tests for the academic-season split, which spans two calendar years."""

from __future__ import annotations

import unittest

import pandas as pd

from holdout.season_splits import (
    parse_season_split,
    season_label_for_date,
    season_split_name,
    select_season_tables,
)


def linked_tables() -> dict[str, pd.DataFrame]:
    """Four events across three calendar years, one per season boundary.

    ``fall23`` belongs to season 2023-24, ``fall24``/``regionals25`` to
    2024-25, and ``fall25`` to 2025-26, so a correct July cutoff keeps exactly
    the middle pair.
    """
    events = [
        ("fall23", "2023-10-21", "2023-24"),
        ("fall24", "2024-10-19", "2024-25"),
        ("regionals25", "2025-02-01", "2024-25"),
        ("fall25", "2025-10-18", "2025-26"),
    ]
    tournaments, games, teams, buzzes, responses, tossups, bonuses = (
        [], [], [], [], [], [], []
    )
    for event, start_date, _season in events:
        tournaments.append(
            {
                "tournament_id": event,
                "question_set_event_id": f"set-{event}",
                "start_date": start_date,
            }
        )
        tossups.append(
            {"tossup_id": f"q-{event}", "question_set_event_id": f"set-{event}"}
        )
        bonuses.append(
            {"bonus_id": f"b-{event}", "question_set_event_id": f"set-{event}"}
        )
        for team in ("x", "y"):
            teams.append({"team_id": f"{event}-{team}", "tournament_id": event})
        games.append(
            {
                "game_id": f"g-{event}",
                "tournament_id": event,
                "round": "round1",
                "packet_id": 1,
                "team_ids": [f"{event}-x", f"{event}-y"],
            }
        )
        buzzes.append(
            {
                "buzz_id": f"z-{event}",
                "game_id": f"g-{event}",
                "tossup_id": f"q-{event}",
                "player_id": f"p-{event}",
            }
        )
        responses.append(
            {
                "response_id": f"r-{event}",
                "game_id": f"g-{event}",
                "bonus_id": f"b-{event}",
            }
        )
    return {
        "tournaments": pd.DataFrame(tournaments),
        "teams": pd.DataFrame(teams),
        "games": pd.DataFrame(games),
        "tossup_buzzes": pd.DataFrame(buzzes),
        "bonus_responses": pd.DataFrame(responses),
        "tossups": pd.DataFrame(tossups),
        "bonuses": pd.DataFrame(bonuses),
    }


class SeasonSplitNameTests(unittest.TestCase):
    def test_parses_canonical_name(self):
        self.assertEqual(parse_season_split("season_2024_25"), "2024_25")
        self.assertEqual(season_split_name("2024_25"), "season_2024_25")

    def test_ignores_other_splits(self):
        for split in ("all", "year_2024", "game-holdout:year_2024:test:5:0:42"):
            self.assertIsNone(parse_season_split(split))

    def test_rejects_malformed_and_non_consecutive_names(self):
        for split in ("season_2024", "season_24_25", "season_2024_2025", "season_2024_26"):
            with self.assertRaises(ValueError):
                parse_season_split(split)

    def test_july_cutoff_joins_autumn_to_the_following_spring(self):
        self.assertEqual(season_label_for_date("2024-10-19"), "2024_25")
        self.assertEqual(season_label_for_date("2025-02-01"), "2024_25")
        self.assertEqual(season_label_for_date("2024-04-21"), "2023_24")
        self.assertEqual(season_label_for_date("2024-07-01"), "2024_25")
        self.assertEqual(season_label_for_date("2024-06-30"), "2023_24")
        self.assertIsNone(season_label_for_date("not-a-date"))


class SeasonSelectionTests(unittest.TestCase):
    def test_selects_only_the_requested_season_across_calendar_years(self):
        selected = select_season_tables(linked_tables(), "2024_25")
        self.assertEqual(
            sorted(selected["tournaments"]["tournament_id"]),
            ["fall24", "regionals25"],
        )
        self.assertEqual(sorted(selected["games"]["game_id"]), ["g-fall24", "g-regionals25"])

    def test_linked_tables_stay_consistent(self):
        selected = select_season_tables(linked_tables(), "2024_25")
        game_ids = set(selected["games"]["game_id"])
        self.assertEqual(set(selected["tossup_buzzes"]["game_id"]), game_ids)
        self.assertEqual(set(selected["bonus_responses"]["game_id"]), game_ids)
        self.assertEqual(
            sorted(selected["tossups"]["tossup_id"]), ["q-fall24", "q-regionals25"]
        )
        self.assertEqual(
            sorted(selected["teams"]["team_id"]),
            ["fall24-x", "fall24-y", "regionals25-x", "regionals25-y"],
        )

    def test_unknown_season_reports_what_is_available(self):
        with self.assertRaises(ValueError) as caught:
            select_season_tables(linked_tables(), "2030_31")
        self.assertIn("2024_25", str(caught.exception))

    def test_does_not_mutate_the_input_tables(self):
        tables = linked_tables()
        select_season_tables(tables, "2024_25")
        self.assertEqual(len(tables["games"]), 4)


if __name__ == "__main__":
    unittest.main()
