# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_3/holdout/syn_5/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_3/holdout/syn_5`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 3 |
| synergy | steps | 2000 |
| synergy | final_loss | 87248 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 5 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.210383 |
| mean_synergy_contribution | -0.209202 |
| median_synergy_contribution | -0.117053 |
| negative_synergy_fraction | 0.58729 |
| positive_synergy_fraction | 0.388328 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.931619 |
| log_loss | 0.338978 |
| ece | 0.0305684 |
| part_accuracy | 0.852036 |
| exact_acc | 0.608099 |
| per_bonus_points_mae | 4.71968 |
| ppb_mae | 1.66928 |
| accuracy | 0.852036 |

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
| bonus_part | beta | 4716 | 0.338957 | 1.46237 | -3.15396 | -2.08787 | -0.87883 | 0.430297 | 1.53382 | 2.56217 | 3.98057 |
| bonus_part | alpha_1 | 4716 | 0.0753469 | 0.597881 | -2.25304 | -0.813868 | -0.294634 | 0.0143008 | 0.404558 | 1.16127 | 2.79621 |
| bonus_part | alpha_2 | 4716 | 0.185741 | 0.697817 | -2.10256 | -0.886893 | -0.283678 | 0.110113 | 0.643746 | 1.40572 | 2.68899 |
| bonus_part | alpha_3 | 4716 | 0.00836945 | 0.501611 | -2.61563 | -0.900981 | -0.216698 | 0.0262494 | 0.274718 | 0.812731 | 2.0238 |
| bonus_part | alpha_norm | 4716 | 0.918412 | 0.540943 | 0.0309165 | 0.198771 | 0.460204 | 0.853506 | 1.29561 | 1.89313 | 2.96209 |
