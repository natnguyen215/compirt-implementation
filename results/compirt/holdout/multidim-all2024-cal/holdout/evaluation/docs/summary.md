# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim-all2024-cal/holdout/evaluation`
Result root: `results/compirt/holdout/multidim-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 448600 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | steps | 2000 |
| compositional | final_loss | 83540.2 |
| compositional | calibrate_correctness | True |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.719919 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.934334 |
| log_loss | 0.331262 |
| ece | 0.0286843 |
| part_accuracy | 0.853034 |
| exact_score_accuracy | 0.612052 |
| rounded_score_accuracy | 0.609984 |
| per_bonus_points_mae | 4.77258 |
| ppb_mae | 2.13592 |
| accuracy | 0.853034 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.624491 |
| log_loss | 0.521189 |
| ece | 0.00644668 |
| accuracy | 0.771031 |
| buzz_position_mae | 0.130854 |
| buzz_position_median_absolute_error | 0.107894 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.934334 | 0.93609 | 0.00175579 | synergy |
| log_loss | 0.331262 | 0.329038 | -0.00222385 | synergy |
| ece | 0.0286843 | 0.0314931 | 0.00280883 | no-synergy |
| accuracy | 0.853034 | 0.857352 | 0.00431733 | synergy |
| part_accuracy | 0.853034 | 0.857352 | 0.00431733 | synergy |
| exact_score_accuracy | 0.612052 | 0.621812 | 0.00975949 | synergy |
| rounded_score_accuracy | 0.609984 | 0.621547 | 0.0115625 | synergy |
| per_bonus_points_mae | 4.77258 | 4.59737 | -0.175201 | synergy |
| ppb_mae | 2.13592 | 1.7182 | -0.41772 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 0.873259 | 0.686786 | -1.03549 | -0.186943 | 0.43437 | 0.857494 | 1.28947 | 1.99463 | 3.9196 |
| player | theta_1 | 1755 | -0.45253 | 0.626953 | -2.61498 | -1.47219 | -0.865327 | -0.458008 | -0.0393907 | 0.585282 | 1.34861 |
| player | theta_2 | 1755 | -0.603445 | 0.66941 | -2.63516 | -1.71196 | -1.0673 | -0.600256 | -0.117056 | 0.48866 | 1.83503 |
| player | theta_3 | 1755 | -0.585809 | 0.538781 | -2.54289 | -1.39517 | -0.957533 | -0.630254 | -0.241506 | 0.379623 | 1.56347 |
| player | theta_4 | 1755 | -0.617721 | 0.561655 | -2.52368 | -1.52098 | -1.00787 | -0.630334 | -0.223797 | 0.312053 | 1.17851 |
| player | theta_5 | 1755 | -0.437742 | 0.60178 | -2.15841 | -1.38762 | -0.879137 | -0.450277 | -0.0341543 | 0.614952 | 1.67793 |
| player | theta_norm | 1755 | 1.7486 | 0.485673 | 0.280036 | 0.964491 | 1.39582 | 1.75949 | 2.08945 | 2.52994 | 3.47039 |
| tossup | beta_1 | 1350 | 0.921274 | 0.477858 | -0.607993 | 0.27867 | 0.582725 | 0.83633 | 1.21776 | 1.78179 | 3.05966 |
| tossup | beta_2 | 1350 | 0.86987 | 0.497497 | -0.972541 | 0.235751 | 0.527617 | 0.773381 | 1.12179 | 1.81924 | 3.47475 |
| tossup | beta_3 | 1350 | 0.865718 | 0.49181 | -0.428908 | 0.267089 | 0.512471 | 0.752073 | 1.15713 | 1.74132 | 3.99044 |
| tossup | beta_4 | 1350 | 0.821946 | 0.481805 | -0.524299 | 0.21585 | 0.49749 | 0.711177 | 1.06154 | 1.75032 | 2.98295 |
| tossup | beta_5 | 1350 | 0.813895 | 0.480809 | -0.654412 | 0.215312 | 0.511482 | 0.705591 | 1.02193 | 1.80894 | 3.11122 |
| tossup | gamma_1 | 1350 | 19.4916 | 98.2567 | 0.652497 | 3.02487 | 4.2456 | 5.17769 | 7.35461 | 48.0382 | 2062.21 |
| tossup | gamma_2 | 1350 | 23.3578 | 110.599 | 1.09243 | 2.98285 | 4.39278 | 5.22302 | 6.79798 | 54.2868 | 1670.73 |
| tossup | gamma_3 | 1350 | 21.2411 | 105.218 | 1.1521 | 3.19116 | 4.35699 | 5.13346 | 6.86765 | 40.5169 | 1662.42 |
| tossup | gamma_4 | 1350 | 16.2094 | 80.5627 | 1.04365 | 3.10127 | 4.30899 | 5.15219 | 6.70641 | 29.1033 | 1791.73 |
| tossup | gamma_5 | 1350 | 15.5266 | 78.7214 | 1.25374 | 3.12066 | 4.3047 | 5.06488 | 6.28442 | 24.8355 | 1234.29 |
| tossup | mu_1 | 1350 | 0.543162 | 0.127248 | 0.192682 | 0.377706 | 0.459568 | 0.514108 | 0.614257 | 0.799024 | 0.993535 |
| tossup | mu_2 | 1350 | 0.529766 | 0.116691 | 0.129265 | 0.377493 | 0.457644 | 0.504509 | 0.594173 | 0.74933 | 0.993128 |
| tossup | mu_3 | 1350 | 0.543521 | 0.133975 | 0.154172 | 0.388555 | 0.455428 | 0.504828 | 0.607903 | 0.827318 | 0.993647 |
| tossup | mu_4 | 1350 | 0.519012 | 0.112334 | 0.166881 | 0.379824 | 0.448378 | 0.498941 | 0.575772 | 0.727533 | 0.990913 |
| tossup | mu_5 | 1350 | 0.51961 | 0.109348 | 0.218936 | 0.38675 | 0.450204 | 0.496756 | 0.5654 | 0.74472 | 0.987392 |
| tossup | alpha_1 | 1350 | 1.37539 | 0.726689 | 0.067732 | 0.32058 | 0.801593 | 1.29498 | 1.85891 | 2.68073 | 3.75781 |
| tossup | alpha_2 | 1350 | 1.24406 | 0.642446 | 0.0404117 | 0.328528 | 0.694917 | 1.20841 | 1.74015 | 2.32489 | 3.27207 |
| tossup | alpha_3 | 1350 | 1.34222 | 0.761211 | 0.13405 | 0.394596 | 0.727476 | 1.16292 | 1.83991 | 2.7545 | 3.89883 |
| tossup | alpha_4 | 1350 | 1.20714 | 0.603372 | 0.0401304 | 0.340764 | 0.768524 | 1.13076 | 1.61759 | 2.32789 | 3.51028 |
| tossup | alpha_5 | 1350 | 1.22439 | 0.800562 | 0.0863542 | 0.353421 | 0.68029 | 1.01567 | 1.51919 | 3.04656 | 5.07768 |
| tossup | alpha_norm | 1350 | 3.21431 | 0.623764 | 1.2847 | 2.20937 | 2.80532 | 3.18306 | 3.63161 | 4.25394 | 5.60746 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.00521507 | 1.14638 | -2.40519 | -1.6196 | -0.92743 | -0.0768749 | 0.848375 | 2.0419 | 2.74085 |
| bonus_part | alpha_1 | 4716 | 0.271519 | 0.591881 | -1.7939 | -0.618061 | -0.131766 | 0.249245 | 0.630529 | 1.30538 | 2.80785 |
| bonus_part | alpha_2 | 4716 | 0.196649 | 0.627708 | -1.6745 | -0.820466 | -0.290102 | 0.247131 | 0.650669 | 1.17758 | 2.71732 |
| bonus_part | alpha_3 | 4716 | 0.261257 | 0.647489 | -1.5843 | -0.7679 | -0.218889 | 0.277463 | 0.691086 | 1.33015 | 2.88008 |
| bonus_part | alpha_4 | 4716 | 0.176744 | 0.645296 | -1.96349 | -0.848798 | -0.335216 | 0.247817 | 0.664321 | 1.14579 | 2.47746 |
| bonus_part | alpha_5 | 4716 | 0.218528 | 0.575457 | -1.79553 | -0.621793 | -0.183904 | 0.188702 | 0.568189 | 1.22195 | 2.99804 |
| bonus_part | alpha_norm | 4716 | 1.37589 | 0.526662 | 0.0385806 | 0.569025 | 1.0076 | 1.33902 | 1.69741 | 2.32402 | 3.29134 |
