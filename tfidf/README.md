# TF-IDF Pyramidal Experiments

This folder is isolated from the main baseline scripts. It implements three
TF-IDF-aware variants of the CompIRT pyramidal tossup model:

```text
replace-position:
  d_j(t) = beta_j * sigmoid(gamma_j * (mu_j - tfidf_prefix_j(t)))

cumulative-difficulty:
  d'_j(t) = d_j(t) - lambda_tfidf * tfidf_prefix_j(t)

hazard-spike:
  correctness_ij(t) = theta_i^T alpha_j - d_j(t)
  hazard_ij(t) = correctness_ij(t) - c_i + eta_tfidf * tfidf(w_j,t)
```

`tfidf_prefix_j(t)` is normalized cumulative TF-IDF revealed through token `t`.
`tfidf(w_j,t)` is the local TF-IDF weight of the token at `t`: its
document-normalized term frequency times the smoothed corpus IDF.

Run from the repo root:

```bash
.venv/bin/python -m tfidf.train_tfidf_pyramidal \
  --tfidf-variant replace-position \
  --split year_2024 \
  --steps 1000 \
  --dimensions 1 \
  --output-dir results/compirt/in_sample/tfidf-replace-position-pyramidal
```

Other variants:

```bash
.venv/bin/python -m tfidf.train_tfidf_pyramidal --tfidf-variant cumulative-difficulty
.venv/bin/python -m tfidf.train_tfidf_pyramidal --tfidf-variant hazard-spike
```

The full 2024 runner accepts the same variant through an environment variable:

```bash
TFIDF_VARIANT=hazard-spike bash run_scripts/run_tfidf_compirt_2024.sh
```

Useful environment overrides include `TFIDF_PLOT_COUNT=12` to draw more
TF-IDF-aware diagnostics after evaluation.

## Multidimensional TF-IDF

`tfidf/multidim/` implements the same three clue-timing variants with
`multidimensional/multidim_mirt`'s vector-valued difficulty flow:

```text
d_jk(t) = beta_jk * sigmoid(gamma_jk * (mu_jk - position_j(t)))
correctness_ij(t) = sum_k alpha_jk * (theta_ik - d_jk(t))
```

Run all three multidimensional variants with:

```bash
bash run_scripts/run_tfidf_multidim_all2024.sh
```

Or run one variant with:

```bash
TFIDF_VARIANT=cumulative-difficulty bash run_scripts/run_tfidf_multidim_compirt_2024.sh
```

## Tests

Unit tests for both the scalar and multidimensional variants live in
`tfidf/tests/`:

```bash
.venv/bin/python -m unittest discover -s tfidf/tests -t . -v
```
