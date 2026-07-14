# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/learned-topic-tfidf-all2024/synergy-evaluation`
Result root: `results/compirt/in_sample/learned-topic-tfidf-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 695561 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 224299 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.355891 |
| mean_synergy_contribution | -0.204057 |
| median_synergy_contribution | -0.0624946 |
| negative_synergy_fraction | 0.602828 |
| positive_synergy_fraction | 0.36577 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.919302 |
| log_loss | 0.37741 |
| ece | 0.0565526 |
| part_accuracy | 0.839684 |
| exact_acc | 0.580754 |
| per_bonus_points_mae | 4.89752 |
| ppb_mae | 1.75928 |
| accuracy | 0.839684 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.672301 |
| log_loss | 0.554865 |
| ece | 0.105595 |
| accuracy | 0.725759 |
| buzz_position_mae | 0.144324 |
| buzz_position_median_absolute_error | 0.127784 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 5.64249 | 0.558641 | 3.26025 | 4.65253 | 5.33265 | 5.67179 | 6.01108 | 6.50983 | 7.05209 |
| player | theta_1 | 1455 | -0.510617 | 0.792126 | -2.41369 | -1.54176 | -1.07294 | -0.647184 | -0.0604078 | 1.06497 | 2.63469 |
| player | theta_2 | 1455 | -0.589215 | 0.980225 | -2.69555 | -1.89184 | -1.32898 | -0.75967 | -0.00941316 | 1.26191 | 3.09465 |
| player | theta_3 | 1455 | -0.654185 | 1.00694 | -3.42959 | -2.01607 | -1.40429 | -0.838346 | -0.0118537 | 1.2666 | 2.40558 |
| player | theta_4 | 1455 | -0.709951 | 1.05828 | -2.8042 | -2.03234 | -1.50303 | -0.915472 | -0.0941893 | 1.42923 | 3.24461 |
| player | theta_5 | 1455 | -0.418415 | 0.809492 | -2.31781 | -1.40659 | -0.98492 | -0.583538 | -0.0216236 | 1.21921 | 3.08973 |
| player | theta_norm | 1455 | 2.37775 | 0.660308 | 0.573173 | 1.27474 | 1.95242 | 2.3706 | 2.79215 | 3.45508 | 4.92085 |
| tossup | beta_1 | 1260 | 0.70014 | 1.11965 | -2.73325 | -0.000448532 | 0.105736 | 0.194319 | 0.530807 | 3.45724 | 4.69371 |
| tossup | beta_2 | 1260 | 0.774899 | 1.18501 | -3.08046 | 0.00132636 | 0.089631 | 0.170909 | 0.787501 | 3.44241 | 4.30826 |
| tossup | beta_3 | 1260 | 0.893435 | 1.17738 | -2.6218 | 0.00646334 | 0.0932317 | 0.222985 | 1.5816 | 3.36778 | 4.63809 |
| tossup | beta_4 | 1260 | 0.973544 | 1.32727 | -1.73012 | -0.00414677 | 0.104697 | 0.222104 | 1.81282 | 3.80008 | 4.77457 |
| tossup | beta_5 | 1260 | 0.567644 | 1.00218 | -1.21452 | -0.00682577 | 0.0832422 | 0.166167 | 0.370624 | 3.26841 | 4.84426 |
| tossup | gamma_1 | 1260 | 16.1275 | 85.3668 | 2.36289 | 4.56278 | 4.85718 | 5.10159 | 5.47303 | 28.3109 | 1689.91 |
| tossup | gamma_2 | 1260 | 15.6396 | 57.9779 | 2.58807 | 4.49693 | 4.86684 | 5.11015 | 5.51336 | 62.2723 | 1303.72 |
| tossup | gamma_3 | 1260 | 15.241 | 50.2288 | 0.785446 | 4.52987 | 4.85849 | 5.16257 | 6.31358 | 48.3122 | 1036.84 |
| tossup | gamma_4 | 1260 | 20.9708 | 101.278 | 1.37574 | 4.52695 | 4.89166 | 5.16778 | 5.90483 | 54.1099 | 2023.26 |
| tossup | gamma_5 | 1260 | 13.382 | 65.9478 | 3.53253 | 4.51156 | 4.86262 | 5.08008 | 5.41555 | 23.5011 | 1655.85 |
| tossup | mu_1 | 1260 | 0.54419 | 0.115682 | 0.296918 | 0.476054 | 0.491932 | 0.502665 | 0.516831 | 0.856606 | 0.984213 |
| tossup | mu_2 | 1260 | 0.548768 | 0.123961 | 0.272062 | 0.472029 | 0.491466 | 0.502816 | 0.519647 | 0.870006 | 0.984641 |
| tossup | mu_3 | 1260 | 0.546937 | 0.115568 | 0.166936 | 0.460452 | 0.490861 | 0.504509 | 0.53114 | 0.828077 | 0.978374 |
| tossup | mu_4 | 1260 | 0.563335 | 0.132941 | 0.208719 | 0.469702 | 0.49231 | 0.50544 | 0.550054 | 0.879407 | 0.989278 |
| tossup | mu_5 | 1260 | 0.533794 | 0.101989 | 0.289032 | 0.473787 | 0.491112 | 0.501136 | 0.514495 | 0.8052 | 0.975581 |
| tossup | topic_weight_1 | 1260 | 0.152839 | 0.243053 | 0.0072479 | 0.0132531 | 0.0202406 | 0.0349891 | 0.114748 | 0.768855 | 0.893127 |
| tossup | topic_weight_2 | 1260 | 0.217812 | 0.33166 | 0.0073628 | 0.0114945 | 0.0170425 | 0.030624 | 0.207941 | 0.916745 | 0.961396 |
| tossup | topic_weight_3 | 1260 | 0.240238 | 0.304364 | 0.00645424 | 0.0118574 | 0.0214879 | 0.0574081 | 0.446561 | 0.859305 | 0.95793 |
| tossup | topic_weight_4 | 1260 | 0.257718 | 0.329489 | 0.00849412 | 0.0161509 | 0.0288311 | 0.0602131 | 0.519989 | 0.913188 | 0.96021 |
| tossup | topic_weight_5 | 1260 | 0.131392 | 0.229752 | 0.0101568 | 0.0148978 | 0.0237153 | 0.0375624 | 0.0946854 | 0.845764 | 0.958062 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 3768 | 0.056886 | 0.846692 | -3.28651 | -1.34565 | -0.141944 | 0.0300431 | 0.195988 | 1.69435 | 3.70941 |
| bonus_part | beta_2 | 3768 | 0.0719945 | 0.908401 | -3.30032 | -1.54724 | -0.119741 | 0.0232398 | 0.15984 | 2.01123 | 4.11383 |
| bonus_part | beta_3 | 3768 | 0.0320468 | 0.938196 | -3.22936 | -1.87701 | -0.147825 | 0.0273302 | 0.190117 | 1.88304 | 3.94888 |
| bonus_part | beta_4 | 3768 | 0.064799 | 0.933388 | -3.32021 | -1.67789 | -0.139031 | 0.029292 | 0.193039 | 1.96039 | 4.31071 |
| bonus_part | beta_5 | 3768 | 0.0485901 | 0.634195 | -3.20567 | -0.574528 | -0.111753 | 0.0221081 | 0.15219 | 0.928445 | 3.98389 |
