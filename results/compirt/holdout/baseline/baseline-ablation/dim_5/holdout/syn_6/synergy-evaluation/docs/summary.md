# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_5/holdout/syn_6/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_5/holdout/syn_6`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 89502.6 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 6 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.391717 |
| mean_synergy_contribution | -0.358345 |
| median_synergy_contribution | -0.270448 |
| negative_synergy_fraction | 0.644242 |
| positive_synergy_fraction | 0.331376 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.938434 |
| log_loss | 0.324048 |
| ece | 0.0331568 |
| part_accuracy | 0.859204 |
| part_accuracy_macro_team | 0.861246 |
| part_accuracy_macro_game | 0.859716 |
| part_accuracy_macro_bonus | 0.867819 |
| exact_acc | 0.626675 |
| ppb_mae | 0.688649 |

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
| bonus_part | beta | 4716 | 0.373888 | 1.44138 | -2.75703 | -1.91793 | -0.8775 | 0.455469 | 1.548 | 2.60824 | 4.02082 |
| bonus_part | alpha_1 | 4716 | 0.00237296 | 0.495291 | -2.15092 | -0.8205 | -0.257793 | 0.00921022 | 0.263528 | 0.827903 | 2.18679 |
| bonus_part | alpha_2 | 4716 | 0.0138844 | 0.594057 | -1.98212 | -0.856099 | -0.432035 | -0.0443355 | 0.430387 | 1.04703 | 2.14359 |
| bonus_part | alpha_3 | 4716 | 0.0990131 | 0.656088 | -1.7627 | -0.962129 | -0.335063 | 0.0787946 | 0.515956 | 1.16544 | 2.56093 |
| bonus_part | alpha_4 | 4716 | 0.0642019 | 0.57531 | -2.48047 | -0.798026 | -0.306775 | 0.0242956 | 0.401135 | 1.05038 | 2.69164 |
| bonus_part | alpha_5 | 4716 | 0.103446 | 0.560934 | -1.96641 | -0.745189 | -0.304308 | 0.112755 | 0.476128 | 1.03783 | 2.15669 |
| bonus_part | alpha_norm | 4716 | 1.20192 | 0.50419 | 0.114745 | 0.45 | 0.81887 | 1.17031 | 1.51088 | 2.11063 | 3.39576 |
