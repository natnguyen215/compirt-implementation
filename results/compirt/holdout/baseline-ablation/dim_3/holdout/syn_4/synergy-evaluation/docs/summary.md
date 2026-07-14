# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_3/holdout/syn_4/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_3/holdout/syn_4`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 3 |
| synergy | steps | 2000 |
| synergy | final_loss | 85834 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 4 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.229678 |
| mean_synergy_contribution | -0.256193 |
| median_synergy_contribution | -0.18288 |
| negative_synergy_fraction | 0.61106 |
| positive_synergy_fraction | 0.364558 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.93167 |
| log_loss | 0.339325 |
| ece | 0.0317389 |
| part_accuracy | 0.852064 |
| exact_acc | 0.608099 |
| per_bonus_points_mae | 4.71926 |
| ppb_mae | 1.67473 |
| accuracy | 0.852064 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.66348 |
| log_loss | 0.604299 |
| ece | 0.147822 |
| accuracy | 0.693679 |
| buzz_position_mae | 0.14778 |
| buzz_position_median_absolute_error | 0.1283 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.09231 | 0.868292 | 1.59381 | 3.30136 | 4.6782 | 5.24364 | 5.67418 | 6.22639 | 7.03604 |
| player | theta_1 | 1755 | 0.134341 | 0.778263 | -2.30045 | -1.32459 | -0.325984 | 0.195555 | 0.693329 | 1.3021 | 2.29455 |
| player | theta_2 | 1755 | 0.174061 | 0.88649 | -3.18845 | -1.49703 | -0.26134 | 0.256759 | 0.720381 | 1.46403 | 2.90464 |
| player | theta_3 | 1755 | -0.0298343 | 0.631899 | -2.51016 | -1.07803 | -0.422462 | -0.00142341 | 0.369138 | 0.996696 | 2.06543 |
| player | theta_norm | 1755 | 1.22884 | 0.573773 | 0.09246 | 0.448706 | 0.808957 | 1.1339 | 1.557 | 2.25197 | 3.60474 |
| tossup | beta | 1350 | 3.33298 | 0.809543 | 0.0772755 | 1.80502 | 2.91951 | 3.42372 | 3.84664 | 4.49555 | 5.53021 |
| tossup | gamma | 1350 | 55.2634 | 175.791 | 3.18663 | 5.51951 | 8.36402 | 12.4341 | 25.1619 | 218.626 | 2412.5 |
| tossup | mu | 1350 | 0.594036 | 0.13866 | 0.111297 | 0.358042 | 0.505362 | 0.595705 | 0.68514 | 0.81502 | 0.987363 |
| tossup | alpha_1 | 1350 | 0.709808 | 0.747059 | -1.51042 | -0.404247 | 0.180824 | 0.645446 | 1.18783 | 2.05167 | 3.20922 |
| tossup | alpha_2 | 1350 | 1.0608 | 0.753448 | -1.06778 | -0.153734 | 0.528174 | 1.0363 | 1.56022 | 2.27646 | 3.82384 |
| tossup | alpha_3 | 1350 | -0.0403423 | 0.712204 | -2.04208 | -1.30722 | -0.455217 | 0.000537075 | 0.436644 | 1.06955 | 1.68828 |
| tossup | alpha_norm | 1350 | 1.6998 | 0.611155 | 0.120216 | 0.797771 | 1.29554 | 1.63992 | 2.05828 | 2.8118 | 4.14704 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.319246 | 1.45575 | -3.16282 | -2.09405 | -0.893656 | 0.42084 | 1.50138 | 2.5409 | 3.94577 |
| bonus_part | alpha_1 | 4716 | 0.0767714 | 0.597887 | -2.24847 | -0.808509 | -0.2926 | 0.0144638 | 0.407619 | 1.16064 | 2.79031 |
| bonus_part | alpha_2 | 4716 | 0.18691 | 0.697688 | -2.08939 | -0.882901 | -0.285555 | 0.109664 | 0.642014 | 1.41116 | 2.68135 |
| bonus_part | alpha_3 | 4716 | 0.00690639 | 0.500605 | -2.61568 | -0.901907 | -0.217956 | 0.0237941 | 0.272054 | 0.80681 | 2.01836 |
| bonus_part | alpha_norm | 4716 | 0.918443 | 0.540382 | 0.0305936 | 0.202542 | 0.463204 | 0.850651 | 1.29307 | 1.89538 | 2.98021 |
