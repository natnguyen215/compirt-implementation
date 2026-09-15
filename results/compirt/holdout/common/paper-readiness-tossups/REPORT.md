**Tossup model: publication readiness assessment — 6 September 2026**

_Historical assessment, 2026-09-06. Its §2 issue (unnormalized first-buzz training likelihood) has since been repaired; see [`docs/first-buzz-likelihood.md`](../../../../../docs/first-buzz-likelihood.md). The outputs it describes are in this directory._

The data supports useful tossup prediction. It does not yet establish that the
current model is the best way to extract that signal, or that its most detailed
latent parameters describe identifiable player traits. My priority would be a
coherent first-buzz likelihood, simpler item parameterization, strong baselines,
and an evaluation that separates correctness, timing, and skill transfer.

This assessment focuses on tossups, following the user's clarification. I read
the CompIRT draft, the research log, the local CAIMIRA paper, data-quality and
season analyses, observation construction, lineup inference, frozen splitting
and prediction, Bernstein training, and event evaluation. I also ran new, fixed
specification correctness baselines on all five existing frozen folds. No
CompIRT models were retrained or production model code changed.

**1. A new baseline substantially changes the interpretation of the results.**

I fitted an L2-regularized logistic model with player and question intercepts,
a cubic spline of observed relative buzz position, and a terminal-cell indicator.
Its specification was fixed in advance of this diagnostic: five spline knots,
`C=1`, ordinary unweighted likelihood, and a 0.5 decision threshold. Encoding,
spline knots, and coefficients were fitted using training games only.

The comparison uses the exact saved held-out first buzzes of the simplex
Bernstein 3/3/2 model with learned locations and terminal intercepts: 45,995
buzzes across 2,332 held-out games. I checked held-out correctness labels and
positions against the raw-data reconstruction. Values below are unweighted
five-fold means, matching the main research-log convention.

| Model | Correctness log loss | AUC | Brier | Accuracy |
| --- | ---: | ---: | ---: | ---: |
| Constant training-set correctness rate | 0.54291 | 0.50000 | 0.17873 | 76.70% |
| Position spline + terminal indicator | 0.53870 | 0.55374 | 0.17713 | 76.70% |
| Player + question intercepts + position + terminal | 0.48906 | 0.71474 | 0.15845 | 77.84% |
| Saved simplex DD-Bernstein 3/3/2 | 0.48780 | 0.71547 | 0.15825 | 77.95% |

The selected CompIRT model extracts real signal: its log loss improves about
10.2% relative to the constant predictor. However, the simple additive baseline
captures about 98% of that reduction. CompIRT's incremental advantage is roughly
0.00126 log loss and 0.11 accuracy percentage points. It has better log loss in
four of five folds. This is a small advantage whose robustness needs validation.

A paired bootstrap of the fixed out-of-fold losses illustrates sensitivity to
the sampling unit. The pooled log-loss advantage is 0.001253; separate 2,000-draw
game-cluster and question-cluster percentile intervals are approximately
[0.000067, 0.002625] and [-0.000086, 0.002628]. These are exploratory conditional
intervals, not a full inferential analysis: neither jointly accounts for crossed
game/question dependence, refitting, optimizer variation, or prior model selection.

This baseline predicts correctness **given the observed buzzer and position**.
It does not predict who buzzes, when they buzz, or whether anyone buzzes. Thus it
does not replace CompIRT's survival component. It does mean that correctness
alone currently makes a weak case for the additional latent structure. The
3/3/0.67 arm's logged correctness loss is 0.4873, also close to this baseline;
that arm was not included in the fresh paired comparison.

Sources: [new fold results](../../../../../results/compirt/holdout/common/paper-readiness-tossups/correctness_baselines.csv),
[uncertainty diagnostic](../../../../../results/compirt/holdout/common/paper-readiness-tossups/baseline_uncertainty.json),
[research log](../../../../../RESEARCH_LOG.md).

**2. The highest-priority model issue is the first-buzz probability law.**

The Bernstein training likelihood multiplies survival before the observed token
by the winning player's sigmoid hazard at that token. Conditional on survival
to a token, it effectively assigns each exclusive winner outcome weight $h_i$,
while assigning no event probability $\prod_i (1-h_i)$.

Those weights generally do not sum to one. With two players and one token,
$h_1=h_2=0.5$, the two winner outcomes plus no buzz sum to
$0.5 + 0.5 + 0.25 = 1.25$. Summing over correctness marks does not fix this.
The paper's Equation 7 inherits this discrete-time problem. It resembles a
continuous-time competing-risk expression, but sigmoid probabilities on finite
token cells require an explicit treatment of competing events within a cell.

The current evaluator does construct a normalized distribution. It uses
$H=1-\prod_i(1-h_i)$ for any buzz and allocates $H$ between players in proportion
to their unique-buzzer weights, with a numerical fallback. Away from the fallback,
this allocation is proportional to the odds $h_i/(1-h_i)$. Consequently, the
normalized event score used in the research log is a legitimate score for that
reconstructed distribution, but the training objective fits a different rule.
This does **not** establish that existing model rankings will reverse after a fix.

Using saved row hazards from all five simplex 3/3/2 folds, the normalized event
factor versus the training-form factor changes observed-buzz negative log loss
by about 0.05 nats on average; at terminal buzzes, the difference is about
0.85–0.90 nats. This is material relative to many reported model improvements.
These differences compare formulas on the same saved hazards, not refitted models.

I would choose one normalized categorical event law and use it consistently in
training, scoring, simulation, and recovery. A minimal repair is to train against
the evaluator's current event law. Another coherent option uses within-cell
rates:

$$
\lambda_i(t)=\exp\bigl(\eta_i(t)\bigr),
\qquad
\Lambda(t)=\sum_i\lambda_i(t).
$$

Conditional on no earlier buzz, the probabilities in the current cell are:

$$
\begin{aligned}
P(\text{no buzz at }t\mid\text{survived})
&=e^{-\Delta_t\Lambda(t)}, \\
P(i\text{ wins at }t\mid\text{survived})
&=\frac{\lambda_i(t)}{\Lambda(t)}
  \left(1-e^{-\Delta_t\Lambda(t)}\right).
\end{aligned}
$$

Here $\Delta_t$ represents exposure duration. Ordinary words can initially share
one duration and the final response window can have a separate duration. Without
measured reading times, these remain relative exposure parameters requiring a
scale convention. A multinomial model including a no-event category is another
standard discrete-time option; see
[Heyard et al.](https://onlinelibrary.wiley.com/doi/full/10.1002/bimj.201800293).

Required checks are finite-grid total probability, an observed event's equality
between training and replay, final-cell survival, variable roster sizes, and
recovery from independently simulated normalized races. Simply adding losers'
same-token survival factors would model exactly one latent buzzer but leave
multiple-buzzer outcomes unaccounted for unless a tie rule is also specified.

Sources: [training likelihood](../../../../../hazard_double_difficulty/bernstein/pyramidal_model.py),
[normalized evaluation](../../../../../compirt_eval/scenario_a_tossups/reconstruction.py),
[formula audit](../../../../../results/compirt/holdout/common/paper-readiness-tossups/likelihood_audit.json).

**3. Simplify the difficulty curves without discarding multidimensional skill.**

For either branch of full Bernstein,

$$
\begin{aligned}
z_{ij}(x)
&=\sum_k r_{jk}\theta_{ik}
  -\sum_k r_{jk}\sum_m q_{jkm}B_m(x) \\
&=r_j^\top\theta_i-\sum_m \widetilde{q}_{jm}B_m(x), \\
\widetilde{q}_{jm}
&=\sum_k r_{jk}q_{jkm}.
\end{aligned}
$$

The difficulty curves share the same Bernstein basis and the relevance weights
do not vary with position. Therefore only their weighted sum enters the
likelihood. Individual per-dimension curves cannot be identified separately
from these observations, even with arbitrarily many repetitions. Positive
weights preserve monotonicity of the collapsed curve. Priors can regularize a
particular decomposition, but do not make it empirically unique.

My proposed default is one scalar difficulty curve per branch, retaining
separate correctness and hazard loading vectors. With degree 3 and three skills,
this represents the same branch-wise predictor functions using 14 item
coordinates under positive free loadings, versus the current nominal 30;
simplex loadings give 12 versus 28. This is an equivalence of likelihood
representations, not of prior distributions. A controlled refit must examine
the induced prior on the effective curve.

A further modeling consequence: separate difficulty curves for each dimension
do not, by themselves, let later clues change which skills distinguish players.
That requires time-varying relevance or player-by-clue interactions. Such
structure should be heavily pooled and tested only after the simpler model works.

Source: [Bernstein definition](../../../../../hazard_double_difficulty/bernstein/pyramidal_model.py).

**4. The data is informative, but sparse for the current parameter ambitions.**

The fresh 2024 audit found 2,431 games, 1,296 listed tossups, 58,020 recorded
buzzes, and 47,914 first buzzes before holdout coverage filtering. Among players
with a first buzz, the median is 23; 602 of 1,410 have fewer than 20. Among
questions with a first buzz, the median is 37 first buzzes and seven incorrect
first answers. Four-fold training supplies less evidence than these full-year
counts. These are not counts of independent correctness labels for each
rostered player: censored player rows carry survival information, not unseen
correctness outcomes.

This supports pooled skill, item difficulty, and timing prediction. It gives
much less support to rich player-by-category correctness effects, separate
per-player perception vectors for three position slices, or detailed item
curves with weak sharing. Their failure is not evidence that the whole dataset
is useless. Nor does AUC around 0.72 establish a Bayes ceiling.

The season EDA supports asymmetric complexity. Category timing specialties
repeat across season halves at approximately $r=0.387$, whereas category
correctness specialties repeat at $r=0.009$ under the stated sample-size filter.
These are descriptive residual correlations, not definitive latent-trait tests.
They motivate richer skill structure in timing and stronger shrinkage in
correctness. Likewise, boundary buzzing is enriched 3.65-fold relative to
uniform token opportunity. This could reflect pauses, comprehension, recording
heaping, or all three; it is not evidence for purely semantic difficulty jumps.

There are three concrete data cautions:

- **Risk sets depend on held-out behavior.** Lineups for larger registered rosters
  are inferred from buzzes across the game, including evaluated and later buzzes.
  In 2024, 1,001 of 4,862 game-team entries have registered rosters larger than
  four. There are 466 segments where only one to three observed buzzers are
  treated as the lineup. Silent active players can be omitted. A retrospective
  analysis conditional on reconstructed lineups must say so; prospective winner
  prediction should use independently known lineups or a roster-uncertainty model.
  Start with a sensitivity analysis restricted to games where both registered
  rosters have at most four players; this reduces, but does not eliminate,
  uncertainty about actual participation.
- **The endpoint is a different observation regime.** Value-zero incorrect
  attempts, post-reading delays, and no-buzz outcomes need distinct semantics.
  Do not remove valid incorrect terminal attempts just to improve calibration.
  Report mid-question and terminal behavior separately and audit a sample of
  original records. Broad final-decile calibration can hide a misplaced
  within-decile spike.
- **Coverage differs across sources.** The 2024 slice lacks 336 tossup category
  labels. The 2024–25 season has complete category labels, but overlaps 2024;
  it is not an independent replication. Current local tables also contain 2023
  and later 2025 tossup sets beyond the older documentation. Eligibility,
  provenance, annotation quality, and prior use must be checked before choosing
  a final test panel. Exact-slug identity linking needs an alias/collision audit.

The coverage pass moves 99 of 2,431 originally assigned test games into training
across the five folds. The reported evaluation is consequently a known-player,
known-item population, which is a valid matrix-infill target when stated clearly.
It does not establish cold-start or future-question performance.

Sources: [fresh data audit](../../../../../results/compirt/holdout/common/paper-readiness-tossups/data_audit.json),
[season EDA](../../../../../analysis/season_2024_25_eda/EDA_REPORT.md),
[lineup rules](../../../../../lineup.py), [fold coverage](../../../../../holdout/game_splits.py),
[label sensitivity analysis](../../../../../archive/analysis/buzz_accuracy_timing/report.md).

**5. The model changes I would prioritize after the probability repair.**

Keep separate correctness and timing branches, learned population curve
locations, and an explicit terminal window. Start with a scalar correctness
ability and a small, partially pooled category or latent-skill representation
for timing. Compare shared versus separate skill projections instead of forcing
the same correctness logit to explain when a player buzzes. The perceived-model
experiments already show that this coupling can severely damage correctness.

Next add a small number of shared hazard features: clue boundary, within-clue
position, question length, and a short reaction-lag basis. A global effect or a
hierarchically pooled category effect uses far more evidence than a new parameter
for every player and item. Avoid initially adding free player-specific jumps.
The ordinary knowledge curve can remain monotone while the hazard has boundary
effects and changes in exposure.

For a stronger content contribution, predict curve starts, drops, and relevance
from text or metadata, with shrunk item residuals. Evaluate whether this helps
sparsely observed questions before claiming unseen-question generalization.
The local CAIMIRA paper provides a relevant content-conditioned item approach;
the existing TF-IDF variant uses accumulated lexical rarity, which is not
necessarily clue diagnosticity. For an online information condition, features
must respect what is revealed at the prediction time. Whole-question text can
be legitimate for an analyst with a known packet, but that is a different task.

Game-state effects are a later, bounded addition: pre-event score margin,
questions remaining, and opponent strength may explain risk-taking. The raw
tables have score fields, but confirm their update timing before using them.
Incremental QA explicitly separates answering, confidence, and sequential
decision-making in [Rodriguez et al.](https://arxiv.org/abs/1904.04792).

Bouncebacks are a potentially useful source of additional observations. The
2024 raw data has 10,106 recorded buzzes beyond the first buzz per game-question;
that is an upper bound on usable continuation events, not a count of validated
bouncebacks. Audit ordering, tied recorded positions, lockout, and zero-value
endpoints before adding an opponent-only continuation likelihood. Keep phase-0
evaluation identical across arms.

I would pause new perception-slice, polynomial-degree, and incorrect-class-weight
sweeps. The log shows that loss weighting mostly changes calibration and the
decision threshold, not discrimination. Additional optimization steps may be
needed, but stopping should use training-internal validation and a documented
checkpoint policy, not the held-out scores.

**6. A small experiment program can distinguish data limits from model limits.**

| Experiment | Design | What the result would resolve |
| --- | --- | --- |
| Probability repair | Same folds and parameters; old fit objective versus normalized event objective; at least three optimization seeds | Whether current timing/identity errors partly come from the likelihood mismatch |
| Representation ablation | Scalar branch curves; shared versus separate loadings; matched priors where possible | Whether extra item coordinates add usable prediction or mostly redundant estimation |
| Strong baselines | Current correctness baseline; normalized race with player effects, item effects, global position spline, terminal window; small category-skill extension | Whether CompIRT improves on ordinary partial pooling for the full event |
| Coverage learning curves | Fixed scoring panel; nested subsets of whole training games at 20/40/60/80/100%; maintain a common supported population | Continued improvement indicates that more comparable observations would help; flattening alone does not prove irreducible noise |
| Real-design recovery | Simulate normalized races on actual question lengths, rosters, item exposure and player overlap; multiple seeds and sample sizes | If true-model recovery fails, current design/estimation cannot support those parameters; if it succeeds but real-data fit fails, misspecification becomes more plausible |
| Targeted residual additions | Add boundary/lag features, then text pooling, one at a time | Improvement identifies missing explanatory features rather than a generic need for more dimensions |
| Roster and quality sensitivity | Small registered-roster games, terminal versus nonterminal cells, high- versus low-exposure players/items | Whether headline gains depend on uncertain observation construction or a narrow data regime |
| Skill-transfer validation | Later outcomes or independent calibration population with player estimates frozen; compare training-only empirical/category player summaries | Whether the fitted skill representation has predictive value beyond same-item interpolation |

Recovery should score effective curves, skill projections, first-buzz
distributions, ranking uncertainty, and coverage. Do not demand recovery of
unidentifiable per-dimension difficulty decompositions. Run both well-specified
and deliberately misspecified simulations; simulating and fitting the same
implementation alone can reproduce the same error in both places.

The data-collection decision should follow these results. If learning curves
keep improving, add repeated observations that strengthen sparse player/item
connections. If missing clue features explain residuals, improve annotations and
content sharing. If verified lineups or accurate timestamps change the result,
prioritize those measurements. If the remaining target is an individual's
private wrong guess or unobserved recognition state, more identical logs may
not reveal it; prospective response/recognition annotations would be needed.

**7. What would make a tossup paper defensible.**

The central claim should be prediction of a first-buzz marked event and useful
player-skill estimation from censored incremental responses. Treat correctness
conditional on an observed buzz as one diagnostic, not the whole task.

Use a normalized joint event log score as the primary measure, accompanied by
correctness log loss/Brier, first-buzzer log loss and top-1 accuracy, event-time
Brier and conditional timing error, and separate no-buzz/terminal calibration.
Decompose losses so improved correctness cannot conceal degraded player ordering.
Validate player rankings against later held-out performance, not the same buzzes
used to estimate them. Integrate posterior draws for predictive probabilities
and ranking intervals; mean-field guide intervals need calibration checks.

Retain matrix infill as one explicitly named task. Add either an independent
calibrated-item response holdout for player-skill transfer or a strict
question/packet holdout with a trained cold-start item rule, depending on the
paper's intended claim. Never fit question parameters to the responses being
scored and call that predictive holdout. For unseen-question claims, hold every
mirror play of a question out together. For future-event claims, also enforce
the chronological information boundary on player parameters and lineups.

Choose a small finalist set in development, use matched conventions, and reserve
an outer evaluation from further selection. The existing grid and repeated
research-log comparisons make these folds development data. Selection bias can
be as large as apparent between-model improvements, as demonstrated by
[Cawley and Talbot](https://www.jmlr.org/papers/v11/cawley10a.html). Report paired
uncertainty using sampling units appropriate to crossed game and question
dependence, and report optimization-seed variation separately. Five folds are
not five independent replications of the optimizer.

The draft must match the implemented tossup method: SVI rather than its current
NUTS claim; the actual selected difficulty family and priors; the normalized
event law and terminal survival convention; actual data coverage; and inferred
risk sets. Its original Gaussian sigmoid amplitude does not guarantee decreasing
difficulty when the amplitude is negative. Explain any monotonicity constraints
actually used. Avoid describing a fitted confidence parameter as a validated
psychological trait without external or recovery evidence.

The strongest plausible outcome is a well-validated, relatively small model
whose value lies in censored incremental performance and transferable skills.
High correctness accuracy is neither required nor sufficient. Current evidence
does not justify declaring the data exhausted, and it also does not justify
expecting another layer of latent parameters to solve the remaining errors.

**Reproducing the new diagnostics.**

Run from the repository root:

```bash
PYTHONPATH=. .venv/bin/python analysis/correctness/paper_readiness/audit_data.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=. \
  .venv/bin/python analysis/correctness/paper_readiness/run_correctness_baselines.py
PYTHONPATH=. .venv/bin/python analysis/correctness/paper_readiness/bootstrap_baselines.py
```

These scripts write only to
`results/compirt/holdout/common/paper-readiness-tossups/`. The baseline consumes
the saved simplex 3/3/2 held-out predictions and the current local 2024 tables;
it checks alignment before fitting. The audit is descriptive and depends on
the current generated tables and lineup cache. All reported new results are
exploratory diagnostics on an already studied evaluation panel.
