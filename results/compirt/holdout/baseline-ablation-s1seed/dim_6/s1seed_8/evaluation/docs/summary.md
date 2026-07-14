# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation-s1seed/dim_6/s1seed_8/evaluation`
Result root: `results/compirt/holdout/baseline-ablation-s1seed/dim_6/s1seed_8`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

No stage summary JSON files were found for this evaluation folder.

## Bonus Stage Scalars

No bonus-stage scalar summary values were found.

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.917804 |
| log_loss | 0.365789 |
| ece | 0.0227027 |
| part_accuracy | 0.835065 |
| exact_acc | 0.571128 |
| per_bonus_points_mae | 5.18693 |
| ppb_mae | 2.53522 |
| accuracy | 0.835065 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.690028 |
| log_loss | 0.587926 |
| ece | 0.149858 |
| accuracy | 0.702749 |
| buzz_position_mae | 0.141617 |
| buzz_position_median_absolute_error | 0.122363 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.98648 | 0.787951 | 1.77529 | 3.45186 | 4.5955 | 5.10335 | 5.51806 | 6.05446 | 6.99668 |
| player | theta_1 | 1755 | -0.280561 | 0.606434 | -2.31891 | -1.26093 | -0.65018 | -0.28592 | 0.0886409 | 0.775381 | 1.69725 |
| player | theta_2 | 1755 | -0.14718 | 0.791498 | -2.13482 | -1.32585 | -0.690807 | -0.238477 | 0.303023 | 1.41589 | 2.26131 |
| player | theta_3 | 1755 | 0.0927565 | 0.668271 | -1.83282 | -1.02745 | -0.39165 | 0.106794 | 0.562975 | 1.20995 | 2.36969 |
| player | theta_4 | 1755 | 0.00639044 | 0.473842 | -2.15334 | -0.779332 | -0.291283 | 0.0206991 | 0.333971 | 0.730419 | 1.81039 |
| player | theta_5 | 1755 | 0.0325911 | 0.782945 | -2.2794 | -1.31063 | -0.459145 | 0.063697 | 0.544055 | 1.29555 | 2.35503 |
| player | theta_6 | 1755 | -0.107699 | 0.631697 | -1.90683 | -1.11081 | -0.540155 | -0.143949 | 0.329448 | 0.943537 | 2.02844 |
| player | theta_norm | 1755 | 1.6035 | 0.475867 | 0.458277 | 0.886171 | 1.26974 | 1.55703 | 1.8852 | 2.46772 | 3.13618 |
| tossup | beta | 1350 | 3.37222 | 0.759327 | 0.460836 | 2.01952 | 2.97914 | 3.43481 | 3.87206 | 4.46957 | 5.30197 |
| tossup | gamma | 1350 | 56.7027 | 183.602 | 2.84669 | 5.81855 | 8.88508 | 13.0669 | 26.0079 | 225.617 | 2490.24 |
| tossup | mu | 1350 | 0.590667 | 0.133354 | 0.110812 | 0.368042 | 0.503907 | 0.588556 | 0.676506 | 0.810681 | 0.985928 |
| tossup | alpha_1 | 1350 | 0.468638 | 0.631971 | -1.75166 | -0.606141 | 0.0552398 | 0.502567 | 0.919968 | 1.45137 | 2.27187 |
| tossup | alpha_2 | 1350 | -0.665399 | 0.700273 | -2.81951 | -1.84591 | -1.13398 | -0.65433 | -0.153655 | 0.439259 | 1.36518 |
| tossup | alpha_3 | 1350 | 0.327053 | 0.693201 | -1.29987 | -0.557645 | -0.153121 | 0.169993 | 0.66989 | 1.71353 | 2.81802 |
| tossup | alpha_4 | 1350 | 0.102553 | 0.570676 | -1.96282 | -0.886946 | -0.213842 | 0.12304 | 0.45773 | 1.03137 | 1.92241 |
| tossup | alpha_5 | 1350 | 0.650989 | 0.747937 | -1.37868 | -0.403113 | 0.103874 | 0.579772 | 1.1007 | 1.98383 | 3.46905 |
| tossup | alpha_6 | 1350 | -0.0682342 | 0.644947 | -1.97839 | -1.13543 | -0.490255 | -0.0766806 | 0.349137 | 0.99381 | 1.96124 |
| tossup | alpha_norm | 1350 | 1.90505 | 0.498642 | 0.496576 | 1.14451 | 1.54985 | 1.87986 | 2.21915 | 2.75792 | 3.71925 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.811952 | 1.61274 | -3.04257 | -1.83739 | -0.526298 | 0.928502 | 2.15218 | 3.2333 | 3.96741 |
| bonus_part | alpha_1 | 4716 | 0.747706 | 0.329373 | 0.211961 | 0.349382 | 0.511328 | 0.695428 | 0.905915 | 1.35599 | 2.99251 |
| bonus_part | alpha_2 | 4716 | 0.605858 | 0.217715 | 0.133905 | 0.298854 | 0.46338 | 0.589229 | 0.717458 | 0.966165 | 3.26814 |
| bonus_part | alpha_3 | 4716 | 0.693779 | 0.34621 | 0.170461 | 0.320809 | 0.432917 | 0.609474 | 0.885116 | 1.28009 | 3.32047 |
| bonus_part | alpha_4 | 4716 | 0.708743 | 0.207615 | 0.184086 | 0.426755 | 0.573809 | 0.690757 | 0.811527 | 1.04108 | 2.32476 |
| bonus_part | alpha_5 | 4716 | 0.719441 | 0.423225 | 0.161139 | 0.283736 | 0.405214 | 0.641464 | 0.90879 | 1.38306 | 4.05582 |
| bonus_part | alpha_6 | 4716 | 0.649902 | 0.217235 | 0.127911 | 0.307054 | 0.517171 | 0.640795 | 0.763252 | 1.01145 | 2.24578 |
| bonus_part | alpha_norm | 4716 | 1.78849 | 0.442854 | 0.791277 | 1.14998 | 1.44715 | 1.78036 | 2.06567 | 2.48757 | 4.30284 |
