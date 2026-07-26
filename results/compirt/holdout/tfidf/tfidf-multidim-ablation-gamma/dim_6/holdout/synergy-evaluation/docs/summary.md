# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_6/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_6`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 468664 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 6 |
| synergy | steps | 2000 |
| synergy | final_loss | 86406.6 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.462616 |
| mean_synergy_contribution | -1.32479 |
| median_synergy_contribution | -1.32918 |
| negative_synergy_fraction | 0.93084 |
| positive_synergy_fraction | 0.0447778 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.927494 |
| log_loss | 0.351452 |
| ece | 0.0379118 |
| part_accuracy | 0.847179 |
| part_accuracy_macro_team | 0.850043 |
| part_accuracy_macro_game | 0.84766 |
| part_accuracy_macro_bonus | 0.854761 |
| exact_acc | 0.598571 |
| ppb_mae | 1.00639 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.680862 |
| log_loss | 0.592672 |
| ece | 0.136757 |
| accuracy | 0.707854 |
| buzz_position_mae | 0.132832 |
| buzz_position_median_absolute_error | 0.110857 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.8481 | 1.00344 | 1.18598 | 2.6937 | 4.39779 | 5.04252 | 5.53804 | 6.14164 | 7.0762 |
| player | theta_1 | 1755 | 0.226444 | 0.561085 | -2.05417 | -0.858609 | -0.0926179 | 0.285748 | 0.593198 | 1.048 | 1.82112 |
| player | theta_2 | 1755 | 0.0684095 | 0.545575 | -1.78939 | -0.824174 | -0.307436 | 0.101676 | 0.445114 | 0.966162 | 1.8209 |
| player | theta_3 | 1755 | 0.0699637 | 0.623955 | -2.04148 | -1.09598 | -0.318436 | 0.141804 | 0.535227 | 0.975174 | 1.47859 |
| player | theta_4 | 1755 | 0.113763 | 0.556849 | -1.7224 | -0.89625 | -0.226597 | 0.178347 | 0.484901 | 0.944075 | 1.77886 |
| player | theta_5 | 1755 | -0.146582 | 0.617254 | -2.40854 | -1.21942 | -0.544297 | -0.0917793 | 0.259144 | 0.831675 | 1.90711 |
| player | theta_6 | 1755 | 0.102001 | 0.602851 | -1.94528 | -0.999715 | -0.281688 | 0.14769 | 0.50863 | 1.02796 | 1.96951 |
| player | theta_norm | 1755 | 1.40242 | 0.440605 | 0.358326 | 0.753606 | 1.08227 | 1.36396 | 1.67524 | 2.21561 | 3.21113 |
| tossup | beta_1 | 1350 | 0.684985 | 0.402921 | -1.65805 | 0.189683 | 0.441607 | 0.617524 | 0.872317 | 1.42191 | 2.74162 |
| tossup | beta_2 | 1350 | 0.594431 | 0.418496 | -2.44371 | 0.1374 | 0.368358 | 0.510274 | 0.697827 | 1.4669 | 2.65051 |
| tossup | beta_3 | 1350 | 0.761863 | 0.536384 | -0.862958 | 0.155863 | 0.391119 | 0.577574 | 1.09125 | 1.84353 | 2.92636 |
| tossup | beta_4 | 1350 | 0.636218 | 0.419193 | -1.36583 | 0.170555 | 0.370998 | 0.539078 | 0.756333 | 1.52891 | 2.55965 |
| tossup | beta_5 | 1350 | 0.73425 | 0.550338 | -1.99651 | 0.107525 | 0.3684 | 0.563454 | 1.05025 | 1.84979 | 2.72622 |
| tossup | beta_6 | 1350 | 0.698455 | 0.51574 | -1.76729 | 0.129796 | 0.376672 | 0.542819 | 0.865101 | 1.80666 | 3.19276 |
| tossup | gamma_1 | 1350 | 11.8683 | 44.8405 | 0.296516 | 2.60661 | 4.05461 | 4.77896 | 5.79947 | 24.0698 | 801.464 |
| tossup | gamma_2 | 1350 | 11.3292 | 59.0507 | 0.09188 | 3.18998 | 4.25427 | 4.9064 | 5.67021 | 14.6369 | 1550.38 |
| tossup | gamma_3 | 1350 | 21.1298 | 115.028 | 0.866498 | 3.27575 | 4.41839 | 5.09909 | 6.40575 | 39.7267 | 2203.94 |
| tossup | gamma_4 | 1350 | 13.6448 | 76.2097 | 0.203873 | 2.84209 | 4.29836 | 4.9384 | 5.83784 | 22.8018 | 1513.3 |
| tossup | gamma_5 | 1350 | 20.3044 | 99.0988 | 0.146312 | 3.23323 | 4.38569 | 5.08065 | 6.49989 | 36.4965 | 1605.91 |
| tossup | gamma_6 | 1350 | 15.6948 | 95.7421 | 0.40654 | 3.15636 | 4.37261 | 5.01347 | 5.85016 | 24.5433 | 2340.34 |
| tossup | mu_1 | 1350 | 0.496905 | 0.100634 | 0.111097 | 0.356213 | 0.444054 | 0.48454 | 0.537105 | 0.677944 | 0.986376 |
| tossup | mu_2 | 1350 | 0.487815 | 0.0967648 | 0.188825 | 0.382885 | 0.43888 | 0.470957 | 0.508536 | 0.689032 | 0.982837 |
| tossup | mu_3 | 1350 | 0.498831 | 0.111411 | 0.132288 | 0.366836 | 0.440051 | 0.474693 | 0.531988 | 0.7322 | 0.973602 |
| tossup | mu_4 | 1350 | 0.484978 | 0.0878064 | 0.138177 | 0.373526 | 0.443732 | 0.47365 | 0.509039 | 0.641218 | 0.991673 |
| tossup | mu_5 | 1350 | 0.506466 | 0.127003 | 0.142489 | 0.36854 | 0.432075 | 0.470861 | 0.541057 | 0.769991 | 0.990723 |
| tossup | mu_6 | 1350 | 0.49827 | 0.107594 | 0.210012 | 0.376785 | 0.440216 | 0.473874 | 0.518335 | 0.724051 | 0.989315 |
| tossup | r_1 | 1350 | 1.15899 | 0.90005 | 0.0969836 | 0.229918 | 0.500913 | 0.902238 | 1.57443 | 2.92215 | 7.01791 |
| tossup | r_2 | 1350 | 0.84447 | 0.721055 | 0.0971287 | 0.234213 | 0.404922 | 0.629621 | 0.99086 | 2.54959 | 5.46844 |
| tossup | r_3 | 1350 | 1.16803 | 0.918309 | 0.0578173 | 0.233628 | 0.484194 | 0.812144 | 1.64068 | 3.10275 | 4.64157 |
| tossup | r_4 | 1350 | 0.883388 | 0.652737 | 0.0533524 | 0.220996 | 0.414034 | 0.669998 | 1.17662 | 2.23902 | 4.26203 |
| tossup | r_5 | 1350 | 1.19074 | 0.896411 | 0.0351881 | 0.214939 | 0.528098 | 0.925917 | 1.62582 | 3.10553 | 4.34609 |
| tossup | r_6 | 1350 | 1.07524 | 0.971253 | 0.0659986 | 0.237429 | 0.43862 | 0.704063 | 1.23093 | 3.35669 | 5.21587 |
| tossup | r_norm | 1350 | 3.22842 | 0.834217 | 1.24156 | 1.98768 | 2.67797 | 3.14602 | 3.73595 | 4.70176 | 7.83024 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.443612 | 1.46878 | -2.88237 | -1.88218 | -0.840377 | 0.563575 | 1.65562 | 2.60956 | 4.07268 |
| bonus_part | alpha_1 | 4716 | 0.831505 | 0.429781 | 0.187949 | 0.397555 | 0.531538 | 0.727597 | 1.0135 | 1.53833 | 4.43714 |
| bonus_part | alpha_2 | 4716 | 0.769883 | 0.291942 | 0.249048 | 0.444908 | 0.555318 | 0.707178 | 0.928673 | 1.22809 | 3.02596 |
| bonus_part | alpha_3 | 4716 | 0.782704 | 0.361971 | 0.236888 | 0.428939 | 0.547452 | 0.705767 | 0.924667 | 1.32587 | 4.51833 |
| bonus_part | alpha_4 | 4716 | 0.774681 | 0.305348 | 0.188358 | 0.437036 | 0.548812 | 0.711949 | 0.944896 | 1.27303 | 4.23098 |
| bonus_part | alpha_5 | 4716 | 0.781601 | 0.310478 | 0.222023 | 0.435474 | 0.584648 | 0.732516 | 0.893505 | 1.30193 | 3.61695 |
| bonus_part | alpha_6 | 4716 | 0.812937 | 0.374823 | 0.261909 | 0.437649 | 0.561624 | 0.738704 | 0.955971 | 1.45921 | 4.39878 |
| bonus_part | alpha_norm | 4716 | 2.03796 | 0.588536 | 1.04864 | 1.22274 | 1.56846 | 1.9893 | 2.43354 | 3.0595 | 4.80913 |
