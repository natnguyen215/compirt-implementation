# Direct team-skill IRT for bonus questions

This study fits one- and three-dimensional team IRT directly to bonus part
outcomes. It compares frozen predictions with four saved compositional
references on matched games.

## Reproduction

From the repository root, using the local generated dataset:

```bash
.venv/bin/python -B -u -m analysis.bonus_team_irt.run \
  --output-dir results/compirt/holdout/common/bonus-team-irt/2026-09-17 \
  --steps 3000
```

Run configuration, data signatures, reference hashes, and source hashes are
recorded in [configuration.json](configuration.json). Fit and split seeds are
42; the learning rate is 0.01. All five existing 2024 whole-game folds are
used. The saved reference models used 2,000 bonus-stage steps and their
existing player-skill sources; this is a predictive baseline comparison,
not an isolated ablation of parameterization under equal training budgets.

## Artifacts

- [Report](aggregate/report.md): existing bonus metrics, difficulty, PPG, margins, and category breakdowns.
- [Overall metrics](aggregate/metrics.csv) and [fold metrics](aggregate/metrics_by_fold.csv).
- [Question-type metrics](aggregate/metrics_by_question_type.csv): category,
  declared difficulty, and category x difficulty, with denominators.
- [Excluded games](aggregate/excluded_games.csv): identical exclusions for all arms.
- [Existing-metric parity audit](aggregate/existing_metrics_parity.csv): original
  published reference metrics reproduced within 1e-6; every retained reference
  game's observed/predicted margin and absolute error matches within 1e-10.
- `fold_N/split.json`: training games, original test games, scored games, counts.
- `fold_N/team_irt_{1,3}d/`: fitted parameters, team/part IDs and CSVs,
  posterior marginal quantiles, loss traces, fit summaries, frozen predictions.
- `aggregate/<model>/`: team-game points, pooled team PPG, tournament metrics,
  and signed bonus-only margins.
- `code/`: current study source snapshot. `configuration.json` and `run.log`
  retain the original fitting provenance; `aggregate/report_rendering.json`
  records the current renderer and metric inputs. The comparison contains six
  arms; retained metrics and fitted parameters are unchanged.

Refresh report formatting directly from the saved metric CSVs:

```bash
.venv/bin/python -B -m analysis.bonus_team_irt.report \
  --output-dir results/compirt/holdout/common/bonus-team-irt/2026-09-17
```

The parity audit can be rerun from the repository root:

```bash
PYTHONPATH=. .venv/bin/python -B \
  results/compirt/holdout/common/bonus-team-irt/2026-09-17/code/audit_existing_metrics.py
```

The maintained configurable implementation is
[`analysis/bonus_team_irt/`](../../../../../../analysis/bonus_team_irt/README.md).
Tests are in `tests/test_bonus_team_irt.py`; protocol details and interpretation
limits are in that package's README and the generated report. The research
summary is in [`RESEARCH_LOG_2.md`](../../../../../../RESEARCH_LOG_2.md).
