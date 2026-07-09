# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim-ablation/dim_3/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/multidim-ablation/dim_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 468207 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 3 |
| synergy | steps | 2000 |
| synergy | final_loss | 85198.8 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.1561 |
| mean_synergy_contribution | -0.11346 |
| median_synergy_contribution | -0.0276858 |
| negative_synergy_fraction | 0.549393 |
| positive_synergy_fraction | 0.427631 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.928864 |
| log_loss | 0.346551 |
| ece | 0.0340229 |
| part_accuracy | 0.848441 |
| exact_score_accuracy | 0.60006 |
| rounded_score_accuracy | 0.600953 |
| per_bonus_points_mae | 4.80495 |
| ppb_mae | 1.70845 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.664712 |
| log_loss | 0.609524 |
| ece | 0.143414 |
| accuracy | 0.698121 |
| buzz_position_mae | 0.138302 |
| buzz_position_median_absolute_error | 0.116528 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1791 | 4.97108 | 1.07462 | 1.42731 | 2.37091 | 4.57246 | 5.19652 | 5.66609 | 6.27981 | 7.2 |
| player | theta_1 | 1791 | 0.186126 | 0.647973 | -2.18196 | -1.30204 | -0.101981 | 0.295391 | 0.643364 | 1.04594 | 1.57014 |
| player | theta_2 | 1791 | 0.125638 | 0.5887 | -1.86011 | -1.15164 | -0.169494 | 0.187948 | 0.499755 | 0.983823 | 1.65013 |
| player | theta_3 | 1791 | 0.166037 | 0.615279 | -2.29903 | -1.09439 | -0.15283 | 0.246089 | 0.573571 | 1.04264 | 1.93053 |
| player | theta_norm | 1791 | 1.0059 | 0.458962 | 0.0569583 | 0.383262 | 0.687628 | 0.931831 | 1.23638 | 1.96322 | 2.72271 |
| tossup | beta_1 | 1350 | 1.00749 | 0.663623 | -3.10417 | 0.201236 | 0.45507 | 0.846509 | 1.55138 | 2.15267 | 2.72888 |
| tossup | beta_2 | 1350 | 1.0214 | 0.657475 | -1.37031 | 0.183695 | 0.477354 | 0.904253 | 1.51898 | 2.18592 | 2.7798 |
| tossup | beta_3 | 1350 | 0.876508 | 0.632993 | -2.96705 | 0.185826 | 0.412158 | 0.643011 | 1.32323 | 2.11703 | 2.99016 |
| tossup | gamma_1 | 1350 | 26.3958 | 133.032 | 0.0921382 | 2.74034 | 4.30513 | 5.1981 | 7.53271 | 64.9649 | 2231.66 |
| tossup | gamma_2 | 1350 | 21.7101 | 97.5267 | 0.356682 | 2.69133 | 4.18474 | 5.05621 | 7.41374 | 52.7226 | 1694.98 |
| tossup | gamma_3 | 1350 | 20.4107 | 98.2082 | 0.117546 | 2.70677 | 4.24843 | 4.97459 | 6.50414 | 53.5007 | 1982.12 |
| tossup | mu_1 | 1350 | 0.50611 | 0.129676 | 0.125556 | 0.321914 | 0.434419 | 0.479499 | 0.573164 | 0.76565 | 0.976547 |
| tossup | mu_2 | 1350 | 0.534098 | 0.14693 | 0.111832 | 0.344608 | 0.438277 | 0.490382 | 0.623933 | 0.828781 | 0.992039 |
| tossup | mu_3 | 1350 | 0.502239 | 0.120536 | 0.166867 | 0.345442 | 0.436143 | 0.474643 | 0.547615 | 0.75013 | 0.989319 |
| tossup | alpha_1 | 1350 | 1.55329 | 1.06596 | 0.0750306 | 0.303537 | 0.661428 | 1.2977 | 2.2586 | 3.62855 | 5.11442 |
| tossup | alpha_2 | 1350 | 1.7183 | 1.26338 | 0.0823956 | 0.310754 | 0.70003 | 1.37824 | 2.47199 | 4.13827 | 8.31941 |
| tossup | alpha_3 | 1350 | 1.31858 | 1.02639 | 0.0728255 | 0.273003 | 0.552488 | 1.00858 | 1.71392 | 3.53071 | 5.44426 |
| tossup | alpha_norm | 1350 | 3.16041 | 0.948405 | 0.997563 | 1.77098 | 2.52061 | 3.10208 | 3.74052 | 4.7665 | 9.18016 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.274277 | 1.47075 | -3.14607 | -2.12968 | -0.982753 | 0.398685 | 1.47908 | 2.49367 | 4.06113 |
| bonus_part | alpha_1 | 4716 | 0.0847946 | 0.584425 | -1.96218 | -0.81681 | -0.297505 | 0.0461971 | 0.420992 | 1.08559 | 2.72726 |
| bonus_part | alpha_2 | 4716 | 0.0983987 | 0.607507 | -2.1705 | -0.828045 | -0.27684 | 0.0631108 | 0.427852 | 1.07393 | 2.96891 |
| bonus_part | alpha_3 | 4716 | 0.0931123 | 0.584338 | -1.79157 | -0.817435 | -0.296112 | 0.0613356 | 0.460159 | 1.08585 | 2.784 |
| bonus_part | alpha_norm | 4716 | 0.897542 | 0.521405 | 0.0141706 | 0.19459 | 0.470753 | 0.823938 | 1.27451 | 1.80564 | 2.97818 |
