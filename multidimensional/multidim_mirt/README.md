# Multidimensional-Difficulty CompIRT

This package contains the side-by-side MIRT-style tossup variant:

```text
d_jk(t) = beta_jk * sigmoid(gamma_jk * (mu_jk - t / T_j))
logit_ij(t) = sum_k r_jk * (theta_ik - d_jk(t))
hazard_ij(t) = logit_ij(t) - c_i
```

The sigmoid inside `d_jk(t)` is the default link; the opt-in
`--difficulty-link tanh` trainer flag replaces it with tanh so the curve can go
negative late in the question (`d_jk(t)` spans `(-beta_jk, beta_jk)` instead of
`(0, beta_jk)`). The choice is recorded as `difficulty_link` in `summary.json`
and `evaluate_compirt.py` auto-detects it when replaying curves. Runners pass
it via the `DIFFICULTY_LINK` env var.

The tossup relevance vector uses a positive `Gamma(2, 2)` prior on `r`, so
higher player skill on a loaded dimension always helps. The weight is named `r`
rather than the baseline's `alpha` because per-dimension difficulty puts it
outside the skill gap; Stage 1 saves it as `r_1..K` columns.

It keeps the root CompIRT pipeline shape:

```text
multidimensional/multidim_mirt/train_pyramidal.py
-> train_compositional.py
-> train_compositional.py --use-synergy
-> evaluate_compirt.py
```

Convenience runs:

```bash
./run_scripts/multidimensional/multidim/run_multidim_all2024.sh
./run_scripts/multidimensional/multidim/run_multidim_holdout.sh
```

Both wrappers run no-calibration and calibration variants, and both include the
synergy bonus branch by default. The default multidim skill/difficulty width is
5 dimensions, matching the topic-model comparison runs; the synergy term remains
3-dimensional by default. Evaluation writes the usual aggregate difficulty graph
plus `tossup_difficulty_curves_by_dimension.png`, the multidim analogue of the
topic model's per-topic difficulty-curve graph.
