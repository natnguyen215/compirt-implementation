# CompIRT research log II: bonuses

_2026-09-13. Companion to the [tossup research log](RESEARCH_LOG.md)._

**DD-Bernstein skills improve bonus probability forecasts modestly over the
saved multidimensional reference. Synergy improves prediction in every DD
fold, but its interpretation remains a roster adjustment.**

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

| Model | Rosters | Synergy | Part acc. ↑ | Exact bonus acc. ↑ | AUC ↑ | Log loss ↓ |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| DD-Bernstein | Familiar (40,549) | off | 80.79% | 50.98% | 0.8904 | 0.4184 |
| DD-Bernstein | Familiar | on | 81.75% | 53.06% | 0.8989 | 0.4032 |
| DD-Bernstein | New (2,151) | off | 80.88% | 52.30% | 0.8884 | 0.4222 |
| DD-Bernstein | New | on | 81.11% | 53.14% | 0.8871 | 0.4281 |
| Multidimensional | Familiar | off | 80.80% | 51.14% | 0.8880 | 0.4229 |
| Multidimensional | Familiar | on | 81.48% | 52.61% | 0.8968 | 0.4094 |
| Multidimensional | New | off | 81.39% | 52.77% | 0.8892 | 0.4192 |
| Multidimensional | New | on | 79.70% | 49.28% | 0.8753 | 0.4454 |

**Synergy's gains come from familiar rosters.** On new rosters DD synergy
nudges thresholded accuracy up but worsens AUC and log loss; multidimensional
synergy loses 1.7 points of part accuracy and 3.5 points of exact accuracy.
New rosters are not harder for the base arms. This is consistent with $s$
acting as a roster-specific adjustment that does not transfer. No uncertainty
was computed; with 2,151 bonuses, AUC gaps near 0.001 may be noise.

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
