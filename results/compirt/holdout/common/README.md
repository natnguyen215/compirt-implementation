# Held-out studies that span model families

`common/` is not a model family. It holds runs whose question is about the data
or about several families at once, so filing them under `baseline/` or
`double-difficulty/` would be misleading.

| Run directory | Written by | What it holds |
| --- | --- | --- |
| `paper-readiness-tossups/` | [`analysis/correctness/paper_readiness/`](../../../../analysis/correctness/paper_readiness/) | Fixed-specification correctness baselines, the coverage and likelihood audits, and the paired cluster bootstrap |
| `tossup-accuracy-study/` | [`analysis/correctness/tossup_accuracy_study/`](../../../../analysis/correctness/tossup_accuracy_study/) | Validation-selected splines, frozen timing skills, boosted trees, the tree/spline ensemble, exported predictors, and `timing_comparison/` |
| `bayesian-mark-study/` | [`analysis/correctness/bayesian_mark_study/`](../../../../analysis/correctness/bayesian_mark_study/) | Variational Bayes and Bayesian/prefix mixture fits on the point study's exact inner splits |
| [`bonus-team-irt/`](bonus-team-irt/team-skills-1d-gamma-alpha-3d-simplex-relevance-5fold/README.md) | [`analysis/bonus_team_irt/`](../../../../analysis/bonus_team_irt/README.md) | Saved Team IRT fits; current results are in the [shared bonus comparison](../../comparisons/bonuses/dd-bernstein-and-team-irt-5fold/README.md) |
| [`bad-experiments/`](bad-experiments/) | [`archive/neg_test/run_neg_test.py`](../../../../archive/neg_test/run_neg_test.py) | Retired neg/buzz cross-validation configurations, kept as a record of what was tried and rejected |
| [`token-threshold-replay/`](token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/README.md) | `replay_research_log_outcomes.py`, kept beside its results | Token-threshold game, round, and PPG replay of 15 saved held-out model arms for the Research Log tables |
| [`game-winner-ablations/`](game-winner-ablations/skills-lse-observed-position-correctness-and-token-replay-5fold/README.md) | `code/compare.py`, kept beside its results | Skills-only LSE, correctness-only scoring at observed buzz positions, and full tossup replay on matched games |
| [`execution/`](execution/) | [`run_scripts/common/run_parallel_game_holdout.py`](../../../../run_scripts/common/run_parallel_game_holdout.py) and its GPU queue | Queue state, logs, and comparison reports for the normalized-likelihood refits written to `double-difficulty/` and `multidim/` |

The first three are one research line, evaluated under one shared protocol. Read
[`analysis/correctness/README.md`](../../../../analysis/correctness/README.md)
before comparing numbers across them: they score the same 45,995 held-out first
buzzes on the same five whole-game folds, conditioning on the observed buzzer and
position. The consolidated table is
[`docs/correctness-benchmarks.md`](../../../../docs/correctness-benchmarks.md).

[`bad-experiments/`](bad-experiments/) was written under an older `results/neg_test` root, before
`resolve_result_root` forced runs into a tier; its `run.log` still records that
original path. These are historical calibration comparisons with test-period
parameter fitting, distinct from frozen replay. Their results are documented in
[`archive/neg_test/README.md`](../../../../archive/neg_test/README.md).

These are held-out runs, but read each study's protocol before calling any of
them a generalization estimate — the correctness folds have been reused
repeatedly for development.
