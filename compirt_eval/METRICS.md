# CompIRT evaluation metrics

This document is the metric contract for `compirt_eval`. It records which saved
rows enter each metric, the order of aggregation, the equation, the output
artifact, and interpretation limits. The standard, topic-weighted, and
topic-TF-IDF evaluators share these metric definitions; the topic evaluators
only change how saved difficulty and timing parameters are replayed.

This is also the canonical guide for the newer end-to-end diagnostics: Brier
score and bonus RPS, sharpness and strata, survival-curve metrics,
first-buzzer identity, match simulation, posterior predictive checks, and
parameter recovery. They are summarized in dedicated sections below rather
than in a second metric specification.

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
| Scenario C PPB MAE | Sum parts within each response → average responses within each `(game_id, team_id)` → take absolute game-team error → average errors | One vote per game-team | Lower |

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

Use 0.5 as the yes/no cutoff, then divide the number of matching labels by
$N$. Higher is better.

Binary log loss is

$$
\operatorname{LogLoss}
=-\frac{1}{N}\sum_{n=1}^{N}
\left(y_n\log p_n+(1-y_n)\log(1-p_n)\right).
$$

This sums one penalty per row and divides by $N$. Confident wrong predictions
receive a large penalty. Lower is better.

AUC is the ordinary ROC AUC and is undefined when the selected rows contain
only one outcome class.

AUC asks whether a randomly chosen correct row tends to rank above a randomly
chosen incorrect row. An AUC of 1 is perfect and 0.5 is chance-level. Higher
is better. Unlike the other shared metrics, AUC compares correct/incorrect
pairs rather than summing one independent loss per row.

Expected calibration error uses ten equal-width probability bins. Let $C_m$
be the set of row indices assigned to bin $m$:

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
it from 1 gives the chance that at least one teammate buzzes. Survival through
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
dead. The training likelihood's dead-tossup censoring term instead uses
survival before the final token. The displayed distribution is therefore an
end-inclusive diagnostic derived from the fitted hazards, not the exact
probability term that was optimized for dead tossups.

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
part-level accuracy is reported once, as `part_accuracy` (the formerly
duplicated `accuracy` column was dropped). For these micro metrics, all part
rows are one batch and each part has one vote. Thus a bonus question with ten
responses has five times the weight of one with two.

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

## Scenario C differences

Scenario C uses the shared part metrics and exact three-part accuracy. It adds
two response-level metrics: group parts by `response_id`, sum their predicted
points, then average either the absolute expected-score error
(`per_bonus_points_mae`) or the thresholded exact-score match
(`exact_score_accuracy`) across responses. Exact-score accuracy requires only
the correct 0/10/20/30 total; the identities of the predicted parts may differ.

$$
\operatorname{PerBonusPointsMAE}
=\frac{1}{R}\sum_{r=1}^{R}|S_r-\widehat S_r|.
$$

This is retained for Scenario C compatibility; because it compares an expected
score with one discrete outcome, it also includes outcome randomness.

Scenario C PPB has a different final unit from standard PPB. It averages bonus
responses within each `(game_id, team_id)`, takes one absolute PPB gap per
game-team, and averages those gaps. If $\mathcal H$ is the set of eligible
game-teams and $\mathcal R_h$ contains game-team $h$'s responses, then

$$
\operatorname{ScenarioPPBMAE}
=\frac{1}{|\mathcal H|}\sum_{h\in\mathcal H}
\left|
\operatorname{mean}_{r\in\mathcal R_h}(S_r)
-\operatorname{mean}_{r\in\mathcal R_h}(\widehat S_r)
\right|.
$$

The inner means pool responses within one game-team; the outer sum gives every
eligible game-team one vote. For a single C1--C4 scenario, game-teams
containing responses from multiple scenarios are excluded from PPB only; other
metrics retain their responses. `ppb_excluded_mixed_game_teams` records how
many were removed.

**Related files:** `csvs/scenario_metrics.csv` stores metrics by model, scope,
and scenario; `csvs/scenario_counts.csv` records the relevant denominators;
`csvs/synergy_comparison.csv` stores paired model differences; and
`graphs/scenario_c_auc.png` visualizes part-level AUC only.

## Player summary and ranking artifacts

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
input file.

### Tournament ranking comparison

The `compirt_eval/player_rankings/` study (run via
`run_scripts/common/run_player_rankings.py`) ranks players by $\overline p_i$
and compares that ordering with either

$$
\operatorname{actualPPG}_i
=\frac{\operatorname{actual tossup points}_i}{\operatorname{games}_i}
$$

or

$$
\operatorname{actualPP20}_i
=20\frac{\operatorname{actual tossup points}_i}
{\operatorname{tossups heard}_i}.
$$

Actual PPG sums a player's tossup points and divides by credited games. PP20
uses the same point sum but divides by tossups heard and scales to 20. These
measure scoring volume, unlike $\overline p_i$.

Because the source lacks game-specific lineups, every registered roster member
is credited with all team games and tossups heard. Sit-outs can therefore
inflate the denominator. The script correlates the two final rank-number
columns and computes top-$k$ overlap; it does not batch or average correlations
by game. Weak agreement is expected because conditional accuracy and scoring
volume are different quantities.

**Related files:** `player_ranking_comparison.csv`,
`player_ranking_comparison.md`, and `summary.json` are written under the
requested ranking output directory. This calculation has no rank graph.

### Noise-floor expected PPG

The noise-floor analysis instead models expected scoring over every tossup a
player faced. Let $G_i$ be games, $p_{iet}$ be correctness if player $i$ is
first to buzz in event $e$ at token $t$, and
$P_{iet}^{\mathrm{first}}$ be the probability of that first-buzz outcome:

$$
\widehat{\operatorname{PPG}}_i
=\frac{1}{G_i}\sum_e\sum_t
P_{iet}^{\mathrm{first}}
\left(10p_{iet}-5(1-p_{iet})\right).
$$

For each player, the inner sum combines mutually exclusive token-level
first-buzz outcomes within an event; the outer sum combines events; division by
$G_i$ converts total expected points to PPG. Expected score is +10 for correct
and -5 for incorrect; no-buzz contributes zero and powers are not modeled.
When teammates can buzz at the same token, team buzz mass is allocated among
them in proportion to their first-buzz-alone weights. This includes predicted
buzz frequency and accuracy, so it is neither actual PPG nor the observed-buzz
ordering above.

`run_scripts/multidimensional/multidim/run_multidim_noise_floor.py` compares the
resulting rankings across seeds using Kendall $\tau$, Spearman correlation,
top-$k$ Jaccard similarity, and per-player rank spread. Pass `--collect-only`
to analyze the completed fits without launching training.

**Related file:** the per-seed values are stored in
`results/compirt/in_sample/multidim/multidim-tanh-all2024-noisefloor/predicted_ppg_by_seed.csv`;
the remaining summaries are printed to standard output.

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
| Match-winner accuracy/Brier | Does the simplified simulator identify winners and useful win probabilities? | Higher / lower |

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
\left(\prod_{i'} S_{i'}(t)\right)h_i(t)
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

The model does not specify a unique winner when multiple players could buzz at
the same token. Evaluation allocates that token's event mass among players in
proportion to their “only this player buzzes” weights, with a normalized-hazard
fallback for numerical degeneracy. Summing token allocations gives the
first-buzzer distribution used by top-1 accuracy, mean reciprocal rank, and
conditional log loss. `first_buzzer_predictions.csv` makes the convention and
probabilities auditable; it must not be described as uniquely implied by the
training likelihood. `graphs/tossup/first_buzzer_identity.png` plots top-1 accuracy
and MRR by roster size against the uniform 1/n chance line, since the
aggregate top-1 value depends on how many players race for each buzz.

### Match-winner simulation

The seeded game diagnostic samples a first buzzer/time or dead tossup, samples
position-specific correctness, awards +10/-5, and samples a bonus total after
a correct buzz. Bonus distributions fall back from team to tier to the global
pool when needed. It reports winner accuracy, binary Brier score, expected
scores, and margin error.

This is an approximation, not an official score reconstruction: powers,
bouncebacks, overtime, strategic score effects, and corrections are omitted.
Fixed seeds must reproduce identical simulations.
`graphs/match/match_winner_reliability.png` shows whether the win probabilities are
calibrated; `graphs/match/match_score_predictions.png` scatters simulated against
actual game-team scores and should be read as a diagnostic of the simulator's
simplifications, not a score-accuracy claim.

### Posterior predictive checks and parameter recovery

Posterior predictive checks draw from the fitted AutoNormal guide and compare
capped, seeded replicated discrepancies with observed dead-tossup rates,
buzz-position mass, correctness patterns, and bonus-score frequencies. An
observed value outside the replicated interval is diagnostic evidence of model
misfit, not a standalone hypothesis-test decision.

Parameter recovery instead generates a small synthetic problem with known
truth, fits the normal SVI pipeline, aligns exchangeable dimensions, and
reports bias, RMSE, approximate 95% interval coverage, and interval width.
Raw latent-coordinate RMSE without alignment is not interpreted. The default
run is a smoke test; publication-level identifiability claims require repeated
seeds and design sweeps.

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
relevance-weighted sum $\sum_k r_{jk} d_{jk}(t)$. TF-IDF runs plot the
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

The standalone `tfidf.plot_tfidf_difficulty_curves` script writes
`tfidf_effective_difficulty_curves.png` flat into the graphs directory it is
given; the run scripts point it at the evaluation `graphs/` folder.

### Parameter distributions

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

### Bonus-model comparison

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
