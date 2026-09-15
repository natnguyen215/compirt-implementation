# Pyro frozen skills

A Bayesian version of the [original frozen-skills model](../docs/frozen-skills.md)
on the same five whole-game holdouts. It models first-buzz timing, first-buzzer
identity, and conditional correctness, keeping the original timing-rate and
correctness-feature equations but replacing the penalized point fits with Pyro
variational inference. Original MAP and DD-Bernstein artifacts are not
overwritten.

The [five-fold comparison](../../results/compirt/holdout/frozen-skills/pyro-cut-vi/REPORT.md)
improves correctness log loss over the original MAP fit but has worse timing
and joint event loss at this budget; both beat the saved DD reference on those
scores. Timing convergence and posterior-draw precision remain open.

The package also holds two follow-ups documented in the model guide: the
[simplified correctness branch](../docs/frozen-skills.md#simplified-correctness-branch)
(`frozen_skills.simplified`) and
[joint MAP fine-tuning](../docs/frozen-skills.md#joint-map-fine-tuning)
(`frozen_skills.joint`).

## Model and inference

The timing equation remains

$$
\lambda_{ij}(x)=\exp(\theta_i^\top\operatorname{softmax}(r_j)+v_i+a_j+
\operatorname{softplus}(b_j)x).
$$

Player skills/speed and relevance logits have independent standard-normal
priors. Question starts have Normal(−2,2²) priors, raw slopes Normal(2,2²),
and terminal log-exposure Normal(−2.3,2²). The original numerical clamps,
normalized ordinary-token exposure, terminal exposure and categorical winner
likelihood are preserved. Correctness does not enter timing fitting.

Correctness retains shared and question-specific cubic position splines,
player/question intercepts, terminal effects, and question-specific weights
on the four standardized timing features. Normal(0,1) priors on coefficients
of the scaled features reproduce the original L2 penalties. A proper
Normal(0,10²) global intercept prior replaces the original unpenalized intercept;
this is the one explicit prior change. See the original guide for full equations.

Let phi denote timing parameters, beta correctness coefficients, D_H timing
observations, and D_C correctness labels. We approximate the **cut posterior**

$$
p_{\rm cut}(\phi,\beta\mid D_H,D_C)
=p(\phi\mid D_H)\,p(\beta\mid D_C,\phi).
$$

This intentionally prevents correctness from feeding back into timing. It is
not the jointly updated posterior p(phi,beta | D_H,D_C). The approximation is

$$
q_{\rm cut}(\phi,\beta)
=\frac1M\sum_{m=1}^M\delta_{\phi^{(m)}}(\phi)q_m(\beta),
\qquad \phi^{(m)}\sim q_H(\phi).
$$

1. Fit the timing posterior q_H with the repository's `AutoNormal`, `Trace_ELBO`,
   `ClippedAdam`, and shared `utils.training.fit_svi` loop. Save aligned draws.
2. Detach M=16 timing draws. For each draw, standardize its player skills/speed
   using correctness-training rows only, with the original SD floor of 0.1.
3. Fit one independent `AutoNormal` correctness posterior q_m for each fixed
   timing draw. These are vectorized in one model using distinct coefficient
   arrays, not one coefficient vector shared across uncertain covariates.
   Each conditional posterior has the full training likelihood and priors.
4. Integrate coefficient uncertainty using 48-point Gauss-Hermite quadrature,
   then average paired timing/correctness probabilities over components.

Because the correctness logit is linear in Gaussian coefficients, its conditional
mean/variance are available exactly under the diagonal guide. Quadrature
integrates its sigmoid. Timing uncertainty is a finite Monte Carlo mixture;
16 draws and mean-field guides are approximations, not exact Bayesian inference.
The code checks 24-versus-48-node quadrature agreement and preserves all draws,
coefficient locations/scales, transforms and ELBO traces for auditing.

For an observed winner/time (i,t), the main conditional incorrect probability is

$$
P(Y=0\mid I=i,\tau=t,D)
\approx\frac{\sum_m P_{\phi^{(m)}}(I=i,\tau=t)
\,E_{q_m}[p^-_{ij}(t/T_j)]}
{\sum_m P_{\phi^{(m)}}(I=i,\tau=t)}.
$$

This conditions the mixture on the observed timing/identity, without using
held-out correctness labels or changing the fitted timing posterior. The saved
`mark_only_neg` column also reports the unweighted mean of the correctness
heads, so the effect of this conditioning is visible. Joint event log loss
uses the paired mixture probabilities, never the average of component losses.

## Holdout protocol

The runner reads the existing DD-Bernstein training/holdout roster CSVs and
checks their game sets against the original frozen study's split manifests.
It verifies disjoint training/test games and identical held-out correctness
IDs/labels. The reference is simplex DD-Bernstein 3/3/2 with learned locations
and terminal intercepts, without player propensity.

The original fold-specific inner-selected spline/skill scales are reused.
There is no new feature search or test-selected stopping, and only the fixed
0.5 threshold is reported. These repeatedly used folds remain development
comparisons. Both stages use 3,000 full-batch SVI steps at learning rate 0.005.
Timing uses seed 42+fold, coefficient fitting 142+fold, and timing posterior
sampling 1042+fold. The earlier point model used different optimizers/budgets;
this comparison does not isolate posterior averaging from fitting changes.

## Run and replay

```bash
PYTHONPATH=archive:. .venv/bin/python -m pytest -q archive/tests/test_frozen_skills.py
.venv/bin/python -m frozen_skills.train_holdout
.venv/bin/python -m frozen_skills.report
.venv/bin/python -m frozen_skills.verify
```

Default output:
[`results/compirt/holdout/frozen-skills/pyro-cut-vi/`](../../results/compirt/holdout/frozen-skills/pyro-cut-vi/).
Completed folds resume. Changing configuration requires a fresh `--output`.
Incomplete folds restart from scratch. To distribute independent folds over
two GPUs, use disjoint `--folds` lists with the same output configuration:

```bash
CUDA_VISIBLE_DEVICES=0 .venv/bin/python -m frozen_skills.train_holdout --folds 0 1 2
CUDA_VISIBLE_DEVICES=1 .venv/bin/python -m frozen_skills.train_holdout --folds 3 4
```

Each fold saves:

| Artifact | Contents |
| --- | --- |
| `original_inner_split.csv`, `holdout_games.csv` | Exact game partitions |
| `feature_config.json` | Reused training-validation-selected feature settings |
| `timing/posterior_draws/`, `posterior_quantiles.*` | Aligned timing draws and marginal uncertainty |
| `timing/guide.pt`, `timing/losses.csv` | Timing SVI state/medians and complete loss trace |
| `correctness/guide.pt` | Separate coefficient posterior locations/scales per timing draw, plus SVI state |
| `correctness/transforms.joblib` | Training spline, ID maps and draw-specific skill normalization |
| `correctness/conditional_mark_probabilities.npy` | Posterior-averaged correctness heads paired with timing draws |
| `events.csv`, `predictions.csv`, `metrics.json` | Full event scores and conditional correctness predictions |
| `checks.json`, `summary.json`, `complete.json` | Freeze/normalization checks, training metadata and completion |

A saved predictor requires no live Pyro parameter store or fitting:

```python
from frozen_skills.predict import FrozenSkillsPredictor

predictor = FrozenSkillsPredictor(
    'results/compirt/holdout/frozen-skills/pyro-cut-vi/fold_0', device='cpu'
)
# rows: one row per active player, with event/game/question IDs, player_id,
# T_j, t_star, relative_position and z (BUZZ/CENSORED/NO-BUZZ).
# The method erases y; correctness outcomes never enter prediction.
events, checks = predictor.predict(rows)
```

Known player/question identities are required, as in the matrix-infill protocol.
The verifier reloads saved artifacts on CPU and checks ordinary, terminal and
dead held-out examples against original predictions, with labels erased. It
also reports sensitivity to using eight versus sixteen timing components on
that verification subset; this is not a full Monte Carlo convergence study.

## Scope

This run evaluates timing, first-buzzer identity, conditional correctness and
joint event probabilities. It does not implement downstream game/leaderboard
or bonus simulation for this family, and is not advertised as compatible with
the generic sigmoid-hazard `holdout/frozen_predict.py` schema. Its own replay
uses the same normalized rate likelihood as its trainer.

The saved DD reference predates the normalized CompIRT training-likelihood
repair; its comparison scores use normalized full-grid replay, not a repaired
refit. A matched multi-seed/budget study remains necessary before attributing
performance differences to Bayesian inference or selecting a paper model.
