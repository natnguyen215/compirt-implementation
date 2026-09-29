# CompIRT evaluation metrics

This document is the metric contract for `compirt_eval`. It records which saved
rows enter each metric, the order of aggregation, the equation, the output
artifact, and interpretation limits.

It also covers the end-to-end diagnostics: Brier score and bonus RPS,
sharpness and strata, survival-curve metrics, first-buzzer identity, and the
token-threshold game replay.

## Evaluation regime

The evaluator consumes saved posterior-median predictions. A single-split run
therefore reports fitted, in-sample performance. The temporal runner is
transductive: it uses historical player posteriors as priors, but test-player
and test-question parameters are updated from test-period outcomes, and the
test bonus model is fit from test bonus outcomes. These metrics are not fully
inductive predictions for unseen questions.

## Aggregation map

Here **batch** means a group used for evaluation, not a training minibatch. The
evaluator loads all eligible saved rows for a run; it does not calculate a
metric in each training minibatch and then average the batch metrics.

In the **Related files** notes below, bare prediction filenames are saved model
inputs. Paths beginning with `csvs/` or `graphs/` are evaluator outputs
(figures sort into themed `graphs/<group>/` subdirectories).

Aggregation order matters. “Average within each team, then across teams” gives
each team equal weight; averaging all rows at once gives teams with more rows
more weight. The table states the exact order used:

| Metric | Calculation order | Final weight | Better |
| --- | --- | --- | --- |
| Accuracy, log loss, ECE | Select eligible rows → score all rows together | One vote per row (ECE applies this through bin-size weights) | Accuracy higher; loss/ECE lower |
| AUC | Select eligible rows → compare the ranking of every correct/incorrect pair | One vote per cross-class pair | Higher |
| Buzz-position MAE / median AE | One conditional expected position per observed-buzz event → one absolute error per event → mean / median | One vote per event | Lower |
| Bonus part accuracy (micro) | Score all response-part rows together | One vote per part | Higher |
| Bonus part accuracy (macro) | Score parts → average within each team or bonus question → average the group means | One vote per team or bonus question | Higher |
| Exact three-part accuracy | Group parts by `response_id` → mark whether all three labels match → average response marks | One vote per bonus response | Higher |
| PPB MAE | Sum three part scores within each response → average all responses for each team → take each team's absolute PPB error → average team errors | One vote per team | Lower |
| Bonus accuracy by difficulty | Join declared part labels → score all rows within easy, medium, hard, or unknown | One vote per part within its difficulty | Higher |
| Bonus precision, recall, F1 (research log) | Threshold correctness → pool confusion counts over held-out folds → calculate ratios | One vote per response-part row | Higher |
| Bonus difficulty-order accuracy (research log) | Compute effective part difficulty → mark each distinct bonus 1 if easy < medium < hard, otherwise 0 → average marks | One vote per fitted bonus question | Higher |
| Bonus-only team PPG MAE | Pool held-out games → sum team bonus points → divide team totals by games → absolute team PPG error → mean within tournament → mean across tournaments | Equal tournaments; equal teams within tournament | Lower |
| Bonus-only team PPG Spearman | Pool games and compute team PPG → rank observed and predicted PPG within tournament → correlate ranks → average defined tournament correlations | Equal tournaments | Higher |
| Bonus-only game margin MAE | Sum each team’s bonus points per game → subtract opponent totals → absolute error in the signed margin → mean across games | Equal games | Lower |

## How to read the notation

You do not need to memorize one global list of symbols. Each section below
defines its symbols where they are used. The same few conventions recur:

| Notation | How to read it |
| --- | --- |
| $y$ | What actually happened, usually 1 for correct and 0 for incorrect |
| $p$ | The model's predicted probability that the response is correct |
| A hat, as in $\widehat S$ | A model prediction; the same letter without a hat is observed |
| $\sum$ | Add the following quantity over all indicated rows, tokens, or responses |
| $\prod$ | Multiply the following quantity over all indicated players |
| $\mathcal R_u$ | A collection (set), here the bonus responses heard by team $u$ |
| $|\mathcal R_u|$ | The number of items in that collection |
| $|a-b|$ | The absolute size of the difference between two numbers; signs are ignored |
| $\#\{r:\text{condition}\}$ | The number of responses $r$ that satisfy the condition |
| $E[x\mid\text{condition}]$ | The average value expected for $x$ when considering only the stated condition |
| $\operatorname{mean}_{r\in\mathcal R}(S_r)$ | Add $S_r$ over responses in $\mathcal R$, then divide by the number of responses |

Subscripts identify which object a value belongs to. For example, $p_{rb}$ is
the predicted probability for bonus response $r$, part $b$. Letters such as
$e$, $r$, and $u$ are only labels; they stand for an event, response, and team
respectively, rather than values that are multiplied together.

## Shared binary-classification metrics

For each eligible row $n$, $y_n\in\{0,1\}$ is the observed result and $p_n$ is
the predicted probability of a correct response. $N$ is the total number of
eligible rows. All $N$ rows are scored together, so these are **micro**
metrics: a player, team, or question with more rows has more influence. The
evaluator clips probabilities to $[10^{-6},1-10^{-6}]$ before scoring.

Predict a correct response ($y_n=1$) when $p_n\ge 0.5$ and an incorrect
response ($y_n=0$) otherwise. Accuracy is

$$
\text{Accuracy}
=\frac{\text{number of correctly classified rows}}
{\text{total number of eligible rows}}.
$$

Negative-class precision and recall use the same decision: an exact tie
predicts correct. Higher is better.

Binary log loss is

$$
\operatorname{LogLoss}
=-\frac{1}{N}\sum_{n=1}^{N}
\left(y_n\log p_n+(1-y_n)\log(1-p_n)\right).
$$

This sums one penalty per row and divides by $N$. Confident wrong predictions
receive a large penalty. Lower is better.

AUC is the ordinary ROC AUC, computed from probabilities before the numerical
clipping used for log loss. It is undefined when the selected rows contain
only one outcome class.

AUC asks whether a randomly chosen correct row tends to rank above a randomly
chosen incorrect row. An AUC of 1 is perfect and 0.5 is chance-level. Higher
is better. Unlike the other shared metrics, AUC compares correct/incorrect
pairs rather than summing one independent loss per row.

Expected calibration error uses the same ten equal-width probability bins as
the reliability table: $[0, 0.1], (0.1, 0.2], \ldots, (0.9, 1]$. Let $C_m$ be
the set of row indices assigned to bin $m$:

$$
\operatorname{ECE}
=\sum_m\frac{|C_m|}{N}
\left|\operatorname{mean}_{n\in C_m}(y_n)
-\operatorname{mean}_{n\in C_m}(p_n)\right|.
$$

Predictions are divided into ten equal-width confidence bins $C_m$. Within
each bin, compare mean confidence with the observed correct rate. The outer
sum weights each gap by the bin's share $|C_m|/N$, so large bins count more.
Lower is better; 0 means every bin is perfectly calibrated.

## Tossup metrics

### Correctness

Tossup correctness is observed only for the recorded first buzzer, so AUC,
log loss, ECE, and accuracy use only rows with `z == "BUZZ"`. They measure
correctness conditional on taking the first buzz, not total scoring or tossups
converted. All selected buzz rows are scored in one batch, with one vote per
observed buzz. The position-stratified output separately repeats this process
within five fixed equal-width relative-position bands.

**Related files:** `tossup_predictions.csv` supplies the rows;
`csvs/tossup_metrics.csv` stores the overall metrics;
`csvs/tossup_metrics_by_buzz_position.csv` stores the fifths; and
`graphs/tossup/tossup_reliability.png` plus
`graphs/tossup/tossup_reliability_by_buzz_position.png` visualize calibration.

### Buzz-position MAE

Only events with an observed buzz are written to
`buzz_event_predictions.csv`, so the saved prediction is the buzz-conditioned
expectation. For event $e$, the numerator below sums position times predicted
first-buzz mass over every token $t$; the denominator is the event's total
predicted buzz mass:

$$
\widehat x_e
=E[x_e\mid\text{buzz}]
=\frac{\sum_t x_{et}q_{et}}{1-q_{eD}}.
$$

Here:

- $x_{et}$ is token $t$'s relative position from 0 (start) to 1 (end);
- $q_{et}$ is the predicted probability that the first buzz occurs at that
  token; and
- $q_{eD}$ is the predicted probability of no buzz at all.

Thus $\widehat x_e$ is a probability-weighted average position after the
no-buzz mass has been removed. If $1-q_{eD}$ is numerically zero, the evaluator
uses the question end.

The evaluator reports

$$
\operatorname{BuzzPositionMAE}
=\frac{1}{|\mathcal E_{\mathrm{buzz}}|}
\sum_{e\in\mathcal E_{\mathrm{buzz}}}
|x^{\mathrm{obs}}_e-\widehat x_e|.
$$

Here $\mathcal E_{\mathrm{buzz}}$ contains all observed-buzz events and
$x^{\mathrm{obs}}_e$ is the observed position. There is no team- or
question-level batching: sum one absolute error per event, then divide by the
number of events. A MAE of 0.10 is an average miss of about 10% of a question's
length.

The evaluator also reports the median absolute error:

$$
\operatorname{BuzzPositionMedianAE}
=\operatorname{median}_{e\in\mathcal E_{\mathrm{buzz}}}
|x^{\mathrm{obs}}_e-\widehat x_e|.
$$

The median uses the same event errors but selects their middle value instead
of summing them, so outliers matter less. Because either metric compares a
distribution mean with one observed draw per event, it includes irreducible
within-event spread and is best used comparatively. Older saved outputs may
predate buzz conditioning and therefore be biased late.

### Buzz-position bias

Both errors above are unsigned, so they cannot say whether predictions run
early or late. The signed companion is

$$
\operatorname{BuzzPositionBias}
=\frac{1}{|\mathcal E_{\mathrm{buzz}}|}
\sum_{e\in\mathcal E_{\mathrm{buzz}}}
(\widehat x_e-x^{\mathrm{obs}}_e),
$$

predicted minus observed, so positive means predicted too late. The overall
value is reported as `buzz_position_bias`, and the same signed mean and
median are repeated within the five fixed observed-position bands shared
with the correctness strata. The bands are the informative part: a model
that regresses predictions toward mid-question produces large positive bias
for early buzzes and negative bias for late ones while the overall row nets
out near zero, so the overall value alone must not be read as evidence of
unbiased timing.

The bands bin by **observed** position. Conditioning on the observed draw
means even a correctly specified model shows some regression-toward-the-mean
pattern across bands (events that landed unusually early carry positive
error mechanically), so band values are upper bounds on structural timing
bias. Binning by predicted position would answer the complementary
forecast-calibration question and is not currently reported.

**Related files:** `buzz_event_predictions.csv` contains one row per scored
event; the MAE and bias fields are in `csvs/tossup_metrics.csv`;
`csvs/buzz_position_bias.csv` holds the overall and per-band signed rows
(also rendered as the report's "Buzz-Position Bias" table);
`graphs/tossup/tossup_position_predictions.png` plots observed against expected
position per event; and `graphs/tossup/tossup_position_calibration.png` bins observed
position into ten fixed bands and compares mean predictions — the
conditional-mean comparison this section recommends over reading single-draw
errors.

### First-buzz timing distribution

For event $e$, let $\mathcal P_e$ be the players present and let $h_{iet}$ be
player $i$'s probability of buzzing at token $t$ conditional on no earlier
buzz. Independent player hazards are combined into the team hazard

$$
h^{\mathrm{team}}_{et}=1-\prod_{i\in\mathcal P_e}(1-h_{iet}).
$$

The product is the chance that every present player stays silent; subtracting
it from 1 gives the chance that at least one player buzzes. Survival through
earlier tokens times this team hazard gives first-buzz mass at token $t$.

Aggregation then proceeds separately for each selected tossup $j$:

1. Rescale every token position to 0–1 and assign its predicted first-buzz mass
   to one of 12 equal-width bins.
2. For each usable event, add the model's token mass to the 12 predicted-bin
   totals and its no-buzz mass to predicted outcome $D$. Add the observed event
   to one observed buzz bin, or to observed $D$ if nobody buzzed.
3. Divide every predicted and observed total by the same usable-event count.
   This produces the two 13-outcome distributions $\widehat P_j$ and $P_j$.

This timing reconstruction applies the fitted hazard at every token, including
the final token, and calls only the probability remaining after that token
dead. Fits recording `terminal_no_buzz_survival = tokens_1_through_T` were
trained with this same end-inclusive term. Older fits used survival before the
final token, so for them the displayed no-buzz mass is not the term that was
optimized.

The selected tossups come from the most frequently observed quartile and are
spread across mean empirical buzz position. An event is skipped if any rostered
player is absent from `players.csv`; the output's `events` column records the
denominator actually used.

**Related files:** `tossup_predictions.csv`, `players.csv`, and `tossups.csv`
supply the reconstruction inputs; `csvs/tossup_buzz_density_metrics.csv`
stores one row per selected tossup; and `graphs/tossup/tossup_buzz_density_fit.png`
plots the same 12 bins plus no-buzz mass.

## Bonus metrics

Let $r$ identify one team's response to one bonus and let $b\in\{1,2,3\}$
identify a part of that bonus. Then $y_{rb}$ is the observed part result (1 or
0), $p_{rb}$ is its predicted correctness probability, and $R$ is the total
number of bonus responses.

### Part-level classification

Part AUC, log loss, ECE, and accuracy use every $(r,b)$ row directly. The
part-level accuracy is reported as `part_accuracy`. For these micro metrics, all part
rows are one batch and each part has one vote. Thus a bonus question with ten
responses has five times the weight of one with two.

`part_accuracy_easy`, `part_accuracy_medium`, and `part_accuracy_hard` repeat
micro part accuracy separately for the source's declared difficulty labels.
Join `bonuses.parts[part_index].difficulty` by `bonus_id` and zero-based
`part_index`; position alone does not imply difficulty. Empty, missing, and
nonstandard labels go to `unknown`, never an inferred difficulty group.
`part_count_{easy,medium,hard,unknown}` records all denominators. Empty groups
have undefined accuracy. These fields are in `bonus_metrics.csv`; the long
table is `csvs/bonus_part_accuracy_by_difficulty.csv`, and the diagnostic
strata also include difficulty. Direct Python callers supply linked `tables`
to `evaluate_bonuses` for metadata enrichment; otherwise saved difficulty is
used when available, with missing labels explicitly unknown.

More explicitly, let $a_{rb}=1$ when thresholding $p_{rb}$ at 0.5 gives the
correct label and let $a_{rb}=0$ otherwise. For either grouping choice, let
$\mathcal G$ be the observed teams or bonus questions and let
$\mathcal A_g$ contain the response-part rows belonging to group $g$. Then

$$
\operatorname{MacroPartAccuracy}
=\frac{1}{|\mathcal G|}\sum_{g\in\mathcal G}
\frac{1}{|\mathcal A_g|}\sum_{(r,b)\in\mathcal A_g}a_{rb}.
$$

The inner sum counts correct part labels within group $g$ and divides by that
group's row count. The outer sum adds those group accuracies and divides by the
number of groups. Using teams for $\mathcal G$ gives
`part_accuracy_macro_team`; using bonus questions gives
`part_accuracy_macro_bonus`. Each group gets one
vote regardless of volume.

**Related files:** `bonus_part_predictions.csv` supplies the part rows;
`csvs/bonus_metrics.csv` stores the micro and macro metrics; and
`graphs/bonus/bonus_reliability.png` visualizes part-level calibration.

### Research-log bonus classification and difficulty ordering

[`RESEARCH_LOG_2.md`](../RESEARCH_LOG_2.md) records these additional tables
directly from saved fits. They are report calculations, not new automatic
outputs of the standard evaluator.

**Confusion counts and precision/recall/F1.** Predict correct at `p >= 0.5`.
For the overall table, correct is the positive class: TP is a predicted and
observed correct answer, TN a predicted and observed miss, FN a correct answer
predicted to miss, and FP a miss predicted to be correct. Pool counts over
held-out folds before calculating

$$
P=\frac{TP}{TP+FP},\qquad R=\frac{TP}{TP+FN},\qquad
F1=\frac{2TP}{2TP+FP+FN}.
$$

An undefined denominator gives an undefined score. The difficulty-specific
table treats the minority outcome as positive: incorrect for easy, correct
for medium and hard. The decision at exactly 0.5 still predicts correct.
Overall scores retain correct as positive across all difficulties; they are
not averages of the difficulty-specific scores. The matched rows restrict each
fold to the shared comparison's `scored_game_ids` before pooling; the seven
additional synergy variants retain their saved populations. Source files are
`fold_N/holdout/{compositional,synergy}/bonus_part_predictions.csv`,
`fold_N/team_irt_{1d,3d}/bonus_part_predictions.csv`, the comparison's
`fold_N/split.json`, and the bonus metadata labels.

**Difficulty-order accuracy.** Let the effective difficulty of part $b$ be
$D_b=d_b$ for scalar difficulty (`beta` in saved tables), or
$D_b=\sum_k r_{bk}d_{bk}$ for per-dimension difficulty (`r_k * beta_k`).
Use the saved posterior medians in that expression. Do not replace relevance
with uniform weights or divide scalar difficulty by discrimination. Join the
declared easy/medium/hard labels by bonus ID and part index. For each distinct
bonus question $j$ with exactly one finite part of each label, calculate

$$
O_j=\mathbf{1}[D_{j,e}<D_{j,m}<D_{j,h}],\qquad
\operatorname{OrderAccuracy}=\frac{1}{|\mathcal J|}\sum_{j\in\mathcal J}O_j.
$$

Ties and either reversal score zero. Missing or nonstandard triples are
excluded with their counts reported. Each fitted bonus gets one vote,
regardless of how often it was heard. This checks parameter ordering, not
response classification or held-out prediction.

The full-season diagnostic uses fresh `season_2024_25` in-sample fits, covering
Fall 2024 through Nationals 2025. It includes every fitted complete bonus in
that season, independently of the calendar-2024 held-out scoring exclusions.
For a mirror-site mean, average distinct fitted parts of a declared difficulty
heard at that site. Check easy < medium < hard separately at each site.
Season averages over sites give each site equal weight. For question-set
means, count each distinct fitted part once across all mirrors; mirrors sharing
a set are not different difficulty tiers. Within each declared difficulty,
compare the four set means against Fall < Winter < Regionals < Nationals;
report strict full-order agreement and the number of correctly ordered pairs
out of six. A tie earns no correctly ordered pair.

**Related files:** the full-season run is
`results/compirt/in_sample/common/bonus-difficulty-season-2024-25/`.
Its `configuration.json` maps model names to saved `bonus_parts.csv` tables.
`bonus_difficulty_order.csv` retains each bonus's three effective difficulties
and 0/1 score; `difficulty_means_by_tournament.csv`,
`difficulty_means_by_set.csv`, and `difficulty_summary.csv` retain the
aggregates. Cross-model difficulty scales can differ. Team IRT uses distinct
team parameters for each tournament and has disconnected question-set blocks,
so agreement with the external tier order is descriptive rather than proof
of an identified common difficulty scale.

**Uncertainty in within-bonus ordering.** The follow-up in
[`RESEARCH_LOG_2.md`](../RESEARCH_LOG_2.md#how-certain-are-the-individual-bonus-orderings)
covers the full-season `dd/multidim-difficulty-synergy` fit only. Retain its
original $O_j$ and add point gaps $G_{j,em}=D_{j,m}-D_{j,e}$ and
$G_{j,mh}=D_{j,h}-D_{j,m}$, using $D$ at saved parameter medians as above.
Positive gaps follow the declared order; zero is a tie and negative is a
reversal. Do not substitute the posterior median of a gap for this point gap.

For each bonus, draw relevance and difficulty from the saved mean-field
AutoNormal approximation, recompute each part's $D=r^\top d$, and calculate

$$
\widehat p_j=\frac{1}{M}\sum_{s=1}^{M}
\mathbf{1}[G^{(s)}_{j,em}>0\ \text{and}\ G^{(s)}_{j,mh}>0].
$$

Both gaps must use the same sampled medium-part difficulty. Do not multiply
their marginal ordering probabilities or subtract marginal interval endpoints.
The gap intervals are the 2.5% and 97.5% quantiles of sampled differences.
$\widehat p_j$ measures support for parameter ordering, not response accuracy.
At least 95% and at most 5% are descriptive support thresholds; the full
probability is retained for every bonus.

The saved fit has quantiles but no joint draw files. For this model, `beta`
is Normal and `log(r)` is Normal in the AutoNormal guide. Reconstruct each
coordinate with $\mu=q_{0.5}$ and
$\sigma=(q_{0.975}-q_{0.025})/[2\Phi^{-1}(0.975)]$, applying log to the `r`
quantiles first. Draw all coordinates independently as the fitted guide does,
then exponentiate `log(r)`. Use 20,000 draws per bonus and NumPy PCG64 seed 42;
the maximum Monte Carlo standard error of an individual probability is about
0.00354. These approximate intervals omit posterior correlations, uncertainty
in frozen Stage-1 skills, and variation across optimization runs. This
reconstruction is specific to the selected model's Normal/positive sites;
it is not a generic recipe for simplex relevance or other joint distributions.

**Sensitivity to number of attempts.** Count distinct `response_id` values
per bonus in the selected fit's predictions. Each response contains three
distinct part rows and counts once. Summarize 1–9, 10–19, 20–29, and 30+ attempts,
both across the season and within each question set. Within a group, give
each distinct bonus one vote: sum $O_j$ then divide by the number of bonuses;
report that denominator. The 10+ sensitivity excludes bonuses from this
summary only; all parameters still come from the unchanged full-season fit.
Differences between groups are descriptive and can reflect question-set or
question differences as well as exposure.

The run directory stores `bonus_difficulty_uncertainty.csv` (per-bonus values),
`bonus_difficulty_uncertainty_by_attempts.csv` (group summaries), and
`bonus_difficulty_uncertainty_method.json` (inputs, sampling and checks).
These are report calculations, not new standard-evaluator outputs.

### Exact three-part accuracy

After thresholding each part at 0.5, exact accuracy is

$$
\operatorname{ExactAccuracy}
=\frac{\#\{r:\text{all three part labels for response }r\text{ are correct}\}}
{R}.
$$

Group the rows by `response_id`. A response receives 1 only if it has exactly
three saved parts and all three thresholded labels match; otherwise it receives
0. Sum those marks and divide by $R$, giving every response one vote.

**Related files:** `bonus_part_predictions.csv` supplies the grouped rows and
`csvs/bonus_metrics.csv` stores the result as `exact_acc`. There is no dedicated
exact-accuracy graph.

### Bonus response scores used by PPB

`team_predictions.csv` contains one row per bonus response. Its `total_points`
and `predicted_points` columns are

$$
S_r=10\sum_{b=1}^{3}y_{rb},
\qquad
\widehat S_r=10\sum_{b=1}^{3}p_{rb}.
$$

Within response $r$, sum the three binary outcomes and multiply by 10 to get
the observed score. Sum the three probabilities and multiply by 10 to get the
model's expected score; this may be non-integer. These are intermediate values
used by PPB below, not separately reported standard metrics.

**Related files:** `team_predictions.csv` stores the two values, and
`graphs/bonus/bonus_response_score_predictions.png` groups `predicted_points` by
observed score. That graph is response-level; it is not a PPB plot.

### Points per bonus

For team $u$, let $\mathcal R_u$ be every bonus response that team heard in the
evaluated run, across all of its games. Let $U$ be the number of teams. Points
per bonus is total bonus points divided by bonuses heard, which is equivalently
the mean score of those bonuses:

$$
\operatorname{PPB}_u
=\frac{\sum_{r\in\mathcal R_u}S_r}{|\mathcal R_u|}
=\operatorname{mean}_{r\in\mathcal R_u}(S_r),
$$

$$
\widehat{\operatorname{PPB}}_u
=\frac{\sum_{r\in\mathcal R_u}\widehat S_r}{|\mathcal R_u|}.
$$

For team $u$, sum response scores across **all games** and divide by bonuses
heard. Predicted PPB uses the same responses and denominator. Games are not
scored separately and then averaged.

The reported metric is team-level macro MAE:

$$
\operatorname{PPBMAE}
=\frac{1}{U}\sum_{u=1}^{U}
|\operatorname{PPB}_u-\widehat{\operatorname{PPB}}_u|.
$$

Take one absolute PPB gap per team, sum the $U$ gaps, and divide by $U$. Every
team gets equal final weight regardless of games or bonuses heard. A PPB MAE of
1.2 means an average team-level error of 1.2 points per bonus. Over- and
under-predictions may cancel **within** a team's pooled PPB before the absolute
value is taken; averaging absolute part or response errors would be a different
metric.

**Related files:** `team_predictions.csv` supplies one response row at a time;
`csvs/bonus_metrics.csv` stores `ppb_mae`; and
`graphs/bonus/bonus_team_ppb_predictions.png` scatters predicted against observed
PPB with one point per team, the same pooling as the metric.

### Bonus-only team PPG and tournament rankings

Observed response points are recorded `total_points`; predicted response
points are the expectation `10 * sum(predicted_correct)` across three parts.
These are predictions conditional on the recorded bonus opportunities; the
metric does not replay which team earns a bonus.

For team u in tournament t, sum its bonus points across responses,
then divide by its unique games. The game's `team_ids` define participation,
including teams that hear no bonuses and games with zero bonuses. No player
attribution is used. A tournament is a mirror-site `tournament_id`.

The caller must supply tables for exactly the evaluated game population.
Exclude an entire game if any recorded bonus response is missing, any response
lacks the three distinct parts 0/1/2, or predictions include unrecorded responses.
Duplicate response-part predictions, invalid probabilities/labels, inconsistent
response identities, and disagreements with recorded response scores are errors.
Predicted team and tournament IDs must agree with game metadata. Games must have
two distinct teams. Exclusion and included-game counts are saved in the scalar
metrics. Both PPG and margin metrics use these same complete games.

Each team's `absolute_error` is `abs(predicted_bonus_ppg - observed_bonus_ppg)`.
Average these errors equally across teams within each tournament to get its
`bonus_ppg_mae`. This is the error in tournament PPG, not the mean of absolute
game-score errors. Spearman compares observed and predicted team PPG within
that tournament using average ranks for ties. Constant or single-team
rankings have undefined correlation, recorded as NaN.

Pool disjoint held-out game predictions **before** computing full-tournament
PPG or ranks. `tournament_team_bonus_ppg_mae` averages tournament MAEs
equally. `tournament_team_bonus_ppg_spearman` averages defined tournament
correlations equally; `bonus_ppg_spearman_tournaments` records the denominator.
No fold-ranking averages substitute for this pooling.

Audit outputs under `csvs/` are `bonus_team_game_predictions.csv`,
`bonus_team_ppg_leaderboard.csv` (one team/tournament row, including its
absolute error), and `bonus_team_ranking_metrics.csv` (one tournament row,
with team/game counts, PPG MAE, Spearman, and game margin MAE).
The compositional-fold runner delegates scoring and pooling to
`compirt_eval/scenario_b_bonuses/folds.py`, which writes pooled ledgers under
`aggregate/<arm>/`. The historical familiar/new-roster comparison's generator
writes these under `aggregate/bonus_metrics/<model>/<arm>/`, plus
`bonus_ppg_summary.csv`, `bonus_ppg_by_tournament.csv`, and
`bonus_metrics_report.md`. PPG uses all scored rosters together, since a
team's tournament may contain both familiar and new lineups.

`aggregate/pooled.csv` and `pooled.json` contain scores recomputed from pooled
predictions; `per_fold.csv` contains fold metrics and audits, and
`fold_mean_std.csv` describes their mean and standard deviation. Generated
`aggregate/report.md` links fold artifacts and labels the saved
synergy form, link, and dimensions. `--report-only` rewrites the Markdown from
these artifacts.

### Bonus-only game margins

For each complete game, order its two teams by ID as A and B. Sum observed
and expected bonus points separately for each team, including a zero when a
team hears no bonuses. The observed signed margin is `observed_A - observed_B`;
the predicted margin is `predicted_A - predicted_B`.
`bonus_game_margin_mae` is the mean of
`abs(predicted_margin - observed_margin)` across games, with each game counted
once. Reversing A and B leaves the error unchanged. This is a bonus-points
margin, with no tossup points or predicted bonus ownership.

`bonus_game_margin_mae_games` is the denominator. The per-tournament table
also reports the mean margin error within each tournament; the overall scalar
weights games equally, not tournaments. `bonus_game_margin_predictions.csv`
records team IDs, observed/expected team points, both signed margins, and each
game's absolute margin error. Empty populations have undefined MAE.

## Player summary

### Observed-buzz summary

`player_buzz_summary.csv` groups actual first-buzz rows by player. For player
$i$, let $\mathcal E_i$ be that player's recorded first-buzz events and let
$p_{ie}$ be fitted correctness at the observed buzz position:

$$
\overline p_i
=\frac{1}{|\mathcal E_i|}\sum_{e\in\mathcal E_i}p_{ie}.
$$

Sum the fitted probabilities over that player's observed buzzes and divide by
the number of buzzes. Each buzz has one vote within the player; players are not
then averaged into a metric. This is conditional buzz accuracy, **not** skill,
latent theta, buzz volume, or points per game. Shot selection matters: cautious
late buzzers can have a high value without being stronger players.

**Related files:** actual buzz rows come from `tossup_predictions.csv`;
`player_buzz_summary.csv` stores one aggregated row per player beside that
input file. Model-based player PPG and tournament rankings come from the
token-threshold replay described under
[Tossup ownership, game margins, and tournament PPG](#tossup-ownership-game-margins-and-tournament-ppg).

## Extended probabilistic diagnostics

These metrics should be read together. A model can rank responses well while
assigning poorly calibrated probabilities, and sharp forecasts are useful only
when their calibration remains credible.

| Metric | Question | Better |
| --- | --- | --- |
| Accuracy lift over all-correct | Does thresholding beat always predicting a correct response? | Higher |
| Binary Brier score | Are correctness probabilities close to binary outcomes? | Lower |
| ECE | Do probability groups occur at their advertised frequency? | Lower |
| Sharpness | Does the model make informative probabilities away from 0.5? | No standalone direction |
| Bonus RPS | Is the predicted ordered 0/10/20/30 distribution close to the observed score? | Lower |
| Bonus total-score log loss | How much probability reaches the observed 0/10/20/30 score? | Lower |
| Joint tossup event log loss | How much probability reaches the observed dead or player/token/correctness event? | Lower |
| Integrated Brier score | Is the complete buzz-by-position probability curve accurate? | Lower |
| First-buzzer top-1/MRR/log loss | Does the model identify the first player to buzz? | Higher / higher / lower |

### Brier score, all-correct baseline, and sharpness

For a binary outcome $y$ and predicted probability $p$, the Brier score is

$$
\operatorname{Brier}=\frac{1}{N}\sum_i(p_i-y_i)^2.
$$

It is bounded, uses the full probability, and penalizes confident errors more
than cautious ones. `all_correct_accuracy` is simply the observed correct rate
because the reference policy always predicts correct;
`accuracy_lift_over_all_correct` subtracts that reference accuracy from the
model's thresholded accuracy. It is not a majority-class oracle.

Sharpness describes predictions without outcomes. The evaluator records the
standard deviation and 10/50/90 percentiles of $p$, plus mean Bernoulli
variance $\operatorname{mean}(p(1-p))$. Do not optimize these values alone:
extreme but miscalibrated probabilities are sharp and useless.

`prediction_diagnostics_by_stratum.csv` repeats classification and sharpness
metrics by tier/category and, for tossups, five fixed relative-position bands.
Those bands are equal-width fifths of the question, not equal-count empirical
quantiles. Always inspect the observation count before interpreting a stratum.
`graphs/diagnostics/prediction_ece_by_stratum.png` draws the per-stratum ECE values as
bars (counts on the tick labels) against each scenario's aggregate ECE line.

### Bonus ranked probability score

The evaluator convolves three part probabilities into a distribution over
0, 10, 20, and 30 points. For the three ordered-score boundaries it compares
the predicted and observed cumulative distributions:

$$
\operatorname{RPS}=\frac{1}{3}\sum_{k=1}^{3}
(\widehat F(k)-F(k))^2.
$$

Zero is perfect. Because it scores cumulative probabilities, placing mass one
score level away is penalized less than placing it several levels away. Only
complete standard three-part responses are eligible;
`ranked_probability_score_responses` records the denominator and
`bonus_score_probability_predictions.csv` preserves the four probabilities,
the probability assigned to the observed score, RPS, and score log loss.

### Bonus total-score log loss

For observed score index $y\in\{0,1,2,3\}$ and convolved score distribution
$p$, each response receives

$$
-\log p_y.
$$

`bonus_total_score_log_loss` averages this value over the same complete
three-part responses used by RPS. It rewards probability assigned directly to
the realized total, while RPS also reflects the distance between score levels.

### Joint tossup event log loss

The evaluator groups `tossup_predictions.csv` by `event_id` and reconstructs
the fitted event factor. For a dead tossup, the probability is the product of
roster survival terms. For a buzz by player $i$ at token $t$ with correctness
$y$, the probability is

$$
\left(\prod_{i'} S_{i'}(t)\right)
\left[1-\prod_{i'}(1-h_{i'}(t))\right]
\frac{\exp(\eta_i(t))}{\sum_{i'}\exp(\eta_{i'}(t))}
p_i(t)^y(1-p_i(t))^{1-y}.
$$

`joint_tossup_event_log_loss` is the mean negative log probability across
events. `tossup_joint_event_scores.csv` records every factor, the realized
event probability, and its log loss.

### Survival curve and first-buzzer identity

At each normalized question position, the time-dependent Brier score compares
the predicted probability that someone has buzzed with whether the event has
actually produced a buzz. Integrating that curve gives
`integrated_brier_score`. Terminal no-buzz outcomes are part of the curve.

Conditional on a buzz at a token, winner probabilities are proportional to
hazard odds, computed with softmax of the logits. Summing across tokens gives
the first-buzzer distribution used by top-1 accuracy, mean reciprocal rank,
and conditional log loss. `first_buzzer_predictions.csv` records these
probabilities. See [the first-buzz likelihood](../docs/first-buzz-likelihood.md)
for the model definition and run metadata.

`graphs/tossup/first_buzzer_identity.png` plots top-1 accuracy and MRR by roster
size against the uniform 1/n baseline.

### Tossup ownership, game margins, and tournament PPG

Standard downstream scoring uses an end-to-end, tossup-only token replay (outcome
schema version 3). For each recorded game and its actual question lineups,
read tokens 1 through T. The first eligible player whose **current-token** buzz
probability is at least 0.5 buzzes. This is neither a cumulative-hazard threshold
nor an argmax over integrated first-buzzer/scorer probabilities. Same-token ties
use uniform random choice over eligible players, with seed 42 and a stable
event-ID hash. Results are reproducible across roster and event ordering.

At that token, calibrated correctness of at least 0.5 earns +10 and ends the
question. An early first miss earns -5, locks out the entire team, and resumes
reading at the next token for the opponent. A bounceback miss scores zero. The
terminal cell represents the post-reading window, so a terminal miss also
scores zero. If nobody reaches the buzz threshold, the tossup is dead. Replay
decisions use fitted curves at the simulated token, never observed buzz times
or observed correctness. Ground truth uses literal recorded values, including
bouncebacks and zero-point late misses.

`first_buzzer_team_replay_accuracy` compares the replay's first team to the
observed first team on questions with an observed buzz. Scorer player/team
replay accuracies include `no_score` and cover every replayed question. The
separate first-buzzer probability diagnostics retain their top-1/MRR/log-loss
meaning; they do not drive scores, game winners, or PPG.

Games sum **replayed points** for each team and compare the resulting winner
and signed tossup margin with recorded tossup totals. Actual ties are omitted
from decisive-winner accuracy; margin MAE includes ties. The zero-margin MAE
is the no-information baseline. Winner Brier/log-loss and convolved margin
PMFs are retired: this deterministic replay does not produce win probabilities.

Player PPG divides replayed or recorded point totals by unique inferred-lineup
games, including games with no buzz or no points. Full-tournament rankings pool
single out-of-fold game predictions before computing PPG and ranks once.
Reports include Spearman, PPG MAE, and top-10 overlap with K=min(10,N), random
baseline K/N, and adjusted overlap (observed-K/N)/(1-K/N). Tournament metrics
are macro-averaged after pooling. Round summaries use the same replayed games.

Audit artifacts under `csvs/` include `tossup_outcome_predictions.csv` (with
full token/buzzer/correctness/points sequences), `tossup_player_predictions.csv`
(with `predicted_tossup_points`), `tossup_game_predictions.csv`,
`player_ppg_leaderboard.csv`, `player_ranking_metrics.csv`,
`tossup_round_metrics.csv`, and `tossup_outcome_metrics.csv`. Schema versions
invalidate cached expected-points leaderboards when aggregating old runs.

### Conditional correctness-only game-winner diagnostic

The separate [saved game-winner study](../results/compirt/holdout/common/game-winner-ablations/skills-lse-observed-position-correctness-and-token-replay-5fold/README.md)
compares the standard replay with skills-only and correctness-only team scores.
It does not replace the evaluator's game replay. Correctness-only scores use
each phase-0 player's canonical correctness logit at the observed first-buzz
cell, clamped to `1..T_j`; dead tossups use `T_j`. Both teams use the same cell.
Saved question relevance, difficulty, player correctness intercepts, and
terminal correctness intercepts apply. The studied fits have no correctness
calibration; the study rejects nonidentity calibration rather than ignoring it.

For each active team lineup, apply unnormalized temperature-1 LSE to these
player logits and sigmoid to the aggregate. Average the resulting team-question
scores over the game; the team with the larger mean is the predicted winner.
This score is a heuristic, not a calibrated team race probability or predicted
points total. No hazard parameters, observed correctness labels, observed
buzzer identity, or bounceback rows enter the score. Observed timing does enter,
so this is a conditional diagnostic, not an end-to-end forecasting comparison.

Use exactly the full replay's complete-game population and literal recorded
tossup-only winners. Exclude recorded ties, count predicted ties as incorrect,
and pool all decisive held-out games equally before calculating accuracy.
`summary.csv` records `correctness_accuracy`, its correct-game numerator,
`decisive_games`, and predicted tie counts. `game_predictions.csv` records the
team scores and decisions; `validation.json` records source hashes, event
counts, and dead-event counts. These artifacts live beside the study code.

## Difficulty and parameter figures

These figures carry no scalar metric; they answer model-inspection questions
the metrics cannot: does estimated difficulty actually decline over the
question (the pyramidality claim), where do transitions sit relative to real
buzzes, do latent dimensions differentiate, and what do the fitted parameter
populations look like. All of them replay posterior medians from the saved
`players.csv` / `tossups.csv` / `bonus_parts.csv`.

### Difficulty curves over buzz locations

`graphs/tossup/tossup_difficulty_curves.png` shows up to six tossups chosen
by the same rule as the first-buzz timing distribution diagnostic: from the
most frequently observed quartile, spread evenly across mean empirical buzz
position. Each panel draws the
fitted difficulty curve over a histogram of that tossup's observed first-buzz
positions — for scalar runs the Eq. 3 curve
$b_j(t)=\beta_j\,\sigma(\gamma_j(\mu_j - t/T_j))$, for per-dimension runs the
relevance-weighted sum $\sum_k r_{jk} d_{jk}(t)$. Archived TF-IDF runs plot the
effective difficulty $d' = d + \delta$ the model trained on, with the base
curve kept as a dashed reference. Buzz counts and difficulty use separate
y-axes: read curve shape and transition location against the histogram, and
treat the two vertical scales independently.

`graphs/tossup/tossup_difficulty_curves_by_dimension.png` repeats the same
six tossups for per-dimension runs, drawing each dimension's $d_{jk}(t)$ as a
thin line labeled with its relevance $r_{jk}$ and the r-weighted total in
black. This is where to check whether a tossup's difficulty is carried by one
dimension or several. Opt-in larger galleries split across numbered files
(`..._01.png`, `..._02.png`, …) so high-dimensional runs stay readable.

`graphs/tossup/pyramidal_difficulty_curve_distribution.png` is the population
view: every tossup's curve is evaluated on a 150-point position grid, and the
figure shows the median with 25th–75th and 5th–95th percentile bands. A
monotonically falling median with bands that narrow toward the giveaway is
the fitted-model statement of pyramidal question structure.

### Parameter distributions

`graphs/bonus/bonus_prediction_distributions.png` shows evaluated part
probabilities and aggregate ability $A_k(T)$ once per part row, plus the
synergy contribution $\Phi(T)$ once per bonus response. Its statistics are in
`csvs/bonus_prediction_distribution_summary.csv`. These are distributions
over evaluated observations at saved parameter medians, not uncertainty
intervals. For `bonus_aggregation=noisy-or`, the saved `aggregate` is the
effective team logit including difficulty, and synergy is zero. The synergy
contribution is the raw pair sum for either `synergy_form`.
With the default `synergy_link=additive`, a negative $\Phi(T)$ lowers the
bonus logit. With `synergy_link=multiplicative`, the full base logit
$(A_k(T)-\beta_k)$ is multiplied by $1+\Phi(T)$ before optional calibration;
the logit change depends on the part as well as the lineup. Neither setting
establishes a causal teamwork effect.

For `bonus_difficulty=multidim`, LSE pools players separately on each skill
axis: `ts_k = tau * logsumexp_i(theta_ik / tau)`. The saved `aggregate` is
`sum_k r_bk * ts_k`, and the effective difficulty subtracted from it is
`sum_k r_bk * beta_bk`. The same synergy links and calibration follow this
base logit. Parameter dashboards use `r_1..K` and `beta_1..K`; responses
identify only `sum_k r_bk * beta_bk`, so individual difficulty coordinates
follow their prior.

Three dashboards under `graphs/parameters/` (plus a synergy one when that
branch saved profiles) show each fitted parameter class as a
histogram-backed density: a deterministic Gaussian KDE with Scott's-rule
bandwidth over the posterior medians (inputs above 10,000 values are evenly
subsampled, so the curve is reproducible). Dotted vertical lines mark each
series median; signed parameters get a dashed zero reference.

- **Player** (`pyramidal_player_parameter_distributions.png`): buzz threshold
  `c`, the skill coordinates `theta_k` overlaid, and the skill magnitude
  `theta_norm`.
- **Tossup** (`pyramidal_tossup_parameter_distributions.png`): difficulty
  amplitudes `beta`, transition sharpness as `log10(gamma)`, transition
  locations `mu`, and the vector weight coordinates plus norm — labeled
  `alpha` or `r` following the saved schema's naming convention.
- **Bonus part** (`bonus_part_parameter_distributions.png`): part difficulty
  `beta` (scalar and/or per-dimension) and the bonus vector weight
  coordinates plus norm.
- **Synergy** (`synergy_parameter_distributions.png`): profile coordinates
  `psi` and their norm, plus the derived pairwise synergy scores and
  team-level contributions.

Each dashboard also writes its descriptive statistics —
`csvs/pyramidal_parameter_distribution_summary.csv` and
`csvs/bonus_parameter_distribution_summary.csv`, one row per parameter with
observations, mean, standard deviation, and the 5/25/50/75/95 percentiles.
These are the rows `docs/summary.md` renders as its parameter tables.

Frozen bonus replay reads these parameters from the saved `train_compositional`
source in its summary, falling back to the matching `train/` branch for older runs
when `holdout/` contains predictions only. The CSV records `parameter_source`;
the plots label the training source. Pair and team contributions in that
dashboard describe training rosters. These densities summarize variation
across fitted posterior medians, not posterior uncertainty for one parameter.

### Bonus-model comparison

The [shared bonus comparison](../results/compirt/comparisons/bonuses/dd-bernstein-and-team-irt-5fold/README.md)
uses the same bonus metrics on a matched subset of the existing whole-game
folds. It excludes entire games requiring unseen training teams/parts or
missing any reference prediction, recording the exclusions per fold. All arms
share identical parts and complete games; zero-bonus games remain in game
denominators. Pooled team metrics are computed after concatenating folds.
Subject, declared difficulty, and subject-by-difficulty binary metrics give
each observed part one vote and retain Unknown labels. Study artifacts are
`aggregate/metrics.csv`, `metrics_by_fold.csv`, `metrics_by_question_type.csv`,
and per-model team/game tables. The report uses the existing compositional
metric columns and difficulty/PPG/margin layout. DD-Bernstein uses the normalized
first-buzz skill source, alongside Team IRT 1D/3D and the multidimensional
references. All seven arms use 127,986 parts / 42,662 bonuses / 2,330 complete
games; the two additional game exclusions relative to the compositional-only
population enforce team-IRT training coverage. Roster strata classify exact
team/active-lineup combinations from training bonuses only and share that
classification across every arm. `metrics_by_question_type.csv` contains these
`roster_group` rows as well as question strata. Source hashes and the full
exclusion list are saved with the comparison.

The bonus research log also reports minority-class precision, recall, and F1
by declared difficulty from these saved part predictions. Correctness is
classified with `p >= 0.5`; the scored positive class is incorrect (0) for easy
and correct (1) for medium and hard. Pool TP, FP, and FN across the five held-out
folds within each difficulty before computing `TP / (TP + FP)`,
`TP / (TP + FN)`, and `2 TP / (2 TP + FP + FN)` respectively. Join source
difficulty by `bonus_id` and zero-based `part_index`. The seven matched arms use
42,662 parts per difficulty; additional synergy variants in the log keep their
42,700-part populations. These summaries appear only in the `RESEARCH_LOG_2.md`
table.

`compirt_eval/synergy_comparison/` (run through
`run_scripts/common/run_synergy_comparison.py`) reads the
no-synergy and synergy branches' `bonus_metrics.csv`, writes the per-metric
delta table (`bonus_model_comparison.csv` / `.md`) and a side-by-side panel
figure `bonus_model_comparison.png` under the comparison output directory,
and refreshes both branches' `docs/summary.md`. The ordinary evaluator does
not produce this figure.

### How to read these figures

Everything here is a posterior-median replay: bands and densities show
variation **across fitted entities** (tossups, players, parts), not posterior
uncertainty about any one of them. Unconstrained latent coordinates are
identified only up to rotation and sign, so read the coordinate overlays for
exchangeability and spread, and base conclusions on rotation-invariant
quantities — norms, weighted difficulty curves, logits. Topic names supplied
at evaluation time only relabel coordinate legends; they do not change what
was fit.
