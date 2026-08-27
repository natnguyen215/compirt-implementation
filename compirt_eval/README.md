# compirt_eval: the CompIRT evaluation suite

This package turns training runs into metrics, figures, readable reports, and
standalone evaluation studies. Its central boundary is narrower than “nothing
here ever fits”: **the standard `evaluate_compirt.py` pipeline never retrains a
model**. It deterministically replays artifacts the trainers already saved, so
ordinary evaluation can be rerun, extended, or debugged without changing a fit.

Every standalone command and argument parser lives under `run_scripts/`; the
corresponding package here owns reusable calculation, simulation, fitting, and
artifact-writing logic. Parameter recovery still performs a bounded synthetic
refit because that refit is the study itself, but its command follows the same
runner convention.

This file is the developer guide: how data flows through the package, what
every input and output file is, which module owns what, and how to extend it.
The mathematical definitions live in [`METRICS.md`](METRICS.md) (the
contract) and [`docs/METRICS.md`](docs/METRICS.md) (interpretation guidance);
see the [document map](#document-map) at the end.

## Source layout at a glance

```text
compirt_eval/
├── common/                 shared metric, figure, path, and report primitives
├── scenario_a_tossups/     standard Stage 1 / tossup evaluation
├── scenario_b_bonuses/     standard Stage 2 / bonus evaluation
├── scenario_c_rosters/     opt-in roster-generalization study logic
├── diagnostics/            cross-cutting PPC and real-match simulation checks
├── parameter_recovery/     standalone synthetic generate/refit/recovery study
├── imaginary_tournament/   standalone saved-fit tournament simulation
├── noise_floor/            identical-data seed-stability analysis
├── drop_robustness/        random and targeted event-drop analysis
├── player_rankings/        fitted-versus-observed ranking comparison
├── synergy_comparison/     no-synergy versus synergy metric comparison
└── docs/                   interpretation and scope documentation

run_scripts/                every executable command and argument parser
```

The `scenario_*` names follow the paper: Scenario A means tossups, Scenario B
means bonuses, and Scenario C means roster generalization. A conceptual family
in `EVALUATION_TLDR.md` does not necessarily need a same-named package: small
cross-cutting checks live together in `diagnostics/`. Standalone studies do
have same-named implementation packages, while their executable commands live
under `run_scripts/`. The TL;DR’s implementation column is the quickest map
from an output family to its source owner and runner.

## Quick start

```bash
# Evaluate one finished two-stage run (from the repo root):
.venv/bin/python evaluate_compirt.py \
  --pyramidal-results results/compirt/in_sample/<run>/pyramidal \
  --compositional-results results/compirt/in_sample/<run>/synergy \
  --output-dir results/compirt/in_sample/<run>/synergy-evaluation

# Optional flags: --split/--tournament (games table filter for the match
# simulation), --game-simulations 500, --game-seed 42, --skip-game-simulation.

# Compare the no-synergy and synergy bonus branches of one run
# (each flag points at a bonus_metrics.csv; flat and csvs/-nested
# evaluation layouts both resolve):
.venv/bin/python run_scripts/common/run_synergy_comparison.py \
  --compositional-metrics results/compirt/in_sample/<run>/evaluation/bonus_metrics.csv \
  --synergy-metrics results/compirt/in_sample/<run>/synergy-evaluation/bonus_metrics.csv \
  --output-dir results/compirt/in_sample/<run>/comparison

# Rank players by fitted conditional buzz accuracy vs actual PPG/PP20:
.venv/bin/python run_scripts/common/run_player_rankings.py --help

# Fit or analyze the retained identical-data SVI seed study:
.venv/bin/python \
  run_scripts/multidimensional/multidim/run_multidim_noise_floor.py --collect-only

# Run the bounded synthetic parameter-recovery study:
.venv/bin/python \
  run_scripts/multidimensional/multidim/run_parameter_recovery.py --help

# Simulate randomized games from completed Stage 1 and Stage 2 fits:
.venv/bin/python run_scripts/common/run_imaginary_tournament.py --help
```

The `--output-dir` name matters: `common/reports.py` (`bonus_stage_name`)
infers the bonus branch from it (`synergy-evaluation` reads the `synergy/`
stage folder, anything else reads `compositional/`), and infers the
evaluation-regime caveat from the enforced results tier in the path
(`results/compirt/{in_sample,holdout}/...`).

## Data flow

```
train_pyramidal.py          train_compositional.py [--synergy]
        |                            |
        v                            v
  <run>/pyramidal/             <run>/{compositional,synergy}/
  players.csv                  bonus_part_predictions.csv
  tossups.csv                  team_predictions.csv
  tossup_predictions.csv       posterior_predictive_checks.csv
  buzz_event_predictions.csv   summary.json
  posterior_predictive_checks.csv
  player_buzz_summary.csv
  summary.json
        \                           /
         \                         /
          v                       v
        evaluate_compirt.py  (this package)
                  |
                  v
        <run>/<evaluation-dir>/
          experiment_report.md      docs/summary.md
          csvs/*.csv                graphs/<group>/*.png
```

The trainers also *use* two pieces of this package:
`diagnostics.posterior_predictive.save_pyramidal_ppc` / `save_bonus_ppc` draw capped,
seeded replications from the fitted guide and write
`posterior_predictive_checks.csv` next to each stage's outputs. That is the
only evaluation code that produces artifacts during ordinary training;
`evaluate_saved_ppc` later summarizes those saved draws without re-sampling.
The Stage-1 trainers also apply explicitly requested robustness-study drop
lists through `drop_robustness.perturbations` before tensorization.
Neither path changes the replay-only contract of `evaluate_compirt.py`.
Parameter recovery is separate from that evaluator and clearly named as a
synthetic refitting study with its own implementation package and runner.

## Input contract

These are the files the evaluator reads and the columns it depends on.
Trainers across every model family write this same schema (per-dimension
families use numbered columns; scalar families use unnumbered ones).

### `pyramidal/tossup_predictions.csv` — one row per (event, rostered player)

| Column | Meaning |
| --- | --- |
| `event_id` | `{game_id}::{tossup_id}` — one game hearing one tossup |
| `game_id`, `team_id`, `player_id`, `tossup_id` | identifiers |
| `z` | row type: `BUZZ` (recorded first buzzer), `CENSORED` (teammate/opponent preempted at the buzz), `NO-BUZZ` (dead tossup, censored at question end) |
| `y` | correctness of the buzz; only populated on `BUZZ` rows |
| `raw_t_star`, `t_star`, `T_j`, `relative_position` | buzz/censoring token, question length, and `t_star / T_j` |
| `tournament_id`, `tier`, `category`, `roster_size` | stratification metadata (older runs may lack `category`) |
| `predicted_correct`, `predicted_hazard`, `predicted_survival` | fitted probabilities at this row's position |

Correctness metrics use `z == "BUZZ"` rows only — only the actual first
buzzer has an observed outcome. All rows feed the survival/timing replay.

### `pyramidal/buzz_event_predictions.csv` — one row per observed-buzz event

`event_id`, `observed_relative_position`, `predicted_relative_position`. The
prediction is the buzz-conditioned expectation E[position | a buzz occurs];
runs trained before that conditioning fix can be regenerated with
`run_scripts/common/replay_buzz_positions.py`.

### `pyramidal/players.csv` and `pyramidal/tossups.csv` — posterior medians

Players: `player_id`, threshold `c`, skill `theta_1..K` (plus `theta_norm`).
Tossups: scalar runs have `alpha_1..K`, `beta`, `gamma`, `mu`; per-dimension
runs have relevance `r_1..K` and per-dimension `beta_k`, `gamma_k`, `mu_k`.
Double-difficulty runs keep correctness under those canonical names and save
the separate timing family as `hazard_beta_*`, `hazard_gamma_*`,
`hazard_mu_*` (or hazard-prefixed Bernstein parameters). Buzz timing,
survival, first-buzzer, replay, and simulation paths automatically select the
hazard family; correctness scoring continues to select the canonical family.
`scenario_a_tossups/parameters.py` detects which schema is present, which is why the
multidim/embedding/tfidf families reuse this evaluator unmodified. TF-IDF
runs additionally save difficulty-adjustment curves that the timing replay
adds back (`load_difficulty_adjustment_curves`); the difficulty link
(`sigmoid`/`tanh`) and the correctness-calibration flag come from the stage's
`summary.json`.

### `{compositional,synergy}/bonus_part_predictions.csv` — one row per (response, part)

`observation_id`, `response_id` (one team answering one three-part bonus),
`game_id`, `team_id`, `player_ids`, `bonus_id`, `part_index`,
`bonus_part_id`, `correct`, `total_points`, `tournament_id`, `tier`,
`category`, `predicted_correct`, and (synergy branch) `aggregate` and
`synergy_contribution`.

### `{compositional,synergy}/team_predictions.csv` — one row per bonus response

`response_id`, `game_id`, `team_id`, `total_points` (0/10/20/30),
`predicted_points` (10 × sum of the three part probabilities; non-integer).
This is the sole input to PPB and to the match simulator's bonus draw.

## What one evaluation run produces

`evaluate_compirt.main` runs, in order: Scenario A tossup evaluation →
Scenario B bonus evaluation → PPC summary → match-winner simulation (unless
skipped) → metric CSVs → combined stratum diagnostics + ECE graph →
`experiment_report.md` → `docs/summary.md`.

### `experiment_report.md` — the readable overview

Rendered by `common/reports.py`'s `experiment_report_markdown`, sections in order:

1. Evaluation-regime caveats (in-sample vs transductive holdout, inferred
   from the path tier; plus a calibration caveat when Stage 1 trained with
   `calibrate_correctness`).
2. **Stage 1: Tossup Metrics** — grouped vertical tables driven by
   `TOSSUP_METRIC_GROUPS`: buzz correctness, probability sharpness, buzz
   timing/survival, first-buzzer identity — plus the signed buzz-position
   bias table (overall and per fixed band).
3. **Stage 2: Bonus Metrics** — `BONUS_METRIC_GROUPS`: part-level
   correctness, sharpness, bonus-level score — plus, on synergy branches, a
   "Synergy Contributions" section with response-, lineup-, and team-level
   negative fractions and the team-intercept interpretation caveat.
4. **Match Winner Simulation** (omitted by evaluators that never simulate;
   a "skipped" note when the simulation was skipped).
5. **Calibration By Stratum** — the trimmed diagnostics table
   (`STRATUM_REPORT_COLUMNS`).

Any metric a scenario emits that no group lists still renders (under "Other
Metrics"), so adding a metric never silently drops it from the report.
`docs/summary.md` (from `write_eval_docs_summary`) is the companion that
consolidates *everything* into tables: run variables from the stage
`summary.json` files, bonus-stage scalars, full metric rows, stratum and PPC
tables, synergy-comparison deltas, and the parameter-distribution summaries.

### `csvs/` — metric and per-row output CSVs

`tossup_metrics.csv`, `bonus_metrics.csv`, `game_metrics.csv` (one row
each); `tossup_metrics_by_buzz_position.csv`;
`{tossup,bonus,}prediction_diagnostics_by_stratum.csv` (the unprefixed file
is the concatenation); `tossup_joint_event_scores.csv`,
`tossup_time_metrics.csv`, `tossup_buzz_density_metrics.csv`,
`first_buzzer_predictions.csv`, `bonus_score_probability_predictions.csv`,
`game_predictions.csv`, `posterior_predictive_{summary,draws}.csv`, and
`{pyramidal,bonus}_parameter_distribution_summary.csv`. Difficulty reports
also include `pyramidal_difficulty_curve_distribution.csv`; DD runs add
`pyramidal_hazard_difficulty_curve_distribution.csv`.

### `graphs/<group>/` — figures, sorted by theme

`report_paths.graph_path(output_dir, filename, group)` routes evaluator figures
into `GRAPH_GROUPS` subdirectories:

| Group | Figures |
| --- | --- |
| `tossup/` | reliability (aggregate + by buzz position), hazard-based position scatter + binned calibration, buzz-density fit, survival metrics, first-buzzer identity, correctness difficulty curves (+ hazard counterparts for DD, per-dimension pages, population percentiles) |
| `bonus/` | part reliability, team PPB scatter, score-by-observed-score |
| `match/` | winner reliability, simulated-vs-actual scores |
| `parameters/` | player, tossup correctness, DD hazard, bonus-part, synergy distributions |
| `diagnostics/` | posterior predictive checks, ECE by stratum |

Standalone runners (ablation sweeps, drop robustness, Scenario C) call
`graph_path` without a group and keep their documented flat `graphs/`
layouts. An unknown group name raises.

## Module map

| Module | Owns |
| --- | --- |
| `common/metrics.py` | Scenario-agnostic probability math, no I/O: classification metrics, ECE/Brier/sharpness, calibration tables, generic RPS, and stratified metrics |
| `common/ranking_metrics.py` | Generic ranking agreement math used by the standalone stability studies |
| `common/player_scoring.py` | Rotation-invariant actual and expected PPG functionals replayed from saved Stage-1 fits |
| `common/figures.py` | Plotting primitives: `reliability_plot`, `stratified_ece_plot`, density panels/dashboards, `short_id`; plus the shared saved-column readers every family uses — `numeric_columns` (a table or one saved row), `vector_weight_columns` (`alpha_*` or `r_*`), `vector_weight_name` |
| `common/report_paths.py` | Path helpers: `csv_path`, `graph_path` (+ `GRAPH_GROUPS`), `metrics_path`, `evaluation_output_dirs` |
| `common/reports.py` | Everything Markdown: metric groups, `experiment_report_markdown`, `write_eval_docs_summary`, regime notes, result-layout discovery (`load_metrics_row`, `bonus_stage_name`, …) |
| `scenario_a_tossups/` | Scenario A, split by concern: `evaluation` (orchestration), `metrics` (joint event + buzz-position scoring), `parameters` (schema detection + difficulty reconstruction), `position` (position errors/figures), `reliability`, `difficulty`, `distributions`, and `timing` (first-buzz replay, survival metrics, first-buzzer identity) |
| `scenario_b_bonuses/metrics.py` | Scenario B pure scoring: score distributions, response RPS/log loss, exact accuracy, macro part accuracy, and team-pooled PPB |
| `scenario_b_bonuses/distributions.py` | Scenario B fitted bonus-part and synergy parameter distribution figures/summaries |
| `scenario_b_bonuses/figures.py` | Scenario B PPB and observed-score prediction figures |
| `scenario_b_bonuses/evaluation.py` | Scenario B orchestration: load predictions, call metrics/diagnostics, and write reliability/score figures |
| `scenario_c_rosters/classification.py` | Scenario C classification and metric logic (driven by `run_scripts/common/run_scenario_c.py`; see `SCENARIO_C.md`) |
| `diagnostics/match_simulation.py` | Seeded match-winner simulation, its CSV, and its two figures |
| `diagnostics/posterior_predictive.py` | PPC: trainer-side draw saving, evaluator-side summary + figure |
| `noise_floor/` | Seed-run discovery, pairwise stability metrics, and saved-fit artifact analysis used by the multidimensional noise-floor runner |
| `drop_robustness/` | Event perturbations, random/targeted metrics, completed-fit collection, figures, and the mathematical contract |
| `parameter_recovery/` | Self-contained synthetic data generation, multidimensional SVI refit, recovery metrics, and figure; run by `run_scripts/multidimensional/multidim/run_parameter_recovery.py` |
| `imaginary_tournament/` | Randomized-team simulation over saved Stage 1 and Stage 2 fits; run by `run_scripts/common/run_imaginary_tournament.py` |
| `synergy_comparison/` | No-synergy vs synergy metric deltas (CSV/MD/PNG under `comparison/`); run by `run_scripts/common/run_synergy_comparison.py` |
| `player_rankings/` | Fitted conditional buzz accuracy vs actual PPG/PP20 rankings; run by `run_scripts/common/run_player_rankings.py` |

## Variant evaluators and the sync contract

Model families that keep the numbered-column schema — baseline, multidim
(+ tanh variants), embedding, tfidf (scalar and multidim) — reuse this
evaluator **unmodified**. Two parallel evaluators replay topic-weighted
formulas instead and must be kept in sync when a *shared metric definition*
changes: `topic/fixed/topic_compirt/evaluation.py` (also the evaluator for
`topic/learned` runs) and `topic/tfidf/evaluation.py`. Both already reuse
`compirt_eval.scenario_b_bonuses.evaluation.evaluate_bonuses`, the scenario-owned
metric modules, `common/metrics.py`, `common/figures.py`, `common/report_paths.py`,
and `common/reports.py`, so bonus-side
and report-side changes propagate automatically; only their tossup-side replays are
hand-mirrored.

## Extension recipes

**Add a metric.** Put scenario-specific math in the owning scenario's
`metrics.py`; use `common/metrics.py` only when the same primitive is genuinely
shared across scenarios. Keep metric modules pure (no file or figure I/O), and
state the scored population and aggregation order in the docstring. Wire it into
the owning evaluator so it lands in that scenario's metrics dict. Add
it to the right `TOSSUP_METRIC_GROUPS`/`BONUS_METRIC_GROUPS` entry in
`common/reports.py` (otherwise it renders under "Other Metrics"). Document it in
`METRICS.md` — equation, aggregation-map row if it aggregates unusually, and
a "Related files" note. If its definition is shared with the topic replays,
mirror it there. Add a synthetic-data test in `tests/test_compirt.py`.

**Add a figure.** Build it in the module that owns the data; save via
`fig.savefig(graph_path(output_dir, "<name>.png", "<group>"), dpi=160)`.
Match house style: `figsize` ≈ 6–8in, `ax.grid(alpha=0.25)`, dashed `"0.5"`
reference lines, counts annotated in labels/legends, one axis (the
difficulty/buzz twin-axis panels are a documented exception). Name it
in the relevant `METRICS.md` "Related files" note, and assert its path in a
test.

**Change the report layout.** All of it is `common/reports.py`. Existing saved
reports can be regenerated without re-evaluating: load the metric rows with
`load_metrics_row(evaluation_dir, "<file>.csv")` and rewrite with
`experiment_report_markdown` — no trainer artifacts needed.

**Rules of the house** (from `docs/SCOPE.md` and repo conventions): no
bootstrap machinery, no MCMC diagnostics, no post-hoc recalibration in the
evaluator; evaluation must stay a deterministic replay of saved artifacts;
never build player-facing statistics on raw `theta_k` coordinates — the
latent axes are identified only up to rotation, so only rotation-invariant
quantities (logits, expected points, norms) are meaningful.

## Testing

```bash
# Root suite (covers this package end-to-end on synthetic data;
# must not write under results/):
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m unittest tests.test_compirt -v          # just the evaluator

# The parallel topic evaluators:
PYTHONPATH=.:topic/fixed .venv/bin/python -m unittest discover -s topic/fixed/tests -v
PYTHONPATH=. .venv/bin/python -m unittest discover -s topic/tfidf/tests -v
```

`tests/test_compirt.py` fits tiny synthetic models, runs the real evaluation
entry points, and asserts metric values, CSV columns, and graph paths — so a
broken figure path or renamed column fails loudly.

## Document map

| File | Read it for |
| --- | --- |
| `README.md` (this file) | Architecture, I/O contract, module map, extension recipes |
| [`EVALUATION_TLDR.md`](EVALUATION_TLDR.md) | Quick map of every evaluation umbrella, metric denominator, and output/report location |
| [`METRICS.md`](METRICS.md) | The metric contract: exact populations, equations, aggregation order, artifact for every metric |
| [`docs/METRICS.md`](docs/METRICS.md) | Interpretation guidance for the newer diagnostics (what each metric can and cannot establish) |
| [`docs/README.md`](docs/README.md) | Running the full multidim evaluation pipeline; workload knobs (`PPC_DRAWS`, `GAME_SIMULATIONS`, …) |
| [`docs/SCOPE.md`](docs/SCOPE.md) | What is deliberately *not* implemented, and why |
| [`SCENARIO_C.md`](SCENARIO_C.md) | The opt-in C1–C4 roster-generalization study (holdout runs only) |
| [`drop_robustness/README.md`](drop_robustness/README.md) | The data-dropping ranking-stability study: mathematical contract and implementation map |
| [`noise_floor/README.md`](noise_floor/README.md) | The identical-data seed-stability study, runner, and analysis-only mode |
| [`parameter_recovery/README.md`](parameter_recovery/README.md) | The self-contained synthetic refitting study and canonical command |
| [`imaginary_tournament/README.md`](imaginary_tournament/README.md) | The randomized-team saved-fit simulation, outputs, and limitations |
| [`player_rankings/README.md`](player_rankings/README.md) | The fitted-versus-observed player-ranking comparison |
| [`synergy_comparison/README.md`](synergy_comparison/README.md) | The saved-metric comparison between bonus-model branches |
