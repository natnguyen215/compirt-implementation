# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/tfidf-cumulative-difficulty/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/tfidf-cumulative-difficulty`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 61166 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 11447.6 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.317694 |
| mean_synergy_contribution | -2.44682 |
| median_synergy_contribution | -2.34348 |
| negative_synergy_fraction | 0.974491 |
| positive_synergy_fraction | 0.0246544 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.940028 |
| log_loss | 0.323584 |
| ece | 0.0489007 |
| part_accuracy | 0.862239 |
| part_accuracy_macro_team | 0.858208 |
| part_accuracy_macro_game | 0.862335 |
| part_accuracy_macro_bonus | 0.863397 |
| exact_acc | 0.637024 |
| ppb_mae | 1.16868 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.702148 |
| log_loss | 0.561291 |
| ece | 0.0766071 |
| accuracy | 0.71864 |
| buzz_position_mae | 0.122543 |
| buzz_position_median_absolute_error | 0.108559 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 5.57508 | 0.482104 | 3.42422 | 4.80942 | 5.26541 | 5.55409 | 5.92396 | 6.29313 | 6.78652 |
| player | theta_1 | 189 | 0.57501 | 0.763792 | -0.843307 | -0.547026 | 0.0293516 | 0.463931 | 1.03737 | 2.02398 | 2.41235 |
| player | theta_2 | 189 | -0.589537 | 0.693603 | -2.44868 | -1.87549 | -1.08869 | -0.523583 | -0.0548787 | 0.442569 | 1.21199 |
| player | theta_3 | 189 | 0.428376 | 0.642951 | -1.1984 | -0.570607 | -0.0249127 | 0.387126 | 0.827642 | 1.52457 | 2.12753 |
| player | theta_4 | 189 | -0.335258 | 0.603968 | -1.81131 | -1.38084 | -0.824392 | -0.32206 | 0.159841 | 0.54558 | 0.866294 |
| player | theta_5 | 189 | 0.669316 | 0.665327 | -0.889798 | -0.352049 | 0.195322 | 0.664857 | 1.05455 | 2.03802 | 2.3738 |
| player | theta_norm | 189 | 1.79797 | 0.681944 | 0.459342 | 0.819576 | 1.29999 | 1.67467 | 2.20025 | 2.93606 | 3.98233 |
| tossup | beta | 360 | 2.59077 | 0.459033 | 1.24564 | 1.86093 | 2.27509 | 2.60564 | 2.86851 | 3.36994 | 3.93232 |
| tossup | gamma | 360 | 55.2813 | 123.291 | 1.00954 | 5.7402 | 9.56851 | 17.0157 | 46.9685 | 223.996 | 1526.11 |
| tossup | mu | 360 | 0.769529 | 0.117619 | 0.407619 | 0.557684 | 0.68972 | 0.779321 | 0.851685 | 0.945447 | 0.984658 |
| tossup | alpha_1 | 360 | -0.64982 | 0.736313 | -2.33086 | -1.77005 | -1.17756 | -0.708884 | -0.163207 | 0.676099 | 1.21809 |
| tossup | alpha_2 | 360 | 0.606575 | 0.737349 | -1.31405 | -0.49561 | -0.00790876 | 0.597455 | 1.12353 | 1.82004 | 2.59513 |
| tossup | alpha_3 | 360 | -0.500644 | 0.691169 | -2.57998 | -1.67318 | -0.979053 | -0.464471 | 0.0114871 | 0.586058 | 1.27002 |
| tossup | alpha_4 | 360 | 0.439103 | 0.672787 | -1.40959 | -0.69588 | 0.020249 | 0.423291 | 0.842669 | 1.56013 | 2.84512 |
| tossup | alpha_5 | 360 | -0.714036 | 0.646501 | -2.68781 | -1.79219 | -1.18224 | -0.726876 | -0.273093 | 0.351794 | 0.913195 |
| tossup | alpha_norm | 360 | 1.9916 | 0.452776 | 0.86572 | 1.28322 | 1.68271 | 1.9748 | 2.28738 | 2.66548 | 3.97451 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 1071 | 0.185 | 1.15742 | -1.95367 | -1.51373 | -0.885939 | 0.231882 | 1.24647 | 1.90374 | 2.09588 |
| bonus_part | alpha_1 | 1071 | 0.840119 | 0.471937 | 0.304845 | 0.421105 | 0.48809 | 0.643576 | 1.0494 | 1.91247 | 2.64134 |
| bonus_part | alpha_2 | 1071 | 0.841087 | 0.285633 | 0.351823 | 0.523483 | 0.653042 | 0.782553 | 0.939476 | 1.34613 | 2.8104 |
| bonus_part | alpha_3 | 1071 | 0.793283 | 0.34352 | 0.328271 | 0.460042 | 0.529915 | 0.673019 | 0.976352 | 1.44336 | 2.76071 |
| bonus_part | alpha_4 | 1071 | 0.834779 | 0.273166 | 0.345844 | 0.524927 | 0.67199 | 0.783035 | 0.912896 | 1.36882 | 2.75479 |
| bonus_part | alpha_5 | 1071 | 0.849033 | 0.481479 | 0.335763 | 0.429214 | 0.489878 | 0.64348 | 1.05289 | 1.88926 | 2.74245 |
| bonus_part | alpha_norm | 1071 | 1.97449 | 0.538497 | 1.16969 | 1.34621 | 1.50623 | 1.84991 | 2.3156 | 3.00679 | 3.65861 |
| synergy_player | psi_1 | 189 | 0.00227622 | 0.605166 | -1.89778 | -1.18222 | -0.199998 | -0.00478718 | 0.305246 | 1.09304 | 1.74465 |
| synergy_player | psi_2 | 189 | -0.00420275 | 0.751573 | -1.85591 | -1.28994 | -0.440989 | -0.000613534 | 0.182726 | 1.37748 | 2.03111 |
| synergy_player | psi_3 | 189 | 0.00216046 | 0.649532 | -1.66613 | -1.22659 | -0.313296 | 0.00729078 | 0.28051 | 1.17949 | 1.78525 |
| synergy_player | psi_norm | 189 | 1.05189 | 0.490561 | 0.0838719 | 0.274805 | 0.670325 | 1.00465 | 1.37768 | 1.89179 | 2.03294 |
| synergy | synergy_score | 274 | -0.45186 | 1.02571 | -3.45935 | -2.03696 | -1.13948 | -0.483332 | 0.339676 | 1.13678 | 1.86291 |
| synergy | synergy_contribution | 7017 | -2.44682 | 1.25847 | -5.2735 | -4.53459 | -3.34222 | -2.34348 | -1.648 | -0.0152465 | 0.467843 |
