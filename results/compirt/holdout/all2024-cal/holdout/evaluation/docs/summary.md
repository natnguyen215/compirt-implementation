# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/all2024-cal/holdout/evaluation`
Result root: `results/compirt/holdout/all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 453236 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 83516 |
| compositional | calibrate_correctness | True |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.6588 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.929564 |
| log_loss | 0.34149 |
| ece | 0.0268148 |
| part_accuracy | 0.847631 |
| exact_acc | 0.598091 |
| per_bonus_points_mae | 4.91799 |
| ppb_mae | 2.18781 |
| accuracy | 0.847631 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.630624 |
| log_loss | 0.520031 |
| ece | 0.0118527 |
| accuracy | 0.771077 |
| buzz_position_mae | 0.137267 |
| buzz_position_median_absolute_error | 0.11807 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.929564 | 0.932626 | 0.00306151 | synergy |
| log_loss | 0.34149 | 0.335881 | -0.00560899 | synergy |
| ece | 0.0268148 | 0.0286101 | 0.00179532 | no-synergy |
| accuracy | 0.847631 | 0.852852 | 0.0052216 | synergy |
| part_accuracy | 0.847631 | 0.852852 | 0.0052216 | synergy |
| exact_acc | 0.598091 | 0.611291 | 0.0132001 | synergy |
| per_bonus_points_mae | 4.91799 | 4.69172 | -0.22627 | synergy |
| ppb_mae | 2.18781 | 1.70298 | -0.484829 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 1.4317 | 0.603907 | -0.325915 | 0.467042 | 1.00887 | 1.40904 | 1.83342 | 2.48035 | 3.66229 |
| player | theta_1 | 1755 | 1.22293 | 0.507999 | -0.641644 | 0.353356 | 0.887629 | 1.25834 | 1.58084 | 1.99659 | 3.07936 |
| player | theta_2 | 1755 | 0.240113 | 0.624155 | -1.86318 | -0.674213 | -0.177823 | 0.171768 | 0.598633 | 1.35321 | 2.83106 |
| player | theta_3 | 1755 | 1.01111 | 0.44711 | -0.82587 | 0.235275 | 0.751772 | 1.04845 | 1.2946 | 1.70938 | 2.45766 |
| player | theta_4 | 1755 | 0.536001 | 0.657487 | -1.77645 | -0.669554 | 0.125967 | 0.624821 | 0.999384 | 1.51505 | 2.40403 |
| player | theta_5 | 1755 | 0.523896 | 0.767195 | -2.10031 | -0.743562 | -0.0268291 | 0.54383 | 1.10834 | 1.71428 | 2.82676 |
| player | theta_norm | 1755 | 2.19093 | 0.452328 | 0.850866 | 1.42609 | 1.88698 | 2.18791 | 2.50845 | 2.94251 | 3.53843 |
| tossup | beta | 1350 | 3.7846 | 0.776799 | 0.729853 | 2.50687 | 3.36219 | 3.78042 | 4.27951 | 4.91997 | 7.22907 |
| tossup | gamma | 1350 | 59.1859 | 187.419 | 3.42459 | 6.13964 | 9.16061 | 13.0087 | 25.8248 | 234.06 | 2064.57 |
| tossup | mu | 1350 | 0.637176 | 0.135423 | 0.14524 | 0.413451 | 0.548255 | 0.637642 | 0.723742 | 0.857187 | 0.993332 |
| tossup | alpha_1 | 1350 | -1.36575 | 0.616562 | -2.98741 | -2.31815 | -1.79205 | -1.38153 | -0.969476 | -0.337749 | 0.743578 |
| tossup | alpha_2 | 1350 | -0.29962 | 0.703684 | -2.53949 | -1.48614 | -0.773172 | -0.295511 | 0.13588 | 0.894626 | 2.14733 |
| tossup | alpha_3 | 1350 | -1.0416 | 0.608499 | -3.18043 | -2.02842 | -1.40884 | -1.04001 | -0.663997 | -0.0241797 | 1.26231 |
| tossup | alpha_4 | 1350 | -0.457134 | 0.774136 | -2.91404 | -1.69951 | -1.00399 | -0.453008 | 0.13044 | 0.784304 | 1.69631 |
| tossup | alpha_5 | 1350 | -0.357359 | 0.80261 | -2.35115 | -1.50551 | -0.999591 | -0.467421 | 0.229352 | 1.03495 | 2.21464 |
| tossup | alpha_norm | 1350 | 2.37264 | 0.484348 | 0.706383 | 1.54981 | 2.04489 | 2.39974 | 2.69855 | 3.1251 | 3.76717 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.00127637 | 0.836656 | -1.80089 | -1.19216 | -0.704997 | -0.0360308 | 0.637611 | 1.46916 | 2.16046 |
| bonus_part | alpha_1 | 4716 | -0.218496 | 0.819327 | -2.64446 | -1.42566 | -0.911747 | -0.295202 | 0.459726 | 1.11117 | 1.58277 |
| bonus_part | alpha_2 | 4716 | 0.00600067 | 0.572075 | -1.88803 | -0.865471 | -0.388344 | 0.0095958 | 0.359982 | 0.943484 | 3.00189 |
| bonus_part | alpha_3 | 4716 | -0.135896 | 0.767499 | -2.45141 | -1.28868 | -0.777222 | -0.169955 | 0.499535 | 1.0832 | 1.58221 |
| bonus_part | alpha_4 | 4716 | -0.243383 | 0.624155 | -3.18983 | -1.40469 | -0.571758 | -0.171003 | 0.173492 | 0.609761 | 1.95803 |
| bonus_part | alpha_5 | 4716 | -0.235591 | 0.626781 | -2.52462 | -1.34623 | -0.64924 | -0.20828 | 0.220402 | 0.699445 | 1.75185 |
| bonus_part | alpha_norm | 4716 | 1.50925 | 0.522239 | 0.102195 | 0.621755 | 1.17653 | 1.49959 | 1.85213 | 2.38081 | 3.47682 |
