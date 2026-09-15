# Superseded game and tournament evaluations

These Research Log tables used the earlier integrated first-buzz/scorer
probabilities, expected points, and convolved game-margin distributions. They
are historical results, not token-threshold replay evaluations. The current
[Research Log](../../../../../../RESEARCH_LOG.md) replaces them with the September 13, 2026
replay using 0.5 buzz/correctness thresholds and seeded random token ties.

Corrected downstream results for the same held-out models are organized by the
question they answer. Actual targets include every recorded tossup value,
including post-neg conversions and zero-point late misses. Predicted questions
use the fitted first-buzz race and an opponent-only continuation after an early
miss. Question-level score distributions are combined exactly across each
game. Accuracy is higher-is-better; point errors are lower-is-better. The
zero-predicted-margin baseline has an average error of 57.15 points.

#### Direct prediction quality

This is the headline table. “Scoring player/team” means who eventually earns
the +10, including a possible opponent conversion after a neg. “Margin error” is the average absolute error in the predicted
tossup-point difference between the teams, measured in points. First-buzzer
accuracy uses the 45,995 questions with a recorded buzz. Scoring-player and
scoring-team accuracy use all 46,640 questions, with `no_score` as the outcome
whenever no player earned +10.

| Model | First-buzzer player accuracy | Tossup scoring-player accuracy | Tossup scoring-team accuracy | Tossup-only game winner accuracy | Average tossup margin error |
| --- | ---: | ---: | ---: | ---: | ---: |
| Single-difficulty Bernstein 5/5/2, legacy | **40.07%** | **35.56%** | 57.04% | 75.32% | 40.68 |
| DD-Bernstein 3/3/2, no terminal | 38.08% | 33.01% | 56.37% | 75.41% | 39.87 |
| DD-Bernstein 3/3/2, terminal | 37.99% | 35.08% | **58.72%** | 76.25% | **39.82** |
| Simplex relevance, no terminal | 34.04% | 26.66% | 51.78% | 75.86% | 41.86 |
| Simplex relevance, terminal | 33.67% | 30.28% | 56.98% | 75.33% | 42.49 |
| Simplex relevance, locations + terminal | 35.16% | 32.41% | 58.02% | **76.34%** | 40.53 |
| Simplex relevance 3/3/0.67, locations + terminal | 35.11% | 32.34% | 58.11% | 76.29% | 40.53 |
| Simplex relevance, locations + terminal + player `a_i` | 36.09% | 33.55% | 58.29% | 76.07% | 40.71 |
| Perceived difficulty, unconstrained `alpha` | 35.10% | 15.06% | 34.75% | 73.44% | 46.26 |
| Perceived difficulty, `alpha > 0` | 39.18% | 30.51% | 54.18% | 72.90% | 44.78 |
| Perceived difficulty, three-slice `alpha,beta` | 37.50% | 25.98% | 49.33% | 69.68% | 47.34 |
| Perceived logit, unconstrained `alpha` | 35.15% | 16.48% | 44.91% | 70.17% | 47.81 |
| Perceived logit, `alpha > 0` | 39.18% | 17.73% | 40.44% | 65.19% | 53.67 |
| DD linear spline | 39.74% | 34.43% | 56.22% | 76.30% | 40.35 |
| Monotone DD linear spline | 32.47% | 24.04% | 41.89% | 65.48% | 50.85 |

#### Win-probability diagnostics

These are secondary diagnostics rather than headline prediction tasks. Brier
and log loss evaluate whether a model's numerical win probabilities are
trustworthy, not merely whether its selected winner is right. Lower is better.
Team-buzzed-first accuracy is retained here because it diagnoses team ownership
of the first attempt, but does not say which team ultimately scores.

| Model | Team-buzzed-first accuracy | Tossup winner Brier | Tossup winner log loss |
| --- | ---: | ---: | ---: |
| Single-difficulty Bernstein 5/5/2, legacy | **66.34%** | 0.1666 | 0.4985 |
| DD-Bernstein 3/3/2, no terminal | 65.57% | **0.1580** | **0.4762** |
| DD-Bernstein 3/3/2, terminal | 65.62% | 0.1582 | 0.4765 |
| Simplex relevance, no terminal | 63.91% | 0.1638 | 0.4931 |
| Simplex relevance, terminal | 63.95% | 0.1682 | 0.5057 |
| Simplex relevance, locations + terminal | 64.54% | 0.1612 | 0.4861 |
| Simplex relevance 3/3/0.67, locations + terminal | 64.64% | 0.1613 | 0.4864 |
| Simplex relevance, locations + terminal + player `a_i` | 64.67% | 0.1609 | 0.4849 |
| Perceived difficulty, unconstrained `alpha` | 63.59% | 0.1773 | 0.5333 |
| Perceived difficulty, `alpha > 0` | 66.06% | 0.1821 | 0.5405 |
| Perceived difficulty, three-slice `alpha,beta` | 65.27% | 0.1982 | 0.5814 |
| Perceived logit, unconstrained `alpha` | 62.44% | 0.1933 | 0.5674 |
| Perceived logit, `alpha > 0` | 65.75% | 0.2229 | 0.6367 |
| DD linear spline | 66.24% | 0.1617 | 0.4893 |
| Monotone DD linear spline | 60.19% | 0.2358 | 0.8057 |

#### Tournament player-leaderboard quality

Player rankings pool all five disjoint held-out folds first, so each tournament
is ranked once using every covered game. Rank correlation measures agreement of
the complete ranking from -1 to 1. PPG error is the average absolute difference
between predicted and recorded tossup PPG. Random top-10 overlap is `K/N`, and
adjusted overlap removes that chance level.

| Model | PPG rank correlation | Average PPG error | Top-10 overlap | Random top-10 overlap | Chance-adjusted top-10 overlap |
| --- | ---: | ---: | ---: | ---: | ---: |
| Single-difficulty Bernstein 5/5/2, legacy | 0.8778 | 6.97 | 77.93% | 23.11% | 71.50% |
| DD-Bernstein 3/3/2, no terminal | 0.8892 | 5.95 | 79.66% | 23.11% | 73.72% |
| DD-Bernstein 3/3/2, terminal | 0.8884 | 5.18 | 77.59% | 23.11% | 71.73% |
| Simplex relevance, no terminal | 0.8860 | 6.84 | 79.31% | 23.11% | 73.12% |
| Simplex relevance, terminal | 0.8753 | 5.90 | 76.21% | 23.11% | 69.58% |
| Simplex relevance, locations + terminal | 0.8814 | **5.10** | 78.28% | 23.11% | 72.11% |
| Simplex relevance 3/3/0.67, locations + terminal | 0.8797 | 5.15 | 78.28% | 23.11% | 72.12% |
| Simplex relevance, locations + terminal + player `a_i` | 0.8759 | 5.25 | 77.93% | 23.11% | 71.66% |
| Perceived difficulty, unconstrained `alpha` | 0.8920 | 9.76 | **82.07%** | 23.11% | **76.70%** |
| Perceived difficulty, `alpha > 0` | 0.8821 | 9.21 | 78.28% | 23.11% | 71.69% |
| Perceived difficulty, three-slice `alpha,beta` | 0.8696 | 11.13 | **82.07%** | 23.11% | 76.65% |
| Perceived logit, unconstrained `alpha` | 0.8346 | 7.70 | 71.03% | 23.11% | 62.35% |
| Perceived logit, `alpha > 0` | 0.8679 | 13.80 | 78.62% | 23.11% | 71.81% |
| DD linear spline | **0.8963** | 6.18 | 81.03% | 23.11% | 75.63% |
| Monotone DD linear spline | 0.4229 | 12.13 | 54.14% | 23.11% | 36.64% |


## Superseded interpretation and limitations

### Tossup ownership, game outcomes, and player leaderboards

First-buzzer mass determines phase-0 player/team ownership. An incorrect early
buzz then starts an opponent-only suffix race, so positive-scorer probabilities
now include post-neg conversions and `no_score` only when neither phase
converts. Actual player/team points come from the literal recorded values,
including −5, 0 and +10 outcomes.

Each question yields a discrete signed-margin PMF. Exact convolution across a
game produces strict regulation-win and tie probabilities; binary winner
probability splits the unmodeled overtime 50/50. Accuracy, Brier and log loss
are reported against the recorded tossup-point winner. The separate seeded
match simulator adds bonus draws.

Tournament leaderboards pool every covered game's single out-of-fold player
point numerator and game denominator before computing PPG and ranks. Raw
top-10 overlap is accompanied by its random `K/N` expectation and a
chance-adjusted value. Per-question, player, game and tournament CSVs live under
each evaluation's `csvs/`; aggregate backfill derives them from saved fits
without retraining.

No one model leads every corrected target. Legacy single difficulty leads
first-buzzer-player and tossup scoring-player accuracy; terminal Gamma
DD-Bernstein leads tossup scoring-team accuracy and average margin error;
simplex locations plus terminal leads tossup-only game-winner accuracy; no-terminal
Gamma DD-Bernstein has the lowest winner-probability errors; and the
unconstrained DD spline leads pooled PPG rank correlation. Frozen skills has
not been evaluated on these downstream targets.

## Limits and next experiments

The main unresolved issues are repeated development-fold selection, one
optimization seed per historical arm (frozen uses one seed per fold), incomplete
matched ablations, and limited season coverage. Bootstrap intervals conditional
on saved predictions do not cover training randomness. Stage-1 results do not
establish bonus prediction, PPB, synergy, future-season skill transfer or match
simulation performance. Model selection should consider the timing distribution,
first-buzzer identity, conditional correctness and joint event scores together;
correctness accuracy alone does not establish a better tossup model.

The corrected downstream tables are sensible probabilistic replays, but they
are not claims about unseen rosters or a fully modeled quizbowl match. The five
test folds contain 2,332 of the 2,431 games in the filtered season; the other 99
are not eligible for this known-player/known-question matrix-infill protocol.
Bouncebacks reuse the fitted phase-0 hazards on the opponent-only suffix because
the historical models were trained without a separate bounceback likelihood.
Terminal misses are assumed to score zero, and modeled ties split an unmodeled
overtime 50/50.

