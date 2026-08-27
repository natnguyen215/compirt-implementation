# CompIRT research log

_Last reviewed: 2026-08-26._

## 1. Scope and evaluation protocol

This log reports Stage-1 tossup results from frozen matrix-infill holdouts. For
each five-fold split, the model trains on four whole-game folds. Saved player
and question posterior medians are replayed on the fifth fold by
`holdout/frozen_predict.py`; held-out outcomes do not update parameters. A run
is included only when its holdout `summary.json` records `frozen_predict: true`.

Unless noted otherwise, the results use `year_2024`, game-split seed 42,
optimization seed 42, 3,000 training steps, and no bouncebacks. The five held-out
folds contain 46,640 player-question events in total. Summary values below are
unweighted means of the five fold-level `evaluation/csvs/tossup_metrics.csv`
rows, so minor differences from pooled reports are expected.

The evaluation population has the following reference rates:

- 76.70% of observed buzzes are correct. This is the accuracy of an
  always-correct classifier.
- 1.38% of player-question events end with no buzz.
- 17.56% of all events, or 17.80% of buzzes, occur in the final question decile.

Results from other evaluation protocols, including in-sample fits and Stage-2
bonus models, are excluded.

Model equations are documented in
[`docs/compirt_deep_dive.md`](docs/compirt_deep_dive.md), and reproducible
commands are in
[`docs/compirt-experiments.md`](docs/compirt-experiments.md).

## 2. Model reference

Let `i` index players, `j` tossups, `t` tokens, and `x = t/T_j`:

$$
P(\mathrm{correct}\mid\mathrm{buzz})=\sigma(z^C_{ijt}),
\qquad
h_{ijt}=P(\mathrm{buzz\ at\ }t\mid\mathrm{survival\ to\ }t)=\sigma(z^H_{ijt}).
$$

The single-curve baseline uses

$$
z^C_{ijt}=\sum_k r_{jk}[\theta_{ik}-d_{jk}(x)],
\qquad z^H_{ijt}=z^C_{ijt}-c_i.
$$

Double difficulty (DD) separates correctness and timing while sharing player
skill `theta_i` and confidence `c_i`:

$$
z^C_{ijt}=\sum_k r^C_{jk}[\theta_{ik}-d^C_{jk}(x)],
\qquad
z^H_{ijt}=\sum_k r^H_{jk}[\theta_{ik}-d^H_{jk}(x)]-c_i.
$$

### 2.1 Variants

| Variant | Definition |
| --- | --- |
| Single-difficulty Bernstein | One monotone Bernstein curve per dimension and one relevance vector, both shared by correctness and hazard; hazard subtracts player confidence from the correctness logit. |
| DD sigmoid | Separate sigmoid-shaped `d^C` and `d^H` curves. |
| Full DD-Bernstein | One monotone curve per dimension and branch: `d(x) = sum_m q_m B_m,p(x)`, with `q_0 >= ... >= q_p`. |
| Full DD-Bernstein + player propensity | Full DD-Bernstein with a partially pooled player correctness intercept `a_i`; negative values represent greater neg propensity. |
| Compact DD-Bernstein | `s_ij = a_j w_j^T theta_i`; `z^C = s_ij-b^C_j(x)` and `z^H = s_ij-b^H_j(x)-c_i`. One scalar curve per branch. |
| DD linear spline | Linear interpolation between clue-aligned landmarks. The monotone variant constrains successive landmarks to decrease. |
| Perceived difficulty Bernstein | `z^C = sum_k r_jk(theta_ik-d_jk)`; `z^H = sum_k r_jk(theta_ik-alpha_ik d_jk+beta_ik)`. Player-vector transform with `alpha_ik > 0`. |
| Perceived logit Bernstein | `z^C = sum_k r_jk(theta_ik-d_jk)`; `z^H = alpha_i z^C + beta_i`. Player-scalar transform with `alpha_i > 0`. |

Both current perceived models use
`alpha ~ LogNormal(0,1)` and free `beta ~ Normal(0,1)`. The old unconstrained
fits are retained below as historical comparisons.

`Bernstein 3/3/k` means degree 3, three latent dimensions, and Bernstein-drop
concentration `k`. Thus `3/3/2` uses concentration 2 and `3/3/0.67` uses
concentration 0.67. The last value controls how the total curve drop is
distributed across control-point steps; it is unrelated to the relevance prior.

### 2.2 Terminal intercepts versus learned locations

Terminal intercepts modify only the final cell:

$$
z^C_{ijt}\mathrel{+}=e_C\mathbf{1}[t=T_j],
\qquad
z^H_{ijt}\mathrel{+}=e_H\mathbf{1}[t=T_j].
$$

The final cell includes the post-reading buzz window. `e_H` corrects late-buzz
and no-buzz mass; `e_C` allows a separate final-cell correctness shift. “No
terminal” fixes both to zero.

Learned locations change the prior center of each curve's starting
difficulty:

$$
\mu_C,\mu_H\sim N(0,1),
\qquad
s^C_j\sim N(\mu_C,1),\quad s^H_j\sim N(\mu_H,1).
$$

Without locations, `mu_C = mu_H = 0`. A location is a vertical difficulty
baseline, not a horizontal shift in token position. In full Bernstein the same
branch location centers every latent dimension's item-specific start; compact
Bernstein has one scalar start per item and branch.

| Compact arm | Terminal intercepts | Learned locations |
| --- | ---: | ---: |
| `terminal only` | Yes | No |
| `locations + terminal` | Yes | Yes |

Their difference estimates the location effect conditional on terminal
intercepts. Full Bernstein now has the corresponding matched comparison under
simplex relevance; Section 3.6 reports it.

### 2.3 Prior reference

Normal and LogNormal arguments below are `(location, scale)`; the second Gamma
argument is a rate. Sites are independent across players, items, dimensions,
and correctness/hazard branches unless the equation or a learned location
shares them.

Player priors:

$$
\theta_{ik}\sim N(0,1),\qquad c_i\sim N(0,1).
$$

The optional hierarchical player-neg-propensity arm adds

$$
\sigma_a\sim\operatorname{HalfNormal}(1),\qquad
a_i\sim N(0,\sigma_a),\qquad z^C_{ijt}\mathrel{+}=a_i.
$$

The population mean is fixed at zero so it does not duplicate the learned
correctness-curve location. Positive `a_i` means unusually reliable conversion;
negative `a_i` means greater neg propensity. The learned `sigma_a` partially
pools low-volume players toward zero.

The perceived models omit `c_i`. These are the priors used to fit each training
fold; frozen replay fits no held-out parameters. Other temporal workflows can
replace the player Normal locations/scales with a saved posterior or a
tier-conditioned population prior.

Relevance and skill-direction priors:

| Model | Prior | Meaning |
| --- | --- | --- |
| Full DD, Gamma arms | $r^C_{jk},r^H_{jk}\sim\operatorname{Gamma}(2,2)$ | Positive direction and magnitude. |
| Full DD, simplex arms | $r^C_j,r^H_j\sim\operatorname{Dirichlet}(\mathbf 1_K)$ | Direction only; each vector sums to one. |
| Perceived models | $r_j\sim\operatorname{Dirichlet}(2\mathbf 1_K)$ | One shared, less edge-seeking simplex. |
| Compact DD | $w_j\sim\operatorname{Dirichlet}(\mathbf 1_K)$ | Shared skill direction; $\sum_k w_{jk}=1$. |

The single-curve Bernstein baseline uses one Gamma relevance vector and one
Bernstein curve under the same priors, rather than separate branch draws.
In the main results table, plain `DD-Bernstein` rows use Gamma relevance;
`Simplex relevance` rows use `Dirichlet(1)`.

Bernstein-curve priors:

For branch $b\in\{C,H\}$,

$$
\mu_b\sim N(0,1),\qquad
s^b_{jk}\mid\mu_b\sim N(\mu_b,1),\qquad
D^b_{jk}\sim\operatorname{LogNormal}(0,0.5),\qquad
\pi^b_{jk}\sim\operatorname{Dirichlet}(\kappa\mathbf 1_p).
$$

`s` is starting difficulty, `D > 0` is total curve drop, and `pi` divides that
drop across the `p` Bernstein steps. Reported `3/3/2` runs use `p=3` and
`kappa=2`. Without learned locations, `mu_C=mu_H=0`; perceived models use one
shared curve with zero location. Compact DD uses scalar `s,D,pi` and also

$$
a_j\sim\operatorname{LogNormal}(0,0.5)
$$

for positive item discrimination. When enabled, terminal effects use

$$
e_C,e_H\sim N(0,2).
$$

Perception-transform priors:

$$
\alpha\sim\operatorname{LogNormal}(0,1)>0,
\qquad \beta\sim N(0,1).
$$

`alpha,beta` are vectors for perceived difficulty and scalars for perceived
logit. `beta` is unconstrained. Historical unconstrained runs instead used
`alpha ~ Normal(1,1)`; their results are retained only for comparison.

Other curve families:

| Family | Curve priors |
| --- | --- |
| DD sigmoid | $\beta^b_{jk}\sim N(0,1)$, $\gamma^b_{jk}\sim\operatorname{HalfCauchy}(5)$, $\mu^b_{jk}\sim\operatorname{Beta}(2,2)$; relevance is $\operatorname{Gamma}(2,2)$. |
| DD linear spline | Each unconstrained landmark is $N(0,1)$; relevance is $\operatorname{Gamma}(2,2)$. |
| Monotone DD spline | Start $\sim N(0,1)$ and each successive drop $\sim\operatorname{HalfNormal}(0.5)$. |
| Optional correctness calibration | Scale $\sim\operatorname{LogNormal}(0,0.5)$ and bias $\sim N(0,3)$; disabled in the reported main-table runs. |

### 2.4 Metric reference

| Metric | Read as |
| --- | --- |
| Accuracy / lift | 0.5-threshold correctness; lift is against always-correct. |
| Neg F1 | Harmonic mean of neg precision and neg recall at the stated threshold; higher is better. |
| Correctness LL / Brier / ECE | Correctness probability error; lower is better. |
| AUC | Correctness ranking; higher is better. |
| Joint event LL | No buzz, or first buzzer + position + correctness; lower is better. |
| Integrated Brier / position MAE | Timing error; lower is better. |
| First-buzzer top-1 | Fraction of buzz events where the highest-probability player is the observed first buzzer; higher is better. |
| No-buzz error | Predicted minus observed rate; zero is ideal. |
| Final-decile mass | Unconditional late-buzz mass; observed value is 17.56%. |

## 3. Current evidence

Results differ by objective:

| Objective | Strongest result in the current runs |
| --- | --- |
| Joint marked-event likelihood | Compact double-Bernstein with learned curve locations and terminal intercepts: 6.4157 log loss |
| Correctness probability and calibration | Simplex-relevance double-Bernstein 3/3/0.67 with learned locations and terminal intercepts: 0.4873 log loss, 0.1581 Brier, 0.0110 ECE |
| Threshold accuracy | Simplex-relevance double-Bernstein 3/3/2 with learned locations, terminal intercepts, and player propensity: 77.95% accuracy |
| Correctness ranking | Unconstrained DD linear spline: 0.7228 AUC |
| Buzz timing | Unconstrained DD linear spline: 0.0928 integrated Brier and 0.1359 position MAE |
| First-buzzer identity | Legacy single-difficulty Bernstein 5/5/2: 40.07% first-buzzer top-1 |
| No-buzz calibration | Simplex-relevance double-Bernstein with learned locations, terminal intercepts, and player propensity: +0.07 percentage-point error |

The main five-fold means are:

| Model | Accuracy | Neg F1 | Lift over all-correct | Joint event LL | Correctness LL | AUC | ECE | Position MAE | First-buzzer top-1 | No-buzz error | Predicted final-decile mass |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [Single-difficulty Bernstein 5/5/2, legacy](results/compirt/holdout/double-difficulty/model-comparisons/double-vs-single-difficulty/single-curve-bernstein-baseline/seed_42/) | 65.71% | 38.91% | −10.99 pp | 6.7289 | 0.7286 | 0.6314 | 0.1918 | 0.1375 | **40.07%** | +4.78 pp | 13.92% |
| [DD-Bernstein 3/3/2, no terminal](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-unconstrained/) | 76.28% | 40.07% | −0.42 pp | 6.4959 | 0.5094 | 0.7114 | 0.0725 | 0.1389 | 38.08% | +4.53 pp | 12.92% |
| [DD-Bernstein 3/3/2, terminal](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-unconstrained-terminal/) | 76.55% | 41.11% | −0.15 pp | 6.4375 | 0.5059 | 0.7166 | 0.0706 | 0.1364 | 37.99% | −0.49 pp | 18.94% |
| [Simplex relevance, no terminal](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex/) | 77.16% | 36.84% | +0.46 pp | 6.7444 | 0.5025 | 0.7115 | 0.0673 | 0.1783 | 34.04% | +6.44 pp | 9.48% |
| [Simplex relevance, terminal](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/) | 77.31% | 37.34% | +0.61 pp | 6.7216 | 0.5021 | 0.7140 | 0.0707 | 0.1667 | 33.67% | −0.19 pp | **17.52%** |
| [Simplex relevance, locations + terminal](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/) | **77.95%** | 23.21% | **+1.25 pp** | 6.6123 | 0.4878 | 0.7155 | 0.0125 | 0.1519 | 35.16% | **+0.09 pp** | 18.82% |
| [Simplex relevance 3/3/0.67, locations + terminal](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-330p67-simplex-locations-terminal/) | 77.94% | 23.88% | +1.24 pp | 6.6090 | **0.4873** | 0.7160 | **0.0110** | 0.1494 | 35.11% | +0.13 pp | 19.62% |
| [Simplex relevance, locations + terminal + player `a_i`](results/compirt/holdout/double-difficulty/variants/player-neg-propensity/) | **77.95%** | 23.92% | **+1.25 pp** | 6.5828 | 0.4878 | 0.7158 | 0.0128 | 0.1511 | 36.09% | **+0.07 pp** | 18.66% |
| [Perceived difficulty, unconstrained `alpha`](results/compirt/holdout/double-difficulty/variants/perceived-difficulty/unconstrained/) | 76.83% | 21.77% | +0.13 pp | 7.6178 | 0.5166 | 0.6605 | 0.0350 | 0.3277 | 35.10% | +20.81 pp | 3.23% |
| [Perceived difficulty, `alpha > 0`](results/compirt/holdout/double-difficulty/variants/perceived-difficulty/positive-alpha/) | 64.87% | 35.59% | −11.83 pp | 6.6373 | 0.6359 | 0.6017 | 0.2022 | 0.1363 | 39.18% | +3.43 pp | 13.85% |
| [Perceived difficulty, three-slice `alpha,beta`](results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice/) | 58.57% | 37.99% | −18.13 pp | 6.8075 | 0.7050 | 0.6009 | 0.2584 | 0.1383 | 37.50% | +3.76 pp | 13.67% |
| [Perceived logit, unconstrained `alpha`](results/compirt/holdout/double-difficulty/variants/perceived-logit/unconstrained/) | 76.65% | 1.67% | −0.05 pp | 7.7776 | 0.6080 | 0.5486 | 0.1058 | 0.3418 | 35.15% | +22.28 pp | 2.86% |
| [Perceived logit, `alpha > 0`](results/compirt/holdout/double-difficulty/variants/perceived-logit/positive-alpha/) | 37.59% | 39.21% | −39.11 pp | 6.7589 | 0.7875 | 0.6065 | 0.3458 | 0.1376 | 39.18% | +3.65 pp | 12.75% |
| [DD linear spline](results/compirt/holdout/double-difficulty/model-comparisons/curve-family/linear-spline/seed_42/) | 73.45% | **46.28%** | −3.25 pp | 6.4596 | 0.5651 | **0.7228** | 0.1185 | **0.1359** | 39.74% | +3.37 pp | 17.76% |
| [Monotone DD linear spline](results/compirt/holdout/double-difficulty/model-comparisons/curve-family/monotone-linear-spline/) | 63.40% | 43.01% | −13.30 pp | 8.1446 | 0.8367 | 0.6571 | 0.2265 | 0.1510 | 32.47% | +18.22 pp | 16.39% |

Each model name links to the run directory it was measured from. The seven
degree-3 Bernstein rows all live in
[`results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/`](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/),
one folder per configuration, named for its own settings:

| Row | Directory |
| --- | --- |
| `DD-Bernstein 3/3/2, no terminal` | `dd-bernstein-332-unconstrained/` |
| `DD-Bernstein 3/3/2, terminal` | `dd-bernstein-332-unconstrained-terminal/` |
| `Simplex relevance, no terminal` | `dd-bernstein-332-simplex/` |
| `Simplex relevance, terminal` | `dd-bernstein-332-simplex-terminal/` |
| `Simplex relevance, locations + terminal` | `dd-bernstein-332-simplex-locations-terminal/` |
| `Simplex relevance 3/3/0.67, locations + terminal` | `dd-bernstein-330p67-simplex-locations-terminal/` |

The naming split is the relevance parameterization, not the curve family: rows
named `DD-Bernstein` use the unconstrained per-dimension relevance, rows named
`Simplex relevance` use `Dirichlet(ones(k))`. Both are degree-3 Bernstein.

`dd-bernstein-332-unconstrained/` is also the `degree_3/curves_3/dirichlet_2`
cell of the hyperparameter grid, and `dd-bernstein-332-unconstrained-terminal/`
is also the Bernstein arm of the curve-family and compact-parameterization
comparisons — the latter still holds a second copy of that same fit
(both report `final_loss = 286419.26131153107` on fold 0).

The learned-location simplex models improve on the always-correct baseline by
1.24–1.25 percentage points. The earlier simplex models improve it by 0.46–0.61
points. Most other models remain at or below the baseline.

No frozen single-difficulty Bernstein 3/3/2 fit is saved in the repository. The
table uses the available single-difficulty Bernstein 5/5/2 model
(degree 5, five latent dimensions, drop concentration 2). Its values are the
unweighted means of the same five fold-level metric files used for the other
main-table rows. This is a legacy fit under older training conventions, so its
comparison with DD-Bernstein 3/3/2 is descriptive rather than a controlled
single-versus-double-difficulty ablation.

### 3.1 Separate correctness and hazard curves

The double-difficulty models give correctness and buzz hazard separate
relevance vectors and difficulty curves. The earlier single-curve model instead
derived hazard from the correctness logit by subtracting player confidence.

The four-arm, five-dimensional comparison in the
[`matrix-infill` report](results/compirt/holdout/double-difficulty/model-comparisons/double-vs-single-difficulty/aggregate/comparison.md)
shows the following pooled results:

| Metric | Sigmoid baseline | Double sigmoid | Bernstein baseline | Double Bernstein |
| --- | ---: | ---: | ---: | ---: |
| Accuracy | 62.75% | 74.14% | 65.71% | **74.66%** |
| Neg F1 at 0.5 | 40.00% | 33.68% | 38.94% | **42.67%** |
| Correctness/neg AUC | 0.632 | 0.675 | 0.631 | **0.709** |
| Neg average precision | 0.327 | 0.368 | 0.338 | **0.442** |
| Correctness log loss | 0.811 | 0.546 | 0.729 | **0.528** |
| ECE | 0.219 | **0.075** | 0.192 | 0.092 |
| Joint marked-event log loss | 6.801 | 6.528 | 6.729 | **6.514** |
| Conditional final-decile mass | 9.71% | 11.36% | 14.83% | **16.57%** |

Relative to its saved single-curve parent, double Bernstein improves AUC by 0.078,
neg average precision by 0.104, correctness log loss by 0.201, and accuracy by
9.0 percentage points. Double sigmoid improves AUC by 0.043, correctness log
loss by 0.264, ECE by 0.143, and accuracy by 11.4 points. The source report
confirms that each of these improvements has the same sign in all five folds.

Bernstein places more mass in the late-question tail, but separating the curves
does not improve
first-buzzer top-1 accuracy: the Bernstein comparison moves from 0.401 to 0.395.
The measured benefit is in correctness prediction and the timing distribution,
not player ordering.

This is not a controlled ablation of decoupling alone. The saved single-curve
baselines were replayed through the current evaluator but were not retrained
under the current terminal-survival convention, positive-amplitude prior, or
learning rate. The parent-to-double differences are strong descriptive evidence,
not an isolated causal estimate.

The saved single-difficulty fold artifacts are under
[`single-curve-bernstein-baseline`](results/compirt/holdout/double-difficulty/model-comparisons/double-vs-single-difficulty/single-curve-bernstein-baseline/).

### 3.2 Terminal-cell intercepts

The final token position also represents the entire post-reading buzz window.
The descriptive analysis in
[`docs/terminal-cell.md`](docs/terminal-cell.md) measures an empirical team
first-buzz hazard of about 0.05 mid-question, 0.29 with one token remaining, and
0.75 in the final cell. A smooth position curve cannot represent that one-cell
jump directly.

The proposed correction adds two global `Normal(0, 2)` intercepts at the final
position only: one for correctness and one for hazard. Two paired comparisons,
under distinct relevance priors, isolate the terminal-intercept flag:

| Metric | Gamma, no terminal | Gamma, terminal | Simplex, no terminal | Simplex, terminal |
| --- | ---: | ---: | ---: | ---: |
| Joint event LL | 6.4959 | **6.4375** | 6.7444 | **6.7216** |
| No-buzz calibration error | +4.53 pp | **−0.49 pp** | +6.44 pp | **−0.19 pp** |
| Final-decile mass (17.56% observed) | 12.92% | 18.94% | 9.48% | 17.52% |
| Position MAE | 0.1389 | **0.1364** | 0.1783 | **0.1667** |
| Accuracy | 76.28% | **76.55%** | 77.16% | **77.31%** |
| Neg F1 at 0.5 | 40.07% | **41.11%** | 36.84% | **37.34%** |
| AUC | 0.7114 | **0.7166** | 0.7115 | **0.7140** |

Under both priors, terminal intercepts reduce no-buzz error, restore
final-decile mass, and improve joint event log loss and position MAE. Accuracy
and AUC also improve slightly.

The benefit is targeted rather than universal. Under the simplex prior, ECE
worsens from 0.0673 to 0.0707 and integrated Brier from 0.1078 to 0.1103.
First-buzzer top-1 accuracy also falls slightly under both priors (0.3808 to
0.3799 for Gamma and 0.3404 to 0.3367 for simplex).

The no-terminal Gamma model has also been run on `season_2024_25`, with 51,600
held-out events. It again overpredicts no-buzz events by 4.27 percentage points,
against a lower observed rate of 0.97%. Accuracy is 76.40% versus a 76.54%
all-correct baseline, and joint event log loss is 6.4737. This reproduces the
calibration problem on a second split; it does not test the benefit
of terminal intercepts, because the matching terminal arm has not been run.

For evaluation validity, the NumPy replay path applies the same learned
intercepts as the fitted model. The implementation check reported in
[`docs/terminal-cell.md`](docs/terminal-cell.md) agrees with model predictions to
`7e-8`. Readers treat missing intercept keys as zero, preserving older fits.

### 3.3 Compact double-Bernstein

The compact model uses a scalar skill projection and one Bernstein curve per
branch, rather than a separate curve for every latent dimension. At three skill
dimensions and degree 3, it has 11 effective item parameters, compared with 30
for full double-Bernstein. The selected compact specification also has four
global parameters: two curve-location means and two terminal intercepts.

| Model | Item parameters | Joint event LL | Correctness LL | AUC | ECE | Accuracy | Neg F1 | First-buzzer top-1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Full DD-Bernstein, terminal | 30 | 6.4375 | **0.5059** | **0.7166** | 0.0706 | 76.55% | 41.11% | 37.99% |
| Compact, terminal only | 11 | 6.4776 | 0.5302 | 0.7091 | 0.0812 | 74.93% | **41.57%** | 39.41% |
| Compact, locations + terminal | 11 | **6.4157** | 0.5151 | 0.7045 | **0.0550** | **76.64%** | 35.64% | **39.50%** |

The compact locations-plus-terminal model has the lowest joint event log loss
and uses fewer item parameters. It improves ECE, accuracy, and first-buzzer
top-1, but has worse correctness log loss, AUC, and position MAE than the full
model.

Learned curve locations improve the terminal-only compact model by 0.0619 joint
event log loss, 0.0262 ECE, and 1.71 accuracy points. This attribution is
conditional on terminal intercepts. The planned 2×2 also includes `compact-base`
and `compact-locations`, but those two arms have not been run, so the effects of
the two global parameter pairs cannot yet be separated fully. The specification
and ablation design are documented in
[`docs/compact-double-bernstein.md`](docs/compact-double-bernstein.md).

### 3.4 Bernstein and linear-spline curves

The completed five-fold comparison in
[`docs/dd-linear-spline-vs-bernstein-3-3-2.md`](docs/dd-linear-spline-vs-bernstein-3-3-2.md)
shows a stable correctness/timing tradeoff:

- Bernstein 3/3/2 is better in all five folds on correctness log loss
  (0.5094 vs 0.5651), ECE (0.0725 vs 0.1185), Brier score (0.1661 vs 0.1822),
  and threshold accuracy (76.28% vs 73.45%).
- The unconstrained linear spline is better in all five folds on integrated
  Brier (0.0928 vs 0.0945), joint event log loss (6.4596 vs 6.4959),
  first-buzzer top-1 accuracy (39.74% vs 38.08%), no-buzz calibration error
  (3.37 vs 4.53 percentage points), and position MAE (0.1359 vs 0.1389).
- The spline has higher AUC (0.7228 vs 0.7114) despite worse probability scores,
  so it ranks correct and incorrect buzzes better but is less well calibrated.

This is a comparison of complete configurations, not an isolated curve-family
ablation. The spline uses five dimensions, learning rate 0.01, and 114,520 total
effective parameters; Bernstein uses three dimensions, learning rate 0.005, and
43,620 parameters.

The current monotone linear-spline implementation has 8.1446 joint event log
loss, 0.8367 correctness log loss, 0.2265 ECE, and 63.40% accuracy. These results
apply to this implementation, not to monotone splines in general.

### 3.5 Relevance prior

The simplex variant replaces independent `Gamma(2, 2)` relevance coordinates
with a `Dirichlet(1, ..., 1)` vector for each branch. This fixes relevance
magnitude at one and retains only its direction.

| Metric | Gamma + terminal | Simplex + terminal |
| --- | ---: | ---: |
| Accuracy | 76.55% | **77.31%** |
| Lift over all-correct | −0.15 pp | **+0.61 pp** |
| Correctness log loss | 0.5059 | **0.5021** |
| Brier score | 0.1644 | **0.1636** |
| AUC | **0.7166** | 0.7140 |
| Neg precision / recall | 0.495 / **0.351** | **0.524** / 0.290 |
| Neg F1 at 0.5 | **41.11%** | 37.34% |
| Joint event LL | **6.4375** | 6.7216 |
| Position MAE | **0.1364** | 0.1667 |
| Integrated Brier | **0.0942** | 0.1103 |
| First-buzzer top-1 | **0.3799** | 0.3367 |

The simplex prior improves correctness probability scores and is the only
competitive specification to exceed the always-correct threshold baseline.
It is substantially worse on timing and first-buzzer identity. Its slightly
lower AUC, higher neg precision, lower neg recall, and narrower prediction
distribution (standard deviation 0.164 vs 0.202) indicate a change in
calibration and threshold behavior rather than better discrimination.

### 3.6 Learned curve locations in simplex Bernstein

The full 3/3/2 simplex model now has a clean learned-location comparison with
terminal intercepts held on. The only structural change is two global
`Normal(0, 1)` population means for correctness and hazard curve starts. Both
arms use the same folds, split and optimization seeds, 3,000 steps, and learning
rate.

| Metric | Simplex + terminal | Simplex + locations + terminal | Change |
| --- | ---: | ---: | ---: |
| Joint event LL | 6.7216 | **6.6123** | −0.1093 |
| Correctness LL | 0.5021 | **0.4878** | −0.0143 |
| Brier score | 0.1636 | **0.1582** | −0.0054 |
| ECE | 0.0707 | **0.0125** | −0.0582 |
| Accuracy | 77.31% | **77.95%** | +0.64 pp |
| Lift over all-correct | +0.61 pp | **+1.25 pp** | +0.64 pp |
| AUC | 0.7140 | **0.7155** | +0.0014 |
| Neg F1 at 0.5 | **37.34%** | 23.21% | −14.13 pp |
| Position MAE | 0.1667 | **0.1519** | −0.0149 |
| Integrated Brier | 0.1103 | **0.1017** | −0.0087 |
| First-buzzer top-1 | 33.67% | **35.16%** | +1.49 pp |
| No-buzz calibration error | −0.19 pp | +0.09 pp | 0.10 pp closer to zero |
| Final-decile mass (17.56% observed) | **17.52%** | 18.82% | +1.30 pp |

Joint event LL, correctness LL, Brier, ECE, accuracy, position MAE, integrated
Brier, and first-buzzer top-1 improve in all five matched folds. AUC improves in
three of five. The no-buzz rate remains well calibrated and is closer to zero on
average, but the late-buzz distribution overshoots: final-decile mass moves from
nearly exact at 17.52% to 18.82%.

The two learned centers are extremely stable across folds:
`mu_C = -1.767 ± 0.008` and `mu_H = 4.456 ± 0.004`. They are large vertical
recenterings, not token-position shifts, and indicate that a zero-centered start
prior is a poor match when relevance magnitude is fixed to one by the simplex.
The configuration has 28 effective item parameters plus four globals (the two
locations and two terminal intercepts), only two globals more than the earlier
simplex-terminal arm.

At concentration 2.0, this model has the highest threshold accuracy, but its
joint LL and position MAE trail the compact and Gamma alternatives. The mean
final-100-step slope is −4.25, so the 3,000-step fits have not plateaued.

Artifacts are under
[`dd-bernstein-332-simplex-locations-terminal`](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/),
with fold means in
[`aggregate/fold_mean_std.csv`](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/aggregate/fold_mean_std.csv).

#### Accuracy-tuned neg thresholds

The frozen DD-Bernstein 3/3/2 model without terminal intercepts and the frozen
3/3/2 simplex-relevance model with learned locations and terminal intercepts
use different operating points at the neg decision boundary. Both models use
the same matrix-infill protocol: parameters are fitted on four whole-game folds
and replayed without refitting on the fifth. Here a neg probability is
`1 - predicted_correct`, and a buzz is classified as a neg when that
probability is at least the threshold. The observed neg rate is 23.30% in the
shared 45,995 held-out first buzzes.

As a diagnostic, pooling all five held-out folds and searching thresholds from
0 to 1 in increments of 0.002 gives:

| Model | Threshold | Accuracy | Neg precision | Neg recall | Neg F1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| DD-Bernstein 3/3/2, fixed | 0.500 | 76.28% | 48.70% | **34.04%** | **40.07%** |
| DD-Bernstein 3/3/2, accuracy-tuned | **0.648** | 77.89% | 60.87% | 14.31% | 23.18% |
| Simplex locations + terminal, fixed | 0.500 | **77.95%** | **61.55%** | 14.30% | 23.20% |
| Simplex locations + terminal, accuracy-tuned | **0.500** | **77.95%** | **61.55%** | 14.30% | 23.20% |

The pooled threshold and its score use the same observations, so the tuned
accuracy is optimistic and is not a new held-out model result. A
leave-one-fold-out threshold-transfer check selects the accuracy-maximizing
threshold on the other four folds and applies it to the omitted fold. It gives
the same qualitative result:

| Model | Mean transferred threshold | Accuracy | Neg precision | Neg recall | Neg F1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| DD-Bernstein 3/3/2 | 0.6480 | **77.86%** | **60.60%** | 14.24% | 23.06% |
| Simplex locations + terminal | 0.4944 | **77.86%** | 60.24% | **14.69%** | **23.62%** |

Much of the fixed-threshold difference is an operating-point choice. The
unconstrained DD-Bernstein model trades accuracy for neg recall at 0.5; moving
its threshold near 0.65 produces almost the same transferred accuracy,
precision, recall, and F1 as the simplex locations + terminal model near 0.5.
The simplex model reaches that operating point without a large threshold shift,
consistent with its lower calibration error. The transferred thresholds are a
stronger diagnostic than the pooled optimum, but a production estimate should
still tune the threshold inside each training split and reserve its held-out
fold only for final evaluation.

#### Drop-concentration follow-up: 0.67

A matched five-fold run changed only the Bernstein drop concentration from 2.0
to 0.67 in the degree-3, three-dimensional simplex-relevance model with learned
curve locations and terminal intercepts. Both arms use the `year_2024` split,
split and optimization seed 42, 3,000 SVI steps, and learning rate 0.005.

| Metric | Concentration 2.0 | Concentration 0.67 | Change |
| --- | ---: | ---: | ---: |
| Joint event LL | 6.6124 | **6.6091** | −0.0032 |
| Correctness LL | 0.4878 | **0.4873** | −0.0005 |
| Brier score | 0.1582 | **0.1581** | −0.0002 |
| ECE | 0.0098 | **0.0070** | −0.0029 |
| Accuracy | **77.95%** | 77.94% | −0.01 pp |
| AUC | 0.7154 | **0.7160** | +0.0006 |
| Neg F1 at 0.5 | 23.21% | **23.88%** | +0.67 pp |
| Position MAE | 0.1519 | **0.1494** | −0.0024 |
| Integrated Brier | 0.1017 | **0.1010** | −0.0007 |
| First-buzzer top-1 | **35.16%** | 35.11% | −0.05 pp |
| No-buzz Brier | **0.01323** | 0.01335 | +0.00012 |

Concentration 0.67 improves joint event LL, integrated Brier, and position MAE
in all five matched folds. It improves correctness LL, Brier, AUC, and ECE in
four of five. Threshold accuracy and first-buzzer identification are
effectively tied, while no-buzz Brier is slightly worse in every fold. The
average final-100-step loss slope is still −4.39, so the fits have not fully
plateaued at 3,000 steps. This is a small equal-budget advantage, not a firm
concentration selection; the existing
6,000- and 20,000-step concentration-2.0 runs also show that training duration
materially affects joint event LL.

Artifacts are under
[`dd-bernstein-330p67-simplex-locations-terminal`](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-330p67-simplex-locations-terminal/),
with pooled metrics in
[`aggregate/pooled.csv`](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-330p67-simplex-locations-terminal/aggregate/pooled.csv).

### 3.7 Bernstein hyperparameter grid

The
[`dd-bernstein-ablation` summary](results/compirt/holdout/double-difficulty/ablations/hyperparameter-grid/aggregate/summary.md)
covers 100 no-terminal configurations: degree 3–6, one to five dimensions, and
Dirichlet drop concentration 0.67–2.0.

- The selected configuration is degree 3, four dimensions, concentration 2.0,
  with pooled joint event log loss 6.48525.
- The top 20 configurations span 6.48525–6.49971. These small differences should
  require optimizer-seed replication or an explicit
  matched-fold uncertainty analysis.
- Degree 3 occupies the top four ranks, but its advantage is not uniform at
  matched dimension and concentration. Degree 5 wins some three-dimensional
  comparisons, degree 4 wins the two-dimensional comparisons, and degree 6 wins
  the one-dimensional comparisons.
- Concentration 2.0 gives the lowest joint event log loss in every fixed
  degree-by-dimension cell in this grid.
- Adding terminal intercepts to the degree-3, three-dimensional,
  concentration-2 model reaches 6.4375, better than every no-terminal grid arm.
- Grid accuracy ranges from 72.74% to 76.71%. The highest-accuracy configurations
  are one-dimensional and remain essentially at the always-correct baseline
  while having among the worst joint event losses. Accuracy is not sufficient
  for model selection.

The reported winner was selected on the same cross-validation folds used to
score it. It is a model-selection result, not an unbiased test estimate.

### 3.8 Perceived difficulty Bernstein

The player transform is inside the hazard equation:

$$
z^C_{ijt}=\sum_k r_{jk}[\theta_{ik}-d_{jk}(x)],
\qquad
z^H_{ijt}=\sum_k r_{jk}[\theta_{ik}-\alpha_{ik}d_{jk}(x)+\beta_{ik}].
$$

Current priors are

$$
\alpha_{ik}\sim\operatorname{LogNormal}(0,1)>0,
\qquad \beta_{ik}\sim N(0,1).
$$

| Metric | Unconstrained `alpha` | `alpha > 0` | Change |
| --- | ---: | ---: | ---: |
| Joint event LL | 7.6178 | **6.6373** | −0.9805 |
| Position MAE | 0.3277 | **0.1363** | −0.1914 |
| Integrated Brier | 0.1682 | **0.0943** | −0.0739 |
| First-buzzer top-1 | 35.10% | **39.18%** | +4.09 pp |
| No-buzz error | +20.81 pp | **+3.43 pp** | −17.38 pp |
| Correctness LL | **0.5166** | 0.6359 | +0.1193 |
| Accuracy | **76.83%** | 64.87% | −11.96 pp |
| Neg F1 at 0.5 | 21.77% | **35.59%** | +13.82 pp |

Timing improves and correctness worsens in all five matched folds. Mean fitted
`alpha` is 8.27 and mean `beta` is −1.48. With `alpha > 0`, the joint objective
uses the shared `theta,d,r` to fit hazard, distorting the same logit used for
correctness. This formulation underperforms the reference model.

#### Three-slice perception follow-up

The follow-up arm gives each player separate perception vectors for relative
position thirds while leaving correctness and the shared item curve unchanged:

$$
s(x)=
\begin{cases}
\text{first}, & x<1/3,\\
\text{middle}, & 1/3\le x<2/3,\\
\text{last}, & x\ge 2/3,
\end{cases}
\qquad
z^H_{ijt}=\sum_k r_{jk}
[\theta_{ik}-\alpha_{i,s(x),k}d_{jk}(x)+\beta_{i,s(x),k}].
$$

Each sliced `alpha` remains an independent `LogNormal(0,1)` draw and each
sliced `beta` an independent `Normal(0,1)` draw. The comparison uses the same
five `year_2024` game-holdout folds, optimization seed 42, and 3,000 SVI steps
as the one-slice positive-`alpha` arm.

| Metric | One slice | Three slices | Change |
| --- | ---: | ---: | ---: |
| Joint event LL | **6.6373** | 6.8075 | +0.1701 |
| Correctness LL | **0.6359** | 0.7050 | +0.0690 |
| Accuracy | **64.87%** | 58.57% | −6.30 pp |
| AUC | **0.6017** | 0.6009 | −0.0008 |
| Neg F1 at 0.5 | 35.59% | **37.99%** | +2.40 pp |
| ECE | **0.2022** | 0.2584 | +0.0562 |
| Position MAE | **0.1363** | 0.1383 | +0.0020 |
| Integrated Brier | **0.09429** | 0.09434 | +0.00004 |
| First-buzzer top-1 | **39.18%** | 37.50% | −1.68 pp |
| No-buzz error | **+3.43 pp** | +3.76 pp | +0.33 pp |

The extra flexibility worsens the main held-out objectives and increases the
effective parameter count from 30,735 to 48,195. Pooled over the five training
fold posterior medians, fitted `(mean alpha, mean beta)` moves from
`(5.24, −0.40)` in the first third to `(4.97, −0.69)` in the middle and
`(4.73, −0.87)` in the last third. The fitted transforms vary by slice but do
not generalize better. All five fits have
finite losses; their final-100-step slopes average −3.34, so the optimization
is still descending slightly at 3,000 steps, as in several other arms.

Artifacts: [unconstrained](results/compirt/holdout/double-difficulty/variants/perceived-difficulty/unconstrained/configuration.json),
[positive `alpha`](results/compirt/holdout/double-difficulty/variants/perceived-difficulty/positive-alpha/configuration.json), and
[three-slice `alpha,beta`](results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice/configuration.json).
Three-slice fold and pooled summaries are under
[`aggregate/`](results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice/aggregate/).

#### Alternating-optimization follow-up

Because the three-slice fits were still descending at 3,000 steps, a follow-up
alternated theta-only and alpha/beta-only player updates while continuing to
update every item parameter on every step. The same five `year_2024` folds,
seeds, degree-3 curves, three dimensions, learning rate 0.005, and concentration
2.0 priors were used. The alternating fit was evaluated first at 3,000 steps
and then rerun from scratch for 10,000 steps. A simultaneous-update 10,000-step
run provides the matched optimization-budget control.

| Metric | Standard 3k | Alternating 3k | Alternating 10k | Standard 10k |
| --- | ---: | ---: | ---: | ---: |
| Joint event LL | 6.8076 | 6.8625 | 6.7658 | **6.7303** |
| Correctness LL | 0.7050 | 0.7337 | 0.6612 | **0.6389** |
| Accuracy | 58.58% | 55.04% | 62.86% | **65.48%** |
| AUC | 0.6008 | 0.5939 | 0.6165 | **0.6215** |
| Neg F1 at 0.5 | 37.99% | **38.12%** | 38.07% | 37.48% |
| ECE | 0.2584 | 0.2823 | 0.2206 | **0.2000** |
| Brier | 0.2518 | 0.2649 | 0.2324 | **0.2223** |
| Position MAE | **0.1383** | 0.1392 | 0.1389 | 0.1389 |
| Integrated Brier | **0.09434** | 0.09500 | 0.09497 | 0.09493 |

At 3,000 steps, alternating updates worsen every correctness metric. At 10,000
steps, both schedules improve, but simultaneous updates have better correctness
metrics except negative-class F1 and lower joint event LL. Their mean
final-100-step slopes are −0.57 for simultaneous updates and 0.32 for
alternating updates. Position MAE and integrated Brier are nearly equal. The
matched-budget comparison attributes the gains to training duration, not the
alternating schedule.

Artifacts: [alternating 3k](results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating/configuration.json),
[alternating 10k](results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating-10000-steps/configuration.json),
and [standard 10k](results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-10000-steps/configuration.json).

### 3.9 Perceived logit Bernstein

The scalar affine transform is applied to the completed correctness logit:

$$
z^C_{ijt}=\sum_k r_{jk}[\theta_{ik}-d_{jk}(x)],
\qquad
z^H_{ijt}=\alpha_i z^C_{ijt}+\beta_i.
$$

Current priors are

$$
\alpha_i\sim\operatorname{LogNormal}(0,1)>0,
\qquad \beta_i\sim N(0,1).
$$

| Metric | Unconstrained `alpha` | `alpha > 0` | Change |
| --- | ---: | ---: | ---: |
| Joint event LL | 7.7776 | **6.7589** | −1.0187 |
| Position MAE | 0.3418 | **0.1376** | −0.2042 |
| Integrated Brier | 0.1750 | **0.0938** | −0.0813 |
| First-buzzer top-1 | 35.15% | **39.18%** | +4.03 pp |
| No-buzz error | +22.28 pp | **+3.65 pp** | −18.63 pp |
| AUC | 0.5486 | **0.6065** | +0.0579 |
| Correctness LL | **0.6080** | 0.7875 | +0.1795 |
| Accuracy | **76.65%** | 37.59% | −39.06 pp |
| Neg F1 at 0.5 | 1.67% | **39.21%** | +37.54 pp |

Timing and AUC improve in all five matched folds, while correctness LL, ECE,
and accuracy worsen in all five. Mean fitted `alpha` is 5.32 and mean `beta` is
−2.74. The constraint removes the sign reversal, but the hazard-heavy joint
objective then reshapes shared `z^C` at the expense of correctness. This fitted
scalar coupling underperforms the reference model.

Artifacts: [unconstrained](results/compirt/holdout/double-difficulty/variants/perceived-logit/unconstrained/configuration.json),
[positive `alpha`](results/compirt/holdout/double-difficulty/variants/perceived-logit/positive-alpha/configuration.json).

### 3.10 Hierarchical player neg propensity

The selected full DD-Bernstein 3/3/2 model was augmented with the zero-centered
player hierarchy from Section 2.3 while retaining simplex relevance, learned
curve locations, terminal intercepts, and the ordinary unweighted likelihood.
The new player effect enters correctness only; hazard remains unchanged
conditionally, although shared skill can move when the joint model is refit.
Every fold used the standard `year_2024` frozen matrix-infill protocol, seed 42,
and 3,000 SVI steps.

| Metric | Baseline | Player `a_i` | Change |
| --- | ---: | ---: | ---: |
| Joint event LL | 6.6123 | **6.5828** | −0.0295 |
| Correctness LL | 0.48780 | **0.48777** | −0.00003 |
| Brier | 0.15825 | **0.15806** | −0.00019 |
| Accuracy at 0.5 | **77.95%** | **77.95%** | 0.00 pp |
| AUC | 0.71547 | **0.71578** | +0.00031 |
| Neg average precision | 0.44991 | **0.45069** | +0.00078 |
| Neg precision at 0.5 | **61.59%** | 61.00% | −0.59 pp |
| Neg recall at 0.5 | 14.30% | **14.88%** | +0.57 pp |
| Neg F1 at 0.5 | 23.21% | **23.92%** | +0.71 pp |
| Integrated Brier | 0.10170 | **0.10093** | −0.00076 |
| Position MAE | 0.15186 | **0.15108** | −0.00078 |
| First-buzzer top-1 | 35.16% | **36.09%** | +0.92 pp |
| No-buzz error | +0.09 pp | **+0.07 pp** | −0.02 pp |

Threshold selection gives a small neg benefit.
For each held-out fold, the accuracy-maximizing threshold was selected using
the other four folds. The mean threshold moved from 0.506 to 0.511; held-out
accuracy rose from 77.865% to 77.993%, neg precision from 60.27% to 60.46%, neg
recall from 14.68% to 16.05%, and neg F1 from 23.61% to 25.37%.

The learned population scale is stable across folds (`sigma_a = 0.328--0.349`).
Posterior-median player effects have standard deviations of 0.134--0.153,
showing substantial shrinkage toward zero. The ranking gains are not fully
consistent: AUC and neg average precision improve in three of five folds,
while joint event LL improves in four. The hierarchy has a small effect; AUC
and average-precision changes require optimization-seed replication.

Artifacts: [configuration](results/compirt/holdout/double-difficulty/variants/player-neg-propensity/configuration.json)
and [aggregate results](results/compirt/holdout/double-difficulty/variants/player-neg-propensity/aggregate/).

### 3.11 Incorrect-response loss balancing and threshold equivalence

The selected full DD-Bernstein 3/3/2 model was refit with incorrect correctness
terms weighted by 1×, 1.5×, 2×, and 3×. Only the correctness loss was
reweighted; the survival/hazard loss was unchanged. All runs used simplex
relevance, learned curve locations, terminal intercepts, the five frozen
game-holdout folds, seed 42, and 3,000 SVI steps. The tables below pool the
out-of-fold predictions.

At the same fixed threshold of 0.5, higher weights produce more predicted
negs. Neg recall rises, but neg precision, accuracy, probability calibration,
and the joint likelihood worsen. Ranking also does not improve: both AUC and
neg average precision decline slightly.

| Incorrect weight | Accuracy | Neg precision | Neg recall | Neg F1 | AUC | Neg AP | Correctness LL | ECE | Joint event LL |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1× | **77.95%** | **61.55%** | 14.30% | 23.20% | **0.7154** | **0.4493** | **0.4878** | **0.0098** | **6.6124** |
| 1.5× | 77.20% | 51.89% | 29.34% | 37.48% | 0.7144 | 0.4485 | 0.4991 | 0.0604 | 6.6191 |
| 2× | 74.89% | 45.74% | 41.67% | 43.61% | 0.7130 | 0.4470 | 0.5256 | 0.1128 | 6.6441 |
| 3× | 69.07% | 39.04% | **58.36%** | **46.78%** | 0.7105 | 0.4440 | 0.5880 | 0.1870 | 6.7070 |

Weighting mainly changes the probability scale. If the ordinary probability
of correctness is $p$, weighted binary
cross-entropy is minimized at

$$
q_w=\frac{p}{p+w(1-p)},
\qquad
\operatorname{logit}(q_w)=\operatorname{logit}(p)-\log w.
$$

This transformation lowers correctness scores while mostly preserving their
ordering. For example, a 2× model score near 0.33 represents approximately the
same decision boundary as an unweighted score of 0.50. Comparing every model
at 0.50 compares different operating points, not just different
models. The theoretical and empirical accuracy thresholds show this shift:

| Incorrect weight | Theoretical threshold equivalent to ordinary 0.5 | Cross-fitted accuracy threshold |
| ---: | ---: | ---: |
| 1× | 0.500 | 0.506 |
| 1.5× | 0.400 | 0.387 |
| 2× | 0.333 | 0.300 |
| 3× | 0.250 | 0.204 |

Thresholds were selected without using the fold being evaluated: each held-out
fold used a threshold learned from the other four folds. Once each model gets
its own accuracy-maximizing threshold, the apparent differences nearly vanish.

| Incorrect weight | Mean threshold | Accuracy | Neg precision | Neg recall | Neg F1 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1× | 0.506 | 77.87% | 60.27% | 14.68% | 23.61% |
| 1.5× | 0.387 | 77.90% | 60.11% | **15.26%** | **24.34%** |
| 2× | 0.300 | **77.94%** | **61.15%** | 14.56% | 23.52% |
| 3× | 0.204 | 77.82% | 60.41% | 13.97% | 22.69% |

A threshold cannot maximize AUC because AUC evaluates the ranking over all
thresholds. For the requested “AUC threshold,” the cross-fitted Youden-J
threshold was used; it chooses the point on the ROC curve with the best
true-positive/false-positive tradeoff, equivalently maximum balanced accuracy.
Those operating points are also very similar across loss weights.

| Incorrect weight | Mean Youden threshold | Accuracy | Balanced accuracy | Neg precision | Neg recall | Neg F1 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1× | 0.779 | **66.47%** | **65.72%** | **37.27%** | 64.32% | **47.20%** |
| 1.5× | 0.711 | 65.02% | 65.66% | 36.37% | **66.86%** | 47.11% |
| 2× | 0.651 | 64.77% | 65.48% | 36.15% | 66.79% | 46.91% |
| 3× | 0.535 | 66.34% | 65.32% | 37.02% | 63.40% | 46.75% |

Incorrect-response weighting moves the score scale and changes the
precision-recall tradeoff at a fixed 0.5 cutoff. It does not improve AUC or neg
average precision, and the models are similar after threshold correction. For
calibrated probabilities or maximum accuracy, retain the ordinary likelihood
and tune the deployment threshold.

Artifacts: [1× baseline](results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/configuration.json),
[1.5× incorrect loss](results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-1.5/configuration.json),
[2× incorrect loss](results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-2/configuration.json),
and [3× incorrect loss](results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-3/configuration.json).

## 4. Limits on interpretation

- One optimization seed: the five folds are held-out data partitions, not
  independent training replications. Fold standard deviations describe split
  variation but omit optimizer-seed variation.
- Confounded comparisons: the spline comparison
  changes dimensionality and learning rate; the legacy single-curve baselines
  were not retrained under current conventions; and the compact 2×2 is incomplete.
- Cross-validation selection bias: the Bernstein grid winner was chosen and
  reported on the same folds. It needs nested cross-validation or a separate
  test set for an unbiased final estimate.
- Limited dataset coverage: most arms use the `year_2024` split. The
  `season_2024_25` run reproduces the no-terminal calibration problem only.
- Small threshold-accuracy margins: the best lift is 1.25 percentage points.
  Its five-fold consistency is encouraging, but it has not been tested across
  optimization seeds.
- Stage 1 only: these results do not support claims about bonuses, PPB, or
  team synergy.

## 5. Recommended next experiments

1. Run the `season_2024_25` Gamma model with terminal intercepts to test the
   terminal-cell result on the second split.
2. Complete the compact 2×2 with `compact-base` and `compact-locations` to
   separate location and terminal-intercept effects.
3. Repeat the main models across optimization seeds: compact
   locations-plus-terminal, Gamma-plus-terminal, both simplex terminal arms,
   and the unconstrained linear spline.
4. Repeat the standard and alternating three-slice 10,000-step runs across
   optimization seeds. The matched seed-42 result favors standard updates.
5. Retrain the single-curve baselines under the current survival convention,
   amplitude prior, learning rate, and checkpoint policy.
