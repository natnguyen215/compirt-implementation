# Multidimensional-difficulty CompIRT

Stage-1 tossup model with a separate difficulty curve per latent dimension:

```text
d_jk(t)      = beta_jk * sigmoid(gamma_jk * (mu_jk - t / T_j))
logit_ij(t)  = sum_k r_jk * (theta_ik - d_jk(t))
hazard_ij(t) = logit_ij(t) - c_i
```

The relevance vector `r` has a positive `Gamma(2, 2)` prior, so more skill on a
loaded dimension always helps. It is named `r` rather than the baseline's
`alpha` because it weights the whole per-dimension skill gap, and it is saved as
`r_1..K` columns in `tossups.csv`.

`--difficulty-link tanh` replaces the sigmoid, so `d_jk(t)` spans
`(-beta_jk, beta_jk)` and can go negative late in a question. The choice is
saved as `difficulty_link` in `summary.json`, where the evaluator reads it.
Stage 2 and evaluation use the root `train_compositional.py` and
`evaluate_compirt.py` unchanged.

## Running

```bash
.venv/bin/python -m multidimensional.multidim_mirt.train_pyramidal --help

# Temporal holdout through both stages, with the synergy branch
MODEL=multidim RUN_SYNERGY=1 .venv/bin/python -m run_scripts.common.run_compirt_holdout
```

The holdout runner defaults to five skill dimensions and three synergy
dimensions, and reads `DIFFICULTY_LINK` and `CALIBRATE_CORRECTNESS`; give each
configuration its own `ROOT`. Whole-game fold runners are listed in the
[runner guide](../../run_scripts/README.md). Evaluation adds
`tossup_difficulty_curves_by_dimension.png`, which draws each dimension's curve
for sampled tossups.
