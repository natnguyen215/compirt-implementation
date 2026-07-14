# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation-s1seed/dim_6/s1seed_7/evaluation`
Result root: `results/compirt/holdout/baseline-ablation-s1seed/dim_6/s1seed_7`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

No stage summary JSON files were found for this evaluation folder.

## Bonus Stage Scalars

No bonus-stage scalar summary values were found.

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.916554 |
| log_loss | 0.368635 |
| ece | 0.0221335 |
| part_accuracy | 0.833135 |
| exact_acc | 0.567291 |
| per_bonus_points_mae | 5.22748 |
| ppb_mae | 2.67159 |
| accuracy | 0.833135 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.692056 |
| log_loss | 0.58533 |
| ece | 0.14958 |
| accuracy | 0.704229 |
| buzz_position_mae | 0.141205 |
| buzz_position_median_absolute_error | 0.121778 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.00036 | 0.801097 | 1.43556 | 3.43202 | 4.63525 | 5.13878 | 5.53382 | 6.05402 | 6.90931 |
| player | theta_1 | 1755 | -0.183065 | 0.569747 | -2.33263 | -1.07362 | -0.570251 | -0.182429 | 0.163542 | 0.786613 | 1.91868 |
| player | theta_2 | 1755 | 0.130671 | 0.624367 | -2.12091 | -0.898993 | -0.258528 | 0.121853 | 0.51825 | 1.17463 | 2.50267 |
| player | theta_3 | 1755 | -0.0403435 | 0.694921 | -2.56912 | -1.18741 | -0.500335 | -0.0146059 | 0.470716 | 1.03085 | 1.83616 |
| player | theta_4 | 1755 | 0.0351479 | 0.739091 | -2.16327 | -1.15956 | -0.471729 | 0.0228909 | 0.525355 | 1.27395 | 2.53801 |
| player | theta_5 | 1755 | -0.0609378 | 0.569636 | -2.28541 | -0.991883 | -0.461162 | -0.0309673 | 0.336443 | 0.848083 | 1.85761 |
| player | theta_6 | 1755 | -0.224031 | 0.814287 | -2.67327 | -1.30956 | -0.744234 | -0.318192 | 0.129415 | 1.28588 | 3.2437 |
| player | theta_norm | 1755 | 1.61124 | 0.49093 | 0.39744 | 0.900905 | 1.27672 | 1.57159 | 1.88826 | 2.46506 | 3.47599 |
| tossup | beta | 1350 | 3.3425 | 0.763702 | 0.374065 | 2.0521 | 2.93092 | 3.40957 | 3.83502 | 4.4925 | 5.33166 |
| tossup | gamma | 1350 | 60.8219 | 191.762 | 2.64758 | 5.81645 | 9.03765 | 13.3598 | 28.7654 | 236.047 | 2473.57 |
| tossup | mu | 1350 | 0.586431 | 0.132866 | 0.110498 | 0.363089 | 0.502205 | 0.584527 | 0.669969 | 0.806092 | 0.984913 |
| tossup | alpha_1 | 1350 | 0.0480113 | 0.673962 | -1.86526 | -0.980389 | -0.467247 | 0.020728 | 0.51619 | 1.2229 | 2.04791 |
| tossup | alpha_2 | 1350 | -0.605313 | 0.641377 | -2.81882 | -1.6684 | -1.03589 | -0.62856 | -0.155556 | 0.472683 | 1.02103 |
| tossup | alpha_3 | 1350 | 0.497696 | 0.653283 | -1.41676 | -0.580987 | 0.045757 | 0.493222 | 0.949023 | 1.56677 | 2.57752 |
| tossup | alpha_4 | 1350 | 0.418613 | 0.716653 | -1.27709 | -0.548839 | -0.0488951 | 0.270417 | 0.738363 | 1.86925 | 2.79038 |
| tossup | alpha_5 | 1350 | 0.168875 | 0.646837 | -1.5343 | -0.88179 | -0.307779 | 0.143632 | 0.660719 | 1.1891 | 1.86732 |
| tossup | alpha_6 | 1350 | -0.35329 | 0.845011 | -3.39681 | -2.00369 | -0.813846 | -0.158925 | 0.262535 | 0.715298 | 1.4695 |
| tossup | alpha_norm | 1350 | 1.90813 | 0.490316 | 0.425241 | 1.14359 | 1.57743 | 1.89347 | 2.23267 | 2.70559 | 3.73081 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.769427 | 1.63356 | -3.10761 | -1.88647 | -0.612979 | 0.884486 | 2.1295 | 3.21229 | 4.09692 |
| bonus_part | alpha_1 | 4716 | 0.668053 | 0.261876 | 0.168816 | 0.345453 | 0.495263 | 0.64527 | 0.782113 | 1.0915 | 3.48268 |
| bonus_part | alpha_2 | 4716 | 0.631116 | 0.231813 | 0.136173 | 0.299232 | 0.471504 | 0.606163 | 0.759006 | 1.02692 | 2.42988 |
| bonus_part | alpha_3 | 4716 | 0.756338 | 0.338074 | 0.225252 | 0.357064 | 0.508476 | 0.702297 | 0.915811 | 1.37017 | 3.10682 |
| bonus_part | alpha_4 | 4716 | 0.730482 | 0.381344 | 0.192178 | 0.306926 | 0.44028 | 0.643817 | 0.925095 | 1.41821 | 3.39094 |
| bonus_part | alpha_5 | 4716 | 0.680933 | 0.256569 | 0.164395 | 0.351121 | 0.497352 | 0.657435 | 0.814073 | 1.10068 | 2.57995 |
| bonus_part | alpha_6 | 4716 | 0.648094 | 0.267022 | 0.0749712 | 0.231663 | 0.479379 | 0.631738 | 0.782299 | 1.11429 | 2.40006 |
| bonus_part | alpha_norm | 4716 | 1.78458 | 0.410247 | 0.793153 | 1.17722 | 1.4746 | 1.77732 | 2.0556 | 2.45783 | 4.01887 |
