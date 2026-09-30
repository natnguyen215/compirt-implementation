# Repository guidance

Quizbowl IRT builds linked Hugging Face tables from SQLite and fits models of
player and team performance. Run commands from the repository root using the
project-local virtual environment. Read a directory's local `CLAUDE.md` when
present for additional model-specific instructions. Those guides are ignored
by Git; public contracts belong in the tracked READMEs and `docs/`.

## Setup and checks

Environment setup is in `README.md`; suite commands and discovery rules are in
`tests/README.md`; dataset rebuilding (requires the ignored `data/database.db`)
is in `data/README.md`. The complete check is:

```bash
.venv/bin/python -B run_scripts/common/check_repo.py
```

Add `--include-data-validation` when generated data is available. Use pytest
for the root and correctness-study suites (they mix unittest classes with bare
functions). Tests must not run full experiments or write under `results/`.
There is no configured formatter. Do not rebuild data or train models just to
validate a documentation change.

## Code map

`README.md` maps the repository. Live code must not import from `archive/`, and
checks do not run its tests.

## Model and data contracts

Ordinary CompIRT fits Stage-1 player skills `theta` and tossup parameters with
`AutoNormal` SVI, then freezes `theta` while fitting bonus parameters. Stage 2
uses literal, roster-size-unnormalized log-sum-exp aggregation (Eq. 8), optional
pairwise synergy (Eq. 10), and Bernoulli part outcomes (Eq. 11). Optional Eq. 9
Noisy-OR uses scalar difficulty inside each member's sigmoid, no temperature,
and no synergy or calibration; frozen replay reads `bonus_aggregation` from
the fit summary (missing means LSE).

Scalar difficulty uses `theta_i · alpha_j - b_j(t)`; per-dimension difficulty
uses `sum_k r_jk * (theta_ik - d_jk(t))`. Double-difficulty families separate
correctness and hazard curves; perception families transform shared evidence
with player parameters. Inspect imports before assuming a baseline fix
propagates: some families share helpers and others implement their own math.

Preserve the discrete sigmoid-hazard first-buzz law in `compirt_race.py`:

```text
h_i(t) = sigmoid(eta_i(t))
q(t) = product_i (1 - h_i(t))
P(winner i at t | survived to t) = (1 - q(t)) * softmax(eta(t))_i
P(dead tossup) = product_{t=1..T_j} q(t)
```

Use all active players in the stopping-cell risk set. Individual sigmoid
hazards are not exclusive-winner probabilities. Dead races survive through
`T_j`; observed-buzz survival stops before the event cell. Keep training,
prediction, evaluation, and simulation consistent with
`docs/first-buzz-likelihood.md`. Current summaries record
`first_buzz_likelihood = normalized_hazard_odds_v1` and
`terminal_no_buzz_survival = tokens_1_through_T`. Older fits need a fresh refit
to adopt this likelihood; replay does not repair their fitted parameters.

Observations include `BUZZ`, `CENSORED`, and `NO-BUZZ` rows. Baseline and
multidimensional Stage 1 optionally include opponent-only bounceback phases.
Those enter fitting but must not duplicate players in phase-0 diagnostics.
Preserve event order, masks, and question lengths (`utils/prediction.py`).
Games without lineup evidence fall back to full rosters; bonuses reuse the
cycle's inferred lineup. Player identity uses exact raw-slug matching.

## Evaluation and experiments

The standard evaluator replays saved fits without retraining. Metric changes
must update populations, aggregation order, and artifacts in
`compirt_eval/METRICS.md`.

Scenario A separates reconstruction, survival/identity scoring, timing figures,
and outcome replay. Games and PPG use the same token-threshold tossup replay
(`compirt_eval/scenario_a_tossups/outcomes.py`), with 0.5 buzz/correctness
thresholds, team lockout, and opponent
continuation. Preserve incomplete-game exclusions and cache invalidation.

Distinguish in-sample diagnostics, transductive holdout (test question
parameters fitted using cross-split player priors), and frozen matrix infill
(training parameters replayed without test fitting). Whole-game frozen splits
enforce entity coverage. Reused development folds are not untouched tests.
Synergy is not an established teamwork measure; latent skill axes are not
identified player traits.

Run root trainers as files and family trainers as modules from the root.
Environment-driven pipelines do not provide CLI `--help`; read their settings
or `run_scripts/README.md`. CLI study runners do expose `--help`. Extend
configurable runners instead of adding launchers per seed, dimension, or
calibration setting. Record configuration and seeds; trainer seed support
varies. `COMPIRT_SURVIVAL_CHUNK` controls memory in models that call
`utils.training.survival_chunk_size`; inspect callers before extending it.

Pipeline roots go through `resolve_result_root` in `utils/run_logging.py`. Runs
normally use `results/compirt/{in_sample,holdout}/<family>/<run>/`;
cross-family studies use `common/`, and comparisons use
`results/compirt/comparisons/`. Descriptive EDA writes beside its code;
correctness experiments use `holdout/common/`. Use fresh roots for changed
configurations or likelihoods. Preserve saved artifacts and marker-based
resume. Delete runners for finished experiments (git history keeps them); code
for completed evaluation studies lives in a `code/` folder beside its results.

## Documentation

Edit reports and research logs directly in Markdown. Do not build report
generators, comparison frameworks, or tests for a reporting/documentation task,
and do not run test suites just to validate prose or tables. Short calculations
or data extraction are fine when needed for accurate numbers; keep them minimal.
Use the existing metric outputs and consolidate summaries instead of producing
duplicate reports. Preserve existing explicitly generated-document contracts.

Start at `docs/README.md`; use `docs/code-guide.md` for data contracts, model
math, and code paths, `docs/compirt-experiments.md` for commands,
`docs/dataset-schema.md` for tables, and `results/README.md` for output layout.
Add new documents to the index; put a report about one set of runs beside those
runs instead of in `docs/`. `docs/correctness-benchmarks.md` is generated by
`analysis/correctness/tossup_accuracy_study/report.py`; edit its generator.
`RESEARCH_LOG.md` records findings. Local context notes and historical reports
may predate current code; verify their claims against the implementation.
