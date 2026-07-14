# Topic-Specific TF-IDF Pyramidal Experiments

This directory is the isolated Stage 1 topic-model TF-IDF experiment family.
It does not alter the baseline fixed-topic or learned-topic trainers,
likelihoods, runners, or evaluators.

For each topic coordinate it learns one global nonnegative lambda:

```text
d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)
```

Thus a tossup with topic mixture `r_j` receives the effective adjustment
`-tfidf_prefix_j(t) * sum_k r_jk * lambda_k`. TF-IDF prefix mass is normalized
within each tossup by default; `--no-normalize-tfidf` uses raw cumulative mass.

## Fixed-topic runs

PLDA, LDA, and category vectors all use the same trainer because they share
the standard `document_latent_vectors.csv` schema.

```bash
.venv/bin/python -m topic.tfidf.train_fixed_pyramidal \
  --topic-vectors topic/fixed/outputs/plda/document_latent_vectors.csv \
  --dimensions 5 --steps 5000
```

The end-to-end fixed-topic runner has its own output root and uses the
unchanged topic compositional bonus stage:

```bash
DIMENSIONS=5 \
TOPIC_VECTORS=topic/fixed/outputs/plda/document_latent_vectors.csv \
TOPIC_TFIDF_EFFECT_PRIOR_SCALE=1.0 \
topic/tfidf/run_fixed_topic_tfidf.sh
```

`NO_NORMALIZE_TFIDF=1` selects raw cumulative TF-IDF in the runner. The runner
also fits a synergy bonus branch by default (`RUN_SYNERGY=1`,
`SYNERGY_DIMENSIONS=3`) and evaluates it to `synergy-evaluation/`.

Held-out temporal splits use the shared runner with `MODEL=topic_tfidf`
(fixed vectors) or `MODEL=learned_tfidf` (joint sLDA):

```bash
MODEL=topic_tfidf TOPIC_VECTORS=topic/fixed/outputs/plda/document_latent_vectors.csv \
  RUN_SYNERGY=1 .venv/bin/python run_scripts/run_compirt_holdout.py
```

## Learned-topic runs

The learned version keeps `theta_doc ~ Dirichlet` as the topic mixture, so it
learns topics and their TF-IDF effects in the same SVI:

```bash
.venv/bin/python -m topic.tfidf.train_learned_pyramidal \
  --split year_2024 --dimensions 5 --steps 2000
```

Its output retains `topic_word_matrix.npy`, `vocabulary.json`, and
`document_latent_vectors.csv`, so the existing learned compositional Stage 2
can consume it unchanged.

## Outputs and evaluation

Both trainers write their own result directories by default:

- fixed topic: `results/compirt/topic-tfidf-pyramidal`
- learned topic: `results/compirt/joint-slda-tfidf`

`topic_tfidf_lambdas.csv` records topic dimension, label, and fitted lambda.
`tfidf_adjustment_curves.csv` stores the signed aggregate effective-difficulty
adjustment used by the dedicated evaluator. Row-level `tfidf_prefix_score`
diagnostics are included in `tossup_predictions.csv`; `summary.json` records
the formula, prior scale, feature metadata, and lambda mapping.

Use the dedicated evaluator with the usual topic bonus results:

```bash
.venv/bin/python -m topic.tfidf.evaluate \
  --pyramidal-results results/compirt/topic-tfidf-pyramidal \
  --compositional-results results/compirt/topic-tfidf-compositional \
  --output-dir results/compirt/topic-tfidf-evaluation
```

It replays saved adjustments in both the effective difficulty plot and the
first-buzz timing reconstruction, while reusing standard topic metrics and
bonus evaluation.

## Tests

```bash
PYTHONPATH=.:topic/fixed:topic/learned \
  .venv/bin/python -m unittest topic.tfidf.tests.test_topic_tfidf -v
```
