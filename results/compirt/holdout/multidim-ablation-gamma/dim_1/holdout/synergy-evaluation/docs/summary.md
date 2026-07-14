# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim-ablation-gamma/dim_1/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/multidim-ablation-gamma/dim_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 474088 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 1 |
| synergy | steps | 2000 |
| synergy | final_loss | 81560.4 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.00668263 |
| mean_synergy_contribution | -0.245495 |
| median_synergy_contribution | -0.174471 |
| negative_synergy_fraction | 0.635309 |
| positive_synergy_fraction | 0.340308 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.918173 |
| log_loss | 0.366698 |
| ece | 0.0293734 |
| part_accuracy | 0.836614 |
| exact_acc | 0.571625 |
| per_bonus_points_mae | 5.05894 |
| ppb_mae | 1.73082 |
| accuracy | 0.836614 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.632801 |
| log_loss | 0.63233 |
| ece | 0.158099 |
| accuracy | 0.678286 |
| buzz_position_mae | 0.146265 |
| buzz_position_median_absolute_error | 0.123552 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.28028 | 1.01901 | 1.145 | 3.32503 | 4.8491 | 5.38652 | 5.90587 | 6.64685 | 7.97405 |
| player | theta_1 | 1755 | 0.393026 | 0.617199 | -2.61209 | -0.797986 | 0.198742 | 0.482327 | 0.737614 | 1.14543 | 1.77046 |
| player | theta_norm | 1755 | 0.609095 | 0.405319 | 0.00113243 | 0.0898635 | 0.323481 | 0.544674 | 0.808553 | 1.31733 | 2.61209 |
| tossup | beta_1 | 1350 | 1.81616 | 0.49284 | -0.103511 | 0.98614 | 1.4518 | 1.84575 | 2.17608 | 2.56088 | 3.18582 |
| tossup | gamma_1 | 1350 | 27.8665 | 128.83 | 1.48303 | 2.99707 | 4.80809 | 6.69467 | 11.0707 | 69.6249 | 2192.75 |
| tossup | mu_1 | 1350 | 0.580504 | 0.16647 | 0.104797 | 0.303968 | 0.472095 | 0.580262 | 0.694639 | 0.856608 | 0.986768 |
| tossup | r_1 | 1350 | 3.07589 | 1.36653 | 0.350934 | 1.42444 | 2.09951 | 2.80676 | 3.77409 | 5.73955 | 9.1916 |
| tossup | r_norm | 1350 | 3.07589 | 1.36653 | 0.350934 | 1.42444 | 2.09951 | 2.80676 | 3.77409 | 5.73955 | 9.1916 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.276829 | 1.38157 | -2.86477 | -1.88655 | -0.93839 | 0.325182 | 1.40911 | 2.36806 | 3.70077 |
| bonus_part | alpha_1 | 4716 | 0.936525 | 0.633373 | 0.219698 | 0.299196 | 0.442837 | 0.696504 | 1.2679 | 2.2296 | 3.62033 |
| bonus_part | alpha_norm | 4716 | 0.936525 | 0.633373 | 0.219698 | 0.299196 | 0.442837 | 0.696504 | 1.2679 | 2.2296 | 3.62033 |
