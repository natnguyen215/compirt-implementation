# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_4/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_4`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 469592 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 4 |
| synergy | steps | 2000 |
| synergy | final_loss | 83940.8 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.219207 |
| mean_synergy_contribution | -0.778794 |
| median_synergy_contribution | -0.737216 |
| negative_synergy_fraction | 0.856321 |
| positive_synergy_fraction | 0.119297 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.92501 |
| log_loss | 0.355748 |
| ece | 0.0351874 |
| part_accuracy | 0.844405 |
| exact_acc | 0.590763 |
| per_bonus_points_mae | 4.88975 |
| ppb_mae | 1.80022 |
| accuracy | 0.844405 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.666424 |
| log_loss | 0.608392 |
| ece | 0.14344 |
| accuracy | 0.697073 |
| buzz_position_mae | 0.13697 |
| buzz_position_median_absolute_error | 0.115184 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.94934 | 0.992472 | 1.18396 | 2.87045 | 4.50569 | 5.12375 | 5.61122 | 6.24451 | 7.63292 |
| player | theta_1 | 1755 | 0.16298 | 0.546281 | -1.58796 | -0.895171 | -0.132645 | 0.209699 | 0.520537 | 0.992207 | 1.53052 |
| player | theta_2 | 1755 | 0.0769724 | 0.579422 | -2.40137 | -1.05287 | -0.247091 | 0.158757 | 0.461707 | 0.915428 | 1.67069 |
| player | theta_3 | 1755 | 0.105449 | 0.568491 | -1.97244 | -0.952541 | -0.250345 | 0.150637 | 0.478731 | 0.983867 | 1.60894 |
| player | theta_4 | 1755 | -0.0809121 | 0.607813 | -1.98038 | -1.20169 | -0.489781 | -0.0247081 | 0.369816 | 0.807182 | 1.55394 |
| player | theta_norm | 1755 | 1.08762 | 0.439731 | 0.177956 | 0.486995 | 0.754401 | 1.03075 | 1.35602 | 1.88353 | 2.65653 |
| tossup | beta_1 | 1350 | 0.88214 | 0.576544 | -1.94559 | 0.153868 | 0.454091 | 0.791307 | 1.3023 | 1.9031 | 2.48091 |
| tossup | beta_2 | 1350 | 0.788065 | 0.559269 | -3.14284 | 0.122957 | 0.406269 | 0.629393 | 1.14405 | 1.85841 | 2.70002 |
| tossup | beta_3 | 1350 | 0.747137 | 0.557692 | -2.92714 | 0.121335 | 0.384442 | 0.601744 | 1.03612 | 1.8801 | 3.13472 |
| tossup | beta_4 | 1350 | 0.875221 | 0.619464 | -2.50484 | 0.126672 | 0.403177 | 0.730412 | 1.32232 | 1.96739 | 3.43078 |
| tossup | gamma_1 | 1350 | 18.7541 | 87.4945 | 0.148923 | 2.58075 | 4.00025 | 4.88765 | 6.37814 | 46.1437 | 1907.65 |
| tossup | gamma_2 | 1350 | 25.4269 | 139.991 | 0.106833 | 1.99351 | 4.02726 | 4.87013 | 6.01729 | 42.0422 | 2095.01 |
| tossup | gamma_3 | 1350 | 21.0214 | 105.475 | 0.0705638 | 2.53525 | 4.09754 | 4.8245 | 5.80939 | 42.977 | 1695.37 |
| tossup | gamma_4 | 1350 | 23.6703 | 97.8669 | 0.0955847 | 2.58773 | 4.25059 | 5.06613 | 7.73011 | 73.3656 | 1708.91 |
| tossup | mu_1 | 1350 | 0.536468 | 0.141802 | 0.110537 | 0.351046 | 0.444957 | 0.499892 | 0.623527 | 0.82036 | 0.993298 |
| tossup | mu_2 | 1350 | 0.515355 | 0.119652 | 0.112017 | 0.372075 | 0.444229 | 0.484511 | 0.568745 | 0.757504 | 0.992979 |
| tossup | mu_3 | 1350 | 0.50124 | 0.11489 | 0.132893 | 0.360921 | 0.436938 | 0.479358 | 0.547756 | 0.714996 | 0.99052 |
| tossup | mu_4 | 1350 | 0.51039 | 0.131619 | 0.124864 | 0.339584 | 0.432026 | 0.478729 | 0.571073 | 0.780171 | 0.993814 |
| tossup | r_1 | 1350 | 1.57299 | 1.15371 | 0.0706276 | 0.308132 | 0.650419 | 1.22774 | 2.21435 | 3.77632 | 7.7973 |
| tossup | r_2 | 1350 | 1.19503 | 0.808411 | 0.0828799 | 0.212614 | 0.523524 | 1.05564 | 1.72351 | 2.72252 | 4.45696 |
| tossup | r_3 | 1350 | 1.12851 | 0.814019 | 0.0775931 | 0.233107 | 0.542343 | 0.926233 | 1.48271 | 2.70938 | 6.19055 |
| tossup | r_4 | 1350 | 1.26436 | 0.790259 | 0.0768731 | 0.269818 | 0.622104 | 1.10612 | 1.74764 | 2.79798 | 4.44869 |
| tossup | r_norm | 1350 | 3.03452 | 0.914393 | 1.07764 | 1.72377 | 2.41583 | 2.96149 | 3.5317 | 4.6124 | 8.60308 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.391017 | 1.47991 | -3.05822 | -1.99786 | -0.893688 | 0.513936 | 1.61816 | 2.55933 | 3.97114 |
| bonus_part | alpha_1 | 4716 | 0.835364 | 0.463593 | 0.221562 | 0.394128 | 0.525374 | 0.720876 | 0.98274 | 1.61902 | 4.57544 |
| bonus_part | alpha_2 | 4716 | 0.794455 | 0.32773 | 0.235975 | 0.424683 | 0.544311 | 0.724173 | 0.979899 | 1.36115 | 2.84986 |
| bonus_part | alpha_3 | 4716 | 0.817242 | 0.378432 | 0.2337 | 0.430572 | 0.554292 | 0.735532 | 0.983206 | 1.44396 | 4.34293 |
| bonus_part | alpha_4 | 4716 | 0.776459 | 0.321496 | 0.183739 | 0.430985 | 0.562414 | 0.722372 | 0.899333 | 1.2741 | 3.52873 |
| bonus_part | alpha_norm | 4716 | 1.68333 | 0.578805 | 0.801051 | 0.927942 | 1.24205 | 1.6076 | 2.03854 | 2.68876 | 4.78678 |
