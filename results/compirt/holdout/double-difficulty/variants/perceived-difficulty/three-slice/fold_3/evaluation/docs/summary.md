# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 318966 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.60348 |
| log_loss | 0.700408 |
| ece | 0.260539 |
| brier | 0.250141 |
| accuracy | 0.585022 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.185022 |
| probability_std | 0.162868 |
| probability_p10 | 0.274874 |
| probability_p50 | 0.528582 |
| probability_p90 | 0.709369 |
| mean_predictive_variance | 0.223384 |
| integrated_brier_score | 0.0932968 |
| joint_tossup_event_log_loss | 6.76029 |
| buzz_position_mae | 0.137383 |
| buzz_position_median_absolute_error | 0.113291 |
| buzz_position_bias | -0.00791133 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.378304 |
| first_buzzer_mean_reciprocal_rank | 0.585863 |
| first_buzzer_log_loss | 1.6254 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.60348 |
| neg_average_precision | 0.308289 |
| neg_precision | 0.287126 |
| neg_recall | 0.542625 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.132838 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0495152 |
| no_buzz_calibration_error | 0.0343308 |
| no_buzz_brier | 0.0187992 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.60348 | 0.700408 | 0.260539 | 0.250141 | 0.585022 | 0.770044 | -0.185022 | 0.162868 | 0.274874 | 0.528582 | 0.709369 | 0.223384 |
| tossup_correctness | tier | fall | 2817 | 0.603815 | 0.717802 | 0.286714 | 0.257893 | 0.56656 | 0.781683 | -0.215122 | 0.165539 | 0.250703 | 0.516898 | 0.694244 | 0.222571 |
| tossup_correctness | tier | nationals | 1542 | 0.580034 | 0.67046 | 0.198953 | 0.238509 | 0.595331 | 0.73476 | -0.139429 | 0.136374 | 0.345962 | 0.546073 | 0.70545 | 0.23012 |
| tossup_correctness | tier | regionals | 1934 | 0.631829 | 0.688496 | 0.243279 | 0.243743 | 0.608583 | 0.75698 | -0.148397 | 0.169498 | 0.273263 | 0.531281 | 0.722946 | 0.221083 |
| tossup_correctness | tier | winter | 2787 | 0.605402 | 0.707663 | 0.280133 | 0.253182 | 0.581629 | 0.786868 | -0.205239 | 0.166975 | 0.26602 | 0.527217 | 0.713215 | 0.222074 |
| tossup_correctness | category | Current Events | 125 | 0.603194 | 0.717674 | 0.203499 | 0.256449 | 0.624 | 0.704 | -0.08 | 0.157283 | 0.247993 | 0.527735 | 0.66156 | 0.225262 |
| tossup_correctness | category | Fine Arts | 1072 | 0.582885 | 0.70507 | 0.259219 | 0.252585 | 0.583022 | 0.770522 | -0.1875 | 0.158422 | 0.275051 | 0.533245 | 0.702215 | 0.224775 |
| tossup_correctness | category | Geography | 185 | 0.550909 | 0.76775 | 0.238721 | 0.281061 | 0.508108 | 0.702703 | -0.194595 | 0.167767 | 0.226694 | 0.46773 | 0.673625 | 0.220557 |
| tossup_correctness | category | History | 1443 | 0.597166 | 0.713673 | 0.268948 | 0.256727 | 0.551629 | 0.765073 | -0.213444 | 0.159202 | 0.26464 | 0.510876 | 0.689802 | 0.22464 |
| tossup_correctness | category | Literature | 1411 | 0.56989 | 0.686034 | 0.280841 | 0.244083 | 0.593905 | 0.81219 | -0.218285 | 0.157506 | 0.30137 | 0.557249 | 0.719525 | 0.224209 |
| tossup_correctness | category | Mythology | 320 | 0.583035 | 0.702983 | 0.28345 | 0.25267 | 0.565625 | 0.79375 | -0.228125 | 0.158915 | 0.288974 | 0.536342 | 0.707764 | 0.22464 |
| tossup_correctness | category | Other Academic | 64 | 0.628906 | 0.65241 | 0.226175 | 0.230139 | 0.640625 | 0.75 | -0.109375 | 0.13247 | 0.332552 | 0.550245 | 0.66572 | 0.231884 |
| tossup_correctness | category | Philosophy | 312 | 0.623871 | 0.650541 | 0.26545 | 0.228519 | 0.61859 | 0.801282 | -0.182692 | 0.155715 | 0.335218 | 0.55568 | 0.730365 | 0.224442 |
| tossup_correctness | category | Popular Culture | 104 | 0.522727 | 0.934896 | 0.435654 | 0.345721 | 0.394231 | 0.846154 | -0.451923 | 0.175432 | 0.168642 | 0.439973 | 0.629271 | 0.211213 |
| tossup_correctness | category | Religion | 358 | 0.623469 | 0.707888 | 0.241714 | 0.254543 | 0.575419 | 0.726257 | -0.150838 | 0.168308 | 0.248133 | 0.503649 | 0.685961 | 0.221433 |
| tossup_correctness | category | Science | 1431 | 0.606167 | 0.699605 | 0.256518 | 0.24971 | 0.591894 | 0.765199 | -0.173305 | 0.161872 | 0.276028 | 0.529498 | 0.709547 | 0.223722 |
| tossup_correctness | category | Social Science | 321 | 0.624094 | 0.689363 | 0.240334 | 0.245814 | 0.607477 | 0.744548 | -0.137072 | 0.158455 | 0.293073 | 0.514497 | 0.713884 | 0.224855 |
| tossup_correctness | category | Unknown | 1934 | 0.631829 | 0.688496 | 0.243279 | 0.243743 | 0.608583 | 0.75698 | -0.148397 | 0.169498 | 0.273263 | 0.531281 | 0.722946 | 0.221083 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.712172 | 0.737322 | 0.280613 | 0.266297 | 0.536458 | 0.697917 | -0.161458 | 0.154843 | 0.202174 | 0.42091 | 0.636957 | 0.219216 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.619412 | 0.757724 | 0.287191 | 0.276017 | 0.519685 | 0.733408 | -0.213723 | 0.159624 | 0.21272 | 0.462368 | 0.643548 | 0.221628 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.618743 | 0.72178 | 0.274787 | 0.25927 | 0.566968 | 0.759276 | -0.192308 | 0.160314 | 0.252235 | 0.508799 | 0.677016 | 0.224059 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.590686 | 0.697817 | 0.271991 | 0.248849 | 0.58313 | 0.789125 | -0.205995 | 0.158108 | 0.289491 | 0.536703 | 0.710725 | 0.224708 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.586467 | 0.666901 | 0.22908 | 0.235562 | 0.62363 | 0.775342 | -0.151712 | 0.159625 | 0.315377 | 0.566291 | 0.737778 | 0.22238 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | 0.216646 | 0.9099 | -2.06012 | -1.06505 | -0.460032 | 0.0887971 | 0.851424 | 1.83781 | 2.91636 |
| player | theta_2 | 1133 | 0.223405 | 0.894948 | -1.89068 | -1.05188 | -0.381043 | 0.0900571 | 0.767133 | 1.89977 | 3.40802 |
| player | theta_3 | 1133 | 0.574516 | 1.15914 | -2.03075 | -1.23208 | -0.336699 | 0.551218 | 1.48093 | 2.42471 | 3.52582 |
| player | theta_norm | 1133 | 1.67146 | 0.776847 | 0.18613 | 0.537625 | 1.06514 | 1.57179 | 2.21615 | 3.03883 | 4.03359 |
| tossup | start_difficulty_d1 | 1240 | 1.55649 | 0.378902 | -0.418908 | 0.811315 | 1.38151 | 1.61631 | 1.80608 | 2.06204 | 2.52365 |
| tossup | start_difficulty_d2 | 1240 | 1.46995 | 0.459844 | -0.729876 | 0.616995 | 1.21758 | 1.51989 | 1.77807 | 2.11197 | 2.55266 |
| tossup | start_difficulty_d3 | 1240 | 1.69454 | 0.439644 | -0.46347 | 0.87465 | 1.45561 | 1.73416 | 1.99747 | 2.317 | 3.0289 |
| tossup | end_difficulty_d1 | 1240 | 0.335643 | 0.452849 | -1.82737 | -0.484734 | 0.103895 | 0.384843 | 0.639463 | 0.984659 | 1.47965 |
| tossup | end_difficulty_d2 | 1240 | 0.310552 | 0.542198 | -2.41966 | -0.709348 | 0.0380152 | 0.370248 | 0.647092 | 1.12742 | 1.74278 |
| tossup | end_difficulty_d3 | 1240 | 0.625065 | 0.526294 | -1.40559 | -0.28279 | 0.326545 | 0.661625 | 0.919834 | 1.48027 | 2.4469 |
| tossup | total_drop_d1 | 1240 | 1.22084 | 0.384263 | 0.479594 | 0.729584 | 0.916646 | 1.15456 | 1.46237 | 1.89644 | 2.92184 |
| tossup | total_drop_d2 | 1240 | 1.1594 | 0.429757 | 0.498343 | 0.702559 | 0.854509 | 1.02614 | 1.36018 | 2.00429 | 4.08162 |
| tossup | total_drop_d3 | 1240 | 1.06948 | 0.384505 | 0.452641 | 0.659393 | 0.788535 | 0.93673 | 1.27111 | 1.83233 | 3.12054 |
| tossup | drop_share_1_d1 | 1240 | 0.188444 | 0.0653039 | 0.0462616 | 0.0959549 | 0.135696 | 0.178937 | 0.242261 | 0.297272 | 0.480876 |
| tossup | drop_share_2_d1 | 1240 | 0.265238 | 0.0753478 | 0.0711709 | 0.134816 | 0.204628 | 0.27686 | 0.326335 | 0.364558 | 0.567764 |
| tossup | drop_share_3_d1 | 1240 | 0.546318 | 0.131832 | 0.224101 | 0.36313 | 0.428601 | 0.536937 | 0.654601 | 0.764976 | 0.880905 |
| tossup | drop_share_1_d2 | 1240 | 0.207201 | 0.0646397 | 0.0495293 | 0.100768 | 0.151509 | 0.215609 | 0.26025 | 0.298886 | 0.397256 |
| tossup | drop_share_2_d2 | 1240 | 0.281656 | 0.0697064 | 0.0804983 | 0.143789 | 0.238036 | 0.301882 | 0.33222 | 0.362529 | 0.538566 |
| tossup | drop_share_3_d2 | 1240 | 0.511143 | 0.126219 | 0.224404 | 0.361465 | 0.408148 | 0.477422 | 0.602571 | 0.753273 | 0.863947 |
| tossup | drop_share_1_d3 | 1240 | 0.206371 | 0.0666024 | 0.0380848 | 0.0920389 | 0.152498 | 0.2191 | 0.260506 | 0.288614 | 0.491337 |
| tossup | drop_share_2_d3 | 1240 | 0.283101 | 0.0730398 | 0.0557639 | 0.139023 | 0.246268 | 0.305173 | 0.329192 | 0.360126 | 0.620074 |
| tossup | drop_share_3_d3 | 1240 | 0.510527 | 0.127162 | 0.209175 | 0.370534 | 0.413598 | 0.467827 | 0.596805 | 0.761738 | 0.902322 |
| tossup | r_1 | 1240 | 0.359178 | 0.209105 | 0.018283 | 0.0496395 | 0.178258 | 0.360741 | 0.508424 | 0.719229 | 0.884516 |
| tossup | r_2 | 1240 | 0.269051 | 0.173237 | 0.025547 | 0.0475292 | 0.124335 | 0.230686 | 0.391231 | 0.599899 | 0.773086 |
| tossup | r_3 | 1240 | 0.371771 | 0.219564 | 0.0376693 | 0.0725401 | 0.179409 | 0.344766 | 0.529314 | 0.768325 | 0.892589 |
| tossup | r_norm | 1240 | 0.676189 | 0.0650321 | 0.577352 | 0.587602 | 0.626054 | 0.668089 | 0.713681 | 0.803705 | 0.895939 |
