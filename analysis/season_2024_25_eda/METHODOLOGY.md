# Methodology

## Scope

Everything is computed from the `all` split of the HuggingFace-style tables under `data/hf/quizbowl-irt/`, filtered to the **2024–25 competitive season**.

A tournament's season is derived from `tournaments.start_date`, cut at July: a start month of 7 or later belongs to season `Y-(Y+1)`, otherwise to `(Y-1)-Y`. This recovers the actual competitive calendar, in which Fall (October) and Winter (November) precede Regionals (January/February) and Nationals (April) of the following calendar year.

That selects 33 mirror sites spanning 2024-10-19 to 2025-04-19 across four tiers. Question sets are then scoped to the four events those sites actually played, and buzzes, bonus responses, teams, and players are scoped to those sites' games. Players are retained only if they have at least one buzz in the season.

The corpus holds three seasons — 2023–24 (Regionals and Nationals only), 2024–25 (complete), and 2025–26 (Fall and Winter only). **2024–25 is the only complete one**, which is why it gets its own analysis.

## Why year is not an axis

Within this season, calendar year is perfectly collinear with tier: Fall and Winter are 2024, Regionals and Nationals are 2025. Splitting by year would just relabel the tier axis. Every figure therefore uses tier, which is simultaneously the chronological axis and the difficulty axis.

The flip side is that **tier confounds difficulty with calendar time**. Nothing in this folder can separate "this set was harder" from "this event happened later in the season, with a different field". Section 5 of [EDA_REPORT.md](EDA_REPORT.md) gets closest by holding the question set fixed and varying only the players.

## Grains

- **Question-set event** (4) — a shared packet set, e.g. `2025-acf-regionals::2025-02-01`. Tossups and bonuses live here.
- **Mirror site** (33) — one tournament at one location. Games and team entries live here.
- **Team entry** (492) — one team at one mirror site, `tournament_id::team_slug`. No cross-tournament team identity exists, so a program at three tournaments is three team entries.
- **Player ID** (1,339 with a buzz) — a raw player slug, shared across tournaments. The only identifier that links across events, and therefore the only one that supports the progression analysis.

## Transformations

**Buzz position.** `position_pct = 100 * token_position / num_tokens_total`, clipped to [0, 100]. 53 attempts exceed the token count before clipping and are retained. Positions are always a percentage of the question revealed, never raw tokens, because question length varies substantially across tiers.

**Outcome coding.** `value` is `+10`, `−5`, or `0`. Two denominators are used and always labelled:

- **All-attempt accuracy** = correct / all attempts. Treats value-0 attempts as failures.
- **Scored accuracy** = correct / (correct + negs). Excludes value-0 attempts.

They differ by 4.5 points season-wide (76.6% against 82.1%) and the gap grows with tier difficulty, which is the subject of section 2 of the report. No figure or table mixes them without saying which it uses. Where a single measure had to be chosen for a player- or category-level statistic, **scored accuracy is the default here**, because the value-0 rate varies so strongly across tiers that all-attempt accuracy would mostly be measuring set difficulty.

**Timing bands.** Deciles and quartiles of `position_pct` with left-closed bins.

**Bonus metrics.** PPB is the mean of `total_points` over bonuses heard. Parts are exploded to one row per part (147,126 observations) and labelled with the declared easy/medium/hard modifier; nonstandard modifiers are kept verbatim.

**Categories.** Cleaned of HTML entities and aliased into a fixed list (`Any History` to History, `Painting/Sculpture` and `Painting & Sculpture` to Fine Arts, `Geography` and `Current Events` to Geography/Current Events, `Popular Culture` to Pop Culture, `World/Other Literature` to Literature). **No question in this season is unlabelled**, so the `Unknown` bucket is empty and nothing is excluded.

**Team-game results.** Games are exploded to two rows, one per side. `games.final_scores` is the builder's derived score timeline.

## Sample thresholds

| Statistic | Threshold | Surviving |
|---|---|---:|
| Player-level accuracy and timing | at least 30 attempts | 718 of 1,339 |
| Selection on a fixed set | at least 20 attempts *on that set* | see `selection_on_fixed_set.csv` |
| Team-level metrics and team MDS | at least 5 games, 30 attempts, 15 bonuses heard | 480 of 492 |
| Site-level metrics and site MDS | none | 33 of 33 |

Per-question summaries are unfiltered, so questions carry noisy rates; figures using them plot distributions rather than rankings.

## The selection analysis

Section 5 of the report compares players by how far they later go in the season, measured **on a single fixed question set**. The design point is that fixing the set removes the difficulty confound: any cross-tier comparison of player performance mixes "this player is better" with "this set was harder", and holding the set constant leaves only the former.

Two honest caveats:

- It **conditions on an outcome**. Grouping players by how far they later go is selection, not development. Nothing here says a player improved; it says players who went further were already different on the earlier set.
- Cells are uneven. The Fall-set Nationals group is 17 players. The timing result is monotone across all three fixed sets and all cell sizes; the accuracy result is smaller and not monotone on the Fall set, and should be treated as the weaker of the two.

## Model-adjustment diagnostics

**Clue phase.** Every scored buzz is placed within the dataset-provided sentence span containing its (clipped) token position. Phase 0 is the first token after the previous boundary and phase 1 is the boundary token. First buzzes use the same event ordering as `compirt_data.py`: token position, then the numeric suffix of `buzz_id` as a deterministic tiebreaker. The displayed distribution uses scored phase-0 first buzzes; the CSVs also export correct, neg, and all-scored views. Each is compared with a uniform-token opportunity baseline from the *same tossups*, weighted by the number of buzzes observed on each tossup. This controls question length and boundary density, but it is not a survival model and does not assert that a constant token hazard is realistic. Exact-boundary counts use only explicit source boundaries; an appended terminal token used to close malformed spans is not marked as a boundary.

**Adjacent-tier player stability.** Only scored (+10/−5) buzzes are used. Timing and correctness are centered on their question means, then averaged by player×tier. Pearson correlations compare returning players in each adjacent tier pair with at least 20 scored attempts in both tiers. Question centering removes raw set/item level but does not remove selection, learning, lineup, or site effects.

**Category specialization.** The season is split into Fall+Winter and Regionals+Nationals. Scored-buzz timing and correctness are first question-centered. A player's all-category residual in that half is then subtracted from each player×category mean, leaving a relative specialty. Early and late specialties are correlated for cells clearing the same observation threshold in both halves. Thresholds 5, 8, 10, and 15 are all exported; 10 is the displayed analysis. This is a repeatability diagnostic, not an IRT dimension estimate, and sparse categories naturally disappear at stricter thresholds.

**Question-signal coupling.** Question-level mean scored-buzz position, no-buzz/value-0 rate, scored accuracy, and all-attempt accuracy are correlated pooled and within tier. Using scored-buzz position avoids mechanically moving mean timing later merely because value-0 rows sit at the question end.

## Statistics

All correlations are Pearson on the stated subset. **No significance tests, confidence intervals, bootstrap resampling, or multiple-comparison corrections are computed** — with 64,037 attempts nearly any correlation would be "significant", so effect sizes are the informative quantity.

Nothing here is a model fit. No latent skill is estimated and no held-out prediction is made. Every difficulty number is a raw rate confounded with who was in the room.

## Reproducibility

Fully deterministic: no sampling, no random initialization, no seed. Repeated runs are byte-identical given the same input tables.

```bash
MPLCONFIGDIR=/tmp/season_eda_mpl \
  .venv/bin/python -B analysis/season_2024_25_eda/analyze.py
```

Options: `--data-dir` (default `data/hf/quizbowl-irt`), `--output-dir` (default this folder), `--skip-figures`.

Dependencies are already in the project venv: `datasets`, `pandas`, `numpy`, `matplotlib`. MDS is implemented directly in NumPy, so scikit-learn is not required.

The script writes only into this folder's `data/` and `figures/`. It never writes under `results/` and never modifies the source tables.

`data/validation.json` records automated checks on every run: that the scope resolved to 33 sites, all four tiers, 4 events, and 64,037 attempts; that every buzz and bonus response resolves to a game and a question; that every game has two teams and two scores; and that every selected site really belongs to the season. All checks pass on the current build.
