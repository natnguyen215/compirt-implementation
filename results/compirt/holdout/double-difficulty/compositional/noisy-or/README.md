# Noisy-OR bonuses from frozen DD-Bernstein skills

This run implements the paper's Eq. 9, using the same five `year_2024`
whole-game folds and frozen 3D skills as
[`no-synergy-and-dot-additive-1d`](../no-synergy-and-dot-additive-1d/aggregate/report.md).
Each fold fits scalar part difficulty and Gamma(2,2) discrimination for 3,000
AutoNormal SVI steps, learning rate 0.01, optimization and split seed 42.
There is no temperature, synergy, or correctness calibration. Predictions
freeze the training posterior medians. These are reused development folds.

The [bonus research log](../../../../../../RESEARCH_LOG_2.md) contains the
comparison tables. Its Noisy-OR row uses exactly the shared comparison's
127,986 parts / 42,662 bonuses / 2,330 games, including the two game exclusions
needed for Team IRT coverage. The ordinary [pooled report](aggregate/report.md)
retains all 128,100 parts / 42,700 bonuses / 2,332 compositional games.

Saved scores and provenance:

- [Configuration and source hashes](configuration.json), per-fold command
  manifests, train/replay summaries, and evaluation reports.
- [Matched metrics](aggregate/matched_metrics.json),
  [matched population and prediction hashes](aggregate/matched_population.json),
  and [fold scores](aggregate/matched_per_fold.csv).
- [Minority precision/recall/F1](aggregate/matched_minority_metrics.csv) and
  [familiar/new-roster metrics](aggregate/matched_roster_metrics.csv).
- [Training diagnostics](aggregate/training_metrics.json): pool training
  predictions, keeping team and response identities distinct by fold.
- [Validation](validation.json) and [repository check output](repository_checks.log).

Matched metrics call the existing bonus scorer on each comparison
`fold_N/split.json`'s `scored_game_ids`. Saved observed part identities and
outcomes are checked against the DD baseline before scoring. Roster familiarity
uses the exact team and active-player set in that fold's training bonuses.
Minority precision/recall/F1 uses incorrect as positive for easy and correct
for medium/hard, pooling counts at correctness threshold 0.5.

Reproduce from the repository root:

```bash
.venv/bin/python -B -m run_scripts.common.run_compositional_from_folds \
  --stage1-root results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps \
  --root results/compirt/holdout/double-difficulty/compositional/noisy-or \
  --arms compositional --bonus-aggregation noisy-or \
  --steps 3000 --lr 0.01 --seed 42 --alpha-prior gamma --device cuda
```

For a new fit after implementation changes, use a fresh output root. The
original launch configuration retains its code hashes; `--collect-only`
refreshes full-population aggregates without fitting. `aggregate/matched_*`
records the additional population restriction used in the research log.

Tests, Pyflakes, and whitespace checks passed. Optional full-dataset validation
found the local generated tables and SQLite source have different row counts
(77 versus 68 tournaments, for example). No dataset was rebuilt: this run
retains the comparison's existing generated tables and verifies the matched
observed outcomes directly.
