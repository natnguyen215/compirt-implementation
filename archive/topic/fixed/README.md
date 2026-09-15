# Fixed-topic CompIRT

Replaces CompIRT's learned relevance with a fixed topic mixture `r` built from
PLDA, LDA, or category one-hots, and learns a difficulty curve per topic. The
equations in paper order are in [`equation_flow.md`](equation_flow.md).

```text
tossup logit = sum_k r_jk * (theta_ik - d_jk(t))
bonus logit  = LSE_m(sum_k r_bk * theta_mk; tau) - sum_k r_bk * beta_bk   (+ synergy)
```

- `r` is an input, not a Pyro site. `topic_compirt/topics.py` L1-normalizes
  each row of `document_latent_vectors.csv` and fails if a tossup or bonus has
  no vector.
- The three parts of a bonus share one `r_b` but learn separate `beta_bk`.
- Stage 2 fixes Stage-1 `theta` and drops bonus rows whose roster includes a
  player without a fitted `theta`.
- `CALIBRATE_CORRECTNESS=1` refits with a scale and bias on the correctness
  logit only; the hazard is unchanged.

## Files

| File | Role |
| --- | --- |
| `run_plda.py`, `run_lda.py`, `build_category_vectors.py` | Build `document_latent_vectors.csv` |
| `topic_compirt/topics.py` | Load, normalize, and align topic vectors |
| `train_topic_pyramidal.py`, `topic_compirt/pyramidal.py` | Stage 1 tossups |
| `train_topic_compositional.py`, `topic_compirt/compositional.py` | Stage 2 bonuses |
| `evaluate_topic_compirt.py`, `topic_compirt/evaluation.py` | Metrics, plots, and `experiment_report.md` |
| `run_topic_compirt.sh` | Chains topic vectors, both stages, optional synergy, and evaluation |
| `compare_bonus_runs.py` | Prints bonus metrics side by side across runs |
| `../utils/` | Corpus loading, category normalization, and the vector CSV schema |

## Topic vectors

The CSV has `document_id`, `question_type`, and `latent_topic_NN` columns.
`document_id` must match CompIRT IDs: `question_set::edition::p<packet>::q<n>`
for tossups and `...::b<n>` for bonuses.

```bash
.venv/bin/python -m topic.fixed.run_plda --dimensions 5 --iterations 500 \
  --output-dir topic/fixed/outputs/plda
.venv/bin/python -m topic.fixed.run_lda --dimensions 5 --iterations 500 \
  --output-dir topic/fixed/outputs/lda
.venv/bin/python -m topic.fixed.build_category_vectors \
  --source topic/fixed/outputs/plda/document_latent_vectors.csv \
  --out-dir topic/fixed/outputs/category
```

PLDA uses database categories as labels but exports only its shared latent
topics. The category builder prints its dimension count and writes names to
`category_index.csv`. `outputs/` is gitignored.

## Runs

The saved in-sample runs used this setup:

```bash
export SPLIT=year_2024 TOURNAMENT="" RUN_PLDA=0 RUN_SYNERGY=1 SYNERGY_DIMENSIONS=3 \
  SAVE_SYNERGY_DETAILS=1 PYRAMIDAL_STEPS=5000 BONUS_STEPS=3000 LR=0.005 EVALUATE=1 DEVICE=cuda
DIMENSIONS=5 TOPIC_VECTORS=topic/fixed/outputs/plda/document_latent_vectors.csv \
  ROOT=results/compirt/in_sample/topic/plda-all2024 topic/fixed/run_topic_compirt.sh
```

| Run | `DIMENSIONS` | `TOPIC_VECTORS` under `topic/fixed/outputs/` |
| --- | ---: | --- |
| `plda-all2024` | 5 | `plda/document_latent_vectors.csv` |
| `lda-all2024` | 5 | `lda/document_latent_vectors.csv` |
| `category-all2024` | 13 | `category/document_latent_vectors.csv`, with `TOPIC_NAMES=.../category_index.csv` |

`-cal` runs add `CALIBRATE_CORRECTNESS=1`. `DIMENSIONS` must equal the number
of `latent_topic_NN` columns, `RUN_PLDA=1` rebuilds PLDA vectors first, and
`TOPIC_NAMES` only relabels plots. Each root gets `pyramidal/`,
`compositional/`, `synergy/`, `evaluation/`, `synergy-evaluation/`, and
`run.log`.

Runs are in
[`results/compirt/in_sample/topic/`](../../../results/compirt/in_sample/topic/).
Held-out runs of the same names, which used 2024 player posteriors as priors
for a 2025 fit, are in
[`results/compirt/holdout/topic/`](../../../results/compirt/holdout/topic/).

```bash
.venv/bin/python -m topic.fixed.compare_bonus_runs \
  results/compirt/in_sample/topic/plda-all2024 \
  results/compirt/in_sample/topic/lda-all2024 \
  results/compirt/in_sample/topic/category-all2024
```
