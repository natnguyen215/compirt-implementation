# Frozen timing skills and correctness

`frozen_skills` is a two-stage predictive model: learn player features from
first-buzz timing, then hold them fixed while fitting correctness. The timing
model is trained from scratch; it is not a frozen copy of saved DD-Bernstein.

This document covers the original penalized point-fit model and two follow-up
experiments built on it: a [simplified correctness branch](#simplified-correctness-branch)
and [joint MAP fine-tuning](#joint-map-fine-tuning). The
[Pyro adaptation](../frozen_skills/README.md) retains the original equations and
fits a timing posterior plus conditional correctness posteriors. See the
[research log](frozen-skills-results.md#frozen-skills-model-and-measured-results) for
its place among the other experiments.

## Timing model

For player i, question j, relative token position x=t/T_j, and active roster R,

$$
\lambda_{ij}(x)=\exp\{\theta_i^\top\rho_j+v_i+a_j+k_jx\},
\qquad \rho_j=\operatorname{softmax}(r_j),
\qquad k_j=\operatorname{softplus}(b_j)>0.
$$

| Parameter | Meaning |
| --- | --- |
| Three-vector `theta_i` | Player's timing-derived latent skills |
| Scalar `v_i` (`speed`) | Player's overall buzz speed |
| Three-vector `r_j` (`relevance`) | Question logits whose softmax gives nonnegative skill weights summing to one |
| Scalar `a_j` (`start`) | Question's starting log-rate |
| Scalar `b_j` (`slope`) | Unconstrained parameter transformed into a positive log-rate slope |
| Global scalar `e` (`end`) | Log exposure of the final cell |

Holding the player terms fixed, increasing a_j multiplies buzz rates throughout
the question. Increasing k_j makes rates grow faster as the question is read.
For example, k_j=2 makes the end rate e²≈7.4 times the rate at x=0, before
accounting for terminal exposure. x=0 is the conceptual start; the first scored
cell is x=1/T_j. A rate is not a probability.

The implementation clips the base log-rate `theta_i @ rho_j + v_i + a_j` to
[−15,12] and caps the transformed slope at 15 for numerical stability. Every
player on a question shares the same position slope, so their rate ratios and
conditional winner ordering are constant across position. The model cannot
represent one player overtaking another as particular clues are revealed.

### Cell probabilities and likelihood

Ordinary token cells have exposure Δ_jt=1/T_j; the final cell has exposure
Δ_jT=exp(e), representing the end-of-question/post-reading window. Define

$$
A_{jt}=\Delta_{jt}\sum_{i\in R}\lambda_{ij}(t/T_j),
\qquad S_j(t)=\exp\left(-\sum_{s<t}A_{js}\right).
$$

Conditional on survival to a cell, the no-buzz probability is exp(−A_jt),
and the any-buzz probability is 1−exp(−A_jt). Allocate the latter among the
roster in proportion to their rates:

$$
P(\text{first buzzer}=i,\text{ token}=t)
=S_j(t)[1-\exp(-A_{jt})]
\frac{\lambda_{ij}(t/T_j)}{\sum_{u\in R}\lambda_{uj}(t/T_j)}.
$$

The no-buzz outcome has probability exp(−Σ_{t=1}^{T_j} A_jt), including the
terminal cell. These player/token probabilities plus no-buzz mass sum to one.
An observed buzz contributes survival before its token, any-buzz probability
at that token and winner attribution. Other roster members participate in the
race; they are not independent extra winner observations. A dead question
contributes survival through the end. Correctness labels never enter this fit.

Because rates grow geometrically across ordinary tokens, the training code
computes cumulative exposure with a geometric-series formula rather than
walking every token. Full-distribution evaluation expands the same cell law.

### Fitting and penalties

The minimized objective is `(sum of event negative log likelihoods + penalty)
/ number of training events`. The quadratic penalty is equivalent, up to
constants, to these independent Gaussian penalties on the raw parameters:

| Raw parameter | Center | Standard deviation |
| --- | ---: | ---: |
| `theta`, `speed`, `relevance` | 0 | 1 |
| `start` | −2 | 2 |
| `slope` before softplus | 2 | 2 |
| `end` before exponential | −2.3 | 2 |

This is a penalized point fit, not variational posterior inference. Initialization
uses `theta ~ N(0,0.1²)`, `relevance ~ N(0,0.3²)`, speed 0, start −2,
raw slope 2 and end −2.3. Training uses CUDA, 800 full-batch Adam steps,
learning rate 0.025, seed `42 + fold`, and gradient norm clipping at 10.
It checks finite losses but has no timing-validation early stopping or
convergence-based stopping criterion.

Implementation: [`TimingModel`, `fit_timing`](../../analysis/correctness/tossup_accuracy_study/models.py).

## Correctness model

Extract four player features `s_i = [theta_i1, theta_i2, theta_i3, speed_i]`.
For each feature, compute the mean and standard deviation over the observed-buzz
**correctness training rows**, so players are weighted by their training-buzz
frequency. Standardize with the standard deviation floored at 0.1. Evaluation
uses those same training statistics. The resulting features are fixed inputs;
correctness loss cannot update timing parameters.

With x the observed relative position, E=1[t=T_j], and B_l cubic-spline basis
functions, the selected correctness design is

$$
\begin{aligned}
\eta_{ij}(x)={}&\beta_0+u_i+q_j
+\sum_l\beta_l B_l(x)+\beta_E E\\
&+\sum_l\gamma_{jl}B_l(x)+\gamma_{jE}E
+w_j^\top\widetilde{s}_i,\\
P(\text{incorrect}\mid i,j,x)={}&\sigma(\eta_{ij}(x)).
\end{aligned}
$$

The spline transformer has five knots, degree 3 and `include_bias=False`.
Player/question effects use one-hot encodings. Every question learns its own
spline deviations, terminal effect and four skill coefficients. The correctness
curves and skill coefficients are unconstrained: conditional correctness need
not be monotone in position. They are predictive coefficients, not automatically
interpretable CompIRT ability or difficulty parameters.

Fitting uses ordinary unweighted logistic likelihood with L2 regularization:
`LogisticRegression(C=1, solver='lbfgs', max_iter=2000, tol=1e-6)`.
Reaching the iteration limit raises an error. Incorrect includes every incorrect
first buzz, including zero-point errors. `predict_proba(frame)[:, 1]` is
**P(incorrect)**; correctness probability is its complement.

Feature scales control effective shrinkage under the fixed L2 penalty. The
inner grid compares player/item/local scales, linear versus spline question
curves, and optional clue effects. All five selected base configurations use
player/item scale 1 and question-local spline/terminal scale 3. Frozen skills
inherits that selected base and compares skill-feature scales 0.25, 0.5 and 1.
These scales are regularization choices, not additional fitted timing skills.
The `regularized` family omits only the final skill-interaction term.

Implementation: [`linear_features`, `fit_linear`](../../analysis/correctness/tossup_accuracy_study/models.py),
[serializable predictor](../../analysis/correctness/tossup_accuracy_study/predictor.py).

## Splits and what is frozen

Each outer fold withholds whole games using `year_2024`, five folds and split
seed 42. Inside its training games, `GroupShuffleSplit(test_size=0.2,
random_state=20260908 + fold)` defines fit and validation partitions, including
games with dead questions.

1. Select the regularized correctness configuration by inner-validation
   incorrect-buzz average precision (AP).
2. Fit an **inner timing model** using only the inner fit games. Its features
   select the skill scale by validation AP and the threshold policies by their
   stated validation objectives.
3. Fit an **outer timing model** on all outer training games and refit the
   selected correctness design using its features. This outer model is trained
   independently with the same fold-specific seed, not updated using holdout data.
4. Apply the refitted predictor and saved validation thresholds to outer held-out
   games. The timing comparison replays the outer checkpoint on those rosters.

Both timing states are saved in `timing_skills.pt` with player/item maps.
Only `outer` belongs in the final fold evaluation. Validation labels affect
correctness selection, but never timing loss. No outer outcomes tune models
or thresholds in these runners. Repeated research on these same folds still
means the overall experiment sequence needs independent confirmation.

“Frozen” is distinct from the general frozen-parameter holdout protocol:
DD-Bernstein also freezes parameters during evaluation, but jointly learned its
skills through correctness and timing. Here the freeze occurs **between the two
training stages**.

Runner: [`run.py`](../../analysis/correctness/tossup_accuracy_study/run.py).

## Evaluation and results

The September 7 replay compares all five outer timing checkpoints with saved
DD-Bernstein **3/3/2, simplex relevance, learned locations and terminal
intercepts**, without player propensity. The common population is 46,640 race
events: 45,995 buzzes and 645 dead questions. The reference path is
[`dd-bernstein-332-simplex-locations-terminal/`](../../results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/).

Frozen improves position MAE **0.15186 → 0.14307**, integrated timing Brier
**0.10170 → 0.09477**, first-buzzer accuracy **35.16% → 39.67%**, and full
marked-event log loss **6.61553 → 6.37347**. The timing improvements hold in all
five folds. At correctness threshold 0.5, accuracy improves **77.95% → 78.76%**,
neg F1 **23.20% → 41.38%**, AP **44.93% → 50.20%**, and correctness log loss
**0.48777 → 0.48117**. Neg precision falls **61.55% → 57.95%**.

Position errors use the conditional expected relative position on buzz events;
first-buzzer metrics integrate over possible buzz times. The integrated Brier
score evaluates cumulative buzz probabilities on 21 equally spaced points
from 0 to 1, including dead questions. Exact-token timing log loss includes
no-buzz; race log loss adds identity; joint log loss adds correctness at the
observed player/token. This is evaluation of a normalized event distribution,
not full-game simulation.

The [complete report](../../results/compirt/holdout/common/tossup-accuracy-study/timing_comparison/REPORT.md)
contains pooled and fold metrics, per-event scores, paired game-bootstrap
intervals and verification. Every replay PMF normalizes; 2,665 independent
checks agree with the actual timing training loss to within 1.20e-5; DD expected
positions agree with its saved outputs to within 4.69e-6. The 95% game-bootstrap
interval for frozen minus saved MAE is [−0.00935, −0.00822], conditional on
fixed fits and excluding cross-game question dependence.

These results support this complete model against this saved reference, not an
isolated advantage of exponential over Bernstein curves. Curve shape,
regularization, fitting budget, normalized cell law and coupling all differ.
The saved DD parameters predate the [normalized CompIRT likelihood
repair](../../docs/first-buzz-likelihood.md); replay does not retrain them. Historical
joint-loss numbers around 6.6123 use different evaluation conventions from this
full-grid comparison.

The comparison changes the correctness specification as well as the timing
model, so it does not attribute correctness gains to timing-derived features
alone. Frozen does not beat every historical timing configuration. Its no-buzz
Brier improves, but aggregate predicted no-buzz prevalence is 1.63%, farther
from the observed 1.38% than saved DD's 1.48%. Neither future-season transfer,
unseen-item performance nor interpretable skill recovery is established.

## Reproduction and artifacts

From the repository root, with the existing environment and dataset:

```bash
# Fit retained spline/frozen candidates; requires CUDA and resumes completed folds.
.venv/bin/python -m analysis.correctness.tossup_accuracy_study.run
# Deterministically refit/export selected correctness predictors and verify them.
.venv/bin/python -m analysis.correctness.tossup_accuracy_study.export
# Replay saved timing checkpoints on CPU; no model fitting.
.venv/bin/python -m analysis.correctness.tossup_accuracy_study.evaluate_timing
# Summarize timing/correctness, verify DD saved positions, and bootstrap by game.
.venv/bin/python -m analysis.correctness.tossup_accuracy_study.report_timing
```

The runner skips completed folds; rerunning it is not a fresh experiment. The
exporter refits the selected correctness model on the original training games,
then checks its exported probabilities against saved predictions within 1e-9.

Artifacts under
[`results/compirt/holdout/common/tossup-accuracy-study/`](../../results/compirt/holdout/common/tossup-accuracy-study/):

| Artifact | Contents |
| --- | --- |
| `fold_N/inner_split.csv` | Exact inner fit/validation game partition |
| `fold_N/candidates.json`, `selection.json` | Candidate scores, selected feature scales and thresholds |
| `fold_N/timing_skills.pt` | Inner/outer timing states and player/item ID maps |
| `fold_N/frozen_skills.joblib` | Correctness predictor, frozen player features, training transforms and threshold policies |
| `fold_N/predictions.csv` | Saved outer correctness probabilities and labels |
| `summary.csv`, `fold_metrics.csv`, `export_checks.json` | Correctness scores and export reproduction |
| `timing_comparison/` | Full timing report, pooled/fold/per-event scores, bootstrap and replay checks |

Example using an exported fold predictor:

```python
import joblib

artifact = joblib.load(
    'results/compirt/holdout/common/tossup-accuracy-study/fold_0/frozen_skills.joblib'
)
# frame has player_id, tossup_id, relative_position (t / T), terminal (int(t == T)).
p_incorrect = artifact['predictor'].predict_proba(frame)[:, 1]
predicted_incorrect = p_incorrect >= artifact['thresholds']['default']
```

Unseen player/question one-hot levels are ignored and an unknown player's raw
skill vector falls back to zeros; this makes prediction defined but does not
establish cold-start accuracy. The five exported artifacts are evaluation-fold
models, not a production model fitted on all games.

## Simplified correctness branch

Question: can the original spline correctness expansion be replaced by one
familiar IRT-style equation while keeping the timing model? Freeze the original
MAP timing checkpoint's player features $\hat s_i=(\hat\theta_i,\hat v_i)$ and fit

$$
P(Y_{ij}=1\mid i,j,x)=\sigma\!\left(u_i+w_j^\top\hat s_i-d_j(x)+e_C\mathbf 1[x=1]\right),
$$

where $u_i$ is extra player correctness ability, $w_j$ are unconstrained
question weights on the frozen traits, $d_j$ is one scalar cubic
[monotone Bernstein curve](../../docs/double-difficulty-bernstein.md#monotone-bernstein-curves)
per question, and $e_C$ is a shared terminal-cell adjustment. Priors are
$u_i,w_{jk},b^C_j\sim\mathcal N(0,1)$, $\log D_j\sim\mathcal N(0,0.5^2)$,
$\pi_j\sim\operatorname{Dirichlet}(2,2,2)$, $e_C\sim\mathcal N(0,2^2)$. Stage two
is Bayesian inference conditional on the fixed timing estimate, fit with
`AutoNormal` SVI (3,000 steps, learning rate 0.005, seed 42 + fold); it does not
propagate timing uncertainty. The ordered curve assumes correctness rises with
position, a substantive restriction relative to the flexible spline.

```bash
.venv/bin/python -m frozen_skills.simplified
```

The runner saves the conditional posterior, one median parameter set,
predictions, loss traces, game manifests and checks; `model.pt` loads with
`torch.load(..., weights_only=False)` and predicts via
`frozen_skills.simplified.predict(frame, artifact)`.

Timing predictions are identical to the original MAP fit, but correctness and
joint event loss are worse, so the smaller branch is not a replacement.
Constraints, priors and fitting all changed, so this does not show Bernstein
itself is worse. Numbers are in the
[research log](frozen-skills-results.md#tested-simplification-one-frozen-fit-and-one-correctness-model);
the full report is
[`simplified-bernstein-map-timing`](../../results/compirt/holdout/frozen-skills/simplified-bernstein-map-timing/REPORT.md).

## Joint MAP fine-tuning

Question: should correctness update the shared player traits? Both arms start
from the saved original timing parameters and logistic coefficients (saved
predictions are reproduced first) and run 1,000 full-batch Adam steps at
learning rate 0.005 on

$$
\mathcal L(\phi,\beta)=-\log p(D_H\mid\phi)-\log p(D_C\mid\beta,\tilde s(\phi))
+R_H(\phi)+\tfrac12\lVert\beta_{\mathrm{penalized}}\rVert^2,
$$

divided by training race count, with the original timing penalty and L2
penalty (global correctness intercept unpenalized). The **joint arm**
differentiates both likelihoods with respect to theta and speed. The
**blocked-gradient control** detaches the traits before the correctness
calculation, so timing learns only from timing observations while correctness
follows the moving traits. Training-row standardization
$\tilde s_i=(s_i-\mu)/\max(\sigma,0.1)$ is recomputed each step (with gradients
only in the joint arm). No held-out outcome enters optimization or stopping.

```bash
.venv/bin/python -m frozen_skills.joint
```

Each arm saves `model.joblib`, `events.csv`, `losses.csv`, `summary.json` and
`checks.json`; `frozen_skills.joint.predict_saved(frame, artifact)` predicts
without reading outcomes.

Joint fine-tuning retains almost all original performance but does not beat
the matched control. This is a warm-started experiment and says nothing about
joint training from scratch. Numbers are in the
[research log](frozen-skills-results.md#frozen-skills-model-and-measured-results); the
full report is
[`joint-map-spline`](../../results/compirt/holdout/frozen-skills/joint-map-spline/REPORT.md).
