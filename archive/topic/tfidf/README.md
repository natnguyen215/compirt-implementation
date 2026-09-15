# Topic-specific TF-IDF CompIRT

Adds a cumulative TF-IDF effect to the fixed- and learned-topic Stage-1 models,
with one nonnegative global `lambda_k` per topic:

```text
d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)
```

A tossup with mixture `r_j` therefore gets the adjustment
`-tfidf_prefix_j(t) * sum_k r_jk * lambda_k`. The prefix is normalized within
each tossup unless `--no-normalize-tfidf` (runner: `NO_NORMALIZE_TFIDF=1`) is
given. See [`../../tfidf/README.md`](../../tfidf/README.md) for how the prefix
is built.

## Fixed topics

PLDA, LDA, and category vectors share one trainer:

```bash
.venv/bin/python -m topic.tfidf.train_fixed_pyramidal \
  --topic-vectors topic/fixed/outputs/plda/document_latent_vectors.csv \
  --dimensions 5 --steps 5000
```

`run_fixed_topic_tfidf.sh` adds the fixed-topic bonus stage, a synergy branch
(`RUN_SYNERGY=1`, `SYNERGY_DIMENSIONS=3` by default), and evaluation. Its
default root is `results/compirt/in_sample/topic/topic-tfidf`.

```bash
DIMENSIONS=5 TOPIC_VECTORS=topic/fixed/outputs/plda/document_latent_vectors.csv \
  TOPIC_TFIDF_EFFECT_PRIOR_SCALE=1.0 topic/tfidf/run_fixed_topic_tfidf.sh
```

## Learned topics

`theta_doc` stays a Dirichlet latent, so topics and their TF-IDF effects are
fitted together. The output keeps `topic_word_matrix.npy`, `vocabulary.json`,
and `document_latent_vectors.csv` for the learned bonus stage.

```bash
.venv/bin/python -m topic.tfidf.train_learned_pyramidal \
  --split year_2024 --dimensions 5 --steps 2000
```

## Outputs and evaluation

The trainers default to `results/compirt/topic-tfidf-pyramidal` (fixed) and
`results/compirt/joint-slda-tfidf` (learned). Each writes
`topic_tfidf_lambdas.csv`, `tfidf_adjustment_curves.csv` (the signed aggregate
difficulty adjustment), `tfidf_prefix_score` in `tossup_predictions.csv`, and
the formula and lambda mapping in `summary.json`. The evaluator replays the
saved adjustments in the difficulty plots and first-buzz timing:

```bash
.venv/bin/python -m topic.tfidf.evaluate \
  --pyramidal-results <pyramidal dir> \
  --compositional-results <compositional dir> --output-dir <evaluation dir>
```

## Saved runs

`learned-topic-tfidf-all2024` and `-cal` are in
[`results/compirt/in_sample/topic/`](../../../results/compirt/in_sample/topic/)
and [`results/compirt/holdout/topic/`](../../../results/compirt/holdout/topic/);
the held-out topic-count ablation is
[`holdout/topic/topic-tfidf-ablation/`](../../../results/compirt/holdout/topic/topic-tfidf-ablation/).
