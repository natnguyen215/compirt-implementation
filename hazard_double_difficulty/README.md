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

Everything else is the parent's math verbatim. The skill `theta` and confidence
`c` stay shared. The vector DD families give correctness and hazard independent
relevance vectors and difficulty curves under matching priors. Set both
relevance vectors and both curves equal and the model reproduces its parent
exactly (asserted in `tests/`).

## Variants

| Subpackage | Parent | Curve |
| --- | --- | --- |
| `multidim/` | `multidimensional/multidim_mirt/` | `d_jk(t) = beta_jk · link(gamma_jk · (mu_jk − t/T_j))`, `link ∈ {sigmoid, tanh}` |
| `bernstein/` | `polynomial_compirt/` | strictly-decreasing degree-`p` Bernstein polynomial in `x = t/T_j` |
| `compact_bernstein/` | scalar CompIRT spine | normalized skill direction and positive discrimination, with separate scalar correctness/hazard Bernstein curves |
| `perceived_difficulty_bernstein/` | `polynomial_compirt/` | one shared vector Bernstein curve and simplex relevance; player vectors transform difficulty only for buzzing |
| `perceived_logit_bernstein/` | `polynomial_compirt/` | one shared vector Bernstein curve and simplex relevance; player scalars transform the complete correctness logit for buzzing |

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
no confidence `c`, correctness calibration, or terminal-cell intercepts.  The
ready-made frozen five-fold arm is
`python -m run_scripts.bernstein.run_perceived_difficulty_bernstein_332`.
Completed legacy result directories remain readable because replay detects the
saved numbered player columns rather than relying on the directory name.

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
`python -m run_scripts.bernstein.run_perceived_difficulty_sliced_bernstein_332`.
The one-slice default and runner are unchanged.

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
`python -m run_scripts.bernstein.run_perceived_logit_bernstein_332`.

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

The Bernstein trainer also accepts `--learn-curve-locations`. Like compact DB,
this learns two global population locations,
`curve_location_correct, curve_location_hazard ~ Normal(0, 1)`, and centers
each branch's item-by-dimension start difficulties at its corresponding
location with unit scale. Without the flag both start priors remain
`Normal(0, 1)`, reproducing earlier fits.

### Terminal-cell intercepts

`bernstein/` additionally samples two **global** scalars, `end_correct` and
`end_hazard`, both `Normal(0, 2)`, on by default. They are added to the
correctness and hazard logits only at `t = T_j`. That final cell is not one more
token: it also absorbs the whole post-reading buzz window, and the empirical
team hazard there is 0.75 against 0.29 one token earlier and 0.05 mid-question
(`analysis/terminal_cell/`). Because they are global they live in
`summary.json`, not `tossups.csv`; `holdout.frozen_predict` and the Scenario A
timing replay both read them from there and treat their absence as zero, so
fits without the sites and every earlier fit are unaffected.
`--no-terminal-intercepts` drops both sites and reproduces the earlier model
exactly. `dd_linear_spline/` carries the same two sites.

The multidim family exposes the same sites as an opt-in
`--terminal-intercepts` feature. Its default remains off so earlier sigmoid and
tanh protocols are unchanged.

## Commands (modules from the repo root)

```bash
.venv/bin/python -m hazard_double_difficulty.multidim.train_pyramidal --help
.venv/bin/python -m hazard_double_difficulty.bernstein.train_pyramidal --help
.venv/bin/python -m hazard_double_difficulty.compact_bernstein.train_pyramidal --help
.venv/bin/python -m hazard_double_difficulty.perceived_difficulty_bernstein.train_pyramidal --help
.venv/bin/python -m hazard_double_difficulty.perceived_logit_bernstein.train_pyramidal --help

# 5-fold neg/buzz benchmark against the single-curve arms
CONFIGS=dd-multidim,multidim .venv/bin/python -m neg_test.run_neg_test

# tests (synthetic data only)
.venv/bin/python -m unittest discover -s hazard_double_difficulty/tests -t . -v
```

CLI flags are at parity with each parent (`--dimensions`, `--steps`, `--lr`,
`--seed`, `--device`, `--calibrate-correctness`, `--calibration-no-scale`,
`--include-bounceback`, `--train-posterior`, `--new-player-prior`; plus
`--difficulty-link` / `--relevance-prior` / `--terminal-intercepts` /
`--ppc-draws` / `--drop-events` for multidim and
`--degree` / `--drop-concentration` / `--relevance-prior` /
`--learn-curve-locations` / `--no-terminal-intercepts` for Bernstein), and
`--perception-slices {1,3}` for perceived difficulty.

The 3/3/2 simplex-relevance, learned-location, terminal-intercept arm is:

```bash
.venv/bin/python -m run_scripts.bernstein.run_dd_bernstein_332 \
  --relevance-prior simplex --learn-curve-locations \
  --root results/compirt/holdout/double-difficulty/reference-model
```

Its requested sigmoid counterpart (three dimensions, independent simplex
relevance, and terminal intercepts) is pinned by a five-fold runner:

```bash
.venv/bin/python -m run_scripts.multidimensional.multidim.run_dd_sigmoid_simplex_terminal
```

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
