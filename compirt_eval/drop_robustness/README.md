# Drop-robustness evaluation: mathematical contract

This document is the full mathematical specification of the data-dropping
robustness study, in the style of `METRICS.md`. It defines the perturbation
model, every ranking functional, the agreement statistics, the exact
procedures of both tiers, and the relationship to the source paper's method.
The evaluation code lives beside this contract: `tier1.py` and `tier2.py`
collect completed fits, `metrics.py` owns drop-specific measurements,
`perturbations.py` owns drop selection and filtering, and shared scoring and
ranking metrics live in `compirt_eval/common/`. Training launchers remain in
`run_scripts/common/`. Commands and interpretation guidance are in
`docs/compirt-experiments.md`; this file is the math.

**The question.** Huang, Shen, Wei, and Broderick (arXiv 2508.11847) showed
that Bradley–Terry rankings of LLM arenas can flip their top entry when a
worst-case handful of preference records — as few as 0.003% of the data — is
deleted and the model refit. The analogous question here: how many deleted
quizbowl buzz events does it take to move, or flip, a player ranking? The
hypothesis under test is that model-based rankings (CompIRT, and especially
its multidimensional variant) degrade more gracefully than simpler rankings
built from the same data.

## The perturbation model

### What one observation is

The atomic unit of dropped data is one **buzz event**: one game hearing one
tossup, identified by `event_id = "{game_id}::{tossup_id}"`. This is the
analog of one preference record in the source paper — one competitive
interaction whose outcome feeds the model.

An event is not a single table row. `build_tossup_observations` expands event
$e$ into one row per rostered player:

- one `BUZZ` row for the recorded first buzzer, carrying the buzz position
  $t^*$ and the correctness label $y \in \{0, 1\}$;
- one `CENSORED` row for every other lineup member, recording that their
  potential buzz was preempted at $t^*$;
- for dead tossups, one `NO-BUZZ` row per player, right-censored at the
  question end $T_j$.

Dropping event $e$ removes **all** of these rows at once. Two consequences
are deliberate and worth keeping in mind. First, the perturbation is
information-coherent: there is no state in which a teammate's censoring at
$t^*$ survives while the buzz that caused it is gone. Second, dropping one
player's buzz also deletes the (weaker) survival evidence about every
teammate present at that event — a drop aimed at player $i$ perturbs
teammates' likelihoods too, exactly as deleting a preference record perturbs
both models it compared.

### The formal setup

Let $D = \{e_1, \dots, e_N\}$ be the set of events in the evaluated split
($N = 48{,}612$ for `year_2024`). A perturbation is a drop set
$W \subseteq D$; the perturbed dataset is $D \setminus W$. For each ranking
method $m$ there is a functional

$$
R_m : \text{dataset} \longrightarrow (\text{player} \mapsto \text{score}),
$$

a map from a dataset to one real-valued score per player, whose descending
sort is the ranking. For the three model-based methods, evaluating
$R_m(D \setminus W)$ requires **refitting the model from scratch** on the
reduced data (question and player parameters are co-estimated again — nothing
is frozen from the full fit); for raw actual PPG it is a direct computation.

The study measures, for each method separately,

$$
\operatorname{Agreement}\big(R_m(D),\; R_m(D \setminus W)\big)
$$

for random $W$ of size $\lfloor \alpha N \rfloor$ (Tier 1) and adversarially
chosen $W$ (Tier 2). Adapting the source paper's definition: a method is
**$\alpha$-level robust for a property** (say, the identity of the top-$k$
set) if no examined drop set of size at most $\lfloor \alpha N \rfloor$
changes that property. Because our adversarial sets come from a heuristic
rather than an exhaustive or influence-guided search, we can certify
*non*-robustness (a found flip is real, since it is refit-confirmed) but
never robustness — see the AMIP section at the end.

### Fixed seed and the noise floor

All fits — full-data and dropped — use one model seed (default 42), so a
full-vs-dropped difference is attributable to the data change, not to
re-randomized initialization. But SVI on a nonconvex objective is still not a
deterministic map from data to ranking in any useful sense: even at a fixed
seed, removing rows changes tensor shapes and gradient trajectories, and the
optimizer lands in a slightly different basin. The honest reference for "how
much movement is meaningless" is therefore the **seed-noise floor**: for each
family, the same full dataset is refit at alternate seeds (default 7 and
123), and each alternate-seed ranking is scored against the fixed-seed
ranking with the same agreement metrics. These rows appear with
`fraction = 0` in the output CSV, and the plots shade each family's band
between its minimum and maximum fraction-0 values.

**The significance rule:** a drop-induced agreement drop smaller than the
same family's own seed-noise band is not a finding. Raw actual PPG is a
deterministic computation and has no such band — its curve is pure data
effect. This per-family asymmetry is intentional and must be stated whenever
curves are compared across methods.

## How to read the notation

Symbols are defined where used; these conventions recur:

| Notation | How to read it |
| --- | --- |
| $i$, $j$, $e$ | A player, a tossup, and a buzz event (one game-tossup) |
| $t$, $T_j$ | A token position, and tossup $j$'s total token count |
| $\theta_i \in \mathbb R^K$ | Player $i$'s latent skill vector ($K$ dimensions) |
| $c_i$ | Player $i$'s buzz-confidence threshold (higher = more cautious) |
| $\sigma(x)$ | The logistic function $1/(1+e^{-x})$ |
| $h$, $p$ | A per-token buzz hazard and a correctness probability |
| $S$ | Survival: the probability that no buzz has happened yet |
| $G_i$ | Player $i$'s games played, counted from the (possibly dropped) rows |
| $\mathcal R_e$ | The roster present at event $e$ |
| $\prod_{i \in \mathcal R_e}$ | Multiply over the players present at the event |
| $\hat\theta(w)$ | Parameters refit under data weights $w$ (AMIP section) |

## The four ranking functionals

All four are **rotation-invariant scalars**. This matters because the
multidimensional latent spaces are identified only up to rotation: two refits
can represent the same fit with rotated $\theta$ axes, so any statistic built
on raw $\theta_k$ coordinates would measure basis arbitrariness, not ranking
movement. Expected points are predictions of observable quantities and are
unchanged under any rotation applied jointly to skills and question loadings.

Scores are **not comparable across methods** (they are not even on the same
scale — see each definition). Every agreement statistic compares a method
against *itself* on more data vs. less data; methods meet only at the level
of their agreement curves.

### 1. Raw actual PPG (no model)

For the observation frame under evaluation (full or dropped), let $B_i$ be
player $i$'s `BUZZ` rows and $G_i$ their number of distinct `game_id`s over
rows of *all* types (so presence without buzzing still counts a game). Then

$$
\operatorname{actualPPG}_i
= \frac{1}{G_i} \sum_{b \in B_i} \big( 10\, y_b - 5\,(1 - y_b) \big),
$$

with $\operatorname{actualPPG}_i = 0$ when $B_i$ is empty. The scoring is
deliberately the flat $+10$ correct / $-5$ neg convention rather than the
database's power-aware buzz values: it uses only columns present in the
observation frame, so it is recomputable on any dropped frame, and it matches
the value function inside the model-based walk below. No refit is ever
needed; this functional is an exact, deterministic map from data to ranking.

### 2. Plain IRT (the classical baseline, and the Bradley–Terry analog)

This is the compensatory MIRT model that the CompIRT paper presents as the
classical starting point (its Eq. 2), fit by `simple_mirt/train_plain_irt.py`
reusing `simple_mirt/model.py` unchanged. It knows nothing about buzz timing,
censoring, or competing risks — only *conversion*:

**Response matrix.** From the (possibly dropped) observation frame, build a
player × tossup matrix. Cell $(i, j)$ is *observed* when player $i$ has any
row for tossup $j$ (they were present when it was read); its value is

$$
x_{ij} =
\begin{cases}
1 & \text{if } i \text{ has a BUZZ row for } j \text{ with } y = 1,\\
0 & \text{otherwise (present but did not convert),}
\end{cases}
$$

and duplicate $(i, j)$ pairs (a player hearing the same tossup in two games)
collapse to one cell that is 1 if any hearing converted. Note the asymmetry
against the buzzer: a teammate who never got to buzz and a player who buzzed
wrong both score 0 — the plain model cannot distinguish "preempted" from
"failed", which is precisely the information the CompIRT survival model adds.

**Model.** With priors $\theta_i \sim \mathcal N(0, I_K)$,
$\alpha_j \sim \mathcal N(0, I_K)$, $d_j \sim \mathcal N(0, 1)$ (here
$K = 1$ by default, making it a classical 2PL):

$$
P(x_{ij} = 1) = \sigma\big( \alpha_j^\top \theta_i - d_j \big),
$$

with a Bernoulli likelihood over observed cells only. Inference is the shared
SVI stack (AutoNormal guide, Trace_ELBO, ClippedAdam, `pyro.set_rng_seed`);
posterior medians are the point estimates, exactly as in every other family.

**Ranking functional.** Expected conversions per game, scaled to points:

$$
\operatorname{plainPPG}_i
= \frac{10}{G_i} \sum_{j \in \mathcal O_i}
\sigma\big( \hat\alpha_j^\top \hat\theta_i - \hat d_j \big),
$$

where $\mathcal O_i$ is the set of tossups with an observed cell for $i$.
There is no $-5$ term because the model has no neg concept; the scale
therefore differs from actual/CompIRT PPG, which is fine because comparisons
are within-method. Rotation invariance holds because
$\alpha_j^\top \theta_i$ is invariant under
$(\theta, \alpha) \to (Q\theta, Q\alpha)$ for orthogonal $Q$.

### 3–4. CompIRT predicted PPG (baseline and multidim)

Both CompIRT families share one ranking functional — expected tossup points
per game under the fitted competing-risks model — and differ only in the
correctness/hazard logit that feeds it. This is the same construction as the
noise-floor expected PPG in `METRICS.md`, generalized across families.

**The scalar spine.** For the **baseline** family (root
`pyramidal_model.py`), difficulty is one scalar curve per tossup
(paper Eq. 3):

$$
b_j(t) = \beta_j \, \sigma\big( \gamma_j (\mu_j - t / T_j) \big),
$$

which starts near $\beta_j$ (obscure early clues), transitions at the
inflection $\mu_j$ with sharpness $\gamma_j$, and decays toward 0 at the
giveaway. Correctness and hazard logits (Eq. 4–5):

$$
\ell_{ij}(t) = \theta_i^\top \alpha_j - b_j(t),
\qquad
p_{ij}(t) = \sigma(\ell_{ij}(t)),
\qquad
h_{ij}(t) = \sigma(\ell_{ij}(t) - c_i).
$$

For the **multidim** family (`multidimensional/multidim_mirt/`), each latent
dimension carries its own difficulty curve and the relevance weight moves
outside the skill gap (the CAIMIRA form):

$$
d_{jk}(t) = \beta_{jk} \, g\big( \gamma_{jk} (\mu_{jk} - t / T_j) \big),
\qquad
\ell_{ij}(t) = \sum_{k=1}^{K} r_{jk} \big( \theta_{ik} - d_{jk}(t) \big),
$$

with $g$ the difficulty link ($\sigma$ in this study; `tanh` is the opt-in
alternative that lets late difficulty go negative) and $r_{jk} \ge 0$. The
hazard is again $\sigma(\ell_{ij}(t) - c_i)$. Rotation invariance of
$\ell$ holds by the same joint-rotation argument as above (for the baseline;
the multidim $r \ge 0$ constraint pins the basis differently, but the
functional still depends on parameters only through $\ell$, which is what the
fit identifies).

All parameters come from a completed fit's saved posterior medians
(`players.csv`, `tossups.csv`); the walk below is a deterministic replay, not
an inference step.

**The competing-risks roster walk.** Expected points must respect that
teammates and opponents race for the first buzz. For each event $e$ with
roster $\mathcal R_e$ and length $T_e$, walk token positions
$t = 1, \dots, T_e$ maintaining the event's survival $S_e(t)$ = probability
no one has buzzed before $t$, with $S_e(1) = 1$:

1. **Per-player hazards.** $h_i := h_{ij(e)}(t)$ for each
   $i \in \mathcal R_e$, from the fitted parameters.

2. **Someone-buzzes mass.** Treating players' buzz decisions as independent
   given survival (the model's own aggregation),

$$
H_e(t) = 1 - \prod_{i \in \mathcal R_e} (1 - h_i).
$$

3. **Attribution.** The model does not name a unique first buzzer when
   several players could buzz at the same token, so the token's event mass is
   split in proportion to each player's *only-this-player-buzzes* weight:

$$
w_i = h_i \prod_{i' \ne i} (1 - h_{i'}),
\qquad
A_i(t) = H_e(t) \, \frac{w_i}{\sum_{i' \in \mathcal R_e} w_{i'}}.
$$

   By construction $\sum_i A_i(t) = H_e(t)$: attribution conserves the
   model's own total buzz probability. (When exactly one player has
   $h_i > 0$ this reduces to $A_i = h_i$; the implementation computes
   $w_i$ as $h_i \cdot \prod_{i'}(1-h_{i'}) / (1 - h_i)$ with an
   $\varepsilon$-clamp on the denominator for numerical safety, which is the
   same product.)

4. **Value of buzzing.** If $i$ is first at $t$, the expected score is the
   flat quizbowl payoff

$$
v_i(t) = 10\, p_{ij(e)}(t) - 5\,\big(1 - p_{ij(e)}(t)\big).
$$

5. **Accumulate and advance.**

$$
\operatorname{points}_i \mathrel{+}= S_e(t)\, A_i(t)\, v_i(t),
\qquad
S_e(t+1) = S_e(t)\,\big(1 - H_e(t)\big).
$$

Positions beyond an event's own $T_e$ contribute nothing. The probability
mass remaining at the end, $S_e(T_e + 1)$, is the dead-tossup outcome and
contributes zero points — no-buzz is worth 0, and powers are not modeled.
Summing over a player's events and dividing by games gives the functional:

$$
\widehat{\operatorname{PPG}}_i
= \frac{1}{G_i} \sum_{e \ni i} \sum_{t=1}^{T_e} S_e(t)\, A_i(t)\, v_i(t).
$$

This is a *fully model-mediated* expectation: it integrates each player's
predicted buzz frequency, timing, accuracy, and competition from everyone
else at their events. A dropped event changes it through two channels at
once — the event no longer appears in the sum, and the refit moves every
parameter inside $\ell$.

## Agreement metrics (`compare_rankings`)

Given a reference score series $R$ (the method's full-data ranking) and an
alternate $A$ (a dropped-data or alternate-seed ranking), all statistics are
computed on the **common player set**
$\mathcal C = \operatorname{index}(R) \cap \operatorname{index}(A)$; a
dropped refit can lose players whose only appearances were dropped, and
`n_common` records the denominator actually used. Ranks within $\mathcal C$
use competition ranking (`method="min"`: tied scores share the smaller rank).

| Field | Definition | Better under robustness |
| --- | --- | --- |
| `kendall_tau` | Kendall $\tau_b$ between $R$ and $A$ on $\mathcal C$ | Higher (1 = same order) |
| `spearman` | Pearson correlation of the two rank vectors | Higher |
| `jaccard_top{5,10,25}` | $\lvert T_k(R) \cap T_k(A)\rvert / \lvert T_k(R) \cup T_k(A)\rvert$ | Higher (1 = same set) |
| `top1_changed` | $\arg\max R \ne \arg\max A$ | False |
| `max_displacement_top25` | $\max_{i:\, \operatorname{rank}_R(i) \le 25} \lvert \operatorname{rank}_R(i) - \operatorname{rank}_A(i) \rvert$ | Lower |
| `mean_abs_ppg_change` | $\operatorname{mean}_{i \in \mathcal C} \lvert R_i - A_i \rvert$ | Lower |

**Kendall $\tau_b$** counts concordant and discordant player pairs. A pair
$(i, i')$ is concordant when both rankings order it the same way and
discordant when they disagree; with $P$ concordant, $Q$ discordant, and tie
corrections $T_R$, $T_A$ (pairs tied within each series),

$$
\tau_b = \frac{P - Q}{\sqrt{(P + Q + T_R)(P + Q + T_A)}}.
$$

This is scipy's default variant and is the statistic most sensitive to
diffuse, ranking-wide reshuffling. **Spearman** correlates the two rank
vectors and is dominated by large individual displacements. **Top-$k$
Jaccard** ($T_k(\cdot)$ = the $k$ highest-scored players; ties at the
boundary are broken by index order, i.e. effectively arbitrarily) ignores
order within the top set and asks only whether membership changed — the
statistic closest to the source paper's "did the top-$k$ set change".
`max_displacement_top25` isolates the players anyone actually looks at: how
far did somebody from the reference top 25 move. `mean_abs_ppg_change` is the
only score-scale (not rank-scale) field and is comparable only within a
method.

Because $\tau_b$ and Spearman are computed over all
$\sim \binom{1455}{2} \approx 10^6$ player pairs, they can look reassuringly
high while the top of the ranking churns; conversely top-$k$ Jaccard can be
1 while the mid-field reshuffles. Read them together.

## Tier 1: random dropping (average case)

The uniform data-dropping experiment (source paper's Appendix A.3), on a
grid of fractions $\alpha \in \{0.001, 0.005, 0.01, 0.05\}$ × replicates
$r \in \{1, \dots, R\}$ (default $R = 3$).

**Drop-list generation.** The event universe is
$\operatorname{sorted}(\text{unique event\_ids})$ — sorted so selection is
independent of row order. For cell $(\alpha, r)$, the RNG is seeded with the
sequence $(\text{drop\_seed}, \lfloor \alpha \cdot 10^6 \rceil, r)$, so every
cell's list is deterministic, distinct, and reproducible from the config
alone; the list size is $\max(1, \lfloor \alpha N \rfloor)$ events, drawn
without replacement. Lists are written to
`droplists/frac_<α>/rep_<r>.txt` **before any fit** and never regenerated
once present: completed fits were trained against exactly the file on disk,
so the file, not the generator, is the artifact of record. One list is shared
by all four methods — every comparator sees the identical perturbation.

**Fits.** Per family: one fixed-seed full fit, one fixed-seed fit per drop
cell (`--drop-events` pointing at the cell's list), and one full fit per
noise seed. Every fit is Stage-1 only — player ranking never touches the
bonus model, since Stage 2 freezes $\theta$ — in-sample on the evaluated
split, resumable off its `summary.json`.

**Collection.** For each cell, the runner re-filters the in-memory full
observation frame with the saved list (the same operation the trainer
performed), rebuilds tensors and the games denominator from the filtered
frame, evaluates the family's functional from the cell's saved parameters,
and scores it against the same family's full-data ranking. The raw actual-PPG
row for a cell is computed once per drop list (it is model-independent). The
curves plot, per method, the mean of each metric across replicates at each
fraction (individual replicates shown as scatter), on a log-$x$ fraction
axis, with each family's fraction-0 noise band shaded.

Note the denominators move with the drop: $G_i$ and $\mathcal O_i$ are
recomputed from the dropped frame, so a player who loses an entire game's
events loses that game from their divisor as well. Both the full and dropped
sides of every comparison are internally consistent — each ranking is the
functional applied to its own dataset.

## Tier 2: targeted dropping (worst case)

The paper's headline experiment: find a small drop set aimed at a specific
ranked pair, refit, and report the smallest set that flips them.

**Pair selection.** Following the paper's greedy strategy ("closeness in
score"), the default target is the adjacent pair with the smallest
predicted-PPG gap inside the reference ranking's top 10: with players ordered
by the reference model's full-data $\widehat{\operatorname{PPG}}$,

$$
\text{target} = \arg\min_{i \in \text{top }10}
\big( \widehat{\operatorname{PPG}}_{(i)} - \widehat{\operatorname{PPG}}_{(i+1)} \big),
$$

and the rival is the player ranked immediately below. The smallest gap is the
cheapest to close, so this is the most favorable case for finding a flip.
Explicit `--target-player`/`--target-rank`/`--rival` override the default.

**The heuristic influence proxy.** Candidate events are the target's own
`BUZZ` events, ordered by ascending relative buzz position
(`demote`: their correct buzzes; `promote`: their negs), ties broken by
`event_id` for determinism. The justification comes from the likelihood
itself. A correct buzz by the target at early position $t^*$ contributes to
the log-likelihood (paper Eq. 7):

- a hazard term $\log h_{ij}(t^*)$ and a correctness term
  $\log p_{ij}(t^*)$, both increasing in
  $\ell_{ij}(t^*) = \theta_i^\top \alpha_j - b_j(t^*)$ — and $b_j(t)$ is
  **largest early** ($b_j(t^*) \approx \beta_j$ for small $t^*/T_j$), so an
  early correct buzz forces $\theta_i^\top \alpha_j$ to clear a high bar:
  it is the single strongest upward pull on the target's skill the data
  contains;
- survival terms $\log S_{i'j}(t^*)$ for everyone else, which are the
  (weaker) collateral evidence removed along with the event.

Dropping the earliest correct buzzes first therefore removes the target's
best supporting evidence in approximately decreasing order of influence —
a zeroth-order surrogate for the gradient-based influence score AMIP would
compute (see below). For `promote`, the same logic inverts: an early neg is
the strongest *downward* evidence (confident enough to buzz, wrong anyway),
and removing negs relieves the target's estimate.

**Nesting.** The ranked candidate table is saved once
(`ranked_events.csv`), and the drop list for count $n$ is its $n$-prefix.
Prefixes are nested, so "flips at $n$" is monotone in evidence removed and
the minimum flip count is well defined up to the granularity of the counts
grid.

**Refit and flip test.** For each family and count
$n \in \{5, 10, 25, 50, 100, 200\}$ (bounded by the target's candidate
supply), one fixed-seed refit on $D$ minus the $n$-prefix. With
$g(n) = \widehat{\operatorname{PPG}}_{\text{target}} -
\widehat{\operatorname{PPG}}_{\text{rival}}$ evaluated on that refit,

$$
\operatorname{flipped}(n) \iff \operatorname{sign}\, g(n) \ne \operatorname{sign}\, g(0),
$$

and the reported **flip bracket** is
$(\max\{n : \text{held}\},\ \min\{n : \text{flipped}\}]$ over the counts
actually run — an interval, because the grid does not test every integer.
Both players' ranks in each refit ranking, and the whole-ranking agreement
fields, are recorded alongside the gap.

**The exact raw curve.** Raw actual PPG needs no refit, so it is evaluated at
*every* prefix length $n = 0, 1, \dots$, giving the raw ranking's **exact**
minimal flip count. For a demote attack the raw arithmetic is transparent:
each dropped correct buzz removes 10 points from the target (until a game
loses its last event and $G_i$ shrinks), so the raw gap falls by roughly
$10 / G_{\text{target}}$ per drop — which is why the raw ranking flips after
a handful of events and the model rankings, which re-estimate skill from all
remaining evidence, are hypothesized to hold longer.

**Noise context for the gap.** Because the pair gap is a difference of two
noisy estimates, each family's flip is read against its own gap jitter: with
$g^{(s)}$ the pair gap under the family's alternate-seed full fits,
`noise_gap_std` is the population standard deviation ($\mathrm{ddof}=0$) of
$\{g(0)\} \cup \{g^{(s)}\}$. A flip whose driving gap change is within this
jitter is not a finding, even though the sign test formally triggered.

## Relation to AMIP (what is and is not inherited)

The source paper's selector is the Approximate Maximum Influence
Perturbation. In their setting the fit is an M-estimator
$\hat\theta(w) = \arg\max_\theta \sum_n w_n \ell_n(\theta)$ with per-datum
weights $w \in \{0,1\}^N$, and the effect of dropping datum $n$ on a scalar
functional $\varphi(\hat\theta)$ (there: a Bradley–Terry score gap) is
linearized at $w = \mathbf 1$:

$$
\frac{\partial \varphi(\hat\theta(w))}{\partial w_n}
= -\nabla_\theta \varphi^\top H^{-1} g_n,
\qquad
H = \nabla^2_\theta \textstyle\sum_n \ell_n,\quad
g_n = \nabla_\theta \ell_n,
$$

so the most damaging $\lfloor \alpha N \rfloor$-subset under the linear
approximation is simply the points with the most negative influence on
$\varphi$. Crucially, they then **refit exactly** with those points removed
and report only refit-confirmed reversals.

This study keeps the second half of that contract and replaces the first:

- **Kept — refit confirmation.** Every Tier-2 flip is the result of an
  actual refit on the reduced data. A reported flip is therefore definitive
  for the examined drop set, exactly as in the paper.
- **Replaced — the selector.** Instead of $-\nabla\varphi^\top H^{-1} g_n$
  (which for the CompIRT survival likelihood would require per-event
  gradients and Hessian-inverse–vector products through a Pyro SVI fit), the
  selector is the likelihood-motivated heuristic above. It shares the drop
  list interface (`observations → ordered event_ids`), so a true
  influence-based selector can replace it later without touching anything
  downstream.
- **The resulting asymmetry.** Both the heuristic and AMIP itself can miss
  the true worst-case subset (the paper notes its own false negatives —
  the linearization is not exhaustive search). Therefore: *flip counts are
  upper bounds on the worst case's size; "no flip within $n$" is evidence,
  not a certificate.* Comparative statements across methods are still valid
  because every method faces the same drop sets.
- **Not copied — bootstrap intervals.** The paper reads its flips against
  bootstrap confidence intervals; this study substitutes the repo's existing
  fixed-seed noise-floor pattern (a few alternate-seed refits), which
  answers the same question — is the movement bigger than fitting noise? —
  at a fraction of the cost.

## Interpretation limits

- **In-sample, transductive.** All fits estimate players and questions
  jointly on the evaluated split. The study measures the stability of the
  *fitted* ranking under data deletion, not out-of-sample generalization.
- **Within-method comparisons only.** The functionals live on different
  scales (plain PPG has no neg penalty; raw PPG uses discrete outcomes;
  model PPG integrates predicted buzz frequency). Only the agreement curves
  are cross-method comparable.
- **Seed jitter bounds resolution.** Even at a fixed seed, refits move.
  Effects inside a family's fraction-0 band are unresolvable; conclusions
  should quote the band. The committed
  `multidim-tanh-all2024-noisefloor` results are for the tanh link and are
  *not* the floor for this study's sigmoid default — the runners fit their
  own.
- **Drops are event-coherent, not player-surgical.** Removing a target's
  buzz also removes teammates' censored rows for that event, slightly
  perturbing their fits too. This mirrors reality (a deleted record deletes
  all its information) but means a "targeted" drop is not a pure
  single-player intervention.
- **Minimum drop granularity.** Tier 1 drops at least one event even at
  fractions below $1/N$; `n_events_dropped` in the CSV records the truth.
- **Unequal candidate supplies.** A Tier-2 target with fewer correct buzzes
  than the largest requested count silently truncates the counts grid (the
  runner prints the truncation); flip brackets are relative to the counts
  actually run.

## Artifact map

| Artifact | Contents |
| --- | --- |
| `<root>/droplists/frac_<α>/rep_<r>.txt` | One dropped `event_id` per line; the perturbation of record for that cell |
| `<root>/<family>/{full,noisefloor/seed_<s>,frac_<α>/rep_<r>}/pyramidal/` | Each fit's `players.csv`, `tossups.csv` (or `questions.csv` for plain), `summary.json` with drop bookkeeping |
| `<root>/csvs/drop_robustness_metrics.csv` | One row per (method, fraction, replicate) and per (family, fraction 0, noise seed) with every agreement field |
| `<root>/graphs/{kendall_tau,topk_jaccard}_vs_fraction.png` | The two Tier-1 curves, noise bands shaded |
| `<targeted-root>/droplists/<direction>_<player>/ranked_events.csv`, `n_<count>.txt` | The influence-proxy ordering and its prefixes |
| `<targeted-root>/csvs/targeted_flip_metrics.csv` | Per (family, count): gap, both ranks, flip flag, `noise_gap_std`, agreement fields |
| `<targeted-root>/csvs/actual_flip_curve.csv` | The exact raw-PPG gap at every prefix length |
| `<targeted-root>/graphs/gap_vs_dropped.png` | Gap trajectories with the zero line and seed-noise error bars |
| `<root>/ablation_config.json`, `run.log` | Every resolved runner setting and the full command log |
| `<root>/README.md` | Written per completed run: measured noise floors, aggregate tables, and that run's reading under the significance rule (the committed Tier-1 run: `results/compirt/in_sample/common/drop-robustness/README.md`) |
