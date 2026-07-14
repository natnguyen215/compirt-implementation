# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_4/holdout/syn_2/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_4/holdout/syn_2`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 4 |
| synergy | steps | 2000 |
| synergy | final_loss | 83653.8 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 2 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.431498 |
| mean_synergy_contribution | -0.482448 |
| median_synergy_contribution | -0.460225 |
| negative_synergy_fraction | 0.7247 |
| positive_synergy_fraction | 0.250918 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.9359 |
| log_loss | 0.330267 |
| ece | 0.0335816 |
| part_accuracy | 0.856133 |
| exact_acc | 0.618073 |
| per_bonus_points_mae | 4.62209 |
| ppb_mae | 1.65834 |
| accuracy | 0.856133 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.675263 |
| log_loss | 0.598647 |
| ece | 0.151109 |
| accuracy | 0.696872 |
| buzz_position_mae | 0.145206 |
| buzz_position_median_absolute_error | 0.126221 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.04166 | 0.820328 | 1.57959 | 3.35859 | 4.64504 | 5.1694 | 5.60326 | 6.13275 | 6.92307 |
| player | theta_1 | 1755 | 0.245881 | 0.618972 | -1.65976 | -0.799675 | -0.148318 | 0.273862 | 0.644532 | 1.23594 | 2.80276 |
| player | theta_2 | 1755 | 0.29218 | 0.711648 | -2.31342 | -1.03116 | -0.079412 | 0.35028 | 0.744606 | 1.34316 | 3.41047 |
| player | theta_3 | 1755 | 0.0237141 | 0.904335 | -3.33637 | -1.71773 | -0.471462 | 0.147226 | 0.610191 | 1.3165 | 2.3242 |
| player | theta_4 | 1755 | 0.00344224 | 0.721661 | -2.32564 | -1.13265 | -0.498729 | 0.0132605 | 0.509278 | 1.18918 | 2.3372 |
| player | theta_norm | 1755 | 1.44355 | 0.538173 | 0.167389 | 0.667774 | 1.07167 | 1.39423 | 1.7521 | 2.34449 | 3.68573 |
| tossup | beta | 1350 | 3.31971 | 0.786944 | 0.216614 | 1.87139 | 2.88939 | 3.38498 | 3.82251 | 4.46125 | 5.45026 |
| tossup | gamma | 1350 | 55.4887 | 177.336 | 3.01183 | 5.73794 | 8.84678 | 13.4245 | 27.5125 | 197.253 | 2149.88 |
| tossup | mu | 1350 | 0.589508 | 0.136681 | 0.11219 | 0.361494 | 0.50161 | 0.586737 | 0.678035 | 0.817556 | 0.985512 |
| tossup | alpha_1 | 1350 | -0.130187 | 0.737664 | -2.15958 | -1.56392 | -0.54537 | -0.0532618 | 0.391482 | 0.912838 | 2.20721 |
| tossup | alpha_2 | 1350 | 0.207322 | 0.787195 | -1.55129 | -0.835696 | -0.323024 | 0.0504529 | 0.627672 | 1.72018 | 3.6974 |
| tossup | alpha_3 | 1350 | 1.00807 | 0.638875 | -1.29324 | -0.0947172 | 0.60146 | 1.06282 | 1.44506 | 1.96598 | 3.1617 |
| tossup | alpha_4 | 1350 | 0.468585 | 0.724659 | -1.20953 | -0.536758 | -0.0168978 | 0.326961 | 0.797457 | 1.94011 | 2.90375 |
| tossup | alpha_norm | 1350 | 1.76335 | 0.531095 | 0.281402 | 0.948945 | 1.39034 | 1.75167 | 2.09731 | 2.66036 | 3.81788 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.287365 | 1.39871 | -2.8164 | -1.94514 | -0.926875 | 0.365029 | 1.4246 | 2.44265 | 3.80664 |
| bonus_part | alpha_1 | 4716 | -0.0610562 | 0.576938 | -2.60075 | -1.0586 | -0.387269 | -0.078694 | 0.274448 | 0.88735 | 2.34145 |
| bonus_part | alpha_2 | 4716 | 0.000543439 | 0.611048 | -2.0276 | -0.928817 | -0.418712 | -0.0626883 | 0.361353 | 1.1009 | 2.54975 |
| bonus_part | alpha_3 | 4716 | 0.159082 | 0.660912 | -1.91713 | -0.90053 | -0.278496 | 0.121274 | 0.559984 | 1.35247 | 2.58962 |
| bonus_part | alpha_4 | 4716 | 0.0672187 | 0.573556 | -1.75508 | -0.774839 | -0.309076 | 0.0338985 | 0.395509 | 1.0704 | 2.87633 |
| bonus_part | alpha_norm | 4716 | 1.1228 | 0.494582 | 0.0754923 | 0.395156 | 0.751217 | 1.07413 | 1.45855 | 2.03184 | 3.12344 |
