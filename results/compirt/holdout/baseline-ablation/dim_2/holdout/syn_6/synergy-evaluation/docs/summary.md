# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_2/holdout/syn_6/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_2/holdout/syn_6`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 2 |
| synergy | steps | 2000 |
| synergy | final_loss | 87985.2 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 6 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.111902 |
| mean_synergy_contribution | -0.0582179 |
| median_synergy_contribution | -0.00414599 |
| negative_synergy_fraction | 0.506501 |
| positive_synergy_fraction | 0.469117 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.926194 |
| log_loss | 0.348855 |
| ece | 0.0259748 |
| part_accuracy | 0.844455 |
| exact_acc | 0.589986 |
| per_bonus_points_mae | 4.85711 |
| ppb_mae | 1.68813 |
| accuracy | 0.844455 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.646583 |
| log_loss | 0.6231 |
| ece | 0.159369 |
| accuracy | 0.677947 |
| buzz_position_mae | 0.152097 |
| buzz_position_median_absolute_error | 0.133087 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.19161 | 0.902728 | 1.60359 | 3.31873 | 4.76706 | 5.31464 | 5.76192 | 6.43912 | 7.75525 |
| player | theta_1 | 1755 | -0.0220725 | 0.627349 | -2.33078 | -1.07694 | -0.397794 | -0.00945902 | 0.371319 | 1.01589 | 2.02438 |
| player | theta_2 | 1755 | 0.302642 | 1.01076 | -4.06236 | -1.68617 | -0.0941787 | 0.451406 | 0.923831 | 1.64746 | 2.76475 |
| player | theta_norm | 1755 | 1.05569 | 0.626274 | 0.0161641 | 0.270883 | 0.616267 | 0.9434 | 1.36832 | 2.16747 | 4.09201 |
| tossup | beta | 1350 | 3.22932 | 0.810488 | -0.180627 | 1.78408 | 2.78803 | 3.28561 | 3.75554 | 4.42239 | 5.58873 |
| tossup | gamma | 1350 | 62.353 | 187.398 | 3.53177 | 5.79222 | 8.74982 | 13.3814 | 29.5267 | 280.174 | 2170.95 |
| tossup | mu | 1350 | 0.59123 | 0.146716 | 0.0692394 | 0.34643 | 0.495513 | 0.590603 | 0.687654 | 0.837275 | 0.988427 |
| tossup | alpha_1 | 1350 | -0.05952 | 0.738911 | -2.55373 | -1.46926 | -0.474516 | 0.00757134 | 0.453044 | 1.03443 | 1.78442 |
| tossup | alpha_2 | 1350 | 1.2908 | 0.709052 | -1.02507 | 0.236286 | 0.854295 | 1.22103 | 1.67787 | 2.46248 | 4.34146 |
| tossup | alpha_norm | 1350 | 1.52436 | 0.627934 | 0.0804245 | 0.640398 | 1.08583 | 1.45005 | 1.90733 | 2.61956 | 4.42768 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.324487 | 1.42164 | -3.12288 | -1.98867 | -0.852515 | 0.382196 | 1.49834 | 2.51436 | 3.92073 |
| bonus_part | alpha_1 | 4716 | -0.00967283 | 0.511328 | -2.50149 | -0.947398 | -0.207685 | 0.01034 | 0.254935 | 0.752045 | 1.97759 |
| bonus_part | alpha_2 | 4716 | 0.220918 | 0.781435 | -2.01212 | -1.02444 | -0.289861 | 0.0877847 | 0.737386 | 1.62257 | 2.59453 |
| bonus_part | alpha_norm | 4716 | 0.79801 | 0.532963 | 0.00164758 | 0.13268 | 0.337431 | 0.685911 | 1.19436 | 1.75369 | 2.654 |
