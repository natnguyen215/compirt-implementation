# Fixed-topic CompIRT equations

Read "topic form of Eq. N" as Eq. N with the learned relevance replaced by a
fixed topic mixture `r` and the difficulty moved inside the per-topic sum. The
functions named below are in `topic_compirt/pyramidal.py` and
`topic_compirt/compositional.py`.

Symbols:

- $\theta_i$ — player $i$ skill, one coordinate per topic $k$.
- $c_i$ — player $i$ buzz threshold.
- $r_j$, $r_b$ — fixed topic mixture for tossup $j$ or bonus $b$; sums to 1.
- $\beta$, $\gamma$, $\mu$ — per-topic difficulty-curve parameters.
- $t$, $T_j$ — token position and tossup length.
- $\tau$ — bonus aggregation temperature; $\psi_i$ — player synergy profile.

## Priors (Eq. 14)

Sampled in `pyramidal.sample_parameters` and `compositional.compositional_model`.

| Parameter | Prior | Shape | Versus root |
| --- | --- | --- | --- |
| $\theta_i$ | $\mathcal{N}(0, I)$ | $(n_\text{players}, n_\text{dim})$ | same |
| $c_i$ | $\mathcal{N}(0, 1)$ | $(n_\text{players},)$ | same |
| $\beta_{jk}$ | $\mathcal{N}(0, 1)$ | $(n_\text{tossups}, n_\text{dim})$ | per topic (root: scalar) |
| $\gamma_{jk}$ | $\text{Half-Cauchy}(5)$ | $(n_\text{tossups}, n_\text{dim})$ | per topic |
| $\mu_{jk}$ | $\text{Beta}(2, 2)$ | $(n_\text{tossups}, n_\text{dim})$ | per topic |
| $\beta_{bk}$ | $\mathcal{N}(0, 1)$ | $(n_\text{parts}, n_\text{dim})$ | per-topic bonus-part difficulty |
| $\tau$ | $\text{Half-Cauchy}(1)$ | scalar | same |
| $\psi_i$ | $\mathcal{N}(0, 0.5\,I)$ | $(n_\text{players}, n_\text{syn})$ | same |

There is no $\alpha$. The mixtures $r_j$ and $r_b$ are loaded by `topics.py`
into `data["topic_weight"]` before training.

## Stage 1 — tossups (Eq. 3–7, 13)

### Eq. 3 — difficulty curve (`difficulty_curve`)

$$d_{jk}(t) = \beta_{jk} \cdot \sigma\!\left(\gamma_{jk}\!\left(\mu_{jk} - \frac{t}{T_j}\right)\right)$$

### Eq. 4 — correctness logit (`correctness_logit`)

$$\text{root:} \quad \theta_i \cdot \alpha_j - d_j(t) \qquad \text{topic:} \quad \sum_k r_{jk}\bigl(\theta_{ik} - d_{jk}(t)\bigr)$$

A player pays a topic's difficulty only to the extent the tossup weights it.

### Eq. 5 — hazard (`hazard_logit`)

$$h_{ij}(t) = \sigma\!\bigl(\text{correctness\_logit}_{ij}(t) - c_i\bigr)$$

### Eq. 6 — survival (`log_survival`)

$$\log S_{ij} = \sum_{s} \log\!\bigl(1 - h_{ij}(s)\bigr)$$

The sum runs over cells before the first buzz, or through $T_j$ for a dead
tossup, and is computed with `F.logsigmoid(-logits)`.

### Eq. 13 — dead tossups

A `NO-BUZZ` event has no winner or correctness term; every rostered player's
survival runs through $T_j$.

### Eq. 7 — first-buzz likelihood (`competing_risks_model`)

Every rostered player is in the race. At the stopping cell $t^*$, with
$q(t) = \prod_i (1 - h_{ij}(t))$,

$$\log L = \sum_i \log S_{ij} + \log\!\Bigl[\bigl(1 - q(t^*)\bigr)\,\operatorname{softmax}\bigl(\eta(t^*)\bigr)_{i^*}\Bigr] + \log P\bigl(y_{i^*j} \mid p_{i^*j}(t^*)\bigr)$$

where $\eta$ are the hazard logits and $i^*$ is the first buzzer. The winner
term is `compirt_race.winner_log_prob`; see
[`docs/first-buzz-likelihood.md`](../../../docs/first-buzz-likelihood.md). The
sum is attached with `pyro.factor`. With `calibrate_correctness`, only the
correctness probability $p$ is scaled ($s \cdot \text{logit} + b$).

Stage 1 saves $\theta$ to `players.csv` and per-topic difficulty to
`tossups.csv`. `posterior_row_predictions` replays Eq. 4–6 at the posterior
medians.

## Stage 2 — bonuses (Eq. 8, 10, 11)

Stage 2 holds $\theta$ fixed. One observation is one team on one bonus part.

### Eq. 8 — member ability and aggregation

$$a_{bm} = \sum_k r_{bk}\,\theta_{mk} \qquad A_b(R) = \tau \log \sum_{m \in R} \exp\!\left(\frac{a_{bm}}{\tau}\right)$$

`topic_weighted_member_abilities` computes $a_{bm}$; `lse_aggregation` from the
root `compositional_model.py` computes $A_b$ with padded slots masked out.

### Eq. 9 — Noisy-OR

Not implemented.

### Eq. 10 — pairwise synergy (`synergy_contribution`, optional)

$$\text{synergy}(R) = \sum_{i < k,\; i,k \in R} \psi_i \cdot \psi_k$$

Synergy does not depend on the topic weights or $\theta$.

### Eq. 11 — bonus-part outcome

$$\eta_{rb} = A_b(R_r) - \sum_k r_{bk}\,\beta_{bk} \;(+\;\text{synergy}), \qquad y_{rb} \sim \mathrm{Bernoulli}\bigl(\sigma(\eta_{rb})\bigr)$$

Subtracting the weighted part difficulty outside the smooth max equals
subtracting it from every member score, because
$\text{LSE}_m(a_m - d; \tau) = \text{LSE}_m(a_m; \tau) - d$. With
`calibrate_correctness`, the whole logit is scaled.

## Map

| Paper eq. | Function | Change from root |
| --- | --- | --- |
| Eq. 14 | `sample_parameters`, `compositional_model` | no $\alpha$; per-topic $\beta, \gamma, \mu$ |
| Eq. 3 | `difficulty_curve` | per topic |
| Eq. 4 | `correctness_logit` | $r$ replaces $\alpha$ |
| Eq. 5 | `hazard_logit` | — |
| Eq. 6 | `log_survival` | — |
| Eq. 7, 13 | `competing_risks_model` | — |
| Eq. 8 | `topic_weighted_member_abilities`, `lse_aggregation` | $r$ replaces $\alpha$ |
| Eq. 10 | `synergy_contribution` | — |
| Eq. 11 | `compositional_model` | per-topic $\beta_{bk}$ |
