# Inferred Game Lineups

## Why

The source quizbowl reporting data records each team's registered **roster** (a
tournament-level list of players) but never the lineup that actually played a
particular game. CompIRT originally treated the full roster as active in every
game. That has two costs:

- **Tossups** (`pyramidal_model.py`, competing risks): every rostered player of
  both teams becomes a competing risk (a BUZZ/CENSORED/NO-BUZZ row) on every
  tossup, so players who did not play inflate the censored population.
- **Bonuses** (`compositional_model.py`, log-sum-exp aggregation + pairwise
  synergy): the aggregation and every synergy pair run over the whole roster,
  mixing in players who did not play that game.

`lineup.py` reconstructs a plausible active lineup — usually four players — for
each team in each game from *who actually buzzed*, and feeds that to both model
stages in place of the full roster. This is a **data-stage** change; the models
are unchanged and consume whatever player set the observation builders emit.

## Where it runs

- Inference lives in [`lineup.py`](../lineup.py). It reads the loaded HF tables
  (`teams`, `games`, `tossups`, `tossup_buzzes`) and produces one row per
  `(game_id, team_id, segment)`.
- The result is cached to `data/lineups/lineup_segments.csv` and **loaded** by
  every training run — lineups are not recomputed each run. Rebuild the cache
  after changing the logic with `python lineup.py --rebuild`.
- [`compirt_data.py`](../compirt_data.py) consumes it: `build_tossup_observations`
  unions both teams' lineups per tossup event; `build_bonus_part_observations`
  attaches the answering team's lineup to each bonus part. Both accept an
  optional in-memory `LineupIndex` (used by tests to avoid touching the cache).

## Inputs

For each `(game_id, team_id)`:

- `roster` = `teams.player_ids` (registered roster) and `roster_size`.
- `buzzers` = the distinct players who buzzed that game for that team, taken from
  **all** `tossup_buzzes` rows (not just first buzzes). Each buzz is attributed
  to a team by roster membership and to a half by the packet `question_num` of
  its tossup: `question_num <= 10` is the first half, `>= 11` the second. (`question_num`
  equals `question_number_in_game` and is always present, so the logic does not
  depend on the buzz-level game-position column.)

## Resolution rules (in priority order)

Let `n = |distinct game buzzers|`.

| # | Condition | Lineup | `resolution_rule` |
|---|---|---|---|
| 1 | `roster_size <= 4` | entire roster (short-handed if < 4) | `whole_game_small_roster` |
| 2 | `roster_size > 4` and `n == 4` | the four buzzers | `whole_game_exact_four_buzzers` |
| 3 | `roster_size > 4` and `1 <= n <= 3` | those buzzers only, **no fill** (short-handed) | `whole_game_short_handed` |
| 4 | `roster_size > 4` and `n == 0` | full roster (no evidence to infer from) | `whole_game_no_evidence` |
| 5 | `roster_size > 4` and `n >= 5` | split into halves (below) | `half_substitution` |

Rules 1–4 assign one `whole_game` segment. Rule 5 emits two segments,
`first_half` (questions 1–10) and `second_half` (11+):

- **first_half**: start from the first-half buzzers. If fewer than four, randomly
  fill up to four from the **second-half buzzers** (players who buzzed later and
  were therefore in the game) that are not already present.
- **second_half**: start from the second-half buzzers. If fewer than four,
  randomly fill up to four from the **first-half buzzers** not already present.
- A half with **more than four** buzzers keeps them all (a buzzer is never
  removed), so a lineup can exceed four in this rare case.

The idea is to isolate the substitution by inferring each half separately while
keeping cross-half (consistent) players consistent: a short half is completed
from the *other* half's buzzers — the players known to have played that game —
never from the bench. With `n >= 5`, the two half-buzzer sets always union to at
least four, so a half can always reach four from the buzzers alone: no bench
fill and no removal are ever needed.

## Bonus reuse

A bonus belongs to the same cycle as the tossup immediately before it and shares
its packet `question_num`. Because both a tossup and its bonus resolve their
lineup through the same `(game, team, question_num -> segment)` mapping
(`LineupIndex.roster_for`), the bonus lineup is **identical** to its tossup
lineup by construction — there is no separate copy step.

## Determinism

Every random fill uses `random.Random(seed)` with

```
seed = int.from_bytes(sha256(f"{game_id}|{team_id}|{segment}").digest()[:8], "big")
```

so the same database always produces the same lineups. (Python's builtin `hash`
is per-process salted and must not be used for this.) The seed is recorded in the
`random_seed` column of `lineup_segments.csv`.

## Edge cases

- **0 buzzers, roster > 4** (rule 4): there is no positive evidence of who
  played, so the full roster is kept rather than inventing a lineup. A team that
  answered a bonus always has at least one buzzer, so bonus lineups are never
  empty.
- **> 4 buzzers in one half** (rule 5): kept as-is; the `<= 4` expectation is a
  soft check, not a hard invariant. Observed buzzers are never dropped.

## Cached table: `lineup_segments.csv`

One row per `(game_id, team_id, segment)`:

| Column | Meaning |
|---|---|
| `game_id`, `team_id` | keys |
| `segment` | `whole_game`, `first_half`, or `second_half` |
| `start_question_number`, `end_question_number` | question range the segment covers |
| `roster_size`, `distinct_game_buzzers`, `lineup_size` | diagnostics |
| `player_ids` | pipe-joined lineup (source of truth) |
| `player_1_id`..`player_4_id` | first four members, for human inspection |
| `short_handed` | `True` when `lineup_size < 4` |
| `confidence` | qualitative confidence tag |
| `resolution_rule` | rule from the table above |
| `random_seed` | seed used for any random fill (blank when none) |
| `notes` | free-text explanation |

`python lineup.py --dump-debug` additionally writes `bonus_team_lineup.csv`
mapping every observed bonus response to the lineup it reuses.

## Validation invariants (see `tests/test_lineup.py`)

- Every player that buzzed in a segment appears in that segment's lineup.
- No random fill ever removes a buzzer.
- Every assigned player belongs to that team's registered roster.
- If `roster_size >= 4`, a whole-game lineup has exactly four members unless
  short-handed by rule 3.
- A bonus lineup equals the lineup of the tossup in the same cycle.
