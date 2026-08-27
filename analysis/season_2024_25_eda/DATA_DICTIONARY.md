# Data dictionary

Definitions for the CSVs written to [data/](data/) by [analyze.py](analyze.py). Source-table fields are documented in [`../../docs/dataset-schema.md`](../../docs/dataset-schema.md); this file covers only what this analysis derives.

## Shared metric columns

Most summary tables share a common block of metrics, defined once here.

### Buzz metrics

| Column | Definition |
|---|---|
| `buzz_events` | Number of tossup attempts in the group. |
| `correct` | Attempts with `value == 10`. |
| `negs` | Attempts with `value == -5`. |
| `zeros` | Attempts with `value == 0`. |
| `scored` | `correct + negs`. |
| `accuracy_all_attempts` | `correct / buzz_events`. Counts value-0 attempts as failures. |
| `scored_accuracy` | `correct / scored`. Excludes value-0 attempts. The default measure in this folder. |
| `neg_rate` | `negs / buzz_events`. |
| `zero_rate` | `zeros / buzz_events`. |
| `mean_position_pct`, `median_position_pct` | Buzz position as a percentage of the tossup revealed, clipped to [0, 100]. |
| `early_share` | Fraction of attempts below 50% revealed. |
| `very_late_share` | Fraction at or above 90% revealed. |

### Bonus metrics

| Column | Definition |
|---|---|
| `bonuses_heard` | Number of bonus responses in the group. |
| `ppb` | Mean `total_points` per bonus heard. |
| `perfect_bonus_rate` | Fraction scoring 30. |
| `zero_bonus_rate` | Fraction scoring 0. |
| `mean_parts_correct` | Mean number of the three parts answered correctly. |

### Shared keys

| Column | Definition |
|---|---|
| `tier` | `fall`, `winter`, `regionals`, or `nationals` — the chronological and difficulty axis. `tier_label` is the display form; `tier_rank` is 0–3 in season order. |
| `site` | Mirror-site name with the redundant year and tier prefix stripped. |

There is no `year` column anywhere in this folder: within one season it would be a relabelling of `tier`.

## Season structure

### `dataset_summary.csv` (26 rows)
Headline counts as `metric`/`value` pairs, including the season label, date range, progression counts, and both MDS stress values.

### `tier_summary.csv` (4 rows)
One row per tier in chronological order. Counts (`tournament_sites`, `teams`, `games`, `player_ids`, `tossup_questions`, `bonus_questions`, `roster_memberships`), the shared metric blocks, `mean_team_score`, and `median_abs_margin`. This is the table behind most headline claims.

### `site_summary.csv` (33 rows)
One row per mirror site: source metadata (`num_packets`, `level`, `start_date`), `teams`, `games`, `mean_tossups_read`, `mean_team_score`, `median_abs_margin`, and the shared metric blocks.

### `outcome_summary.csv` (12 rows)
One row per tier × outcome (`Correct (+10)`, `Neg (-5)`, `Zero (0)`), with `share_within_tier` and that outcome's median position.

## Players and progression

### `player_summary.csv` (1,339 rows)
One row per player ID with at least one buzz in the season. Adds `tournaments`, `games`, `tiers_played` (1–4), `points_per_attempt` (mean raw `value`), `entry_tier` (earliest tier played), and `furthest_tier` (latest tier played).

### `player_tier_summary.csv` (1,902 rows)
One row per player ID × tier — the per-event breakdown behind the progression analysis.

### `player_retention.csv` (16 rows)
Every ordered tier pair. `overlap` is the number of players appearing in both; `share_of_from` is that as a fraction of the `from_tier` player count. The matrix is **not** symmetric in `share_of_from` because the tiers have different field sizes: 25% of Fall players also played Regionals, but 27% of Regionals players also played Fall.

### `field_composition.csv` (4 rows)
Per tier: how much of the field had already appeared earlier *in this season*. `seen_earlier_id_share` is over distinct players, `seen_earlier_buzz_share` over attempt volume. Fall is 0 by construction.

### `selection_on_fixed_set.csv` (9 rows)
The selection analysis. Each row is one (fixed question set, furthest tier reached) cell: `players`, `mean_scored_accuracy`, and `mean_position_pct` measured **only on the fixed set**, among players with at least 20 attempts on it. Holding the set fixed removes the difficulty confound. See the caveats in [METHODOLOGY.md](METHODOLOGY.md).

## Teams and games

### `team_summary.csv` (492 rows)
One row per team entry. Adds `roster_size`, `games`, `wins`, `win_rate`, `points_per_game`, `mean_margin`, and the shared metric blocks. Unfiltered — apply the thresholds in [METHODOLOGY.md](METHODOLOGY.md) before ranking.

### `team_game_results.csv` (5,322 rows)
Games exploded to one row per side: `score`, `opponent_score`, `margin`, `win`/`loss`/`tie`, `tossups_read`. Exactly two rows per game.

### `team_metric_correlations.csv` (12 rows)
Pearson correlation matrix over twelve team metrics, on the 480 stable team entries.

## Questions

### `tossup_question_summary.csv` (1,360 rows)
One row per tossup: `num_tokens`, `num_clues`, `category_group`, `answer_clean`, plus the buzz metric block over every attempt on that question. `mean_scored_position_pct` excludes value-0/no-buzz rows; `conversion_rate` aliases `accuracy_all_attempts`.

### `bonus_question_summary.csv` (1,359 rows)
One row per bonus, with `num_parts`, `leadin_tokens`, and the bonus metric block.

### `bonus_part_summary.csv` (12 rows)
Conversion by tier × declared part difficulty. `observations` is the part-attempt count.

### `category_summary.csv` (11 rows)
One row per category, pooled over the season. Both metric blocks plus `tossup_questions` and `bonus_questions`. There is no `Unknown` row.

### `category_by_tier.csv` (42 rows)
The same split by tier, with per-tier `tossup_questions` counts.

## Timing

### `position_decile_pooled.csv` (10 rows)
Season-wide position deciles with `accuracy`, `scored_accuracy`, `neg_rate`, and `zero_rate`. This is the table behind the value-0 artifact figure.

### `position_decile_summary.csv` (40 rows)
The same split by tier. Empty deciles are present with zero counts.

### `timing_band_summary.csv` (16 rows)
Quartile resolution by tier.

## CompIRT adjustment diagnostics

### `clue_phase_summary.csv` (40 rows)
Ten within-clue phase bins for correct, neg, all scored, and scored phase-0 first buzzes. `observed_share` is compared with `uniform_expected_share`, the token opportunity in the same questions weighted by their observed buzz counts; `enrichment` is their ratio.

### `clue_boundary_summary.csv` (4 rows)
Exact sentence/clue-boundary share and uniform-opportunity expectation for correct, neg, all scored, and scored phase-0 first buzzes.

### `player_parameter_stability.csv` (3 rows)
Adjacent tier pairs. `timing_residual_correlation` and `correctness_residual_correlation` compare returning players after question-centering, requiring `minimum_scored_attempts_per_tier` in both tiers.

### `category_specialization_sensitivity.csv` (4 rows)
Early-half/late-half player×category specialty repeatability at minimum cell sizes 5, 8, 10, and 15. Reports eligible cells, distinct players, and timing/correctness correlations.

### `category_specialization_stability.csv` (478 rows)
The paired player×category cells behind figure 28 at the displayed 10-attempt threshold: early/late counts, raw question-centered category residuals, general player residuals, specialties, and metric (`timing` or `correctness`).

### `question_signal_correlations.csv` (5 rows)
Pooled plus four within-tier question-level correlations among mean scored-buzz position, zero rate, scored accuracy, and all-attempt accuracy.

## Data quality

### `missingness_summary.csv` (16 rows)
Per checked field: `rows`, `missing`, `missing_rate`. Missing means null, empty or whitespace-only string, or empty list.

### `validation.json`
Scope checks, referential checks, known quality items, and MDS fit statistics. See [METHODOLOGY.md](METHODOLOGY.md).

## MDS

Two grains, three files each. See [MDS.md](MDS.md).

| File | Rows | Contents |
|---|---:|---|
| `team_mds_coordinates.csv` | 480 | Identity columns plus `mds1`, `mds2`. |
| `team_mds_features.csv` | 480 | `raw_*` inputs and `z_*` standardized inputs. |
| `team_mds_loadings.csv` | 12 | Correlation of each standardized feature with each axis. |
| `site_mds_coordinates.csv` | 33 | As above, mirror sites. |
| `site_mds_features.csv` | 33 | |
| `site_mds_loadings.csv` | 10 | |

Coordinates are identified only up to reflection and rotation. Interpret axes through the loadings files, never through the raw sign of a coordinate.
