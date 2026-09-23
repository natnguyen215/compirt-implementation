# Quizbowl IRT

Builds linked quizbowl tournament tables from a SQLite export and fits CompIRT,
a two-stage Pyro model of player and team performance. Stage 1 models which
player buzzes first on a tossup, when, and whether the buzz is correct. Stage 2
holds the learned player skills fixed and models bonus-part conversion.

## Setup

From the repository root:

```bash
python -m venv --system-site-packages .venv
.venv/bin/python -m pip install -r requirements/dev.txt
```

`requirements/dev.txt` adds pytest and Pyflakes to the runtime dependencies.
Training and evaluation need the generated dataset described in
[`data/README.md`](data/README.md).

This project builds linked quizbowl datasets and uses Pyro to model player and
team performance.

## Repository Layout

The root CompIRT files are separated by responsibility through their names:

- `pyramidal_model.py` and `compositional_model.py`: paper equation implementations.
- `compirt_data.py`: observation and tensor construction.
- `train_pyramidal.py` and `train_compositional.py`: experiment training.
- `evaluate_compirt.py` and the `compirt_eval/` package: the executed evaluation code
   plus its metrics, figures, and per-scenario (tossup/bonus) modules. See
   [`compirt_eval/METRICS.md`](compirt_eval/METRICS.md) for the scored populations,
   aggregation order, equations, graphs, and interpretation limits.
- `data_pipeline/`: source-database to Hugging Face dataset builder and validator.
- `run_scripts/common/run_compirt.py`: end to end configurable experiment (train,
  evaluate, and compare in one pass). `run_scripts/common/run_compirt.sh` is a thin
  wrapper around it.
- `run_scripts/common/run_compirt_2024.py`: full-2024 reproducibility wrapper. It runs
  dataset validation, then calls the configurable runner with all-2024
  defaults. `run_scripts/common/run_compirt_2024.sh` is a thin wrapper around it.
- `run_scripts/common/run_compirt_round_holdout.py`: derives linked train/test data by
  holding out the final 20% of complete rounds in every tournament, then reuses
  the standard transductive holdout runner. Its `.sh` file is the shell entry
  point.
- `holdout/`: held-out evaluation infrastructure — the round/game split builders,
  the cross-split player priors used by the transductive runners, and
  `frozen_predict.py`, which replays both stages at the training posterior
  medians for a pure "matrix infill" forward pass with no test-set learning.
- `lineup.py`: per-game active-lineup inference from buzz evidence.
- `scenario_c_model.py`: the paper's Scenario C fit — new bonus-item parameters
  learned while player/team parameters stay frozen.
- `utils/`: shared saving, training, posterior, and run-logging helpers.
- `simple_mirt/`: legacy/pedagogical MIRT baseline outside the two-stage
  pipeline; also supplies the plain-IRT comparator for the drop-robustness study.
- `neg_test/`: 5-fold cross-validated neg/buzz comparison across difficulty-curve
  families.
- `topic/`: topic-model experiments — `topic/fixed/` (topics fit upstream via
  LDA/PLDA/categories and fed in as fixed weights), `topic/learned/` (topics
  learned jointly with the IRT model), and shared topic helpers in `topic/utils/`.
- `tfidf/`: isolated cumulative IDF-aware pyramidal model for clue timing.
- `multidimensional/`: multidimensional-difficulty experiments —
  `multidimensional/multidim_mirt/` (the multidimensional-skill pyramidal
  variant, with a free learned relevance vector `r`),
  `multidimensional/embedding_mirt/` (sibling whose `r` is instead a
  CAIMIRA-style relevance vector computed from a frozen Qwen3-Embedding-8B
  vector of the question text through a learned linear projection). The
  embedding variant reuses `multidim_mirt`'s tossup math and the root
  `compositional_model.py` rather than duplicating them. Both name the weight
  `r` rather than the baseline's `alpha` because their difficulty is
  per-dimension: `alpha` weights a scalar-difficulty dot product, while `r`
  weights per-dimension skill-minus-difficulty gaps.
- `polynomial_compirt/`: isolated multidimensional Stage-1 variant whose
  per-tossup difficulty coordinates are strictly decreasing degree 3--6
  Bernstein polynomials, plus the resumable 1D/5D degree sweep launcher.

Variant scripts run as modules from the repo root, e.g.
`.venv/bin/python -m topic.fixed.train_topic_pyramidal --help`.

Start with the [documentation index](docs/README.md). Reproduction entry points
live under `run_scripts/`; for scored populations and equations, see the
[evaluation metric contract](compirt_eval/METRICS.md).

# CompIRT Paper Implementation

Each file has a module docstring and per-function paper-equation references; the smaller
helper functions sit above the `run_experiment`/`main` entry point that ties
them together.

1. `compirt_data.py`: turns the linked tables into model-ready observations and
   padded tensors (paper Section 3.1 tossups, Section 3.2 bonus parts).
2. `pyramidal_model.py`: the Stage 1 tossup competing-risks model
   (Eq. 3-7 and the dead-tossup survival term in Eq. 13).
3. `train_pyramidal.py`: fits Stage 1 and saves player/tossup parameters; start
   at `run_experiment`.
4. `compositional_model.py`: the Stage 2 bonus model that holds player skill
   `theta` fixed and learns how parts reward it (Eq. 8 aggregation, Eq. 10
   synergy, Eq. 11 outcome).
5. `train_compositional.py`: fits Stage 2 from the saved `theta`; start at
   `run_experiment`.
6. `evaluate_compirt.py`: turns saved predictions into metrics and figures; start
   at `main`, which calls `compirt_eval/scenario_a_tossups/` for paper Scenario A
   and `compirt_eval/scenario_b_bonuses/` for Scenario B. Cross-scenario metrics,
   figures, report paths, and report builders live in `compirt_eval/common/`.

## Dataset Pipeline

`data_pipeline.dataset` builds the linked HuggingFace tables from
`data/database.db`. Player rows that share the same raw player slug are grouped
under that slug; the builder does not attempt cross-slug identity resolution.

Rebuild and validate the generated data:

```bash
.venv/bin/python -m data_pipeline.build --overwrite
.venv/bin/python -m data_pipeline.validate
```

## Repository layout

| Path | Contents |
| --- | --- |
| `compirt_data.py` | Linked tables to model observations and padded tensors (paper §3.1 tossups, §3.2 bonus parts) |
| `compirt_race.py` | Normalized first-buzz law shared by every Stage-1 family and by replay ([spec](docs/first-buzz-likelihood.md)) |
| `pyramidal_model.py`, `train_pyramidal.py` | Stage-1 competing-risks tossup model (Eq. 3–7, 13) and trainer |
| `compositional_model.py`, `train_compositional.py` | Stage-2 bonus model (Eq. 8, 10, 11) and trainer |
| `evaluate_compirt.py`, `compirt_eval/` | Metrics, figures, and reports replayed from saved fits |
| `lineup.py` | Per-game active lineups inferred from buzz evidence |
| `multidimensional/multidim_mirt/` | Stage 1 with per-dimension difficulty and positive relevance `r` |
| `hazard_double_difficulty/` | Stage 1 with separate correctness and buzz-timing curves, plus player-perception variants |
| `holdout/` | Round, game, and season splits; transferred player priors; frozen replay of training medians |
| [`run_scripts/`](run_scripts/README.md) | Experiment pipelines and runners |
| [`analysis/`](analysis/README.md) | Descriptive EDA and conditional-correctness studies |
| `data_pipeline/` | SQLite to Hugging Face table builder and validator |
| `utils/` | SVI, posterior, saving, roster, and run-logging helpers |
| [`results/`](results/README.md) | Saved runs and reports |
| [`archive/`](archive/README.md) | Retired model families and studies; not imported by live code or run by the checks |

Trainers start at `run_experiment` and evaluators at `main`. Root trainers run
as files; family packages run as modules from the repository root, for example
`.venv/bin/python -m multidimensional.multidim_mirt.train_pyramidal --help`.

## Documentation

- [Code guide](docs/code-guide.md): data contracts, model math, fitting,
  artifacts, and evaluation regimes, end to end.
- [Experiment commands](docs/compirt-experiments.md) for single fits and full runs.
- [Metric contract](compirt_eval/METRICS.md): scored populations, equations,
  and aggregation order.
- [Documentation index](docs/README.md): each research line's notes, code, and
  results.

## Checks

```bash
.venv/bin/python -B run_scripts/common/check_repo.py
```

Runs every test suite, Pyflakes, and a whitespace check without writing under
`results/`. Add `--include-data-validation` when the generated dataset is
available. Individual suites are listed in [`tests/README.md`](tests/README.md).

## Implementation notes

- Bonus team skill uses the paper's Eq. 8 log-sum-exp aggregation, unnormalized
  by roster size. Eq. 9 Noisy-OR is not implemented.
- Only the first buzz is modeled by default. `--include-bounceback` on the
  baseline and `multidim_mirt` Stage-1 trainers adds the paper's opponent-only
  continuation after a neg.
- Lineups are inferred from buzz evidence and cached under `data/lineups/`.
  Games with no buzz evidence fall back to the full roster, and each bonus
  reuses the lineup of the tossup in its cycle
  ([rules](docs/lineup-inference.md)).
- Fitting uses stochastic variational inference with an `AutoNormal` guide
  rather than the paper's NUTS-MCMC.
- Player identity is exact raw-slug matching.
