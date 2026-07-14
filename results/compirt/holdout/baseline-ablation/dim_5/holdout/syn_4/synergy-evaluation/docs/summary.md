# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_5/holdout/syn_4/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_5/holdout/syn_4`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 86859.3 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 4 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.441824 |
| mean_synergy_contribution | -0.460854 |
| median_synergy_contribution | -0.380774 |
| negative_synergy_fraction | 0.698548 |
| positive_synergy_fraction | 0.27707 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.938471 |
| log_loss | 0.324797 |
| ece | 0.0352459 |
| part_accuracy | 0.859088 |
| exact_acc | 0.625897 |
| per_bonus_points_mae | 4.56677 |
| ppb_mae | 1.67742 |
| accuracy | 0.859088 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.683262 |
| log_loss | 0.592354 |
| ece | 0.150048 |
| accuracy | 0.699309 |
| buzz_position_mae | 0.143617 |
| buzz_position_median_absolute_error | 0.12406 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.01397 | 0.797102 | 1.6229 | 3.43786 | 4.62073 | 5.12707 | 5.55358 | 6.08014 | 7.03272 |
| player | theta_1 | 1755 | 0.0933766 | 0.637051 | -2.13929 | -0.894105 | -0.353211 | 0.0985565 | 0.503047 | 1.13121 | 2.3167 |
| player | theta_2 | 1755 | 0.261101 | 0.693895 | -2.30197 | -1.01314 | -0.121013 | 0.341143 | 0.741615 | 1.22895 | 2.29241 |
| player | theta_3 | 1755 | -0.000619728 | 0.791894 | -2.65804 | -1.45212 | -0.482228 | 0.0523603 | 0.563551 | 1.23039 | 2.04341 |
| player | theta_4 | 1755 | 0.063624 | 0.771598 | -2.72815 | -1.27865 | -0.450468 | 0.0807205 | 0.626014 | 1.28161 | 2.0578 |
| player | theta_5 | 1755 | -0.22916 | 0.599263 | -2.20663 | -1.1928 | -0.629247 | -0.232039 | 0.16133 | 0.808317 | 1.82039 |
| player | theta_norm | 1755 | 1.53745 | 0.487153 | 0.356187 | 0.826082 | 1.19474 | 1.50235 | 1.83205 | 2.4212 | 3.283 |
| tossup | beta | 1350 | 3.34783 | 0.774919 | 0.373888 | 2.00667 | 2.93663 | 3.39644 | 3.86392 | 4.48253 | 5.36989 |
| tossup | gamma | 1350 | 55.9767 | 178.82 | 2.85631 | 5.7835 | 9.00031 | 13.2413 | 26.736 | 210.364 | 2133.35 |
| tossup | mu | 1350 | 0.590147 | 0.134651 | 0.111239 | 0.366779 | 0.501543 | 0.586889 | 0.677336 | 0.812952 | 0.985681 |
| tossup | alpha_1 | 1350 | 0.0512364 | 0.664602 | -1.71029 | -1.03553 | -0.467605 | 0.0535762 | 0.561063 | 1.12002 | 1.87094 |
| tossup | alpha_2 | 1350 | 0.43044 | 0.734804 | -1.19605 | -0.631987 | -0.123202 | 0.376798 | 0.90754 | 1.70943 | 3.15966 |
| tossup | alpha_3 | 1350 | 0.703086 | 0.695615 | -1.15411 | -0.354318 | 0.233291 | 0.649074 | 1.11027 | 1.94143 | 3.04176 |
| tossup | alpha_4 | 1350 | 0.569733 | 0.710398 | -1.44498 | -0.56438 | 0.0751804 | 0.528224 | 1.06927 | 1.80282 | 2.51708 |
| tossup | alpha_5 | 1350 | 0.415038 | 0.635497 | -1.80808 | -0.635314 | -0.0215566 | 0.418097 | 0.844802 | 1.48885 | 2.06952 |
| tossup | alpha_norm | 1350 | 1.81505 | 0.507088 | 0.373045 | 1.02842 | 1.45255 | 1.7989 | 2.13786 | 2.68165 | 3.4697 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.32988 | 1.42503 | -2.75154 | -1.93796 | -0.903999 | 0.416531 | 1.48803 | 2.54933 | 3.95352 |
| bonus_part | alpha_1 | 4716 | -0.00340744 | 0.495076 | -2.12649 | -0.830708 | -0.262671 | 0.00519158 | 0.2622 | 0.817752 | 2.17424 |
| bonus_part | alpha_2 | 4716 | 0.0204614 | 0.593591 | -1.97186 | -0.854922 | -0.425535 | -0.0435967 | 0.439155 | 1.05272 | 2.11986 |
| bonus_part | alpha_3 | 4716 | 0.105977 | 0.650218 | -1.71183 | -0.937473 | -0.324688 | 0.0831666 | 0.518726 | 1.16696 | 2.54691 |
| bonus_part | alpha_4 | 4716 | 0.0692537 | 0.573408 | -2.45385 | -0.794073 | -0.298469 | 0.0292329 | 0.404828 | 1.05279 | 2.66225 |
| bonus_part | alpha_5 | 4716 | 0.0999759 | 0.55883 | -1.97414 | -0.740155 | -0.306022 | 0.105822 | 0.469619 | 1.03299 | 2.15493 |
| bonus_part | alpha_norm | 4716 | 1.198 | 0.502257 | 0.117766 | 0.447427 | 0.819894 | 1.16405 | 1.50862 | 2.10522 | 3.37337 |
