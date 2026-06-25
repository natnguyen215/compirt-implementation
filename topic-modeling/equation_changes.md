# Topic Equation Changes

This note records the equation change made in the isolated `topic-modeling`
CompIRT path. The root `pyramidal_model.py` and `compositional_model.py`
implementations are unchanged.

## Pyramidal Tossups

The earlier topic prototype still learned tossup discrimination and used the
topic vector as a mask:

```text
old topic tossup: sum_k r_jk * theta_ik * alpha_jk - d_j(t)
```

The current topic pyramidal model uses the CAIMIRA-style weighted gap:

```text
new topic tossup: sum_k r_jk * (theta_ik - d_jk(t))
```

The important change is that fixed topic weights `r_jk` replace learned tossup
discrimination `alpha_jk`. Difficulty also moved inside the weighted sum:
`beta`, `gamma`, and `mu` are now learned per topic, so each tossup has a
per-topic difficulty curve `d_jk(t)`.

## Compositional Bonuses

The earlier topic prototype also learned bonus-part discrimination and used the
topic vector as a mask:

```text
old topic bonus: LSE_m(sum_k r_bk * theta_pmk * alpha_bk; tau) - beta_b
```

The current topic compositional model uses topic-weighted member skill and
topic-weighted part difficulty:

```text
new topic bonus: LSE_m(sum_k r_bk * theta_pmk; tau) - sum_k r_bk * beta_bk
```

The important change is that fixed bonus topic weights `r_bk` replace learned
bonus discrimination `alpha_bk`. Bonus-part difficulty is now a per-topic vector
`beta_bk`, combined with the same fixed topic weights. The root smooth-max
aggregation, optional synergy term, and correctness calibration behavior are
unchanged.

Although the difficulty term is written outside the smooth-max, this is
equivalent to putting the weighted gap inside it:

```text
LSE_m(sum_k r_bk * (theta_pmk - beta_bk); tau)
= LSE_m(sum_k r_bk * theta_pmk - sum_k r_bk * beta_bk; tau)
= LSE_m(sum_k r_bk * theta_pmk; tau) - sum_k r_bk * beta_bk
```

The equivalence holds because the same weighted part difficulty is subtracted
from every roster member, and log-sum-exp is shift-equivariant:
`LSE_m(a_m - d; tau) = LSE_m(a_m; tau) - d`.
