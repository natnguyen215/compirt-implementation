# hazard_double_difficulty

CompIRT Stage-1 variants that separate correctness evidence from buzz timing.

## Why

Every other family fits one curve and uses it for both jobs:

```
correctness_logit = sum_k r_jk * (theta_ik - d_jk(t))
hazard_logit      = correctness_logit - c_i
```

The hazard is the correctness logit shifted by a single per-player scalar `c_i`,
so one curve has to explain both "how hard is this to answer right at token `t`"
and "how tempting is this to buzz on at token `t`". The only freedom between them
is a constant that varies with neither `t` nor the question.

This family gives each term its own curve:

```
correctness_logit = sum_k r^corr_jk * (theta_ik - d^corr_jk(t))
hazard_logit      = sum_k r^haz_jk * (theta_ik - d^haz_jk(t)) - c_i
```

The skill `theta` and confidence `c` stay shared. The two-curve families give
correctness and hazard independent relevance vectors and difficulty curves
under matching priors. `multidim/` is a near-copy of
`multidimensional/multidim_mirt/`: setting both relevance vectors and both
curves equal reproduces that model exactly (asserted in `tests/`).

## Variants

| Subpackage | Curve |
| --- | --- |
| `multidim/` | `d_jk(t) = beta_jk · link(gamma_jk · (mu_jk − t/T_j))`, `link ∈ {sigmoid, tanh}` |
| `bernstein/` | strictly decreasing degree-`p` Bernstein polynomial in `x = t/T_j` |
| `perceived_difficulty_bernstein/` | one shared vector Bernstein curve and simplex relevance; player vectors transform difficulty only for buzzing |
| `perceived_logit_bernstein/` | one shared vector Bernstein curve and simplex relevance; player scalars transform the complete correctness logit for buzzing |

### Shared difficulty with player perception

`perceived_difficulty_bernstein/` is an intentionally coupled exception to the
two-curve families above. It learns one item curve and one relevance simplex:

```
correctness_logit = sum_k r_jk * (theta_ik - d_jk(t))
hazard_logit      = sum_k r_jk * (theta_ik - alpha_ik*d_jk(t) + beta_ik)
```

Here `r_j ~ Dirichlet(2)`, `alpha_i ~ LogNormal(0, 1)`, and
`beta_i ~ Normal(0, 1)` coordinate-wise. Thus `alpha > 0` (with prior median
one), while `beta` is unconstrained. The literal equations have
no confidence `c`, correctness calibration, or terminal-cell intercepts. The
frozen five-fold runner is
`python -m run_scripts.double_difficulty.run_perceived_difficulty_bernstein_332`.

An opt-in three-slice arm replaces each player's single perception vectors
with first/middle/last vectors selected by relative token position:

```
slice(x)          = first if x < 1/3, middle if x < 2/3, else last
hazard_logit      = sum_k r_jk *
                    (theta_ik - alpha_i,slice(x),k*d_jk(t)
                              + beta_i,slice(x),k)
```

Every sliced `alpha` remains an independent `LogNormal(0, 1)` draw and every
sliced `beta` an independent `Normal(0, 1)` draw. Enable it directly with
`--perception-slices 3`, or use the frozen five-fold runner
`python -m run_scripts.double_difficulty.run_perceived_difficulty_sliced_bernstein_332`.
`--alternate-player-steps` alternates theta-only and perception-only player
updates (runner `run_perceived_difficulty_sliced_alternating_bernstein_332`).

`perceived_logit_bernstein/` shares the same correctness evidence literally,
then applies one scalar affine transform per player:

```
correctness_logit = sum_k r_jk * (theta_ik - d_jk(t))
hazard_logit      = alpha_i * correctness_logit + beta_i
```

Here `alpha_i ~ LogNormal(0, 1)` and `beta_i ~ Normal(0, 1)`. Both are reused
for every question heard by player `i`; there are no player-question
interaction parameters. Thus `alpha > 0` (with prior median one), while `beta`
is unconstrained. This model likewise has no `c`, correctness calibration, or
terminal-cell intercepts. Its five-fold runner is
`python -m run_scripts.double_difficulty.run_perceived_logit_bernstein_332`.

Both perception trainers accept `--alpha-prior normal-zero` or `normal-one`,
which replace the LogNormal with `Normal(0, 1)` or `Normal(1, 1)` and leave
`alpha` unconstrained.

Both curves in a run share the link (multidim) or the degree and Dirichlet
concentration (Bernstein), so they stay the same functional form.

### Sample sites

Each full-model difficulty site appears twice:

| multidim | Bernstein | prior |
| --- | --- | --- |
| `beta_{correct,hazard}` | `start_difficulty_{correct,hazard}` | `Normal(0, 1)` / `Normal(0, 1)` |
| `gamma_{correct,hazard}` | `total_drop_{correct,hazard}` | `HalfCauchy(5)` / `LogNormal(0, 0.5)` |
| `mu_{correct,hazard}` | `drop_proportions_{correct,hazard}` | `Beta(2, 2)` / `Dirichlet(conc)` |

`r_correct, r_hazard ~ Gamma(2, 2)` are independent draws by default in the
vector DD families. The multidim and Bernstein trainers also accept
`--relevance-prior simplex`, which instead gives both sites independent
`Dirichlet(1, ..., 1)` priors with no separate discrimination scale. In both
forms, `theta ~ N(0, I)` and `c ~ N(0, 1)` remain shared.

The Bernstein trainer also accepts `--learn-curve-locations`. This learns two
global population locations,
`curve_location_correct, curve_location_hazard ~ Normal(0, 1)`, and centers
each branch's item-by-dimension start difficulties at its corresponding
location with unit scale. Without the flag both start priors are
`Normal(0, 1)`.

### Terminal-cell intercepts

`bernstein/` adds two global scalars, `end_correct` and `end_hazard`
(`Normal(0, 2)`), to the correctness and hazard logits at `t = T_j` only. They
are on by default; `--no-terminal-intercepts` removes them. `multidim/` exposes
the same sites through opt-in `--terminal-intercepts`. The values are saved in
`summary.json`, and replay treats a missing key as zero. The measurement behind
them is in
[`docs/double-difficulty-bernstein.md`](../docs/double-difficulty-bernstein.md#terminal-cell-intercepts).

## Commands (modules from the repo root)

```bash
.venv/bin/python -m hazard_double_difficulty.multidim.train_pyramidal --help
.venv/bin/python -m hazard_double_difficulty.bernstein.train_pyramidal --help
.venv/bin/python -m hazard_double_difficulty.perceived_difficulty_bernstein.train_pyramidal --help
.venv/bin/python -m hazard_double_difficulty.perceived_logit_bernstein.train_pyramidal --help

# tests (synthetic data only)
.venv/bin/python -m unittest discover -s hazard_double_difficulty/tests -t . -v
```

Each trainer's `--help` lists its options. Family-specific ones are
`--difficulty-link`, `--relevance-prior`, and `--terminal-intercepts` for
multidim; `--degree`, `--drop-concentration`, `--relevance-prior`,
`--learn-curve-locations`, and `--no-terminal-intercepts` for Bernstein; and
`--alpha-prior`, `--relevance-concentration`, plus (perceived difficulty only)
`--perception-slices` and `--alternate-player-steps` for the perception models.

The 3/3/2 simplex-relevance, learned-location, terminal-intercept arm is:

```bash
.venv/bin/python -m run_scripts.double_difficulty.run_dd_bernstein_332 \
  --relevance-prior simplex --learn-curve-locations \
  --root results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal
```

Its sigmoid counterpart (three dimensions, independent simplex relevance, and
terminal intercepts) is the multidim trainer with `--relevance-prior simplex
--terminal-intercepts --difficulty-link sigmoid`; its completed five folds are in
`results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid/`.

## Saved columns

`players.csv` is unchanged from the parents, so Stage 2
(`train_compositional.py`) works against these runs unmodified.

In `tossups.csv` the **correctness** curve takes the parents' canonical column
names and the **hazard** curve is prefixed with `hazard_`:

```
multidim:   r_1..K, hazard_r_1..K,
            beta_1..K / gamma_1..K / mu_1..K
            hazard_beta_1..K / hazard_gamma_1..K / hazard_mu_1..K

bernstein:  r_1..K, hazard_r_1..K,
            start_difficulty_dK / end_difficulty_dK / total_drop_dK / drop_share_M_dK
            hazard_start_difficulty_dK / hazard_end_difficulty_dK /
            hazard_total_drop_dK / hazard_drop_share_M_dK

perceived difficulty: players.csv has theta_1..K, alpha_1..K, beta_1..K (no c);
                      schema is `perceived-difficulty-bernstein`

sliced perceived difficulty: players.csv has theta_1..K plus
                      alpha_{first,middle,last}_1..K and matching beta columns;
                      schema is `perceived-difficulty-sliced-bernstein`

perceived logit: players.csv has theta_1..K plus scalar alpha and beta (no c);
                 schema is `perceived-logit-bernstein`

both perceived families: tossups.csv has simplex r_1..K and one canonical
                         Bernstein curve
```

`compirt_eval/scenario_a_tossups/parameters.py` reads these as two explicit
families. Correctness plots and probabilities use the canonical columns.
Buzz-position replay, survival, first-buzzer identity, and simulations
automatically select `hazard_*`. Standard evaluation also writes separate
correctness and hazard curve galleries, per-dimension pages, population
percentile figures, and sampled percentile CSVs.
