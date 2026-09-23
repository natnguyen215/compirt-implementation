# Held-out studies that span model families

`common/` is not a model family. It holds runs whose question is about the data
or about several families at once, so filing them under `baseline/` or
`double-difficulty/` would be misleading.

| Run directory | Written by | What it holds |
| --- | --- | --- |
| `paper-readiness-tossups/` | [`analysis/correctness/paper_readiness/`](../../../../analysis/correctness/paper_readiness/) | Fixed-specification correctness baselines, the coverage and likelihood audits, and the paired cluster bootstrap |
| `tossup-accuracy-study/` | [`analysis/correctness/tossup_accuracy_study/`](../../../../analysis/correctness/tossup_accuracy_study/) | Validation-selected splines, frozen timing skills, boosted trees, the tree/spline ensemble, exported predictors, and `timing_comparison/` |
| `bayesian-mark-study/` | [`analysis/correctness/bayesian_mark_study/`](../../../../analysis/correctness/bayesian_mark_study/) | Variational Bayes and Bayesian/prefix mixture fits on the point study's exact inner splits |
| [`bonus-team-irt/`](bonus-team-irt/2026-09-17/README.md) | [`analysis/bonus_team_irt/`](../../../../analysis/bonus_team_irt/README.md) | Direct team-vector bonus IRT, matched saved compositional references, game margins, and subject/difficulty breakdowns |
| `bad-experiments/` | [`archive/neg_test/run_neg_test.py`](../../../../archive/neg_test/run_neg_test.py) | Retired neg/buzz cross-validation configurations, kept as a record of what was tried and rejected |
| [`token-threshold-replay/`](token-threshold-replay/2026-09-13/README.md) | `replay_research_log_outcomes.py`, kept beside its results | Token-threshold game, round, and PPG replay of 15 saved held-out model arms for the Research Log tables |
| [`game-winner-ablations/`](game-winner-ablations/2026-09-16/README.md) | `code/compare.py`, kept beside its results | Skills-only LSE, correctness-only scoring at observed buzz positions, and full tossup replay on matched games |
| `parallel-normalized-v1-20260913-150350/`, `parallel-dd-normalized-v1-10000-20260913-195429/` | [`run_scripts/common/run_parallel_game_holdout.py`](../../../../run_scripts/common/run_parallel_game_holdout.py) and its GPU queue | Queue state, logs, and comparison reports for the normalized-likelihood refits written to `double-difficulty/` and `multidim/` |

The first three are one research line, evaluated under one shared protocol. Read
[`analysis/correctness/README.md`](../../../../analysis/correctness/README.md)
before comparing numbers across them: they score the same 45,995 held-out first
buzzes on the same five whole-game folds, conditioning on the observed buzzer and
position. The consolidated table is
[`docs/correctness-benchmarks.md`](../../../../docs/correctness-benchmarks.md).

`bad-experiments/` was written under an older `results/neg_test` root, before
`resolve_result_root` forced runs into a tier; its `run.log` still records that
original path. Its name is a judgment about the configurations, not about the
runs being corrupt. The retained neg/buzz comparison is documented in
[`archive/neg_test/README.md`](../../../../archive/neg_test/README.md).

These are held-out runs, but read each study's protocol before calling any of
them a generalization estimate — the correctness folds have been reused
repeatedly for development.
