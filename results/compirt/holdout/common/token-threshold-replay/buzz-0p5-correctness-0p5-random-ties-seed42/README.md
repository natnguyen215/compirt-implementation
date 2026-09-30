# Research Log token-threshold replay, September 13, 2026

This rerun evaluates the 15 saved historical model arms listed in `models.json`
on their five whole-game held-out folds. It does not train models or select
parameters. `model_metrics.csv` supplies the downstream Research Log tables.

Each tossup is read from token 1 through its terminal cell. An eligible player
buzzes when their current-token probability reaches 0.5. Same-token ties use
uniform random choice with seed 42 and a stable event-ID hash. Calibrated
correctness of at least 0.5 earns +10. An early first miss earns -5 and locks
out that team; the opponent continues from the next token. Terminal and
bounceback misses earn zero. Questions with no threshold crossing are dead.
Ground truth uses literal recorded tossup scores; bonuses are excluded from
all predicted scores. The saved player correctness intercept `a` is included
when present.

The replay script is kept beside these results. It locates the repository root
from `run_scripts/common/`, so copy it there before rerunning from the
repository root:

```bash
cp results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/replay_research_log_outcomes.py \
  run_scripts/common/
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .venv/bin/python \
  run_scripts/common/replay_research_log_outcomes.py \
  --manifest results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/models.json \
  --output-dir results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42 \
  --workers 10
```

Completed folds are reused only when source file sizes/modification times,
reconstruction code hashes, replay schema, and seed match `complete.json`.
The literal scoring and game metadata come from the local source dataset for
each saved split. Reevaluate into a fresh directory if that dataset changes.

- `fold_metrics.csv`: one row per model/fold, including eligible event/game
  counts and the number of incomplete games excluded.
- `model_metrics.csv`: unweighted means of five fold-level event/game metrics;
  tournament PPG metrics instead pool all disjoint held-out game/player rows,
  rank each tournament once, and macro-average across tournaments.
- `replay_diagnostics.csv`: replay no-buzz/no-score rates, tied and 0–0 game
  rates, team tossup-point MAE (pooled and round-macro, with the all-zero
  baseline), and unweighted tournament-round accuracy/margin summaries.
- `validation.json`: all 75 folds pass trace/player/game score-conservation
  checks; all models share identical targets matching raw recorded buzz scores.
- `game_coverage.csv`: the scored game IDs for each model.
- `<model>/fold_<n>/csvs/`: per-event buzz sequences, player points, games,
  rounds, rankings, and metric rows.
- `<model>/pooled_game_predictions.csv`: the model's complete held-out games.
- `<model>/pooled_round_metrics.csv`: summaries over the same games by
  tournament and round.
- `<model>/pooled_player_ppg_leaderboard.csv` and
  `pooled_player_ranking_metrics.csv`: full-tournament PPG and ranking results.

Actual tossup ties are omitted only from decisive-winner accuracy, not margin
error or PPG. Each inferred-lineup game contributes once to a player's PPG
denominator, even if the player never buzzes. Incomplete games are excluded
from all scoring totals. These seeded replays do not produce winner
probabilities, so game-winner Brier and log loss are retired.

The previous probability-based tables are preserved in
[the historical snapshot](superseded-probability-tables.md).

## Complete-game coverage

The rerun excludes `2024-acf-winter-at-clemson::game-674`: source metadata
reports 21 tossups read, while its saved prediction rows cover only 20. This
removes the whole game from scores and PPG denominators. The retained shared
population is 46,620 tossups (45,976 with a recorded buzz) and 2,331 games.
The upstream timing/correctness tables retain their original 46,640-event
coverage and are separate historical evaluations.
