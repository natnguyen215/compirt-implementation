# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_4/holdout/syn_4/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_4/holdout/syn_4`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 4 |
| synergy | steps | 2000 |
| synergy | final_loss | 86257.6 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 4 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.345635 |
| mean_synergy_contribution | -0.3705 |
| median_synergy_contribution | -0.324187 |
| negative_synergy_fraction | 0.672958 |
| positive_synergy_fraction | 0.30266 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.935984 |
| log_loss | 0.329618 |
| ece | 0.032578 |
| part_accuracy | 0.856409 |
| exact_acc | 0.618669 |
| per_bonus_points_mae | 4.61659 |
| ppb_mae | 1.65784 |
| accuracy | 0.856409 |

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
| bonus_part | beta | 4716 | 0.330376 | 1.41301 | -2.79745 | -1.91898 | -0.902429 | 0.409173 | 1.47889 | 2.50815 | 3.88458 |
| bonus_part | alpha_1 | 4716 | -0.0653429 | 0.577399 | -2.61118 | -1.05431 | -0.388268 | -0.0829348 | 0.26665 | 0.885917 | 2.3588 |
| bonus_part | alpha_2 | 4716 | -0.0073163 | 0.612423 | -2.01327 | -0.931598 | -0.428132 | -0.0725833 | 0.352059 | 1.10236 | 2.55097 |
| bonus_part | alpha_3 | 4716 | 0.156065 | 0.661355 | -1.95732 | -0.911678 | -0.281015 | 0.12281 | 0.561688 | 1.33929 | 2.58417 |
| bonus_part | alpha_4 | 4716 | 0.0685811 | 0.573814 | -1.73639 | -0.773413 | -0.305628 | 0.0403226 | 0.395151 | 1.08718 | 2.86506 |
| bonus_part | alpha_norm | 4716 | 1.12375 | 0.495397 | 0.0692591 | 0.390253 | 0.752387 | 1.07782 | 1.45502 | 2.03323 | 3.12873 |
