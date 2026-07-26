# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/tfidf-cumulative-difficulty-all2024-cal/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/tfidf-cumulative-difficulty-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 343695 |
| pyramidal | calibrate_correctness | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 68509.3 |
| compositional | calibrate_correctness | True |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.04683 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.904664 |
| log_loss | 0.393597 |
| ece | 0.0258666 |
| part_accuracy | 0.821214 |
| part_accuracy_macro_team | 0.822742 |
| part_accuracy_macro_game | 0.821361 |
| part_accuracy_macro_bonus | 0.82273 |
| exact_acc | 0.543305 |
| ppb_mae | 2.51394 |

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
| part_accuracy | 0.821214 | 0.848323 | 0.027109 | synergy |
| part_accuracy_macro_team | 0.822742 | 0.850983 | 0.0282408 | synergy |
| part_accuracy_macro_game | 0.821361 | 0.848868 | 0.0275071 | synergy |
| part_accuracy_macro_bonus | 0.82273 | 0.848751 | 0.0260214 | synergy |
| exact_acc | 0.543305 | 0.602198 | 0.0588936 | synergy |
| ppb_mae | 2.51394 | 0.613089 | -1.90085 | synergy |

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
| bonus_part | beta | 3768 | 0.00182698 | 1.25307 | -2.83527 | -2.05825 | -0.980959 | 0.0493644 | 1.10137 | 1.81907 | 2.58332 |
| bonus_part | alpha_1 | 3768 | 0.76679 | 0.345345 | 0.234033 | 0.39842 | 0.522584 | 0.667362 | 0.909232 | 1.46156 | 3.6708 |
| bonus_part | alpha_2 | 3768 | 0.786245 | 0.444265 | 0.230072 | 0.337815 | 0.463788 | 0.667757 | 0.949338 | 1.72826 | 3.68496 |
| bonus_part | alpha_3 | 3768 | 1.01085 | 0.626708 | 0.233975 | 0.352148 | 0.488035 | 0.789531 | 1.42018 | 2.24688 | 3.51591 |
| bonus_part | alpha_4 | 3768 | 0.813193 | 0.702226 | 0.14176 | 0.272204 | 0.39167 | 0.638805 | 0.826299 | 2.60018 | 4.04356 |
| bonus_part | alpha_5 | 3768 | 0.686322 | 0.297394 | 0.23577 | 0.363933 | 0.479374 | 0.624661 | 0.808221 | 1.20427 | 3.16074 |
| bonus_part | alpha_norm | 3768 | 2.08513 | 0.550665 | 0.851409 | 1.34582 | 1.688 | 1.99037 | 2.42263 | 3.085 | 4.18645 |
