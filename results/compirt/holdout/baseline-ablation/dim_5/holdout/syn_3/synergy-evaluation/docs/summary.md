# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_5/holdout/syn_3/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_5/holdout/syn_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 85365.1 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.492377 |
| mean_synergy_contribution | -0.516938 |
| median_synergy_contribution | -0.457992 |
| negative_synergy_fraction | 0.734956 |
| positive_synergy_fraction | 0.240662 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.938321 |
| log_loss | 0.325211 |
| ece | 0.0352488 |
| part_accuracy | 0.858719 |
| exact_acc | 0.624971 |
| per_bonus_points_mae | 4.57303 |
| ppb_mae | 1.67643 |
| accuracy | 0.858719 |

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
| bonus_part | beta | 4716 | 0.309997 | 1.41834 | -2.7674 | -1.95417 | -0.919297 | 0.395459 | 1.46672 | 2.51839 | 3.91368 |
| bonus_part | alpha_1 | 4716 | -0.00144481 | 0.495605 | -2.1244 | -0.821335 | -0.259128 | 0.00529703 | 0.261458 | 0.82136 | 2.17191 |
| bonus_part | alpha_2 | 4716 | 0.0244181 | 0.593166 | -1.94771 | -0.848304 | -0.421898 | -0.0356644 | 0.4455 | 1.05018 | 2.1316 |
| bonus_part | alpha_3 | 4716 | 0.10506 | 0.649077 | -1.70617 | -0.934856 | -0.326546 | 0.0803419 | 0.515727 | 1.16733 | 2.53286 |
| bonus_part | alpha_4 | 4716 | 0.0676672 | 0.572503 | -2.46014 | -0.791687 | -0.299752 | 0.0260452 | 0.401732 | 1.04707 | 2.65678 |
| bonus_part | alpha_5 | 4716 | 0.0919402 | 0.557534 | -1.99514 | -0.745032 | -0.313867 | 0.0976346 | 0.461929 | 1.01638 | 2.12529 |
| bonus_part | alpha_norm | 4716 | 1.19634 | 0.500517 | 0.119743 | 0.448669 | 0.8204 | 1.16203 | 1.50586 | 2.10156 | 3.36787 |
