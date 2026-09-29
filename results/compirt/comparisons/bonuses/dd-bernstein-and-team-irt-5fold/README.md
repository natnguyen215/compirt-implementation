# Bonus comparison data

The [bonus research log](../../../../../RESEARCH_LOG_2.md) is the single written
report for DD-Bernstein, multidimensional references, and Team IRT 1D and 3D.
Edit that Markdown directly. This directory retains the data supporting its
matched comparison, without a separate report generator or duplicate report.

All seven models score 127,986 parts / 42,662 bonuses / 2,330 complete games.
DD uses frozen 3D skills from the normalized first-buzz likelihood. Whole-game
exclusions enforce training entity coverage and complete predictions for every
model. The original fitted models remain in their source directories.

- [Overall scores](aggregate/metrics.csv) and [fold scores](aggregate/metrics_by_fold.csv).
- [Question and roster strata](aggregate/metrics_by_question_type.csv).
- [Concrete question examples](../../../../../examples.md): helpful and harmful synergy flips,
  plus the highest fitted bonus difficulty in each dimension.
- [Excluded games](aggregate/excluded_games.csv) and `fold_N/split.json`.
- `aggregate/<model>/`: team-game predictions, team PPG, tournament scores, and margins.
- [Configuration](configuration.json) and [sources](aggregate/evaluation_sources.json):
  source paths, hashes, training budgets, and population provenance from the
  completed calculation. Code hashes record the calculation at the time;
  its temporary comparison/report machinery has been removed.
- [code/rescore_team_irt.py](code/rescore_team_irt.py): rescored the Team IRT
  rows and `aggregate/team_irt_*d/` on 2026-09-25, when the simplex-relevance
  Team IRT 3D replaced the earlier Gamma-loading arm. Its `--check` mode
  reproduced the previous rows to within 4e-15 before replacement. It also prints Team IRT
  in-sample scores. Other models' rows are unchanged.

The [metric contract](../../../../../compirt_eval/METRICS.md#bonus-model-comparison)
defines the populations and aggregation.
