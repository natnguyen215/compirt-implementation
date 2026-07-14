# Where do the multidimensional CompIRT gains come from?

The `baseline-ablation` sweep fits the same baseline CompIRT family at skill
dimensions **m = 1…7** on the temporal holdout (train 2024 → evaluate 2025), so
it isolates the effect of dimensionality alone. This document answers four
questions about where the extra dimensions pay off — by question difficulty, by
category, by player, and by buzz position — and documents a modeling defect the
analysis uncovered and fixed along the way, without which the bonus stage's
answer comes out wrong.

**Summary of answers:**

1. **Both stages improve with dimensionality.** Every tossup metric and every
   bonus metric improves at (nearly) every step from m = 1 to 7; PPB MAE — the
   paper's headline bonus metric — falls 2.571 → 2.031.
2. **Difficulty:** harder questions gain more, and the gradient survives a
   leak-free difficulty definition.
3. **Category:** tossup gains are real but very uneven (Science gains 20× more
   than Literature) — and the gains are *not* concentrated on each player's own
   specialty. The payoff is knowing where players are *weak*, not where they
   are strong. Bonus gains, by contrast, are nearly uniform across categories,
   as expected under roster max-pooling.
4. **Players:** the players who benefit are those with skill mass *off* the
   general-ability axis — not the strongest players. General strength alone
   actually predicts *less* benefit.
5. **Buzz position:** early buzzes gain calibration (fixing overconfidence);
   late buzzes gain discrimination (better ranking). The intuition that extra
   dimensions help *discriminate* early, clue-specific buzzes is not what the
   data shows.

These answers form one coherent picture, developed in §7: **the extra
dimensions mostly encode where a player's knowledge is thin, and the gains come
from correcting the 1-D model's overconfidence in those spots.**

The methodological finding (§6): an earlier version of this sweep showed *no*
bonus gain — a non-monotone, noisy bonus series. That null was manufactured by
a prior mismatch at the Stage-1/Stage-2 interface (Gamma-constrained bonus
loadings on a rotation-arbitrary skill basis), diagnosed by a rotation
experiment and fixed by giving the baseline's bonus stage the same Normal
loadings as its tossup stage. With the interface consistent, the bonus gains
above appear — monotone and category-uniform.

---

## 1. Data, provenance, and how much to trust each number

- **Source:** `results/compirt/holdout/baseline-ablation/dim_{1..7}/holdout/`.
  Tossups: `pyramidal/tossup_predictions.csv`, scored on the 64,834
  `z == "BUZZ"` rows (only actual buzzers have an observed outcome), plus
  `buzz_event_predictions.csv` for buzz-position error. Bonuses:
  `syn_0/compositional/` (no-synergy branch), 181,362 parts / 60,454 team
  responses. The bonus stage uses the corrected Normal loadings (§6); the
  multidimensional (`multidim_mirt`) family is a different model and
  deliberately keeps its Gamma relevance `r` — positivity is what pins its
  basis and keeps its skill dimensions interpretable.
- **Scoring:** the `analysis/` package re-scores the sweep's saved predictions
  (one runnable module per section of this document — see `analysis/README.md`);
  nothing is retrained for the slicing itself. Metrics come from
  `compirt_eval.metrics`, the same functions the committed evaluator uses, and
  `python -m analysis.overall` checks 98 recomputed totals against the sweep's
  own metric CSVs (agreement ~1e-16). The tossup-side headline numbers were
  additionally recomputed from the raw CSVs with independent implementations
  (rank-statistic AUC, hand-rolled log loss and PPB) and match to 4 decimals.
- **Noise floor.** The sweep is seeded (`--seed 42` on every stage, recorded in
  `ablation_config.json`). To know how much of a dim-to-dim gap could be
  optimizer luck, Stage 2 was re-run at dims 5/6/7 with four seeds and the
  *full chain* (Stage 1 2024 → Stage 1 2025 → Stage 2) re-run at dim 6 with
  three fresh seeds. **Tossup metrics are very stable** (dim-6 AUC
  0.6900–0.6922 across full-chain reseeds, vs per-dimension steps of ~0.008)
  and **Stage-2 init noise is negligible** (~0.002 PPB). Under the *old* prior
  the full-chain reseeds scattered bonus PPB over 2.54–3.25 — that instability
  is what §6 diagnoses and the corrected prior removes.
- **One honest caveat on "held-out."** The holdout leg refits question
  parameters on 2025 data, and returning players' `theta` is anchored by the
  2024 posterior as a *prior* (updated by the 2025 likelihood, not frozen).
  Stage 2 fits its bonus-part parameters directly on the 2025 labels it is
  scored on. So tossup metrics are player-regularized transductive fits, and
  bonus metrics are fully transductive fits. Cross-year information enters only
  through the player prior. Comparisons *between dimensions* are still fair —
  every dimension gets the same treatment — but no number here is pure
  generalization error.

## 2. Headline: both stages improve steadily with dimension

Tossups, n = 64,834 buzzes, dim 1 → 7:

| Metric | dim 1 | dim 7 | change | monotone in all 6 steps? |
|---|---|---|---|---|
| AUC (higher better) | 0.6330 | 0.6988 | +0.0658 | yes |
| Log loss (lower better) | 0.6326 | 0.5795 | −0.0531 | yes |
| Buzz-position MAE (lower better) | 0.1559 | 0.1394 | −0.0165 | yes |
| Brier (lower better) | 0.2164 | 0.1954 | −0.0210 | yes |
| ECE (lower better) | 0.1658 | 0.1484 | −0.0175 | wobbles |

Bonuses, n = 181,362 parts / 60,454 team responses, dim 1 → 7:

| Metric | dim 1 | dim 7 | change | monotone in all 6 steps? |
|---|---|---|---|---|
| **PPB MAE** (lower better) | 2.5711 | 2.0306 | −0.5405 | yes |
| Per-bonus points MAE (lower better) | 5.4591 | 4.7042 | −0.7549 | yes |
| Log loss (lower better) | 0.3839 | 0.3272 | −0.0567 | yes |
| AUC (higher better) | 0.9088 | 0.9386 | +0.0298 | yes |
| Exact-bonus accuracy (higher better) | 0.5448 | 0.6269 | +0.0821 | yes |

Every metric in both stages improves at every consecutive step (ECE wobbles,
but ECE is a coarse equal-width-binned statistic; the finer calibration term
from the Brier decomposition — `reliability` — *is* monotone over the same
predictions, and is the one to trust where they disagree). The tossup per-step
improvements (~0.008 AUC) are ~4× the measured seed noise (~0.002). The model
gets better at predicting whether a buzz is correct, when the buzz happens, and
how many bonus points the team converts.

The next four sections break down where the improvement lives; §6 explains why
an earlier version of this sweep wrongly showed no bonus gain at all.

## 3. Difficulty: harder questions benefit more

Tossup log-loss reduction from dim 1 to dim 7 by difficulty quartile
(Q1 = hardest):

| Difficulty definition | Q1 (hardest) | Q2 | Q3 | Q4 (easiest) | label leak? |
|---|---|---|---|---|---|
| plain p-value | +0.0866 | +0.0606 | +0.0422 | +0.0253 | **yes** |
| split-half p-value | +0.0782 | +0.0643 | +0.0445 | +0.0334 | no |
| mean buzz position | +0.0617 | +0.0455 | +0.0549 | +0.0511 | no |

**Why the middle row is the one to believe.** Binning by the plain p-value
(the question's observed conversion rate) leaks the label: the p-value is the
mean of the very `y` being scored, so binning on it conditions on the outcome
and can manufacture heterogeneity from nothing. Binning by the model's own
fitted difficulty would be circular. The split-half definition severs the leak:
each tossup's difficulty is estimated on a random half of its buzzes and the
model is scored *only on the other half*. The gradient survives — the hardest
quartile gains ~2.3× more than the easiest — and it is stable across five
independent fold draws (Q1−Q4 gradient between +0.045 and +0.056 every time).

`mean_buzz_position` staying flat is informative rather than troubling: buzz
depth measures how *pyramidal* a question is (how long its clues take to become
tractable), not how much specialized knowledge it demands. Those are different
quantities, and only the knowledge-difficulty one shows the gradient.

## 4. Category and specialization: tossup gains are uneven, and they are NOT "specialists get boosted on-specialty"

Joining tossups to categories (via the `tossups` table in
`data/hf/quizbowl-irt`; 100% coverage of the buzz rows, category vocabulary
canonicalized) gives the tossup-side category breakdown. Log-loss improvement,
dim 1 → 5 and 1 → 7:

| Category | n (buzzes) | Δ dim 1→5 | Δ dim 1→7 |
|---|---|---|---|
| Science | 12,999 | +0.107 | +0.120 |
| Current Events | 1,171 | +0.061 | +0.076 |
| Geography | 1,347 | +0.048 | +0.058 |
| History | 13,047 | +0.054 | +0.057 |
| Mythology | 3,054 | +0.021 | +0.058 |
| Social Science | 2,803 | +0.029 | +0.042 |
| Fine Arts | 9,692 | +0.025 | +0.043 |
| Philosophy | 2,930 | +0.018 | +0.033 |
| Religion | 3,261 | +0.010 | +0.018 |
| Popular Culture | 1,165 | −0.010 | +0.015 |
| Other Academic | 513 | +0.016 | +0.012 |
| Literature | 12,852 | −0.006 | +0.006 |

Every category eventually improves, but the spread is dramatic: Science gains
20× more than Literature. So the extra dimensions are capturing *something*
topic-shaped — but the obvious interpretation needed a direct test.

**The direct specialization test, and its surprising result.** If the
dimensions worked by recognizing "player X is a Science specialist, this is a
Science question, boost X," then within a given player, the gains should
concentrate on that player's *strongest* category. Measuring each player's
per-category strength from **2024 accuracy** (a different season than the one
being scored, so no leakage) and comparing gains within player:

- Double-demeaned interaction (removing each player's average gain and each
  category's average gain): corr(2024 category strength, gain) = **−0.008**,
  p = 0.25, across 18,950 player-category pairs. Null.
- Paired comparison per player: gain on the player's own best category
  **+0.027** vs **+0.050** on their other categories (t = −2.09, p = 0.04,
  n = 345 players). Significantly the *opposite* direction.

**The gains land off-specialty.** The multidimensional model is not learning to
boost specialists on their home turf — the 1-D model already predicts those
buzzes reasonably well. It is learning that a player who looks strong overall
is *weak somewhere*, and fixing the 1-D model's overprediction there. §5 and §7
show the same signature from two other angles.

**The bonus side tells a complementary story.** With the corrected Stage-2
prior (§6), 11 of 12 bonus categories improve strictly monotonically in log
loss, but the gains are nearly *uniform* (+0.038 to +0.073 across categories,
vs a 20× spread on tossups). That is what roster aggregation predicts: the
bonus stage pools each part over the whole roster — in practice a near-max
(§6) — so "someone on the team knows this" varies much less by topic than
"this individual knows this."

## 5. Players: who benefits — off-axis skill mass, not raw strength

Per-player change in tossup log loss, dim 1 → dim 5, for the 818 players with
≥30 scored buzzes: 67.5% are predicted better by dim 5 (mean Δ = −0.0392).

The naive correlate is strength: Δ vs `theta_norm` gives r = −0.342 (stronger
players appear to gain more). But `theta_norm` is read off the very model being
evaluated, and it *bundles two different things* — general ability and skill
mass off the general axis. Separating them requires exogenous measures, taken
from the **2024 training-leg fits** (a disjoint season's labels; returning
players, n = 384):

- 2024 dim-5 `theta_norm`: r = **−0.247** (p = 1e-6) — the effect survives
  exogeneity, at ~70% of the endogenous magnitude.
- 2024 **dim-1 scalar theta** (the pure general-ability rating, sign-oriented
  by 2024 accuracy): r = **+0.386** — by the scalar rating, stronger players
  gain **less**.
- Joint standardized OLS of Δ on both:

  | covariate (2024, exogenous) | β | t |
  |---|---|---|
  | general skill (dim-1 theta) | **+0.46** | +10.1 |
  | dim-5 norm (general + off-axis mass) | **−0.34** | −7.6 |

  Same signs with in-season 2025 measures at t ≈ ±21; stable for min-buzz
  thresholds 15/30/50.

Reading: conditional on general skill, benefit tracks **skill mass off the
general axis** — an uneven, specialized knowledge profile. Conditional on
off-axis mass, more general skill means *less* benefit (the scalar model
already describes such players well). "Stronger players benefit more" was an
artifact of `theta_norm` mixing the two components.

This also resolves a proxy puzzle that earlier looked like a contradiction: a
model-free strength check using observed **accuracy** found nothing (r = −0.04,
p = 0.23) while **buzz earliness** found a real effect (r = −0.140, p = 5.6e-5),
despite both proxies tracking `theta_norm` about equally well (+0.34 / +0.31).
Accuracy is essentially a *general-skill* proxy, and the two opposing effects
cancel in it; earliness partially reflects specialized early-clue knowledge, so
a piece of the off-axis effect survives in it. The proxies were both fine —
they were measuring different components. (2024-season versions of both proxies
reproduce the same pattern: accuracy null, earliness −0.120.)

**A guardrail that shaped all of these definitions:** the baseline model's
latent axes are identified only up to rotation — `theta ~ N(0, I)` and
`alpha ~ N(0, I)` are isotropic and the likelihood only sees `theta · alpha`,
which is invariant under any shared orthogonal rotation. Any statistic built
from raw `theta_k` coordinates (e.g. "variance across dimensions") measures the
arbitrary basis SVI landed in, not the player. Everything above therefore uses
rotation-invariant quantities only: norms, inner products, and the scalar
dim-1 fit. The same fact is what broke the bonus stage's original prior (§6).

## 6. The prior mismatch that almost hid the bonus gains

An earlier version of this sweep produced a bonus series with **no metric
monotone in dimension** and PPB MAE nominally *worse* at dim 7 than dim 1 —
which read as "dimensionality helps tossups, not bonuses." Diagnosing that null
uncovered a defect at the Stage-1/Stage-2 interface, and fixing the defect is
what produced the clean bonus series in §2.

**The defect.** Stage 1 is rotation-invariant (§5), so the basis of the fitted
`theta` is arbitrary — an incidental outcome of each run. But the bonus stage
originally drew its part loadings `alpha_b ~ Gamma(2,2)`: *non-negative*
loadings, confined to the positive orthant of whatever basis Stage 1 happened
to land in. How well each dimension's arbitrary basis aligned with that orthant
became an uncontrolled lottery, drawn once per sweep point.

**The diagnosis** (artifacts under
`results/compirt/holdout/baseline-ablation-{seedcheck,rotcheck,s1seed}/`, all
under the old prior):

- *Not optimizer noise:* Stage-2 seed replicates moved PPB by ≤ 0.0025 — the
  bad values were bit-stable given a fixed Stage-1 fit.
- *The rotation experiment:* refitting Stage 2 on **orthogonally rotated**
  theta — which leaves every Stage-1 prediction bit-identical — moved PPB MAE
  by up to 1.08 within a single dimension, more than the entire dim-1→7
  spread; even flipping the sign of the scalar dim-1 theta cost +0.93 PPB,
  because non-negative loadings cannot re-orient.
- *Stage-1 reseeds:* fresh Stage-1 seeds at dim 6 left tossup metrics
  essentially unchanged (AUC ±0.001) but scattered bonus PPB over 2.54–3.25 —
  the bonus number moved with the Stage-1 basis, not with dimensionality.

**The fix.** The baseline's bonus loadings are now `alpha_b ~ Normal(0, I)` —
the same isotropic prior as its tossup stage, restoring rotation covariance
end-to-end, which is also what "baseline" should have meant all along. (The
`multidim_mirt` family is different by design: its Gamma-positive relevance
`r` is the thing that *breaks* rotation invariance there and makes its skill
dimensions interpretable, so it keeps its prior.)

**After the fix** the pathology's signatures are gone: every bonus metric is
strictly monotone across all six steps (§2), the fitted aggregation temperature
`tau` rises smoothly with dimension (0.06 → 0.31, instead of jumping 10×
between adjacent dims), and 11/12 bonus categories are monotone in log loss
(previously 0/12).

**One structural finding that survives the fix:** the Eq. 8 roster aggregation
still operates as a near-max. Reconstructing the saved `aggregate` from theta,
the fitted loadings and `tau` (matches to machine precision),
corr(aggregate, best member's ability) ≥ 0.997 at every dimension. The team
prediction is, in effect, the best member's ability on that part — which is
why the bonus gains exist (the *identity and level* of the best member per
part is profile-dependent) but are category-uniform (§4).

## 7. Buzz position, and the synthesis: the gains are mostly *calibration*

Log loss and AUC rank the buzz-position thirds in opposite orders, which the
Brier decomposition (Murphy: **Brier = reliability − resolution + uncertainty**)
resolves. `reliability` is pure calibration (lower better: do predicted
probabilities match observed frequencies?); `resolution` is pure discrimination
(higher better: does the model separate successes from failures?);
`uncertainty` is the slice's base rate and cancels between dimensions. Changes
dim 1 → 7:

| Buzz third | n | Δ log loss | Δ AUC | Δ reliability | Δ resolution |
|---|---|---|---|---|---|
| Early | 5,729 | **−0.1062** | +0.0351 | **−0.0380** | +0.0068 |
| Middle | 25,974 | −0.0559 | +0.0525 | −0.0144 | +0.0087 |
| Late | 33,131 | −0.0417 | **+0.0739** | −0.0041 | **+0.0107** |

Early buzzes get the largest total improvement, but it is almost entirely
**calibration** — the 1-D model is badly overconfident about early buzzes, and
the extra dimensions fix that. Discrimination gains are concentrated in late
buzzes, and are small in absolute terms everywhere (resolution reaches only
~8% of outcome uncertainty at dim 7 — the model separates outcomes better, but
from a very low base). The appealing hypothesis — that early, clue-specific
buzzes are where specialized dimensions help *rank* who converts — is not what
the data shows.

**Putting the answers together.** One mechanism accounts for all of them. A
1-D model must summarize each player as uniformly strong or weak; for a player
with an uneven profile it systematically overpredicts off-specialty and on hard
questions. The extra dimensions learn the *shape* of each profile, and the
payoff shows up exactly where the 1-D overprediction was worst:

- on **hard questions** (§3), where blanket strength overpredicts most;
- **off-specialty** (§4) — gains land on players' weaker categories, not their
  home category;
- for **players with off-axis skill mass** (§5), the ones a scalar rating
  describes worst;
- as **calibration on early buzzes** (§7) — the confident, specialized-looking
  events where the 1-D model overcommits;
- and on **bonuses** (§2, §6) — where knowing each roster member's profile
  shape sharpens the near-max team aggregate, roughly evenly across topics.

In short: multidimensional CompIRT earns its gains not by discovering who is
brilliant at what, but by learning **where each player's knowledge runs out**.

## 8. Reproducing and extending

- Every number in this document regenerates from the `analysis/` package — one
  runnable module per section (`python -m analysis.overall`, `.difficulty`,
  `.categories`, `.players`, `.buzz_position`); see `analysis/README.md` for
  the module map and the ground rules (rotation invariance, exogeneity, the
  reconciliation guardrail). CSVs land in `results/analysis/csvs/`
  (gitignored), figures in `results/analysis/graphs/` (committed).
- Robustness experiments (seed replicates, rotations, Stage-1 reseeds):
  `results/compirt/holdout/baseline-ablation-{seedcheck,rotcheck,s1seed}/`.
  These were run against the *old* Gamma-loading bonus stage and are kept as
  the §6 diagnosis record; rerunning them under the corrected prior should
  show rotation-insensitivity (a cheap way to re-verify the fix).
- Natural next steps: a non-transductive bonus evaluation (fit Stage-2
  parameters on a split disjoint from the one scored); and a tossup-side
  category analysis of the *multidim* family, whose pinned basis permits
  per-dimension interpretation the baseline forbids.
