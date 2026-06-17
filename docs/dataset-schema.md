---
pretty_name: Quizbowl IRT Tournament Tables
task_categories:
  - tabular-classification
  - question-answering
tags:
  - quizbowl
  - tournament-data
  - item-response-theory
  - educational-data
---

# Quizbowl IRT Dataset

This dataset turns ACF tournament database records into a set of linked, table-like HuggingFace dataset configs. It is designed for quizbowl modeling work where you want to separate stable entities, such as players, teams, games, tossups, and bonuses, from observations, such as buzzes and bonus part outcomes.

The guiding idea is simple: entities describe what existed, observations describe what happened. That makes it possible to train player models, question difficulty models, buzz timing models, or bonus conversion models without duplicating the same question or roster metadata in every row.

## Current Build

Generated from `data/dbs/acf-24-25.db`.

| Table | Rows |
| --- | ---: |
| `tournaments` | 68 |
| `players` | 2,665 |
| `teams` | 1,054 |
| `games` | 5,704 |
| `tossups` | 2,936 |
| `bonuses` | 2,935 |
| `tossup_buzzes` | 136,586 |
| `bonus_responses` | 104,941 |

The builder also writes `identity_review_report.json`, which records raw-slug
name warnings and game-timeline warnings.

- 1 colliding team slug was preserved with database-ID suffixes.
- 66 duplicate bonus-part score keys were repaired using latest-row-wins; 24
  contained conflicting values.
- 24,045 bonus responses have no uniquely inferable earning player.
- 65 buzz positions exceed the sanitized tossup token count and are retained.
- 1 packet position has a tossup but no bonus.

## Loading

Each table is stored as its own HuggingFace config. Locally, after running the builder:

```python
from datasets import load_from_disk

tossups = load_from_disk("data/hf/quizbowl-irt/tossups")
all_tossups = tossups["all"]
twenty_four_tossups = tossups["year_2024"]
```

From the Hub, use the table name as the config name:

```python
from datasets import load_dataset

buzzes = load_dataset("maharshi/quizbowl-irt", "tossup_buzzes", split="all")
players_2025 = load_dataset("maharshi/quizbowl-irt", "players", split="year_2025")
```

Every config has an `all` split and year splits such as `year_2024` and `year_2025`. The year split is based on the tournament or question-set date, depending on the table.

## ID Model

There are two grains of tournament identity:

- `tournament_id` is a mirror-site tournament from the database, such as `2024-acf-regionals-berkeley`. Games and teams use this ID because they happened at a specific site.
- `question_set_event_id` is the shared question-set event, such as `2024-acf-regionals`. Tossups and bonuses use this ID because the same packet questions are shared across mirror sites.

This avoids duplicating question text for every mirror site while preserving the actual gameplay site for teams and games.

## Tables

### `tournaments`

One row per mirror-site tournament.

| Field | Type | Meaning |
| --- | --- | --- |
| `tournament_id` | string | Stable mirror-site ID, usually the database tournament slug. |
| `name` | string | Human-readable tournament name. |
| `tier` | string | Event tier inferred from the question set, such as `regionals`, `nationals`, `fall`, or `winter`. |
| `year` | integer | Tournament start year. |
| `num_packets` | integer | Number of distinct packets used by rounds in that mirror tournament. |
| `question_set_event_id` | string | Shared event ID for the question set used by this tournament. |
| `level` | string | Tournament level from the database, such as `College` or `Novice`. |
| `location` | string | Location field from the database when present. |
| `start_date` | string | ISO date string. |
| `end_date` | string | ISO date string. |

Use this table to group games by site, year, event tier, or question set.

### `players`

One row per raw player slug.

| Field | Type | Meaning |
| --- | --- | --- |
| `player_id` | string | Raw player slug used as the player ID. |
| `name` | string | Representative player name from the first observed record. |
| `first_seen_tournament` | string | First mirror tournament in which the player appears. |
| `tournaments_played` | list[string] | Mirror tournaments associated with this player ID. |
| `source_slugs` | list[string] | Raw player slugs represented by this row. |
| `source_player_refs` | list[string] | Audit references of the form `tournament_slug::team_slug::player_slug`. |

Rows sharing a raw player slug are grouped under that slug. Numeric suffix
variants such as `kevin`, `kevin-2`, and `kevin-3` remain separate and are
surfaced in `identity_review_report.json` for review.

Use this table to attach player metadata to buzzes or to build player-level skill histories.

### `teams`

One row per team entry in a mirror tournament.

| Field | Type | Meaning |
| --- | --- | --- |
| `team_id` | string | Composite ID: `tournament_id::team_slug`. |
| `tournament_id` | string | Mirror-site tournament ID. |
| `team_name` | string | Human-readable team name. |
| `player_ids` | list[string] | Raw-slug player IDs on the roster. |

Use this table to map buzzes and games back to rosters.

### `games`

One row per game.

| Field | Type | Meaning |
| --- | --- | --- |
| `game_id` | string | Composite ID: `tournament_id::game-{db_id}`. |
| `tournament_id` | string | Mirror-site tournament ID. |
| `round` | string | Round label, such as `round10`. |
| `packet_id` | integer | Source packet used for the game round. |
| `team_ids` | list[string] | Two team IDs, ordered as team one then team two in the database. |
| `final_scores` | list[int] | Final scores parallel to `team_ids`, derived from buzz and bonus scoring rows. |
| `tossups_read` | integer | Number of tossups read in the game. |

Use this table for matchup context, final outcomes, score modeling, or joining observations to tournament metadata.

### `tossups`

One row per tossup question in the shared question set.

| Field | Type | Meaning |
| --- | --- | --- |
| `tossup_id` | string | Composite shared question ID: `question_set_event_id::p{packet_id}::q{question_num}`. |
| `question_set_event_id` | string | Shared question-set event ID. |
| `packet` | integer | Database packet ID. |
| `question_num` | integer | Question number within the packet. |
| `category` | string | Question category, empty if missing in the source DB. |
| `subcategory` | string | Question subcategory, empty if missing in the source DB. |
| `answer` | string | Raw answer line. |
| `tokens` | list[string] | Sanitized tossup text split on whitespace. |
| `sentence_boundaries` | list[int] | Token indices where sentence or clue-like spans end. |
| `question` | string | Sanitized full tossup text. |

Use this table as item metadata for tossup difficulty, buzz timing, clue-level modeling, or answer prediction.

### `bonuses`

One row per bonus question in the shared question set.

| Field | Type | Meaning |
| --- | --- | --- |
| `bonus_id` | string | Composite shared bonus ID: `question_set_event_id::p{packet_id}::b{question_num}`. |
| `question_set_event_id` | string | Shared question-set event ID. |
| `packet` | integer | Database packet ID. |
| `question_num` | integer | Bonus number within the packet. |
| `category` | string | Question category, empty if missing in the source DB. |
| `subcategory` | string | Question subcategory, empty if missing in the source DB. |
| `leadin` | string | Sanitized bonus lead-in text. |
| `parts` | list[dict] | Three part objects with `text`, `answer`, and `difficulty`. |

Each part has:

| Field | Type | Meaning |
| --- | --- | --- |
| `text` | string | Sanitized bonus part text. |
| `answer` | string | Raw answer line for the part. |
| `difficulty` | string | `easy`, `medium`, `hard`, or the raw modifier if it is nonstandard. |

Use this table for bonus difficulty modeling, part-level conversion models, or question-set analysis.

### `tossup_buzzes`

One row per buzz event.

| Field | Type | Meaning |
| --- | --- | --- |
| `buzz_id` | string | Composite game-local buzz ID. |
| `tossup_id` | string | Shared tossup ID. |
| `game_id` | string | Game in which the buzz occurred. |
| `player_id` | string | Raw-slug player ID. |
| `team_id` | string | Team ID for the buzzing player. |
| `token_position` | integer | Buzz position after subtracting moderator instruction offset, clamped at zero. |
| `num_tokens_total` | integer | Total number of sanitized tossup tokens. |
| `correct` | boolean | Whether the buzz value was positive. |
| `team_score` | integer | Buzzing team's score before this buzz. |
| `opponent_score` | integer | Opponent's score before this buzz. |
| `question_number_in_game` | integer | Packet question number used as the game timeline position. |
| `value` | integer | Raw buzz value from the DB, typically `10`, `0`, or `-5`. |

This is the main tossup observation table. Use it for player ability models, clue-position models, neg risk models, or score-aware buzzing policies.

### `bonus_responses`

One row per team bonus heard.

| Field | Type | Meaning |
| --- | --- | --- |
| `response_id` | string | Composite game/team/bonus response ID. |
| `bonus_id` | string | Shared bonus ID. |
| `game_id` | string | Game in which the bonus was heard. |
| `team_id` | string | Team that answered the bonus. |
| `earning_player_id` | string | Player who earned the bonus via a correct tossup buzz when inferable; empty otherwise. |
| `parts_correct` | list[bool] | Three booleans in bonus part order. |
| `total_points` | integer | Sum of scored bonus part values. |
| `team_score` | integer | Team score after the earning tossup and before bonus parts are added. |
| `opponent_score` | integer | Opponent score at the same moment. |
| `question_number_in_game` | integer | Packet question number used as the game timeline position. |

Use this table for bonus conversion models, team-level knowledge models, or studying how tossup conversion leads into bonus opportunities.

## Score Timeline

The builder reconstructs game state from the event rows:

1. Start each game at `0-0`.
2. Process packet question numbers in order.
3. Within a tossup, process buzzes by `buzz_position`.
4. Record `team_score` and `opponent_score` before applying the buzz value.
5. Apply buzz value.
6. For the corresponding bonus, record the score after the earning tossup and before adding bonus points.
7. Add bonus part values to produce the derived final score.

The `games.final_scores` field is derived from this same timeline.

## Player Slug Review

The builder groups rows only when they have the same raw player slug. It writes
`identity_review_report.json` with warning objects such as:

- `ambiguous_suffixed_slug_group`: suffix variants share a base slug but are not merged automatically.
- `raw_slug_name_conflict`: the same raw slug appears with incompatible normalized names.
- `missing_earning_player`: a bonus response could not be linked to a positive tossup buzz for the same game, team, and packet question number.

## Example Joins

Player buzz timing:

```python
from datasets import load_from_disk

base = "data/hf/quizbowl-irt"
buzzes = load_from_disk(f"{base}/tossup_buzzes")["all"].to_pandas()
players = load_from_disk(f"{base}/players")["all"].to_pandas()

player_buzzes = buzzes.merge(players, on="player_id")
player_buzzes["relative_buzz_position"] = (
    player_buzzes["token_position"] / player_buzzes["num_tokens_total"]
)
```

Question-level buzz rates:

```python
tossups = load_from_disk(f"{base}/tossups")["all"].to_pandas()
question_stats = (
    buzzes.groupby("tossup_id")
    .agg(buzzes=("buzz_id", "count"), correct_rate=("correct", "mean"))
    .reset_index()
    .merge(tossups, on="tossup_id")
)
```

Bonus conversion:

```python
responses = load_from_disk(f"{base}/bonus_responses")["all"].to_pandas()
bonuses = load_from_disk(f"{base}/bonuses")["all"].to_pandas()

bonus_stats = (
    responses.groupby("bonus_id")
    .agg(mean_points=("total_points", "mean"), heard=("response_id", "count"))
    .reset_index()
    .merge(bonuses, on="bonus_id")
)
```

## Limitations

- Missing source categories remain empty strings instead of being guessed.
- Some `earning_player_id` values are empty when a bonus cannot be reliably matched to a positive tossup buzz.
- Ambiguous suffix variants remain separate and need manual review outside the
  builder before any future merging approach is added.
- `packet` is the source database packet ID, not a normalized packet label.

## Rebuilding

From the repository root:

```bash
.venv/bin/python -m data_pipeline.build \
  --db-path data/database.db \
  --output-dir data/hf/quizbowl-irt \
  --overwrite
```

The builder performs a SQLite integrity/schema preflight, writes all eight
HuggingFace `DatasetDict` directories to a temporary location, validates them,
and only then replaces the requested output directory.

Validate an existing build independently:

```bash
.venv/bin/python -m data_pipeline.validate \
  --db-path data/database.db \
  --data-dir data/hf/quizbowl-irt
```

The output root also contains:

- `build_report.json`: source/output counts, deterministic repairs, warnings,
  and validation results.
- `identity_review_report.json`: raw-slug player warnings and
  bonus responses whose earning player could not be inferred.

### Deterministic Repair Policy

- Colliding team slugs are preserved as separate team IDs with `::db-{id}`
  suffixes.
- Player rows with the same raw slug are grouped under that slug.
- Numeric suffix variants remain distinct.
- Duplicate direct bonus-part scores use the highest source row ID as the final
  correction. Every affected key and source value is recorded.
- Leading moderator-note markup is removed from tossup text and its token count
  is subtracted from recorded buzz positions. Positions are clamped only at
  zero; positions beyond the sanitized question length are retained and
  reported.
