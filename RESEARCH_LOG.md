# CompIRT research log

_Last reviewed: 2026-09-13._

Bonus results, compositional math, and synergy interpretation are in
[research log II](RESEARCH_LOG_2.md).

This log focuses on models that account for buzz timing and correctness, their
shared player representations, and downstream event predictions. Different
models lead different tasks.

This log retains model definitions, priors, numerical comparisons and the
reasoning behind the experiments. Run directories for each double-difficulty
experiment are indexed in
[`results/compirt/holdout/double-difficulty/README.md`](results/compirt/holdout/double-difficulty/README.md).
The frozen-skills models and results are archived in
[`archive/docs/frozen-skills-results.md`](archive/docs/frozen-skills-results.md).

Jump to [model definitions](#model-reference),
[historical experiments](#historical-compirt-evidence), or
[next experiments](#limits-and-next-experiments).

## Evaluation and comparability

The common population is `year_2024`: five whole-game holdout folds, split seed
42, **46,640 first-buzz race events**, of which **45,995 contain a buzz** and
645 contain no buzz. Each race has a roster of player rows. Correctness is
76.70%, so an always-correct classifier reaches 76.70% accuracy and zero neg F1.
The incorrect class includes zero-point incorrect attempts, not only −5 negs.
No-buzz prevalence is 1.38%; the final decile contains 17.56% of all events or
17.80% of buzzes.

| Evidence | Fitting and evaluation | Aggregation |
| --- | --- | --- |
| Historical CompIRT comparisons | Usually seed 42, 3,000 SVI steps, trained without a bounceback likelihood; four training folds and a fifth fold with `frozen_predict: true` | Unweighted fold means unless explicitly labeled pooled |
| Token-threshold downstream replay | Saved fits, 0.5 current-token buzz/correctness thresholds, seeded random token ties, tossup-only scoring and opponent continuations | Event/game fold means; pooled tournament PPG; separately labeled round-macro summaries |

These are repeatedly used development folds, not an untouched test set. This is
matrix infill with known player/question identities, not a future-season or
unseen-question evaluation. The historical conditional-correctness metrics
condition on the observed buzzer and position; the downstream replay resolves
correctness at its simulated buzzer and token. Position MAE predicts `E[t/T | a buzz occurs]`; timing distribution
scores include no-buzz events. Log losses use natural logarithms; smaller is
better. AUC/AP measure ranking across thresholds; precision, recall, F1 and
accuracy depend on the decision threshold.

The [normalized first-buzz likelihood repair](docs/first-buzz-likelihood.md)
changes subsequent CompIRT fits, not historical parameters. Normalized replay
of a historical fit does not constitute a repaired refit.

## Model reference

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

### Variants

| Variant | Definition |
| --- | --- |
| Single-difficulty Bernstein | One monotone Bernstein curve per dimension and one relevance vector, both shared by correctness and hazard; hazard subtracts player confidence from the correctness logit. |
| DD sigmoid | Separate sigmoid-shaped `d^C` and `d^H` curves. |
| Full DD-Bernstein | One monotone curve per dimension and branch: `d(x) = sum_m q_m B_m,p(x)`, with `q_0 >= ... >= q_p`. |
| Full DD-Bernstein + player propensity | Full DD-Bernstein with a partially pooled player correctness intercept `a_i`; negative values represent greater neg propensity. |
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

### Terminal intercepts versus learned locations

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
branch location centers every latent dimension's item-specific start. Full
Bernstein has a matched location comparison under simplex relevance; the
[location comparison](#learned-curve-locations-in-simplex-bernstein) reports it.

### Prior reference

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

The single-curve Bernstein baseline uses one Gamma relevance vector and one
Bernstein curve under the same priors, rather than separate branch draws.
In the historical results table, plain `DD-Bernstein` rows use Gamma relevance;
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
shared curve with zero location. When enabled, terminal effects use

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

### Metric reference

| Metric | Read as |
| --- | --- |
| Accuracy / lift | 0.5-threshold correctness; lift is against always-correct. |
| Neg F1 | Harmonic mean of neg precision and neg recall at the stated threshold; higher is better. |
| Correctness LL / Brier / ECE | Correctness probability error; lower is better. |
| AUC | Correctness ranking; higher is better. |
| Joint event LL | No buzz, or first buzzer + position + correctness; lower is better. |
| Integrated Brier / position MAE | Timing error; lower is better. |
| First-buzzer top-1 | Fraction of buzz events where the highest-probability player is the observed first buzzer; higher is better. |
| Replayed first-player/team accuracy | Fraction of recorded-buzz questions where the first player/team produced by token replay matches ground truth; higher is better. Separate from probability-argmax top-1. |
| Tossup scoring-player/team accuracy | Fraction of replayed questions where the player/team earning +10 matches ground truth, including opponent continuations and `no_score`; higher is better. |
| Tossup-only game winner | Accuracy of the winner obtained by summing replayed tossup points, compared with recorded tossup totals. Recorded ties are excluded; higher is better. No winner probability is produced. |
| Average tossup margin error / zero baseline | Average absolute error in the predicted tossup-point difference between the two teams. The zero-margin error is the no-information comparison; lower is better. |
| Tournament PPG rank correlation / PPG error / top-10 overlap | Agreement between predicted and recorded tossup PPG after pooling every game's one out-of-fold prediction. Random top-10 overlap is `K/N`; adjusted overlap removes that chance level. Higher correlation/overlap and lower PPG error are better. |
| No-buzz error | Predicted minus observed rate; zero is ideal. |
| Final-decile mass | Unconditional late-buzz mass; observed value is 17.56%. |

## Historical CompIRT evidence

Unless explicitly labeled pooled, these saved fits' tables use unweighted five-fold means. Historical
“best” claims below refer to the stated arms and scoring conventions, not all
current predictors.

The main five-fold means are:

| Model | Accuracy | Neg F1 | Lift over all-correct | Joint event LL | Correctness LL | AUC | ECE | Position MAE | First-buzzer top-1 | No-buzz error | Predicted final-decile mass |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [Single-difficulty Bernstein 5/5/2, legacy](results/compirt/holdout/double-difficulty/model-comparisons/double-vs-single-difficulty/single-curve-bernstein-baseline/seed_42/) | 65.71% | 38.91% | −10.99 pp | 6.7289 | 0.7286 | 0.6314 | 0.1918 | 0.1375 | **40.07%** | +4.78 pp | 13.92% |
| [DD-Bernstein 3/3/2, no terminal](results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-unconstrained/) | 76.28% | 40.07% | −0.42 pp | 6.4959 | 0.5094 | 0.7114 | 0.0725 | 0.1389 | 38.08% | +4.53 pp | 12.92% |
| [DD-Bernstein 3/3/2, terminal](results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-unconstrained-terminal/) | 76.55% | 41.11% | −0.15 pp | 6.4375 | 0.5059 | 0.7166 | 0.0706 | 0.1364 | 37.99% | −0.49 pp | 18.94% |
| [Simplex relevance, no terminal](results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex/) | 77.16% | 36.84% | +0.46 pp | 6.7444 | 0.5025 | 0.7115 | 0.0673 | 0.1783 | 34.04% | +6.44 pp | 9.48% |
| [Simplex relevance, terminal](results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-terminal/) | 77.31% | 37.34% | +0.61 pp | 6.7216 | 0.5021 | 0.7140 | 0.0707 | 0.1667 | 33.67% | −0.19 pp | **17.52%** |
| [Simplex relevance, locations + terminal](results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/) | **77.95%** | 23.21% | **+1.25 pp** | 6.6123 | 0.4878 | 0.7155 | 0.0125 | 0.1519 | 35.16% | **+0.09 pp** | 18.82% |
| [Simplex relevance 3/3/0.67, locations + terminal](results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-330p67-simplex-locations-terminal/) | 77.94% | 23.88% | +1.24 pp | 6.6090 | **0.4873** | 0.7160 | **0.0110** | 0.1494 | 35.11% | +0.13 pp | 19.62% |
| [Simplex relevance, locations + terminal + player `a_i`](results/compirt/holdout/double-difficulty/variants/player-neg-propensity/) | **77.95%** | 23.92% | **+1.25 pp** | 6.5828 | 0.4878 | 0.7158 | 0.0128 | 0.1511 | 36.09% | **+0.07 pp** | 18.66% |
| [Perceived difficulty, unconstrained `alpha`](results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/unconstrained/) | 76.83% | 21.77% | +0.13 pp | 7.6178 | 0.5166 | 0.6605 | 0.0350 | 0.3277 | 35.10% | +20.81 pp | 3.23% |
| [Perceived difficulty, `alpha > 0`](results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/) | 64.87% | 35.59% | −11.83 pp | 6.6373 | 0.6359 | 0.6017 | 0.2022 | 0.1363 | 39.18% | +3.43 pp | 13.85% |
| [Perceived difficulty, three-slice `alpha,beta`](results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice/) | 58.57% | 37.99% | −18.13 pp | 6.8075 | 0.7050 | 0.6009 | 0.2584 | 0.1383 | 37.50% | +3.76 pp | 13.67% |
| [Perceived logit, unconstrained `alpha`](results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/unconstrained/) | 76.65% | 1.67% | −0.05 pp | 7.7776 | 0.6080 | 0.5486 | 0.1058 | 0.3418 | 35.15% | +22.28 pp | 2.86% |
| [Perceived logit, `alpha > 0`](results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/positive-alpha/) | 37.59% | 39.21% | −39.11 pp | 6.7589 | 0.7875 | 0.6065 | 0.3458 | 0.1376 | 39.18% | +3.65 pp | 12.75% |
| [DD linear spline](results/compirt/holdout/double-difficulty/model-comparisons/curve-family/linear-spline/seed_42/) | 73.45% | **46.28%** | −3.25 pp | 6.4596 | 0.5651 | **0.7228** | 0.1185 | **0.1359** | 39.74% | +3.37 pp | 17.76% |
| [Monotone DD linear spline](results/compirt/holdout/double-difficulty/model-comparisons/curve-family/monotone-linear-spline/) | 63.40% | 43.01% | −13.30 pp | 8.1446 | 0.8367 | 0.6571 | 0.2265 | 0.1510 | 32.47% | +18.22 pp | 16.39% |

### Token-threshold game and tournament replay

**Reevaluated September 13, 2026:** all 15 historical model arms below were
replayed from their five saved held-out fits, without retraining or model
selection. The rule is the first **current-token** buzz probability at least
0.5, followed by correctness at least 0.5 at that simulated token. Same-token
ties use uniform random choice with seed 42 and a stable event-ID hash. Buzzes
are not chosen by an argmax over first-buzzer or scoring probabilities.

Correct answers earn +10 and end the tossup. An early first miss earns −5,
locks out the team, and allows the opponent to continue from the next token.
Terminal and bounceback misses earn zero. A question with no threshold crossing
is dead. Games, rounds and PPG all use these replayed points. Ground truth
uses literal recorded tossup values, including opponent conversions and late
misses. Saved correctness calibration and player intercept `a_i` are applied
when present.

Every model covers the same **46,620 tossups, 2,331 games and
29 tournaments**. First-player/team accuracy uses the 45,976
questions with an observed buzz. Tossup-winner accuracy uses 2,265 decisive
recorded games; margin error includes recorded ties. The direct event/game
table uses **unweighted five-fold means**. The zero-predicted-margin baseline
is **57.16 points MAE** on this coverage. The earlier expected-point/argmax
tables are [superseded](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/superseded-probability-tables.md).

#### Direct replay and tournament PPG prediction quality

Player PPG divides point totals by distinct inferred-lineup games, including
games with no buzz or no points. Each tournament is ranked once after pooling
the five test folds; PPG metrics are macro-averages over the 29 tournaments.
The parenthesized count after PPG rank correlation is the number of tournaments
with a defined correlation. Random top-10 overlap is 23.11%; adjusted overlap
removes that chance expectation.

| Model | Replayed first player | Replayed first team | Tossup game winner | Margin MAE | PPG rank correlation (n) | PPG MAE | Top-10 overlap | Chance-adjusted overlap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [Single-difficulty Bernstein 5/5/2, legacy](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/single-difficulty-bernstein-5-5-2-legacy/) | 8.30% | 12.34% | 58.50% | 49.37 | 0.6707 (29) | 17.97 | 59.31% | 46.77% |
| [DD-Bernstein 3/3/2, no terminal](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/dd-bernstein-3-3-2-no-terminal/) | 4.55% | 6.61% | 46.09% | 51.82 | 0.6265 (29) | 20.06 | 61.03% | 48.55% |
| [DD-Bernstein 3/3/2, terminal](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/dd-bernstein-3-3-2-terminal/) | **23.89%** | **54.94%** | **69.27%** | **48.33** | **0.8305 (29)** | **6.43** | **75.17%** | **68.36%** |
| [Simplex relevance, no terminal](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/simplex-relevance-no-terminal/) | 0.80% | 1.37% | 19.12% | 55.63 | 0.4948 (26) | 22.05 | 50.00% | 32.99% |
| [Simplex relevance, terminal](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/simplex-relevance-terminal/) | 18.16% | 45.79% | 65.70% | 50.74 | 0.7868 (29) | 7.43 | 71.38% | 62.80% |
| [Simplex relevance, locations + terminal](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/simplex-relevance-locations-terminal/) | 18.37% | 47.53% | 64.73% | 49.62 | 0.7829 (29) | 7.72 | 69.31% | 60.63% |
| [Simplex relevance 3/3/0.67, locations + terminal](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/simplex-relevance-3-3-0-67-locations-terminal/) | 18.34% | 47.44% | 65.52% | 49.45 | 0.7799 (29) | 7.62 | 70.34% | 61.96% |
| [Simplex relevance, locations + terminal + player `a_i`](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/simplex-relevance-locations-terminal-player-a-i/) | 18.93% | 47.93% | 66.05% | 49.37 | 0.7879 (29) | 7.62 | 72.41% | 64.83% |
| [Perceived difficulty, unconstrained `alpha`](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/perceived-difficulty-unconstrained-alpha/) | 0.00% | 0.00% | 0.04% | 57.16 | -0.1621 (1) | 22.65 | 22.76% | -1.97% |
| [Perceived difficulty, `alpha > 0`](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/perceived-difficulty-alpha-0/) | 4.16% | 8.20% | 49.99% | 52.95 | 0.5909 (29) | 19.54 | 52.41% | 38.28% |
| [Perceived difficulty, three-slice `alpha,beta`](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/perceived-difficulty-three-slice-alpha-beta/) | 2.73% | 5.89% | 45.79% | 53.95 | 0.6416 (29) | 20.32 | 55.86% | 43.13% |
| [Perceived logit, unconstrained `alpha`](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/perceived-logit-unconstrained-alpha/) | 0.00% | 0.00% | 0.00% | 57.16 | — (0) | 22.65 | 22.76% | -1.97% |
| [Perceived logit, `alpha > 0`](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/perceived-logit-alpha-0/) | 3.65% | 6.83% | 42.97% | 54.31 | 0.3280 (29) | 20.15 | 36.21% | 15.82% |
| [DD linear spline](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/dd-linear-spline/) | 8.14% | 11.41% | 58.59% | 49.44 | 0.6890 (29) | 18.65 | 65.17% | 54.75% |
| [Monotone DD linear spline](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/monotone-dd-linear-spline/) | 3.25% | 4.73% | 32.71% | 54.22 | 0.3870 (29) | 21.40 | 44.48% | 24.45% |

#### Replay behavior and round summaries

The observed no-buzz rate is **1.38%**.
A per-token 0.5 threshold can leave a question dead even when many smaller
hazards accumulate substantial total buzz probability. Predicted game ties
remain ties, so they count as incorrect against a decisive recorded winner.
The following rates expose those effects rather than forcing a winner.
Round-macro metrics average each tournament-round's game accuracy or margin
error across **365 tournament-rounds**; these weight rounds equally and
therefore differ from the fold means above.

| Model | Replayed no-buzz rate | Replayed tied games | Round-macro winner accuracy | Round-macro margin MAE |
| --- | ---: | ---: | ---: | ---: |
| Single-difficulty Bernstein 5/5/2, legacy | 82.65% | 18.92% | 58.15% | 50.37 |
| DD-Bernstein 3/3/2, no terminal | 90.71% | 36.51% | 46.50% | 52.49 |
| DD-Bernstein 3/3/2, terminal | 5.49% | 5.75% | **68.21%** | **49.07** |
| Simplex relevance, no terminal | 97.85% | 74.13% | 18.81% | 56.36 |
| Simplex relevance, terminal | 17.84% | 6.95% | 65.69% | 51.83 |
| Simplex relevance, locations + terminal | 15.41% | 6.56% | 63.24% | 50.98 |
| Simplex relevance 3/3/0.67, locations + terminal | 15.05% | 6.82% | 64.31% | 51.40 |
| Simplex relevance, locations + terminal + player `a_i` | 14.57% | 7.76% | 66.17% | 50.00 |
| Perceived difficulty, unconstrained `alpha` | 100.00% | 99.96% | 0.07% | 57.86 |
| Perceived difficulty, `alpha > 0` | 86.46% | 23.68% | 49.61% | 54.25 |
| Perceived difficulty, three-slice `alpha,beta` | 89.87% | 29.34% | 45.69% | 54.57 |
| Perceived logit, unconstrained `alpha` | 100.00% | 100.00% | 0.00% | 57.88 |
| Perceived logit, `alpha > 0` | 89.34% | 33.16% | 40.48% | 55.87 |
| DD linear spline | 84.35% | 19.82% | 58.53% | 50.06 |
| Monotone DD linear spline | 93.32% | 51.78% | 29.58% | 55.28 |

Team-point MAE is the mean absolute difference between replayed and recorded
tossup points per team, over 4,662 team-game rows (two per game); the
round-macro version weights the 365 tournament-rounds equally. Recorded teams
average **81.75** tossup points per game, and predicting zero for every team
gives an MAE of **81.83** (a few recorded totals are negative). Margin MAE hides
this failure, because both teams can be under-predicted by similar amounts.
Dead tossups also explain the tie rates: Simplex relevance, no terminal has no
live replayed tossup in 1,699 of 2,331 games, so 0–0 games account for 72.89 of
its 74.13 percentage points of ties.

| Model | Team-point MAE | Round-macro team-point MAE | Mean replayed team points | Replayed 0–0 games |
| --- | ---: | ---: | ---: | ---: |
| Single-difficulty Bernstein 5/5/2, legacy | 64.95 | 64.51 | 17.35 | 10.73% |
| DD-Bernstein 3/3/2, no terminal | 72.76 | 72.96 | 9.24 | 30.67% |
| DD-Bernstein 3/3/2, terminal | **26.77** | **26.71** | **76.75** | **0.00%** |
| Simplex relevance, no terminal | 79.73 | 80.65 | 2.14 | 72.89% |
| Simplex relevance, terminal | 31.63 | 30.57 | 72.03 | 0.86% |
| Simplex relevance, locations + terminal | 30.78 | 30.22 | 69.24 | 0.64% |
| Simplex relevance 3/3/0.67, locations + terminal | 30.23 | 30.14 | 69.70 | 0.73% |
| Simplex relevance, locations + terminal + player `a_i` | 30.16 | 29.39 | 70.04 | 0.64% |
| Perceived difficulty, unconstrained `alpha` | 81.83 | 82.70 | 0.00 | 99.96% |
| Perceived difficulty, `alpha > 0` | 70.24 | 70.67 | 11.82 | 17.85% |
| Perceived difficulty, three-slice `alpha,beta` | 72.98 | 73.97 | 8.96 | 22.35% |
| Perceived logit, unconstrained `alpha` | 81.83 | 82.71 | 0.00 | 100.00% |
| Perceived logit, `alpha > 0` | 71.48 | 71.94 | 10.67 | 27.33% |
| DD linear spline | 68.07 | 67.80 | 14.04 | 13.90% |
| Monotone DD linear spline | 76.88 | 77.43 | 5.04 | 50.32% |

Artifacts: [run manifest and command](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/README.md),
[fold rows](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/fold_metrics.csv),
[model metrics](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/model_metrics.csv),
[round/replay diagnostics](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/replay_diagnostics.csv), and
[scored game IDs](results/compirt/holdout/common/token-threshold-replay/buzz-0p5-correctness-0p5-random-ties-seed42/game_coverage.csv).

Model names link directly to their artifacts. Plain DD-Bernstein uses Gamma
relevance; simplex rows use Dirichlet(1). The no-terminal Gamma 3/3/2 fit also
appears in the hyperparameter grid; its terminal fit is reused in the curve-family
comparison, not an independent replication.

No frozen single-difficulty Bernstein 3/3/2 fit is saved in the repository. The
table uses the available single-difficulty Bernstein 5/5/2 model
(degree 5, five latent dimensions, drop concentration 2). Its historical timing/correctness values are the
unweighted means of the same five fold-level metric files used for the other
main-table rows. This is a legacy fit under older training conventions, so its
comparison with DD-Bernstein 3/3/2 is descriptive rather than a controlled
single-versus-double-difficulty ablation.

### Separate correctness and hazard curves

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

The source report confirms the correctness improvements have the same sign
in all five folds.

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

### Terminal-cell intercepts

The final token position also represents the entire post-reading buzz window.
The descriptive analysis in
[terminal-cell note](docs/double-difficulty-bernstein.md#terminal-cell-intercepts) measures an empirical team
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

### Bernstein and linear-spline curves

The completed five-fold comparison in
[curve-family comparison](results/compirt/holdout/double-difficulty/model-comparisons/curve-family/README.md)
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

### Relevance prior

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

### Learned curve locations in simplex Bernstein

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
joint LL and position MAE trail the Gamma alternatives. The mean
final-100-step slope is −4.25, so the 3,000-step fits have not plateaued.

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
[`dd-bernstein-330p67-simplex-locations-terminal`](results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-330p67-simplex-locations-terminal/),
with pooled metrics in
[`aggregate/pooled.csv`](results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-330p67-simplex-locations-terminal/aggregate/pooled.csv).

### Bernstein hyperparameter grid

The
[`dd-bernstein-ablation` summary](results/compirt/holdout/double-difficulty/ablations/capacity/degree-dimensions-drop-prior/aggregate/summary.md)
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

### Perceived difficulty Bernstein

The vector perception transform acts inside the hazard equation:

$$
z^C_{ijt}=\sum_k r_{jk}[\theta_{ik}-d_{jk}(x)],
\qquad
z^H_{ijt}=\sum_k r_{jk}[\theta_{ik}-\alpha_{ik}d_{jk}(x)+\beta_{ik}].
$$

This compares unconstrained alpha with the positive-alpha prior documented above.

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

Artifacts: [unconstrained](results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/unconstrained/configuration.json),
[positive `alpha`](results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/configuration.json), and
[three-slice `alpha,beta`](results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice/configuration.json).
Three-slice fold and pooled summaries are under
[`aggregate/`](results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice/aggregate/).

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

Artifacts: [alternating 3k](results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-alternating/configuration.json),
[alternating 10k](results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-alternating-10000-steps/configuration.json),
and [standard 10k](results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-10000-steps/configuration.json).

### Perceived logit Bernstein

The scalar player transform acts on the completed correctness logit:

$$
z^C_{ijt}=\sum_k r_{jk}[\theta_{ik}-d_{jk}(x)],
\qquad z^H_{ijt}=\alpha_i z^C_{ijt}+\beta_i.
$$

This compares unconstrained alpha with the positive-alpha prior documented above.

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

Artifacts: [unconstrained](results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/unconstrained/configuration.json),
[positive `alpha`](results/compirt/holdout/double-difficulty/variants/perception/perceived-logit/positive-alpha/configuration.json).

#### Unconstrained dimension and optimization-budget ablation

The [dimension/budget comparison](results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/aggregate/comparison.md)
links the complete [3,000-step grid](results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/aggregate/summary.md)
and the 10,000-step [logit](results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/perceived-logit-grid/aggregate/summary.md)
and [three-slice difficulty](results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/aggregate/summary.md)
follow-ups. These sweeps use unconstrained alpha: `Normal(1,1)` for scalar logit and independent
`Normal(0,1)` for each player/slice/dimension in three-slice difficulty.
Both use beta `Normal(0,1)`, degree 3, relevance/drop concentration 2, learning
rate 0.005, and the five `year_2024` game-holdout folds with split/optimizer
seed 42. The models differ in transform placement, prior and parameter count;
this is not a controlled comparison of slicing alone.

Select the smallest **tested** K within 1% of each grid's best pooled joint
event loss. Unlike the earlier fold-mean tables, the predictive scores below
are recomputed from pooled held-out rows.

| Model | Steps | Tested K | Selected K | Best K | Selected joint LL | Effective parameters | Accuracy | Neg F1 |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Scalar perceived logit | 3,000 | 1–10 | 6 | 10 | 7.69439 | 48,180 | 76.58% | 4.86% |
| Scalar perceived logit | 10,000 | 6, 8, 10 | 8 | 10 | 6.66725 | 63,690 | 71.73% | 33.36% |
| Three-slice perceived difficulty | 3,000 | 1–10 | 3 | 5 | 6.89727 | 48,195 | 76.71% | 16.54% |
| Three-slice perceived difficulty | 10,000 | 3, 5, 6 | 3 | 5 | 6.93492 | 48,195 | 76.78% | 20.91% |

At matched K=8, extending scalar-logit training reduces joint loss from
7.67617 to 6.66725 and position MAE from 0.32324 to 0.16586. Joint loss improves
in all five folds at each rerun K. However, correctness loss at K=8 increases
by 0.01251 and accuracy falls by 4.81 percentage points while neg F1 rises by
26.68 points. The 10,000-step K=8 selection is only 0.245% above K=10's best
loss of 6.65095. Mean fitted scalar alpha is 0.8954, with 22.05% of fitted
player alphas still negative; the final-100-step loss slope averages −0.630.

Longer three-slice training increases pooled joint loss at every rerun K:
by 0.03765 at K=3, 0.02709 at K=5, and 0.04836 at K=6. Only one of the 15
matched fold comparisons improves. Extra steps therefore do not explain
away this arm's held-out loss.

The sparse 10,000-step follow-ups do not establish the minimum adequate K
among dimensions that were not rerun. Logit's best loss is still at the grid
boundary. The tolerance is a capacity rule, not a statistical plateau test;
these same-fold selection scores require a separate test or nested selection
for an unbiased final estimate, and one optimizer seed does not establish
seed robustness.

### Hierarchical player neg propensity

The selected full DD-Bernstein 3/3/2 model was augmented with the zero-centered
player hierarchy in the [prior reference](#prior-reference) while retaining simplex relevance, learned
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

### Incorrect-response loss balancing and threshold equivalence

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

Artifacts: [1× baseline](results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/configuration.json),
[1.5× incorrect loss](results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-1.5/configuration.json),
[2× incorrect loss](results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-2/configuration.json),
and [3× incorrect loss](results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-3/configuration.json).

### Tossup ownership, game outcomes, and player leaderboards

The current [token-threshold comparison](#token-threshold-game-and-tournament-replay)
supersedes the previous integrated-probability and expected-point tables.
Every game is replayed tossup-only, from the first token through any eligible
opponent continuation, using 0.5 buzz/correctness thresholds and seeded random
ties. Player, team, game, round and tournament metrics share those same points.

Under this threshold policy, **DD-Bernstein 3/3/2 with terminal intercepts**
leads the 15 saved arms on the reported direct-scoring, round and PPG metrics:
**69.27%** tossup-winner accuracy, **48.33 points** margin MAE, **0.8305** tournament PPG rank correlation, and
**6.43 points/game** PPG MAE. These are comparisons under the requested
threshold policy, not a new fit or evidence of superiority on other tasks.

## Limits and next experiments

The main unresolved issues are repeated development-fold selection, one
optimization seed per historical arm, incomplete
matched ablations, and limited season coverage. Bootstrap intervals conditional
on saved predictions do not cover training randomness, model search, or
dependence across games sharing questions. Stage-1 results do not
establish bonus prediction, PPB, synergy, future-season skill transfer or match
simulation performance. Model selection should consider the timing distribution,
first-buzzer identity, conditional correctness and joint event scores together;
correctness accuracy alone does not establish a better tossup model.

The token-threshold replay covers 2,331 of 2,332 held-out games (the filtered
season has 2,431); one game whose saved predictions are missing a tossup is
excluded. Opponent continuations reuse phase-0 fitted hazards because
these historical models were trained without a separate bounceback likelihood.
Terminal misses score zero; predicted ties remain ties, with no overtime model.
High replay no-buzz and tie rates are visible above and materially affect
winner accuracy. A 0.5 per-token decision policy is a different prediction task
from evaluating an integrated event distribution, so its numbers cannot inherit
the previous model ordering or probability-calibration claims.

1. Refit the saved DD reference under the normalized likelihood with multiple
   seeds and explicit optimization budgets.
2. Validate DD-Bernstein on an independent season or nested outer test,
   measuring timing, identity, correctness and joint event scores. Test whether
   player representations transfer beyond same-item infill.
3. Complete the second-season terminal comparison; replicate Gamma + terminal,
   both simplex terminal arms, and the unconstrained spline across seeds.
4. Preserve the earlier controls: retrain single-curve baselines under matched
   survival/prior/learning-rate/checkpoint conventions, and replicate standard
   versus alternating three-slice 10k fits if that family is pursued again.

Reproduction: [CompIRT experiment commands](docs/compirt-experiments.md).
