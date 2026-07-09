# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/tfidf-cumulative-difficulty-all2024-cal/synergy-evaluation`
Result root: `results/compirt/in_sample/tfidf-cumulative-difficulty-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 343695 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 65678 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.679799 |
| mean_synergy_contribution | -0.0651734 |
| median_synergy_contribution | 0.00133561 |
| negative_synergy_fraction | 0.464023 |
| positive_synergy_fraction | 0.504574 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.927831 |
| log_loss | 0.347097 |
| ece | 0.0297489 |
| part_accuracy | 0.848323 |
| exact_score_accuracy | 0.602198 |
| rounded_score_accuracy | 0.598872 |
| per_bonus_points_mae | 4.7947 |
| ppb_mae | 1.72536 |
| accuracy | 0.848323 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.64844 |
| log_loss | 0.516876 |
| ece | 0.00921367 |
| accuracy | 0.769671 |
| buzz_position_mae | 0.130063 |
| buzz_position_median_absolute_error | 0.111996 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.904664 | 0.927831 | 0.0231677 | synergy |
| log_loss | 0.393597 | 0.347097 | -0.0465 | synergy |
| ece | 0.0258666 | 0.0297489 | 0.00388227 | no-synergy |
| accuracy | 0.821214 | 0.848323 | 0.027109 | synergy |
| part_accuracy | 0.821214 | 0.848323 | 0.027109 | synergy |
| exact_score_accuracy | 0.543305 | 0.602198 | 0.0588936 | synergy |
| rounded_score_accuracy | 0.533527 | 0.598872 | 0.0653449 | synergy |
| per_bonus_points_mae | 5.52209 | 4.7947 | -0.727391 | synergy |
| ppb_mae | 3.02324 | 1.72536 | -1.29788 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 1.61213 | 0.707969 | -0.44222 | 0.561092 | 1.14797 | 1.53695 | 1.9982 | 2.89593 | 4.6915 |
| player | theta_1 | 1455 | -0.644098 | 0.689857 | -2.65237 | -1.83312 | -1.11537 | -0.622474 | -0.158195 | 0.499766 | 1.52121 |
| player | theta_2 | 1455 | -0.026375 | 1.00223 | -2.75535 | -1.47863 | -0.793107 | -0.109282 | 0.676254 | 1.76594 | 3.87355 |
| player | theta_3 | 1455 | -1.16123 | 0.584025 | -3.41053 | -2.12408 | -1.55997 | -1.1558 | -0.760603 | -0.2222 | 0.658558 |
| player | theta_4 | 1455 | 0.824423 | 0.745617 | -1.74168 | -0.429389 | 0.291708 | 0.855137 | 1.37719 | 1.95217 | 3.20181 |
| player | theta_5 | 1455 | -0.0784545 | 0.869259 | -2.28024 | -1.37592 | -0.723941 | -0.137457 | 0.569476 | 1.40831 | 3.0262 |
| player | theta_norm | 1455 | 2.30053 | 0.537092 | 0.690883 | 1.47473 | 1.90364 | 2.2741 | 2.67384 | 3.19968 | 4.19284 |
| tossup | beta | 1260 | 3.25542 | 0.707252 | 1.12269 | 2.11534 | 2.79487 | 3.23804 | 3.68642 | 4.48275 | 5.88598 |
| tossup | gamma | 1260 | 58.7898 | 163.267 | 1.50318 | 5.26061 | 8.78121 | 13.4663 | 32.2635 | 263.034 | 1780.03 |
| tossup | mu | 1260 | 0.700219 | 0.151024 | 0.21372 | 0.439636 | 0.597434 | 0.706811 | 0.811297 | 0.936904 | 0.992543 |
| tossup | alpha_1 | 1260 | 0.757998 | 0.758389 | -1.06345 | -0.4018 | 0.187856 | 0.73533 | 1.29229 | 2.09763 | 2.79805 |
| tossup | alpha_2 | 1260 | -0.188063 | 0.91909 | -2.54511 | -1.65825 | -0.89934 | -0.174684 | 0.500045 | 1.34629 | 2.04662 |
| tossup | alpha_3 | 1260 | 1.37213 | 0.671068 | -0.91728 | 0.258873 | 0.927063 | 1.37861 | 1.80768 | 2.51331 | 3.3457 |
| tossup | alpha_4 | 1260 | -0.923564 | 0.964135 | -3.39336 | -2.45157 | -1.56022 | -1.00835 | -0.362179 | 0.79254 | 2.02782 |
| tossup | alpha_5 | 1260 | -0.127286 | 0.868377 | -2.58673 | -1.68995 | -0.704894 | -0.0529158 | 0.445043 | 1.27021 | 2.16514 |
| tossup | alpha_norm | 1260 | 2.57181 | 0.546695 | 1.0349 | 1.74498 | 2.17976 | 2.56102 | 2.92911 | 3.52217 | 4.38399 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.00289704 | 1.16805 | -2.66177 | -1.84995 | -0.979169 | 0.00280256 | 1.0099 | 1.74785 | 2.6142 |
| bonus_part | alpha_1 | 3768 | 0.831199 | 0.361715 | 0.23318 | 0.440276 | 0.569668 | 0.73734 | 1.00315 | 1.50966 | 3.51691 |
| bonus_part | alpha_2 | 3768 | 0.876273 | 0.501552 | 0.22411 | 0.370847 | 0.515727 | 0.735322 | 1.06688 | 1.94139 | 3.73015 |
| bonus_part | alpha_3 | 3768 | 0.961309 | 0.560798 | 0.238803 | 0.367847 | 0.495937 | 0.778842 | 1.31791 | 2.04897 | 3.84337 |
| bonus_part | alpha_4 | 3768 | 0.94815 | 0.684633 | 0.212173 | 0.35368 | 0.520203 | 0.733436 | 1.00627 | 2.58994 | 3.86078 |
| bonus_part | alpha_5 | 3768 | 0.795911 | 0.362413 | 0.259324 | 0.435416 | 0.549104 | 0.700841 | 0.925026 | 1.51045 | 3.21214 |
| bonus_part | alpha_norm | 3768 | 2.22029 | 0.531323 | 1.04241 | 1.47944 | 1.81988 | 2.14743 | 2.52492 | 3.24093 | 4.65313 |
| synergy_player | psi_1 | 1455 | 0.0306493 | 0.399204 | -2.02406 | -0.614991 | -0.0507095 | 0.00518712 | 0.0756277 | 0.718109 | 1.97902 |
| synergy_player | psi_2 | 1455 | 0.000166757 | 0.397103 | -2.08732 | -0.620984 | -0.0573794 | 0.0035614 | 0.0591362 | 0.579701 | 1.98313 |
| synergy_player | psi_3 | 1455 | -0.0104255 | 0.410072 | -2.09268 | -0.673687 | -0.0684605 | -0.00425457 | 0.0477536 | 0.641444 | 2.17747 |
| synergy_player | psi_norm | 1455 | 0.521537 | 0.462682 | 0.00866466 | 0.0505195 | 0.162765 | 0.41245 | 0.699738 | 1.54573 | 2.45085 |
| synergy | synergy_score | 2521 | -0.0401402 | 0.582126 | -4.83455 | -1.16199 | -0.0664549 | 0.0214378 | 0.199338 | 0.551577 | 2.77567 |
| synergy | synergy_contribution | 44487 | -0.0651735 | 1.39596 | -6.03639 | -2.55826 | -0.598041 | 0.00133561 | 0.751007 | 2.04436 | 3.49097 |
