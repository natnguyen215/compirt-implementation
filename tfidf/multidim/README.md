# Multidimensional TF-IDF Pyramidal Experiments

This package combines the existing `tfidf/` cumulative clue-timing model with the
vector-valued difficulty flow from `multidimensional/multidim_mirt/`.

```text
d_jk(t) = beta_jk * sigmoid(gamma_jk * (mu_jk - position_j(t)))
correctness_ij(t) = sum_k r_jk * (theta_ik - d_jk(t))
hazard_ij(t) = correctness_ij(t) - c_i
```

The learned relevance `r_jk` uses the same positive `Gamma(2, 2)` prior as
`multidim_mirt`, so higher skill on a loaded dimension always helps. It is `r`
rather than the scalar model's `alpha` because per-dimension difficulty puts the
weight outside the skill gap (see the repo-root `CLAUDE.md` convention).

## Cumulative TF-IDF difficulty

```text
cumulative-difficulty:
  d'_jk(t) = d_jk(t) - lambda_tfidf * tfidf_prefix_j(t)
  correctness_ij(t) = sum_k r_jk * (theta_ik - d'_jk(t))

```

For `cumulative-difficulty`, the TF-IDF reduction is applied inside each
dimension before the `r`-weighted sum. The saved
`tfidf_adjustment_curves.csv` contains the aggregate replay delta:

```text
-lambda_tfidf * tfidf_prefix_j(t) * sum_k r_jk
```

Stage 2 remains the root `train_compositional.py` and optional synergy branch.
TF-IDF is a tossup clue-timing intervention, and the bonus stage only consumes
the fitted `theta` in `players.csv`.

## Running

The cumulative variant:

```bash
TFIDF_VARIANT=cumulative-difficulty bash run_scripts/run_tfidf_multidim_compirt_2024.sh
```

The all-2024 wrapper runs this cumulative variant:

```bash
bash run_scripts/run_tfidf_multidim_all2024.sh
```

Direct Stage 1 trainer:

```bash
.venv/bin/python -m tfidf.multidim.train_pyramidal \
  --tfidf-variant cumulative-difficulty \
  --split year_2024 \
  --dimensions 5 \
  --steps 1000 \
  --output-dir results/compirt/in_sample/tfidf-multidim-cumulative-pyramidal
```

The runner defaults mirror the scalar TF-IDF all-2024 runs: 5000 pyramidal
steps, 3000 bonus steps, 5 skill/difficulty dimensions, 3 synergy dimensions,
and one calibration setting per invocation.
