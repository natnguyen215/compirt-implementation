# Data quality

Issues in the 2024–25 season slice, how this analysis handles each, and what a downstream model should know. Machine-readable counts are in [data/missingness_summary.csv](data/missingness_summary.csv) and [data/validation.json](data/validation.json).

This slice is materially cleaner than the corpus as a whole. The corpus-wide issues are catalogued in [`../full_dataset_eda/DATA_QUALITY.md`](../full_dataset_eda/DATA_QUALITY.md); this file records only what actually applies here.

## Integrity checks that pass

All automated checks pass on the current build:

- Scope resolved as expected: 33 sites, all four tiers, 4 question-set events, 64,037 attempts.
- Every selected site really belongs to season 2024–25 by start date.
- Every buzz and every bonus response resolves to a game **and** to a question. No orphan observations, so no join drops rows.
- Every game has exactly two team IDs and exactly two final scores.

## 1. Category metadata is complete — the corpus's biggest gap does not apply

| Field | Missing | Rate |
|---|---:|---:|
| `tossups.category` | **0** | **0.0%** |
| `bonuses.category` | **0** | **0.0%** |
| `tossups.subcategory` | 398 | 29.3% |
| `bonuses.subcategory` | 398 | 29.3% |

The corpus's one unlabelled question set is 2024 Regionals (336 tossups, 336 bonuses), and it belongs to season **2023–24**, not this one. Every question in the 2024–25 season carries a category.

This is the strongest practical reason to prefer this slice for any category- or topic-conditioned work: the `topic/fixed/` family gets full supervision here with no set carved out.

Subcategory is missing for 29.3% of questions, spread across events, so it remains unusable as a grouping variable. No analysis here uses it.

## 2. Bonus responses with no earning player

10,892 of 49,042 bonus responses (**22.2%**) have an empty `earning_player_id`, essentially the same rate as the corpus overall (22.9%).

The builder links a bonus to the player whose correct tossup buzz earned it, matching on game, team, and packet question number, and leaves the field empty rather than guessing when the match is not unique.

**Handling.** Team-level bonus statistics use all 49,042 responses and are unaffected. This analysis produces **no** player-attributed bonus statistic, so the gap is never silently absorbed.

**Consequence.** The missingness is unlikely to be random — ambiguity is more probable in high-scoring games. The compositional Stage-2 model aggregates over the whole roster rather than the earning player, so it is not exposed; a model conditioning on the earner would be, at 78% coverage.

## 3. Player identity is raw-slug matching only

Identity is exact slug equality — no fuzzy matching, no manual linking. This is the limitation named in the root `CLAUDE.md`.

**It bears directly on the progression analysis.** Sections 4 and 5 of [EDA_REPORT.md](EDA_REPORT.md) track players across the four tiers of the season. A player whose registered slug changed between October and April is counted as two separate IDs and appears as two different one-tier players.

The direction of the bias is knowable: slug drift can only *understate* continuity. So the retention rates (3% of Fall players reach Nationals) and carry-over shares (72.1% of Nationals attempts from players seen earlier) are lower bounds, and the `tiers_played` distribution is skewed toward 1.

Two mitigating points. Within a single season the window is short — about six months — so drift has less opportunity than across years. And the *contrast* between tiers is more trustworthy than any single level, since slug drift is unlikely to correlate strongly with which tier a player attends.

The selection analysis in section 5 is affected differently: it only requires that a player's buzzes on one fixed set be correctly grouped, plus knowing their furthest tier. A drifted slug would place a player in a lower "furthest tier" bucket than they belong in, which would *attenuate* the observed gaps. The reported effects are therefore conservative.

## 4. Buzz positions beyond the end of the question

53 attempts have `token_position > num_tokens_total`. The cause is the moderator-instruction offset subtraction interacting with sanitized token counts.

**Handling.** Clipped to [0, 100]; the unclipped count is recorded in `validation.json`. At 53 of 64,037 attempts (0.08%) this cannot move any aggregate.

## 5. Nationals is one site, and the tier axis confounds difficulty with time

Not defects in the data, but the two structural facts most likely to cause a misreading.

**Nationals is a single invitational site** with 48 team entries and 182 players, against 8–14 sites and 500–674 players at the other tiers. Every Nationals statistic is one tournament with a selected field. Its apparent "easiness" relative to Regionals on all-attempt accuracy (0.747 vs 0.734) and PPB (15.26 vs 14.18) is partly a stronger field, not only an easier set, and these descriptive statistics cannot separate the two.

**Tier is simultaneously the difficulty axis and the calendar axis.** Within one season, "this set was harder" and "this happened later, with a different field" are the same variable. Nothing in this folder resolves that. The fixed-set selection analysis is the closest available approach, because it varies players while holding questions constant.

## 6. What is *not* a data quality problem

- **Value-0 attempts (4,269, 6.7%).** Genuine end-of-question events — 13.7% of final-decile attempts — not missing data. They do force a choice of denominator, and this folder defaults to scored accuracy for that reason. See [METHODOLOGY.md](METHODOLOGY.md).
- **Uneven tier sizes** (8 Fall sites against 14 Regionals). Real variation in how many mirrors ran.
- **Only 7 players appearing at all four tiers.** A real feature of the sport, not a linkage failure — most players attend one or two events a season. Slug drift makes this a lower bound, but the order of magnitude is genuine.

## Summary for downstream use

| Issue | Scale | Blocks what |
|---|---|---|
| Bonus earning player unlinkable | 22.2% of responses | Player-attributed bonus statistics |
| Raw-slug identity only | Unquantified | Exact progression counts; biases continuity downward |
| Subcategory absent | 29.3% of questions | Subcategory-level grouping |
| Position overruns | 53 attempts (0.08%) | Nothing material; clipped |
| Nationals is one site | 182 players | Treating Nationals rates as a tier average |
| **Category metadata** | **complete** | **nothing — this is the clean slice** |
