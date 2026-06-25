# Topic-Modeling CompIRT

This pipeline swaps out root CompIRT's free discrimination vector for a fixed
topic vector `r` built from PLDA, LDA, or category one-hots. Everything else —
the linked dataset, roster logic, SVI setup, and evaluation style — stays the
same as the root model.

See `equation_flow.md` for the full equation walkthrough and `equation_changes.md`
for what changed from the earlier topic prototype.


## How It Works

Root CompIRT learns a free question-relevance vector. The topic version replaces
that with a fixed topic vector `r`. Each stage writes files the next one reads,
so a full run goes: topic vectors → Stage 1 → Stage 2 → evaluation.
`run_topic_compirt.sh` chains all of that in one pass.

```text
topic vectors                -> document_latent_vectors.csv
train_topic_pyramidal.py     -> players.csv, tossups.csv, tossup_predictions.csv
train_topic_compositional.py -> bonus_parts.csv, team_predictions.csv
evaluate_topic_compirt.py    -> metrics, plots, experiment_report.md
```

The core formulas:

```text
tossup logit = sum_k r_jk * (theta_ik - d_jk(t))
bonus logit  = LSE_m(sum_k r_bk * theta_pmk; tau) - sum_k r_bk * beta_bk
```

**Stage 1 — topic pyramidal tossups** (`train_topic_pyramidal.py`): attaches
fixed tossup topic weights and fits the competing-risks buzz model via Pyro SVI.
Learns per-topic difficulty curves (no free `alpha`), then saves player skills,
tossup parameters, rankings, and optional expected buzz positions.

**Stage 2 — topic compositional bonuses** (`train_topic_compositional.py`):
reads the fixed `theta` from Stage 1, attaches bonus topic weights, and learns
per-topic bonus-part difficulty. Optionally adds a synergy term.

> **Calibration** adds a global correctness scale and bias inside each stage

**Evaluation** (`evaluate_topic_compirt.py`): replays the saved topic-weighted
formulas to produce metrics, reliability plots, parameter distributions, tossup
timing plots, and `experiment_report.md`. `TOPIC_NAMES` only affects plot labels.


## Repository Layout

- `run_topic_compirt.sh` — end-to-end orchestrator: reads env vars, optionally
  builds PLDA vectors, then chains pyramidal training, compositional training,
  optional synergy, and evaluation.
- `run_plda.py`, `run_lda.py`, `build_category_vectors.py` — the three
  topic-vector sources (PLDA, unsupervised LDA, and category one-hots).
- `train_topic_pyramidal.py` + `topic_compirt/pyramidal.py` — Stage 1.
- `train_topic_compositional.py` + `topic_compirt/compositional.py` — Stage 2.
- `evaluate_topic_compirt.py` + `topic_compirt/evaluation.py` — metrics and plots.
- `topic_compirt/topics.py` — loads, normalizes, and aligns topic vectors to
  model tensors.
- `experiments/run_topic_compirt_2024.sh` — full-2024 reproducibility wrapper.
- `experiments/compare_bonus_runs.py` — side-by-side bonus metric comparison
  across multiple result directories.


## Build Topic Vectors

All downstream runs consume a CSV named `document_latent_vectors.csv` with
columns `document_id`, `question_type`, and one or more `latent_topic_XX`
columns. Rows are normalized again during training, so they just need positive
finite mass.

**PLDA** (the main source — uses database category/subcategory as labels):

```bash
.venv/bin/python topic-modeling/run_plda.py \
  --dimensions 5 \
  --iterations 500 \
  --output-dir topic-modeling/outputs/plda
```

**LDA** (same corpus, no labels):

```bash
.venv/bin/python topic-modeling/run_lda.py \
  --dimensions 5 \
  --iterations 500 \
  --output-dir topic-modeling/outputs/lda
```

**Category one-hots** (replaces learned topics with top-level category flags):

```bash
.venv/bin/python topic-modeling/build_category_vectors.py \
  --source topic-modeling/outputs/plda/document_latent_vectors.csv \
  --out-dir topic-modeling/outputs/category
```

The category builder prints the number of dimensions it produced (currently
`13`), with names in `topic-modeling/outputs/category/category_index.csv`.


## All-2024 Runs

These train on the full `year_2024` split. Run this shared setup once:

```bash
export SPLIT=year_2024
export TOURNAMENT=""
export RUN_PLDA=0
export RUN_SYNERGY=1
export SYNERGY_DIMENSIONS=3
export SAVE_SYNERGY_DETAILS=1
export PYRAMIDAL_STEPS=5000
export BONUS_STEPS=3000
export LR=0.005
export PREDICT_BUZZ_POSITIONS=1
export EVALUATE=1
export DEVICE=cuda  # use DEVICE=cpu if no GPU
export GPU=0
```

> To run a calibrated version of any command below, prepend
> `CALIBRATE_CORRECTNESS=1` and change `ROOT` to something like
> `results/compirt/plda-all2024-cal`.

### plda-all2024

```bash
DIMENSIONS=5 \
TOPIC_VECTORS=topic-modeling/outputs/plda/document_latent_vectors.csv \
ROOT=results/compirt/plda-all2024 \
topic-modeling/run_topic_compirt.sh
```

There's also a PLDA-specific helper with the all-2024 defaults baked in:

```bash
ROOT=results/compirt/plda-all2024 \
topic-modeling/experiments/run_topic_compirt_2024.sh
```

### lda-all2024

```bash
DIMENSIONS=5 \
TOPIC_VECTORS=topic-modeling/outputs/lda/document_latent_vectors.csv \
ROOT=results/compirt/lda-all2024 \
topic-modeling/run_topic_compirt.sh
```

### category-all2024

```bash
DIMENSIONS=13 \
TOPIC_VECTORS=topic-modeling/outputs/category/document_latent_vectors.csv \
TOPIC_NAMES=topic-modeling/outputs/category/category_index.csv \
ROOT=results/compirt/category-all2024 \
topic-modeling/run_topic_compirt.sh
```

If you rebuild category vectors and the script prints a different dimension
count, use that number for `DIMENSIONS`.


## Output Layout

Each `ROOT` gets the same structure:

```text
<ROOT>/pyramidal/            tossup model parameters and predictions
<ROOT>/compositional/        bonus model without synergy
<ROOT>/synergy/              bonus model with synergy (if RUN_SYNERGY=1)
<ROOT>/evaluation/           metrics and plots for compositional/
<ROOT>/synergy-evaluation/   metrics and plots for synergy/
<ROOT>/run.log               terminal transcript for the latest run
```

The main reports are:

```text
<ROOT>/evaluation/experiment_report.md
<ROOT>/synergy-evaluation/experiment_report.md
```


## Key Variables

| Variable | What it does |
| --- | --- |
| `ROOT` | Output directory for the whole run. |
| `SPLIT`, `TOURNAMENT` | Data selection. `TOURNAMENT=""` uses the whole split. |
| `DIMENSIONS` | Must match the number of `latent_topic_XX` columns. |
| `TOPIC_VECTORS` | Vector CSV to use when `RUN_PLDA=0`. |
| `RUN_PLDA` | `1` rebuilds PLDA first; `0` reuses `TOPIC_VECTORS`. |
| `TOPIC_NAMES` | Optional topic/category names for evaluation plot labels. |
| `RUN_SYNERGY` | Also train and evaluate the synergy bonus model. |
| `CALIBRATE_CORRECTNESS` | Add a global correctness scale and bias (retrain, not post-processing). |
| `DEVICE`, `GPU` | Torch device selection. |


## Tests

```bash
PYTHONPATH=.:topic-modeling .venv/bin/python -m unittest discover -s topic-modeling/tests -v
```


## Run Scripts

Run all commands from the repo root:

```bash
cd /teapot/students/natnguyen/CompIRT-Implementation
```

Compare bonus metrics across topic sources:

```bash
.venv/bin/python topic-modeling/experiments/compare_bonus_runs.py \
  results/compirt/plda-all2024 \
  results/compirt/lda-all2024 \
  results/compirt/category-all2024
```
