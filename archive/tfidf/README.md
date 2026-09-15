# Cumulative TF-IDF CompIRT

Lowers tossup difficulty by the TF-IDF mass revealed so far, with a learned
nonnegative coefficient:

```text
lambda_tfidf ~ HalfNormal(tfidf_effect_prior_scale)
d'(t) = d(t) - lambda_tfidf * tfidf_prefix_j(t)
hazard_ij(t) = correctness_ij(t) - c_i
```

`tfidf_features.attach_tfidf_prefix_scores` builds `tfidf_prefix`, shape
`(n_tossups, max_T)`, before fitting. Each token contributes
`(count(w) / doc_length) * log((1 + N) / (1 + df(w)))`, and by default the
prefix is normalized so `tfidf_prefix[j, T_j] = 1`.

| Variant | Files | Correctness |
| --- | --- | --- |
| Scalar | `pyramidal_tfidf_model.py`, `train_tfidf_pyramidal.py` | `theta_i^T alpha_j - d'_j(t)`, with `d_j(t) = beta_j * sigmoid(gamma_j * (mu_j - t / T_j))` |
| Multidimensional | `multidim/` | `sum_k r_jk * (theta_ik - d'_jk(t))`, with per-dimension `beta`, `gamma`, `mu` and `r ~ Gamma(2, 2)` |

In the multidimensional model the reduction is applied inside each dimension,
so the saved aggregate delta is `-lambda_tfidf * tfidf_prefix_j(t) * sum_k r_jk`.
Both variants save `tfidf_adjustment_curves.csv` (signed difficulty deltas that
evaluators add to the base curve), `tfidf_prefix_score` in
`tossup_predictions.csv`, and the coefficient in `summary.json`. Stage 2 is the
root `train_compositional.py`.

The prefix is indexed by raw token position but built over tokens kept by
`normalize_token`, which drops numerals and bare punctuation, so the modeled
reveal runs ahead of the text. `plot_tfidf_text_alignment.py` plots both
curves; `plot_tfidf_difficulty_curves.py` plots `d(t)` and `d'(t)`.

## Commands

```bash
bash run_scripts/tfidf/run_tfidf.sh                         # scalar
MODEL=tfidf-multidim bash run_scripts/tfidf/run_tfidf.sh    # multidimensional
.venv/bin/python -m tfidf.train_tfidf_pyramidal \
  --split year_2024 --steps 1000 --dimensions 1 --output-dir <ROOT>/pyramidal
.venv/bin/python -m tfidf.multidim.train_pyramidal \
  --split year_2024 --steps 1000 --dimensions 5 --output-dir <ROOT>/pyramidal
```

The runner fits Stage 1, both Stage-2 branches, evaluation, and a comparison,
writing to `results/compirt/in_sample/tfidf/<MODEL>-cumulative-difficulty-all2024`
(`-cal` when calibrated). `TFIDF_PLOT_COUNT` sets how many diagnostic plots it
draws.

## Saved runs

[`results/compirt/in_sample/tfidf/`](../../results/compirt/in_sample/tfidf/)
holds the scalar and multidimensional runs, each with a `-cal` variant.
