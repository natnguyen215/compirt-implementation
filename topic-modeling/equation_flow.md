# Topic CompIRT Equation Flow

This note walks the topic-weighted CompIRT model the way the CompIRT paper lays
out its equations: priors, then the Stage 1 pyramidal tossup likelihood, then
the Stage 2 compositional bonus likelihood. It is the forward-flow companion to
`equation_changes.md` (which only records the old-prototype to current diff).

Every equation keeps the paper's number. The topic variant changes **what plays
the discrimination role**: root CompIRT learns a free question/bonus
discrimination vector $\alpha$, while the topic model fixes a normalized topic
mixture $r$ (PLDA, LDA, or one-hot category) and learns a *per-topic* difficulty
instead. So throughout, read "topic form of Eq. N" as "Eq. N with $\alpha_k$
replaced by the fixed $r_k$, and difficulty pushed inside the per-topic sum."

Symbols:

- $\theta_i$ — player $i$ latent skill, one coordinate per topic $k$.
- $c_i$ — player $i$ confidence threshold (buzz reluctance).
- $r_j$, $r_b$ — fixed topic mixture for tossup $j$ / bonus $b$, sums to 1
  over topics. This replaces the learned $\alpha$.
- $\beta$, $\gamma$, $\mu$ — per-topic tossup difficulty curve parameters.
- $t$, $T_j$ — token position and total tossup length; $t/T_j$ is relative
  position.
- $\tau$ — bonus aggregation temperature; $\psi_i$ — player synergy profile.

The two stages live in `topic_compirt/pyramidal.py` and
`topic_compirt/compositional.py`. The function names below are in those files.

---

## Stage 0 — Priors (Eq. 14)

Sampled in `pyramidal.sample_parameters` and `compositional.compositional_model`.

| Parameter | Prior | Shape | Note vs. root |
| --- | --- | --- | --- |
| $\theta_i$ | $\mathcal{N}(0, I)$ | $(n_\text{players},\; n_\text{dim})$ | unchanged |
| $c_i$ | $\mathcal{N}(0, 1)$ | $(n_\text{players},)$ | unchanged |
| $\beta_{jk}$ | $\mathcal{N}(0, 1)$ | $(n_\text{tossups},\; n_\text{dim})$ | **per-topic** (root: scalar) |
| $\gamma_{jk}$ | $\text{Half-Cauchy}(5)$ | $(n_\text{tossups},\; n_\text{dim})$ | **per-topic** |
| $\mu_{jk}$ | $\text{Beta}(2, 2)$ | $(n_\text{tossups},\; n_\text{dim})$ | **per-topic** |
| $\beta_{bk}$ | $\mathcal{N}(0, 1)$ | $(n_\text{parts},\; n_\text{dim})$ | **per-topic** bonus-part difficulty |
| $\tau$ | $\text{Half-Cauchy}(1)$ | scalar | unchanged |
| $\psi_i$ | $\mathcal{N}(0,\; 0.5\,I)$ | $(n_\text{players},\; n_\text{syn})$ | unchanged |

There is **no $\alpha$ prior** in either stage: the fixed $r$ is the relevance
weight. The topic mixtures $r_j$ / $r_b$ are not sampled; they are loaded by
`topics.py` and attached to `data["topic_weight"]` before training.

---

## Stage 1 — Pyramidal tossups (Eq. 3–7, 13)

A tossup's difficulty falls as clues are revealed. For each player-tossup row the
model separates correctness, hazard (buzz-now-given-not-yet), and survival.

### Eq. 3 — per-topic difficulty curve (`difficulty_curve`)

Root CompIRT has one scalar curve $b_j(t)$. The topic model makes it per-topic:

$$d_{jk}(t) = \beta_{jk} \cdot \sigma\!\left(\gamma_{jk}\!\left(\mu_{jk} - \frac{t}{T_j}\right)\right)$$

$\beta_{jk}$ is the size/sign, $\gamma_{jk}$ the transition sharpness, $\mu_{jk}$ the
inflection point — now one of each per topic $k$.

### Eq. 4 — topic-weighted correctness logit (`correctness_logit`)

$$\text{root:} \quad \theta_i \cdot \alpha_j - d_j(t)$$

$$\text{topic:} \quad \sum_k r_{jk}\bigl(\theta_{ik} - d_{jk}(t)\bigr)$$

The fixed weights $r_{jk}$ replace $\alpha$, and the per-topic difficulty is
subtracted *inside* the weighted sum. This is the CAIMIRA-style relevance-gap
form: a player only pays the difficulty on topics the tossup actually weights.

### Eq. 5 — buzz hazard logit (`hazard_logit`)

$$h_{ij}(t) = \sigma\!\bigl(\text{correctness\_logit}_{ij}(t) - c_i\bigr)$$

Conditional on not having buzzed yet, the log-odds the player buzzes at $t$.
Confidence $c_i$ shifts every player's whole hazard curve.

### Eq. 6 — survival (`log_survival`)

Probability the player has not buzzed before their stopping position $t^*$:

$$\log S_{ij}(t^*) = \sum_{s \,<\, t^*} \log\!\bigl(1 - h_{ij}(s)\bigr)$$

Computed in log space for stability (`F.logsigmoid(-logits)`), masked so only
positions before $t^*$ count.

### Eq. 13 — dead tossups (no buzz)

Handled implicitly: a `NO-BUZZ` row sets $t^* = T_j$, so it contributes pure
survival across the whole question and never a hazard/correctness term.

### Eq. 7 / Eq. 12 — competing-risks likelihood (`competing_risks_model`)

Each rostered player is a competing risk for the event's first buzz:

$$\sum_i \log S_{ij}(t^*) \;+\; \log h_{i^*j}(t^*) \;+\; \log P\!\bigl(y_{i^*j} \mid p_{i^*j}(t^*)\bigr)$$

where the first term runs over all rows (BUZZ, CENSORED, NO-BUZZ), the second
and third terms apply only to the actual first buzzer $i^*$.

This is hand-summed and attached with `pyro.factor`, because competing risks are
not a single built-in distribution. If `calibrate_correctness` is set, only the
correctness factor $p$ is Platt-scaled ($s \cdot \text{logit} + b$); the shared
hazard/timing is left untouched.

**Output of Stage 1:** posterior $\theta$ (player skill), saved to `players.csv`,
plus per-topic tossup difficulty in `tossups.csv`. `posterior_row_predictions`
replays Eq. 4/5/6 at the medians; `expected_first_buzz_positions` reuses the
Eq. 5 hazards to simulate the team first-buzz distribution.

---

## Stage 2 — Compositional bonuses (Eq. 8, 10, 11)

Stage 2 holds $\theta$ fixed and learns how bonus parts convert team skill into
points. One observation is one team attempting one bonus part.

### Eq. 8 — member ability + smooth-max aggregation

Per-member topic-weighted ability (`topic_weighted_member_abilities`):

$$\text{root:} \quad \sum_k \theta_{pk} \cdot \alpha_{bk}$$

$$\text{topic:} \quad \sum_k r_{bk} \cdot \theta_{pk}$$

Aggregated across the roster by the unnormalized smooth maximum
(`lse_aggregation`, reused unchanged from root CompIRT):

$$A_b(R) = \tau \log \sum_{m \in R} \exp\!\left(\frac{a_{bm}}{\tau}\right)$$

$\tau$ controls how sharply the team score approaches its strongest member.
Padded roster slots are masked to $-\infty$ so they drop out.

### Eq. 9 — Noisy-OR

Not implemented (same as root CompIRT).

### Eq. 10 — pairwise synergy (`synergy_contribution`, optional)

$$\text{synergy}(R) = \sum_{\substack{i < k \\ i,k \in R}} \psi_i \cdot \psi_k$$

Synergy is intentionally independent of the topic weights and of $\theta$; it is
the root CompIRT pairwise roster term, added to the logit after aggregation.
Its sign is not interpretable without held-out recombined-roster validation.

### Eq. 11 — bonus-part outcome

$$\eta_{rb} = A_b(R_r) - \sum_k r_{bk} \cdot \beta_{bk} \quad (+\;\text{synergy})$$

$$y_{rb} \sim \mathrm{Bernoulli}\!\bigl(\sigma(\eta_{rb})\bigr)$$

The per-topic part difficulty $\beta_{bk}$ is collapsed against the same fixed
$r_{bk}$ (`topic_weighted_part_difficulty`). Subtracting this shared difficulty
*outside* the smooth max is equivalent to subtracting it inside, because
log-sum-exp is shift-equivariant — see `equation_changes.md` for the derivation.
Unlike Stage 1, this is a single built-in `Bernoulli`, observed directly rather
than added by hand. `calibrate_correctness` Platt-scales the whole logit, the
bonus parallel of the Stage 1 correctness fix.

**Output of Stage 2:** per-topic bonus-part difficulty (`bonus_parts.csv`) and
per-team point predictions (`team_predictions.csv`). `posterior_predictions`
replays Eq. 8/10/11 at the medians.

---

## One-screen map

| Paper eq. | What it is | Function | Change from root |
| --- | --- | --- | --- |
| Eq. 14 | priors | `sample_parameters` / `compositional_model` | — |
| Eq. 3 | $d_{jk}(t)$ — difficulty curve | `difficulty_curve` | per-topic (was scalar) |
| Eq. 4 | correctness logit | `correctness_logit` | $r$ replaces $\alpha$ |
| Eq. 5 | buzz hazard | `hazard_logit` | — |
| Eq. 6 | survival | `log_survival` | — |
| Eq. 13 | dead tossup | *(implicit: $t^* = T_j$ on NO-BUZZ rows)* | — |
| Eq. 7 | tossup likelihood | `competing_risks_model` | — |
| Eq. 8 | team aggregate | `topic_weighted_member_abilities` + `lse_aggregation` | $r$ replaces $\alpha$ |
| Eq. 9 | Noisy-OR | not implemented | — |
| Eq. 10 | synergy | `synergy_contribution` | — |
| Eq. 11 | bonus outcome | `compositional_model` | per-topic $\beta_{bk}$ |

