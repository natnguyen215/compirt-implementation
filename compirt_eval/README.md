# compirt_eval: the CompIRT evaluation suite

This package turns training runs into metrics, figures, and readable reports.
**`evaluate_compirt.py` only replays saved model artifacts**; it never retrains,
so evaluation can be rerun, extended, or debugged against the same fitted
parameters. Command-line runners live under `run_scripts/`.

This file is the developer guide: data flow, input and output files, module
ownership, and extension recipes. Mathematical definitions and interpretation
live in [`METRICS.md`](METRICS.md).

## Source layout

```text
compirt_eval/
├── common/                 shared metric, category, figure, path, and report primitives
├── scenario_a_tossups/     Stage 1 / tossup evaluation
├── scenario_b_bonuses/     Stage 2 / bonus evaluation
└── synergy_comparison/     no-synergy versus synergy metric comparison
```

The `scenario_*` names follow the paper: Scenario A means tossups and Scenario B
means bonuses. Completed evaluation studies keep their code beside their
results; see [`../results/README.md`](../results/README.md).

## Quick start

```bash
# Evaluate one finished two-stage run (from the repo root):
.venv/bin/python evaluate_compirt.py \
  --pyramidal-results results/compirt/in_sample/<run>/pyramidal \
  --compositional-results results/compirt/in_sample/<run>/synergy \
  --output-dir results/compirt/in_sample/<run>/synergy-evaluation

# --split/--tournament select the recorded ground-truth tables.

# Compare the no-synergy and synergy bonus branches of one run:
.venv/bin/python run_scripts/common/run_synergy_comparison.py \
  --compositional-metrics results/compirt/in_sample/<run>/evaluation/bonus_metrics.csv \
  --synergy-metrics results/compirt/in_sample/<run>/synergy-evaluation/bonus_metrics.csv \
  --output-dir results/compirt/in_sample/<run>/comparison
```

The `--output-dir` name matters: `common/reports.py` (`bonus_stage_name`)
infers the bonus branch from it (`synergy-evaluation` reads the `synergy/`
stage folder, anything else reads `compositional/`), and infers the
evaluation-regime caveat from the results tier in the path
(`results/compirt/{in_sample,holdout}/...`).

## Data flow

```
train_pyramidal.py          train_compositional.py [--use-synergy]
        |                            |
        v                            v
  <run>/pyramidal/             <run>/{compositional,synergy}/
  players.csv                  bonus_part_predictions.csv
  tossups.csv                  team_predictions.csv
  tossup_predictions.csv       summary.json
  buzz_event_predictions.csv
  player_buzz_summary.csv
  summary.json
        \                           /
         v                         v
        evaluate_compirt.py  (this package)
                  |
                  v
        <run>/<evaluation-dir>/
          experiment_report.md      docs/summary.md
          csvs/*.csv                graphs/<group>/*.png
```

Training writes no evaluation artifacts; everything under the evaluation
directory comes from replaying the saved files above.

Bonus evaluation joins declared easy/medium/hard part difficulty from the
linked tables and reports separate accuracies and counts. With those tables,
it also writes team-game bonus totals, team/tournament bonus-only PPG and
absolute errors, per-tournament MAE and Spearman correlations, and signed
bonus-only game margins with MAE. Both metrics use expected points on recorded
bonus opportunities and include zero-bonus games. Pass the exact evaluated game population as `tables=` to the Python
`evaluate_bonuses` API; the CLI supplies its `--split`/`--tournament` selection.
The compositional-fold runner pools held-out games before calculating full
tournament rankings. See [the metric contract](METRICS.md#bonus-only-team-ppg-and-tournament-rankings).

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
prediction is the buzz-conditioned expectation E[position | a buzz occurs].

### `pyramidal/players.csv` and `pyramidal/tossups.csv` — posterior medians

Players: `player_id`, threshold `c`, skill `theta_1..K` (plus `theta_norm`).
Tossups: scalar runs have `alpha_1..K`, `beta`, `gamma`, `mu`; per-dimension
runs have relevance `r_1..K` and per-dimension `beta_k`, `gamma_k`, `mu_k`.
Double-difficulty runs keep correctness under those canonical names and save
the separate timing family as `hazard_beta_*`, `hazard_gamma_*`,
`hazard_mu_*` (or hazard-prefixed Bernstein parameters). Buzz timing,
survival, first-buzzer, and replay paths automatically select the hazard
family; correctness scoring continues to select the canonical family.
`scenario_a_tossups/parameters.py` detects which schema is present, which is why
the multidim and double-difficulty families reuse this evaluator unmodified.
Archived TF-IDF runs additionally save difficulty-adjustment curves that the
timing replay adds back (`load_difficulty_adjustment_curves`); the difficulty
link (`sigmoid`/`tanh`) and the correctness-calibration flag come from the
stage's `summary.json`.

### `{compositional,synergy}/bonus_part_predictions.csv` — one row per (response, part)

`observation_id`, `response_id` (one team answering one three-part bonus),
`game_id`, `team_id`, `player_ids`, `bonus_id`, `part_index`,
`bonus_part_id`, `correct`, `total_points`, `tournament_id`, `tier`,
`category`, `predicted_correct`, and (synergy branch) `aggregate` and
`synergy_contribution`.

### `{compositional,synergy}/team_predictions.csv` — one row per bonus response

`response_id`, `game_id`, `team_id`, `total_points` (0/10/20/30),
`predicted_points` (10 × sum of the three part probabilities; non-integer).
This is the sole input to PPB.

## What one evaluation run produces

`evaluate_compirt.main` runs, in order: Scenario A tossup evaluation (including
the token-threshold game replay) → Scenario B bonus evaluation → metric CSVs →
combined stratum diagnostics + ECE graph → `experiment_report.md` →
`docs/summary.md`.

### `experiment_report.md` — the readable overview

Rendered by `common/reports.py`'s `experiment_report_markdown`, sections in order:

1. Evaluation-regime caveats (in-sample vs transductive holdout, inferred
   from the path tier; plus a calibration caveat when Stage 1 trained with
   `calibrate_correctness`).
2. **Stage 1: Tossup Metrics** — grouped tables driven by
   `TOSSUP_METRIC_GROUPS`: buzz correctness, probability sharpness, buzz
   timing/survival, first-buzzer identity — plus the signed buzz-position
   bias table (overall and per fixed band).
3. **Stage 2: Bonus Metrics** — `BONUS_METRIC_GROUPS`: part-level
   correctness, sharpness, bonus-level score — plus, on synergy branches, a
   "Synergy Contributions" section with response-, lineup-, and team-level
   negative fractions and the team-intercept interpretation caveat.
4. **Tossup Game Replay** — winners and margins from the same integer tossup
   points used for player PPG and tournament rankings.
5. **Calibration By Stratum** — the trimmed diagnostics table
   (`STRATUM_REPORT_COLUMNS`).

Any metric a scenario emits that no group lists still renders (under "Other
Metrics"). `docs/summary.md` (from `write_eval_docs_summary`) consolidates
everything into tables: run variables from the stage `summary.json` files,
bonus-stage scalars, full metric rows, stratum tables, synergy-comparison
deltas, and the parameter-distribution summaries.

### `csvs/` — metric and per-row output CSVs

`tossup_outcome_predictions.csv` records the complete simulated buzz sequence
for every question. `tossup_player_predictions.csv` stores replayed and actual
points; `tossup_game_predictions.csv` (also `game_predictions.csv`) sums those
points by game. `tossup_round_metrics.csv` groups the same games by round.
`player_ppg_leaderboard.csv` divides those totals by unique lineup games.
The replay rules, incomplete-game exclusion, and schema-version cache
invalidation are specified in [METRICS.md](METRICS.md).

`tossup_metrics.csv`, `bonus_metrics.csv`, `game_metrics.csv` (one row
each); `tossup_metrics_by_buzz_position.csv`;
`{tossup,bonus,}prediction_diagnostics_by_stratum.csv` (the unprefixed file
is the concatenation); `tossup_joint_event_scores.csv`,
`tossup_time_metrics.csv`, `tossup_buzz_density_metrics.csv`,
`first_buzzer_predictions.csv`, `bonus_score_probability_predictions.csv`, and
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
| `parameters/` | player, tossup correctness, DD hazard, bonus-part, synergy distributions |
| `diagnostics/` | ECE by stratum |

An unknown group name raises.

## Module map

| Module | Owns |
| --- | --- |
| `common/metrics.py` | Scenario-agnostic probability math, no I/O: classification metrics, ECE/Brier/sharpness, calibration tables, generic RPS, and stratified metrics |
| `common/categories.py` | Canonical top-level quizbowl categories used for strata |
| `common/figures.py` | Plotting primitives (`reliability_plot`, `stratified_ece_plot`, density panels, `short_id`) and the shared saved-column readers `numeric_columns`, `vector_weight_columns`, `vector_weight_name` |
| `common/report_paths.py` | Path helpers: `csv_path`, `graph_path` (+ `GRAPH_GROUPS`), `metrics_path`, `evaluation_output_dirs` |
| `common/reports.py` | Everything Markdown: metric groups, `experiment_report_markdown`, `write_eval_docs_summary`, regime notes, result-layout discovery (`load_metrics_row`, `bonus_stage_name`, …) |
| `scenario_a_tossups/` | Scenario A, split by concern: `evaluation` (orchestration), `metrics`, `parameters` (schema detection + difficulty reconstruction), `position`, `reliability`, `difficulty`, `distributions`, `reconstruction` (saved inputs and first-buzz replay), `survival`, `timing`, and `outcomes` (ownership, games, player PPG) |
| `scenario_b_bonuses/` | Scenario B: `metrics` (pure scoring), `distributions` (parameter figures/summaries), `figures` (PPB and score plots), `outcomes` (team PPG, tournament rankings and game margins), `evaluation` (orchestration) |
| `synergy_comparison/` | No-synergy vs synergy metric deltas (CSV/MD/PNG under `comparison/`); run by `run_scripts/common/run_synergy_comparison.py` |

## Extension recipes

**Add a metric.** Put scenario-specific math in the owning scenario's
`metrics.py`; use `common/metrics.py` only when the same primitive is genuinely
shared across scenarios. Keep metric modules pure (no file or figure I/O), and
state the scored population and aggregation order in the docstring. Wire it into
the owning evaluator, add it to the right `TOSSUP_METRIC_GROUPS`/
`BONUS_METRIC_GROUPS` entry in `common/reports.py`, document it in `METRICS.md`
(equation, aggregation-map row if it aggregates unusually, "Related files"
note), and add a synthetic-data test in `tests/test_compirt.py`.

**Add a figure.** Build it in the module that owns the data; save via
`fig.savefig(graph_path(output_dir, "<name>.png", "<group>"), dpi=160)`.
Match house style: `figsize` ≈ 6–8in, `ax.grid(alpha=0.25)`, dashed `"0.5"`
reference lines, counts annotated in labels/legends. Name it in the relevant
`METRICS.md` "Related files" note, and assert its path in a test.

**Change the report layout.** All of it is `common/reports.py`. Saved reports
can be regenerated without re-evaluating: load the metric rows with
`load_metrics_row(evaluation_dir, "<file>.csv")` and rewrite with
`experiment_report_markdown`.

**Evaluation conventions.** Compute standard metrics by replaying saved
artifacts, including any calibration fitted during training. Express
player-facing statistics through rotation-invariant quantities (see
"How to read these figures" in `METRICS.md`).

## Testing

```bash
.venv/bin/python -B -m pytest -q tests/test_compirt.py tests/test_compirt_eval_suite.py
```

`tests/test_compirt.py` fits tiny synthetic models, runs the real evaluation
entry points, and asserts metric values, CSV columns, and graph paths.
