# Multidim tanh all-2024 seed noise floor

This experiment measures how much the multidimensional CompIRT player ranking
moves solely because of SVI initialization. It refits the same Stage-1 model
under five random seeds and compares the resulting model-predicted points per
game (PPG). Observed PPG is not used because it is unchanged by the fit and
therefore has no seed noise floor.

## Setup

| Setting | Value |
| --- | --- |
| Data split | `year_2024`, in sample |
| Model | Multidimensional difficulty competing risks |
| Dimensions | 5 |
| Difficulty link | `tanh` |
| Seeds | 42, 7, 123, 2024, 31337 |
| Optimization | SVI, 3,000 steps per seed |
| Players | 1,455 |
| Tossups | 1,260 |
| Buzz events | 48,612 |

Each run uses 348,404 observation rows: 295,555 `CENSORED`, 47,914 `BUZZ`, and
4,935 `NO-BUZZ` observations. Only the seeded Stage-1 model is refit; this
experiment does not fit or evaluate a bonus model.

## Optimization results

| Seed | Final ELBO loss |
| ---: | ---: |
| 42 | 361,276.75 |
| 7 | 361,337.93 |
| 123 | 361,417.46 |
| 2024 | 362,204.79 |
| 31337 | 361,047.36 |
| **Mean** | **361,456.86** |

The across-seed sample standard deviation is 440.23, or 0.12% of the mean. The
maximum loss difference is 1,157.43. All runs show the same broad convergence
pattern, although seed 2024 finishes at a somewhat higher loss.

## Ranking agreement

| Seed pair | Kendall tau | Spearman rho |
| --- | ---: | ---: |
| 123 / 2024 | 0.9120 | 0.9889 |
| 123 / 31337 | 0.9104 | 0.9886 |
| 123 / 42 | 0.9148 | 0.9897 |
| 123 / 7 | 0.9147 | 0.9898 |
| 2024 / 31337 | 0.9118 | 0.9883 |
| 2024 / 42 | 0.9095 | 0.9872 |
| 2024 / 7 | 0.9094 | 0.9883 |
| 31337 / 42 | 0.9174 | 0.9901 |
| 31337 / 7 | 0.9095 | 0.9884 |
| 42 / 7 | 0.9110 | 0.9882 |
| **Pairwise mean** | **0.9120** | **0.9888** |

The global ordering is highly consistent, but exact rank positions still move
because the list contains 1,455 players. Across players, the rank standard
deviation has median 33.16, mean 37.01, 90th percentile 66.68, and maximum
261.58.

Top-set membership is more stable:

| Set | Mean pairwise Jaccard similarity | Pairwise range |
| --- | ---: | ---: |
| Top 5 | 0.8000 | 0.6667-1.0000 |
| Top 10 | 0.7727 | 0.6667-0.8182 |
| Top 25 | 0.7999 | 0.7241-0.8519 |

Jack Lewis ranks first under all five seeds. Among players whose mean rank is
at most 50, the largest observed seed-to-seed rank swing is 31 places (Luke
Zhang, ranks 29-60). The next largest swings are 26 places for Mitch McCullar
and 23 places each for Raymond Wang and Ben Russell Jones.

## Bottom-of-ranking stability

The bottom of the ranking is substantially less stable than the global rank
correlations imply. Membership overlap across seeds is:

| Set | Mean pairwise Jaccard similarity | Pairwise range |
| --- | ---: | ---: |
| Bottom 5 | 0.6524 | 0.4286-1.0000 |
| Bottom 10 | 0.5088 | 0.3333-0.6667 |
| Bottom 25 | 0.5506 | 0.4286-0.6667 |
| Bottom 50 | 0.6412 | 0.5873-0.7544 |

Within the fixed cohort of 50 players with the worst mean ranks, mean pairwise
Kendall tau is 0.424 and mean pairwise Spearman rho is 0.578. Rank standard
deviation has median 10.61 and mean 11.74, while the seed-to-seed rank range has
median 23.5, mean 28.34, 90th percentile 53.1, and maximum 85 places. The lower
rank standard deviation than the all-player result partly reflects the hard
lower boundary at rank 1,455; it should not be read as stronger agreement.

Predicted-PPG noise in this bottom-50 cohort is similar in absolute size to the
full ranking: median PPG standard deviation is 0.86, mean is 1.03, and the 90th
percentile is 1.87. The median PPG range is 2.15, the mean is 2.54, and the
maximum is 7.27. Because many players occupy a narrow band of low predicted
PPG, this modest score variation can produce large ordinal-rank changes.

| Player ID | Mean predicted PPG | Rank range | PPG SD |
| --- | ---: | ---: | ---: |
| `hrishit` | -16.98 | 1453-1455 | 2.40 |
| `graham` | -14.71 | 1451-1455 | 1.86 |
| `mark-2` | -13.32 | 1453-1454 | 0.68 |
| `maax` | -11.06 | 1448-1452 | 0.68 |
| `rohan` | -11.04 | 1441-1453 | 1.99 |
| `michael-wu-3` | -10.03 | 1447-1450 | 0.58 |
| `sam-enright` | -9.82 | 1437-1452 | 1.39 |
| `daniel` | -9.45 | 1403-1452 | 2.45 |
| `nadita` | -9.13 | 1442-1448 | 0.79 |
| `janghyun-lee` | -9.02 | 1439-1449 | 1.01 |

These are the ten lowest players by mean predicted PPG, not ten players that
remain in identical positions under every fit. Last place alternates between
`hrishit` and `graham`. The largest bottom-50 movement belongs to
`lucy-dennett`, whose predicted PPG spans -11.52 to -4.26 and whose rank spans
1366 to 1451, an 85-place swing. Negative predicted PPG is possible because
the expectation awards +10 for a correct buzz and -5 for a neg.

## Predicted-PPG variation

Across all players, the per-player PPG standard deviation has median 0.88,
mean 1.06, 90th percentile 2.13, and maximum 8.13 PPG. The per-player range
across the five seeds has median 2.20, mean 2.62, 90th percentile 5.32, and
maximum 16.35 PPG. Averaged over the ten seed pairs, the prediction difference
has approximately 1.28 PPG mean absolute error and 1.90 PPG root mean squared
error.

| Player | Mean predicted PPG | Rank range | PPG SD |
| --- | ---: | ---: | ---: |
| Jack Lewis | 92.30 | 1-1 | 3.09 |
| Pranaav Senthilkumar | 79.67 | 2-3 | 1.00 |
| Jeffery Xu | 79.53 | 2-4 | 3.74 |
| Yrwin Batan | 70.26 | 3-6 | 4.98 |
| Beckett Gilmore | 69.82 | 4-5 | 0.92 |
| Amogh Kulkarni | 66.49 | 5-6 | 2.20 |
| Cameron Wiliams | 60.72 | 7-9 | 2.91 |
| Matt Jackson | 57.85 | 7-12 | 3.09 |
| Orion Keller | 57.78 | 8-11 | 1.49 |
| Karthik Krishnamurthy | 56.90 | 9-10 | 1.61 |

## Interpretation

The fit preserves the overall ranking very well, including a seed-invariant
number-one player, but nearby players can exchange many positions. A later
data-dropping or ranking-flip study should therefore compare its effect with
the same player's seed distribution, not treat every changed ordinal rank as a
finding. As broad reference points, seed jitter here is about 0.88 PPG median
within player, 1.28 PPG mean absolute difference between fits, and as much as a
31-place range within the mean top-50 region. The tail warrants even more
caution: bottom-10 membership overlap is only 0.51 on average, and a player in
the mean bottom-50 cohort moves as many as 85 places without any data change.

These are descriptive noise-floor measurements, not confidence intervals or
hypothesis tests.

## Reproduction and artifacts

- The runner, `run_scripts/multidimensional/multidim/run_multidim_noise_floor.py`,
  and the `compirt_eval/noise_floor/` package it imports are retired; recover
  both from git history (for example
  `git show f999da9d^:run_scripts/multidimensional/multidim/run_multidim_noise_floor.py`).
  It refit any missing seeds and wrote
  [`predicted_ppg_by_seed.csv`](predicted_ppg_by_seed.csv); `--collect-only`
  recomputed the ranking analysis from the saved fits without training.
- Each `seed_*` directory contains its own posterior tables, predictions, loss
  curve, summary, and run log.

Predicted PPG is a rotation-invariant scalar model output. The analysis assigns
the model's probability that someone buzzes at each token across the players in
the event roster, scores a correct buzz as +10 and a neg as -5, sums expected
points over tossups faced, and divides by games played.
