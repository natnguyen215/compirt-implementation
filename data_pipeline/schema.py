"""Schema constants for the linked quizbowl IRT HuggingFace dataset.

The pipeline turns one SQLite database (the raw quizbowl reporting export)
into nine linked tables, each saved as its own HuggingFace 'DatasetDict'
under 'data/hf/quizbowl-irt/<table>'. This module is the single source of
truth for that output schema, so 'dataset.py' (which builds the tables) and
'validate.py' (which checks them) always agree on column names, types, and
primary keys.

Table relationships, for orientation:

* 'tournaments' -- one row per mirror-tournament site.
* 'players' / 'teams' / 'games' -- entities rostered into tournaments.
* 'tossups' / 'bonuses' -- the question text, keyed by packet position.
* 'tossup_buzzes' / 'bonus_responses' -- the raw scoring events.
* 'irt_responses' -- one row per (player, tossup) pair, derived from
  'tossup_buzzes' by 'dataset.py': every rostered player gets a binary
  correct/incorrect label for every tossup their team saw, not just the
  player who actually buzzed.
"""

from __future__ import annotations

from datasets import Features, List, Value


# Source SQLite tables that must exist (with a passing integrity check)
# before the pipeline will attempt to read from the database.
REQUIRED_TABLES = {
    "bonus",
    "bonus_part",
    "bonus_part_direct",
    "buzz",
    "game",
    "packet",
    "packet_question",
    "player",
    "question",
    "question_set",
    "question_set_edition",
    "round",
    "team",
    "tossup",
    "tournament",
}

# Output HuggingFace schema, one Features spec per saved table. Keys here are
# the table (directory) names; keys inside each Features are column names.
TABLE_FEATURES: dict[str, Features] = {
    "tournaments": Features(
        {
            "tournament_id": Value("string"),
            "name": Value("string"),
            "tier": Value("string"),
            "year": Value("int64"),
            "num_packets": Value("int64"),
            "question_set_event_id": Value("string"),
            "level": Value("string"),
            "location": Value("string"),
            "start_date": Value("string"),
            "end_date": Value("string"),
        }
    ),
    "players": Features(
        {
            "player_id": Value("string"),
            "name": Value("string"),
            "first_seen_tournament": Value("string"),
            "tournaments_played": List(Value("string")),
            "source_slugs": List(Value("string")),
            "source_player_refs": List(Value("string")),
        }
    ),
    "teams": Features(
        {
            "team_id": Value("string"),
            "tournament_id": Value("string"),
            "team_name": Value("string"),
            "player_ids": List(Value("string")),
        }
    ),
    "games": Features(
        {
            "game_id": Value("string"),
            "tournament_id": Value("string"),
            "round": Value("string"),
            "packet_id": Value("int64"),
            "team_ids": List(Value("string")),
            "final_scores": List(Value("int64")),
            "tossups_read": Value("int64"),
        }
    ),
    "tossups": Features(
        {
            "tossup_id": Value("string"),
            "question_set_event_id": Value("string"),
            "packet": Value("int64"),
            "question_num": Value("int64"),
            "category": Value("string"),
            "subcategory": Value("string"),
            "answer": Value("string"),
            "tokens": List(Value("string")),
            "sentence_boundaries": List(Value("int64")),
            "question": Value("string"),
        }
    ),
    "bonuses": Features(
        {
            "bonus_id": Value("string"),
            "question_set_event_id": Value("string"),
            "packet": Value("int64"),
            "question_num": Value("int64"),
            "category": Value("string"),
            "subcategory": Value("string"),
            "leadin": Value("string"),
            "parts": List(
                {
                    "text": Value("string"),
                    "answer": Value("string"),
                    "difficulty": Value("string"),
                }
            ),
        }
    ),
    "tossup_buzzes": Features(
        {
            "buzz_id": Value("string"),
            "tossup_id": Value("string"),
            "game_id": Value("string"),
            "player_id": Value("string"),
            "team_id": Value("string"),
            "token_position": Value("int64"),
            "num_tokens_total": Value("int64"),
            "correct": Value("bool"),
            "team_score": Value("int64"),
            "opponent_score": Value("int64"),
            "question_number_in_game": Value("int64"),
            "value": Value("int64"),
        }
    ),
    "bonus_responses": Features(
        {
            "response_id": Value("string"),
            "bonus_id": Value("string"),
            "game_id": Value("string"),
            "team_id": Value("string"),
            "earning_player_id": Value("string"),
            "parts_correct": List(Value("bool")),
            "total_points": Value("int64"),
            "team_score": Value("int64"),
            "opponent_score": Value("int64"),
            "question_number_in_game": Value("int64"),
        }
    ),
    "irt_responses": Features(
        {
            "response_id": Value("string"),
            "player_id": Value("string"),
            "tossup_id": Value("string"),
            "response": Value("int64"),
        }
    ),
}

# Column that uniquely identifies one row within each output table.
PRIMARY_KEYS = {
    "tournaments": "tournament_id",
    "players": "player_id",
    "teams": "team_id",
    "games": "game_id",
    "tossups": "tossup_id",
    "bonuses": "bonus_id",
    "tossup_buzzes": "buzz_id",
    "bonus_responses": "response_id",
    "irt_responses": "response_id",
}
