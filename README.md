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
