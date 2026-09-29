# CompIRT research log II: bonuses

_Updated 2026-09-27. Companion to the [tossup research log](RESEARCH_LOG.md)._

All current bonus models are compared together below: **DD-Bernstein**, **Noisy-OR**,
**maximum skill per dimension** with and without synergy,
**DD-Bernstein + synergy**, the multidimensional-difficulty variant,
multidimensional references, **Team IRT 1D and 3D**, and the dot/phi-psi
additive and multiplicative synergy experiments. The [shared comparison][comparison]
contains the seven-model matched scores; [Noisy-OR][noisy-or] and
[maximum skill][max-skill] use the same matched population.
The additional synergy results use the same skills but
retain their saved populations.

The [full-season difficulty comparison](#full-season-bonus-difficulty-ordering)
uses 2024–25 fits to check the ordering of easy, medium, and hard parts and
the expected increase in difficulty from ACF Fall to Nationals.

## Models and common protocol

**DD-Bernstein** uses frozen 3D player skills from the normalized first-buzz
tossup model: degree-3 Bernstein correctness and hazard curves, drop
concentration 2, simplex relevance, learned curve locations, and terminal
intercepts. Every DD row below uses these skills.

For player skill $\widehat\theta_i$, bonus part $b$, and active roster $R$,
the compositional model uses

$$
u_{ib}=\alpha_b^\top\widehat\theta_i,\qquad
A_b(R)=\tau\log\sum_{i\in R}\exp(u_{ib}/\tau),\qquad
P(Y_{Rb}=1)=\sigma[A_b(R)-\beta_b+s(R)].
$$

The base model sets $s=0$. **DD-Bernstein + synergy** adds
$s(R)=\sum_{i<j\in R}\psi_i\psi_j$, using one scalar profile per player.
Skills remain frozen while bonus weights, difficulty, temperature, and synergy
are learned. Aggregation is unnormalized: $n$ identical players with ability
$u$ give $A=u+\tau\log n$.

**DD-Bernstein, Noisy-OR** implements the paper's Eq. 9 independent-knowledge
baseline with the same frozen DD skills:

$$
P(Y_{Rb}=1)=1-\prod_{i\in R}\left[1-\sigma(
\alpha_b^\top\widehat\theta_i-\beta_b)\right].
$$

Difficulty enters each member's probability before pooling. Alpha uses the
matched Gamma(2,2) prior and scalar beta uses Normal(0,1); these are the only
fitted parameters. It uses the same five folds,
3,000 AutoNormal SVI steps, learning rate 0.01, and seed 42 as the DD rows.

**Maximum skill per dimension** replaces LSE pooling with
$m_k(R)=\max_{i\in R}\widehat\theta_{ik}$ and uses
$P(Y_{Rb}=1)=\sigma[\sum_k\alpha_{bk}m_k(R)-\beta_b+s(R)]$.
Each coordinate can come from a different active teammate; selection is before
part weighting. The two variants set $s=0$ or use the same additive dot 1D
synergy as DD-Bernstein + synergy. Scalar difficulty, Gamma loading priors,
frozen skills, folds, training steps, learning rate, and seed match the LSE rows.

The synergy forms and links are separate choices:

$$
s_{\mathrm{dot}}(R)=\sum_d\sum_{i<j\in R}\psi_{id}\psi_{jd},\qquad
s_{\phi\psi}(R)=\sum_d\sum_{i<j\in R}
\phi_{id}\phi_{jd}(\psi_{id}+\psi_{jd}).
$$

**Additive** uses $\eta=A-\beta+s$; **multiplicative** uses
$\eta=(A-\beta)(1+s)$, with an unconstrained multiplier.
**DD-Bernstein + synergy is the additive dot (psi) 1D model.** The additional
experiments use additive phi-psi and multiplicative dot and phi-psi, each in 1D
and 3D. Phi-psi uses $\phi_{id}\sim N(0,1)$ and $\psi_{id}\sim N(0,0.5)$
(variance notation).

The **multidimensional-difficulty** variant pools teammates separately on each
skill axis before applying positive relevance weights:

$$
\eta=\sum_k r_{bk}\left[\tau\log\sum_{i\in R}
\exp(\widehat\theta_{ik}/\tau)-\beta_{bk}\right]+s(R).
$$

It changes pooling as well as difficulty and uses additive dot synergy in 1D
(matched rows) or 3D; there is no matching run without synergy. The older **multidimensional** reference
uses 5D player skills, Normal bonus weights, and rank-3 synergy. DD bonus
weights use a Gamma(2,2) shape/rate prior. Both use Normal(0,1) scalar difficulty,
HalfCauchy(1) temperature, and Normal(0,0.5) synergy profiles.

**Team IRT 1D and 3D** learn a free skill vector for each tournament-specific
team directly from training bonuses:

$$
\text{1D: } P(Y_{tb}=1)=\sigma(\alpha_b\theta_t-\beta_b),\quad
\alpha_b\sim\operatorname{Gamma}(2,2);\qquad
\text{3D: } P(Y_{tb}=1)=\sigma\Big[\sum_k r_{bk}(\theta_{tk}-\beta_{bk})\Big],\quad
r_b\sim\operatorname{Dirichlet}(1,1,1),
$$

with $\theta_{tk},\beta_{bk}\sim N(0,1)$. The 3D arm has per-dimension
difficulty and simplex relevance ($\sum_k r_{bk}=1$); it replaced the earlier
$\sigma(\theta_t^\top\alpha_b-\beta_b)$ 3D arm on 2026-09-25. They use no tossup
skills, roster pooling, or synergy. Team and part parameters are frozen at
their training posterior medians for held-out prediction.

For the held-out comparison, all models use the same five `year_2024`
whole-game folds, split and optimization
seed 42. DD bonus and team-IRT fits use 3,000 AutoNormal SVI steps at learning
rate 0.01; the multidimensional references use 2,000 steps. No correctness
calibration is applied. The comparison reuses saved predictions without training.

The seven original matched rows, Noisy-OR, and both maximum-skill variants score
**127,986 parts / 42,662 bonuses / 2,330 games / 450 teams /
29 tournaments**. Whole games with missing predictions or unseen training
teams/parts are excluded for every model. Compared with the compositional-only
population, two Regionals MIT games (38 bonuses) are excluded for team-IRT
training coverage. One retained team heard zero bonuses and still contributes
to game-level denominators. These are reused development folds with familiar
entities, not an untouched test or an unseen-team transfer experiment.

## Results

Pooled held-out scores:

| Model | AUC ↑ | Log loss ↓ | Part accuracy ↑ | Exact bonus accuracy ↑ | Team PPB MAE ↓ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Multidimensional | 0.88811 | 0.42271 | 80.83% | 51.22% | 2.045 |
| Multidimensional + synergy | 0.89548 | 0.41127 | 81.39% | 52.44% | 1.176 |
| DD-Bernstein | 0.89043 | 0.41832 | 80.84% | 51.17% | 1.977 |
| DD-Bernstein + synergy | 0.89812 | 0.40492 | 81.66% | 52.94% | 0.945 |
| DD-Bernstein, Noisy-OR | 0.89070 | 0.41737 | 80.82% | 51.22% | 1.938 |
| DD-Bernstein, max skill | 0.88739 | 0.42364 | 80.76% | 51.11% | 1.964 |
| DD-Bernstein, max skill + synergy | 0.89622 | 0.40850 | 81.79% | 53.28% | 0.785 |
| DD-Bernstein, multidimensional difficulty + synergy | 0.89884 | 0.40202 | 81.74% | 53.33% | 0.740 |
| DD-Bernstein, additive phi-psi 1D | 0.89766 | 0.40536 | 81.65% | 52.91% | 1.062 |
| DD-Bernstein, additive phi-psi 3D | 0.89774 | 0.40536 | 81.70% | 53.03% | 1.034 |
| DD-Bernstein, multiplicative dot 1D | 0.89017 | 0.41843 | 80.82% | 51.06% | 1.959 |
| DD-Bernstein, multiplicative dot 3D | 0.89014 | 0.41860 | 80.83% | 51.11% | 1.951 |
| DD-Bernstein, multiplicative phi-psi 1D | 0.89046 | 0.41772 | 80.91% | 51.25% | 1.957 |
| DD-Bernstein, multiplicative phi-psi 3D | 0.89034 | 0.41779 | 80.91% | 51.31% | 1.958 |
| DD-Bernstein, multidimensional difficulty + 3D synergy | 0.89889 | 0.40231 | 81.77% | 53.32% | 0.746 |
| Team IRT 1D | 0.90365 | 0.39783 | **82.24%** | 54.19% | 0.580 |
| Team IRT 3D | **0.90367** | **0.39385** | 82.22% | **54.22%** | **0.464** |

Difficulty accuracy and bonus-only team/game outcomes. Each difficulty contains
42,662 parts and game metrics use 2,330 games for the matched rows.

| Model | Easy acc. ↑ | Medium acc. ↑ | Hard acc. ↑ | Team PPG MAE ↓ | Tournament Spearman ↑ | Normalized inversions ↓ | Bonus margin MAE ↓ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Multidimensional | 90.76% | 67.81% | 83.92% | 18.856 | 0.9585 | 0.0536 | 32.138 |
| Multidimensional + synergy | 90.03% | 69.85% | 84.30% | 11.072 | 0.9702 | 0.0421 | 26.691 |
| DD-Bernstein | 90.61% | 68.05% | 83.85% | 18.059 | 0.8898 | 0.1110 | 33.210 |
| DD-Bernstein + synergy | 90.74% | 70.01% | 84.23% | 8.343 | 0.9374 | 0.0566 | 26.538 |
| DD-Bernstein, Noisy-OR | 90.29% | 68.22% | 83.96% | 17.975 | 0.8897 | 0.1109 | 33.559 |
| DD-Bernstein, max skill | 90.26% | 68.29% | 83.73% | 18.571 | 0.8797 | 0.1148 | 35.842 |
| DD-Bernstein, max skill + synergy | 90.67% | 70.27% | 84.41% | 7.316 | 0.9399 | 0.0581 | 26.492 |
| DD-Bernstein, multidimensional difficulty + synergy | 90.26% | 70.46% | 84.50% | 6.852 | 0.9449 | 0.0507 | 25.740 |
| DD-Bernstein, additive phi-psi 1D | 90.72% | 69.90% | 84.34% | 9.282 | 0.9358 | 0.0618 | 26.899 |
| DD-Bernstein, additive phi-psi 3D | 90.74% | 69.96% | 84.41% | 9.208 | 0.9327 | 0.0659 | 26.781 |
| DD-Bernstein, multiplicative dot 1D | 90.62% | 68.00% | 83.83% | 17.973 | 0.8851 | 0.1142 | 33.358 |
| DD-Bernstein, multiplicative dot 3D | 90.59% | 68.07% | 83.81% | 17.974 | 0.8843 | 0.1152 | 33.450 |
| DD-Bernstein, multiplicative phi-psi 1D | 90.65% | 68.18% | 83.90% | 18.016 | 0.8839 | 0.1150 | 33.219 |
| DD-Bernstein, multiplicative phi-psi 3D | 90.66% | 68.19% | 83.89% | 18.048 | 0.8839 | 0.1153 | 33.357 |
| DD-Bernstein, multidimensional difficulty + 3D synergy | 90.30% | 70.55% | 84.45% | 6.874 | 0.9432 | 0.0527 | 25.762 |
| Team IRT 1D | 91.15% | 70.97% | **84.62%** | 4.814 | 0.9916 | 0.0153 | 22.843 |
| Team IRT 3D | **91.18%** | **70.99%** | 84.49% | **3.600** | **0.9954** | **0.0106** | **22.764** |

For tournament $t$ with $n_t$ teams, the normalized inversion rate compares
the observed bonus-PPG ranking $r$ with the model ranking $\widehat r$:

$$
I_t=\frac{1}{\binom{n_t}{2}}\sum_{i<j}
\mathbf{1}\!\left[(r_i-r_j)(\widehat r_i-\widehat r_j)<0\right].
$$

A pair contributes one when its order is reversed and zero otherwise. A tie in
either ranking is not an inversion. The table reports the equal-weight mean of
$I_t$ over the 29 tournaments. Thus 0 is perfect agreement and 1 is complete
reversal when neither ranking has ties.

The always-predict-correct baseline is 90.93% easy, 49.34% medium, and 16.21%
hard. Hard-part accuracy therefore needs particular care: always predicting a
miss already gives 83.79% accuracy.

### Overall part classification

Correct (1) is the positive class. The model predicts a correct response when
its probability `p >= 0.5`. **TP** counts correct responses predicted as
correct; **TN** counts incorrect responses predicted as incorrect.
**FN** counts correct responses predicted as incorrect; **FP** counts
incorrect responses predicted as correct. Each count represents one team's
response to one bonus part, so a question heard several times contributes
several observations.

Counts are pooled across the five held-out folds before calculating precision
`P = TP / (TP + FP)`, recall `R = TP / (TP + FN)`, and
`F1 = 2 TP / (2 TP + FP + FN)`. Precision measures how often a predicted
correct response was actually correct; recall measures how many of the
observed correct responses the model identified. F1 combines precision and
recall through their harmonic mean. All three scores range from 0 to 1.
Bold marks the highest precision, recall, and F1.

| Model | TP | TN | FN | FP | Overall precision ↑ | Overall recall ↑ | Overall F1 ↑ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Multidimensional | 52,028 | 51,421 | 14,731 | 9,806 | 0.8414 | 0.7793 | 0.8092 |
| Multidimensional + synergy | 52,073 | 52,098 | 14,686 | 9,129 | **0.8508** | 0.7800 | 0.8139 |
| DD-Bernstein | 54,572 | 48,886 | 12,187 | 12,341 | 0.8156 | 0.8174 | 0.8165 |
| DD-Bernstein + synergy | 55,558 | 48,956 | 11,201 | 12,271 | 0.8191 | **0.8322** | 0.8256 |
| DD-Bernstein, Noisy-OR | 53,302 | 50,140 | 13,457 | 11,087 | 0.8278 | 0.7984 | 0.8129 |
| DD-Bernstein, max skill | 53,339 | 50,021 | 13,420 | 11,206 | 0.8264 | 0.7990 | 0.8125 |
| DD-Bernstein, max skill + synergy | 54,646 | 50,028 | 12,113 | 11,199 | 0.8299 | 0.8186 | 0.8242 |
| DD-Bernstein, multidimensional difficulty + synergy | 53,823 | 50,793 | 12,936 | 10,434 | 0.8376 | 0.8062 | 0.8216 |
| DD-Bernstein, additive phi-psi 1D | 55,164 | 49,434 | 11,654 | 11,848 | 0.8232 | 0.8256 | 0.8244 |
| DD-Bernstein, additive phi-psi 3D | 55,222 | 49,438 | 11,596 | 11,844 | 0.8234 | 0.8265 | 0.8249 |
| DD-Bernstein, multiplicative dot 1D | 54,396 | 49,131 | 12,422 | 12,151 | 0.8174 | 0.8141 | 0.8157 |
| DD-Bernstein, multiplicative dot 3D | 54,357 | 49,180 | 12,461 | 12,102 | 0.8179 | 0.8135 | 0.8157 |
| DD-Bernstein, multiplicative phi-psi 1D | 54,414 | 49,233 | 12,404 | 12,049 | 0.8187 | 0.8144 | 0.8165 |
| DD-Bernstein, multiplicative phi-psi 3D | 54,335 | 49,317 | 12,483 | 11,965 | 0.8195 | 0.8132 | 0.8163 |
| DD-Bernstein, multidimensional difficulty + 3D synergy | 54,099 | 50,647 | 12,719 | 10,635 | 0.8357 | 0.8096 | 0.8225 |
| Team IRT 1D | 54,331 | 50,930 | 12,428 | 10,297 | 0.8407 | 0.8138 | 0.8270 |
| Team IRT 3D | 54,603 | 50,628 | 12,156 | 10,599 | 0.8374 | 0.8179 | **0.8276** |

For example, DD-Bernstein's precision of 0.8156 means that 81.56% of the
responses it predicted as correct were correct. Its recall of 0.8174 means
that it identified 81.74% of all observed correct responses.

The four counts sum to **127,986 observed part responses** for each matched
model and **128,100** for each of the seven additional synergy variants.
The difference is 38 bonus responses (114 parts) from the two games excluded
by the matched comparison. Overall F1 uses correct as positive across all
difficulties. The next table changes the positive class by difficulty, so
averaging its F1 values would give a different quantity.

**Classification by declared difficulty (minority class as positive)**, calculated from saved held-out
part predictions pooled across the five folds, with predicted correctness
thresholded at `p >= 0.5`. The minority class is **incorrect (0) for easy**
and **correct (1) for medium and hard**. Precision is `TP / (TP + FP)`,
recall is `TP / (TP + FN)`, and F1 is `2 TP / (2 TP + FP + FN)`,
treating that minority class as positive. Counts are pooled before computing
these ratios; scores are on a 0–1 scale. Each cell lists **precision / recall / F1**;
bold marks the highest F1 in each difficulty.

| Model | Easy P / R / F1 ↑ | Medium P / R / F1 ↑ | Hard P / R / F1 ↑ |
| --- | ---: | ---: | ---: |
| Multidimensional | 0.4699 / 0.1494 / 0.2267 | 0.6968 / 0.6151 / 0.6534 | 0.5157 / 0.1358 / 0.2149 |
| Multidimensional + synergy | 0.4246 / 0.2807 / **0.3379** | 0.7203 / 0.6358 / 0.6754 | 0.5437 / 0.1979 / 0.2902 |
| DD-Bernstein | 0.4346 / 0.1194 / 0.1873 | 0.6680 / 0.7006 / 0.6839 | 0.5043 / 0.2362 / 0.3217 |
| DD-Bernstein + synergy | 0.4647 / 0.1360 / 0.2104 | 0.6834 / 0.7306 / **0.7062** | 0.5249 / 0.2880 / **0.3719** |
| DD-Bernstein, Noisy-OR | 0.4088 / 0.1582 / 0.2281 | 0.6837 / 0.6621 / 0.6727 | 0.5130 / 0.2106 / 0.2987 |
| DD-Bernstein, max skill | 0.4076 / 0.1636 / 0.2335 | 0.6858 / 0.6594 / 0.6723 | 0.4961 / 0.2294 / 0.3138 |
| DD-Bernstein, max skill + synergy | 0.4629 / 0.1791 / 0.2583 | 0.6985 / 0.6994 / 0.6989 | 0.5372 / 0.2797 / 0.3679 |
| DD-Bernstein, multidimensional difficulty + synergy | 0.4257 / 0.2132 / 0.2841 | 0.7092 / 0.6802 / 0.6944 | 0.5458 / 0.2638 / 0.3557 |
| DD-Bernstein, additive phi-psi 1D | 0.4595 / 0.1362 / 0.2101 | 0.6871 / 0.7160 / 0.7013 | 0.5332 / 0.2702 / 0.3586 |
| DD-Bernstein, additive phi-psi 3D | 0.4625 / 0.1370 / 0.2113 | 0.6875 / 0.7171 / 0.7020 | 0.5372 / 0.2745 / 0.3634 |
| DD-Bernstein, multiplicative dot 1D | 0.4383 / 0.1248 / 0.1943 | 0.6708 / 0.6902 / 0.6803 | 0.5026 / 0.2377 / 0.3227 |
| DD-Bernstein, multiplicative dot 3D | 0.4372 / 0.1323 / 0.2031 | 0.6722 / 0.6886 / 0.6803 | 0.5012 / 0.2426 / 0.3269 |
| DD-Bernstein, multiplicative phi-psi 1D | 0.4429 / 0.1233 / 0.1928 | 0.6730 / 0.6907 / 0.6818 | 0.5073 / 0.2358 / 0.3220 |
| DD-Bernstein, multiplicative phi-psi 3D | 0.4486 / 0.1320 / 0.2040 | 0.6739 / 0.6882 / 0.6810 | 0.5067 / 0.2361 / 0.3221 |
| DD-Bernstein, multidimensional difficulty + 3D synergy | 0.4283 / 0.2093 / 0.2812 | 0.7073 / 0.6877 / 0.6974 | 0.5411 / 0.2690 / 0.3594 |
| Team IRT 1D | 0.5408 / 0.1577 / 0.2441 | 0.7117 / 0.6919 / 0.7016 | 0.5672 / 0.2158 / 0.3127 |
| Team IRT 3D | 0.5423 / 0.1773 / 0.2672 | 0.7101 / 0.6964 / 0.7032 | 0.5475 / 0.2501 / 0.3434 |

Populations match the accuracy table above: the seven original matched models,
Noisy-OR, and both maximum-skill variants have
42,662 parts per difficulty, with minority counts of 3,869 easy misses,
21,049 medium correct answers, and 6,917 hard correct answers. The seven
additional synergy variants retain 42,700 parts per difficulty, with respective
minority counts of 3,870, 21,067, and 6,921. To reproduce, use the saved
`fold_N/holdout/{compositional,synergy}/bonus_part_predictions.csv` files
(or `fold_N/team_irt_{1d,3d}/bonus_part_predictions.csv` for Team IRT), restrict
matched models to each comparison `fold_N/split.json`'s `scored_game_ids`,
and join source difficulty labels by `bonus_id` and zero-based `part_index`.
The [comparison configuration](results/compirt/comparisons/bonuses/dd-bernstein-and-team-irt-5fold/configuration.json)
and [saved run index][runs] identify the source runs.

Roster familiarity splits the matched population, including Noisy-OR and maximum skill, into
40,531 familiar-roster bonuses and 2,131 new-roster bonuses. For the additional
synergy rows the counts are 40,549 and 2,151:

| Model | Familiar AUC ↑ | Familiar log loss ↓ | Familiar part acc. ↑ | New AUC ↑ | New log loss ↓ | New part acc. ↑ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Multidimensional | 0.88804 | 0.42289 | 80.80% | 0.88906 | 0.41939 | 81.34% |
| Multidimensional + synergy | 0.89682 | 0.40946 | 81.48% | 0.87509 | 0.44581 | 79.70% |
| DD-Bernstein | 0.89052 | 0.41810 | 80.82% | 0.88819 | 0.42250 | 81.07% |
| DD-Bernstein + synergy | 0.89876 | 0.40371 | 81.68% | 0.88693 | 0.42797 | 81.20% |
| DD-Bernstein, Noisy-OR | 0.89076 | 0.41709 | 80.81% | 0.88908 | 0.42273 | 81.12% |
| DD-Bernstein, max skill | 0.88718 | 0.42389 | 80.73% | 0.89079 | 0.41894 | 81.28% |
| DD-Bernstein, max skill + synergy | 0.89697 | 0.40720 | 81.81% | 0.88398 | 0.43333 | 81.32% |
| DD-Bernstein, multidimensional difficulty + synergy | 0.89931 | 0.40090 | 81.76% | 0.88961 | 0.42341 | 81.40% |
| DD-Bernstein, additive phi-psi 1D | 0.89821 | 0.40426 | 81.67% | 0.88780 | 0.42619 | 81.28% |
| DD-Bernstein, additive phi-psi 3D | 0.89823 | 0.40436 | 81.72% | 0.88926 | 0.42410 | 81.39% |
| DD-Bernstein, multiplicative dot 1D | 0.89022 | 0.41819 | 80.80% | 0.88853 | 0.42305 | 81.13% |
| DD-Bernstein, multiplicative dot 3D | 0.89018 | 0.41834 | 80.80% | 0.88895 | 0.42338 | 81.33% |
| DD-Bernstein, multiplicative phi-psi 1D | 0.89053 | 0.41754 | 80.90% | 0.88857 | 0.42116 | 81.08% |
| DD-Bernstein, multiplicative phi-psi 3D | 0.89041 | 0.41762 | 80.91% | 0.88857 | 0.42089 | 80.97% |
| DD-Bernstein, multidimensional difficulty + 3D synergy | 0.89931 | 0.40124 | 81.78% | 0.89098 | 0.42256 | 81.56% |
| Team IRT 1D | 0.90369 | 0.39784 | **82.23%** | **0.90277** | 0.39763 | 82.42% |
| Team IRT 3D | **0.90373** | **0.39375** | 82.21% | 0.90202 | **0.39573** | **82.45%** |

## Full-season bonus difficulty ordering

We fitted all 17 bonus models on the **complete 2024–25 ACF season**, from
Fall (2024-10-19) and Winter (2024-11-16) through Regionals
(2025-02-01) and Nationals (2025-04-19). The local data cover 33 mirror sites,
2,661 games, and 49,042 bonus responses. This section examines the parameters
fitted to those games. The classification tables above use held-out games
from calendar year 2024, which combines parts of two seasons.

The [season run](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/README.md)
fits DD and multidimensional tossup models on the whole season, then freezes
their player skills for the 15 compositional bonus variants. Team IRT 1D and
3D are fitted directly to the season's bonuses. All fits use seed 42.
Both tossup fits use 3,000 steps (DD learning rate 0.005; multidimensional
0.01); DD bonus and Team IRT fits use
3,000 steps at 0.01, and the two multidimensional bonus references use 2,000
steps at 0.01. Model forms and priors follow the earlier comparison.

### Expected tournament difficulty

ACF describes [Fall as an introductory easy tournament](https://acf-quizbowl.com/tournaments/fall/2024/),
[Winter as halfway between Fall and Regionals](https://acf-quizbowl.com/tournaments/winter/2024/),
[Regionals as preparation for Nationals difficulty](https://acf-quizbowl.com/tournaments/regionals/2025/),
and [Nationals as the season's hardest set](https://acf-quizbowl.com/tournaments/nationals/2025/).
The expected tournament difficulty order is therefore
**Fall < Winter < Regionals < Nationals**. A mirror is a site where teams play
the same question set; the 33 sites here represent four sets. Easy, medium,
and hard describe parts within a set, so an easy Nationals part can be harder
than an easy Fall part.

We check this expected order separately for average easy, medium, and hard
difficulty. ACF's descriptions give the broad order of the sets, without
specifying how large the gaps should be for each part type.

The observed **conversion rate** is the percentage of part responses that
were correct. **PPB** is the average points scored per bonus, out of 30.
A distinct bonus is one question; a bonus response is one occasion when a
team heard it.

| Question set | Sites | Distinct bonuses heard | Bonus responses | Easy correct | Medium correct | Hard correct | Points per bonus |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Fall 2024 | 8 | 280 | 14,112 | 94.47% | 60.74% | 24.45% | 17.965 |
| Winter 2024 | 10 | 299 | 14,104 | 91.51% | 47.29% | 14.75% | 15.356 |
| Regionals 2025 | 14 | 320 | 13,232 | 89.11% | 41.24% | 11.46% | 14.182 |
| Nationals 2025 | 1 | 397 | 7,594 | 94.25% | 48.91% | 9.40% | 15.255 |

These rates pool observed responses within each question set. Easy conversion
exceeds medium, and medium exceeds hard, at **all 33 sites**. Across the four tiers,
hard-part conversion declines from Fall to Nationals. For easy
and medium parts, conversion is highest at Fall, then Nationals, Winter, and
Regionals. The same orders hold when weighting distinct questions equally or
mirror sites equally.

Winter's writing guidance targets 90%/50%/10% conversion for easy/medium/hard.
In the local data, easy conversion is 1.51 percentage points above target,
medium is 2.71 points below, and hard is 4.75 points above. These targets
refer to the teams expected to play Winter. [ACF Winter writing guidance](https://acf-quizbowl.com/tournaments/winter/2024/)

### Agreement with declared bonus difficulty

For each bonus part, use **$D=d$ for scalar difficulty** and
**$D=r^\top d=\sum_k r_kd_k$ for per-dimension difficulty**, evaluated at the
saved parameter medians. The saved names are `beta` or `beta_k`, and `r_k`.
$D$ is the difficulty term subtracted from the skill contribution. Negative
values are valid: −1 is a higher difficulty than −2. Its scale depends on the
model, so compare values within a model. Use relevance weights as fitted;
for multiplicative synergy, $D$ is measured before applying the roster
multiplier.

For each distinct bonus $j$, define

$$
O_j=\begin{cases}
1,&D_{j,\mathrm{easy}}<D_{j,\mathrm{medium}}<D_{j,\mathrm{hard}},\\
0,&\text{otherwise}.
\end{cases}
$$

Ties or either reversal score zero. Labels come from the source metadata,
independently of part position. **Ordering accuracy** is the fraction of
distinct bonuses with score 1. Each question counts once, however often it
was heard. Predicted correctness also depends on how the part's weights
interact with team skills, so ordering $D$ alone does not fix the order of
predicted probabilities.

All 17 fits cover the same **1,296 distinct bonus questions**, each with one
easy, one medium, and one hard part: **3,888 distinct parts** in total.
The 49,042 occasions on which teams heard these bonuses provide **147,126
observed part responses**. No rosters were excluded. Another 63 bonuses in
the source were never heard and have no fitted parameters. The
[per-bonus table](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/bonus_difficulty_order.csv)
records the three difficulties and the 0/1 score for each model and bonus.

The last three columns average difficulty across the season. Within each site,
we average the distinct parts heard there by label, then give each of the
33 sites equal weight. **Every model has mean easy < medium < hard at all
33 sites and all four question sets.**

| Model | Bonuses in expected order | Bonuses out of order | Ordering accuracy ↑ | Mean $D$: easy | Mean $D$: medium | Mean $D$: hard |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Multidimensional | 1,166 | 130 | 0.8997 | -1.044 | 1.164 | 2.375 |
| Multidimensional + synergy | 1,166 | 130 | 0.8997 | -1.604 | 0.631 | 2.077 |
| DD-Bernstein | 1,146 | 150 | 0.8843 | -1.773 | -0.208 | 0.964 |
| DD-Bernstein + synergy | 1,131 | 165 | 0.8727 | -1.703 | -0.205 | 0.948 |
| DD-Bernstein, Noisy-OR | 1,143 | 153 | 0.8819 | -1.755 | -0.484 | 0.680 |
| DD-Bernstein, max skill | 1,180 | 116 | 0.9105 | -2.658 | -0.410 | 1.346 |
| DD-Bernstein, max skill + synergy | 1,181 | 115 | **0.9113** | -2.462 | -0.227 | 1.516 |
| DD-Bernstein, multidimensional difficulty + synergy | 1,174 | 122 | 0.9059 | -3.818 | -0.272 | 1.869 |
| DD-Bernstein, additive phi-psi 1D | 1,127 | 169 | 0.8696 | -1.688 | -0.190 | 0.953 |
| DD-Bernstein, additive phi-psi 3D | 1,132 | 164 | 0.8735 | -1.710 | -0.193 | 0.962 |
| DD-Bernstein, multiplicative dot 1D | 1,129 | 167 | 0.8711 | -1.760 | -0.176 | 0.950 |
| DD-Bernstein, multiplicative dot 3D | 1,124 | 172 | 0.8673 | -1.748 | -0.165 | 0.932 |
| DD-Bernstein, multiplicative phi-psi 1D | 1,129 | 167 | 0.8711 | -1.760 | -0.177 | 0.955 |
| DD-Bernstein, multiplicative phi-psi 3D | 1,128 | 168 | 0.8704 | -1.750 | -0.169 | 0.942 |
| DD-Bernstein, multidimensional difficulty + 3D synergy | 1,171 | 125 | 0.9035 | -3.787 | -0.211 | 1.958 |
| Team IRT 1D | 1,177 | 119 | 0.9082 | -2.150 | 0.167 | 1.791 |
| Team IRT 3D | 1,125 | 171 | 0.8681 | -1.202 | 0.067 | 1.047 |

For example, maximum skill + synergy orders 1,181 of 1,296 bonuses correctly:
1,181 / 1,296 ≈ 0.9113, or 91.13%. Across models, ordering accuracy ranges
from **86.73% to 91.13%**. All site averages follow the expected order even
though some individual bonuses do not.

### How certain are the individual bonus orderings?

This check uses **DD-Bernstein, multidimensional difficulty + synergy**, the
fit examined in the [bonus interpretation study](dd_model_interpretation/bonus/README.md).
Its original score stays **1,174 / 1,296 = 90.6%**. The uncertainty results
below apply to this model only.

**Size of the gaps.** For each bonus, subtract easy difficulty from medium
($D_m-D_e$), and medium from hard ($D_h-D_m$). Positive means the pair is in
the expected order; negative means it is reversed. Across bonuses, the median
gaps are **3.21** and **2.09**, respectively, on this model's difficulty
scale. A gap near zero means the fitted difficulties are almost tied.

**Probability of the expected order.** The fitted model stores uncertainty
about its parameters. We draw 20,000 plausible sets of relevance and difficulty
values for each bonus, calculate $D=r^\top d$ each time, and count how often
easy < medium < hard holds. For example, 90% means the expected order holds
in about nine out of ten draws from the fitted model. This measures support
for the parameter ordering, not the chance that a team answers correctly.

Of the **122 bonuses with a reversed point estimate**, only **9** have an
estimated probability of the expected order at or below 5%. The other 113
do not meet that threshold for strong evidence of a reversal. Two examples
show why the gap and its uncertainty matter:

| Bonus | Times heard | Hard − medium gap | 95% interval for that gap | Probability of full easy < medium < hard order |
| --- | ---: | ---: | --- | ---: |
| Fall, packet 44, bonus 8: Phoenician (medium), Aramaic (hard) | 54 | −0.02 | −1.92 to +1.87 | 48.9% |
| Fall, packet 39, bonus 16: Puerto Rico (medium), Taíno (hard) | 56 | −1.79 | −3.79 to −0.36 | 0.8% |

Each interval contains the middle 95% of sampled gap values. These are
approximate model-based intervals from the saved mean-field fit, conditional
on frozen player skills; they omit parameter correlations and variation
across training seeds.

**Bonuses with few attempts.** One attempt means one team heard the bonus;
its three part responses count as one attempt. Group the existing fitted
bonuses by that count and recompute the original 0/1 ordering rate:

| Times heard | Distinct bonuses | Bonuses in expected order | Ordering rate |
| --- | ---: | ---: | ---: |
| 1–9 | 91 | 53 | 58.2% |
| 10–19 | 138 | 127 | 92.0% |
| 20–29 | 364 | 337 | 92.6% |
| 30 or more | 703 | 657 | 93.5% |

Excluding the 91 bonuses heard fewer than ten times from the summary raises
the rate from **90.6% to 93.0%** (1,121 / 1,205). Their gap estimates are also
less precise: the median 95% interval width for hard − medium is **10.79**
for 1–9 attempts, compared with **4.16** for 30 or more.

Question sets differ in exposure, so we also checked within each set. The
lower rate below ten attempts appears in Fall, Winter, and Nationals;
Regionals is the exception, with all ten low-attempt bonuses ordered correctly.
These are descriptive comparisons of subsets of the same fit. No responses
were removed for training, and this does not estimate what would happen after
collecting more responses and refitting.

The [per-bonus values](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/bonus_difficulty_uncertainty.csv),
[attempt groups within each set](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/bonus_difficulty_uncertainty_by_attempts.csv),
and [calculation record](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/bonus_difficulty_uncertainty_method.json)
retain the gaps, intervals, probabilities, counts, and sampling details.

### Average difficulty by tournament

Each question-set cell lists **mean easy / medium / hard $D$**. Here each
distinct part counts once across all sites playing the set. This differs from
the previous table, which gives each site equal weight.

The expected order is **Fall < Winter < Regionals < Nationals**, where higher
mean $D$ means harder. Four sets have $4 \times 3 / 2 = 6$ distinct pairs:
**Fall < Winter, Fall < Regionals, Fall < Nationals, Winter < Regionals,
Winter < Nationals, and Regionals < Nationals**. The final column counts how
many of these inequalities hold separately for **(easy, medium, hard)**.
For example, **(5, 6, 6)** means one comparison fails for easy parts and all
six pass for medium and hard parts. Comparisons use unrounded means, and
ties count as disagreements.

| Model | Fall 2024: E / M / H | Winter 2024: E / M / H | Regionals 2025: E / M / H | Nationals 2025: E / M / H | Matching pairs (E, M, H), out of 6 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Multidimensional | -1.392 / 0.507 / 1.860 | -1.077 / 1.214 / 2.415 | -0.751 / 1.357 / 2.443 | -0.844 / 0.716 / 1.979 | (5, 4, 4) |
| Multidimensional + synergy | -1.591 / 0.315 / 1.855 | -1.646 / 0.683 / 2.118 | -1.442 / 0.695 / 2.011 | -1.152 / 0.311 / 1.652 | (5, 3, 2) |
| DD-Bernstein | -1.918 / -0.726 / 0.317 | -1.713 / -0.225 / 0.941 | -1.598 / 0.058 / 1.244 | -1.365 / 0.173 / 1.271 | (6, 6, 6) |
| DD-Bernstein + synergy | -1.641 / -0.467 / 0.524 | -1.680 / -0.230 / 0.925 | -1.614 / -0.052 / 1.124 | -1.329 / 0.104 / 1.179 | (5, 6, 6) |
| DD-Bernstein, Noisy-OR | -1.873 / -0.933 / 0.027 | -1.694 / -0.508 / 0.668 | -1.639 / -0.240 / 0.974 | -1.513 / -0.075 / 1.074 | (6, 6, 6) |
| DD-Bernstein, max skill | -2.906 / -1.277 / 0.347 | -2.613 / -0.400 / 1.377 | -2.355 / 0.027 / 1.745 | -1.786 / 0.194 / 1.855 | (6, 6, 6) |
| DD-Bernstein, max skill + synergy | -2.216 / -0.532 / 1.090 | -2.519 / -0.328 / 1.441 | -2.359 / -0.012 / 1.676 | -1.746 / 0.111 / 1.671 | (4, 6, 5) |
| DD-Bernstein, multidimensional difficulty + synergy | -4.112 / -0.940 / 1.048 | -3.740 / -0.252 / 1.816 | -3.418 / 0.065 / 2.239 | -2.688 / 0.146 / 2.519 | (6, 6, 6) |
| DD-Bernstein, additive phi-psi 1D | -1.706 / -0.530 / 0.455 | -1.621 / -0.173 / 0.967 | -1.583 / -0.020 / 1.147 | -1.329 / 0.094 / 1.165 | (6, 6, 6) |
| DD-Bernstein, additive phi-psi 3D | -1.764 / -0.568 / 0.436 | -1.666 / -0.193 / 0.964 | -1.566 / 0.008 / 1.180 | -1.316 / 0.121 / 1.198 | (6, 6, 6) |
| DD-Bernstein, multiplicative dot 1D | -1.896 / -0.682 / 0.300 | -1.738 / -0.200 / 0.939 | -1.561 / 0.088 / 1.232 | -1.335 / 0.218 / 1.285 | (6, 6, 6) |
| DD-Bernstein, multiplicative dot 3D | -1.891 / -0.669 / 0.280 | -1.720 / -0.190 / 0.922 | -1.551 / 0.095 / 1.217 | -1.333 / 0.220 / 1.277 | (6, 6, 6) |
| DD-Bernstein, multiplicative phi-psi 1D | -1.900 / -0.697 / 0.298 | -1.731 / -0.197 / 0.943 | -1.564 / 0.092 / 1.242 | -1.341 / 0.205 / 1.275 | (6, 6, 6) |
| DD-Bernstein, multiplicative phi-psi 3D | -1.896 / -0.686 / 0.291 | -1.712 / -0.187 / 0.926 | -1.560 / 0.094 / 1.228 | -1.343 / 0.205 / 1.267 | (6, 6, 6) |
| DD-Bernstein, multidimensional difficulty + 3D synergy | -3.982 / -0.813 / 1.193 | -3.749 / -0.224 / 1.875 | -3.413 / 0.106 / 2.311 | -2.662 / 0.190 / 2.615 | (6, 6, 6) |
| Team IRT 1D | -1.983 / -0.046 / 1.474 | -2.132 / 0.162 / 1.773 | -2.058 / 0.252 / 1.847 | -1.767 / 0.068 / 1.650 | (4, 4, 4) |
| Team IRT 3D | -1.186 / -0.149 / 0.981 | -1.269 / 0.141 / 1.042 | -1.045 / 0.126 / 1.016 | -0.654 / 0.035 / 0.578 | (5, 3, 2) |

**Eleven of 17 models recover the expected tier order for all three labels.**
All 11 are DD variants. The two DD exceptions are:

- **DD-Bernstein + synergy:** easy means place Winter below Fall
  (−1.680 versus −1.641); medium and hard means match the expected order.
- **Maximum skill + synergy:** easy means order Winter < Regionals < Fall <
  Nationals, and hard means put Nationals slightly below Regionals
  (1.671 versus 1.676). Medium means match.

The two multidimensional references and both Team IRT models deviate from
the expected order. For example, Team IRT 3D assigns Nationals the lowest
mean hard difficulty (0.578), and its medium means place Winter above
Regionals and Nationals. Team IRT's tournament-specific team parameters leave
each question set linked only to its own teams. Compositional fits share
player skills across the season, though relevance weights and roster effects
also affect predictions. The ordering results describe these fitted models.
They use one optimization seed, and uncertainty intervals were not computed
for the differences between sets.

The [site means](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/difficulty_means_by_tournament.csv),
[set means](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/difficulty_means_by_set.csv),
and [model summaries](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/difficulty_summary.csv)
contain the unrounded values and question counts. The
[validation record](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/validation.json)
documents the checks on fitted parameters, losses, and coverage.

## Sources and reproduction

The [comparison directory][comparison] records shared game exclusions, source
hashes, fold metrics, team PPG, and margins. Saved DD and
team-IRT fits remain in their original directories; their run-local reports
are provenance, not separate current leaderboards. The Team IRT rows were
rescored from the [current Team IRT run][team-run] with the comparison's
`code/rescore_team_irt.py`, which reproduced the previous rows to 4e-15 before
replacement; the same script prints the Team IRT in-sample scores.

The [Noisy-OR run][noisy-or] records matched-population metrics, source hashes,
minority-class counts, roster strata, and training diagnostics. Its ordinary
pooled report retains the full compositional population; the tables here use
its `aggregate/matched_*` scores restricted to the shared comparison's games.
All five fits completed with finite losses and disjoint train/test games;
scored part identities and observed outcomes match the saved DD baseline.

The [maximum-skill run][max-skill] retains both five-fold fits and the full
compositional-population report. Its `aggregate/matched/` directory records the
scores used here, minority-class and roster metrics, training diagnostics,
and input hashes. All ten fits have finite losses and disjoint train/test
games, with no dropped unknown-player rosters. Held-out part identities and
outcomes match the LSE reference on the shared comparison's scored games.

Tossup-only skill aggregation and observed-position correctness comparisons
belong to the [game-winner study][game-winners]. They do not score bonus models.
The  rows come from each run's pooled metrics in the [saved bonus run
index][runs]; their familiar/new-roster splits, team PPG and margins are in
the [roster results][synergy-rosters] and [bonus outcome report][bonus-outcomes].

[comparison]: results/compirt/comparisons/bonuses/dd-bernstein-and-team-irt-5fold/README.md
[strata]: results/compirt/comparisons/bonuses/dd-bernstein-and-team-irt-5fold/aggregate/metrics_by_question_type.csv
[runs]: results/compirt/holdout/double-difficulty/compositional/README.md
[game-winners]: results/compirt/holdout/common/game-winner-ablations/skills-lse-observed-position-correctness-and-token-replay-5fold/README.md
[synergy-rosters]: results/compirt/holdout/double-difficulty/compositional/no-synergy-and-dot-additive-1d/aggregate/novel_roster_metrics.csv
[bonus-outcomes]: results/compirt/holdout/double-difficulty/compositional/no-synergy-and-dot-additive-1d/aggregate/bonus_metrics_report.md
[noisy-or]: results/compirt/holdout/double-difficulty/compositional/noisy-or/README.md
[max-skill]: results/compirt/holdout/double-difficulty/compositional/max-skill-no-synergy-and-dot-additive-1d/README.md
[team-run]: results/compirt/holdout/common/bonus-team-irt/team-skills-1d-gamma-alpha-3d-simplex-relevance-5fold/README.md
[team-ident]: results/compirt/holdout/common/bonus-team-irt/team-skills-1d-gamma-alpha-3d-simplex-relevance-5fold/identifiability/README.md

## In-sample scores

Training-fold predictions from each saved fit, pooled over the five training
folds (each game appears in four), scored with the same `bonus_metrics`
function; teams are scored per fold. Populations differ slightly between
models; Team IRT uses DD-Bernstein's 539,205 training parts.

| Model | AUC ↑ | Log loss ↓ | Part accuracy ↑ | Exact bonus accuracy ↑ | Team PPB MAE ↓ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Multidimensional | 0.92983 | 0.35433 | 84.86% | 60.41% | 1.848 |
| Multidimensional + synergy | 0.93846 | 0.33539 | 85.67% | 62.18% | 1.053 |
| DD-Bernstein | 0.91499 | 0.37259 | 83.15% | 56.34% | 1.899 |
| DD-Bernstein + synergy | 0.92490 | 0.35295 | 84.44% | 59.30% | 0.875 |
| DD-Bernstein, Noisy-OR | 0.91723 | 0.36303 | 83.29% | 56.78% | 1.864 |
| DD-Bernstein, max skill | 0.91379 | 0.37882 | 83.05% | 56.23% | 1.985 |
| DD-Bernstein, max skill + synergy | 0.92788 | 0.35344 | 84.81% | 60.26% | 0.721 |
| DD-Bernstein, multidimensional difficulty + synergy | 0.92945 | 0.34084 | 84.67% | 59.94% | 0.631 |
| DD-Bernstein, additive phi-psi 1D | 0.92374 | 0.35502 | 84.31% | 59.02% | 1.013 |
| DD-Bernstein, additive phi-psi 3D | 0.92390 | 0.35399 | 84.33% | 59.02% | 0.988 |
| DD-Bernstein, multiplicative dot 1D | 0.91748 | 0.36598 | 83.22% | 56.61% | 1.885 |
| DD-Bernstein, multiplicative dot 3D | 0.91799 | 0.36399 | 83.23% | 56.65% | 1.878 |
| DD-Bernstein, multiplicative phi-psi 1D | 0.91624 | 0.36951 | 83.21% | 56.52% | 1.878 |
| DD-Bernstein, multiplicative phi-psi 3D | 0.91677 | 0.36856 | 83.23% | 56.57% | 1.880 |
| DD-Bernstein, multidimensional difficulty + 3D synergy | 0.92944 | 0.34004 | 84.67% | 59.98% | 0.648 |
| Team IRT 1D | 0.92466 | 0.36443 | 84.20% | 58.71% | 0.502 |
| Team IRT 3D | 0.92768 | 0.35133 | 84.49% | 59.34% | 0.369 |
