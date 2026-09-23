# CompIRT research log II: bonuses

_Updated 2026-09-21. Companion to the [tossup research log](RESEARCH_LOG.md)._

All current bonus models are compared together below: **DD-Bernstein**,
**DD-Bernstein + synergy**, the multidimensional-difficulty variant,
multidimensional references, **Team IRT 1D and 3D**, and the dot/phi-psi
additive and multiplicative synergy experiments. The [shared comparison][comparison]
contains the seven-model matched scores; the additional synergy results use
the same skills but retain their saved populations.

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
P(Y_{tb}=1)=\sigma(\theta_t^\top\alpha_b-\beta_b),\qquad
\theta_{tk},\beta_b\sim N(0,1),\quad
\alpha_{bk}\sim\operatorname{Gamma}(2,2).
$$

They use no tossup skills, roster pooling, or synergy. Team and part parameters
are frozen at their training posterior medians for held-out prediction.

All models use the same five `year_2024` whole-game folds, split and optimization
seed 42. DD bonus and team-IRT fits use 3,000 AutoNormal SVI steps at learning
rate 0.01; the multidimensional references use 2,000 steps. No correctness
calibration is applied. The comparison reuses saved predictions without training.

The seven matched rows score **127,986 parts / 42,662 bonuses / 2,330 games / 450 teams /
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
| DD-Bernstein, multidimensional difficulty + synergy | 0.89884 | 0.40202 | 81.74% | 53.33% | 0.740 |
| DD-Bernstein, additive phi-psi 1D | 0.89766 | 0.40536 | 81.65% | 52.91% | 1.062 |
| DD-Bernstein, additive phi-psi 3D | 0.89774 | 0.40536 | 81.70% | 53.03% | 1.034 |
| DD-Bernstein, multiplicative dot 1D | 0.89017 | 0.41843 | 80.82% | 51.06% | 1.959 |
| DD-Bernstein, multiplicative dot 3D | 0.89014 | 0.41860 | 80.83% | 51.11% | 1.951 |
| DD-Bernstein, multiplicative phi-psi 1D | 0.89046 | 0.41772 | 80.91% | 51.25% | 1.957 |
| DD-Bernstein, multiplicative phi-psi 3D | 0.89034 | 0.41779 | 80.91% | 51.31% | 1.958 |
| DD-Bernstein, multidimensional difficulty + 3D synergy | 0.89889 | 0.40231 | 81.77% | 53.32% | 0.746 |
| Team IRT 1D | 0.90365 | 0.39783 | 82.24% | 54.19% | 0.580 |
| Team IRT 3D | **0.90392** | **0.39535** | **82.31%** | **54.30%** | **0.511** |

Difficulty accuracy and bonus-only team/game outcomes. Each difficulty contains
42,662 parts and game metrics use 2,330 games for the matched rows.

| Model | Easy acc. ↑ | Medium acc. ↑ | Hard acc. ↑ | Team PPG MAE ↓ | Tournament Spearman ↑ | Bonus margin MAE ↓ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Multidimensional | 90.76% | 67.81% | 83.92% | 18.856 | 0.9585 | 32.138 |
| Multidimensional + synergy | 90.03% | 69.85% | 84.30% | 11.072 | 0.9702 | 26.691 |
| DD-Bernstein | 90.61% | 68.05% | 83.85% | 18.059 | 0.8898 | 33.210 |
| DD-Bernstein + synergy | 90.74% | 70.01% | 84.23% | 8.343 | 0.9374 | 26.538 |
| DD-Bernstein, multidimensional difficulty + synergy | 90.26% | 70.46% | 84.50% | 6.852 | 0.9449 | 25.740 |
| DD-Bernstein, additive phi-psi 1D | 90.72% | 69.90% | 84.34% | 9.282 | 0.9358 | 26.899 |
| DD-Bernstein, additive phi-psi 3D | 90.74% | 69.96% | 84.41% | 9.208 | 0.9327 | 26.781 |
| DD-Bernstein, multiplicative dot 1D | 90.62% | 68.00% | 83.83% | 17.973 | 0.8851 | 33.358 |
| DD-Bernstein, multiplicative dot 3D | 90.59% | 68.07% | 83.81% | 17.974 | 0.8843 | 33.450 |
| DD-Bernstein, multiplicative phi-psi 1D | 90.65% | 68.18% | 83.90% | 18.016 | 0.8839 | 33.219 |
| DD-Bernstein, multiplicative phi-psi 3D | 90.66% | 68.19% | 83.89% | 18.048 | 0.8839 | 33.357 |
| DD-Bernstein, multidimensional difficulty + 3D synergy | 90.30% | 70.55% | 84.45% | 6.874 | 0.9432 | 25.762 |
| Team IRT 1D | 91.15% | 70.97% | 84.62% | 4.814 | 0.9916 | 22.843 |
| Team IRT 3D | **91.15%** | **71.08%** | **84.70%** | **3.994** | **0.9934** | **22.792** |

The always-predict-correct baseline is 90.93% easy, 49.34% medium, and 16.21%
hard. Hard-part accuracy therefore needs particular care: always predicting a
miss already gives 83.79% accuracy.

Roster familiarity splits the matched population into 40,531 familiar-roster
bonuses and 2,131 new-roster bonuses. For  rows the counts are 40,549 and 2,151:

| Model | Familiar AUC ↑ | Familiar log loss ↓ | Familiar part acc. ↑ | New AUC ↑ | New log loss ↓ | New part acc. ↑ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Multidimensional | 0.88804 | 0.42289 | 80.80% | 0.88906 | 0.41939 | 81.34% |
| Multidimensional + synergy | 0.89682 | 0.40946 | 81.48% | 0.87509 | 0.44581 | 79.70% |
| DD-Bernstein | 0.89052 | 0.41810 | 80.82% | 0.88819 | 0.42250 | 81.07% |
| DD-Bernstein + synergy | 0.89876 | 0.40371 | 81.68% | 0.88693 | 0.42797 | 81.20% |
| DD-Bernstein, multidimensional difficulty + synergy | 0.89931 | 0.40090 | 81.76% | 0.88961 | 0.42341 | 81.40% |
| DD-Bernstein, additive phi-psi 1D | 0.89821 | 0.40426 | 81.67% | 0.88780 | 0.42619 | 81.28% |
| DD-Bernstein, additive phi-psi 3D | 0.89823 | 0.40436 | 81.72% | 0.88926 | 0.42410 | 81.39% |
| DD-Bernstein, multiplicative dot 1D | 0.89022 | 0.41819 | 80.80% | 0.88853 | 0.42305 | 81.13% |
| DD-Bernstein, multiplicative dot 3D | 0.89018 | 0.41834 | 80.80% | 0.88895 | 0.42338 | 81.33% |
| DD-Bernstein, multiplicative phi-psi 1D | 0.89053 | 0.41754 | 80.90% | 0.88857 | 0.42116 | 81.08% |
| DD-Bernstein, multiplicative phi-psi 3D | 0.89041 | 0.41762 | 80.91% | 0.88857 | 0.42089 | 80.97% |
| DD-Bernstein, multidimensional difficulty + 3D synergy | 0.89931 | 0.40124 | 81.78% | 0.89098 | 0.42256 | 81.56% |
| Team IRT 1D | 0.90369 | 0.39784 | 82.23% | 0.90277 | 0.39763 | 82.42% |
| Team IRT 3D | **0.90388** | **0.39552** | **82.29%** | **0.90463** | **0.39213** | **82.79%** |

## Interpretation

**Team IRT has the strongest scores in this comparison, with most of its
advantage already present in one dimension.** Moving from 1D to 3D improves
log loss by 0.00249 but bonus-margin MAE by only 0.051 points. DD synergy
improves the overall forecasts, but its log loss worsens on new rosters;
the multidimensional reference shows the same pattern. These are descriptive
comparisons on reused folds, without uncertainty estimates.

Team IRT provides a direct baseline for persistent team bonus ability. Its
vectors ignore lineup changes and cannot predict a new team without estimating
its parameters. Their latent axes are not identified subject traits.

The multiplicative dot and phi-psi variants show essentially no gain over the
base model (log loss 0.41772–0.41860 against 0.41832 without synergy on the
same population). Additive dot 1D beats every multiplicative variant on log loss and
PPB MAE in all five folds. Additive phi-psi nearly matches additive dot:
log loss is 0.00049 higher pooled in both 1D and 3D and higher in four of
five folds, and PPB MAE is also higher (1.062 and 1.034 against 0.943). Moving
from 1D to 3D synergy changes little for any form, including the
multidimensional-difficulty variant (log loss 0.40231 against 0.40201 in 1D).

Synergy is a learned roster adjustment, not an established measure of teamwork.
A roster is familiar only when the exact team and active player combination
appeared in that fold's training bonuses. The seven matched models use the
same roster groups, including team IRT. The [stratified scores][strata] contain the familiar
and new-roster results, subject,
declared difficulty, and subject-by-difficulty results. Unknown categories are
retained. Difficulty labels come from source metadata, not part position or
fitted difficulty; accuracy includes correctly predicted misses.

Expected bonus points are $10\sum_{b=1}^{3}p_b$ on recorded bonus opportunities.
Exact bonus accuracy requires all three part classifications to match at
threshold 0.5. Team PPB MAE averages within each team before taking absolute
errors. Team PPG pools all held-out folds, divides total bonus points by games
played (including zero-bonus games), then computes errors. PPG MAE and Spearman
weight the 29 tournaments equally; signed bonus-margin MAE weights complete
games equally. These metrics condition on recorded bonus ownership and exclude
tossup points.

Only one optimization seed was run. Stage-2 uncertainty is conditional on fixed
player skills, and probabilities use parameter medians rather than posterior
predictive integration. Comparisons change dimensions, priors, and aggregation,
so they do not isolate the effect of the Bernstein curves.

A useful next comparison would put a global bonus intercept, a team intercept,
and pairwise synergy under the same aggregation and folds, then withhold roster
combinations to test transfer. Centering the roster contribution can clarify its
baseline offset without changing predictions if the compensating intercept is
retained; its sign alone does not identify a teamwork effect.

## Sources and reproduction

The [comparison directory][comparison] records shared game exclusions, source
hashes, fold metrics, team PPG, and margins. Saved DD and
team-IRT fits remain in their original directories; their run-local reports
are provenance, not separate current leaderboards.

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

## In-sample scores

Training-fold predictions from each saved fit, pooled over the five training
folds (each game appears in four), scored with the same `bonus_metrics`
function; teams are scored per fold. Populations differ slightly between
models. Team IRT runs did not save training predictions.

| Model | AUC ↑ | Log loss ↓ | Part accuracy ↑ | Exact bonus accuracy ↑ | Team PPB MAE ↓ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Multidimensional | 0.92983 | 0.35433 | 84.86% | 60.41% | 1.848 |
| Multidimensional + synergy | 0.93846 | 0.33539 | 85.67% | 62.18% | 1.053 |
| DD-Bernstein | 0.91499 | 0.37259 | 83.15% | 56.34% | 1.899 |
| DD-Bernstein + synergy | 0.92490 | 0.35295 | 84.44% | 59.30% | 0.875 |
| DD-Bernstein, multidimensional difficulty + synergy | 0.92945 | 0.34084 | 84.67% | 59.94% | 0.631 |
| DD-Bernstein, additive phi-psi 1D | 0.92374 | 0.35502 | 84.31% | 59.02% | 1.013 |
| DD-Bernstein, additive phi-psi 3D | 0.92390 | 0.35399 | 84.33% | 59.02% | 0.988 |
| DD-Bernstein, multiplicative dot 1D | 0.91748 | 0.36598 | 83.22% | 56.61% | 1.885 |
| DD-Bernstein, multiplicative dot 3D | 0.91799 | 0.36399 | 83.23% | 56.65% | 1.878 |
| DD-Bernstein, multiplicative phi-psi 1D | 0.91624 | 0.36951 | 83.21% | 56.52% | 1.878 |
| DD-Bernstein, multiplicative phi-psi 3D | 0.91677 | 0.36856 | 83.23% | 56.57% | 1.880 |
| DD-Bernstein, multidimensional difficulty + 3D synergy | 0.92944 | 0.34004 | 84.67% | 59.98% | 0.648 |
| Team IRT 1D | not saved | not saved | not saved | not saved | not saved |
| Team IRT 3D | not saved | not saved | not saved | not saved | not saved |
