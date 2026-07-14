# TF-IDF Pyramidal Experiments

This folder is isolated from the main baseline scripts. It implements the
cumulative TF-IDF form of the CompIRT pyramidal tossup model:

```text
cumulative-difficulty:
  d'_j(t) = d_j(t) - lambda_tfidf * tfidf_prefix_j(t)
```

`tfidf_prefix_j(t)` is normalized cumulative TF-IDF revealed through token `t`.

Run from the repo root:

```bash
.venv/bin/python -m tfidf.train_tfidf_pyramidal \
  --tfidf-variant cumulative-difficulty \
  --split year_2024 \
  --steps 1000 \
  --dimensions 1 \
  --output-dir results/compirt/in_sample/tfidf-cumulative-difficulty-pyramidal
```

The full 2024 runner uses the same cumulative flag through an environment
variable:

```bash
TFIDF_VARIANT=cumulative-difficulty bash run_scripts/run_tfidf_compirt_2024.sh
```

Useful environment overrides include `TFIDF_PLOT_COUNT=12` to draw more
TF-IDF-aware diagnostics after evaluation.

## Multidimensional TF-IDF

`tfidf/multidim/` implements the same cumulative clue-timing form with
`multidimensional/multidim_mirt`'s vector-valued difficulty flow:

```text
d_jk(t) = beta_jk * sigmoid(gamma_jk * (mu_jk - position_j(t)))
correctness_ij(t) = sum_k alpha_jk * (theta_ik - d_jk(t))
```

Run the multidimensional cumulative form with:

```bash
bash run_scripts/run_tfidf_multidim_all2024.sh
```

Or run it explicitly with:

```bash
TFIDF_VARIANT=cumulative-difficulty bash run_scripts/run_tfidf_multidim_compirt_2024.sh
```

## Tests

Unit tests for both the scalar and multidimensional cumulative models live in
`tfidf/tests/`:

```bash
.venv/bin/python -m unittest discover -s tfidf/tests -t . -v
```
