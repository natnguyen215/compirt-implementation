# CompIRT research log II: bonuses

_2026-09-13. Companion to the [tossup research log](RESEARCH_LOG.md)._

**DD-Bernstein skills improve bonus probability forecasts modestly over the
saved multidimensional reference. Synergy improves prediction in every DD
fold, but its interpretation remains a roster adjustment.**

**2026-09-17 update: directly learning team skills from bonuses outperforms the
saved compositional references on matched familiar-team games. Three-dimensional
team IRT reaches 0.3953 log loss and 22.792-point bonus-margin MAE; a scalar
team model captures most of the improvement.** See the team-IRT study below.

## Model and protocol

For player $i$, bonus part $b$, and inferred active roster $R$:

$$
u_{ib}=\alpha_b^\top\widehat\theta_i,\qquad
A_b(R)=\tau\log\sum_{i\in R}\exp(u_{ib}/\tau),
$$

$$
s(R)=\sum_{\substack{i,j\in R\\i<j}}\psi_i^\top\psi_j,\qquad
Y_{Rb}\sim\operatorname{Bernoulli}\!\left(\sigma[A_b(R)-\beta_b+s(R)]\right).
$$

The base arm sets $s=0$. Skills are frozen Stage-1 posterior medians; bonus
weights, difficulty, aggregation temperature, and optional synergy are learned.
Aggregation is unnormalized: $n$ identical players with ability $u$ yield
$A = u + \tau \log n$. Its zero point and temperature are scale-dependent.

| Configuration | Skill dimensions | Bonus weight prior | Synergy rank |
| --- | ---: | --- | ---: |
| Historical multidimensional | 5 | $\alpha_{bk}\sim N(0,1)$ | 3 |
| DD-Bernstein | 3 | $\alpha_{bk}\sim\operatorname{Gamma}(2,2)$, shape/rate | 1 |

Both use $\beta_b\sim N(0,1)$, $\tau\sim\operatorname{HalfCauchy}(1)$,
and $\psi_i\sim N(0,0.5I)$. DD's source has degree-3 Bernstein curves,
drop concentration 2, learned curve locations, terminal intercepts, and
simplex tossup relevance. The bonus weights are positive but not a simplex.

Five `year_2024` whole-game folds, split/optimization seed 42; 2,000 AutoNormal
SVI steps, learning rate 0.01, no correctness calibration. Bonus parameters
are frozen for held-out replay. All four configurations score the same
**128,100 parts / 42,700 bonuses / 2,332 games / 450 teams**. Labels, lineups,
game separation, and coverage were checked.

These are reused development folds with familiar entities. Stage-1 artifacts
were reused, not refit under the current normalized first-buzz likelihood.
Stage-2 uncertainty is conditional on fixed skills; only one optimization
seed was run. The comparison changes dimensions, priors, and synergy rank as
well as Stage 1, so it does not isolate the Bernstein family effect.

## Results

Pooled held-out scores from the [matched comparison][comparison]:

| Model | AUC ↑ | Log loss ↓ | Part accuracy ↑ | Exact bonus accuracy ↑ | Team PPB MAE ↓ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Multidimensional | 0.8881 | 0.4227 | 80.83% | 51.22% | 2.040 |
| DD-Bernstein | 0.8903 | 0.4186 | 80.79% | 51.04% | 1.990 |
| Multidimensional + synergy | 0.8955 | 0.4112 | 81.39% | 52.44% | 1.172 |
| DD-Bernstein + synergy | **0.8983** | **0.4044** | **81.72%** | **53.06%** | **0.904** |

DD synergy improves AUC, log loss, and PPB MAE in every fold. The base DD
model has slightly lower thresholded accuracy despite better probability
scores. Other historical baseline/topic/TF-IDF runs often fit bonus parameters
on the evaluated responses or use different splits; they need matched reruns.

Expected bonus points are $\widehat P_r=10\sum_{b=1}^{3}p_{rb}$.
PPB MAE averages predictions and actual points within each team first:

$$
\mathrm{PPB\ MAE}=\frac1{G}\sum_{g=1}^{G}
\left|\frac1{n_g}\sum_{r\in g}(\widehat P_r-P_r)\right|.
$$

Thus 0.904 describes error in team averages across many bonuses. Exact bonus
accuracy requires all three part classifications to match, using threshold 0.5.

## Does synergy still behave like a negative intercept?

[Held-out contributions][offsets], weighted by observed bonus responses:

| Quantity | Multidimensional + synergy | DD-Bernstein + synergy |
| --- | ---: | ---: |
| Mean aggregate $A$ | +1.039 | −0.373 |
| Mean $A-\beta$ | +0.711 | −0.088 |
| Mean synergy | −0.707 | +0.280 |
| Median synergy | −0.635 | +0.097 |
| Negative / positive synergy | 77.7% / 19.2% | 34.7% / 62.2% |

The old average correction nearly cancels its positive base logit. DD's
correction is mostly positive, with a 10th–90th percentile range of
−0.48 to +1.17 logits. Holding other fitted terms fixed, adding it raises
correctness probability by 3.33 percentage points on average. This is a
within-fit calculation, not the effect of retraining without synergy.

The sign change does not establish teamwork: **94.96%** of test bonuses use
a team and exact inferred roster already observed in training ([audit][rosters]).
The term can absorb missing bonus expertise or persistent team differences.
Latent skill axes have no established subject labels, and flipping every
synergy profile's sign preserves all pair products. A contribution $s$ changes
the odds by $e^s$, conditional on the other fitted terms.

## Does synergy help unseen rosters?

The same held-out predictions, split by whether the test bonus's exact team and
inferred roster appeared in the fold's training bonuses ([metrics][novel], [code][novel-code]).
Familiar counts match the roster audit. All **2,151** unfamiliar bonuses
(5.04%) come from players seen in training, so these are new combinations or
tournament entries, not new players.

### Familiar rosters

| Model | Synergy | Part acc. ↑ | Easy acc. ↑ (n = 40,549) | Medium acc. ↑ (n = 40,549) | Hard acc. ↑ (n = 40,549) | Exact bonus acc. ↑ | AUC ↑ | Log loss ↓ |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DD-Bernstein | off | 80.79% | 90.67% | 67.98% | 83.72% | 50.98% | 0.8904 | 0.4184 |
| DD-Bernstein | on | 81.75% | 90.80% | 70.18% | 84.27% | 53.06% | 0.8989 | 0.4032 |
| Multidimensional | off | 80.80% | 90.80% | 67.79% | 83.80% | 51.14% | 0.8880 | 0.4229 |
| Multidimensional | on | 81.48% | 90.06% | 70.07% | 84.32% | 52.61% | 0.8968 | 0.4094 |

### New rosters

| Model | Synergy | Part acc. ↑ | Easy acc. ↑ (n = 2,151) | Medium acc. ↑ (n = 2,151) | Hard acc. ↑ (n = 2,151) | Exact bonus acc. ↑ | AUC ↑ | Log loss ↓ |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DD-Bernstein | off | 80.88% | 89.87% | 66.90% | 85.87% | 52.30% | 0.8884 | 0.4222 |
| DD-Bernstein | on | 81.11% | 89.68% | 68.11% | 85.54% | 53.14% | 0.8871 | 0.4281 |
| Multidimensional | off | 81.39% | 90.10% | 67.92% | 86.15% | 52.77% | 0.8892 | 0.4192 |
| Multidimensional | on | 79.70% | 89.45% | 65.50% | 84.15% | 49.28% | 0.8753 | 0.4454 |

Difficulty columns added 2026-09-15 using the source's declared part labels,
joined by bonus ID and part index. Each group has one easy, medium, and hard
part per response (40,549 or 2,151 parts per difficulty); none are unknown.
These are classification accuracies, including correctly predicted misses,
not the fraction of parts answered correctly. Full tables and tournament
bonus-only PPG are in the [extended report][bonus-metrics].

The always-predict-correct baseline is **90.94% easy, 49.34% medium, and
16.21% hard** over all 42,700 parts per difficulty. For familiar rosters it is
**91.02%, 49.57%, and 16.29%**; for new rosters it is **89.40%, 44.91%, and
14.60%**, respectively. These are observed correct-answer rates and are the
same for both models and both synergy settings. Each column’s n counts parts
for one model/configuration, without counting repeated predictions twice.

**Synergy's gains come from familiar rosters.** On new rosters DD synergy
nudges thresholded accuracy up but worsens AUC and log loss; multidimensional
synergy loses 1.7 points of part accuracy and 3.5 points of exact accuracy.
New rosters are not harder for the base arms. This is consistent with $s$
acting as a roster-specific adjustment that does not transfer. No uncertainty
was computed; with 2,151 bonuses, AUC gaps near 0.001 may be noise.

## Bonus-only team PPG and margins

Updated 2026-09-16 from the same saved predictions, pooled across folds before
computing team PPG. Predicted bonus points use `10 * sum(part probabilities)`
on recorded bonus opportunities. Divide each team’s total bonus points by
unique games played, including games with zero bonuses. Each team’s absolute
PPG error is then averaged within its tournament. Spearman compares team PPG
ranks within each tournament.

The PPG MAE and Spearman macro means weight the **29 tournaments** equally.
Bonus-only margin is team A’s bonus total minus team B’s in a game; margin
MAE averages absolute errors in these signed differences across games.
All four arms include **2,332 games / 451 teams**, including one team that
heard no bonuses, and exclude the same 99 source games lacking complete
saved bonus predictions. These metrics condition on actual
bonus opportunities; they do not predict which team earns each bonus.

| Model | Synergy | Team bonus PPG MAE ↓ | Tournament Spearman ↑ | Bonus margin MAE ↓ |
| --- | --- | ---: | ---: | ---: |
| DD-Bernstein | off | 18.083 | 0.8839 | 33.235 |
| DD-Bernstein | on | 8.093 | 0.9400 | 26.517 |
| Multidimensional | off | 18.763 | 0.9583 | 32.151 |
| Multidimensional | on | 10.975 | 0.9696 | 26.683 |

The [extended report][bonus-metrics] lists each tournament separately and
links every team’s observed/predicted PPG and absolute error, plus the
underlying team-game totals and signed game margins. Familiar and new rosters
are pooled for PPG because a team can use both during a tournament.

## Skills-only LSE, correctness-only scoring, and full tossup replay

Added 2026-09-16. Predict the tossup-only winner of each game using frozen
Stage-1 skills, with no question parameters, confidence parameters, or synergy.
First average each player's skill dimensions, then apply LSE
across the active team lineup with temperature 1:

$$
\bar\theta_i=\frac1K\sum_{k=1}^{K}\widehat\theta_{ik},\qquad
S(R)=\log\sum_{i\in R}\exp(\bar\theta_i).
$$

Average each team's lineup score across the game's tossups to account for
substitutions, and predict the team with the higher average score. All active
players enter the score, including players who never buzz. Training and frozen
holdout skill values were checked to agree; all parameters stayed fixed.

All three methods use the same five held-out folds (split seed 42), **2,331 complete
games**, and identical recorded tossup scores. Excluding 66 recorded ties
leaves **n = 2,265 decisive games**. Accuracy pools games equally across folds;
it is not an average of fold accuracies. Bonuses do not enter the target.

| Saved fit | Skills-only LSE accuracy ↑ | Correctness-only accuracy at observed buzz positions ↑ | Full tossup replay accuracy ↑ | LSE gain |
| --- | ---: | ---: | ---: | ---: |
| [DD-Bernstein, unconstrained terminal][lse-dd-unconstrained] | 70.68% | **72.98%** | 69.27% | +1.41 pp |
| [DD-Bernstein, 3,000 steps][lse-dd] | 67.06% | **67.33%** | 65.56% | +1.50 pp |
| [Multidimensional, 3,000 steps][lse-multidim] | 68.26% | **74.48%** | 15.94% | +52.32 pp |

Correctness-only scoring evaluates every active player's saved correctness
curve at the **observed first-buzz position** of the tossup, shared by both
teams. Positions use the fitted model's clamped token cell; dead tossups use
the final cell. Let $\eta^C_{ij}(t_j^*)$ be that player's correctness logit,
including question relevance and difficulty, any player correctness intercept,
and the saved terminal intercept when applicable. For each team-question lineup:

$$
C(R,j)=\sigma\!\left(\log\sum_{i\in R}
\exp\bigl(\eta^C_{ij}(t_j^*)\bigr)\right).
$$

Average these scores across the game's questions and predict the higher-scoring
team. This uses temperature-1 LSE, with no hazard/confidence parameters,
thresholded buzzes, neg predictions, or simulated continuations. Only phase-0
lineups enter; bounceback rows do not duplicate players. The team score is a
comparison heuristic, not a calibrated probability of winning a tossup.
**This is conditional on observed timing, not an end-to-end game forecast**,
so its accuracy is not directly equivalent to replay accuracy.

Full replay here means the repository's [token-threshold tossup replay](RESEARCH_LOG.md#token-threshold-game-and-tournament-replay):
0.5 buzz and correctness thresholds, seeded token ties (seed 42), negs, team
lockout, and opponent continuations. Predicted game ties count as incorrect
against decisive recorded winners. The multidimensional replay predicts
**1,802** such ties. Its large accuracy gap therefore reflects the threshold replay's
frequent failure to produce a decisive winner.

These are explicit skill summaries, not
identified player traits. The comparison uses reused development folds.

[Reproduction and audit artifacts][game-winner-ablations] include all game
predictions, exact correct-game counts, source hashes, and the scoring code.
Reconstructed correctness probabilities agree with the saved row predictions;
all methods retain the same complete-game population and targets.

## Direct team-skill bonus IRT

Added 2026-09-17. Fit bonus outcomes directly with a free skill vector for each
tournament-specific `team_id`, a positive discrimination vector for each bonus
part, and scalar part difficulty:

$$
Y_{tj}\sim\operatorname{Bernoulli}\!\left(\sigma[\theta_t^\top\alpha_j-\beta_j]\right),
\qquad \theta_{tk},\beta_j\sim N(0,1),\quad
\alpha_{jk}\sim\operatorname{Gamma}(2,2)\ \text{(shape/rate)}.
$$

The 1D and 3D arms use **3,000 AutoNormal SVI steps**, learning rate 0.01,
optimization seed 42, and the existing five `year_2024` whole-game folds with
split seed 42. Team and part parameters are fitted only on training bonuses;
held-out probabilities replay their saved posterior medians. No tossup skills,
roster aggregation, or synergy enter these models.

All six arms score the same **127,986 parts / 42,662 bonuses / 2,330 games /
450 teams / 29 tournaments**, including a team with zero bonuses. Relative to
the earlier comparison, two fold-0 games at 2024 Regionals MIT are excluded
because one team has no training bonus responses. Excluding entire games
removes 38 bonuses, including 20 from that unseen team, from every arm.
The original fold coverage exclusions still apply. Saved DD and multidimensional
references were reused at their original **2,000 bonus-stage steps**, with their
existing Stage-1 fits; this is not an equal-budget parameterization ablation.

**Metric parity check:** this study calls the existing `bonus_metrics` and
`bonus_team_outcomes` functions. Recomputing the original reference populations
reproduces their published AUC, log loss, accuracy, Brier, and PPB MAE within
1e-6. Every retained reference game's observed/predicted margin and absolute
error matches its earlier artifact within 1e-10. The small reference-table
changes below come from excluding two games, not new metric definitions:
DD + synergy log loss changes from 0.404436 to 0.404482 and margin MAE from
26.516549 to 26.516254. The [parity audit][team-irt-parity] records all four arms.

### Overall and bonus margins

Pooled held-out scores from the [new matched report][team-irt-report]:

| Model | AUC ↑ | Log loss ↓ | Part accuracy ↑ | Exact bonus accuracy ↑ | Team PPB MAE ↓ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Team IRT, 1D | 0.9037 | 0.3978 | 82.24% | 54.19% | 0.580 |
| Team IRT, 3D | **0.9039** | **0.3953** | **82.31%** | **54.30%** | **0.511** |
| DD-Bernstein | 0.8903 | 0.4186 | 80.79% | 51.05% | 1.989 |
| DD-Bernstein + synergy | 0.8982 | 0.4045 | 81.71% | 53.05% | 0.904 |
| Multidimensional | 0.8881 | 0.4227 | 80.83% | 51.22% | 2.045 |
| Multidimensional + synergy | 0.8955 | 0.4113 | 81.39% | 52.44% | 1.176 |

Bonus-only PPG and margins:

| Model | Team bonus PPG MAE ↓ | Tournament Spearman ↑ | Bonus margin MAE ↓ |
| --- | ---: | ---: | ---: |
| Team IRT, 1D | 4.814 | 0.9916 | 22.843 |
| Team IRT, 3D | **3.994** | **0.9934** | **22.792** |
| DD-Bernstein | 18.106 | 0.8855 | 33.220 |
| DD-Bernstein + synergy | 8.121 | 0.9402 | 26.516 |
| Multidimensional | 18.856 | 0.9585 | 32.138 |
| Multidimensional + synergy | 11.072 | 0.9702 | 26.691 |

Margins sum expected bonus points, `10 * sum(part probabilities)`, for each
team and subtract opponent totals. They condition on recorded bonus ownership
and omit tossup points. Each complete game gets one vote. Team PPB and PPG
pool held-out predictions across folds before taking errors. Tournament-macro
bonus PPG MAE is **3.994** for 3D team IRT, **4.814** for 1D, and **8.121** for
DD + synergy; corresponding mean within-tournament Spearman correlations are
**0.9934**, **0.9916**, and **0.9402**.

Both team IRT arms improve log loss and margin MAE over DD + synergy in every
fold. The 3D model lowers log loss by **0.00914** and margin MAE by **3.725
points** (14.0%). Three dimensions improve log loss over one by **0.00249**,
but their margin MAEs differ by only **0.051 points**. These are descriptive
comparisons from one optimization seed on reused development folds.

### Declared question difficulty

Each difficulty has **42,662 parts**. Labels come from source metadata, not
part position. Accuracy includes correctly predicted misses; observed
conversion is shown separately.

| Model | Easy acc. ↑ (n = 42,662) | Medium acc. ↑ (n = 42,662) | Hard acc. ↑ (n = 42,662) |
| --- | ---: | ---: | ---: |
| Team IRT, 1D | 91.15% | 70.97% | 84.62% |
| Team IRT, 3D | 91.15% | 71.08% | 84.70% |
| DD-Bernstein | 90.62% | 67.94% | 83.82% |
| DD-Bernstein + synergy | 90.74% | 70.07% | 84.33% |
| Multidimensional | 90.76% | 67.81% | 83.92% |
| Multidimensional + synergy | 90.03% | 69.85% | 84.30% |

The always-predict-correct baseline (observed conversion) is **90.93% easy,
49.34% medium, and 16.21% hard** on this matched population.

Most of the 3D-versus-DD log-loss gain comes from medium parts; easy-part log
loss is slightly worse despite higher thresholded accuracy. The hard-part
always-incorrect accuracy is already 83.79%, so raw accuracy alone overstates
how informative that stratum is.

### Subject categories

The 3D arm has lower log-loss point estimates than DD + synergy in every
reported category, including Unknown. Differences are descriptive; no
category-specific uncertainty or multiple-comparison adjustment was computed.

| Category | Parts | 3D accuracy | DD + synergy accuracy | 3D log loss | DD + synergy log loss |
| --- | ---: | ---: | ---: | ---: | ---: |
| Current Events | 1,224 | 83.01% | 83.01% | 0.3830 | 0.3980 |
| Fine Arts | 14,916 | 80.75% | 80.20% | 0.4179 | 0.4286 |
| Geography | 2,319 | 81.59% | 81.37% | 0.4080 | 0.4085 |
| History | 20,427 | 81.95% | 81.77% | 0.3951 | 0.3967 |
| Literature | 20,430 | 83.87% | 82.78% | 0.3742 | 0.3899 |
| Mythology | 4,707 | 80.14% | 80.26% | 0.4203 | 0.4232 |
| Other Academic | 1,245 | 84.50% | 83.37% | 0.3680 | 0.3764 |
| Philosophy | 4,785 | 81.88% | 80.96% | 0.4101 | 0.4195 |
| Popular Culture | 1,470 | 78.44% | 77.89% | 0.4333 | 0.4405 |
| Religion | 5,076 | 82.45% | 82.09% | 0.3933 | 0.4011 |
| Science | 20,349 | 82.11% | 81.74% | 0.3994 | 0.4085 |
| Social Science | 4,518 | 84.24% | 83.42% | 0.3651 | 0.3666 |
| Unknown | 26,520 | 82.69% | 81.81% | 0.3931 | 0.4054 |

Unknown comprises **20.72%** of scored parts and is retained rather than
dropped. [Full stratified CSVs][team-irt-strata] also include category x
difficulty results, counts, AUC, Brier, calibration, and all six arms.
Three dimensions do not uniformly improve on one across subjects: for example,
Literature improves from 0.3835 to 0.3742 log loss, while Mythology worsens from
0.4168 to 0.4203.

**Direct bonus-trained team ability is a strong familiar-team baseline; most
of its advantage is already present in one dimension.** This supports testing
whether synergy absorbs persistent team-level bonus ability, but does not
identify its mechanism. These reused development folds contain familiar teams
and questions, and free team vectors do not provide unseen-team transfer or
account for lineup changes. Their latent axes are not identified subject traits.
Only one optimization seed was run. All ten fits had finite loss traces;
serialized parameter replay matched the saved predictions, and train/test
separation and common scoring populations were checked.

Implementation, reproduction command, parameters, prediction tables, plots,
source hashes, and code snapshot: [experiment folder][team-irt]. The full
repository check passed after adding the study and its five focused tests.

## Centering and next experiment — proposed, not fitted

Centering can clarify the decomposition without changing predictions. With
reference means computed on training data and retained for test replay:

$$
\eta=\delta+(A-\bar A)-(\beta-\bar\beta)+(s-\bar s),\qquad
\delta=\bar A-\bar\beta+\bar s.
$$

The baseline collects the common offset; the remaining terms describe
deviations from the chosen reference population. Center the roster effect $s$,
not merely the individual profiles. Shifting ability alone changes predictions;
refitting with unchanged priors after shifting also changes the model.

Next compare a global bonus intercept, a team intercept, and pairwise synergy
under the same aggregation and folds. A free baseline needs an identified
difficulty offset, such as zero-centered difficulty deviations. Withheld
roster combinations are needed to test transfer beyond familiar teams.

Implementation and reproduction: [bonus model](compositional_model.py),
[runner](run_scripts/common/run_compositional_from_folds.py),
[run guide](run_scripts/README.md#bonus-stage-from-saved-folds), [full results][results].

[comparison]: results/compirt/holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal/aggregate/comparison_with_multidim.json
[offsets]: results/compirt/holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal/aggregate/synergy_location_diagnostics.json
[rosters]: results/compirt/holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal/aggregate/roster_familiarity.json
[novel]: results/compirt/holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal/aggregate/novel_roster_metrics.csv
[novel-code]: results/compirt/holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal/code/novel_roster_metrics.py
[results]: results/compirt/holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal/aggregate/report.md
[bonus-metrics]: results/compirt/holdout/double-difficulty/compositional/dd-bernstein-332-simplex-locations-terminal/aggregate/bonus_metrics_report.md
[lse-dd-unconstrained]: results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-unconstrained-terminal/
[lse-dd]: results/compirt/holdout/double-difficulty/dd-332-normalized-v1-20260913-150350/
[lse-multidim]: results/compirt/holdout/multidim/multidim-normalized-v1-20260913-150350/
[game-winner-ablations]: results/compirt/holdout/common/game-winner-ablations/2026-09-16/README.md
[team-irt]: results/compirt/holdout/common/bonus-team-irt/2026-09-17/README.md
[team-irt-report]: results/compirt/holdout/common/bonus-team-irt/2026-09-17/aggregate/report.md
[team-irt-strata]: results/compirt/holdout/common/bonus-team-irt/2026-09-17/aggregate/metrics_by_question_type.csv
[team-irt-parity]: results/compirt/holdout/common/bonus-team-irt/2026-09-17/aggregate/existing_metrics_parity.csv
