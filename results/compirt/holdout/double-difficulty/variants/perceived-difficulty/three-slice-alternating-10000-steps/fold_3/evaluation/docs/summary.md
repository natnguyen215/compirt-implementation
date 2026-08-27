# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating-10000-steps/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating-10000-steps/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 310785 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.613718 |
| log_loss | 0.657518 |
| ece | 0.221213 |
| brier | 0.231148 |
| accuracy | 0.628194 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.14185 |
| probability_std | 0.174433 |
| probability_p10 | 0.303068 |
| probability_p50 | 0.564488 |
| probability_p90 | 0.766667 |
| mean_predictive_variance | 0.217189 |
| integrated_brier_score | 0.0933317 |
| joint_tossup_event_log_loss | 6.70487 |
| buzz_position_mae | 0.137421 |
| buzz_position_median_absolute_error | 0.113318 |
| buzz_position_bias | -0.00585544 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.373568 |
| first_buzzer_mean_reciprocal_rank | 0.582354 |
| first_buzzer_log_loss | 1.64313 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.613718 |
| neg_average_precision | 0.316013 |
| neg_precision | 0.304374 |
| neg_recall | 0.479885 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.139138 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0484018 |
| no_buzz_calibration_error | 0.0332174 |
| no_buzz_brier | 0.0184381 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.613718 | 0.657518 | 0.221213 | 0.231148 | 0.628194 | 0.770044 | -0.14185 | 0.174433 | 0.303068 | 0.564488 | 0.766667 | 0.217189 |
| tossup_correctness | tier | fall | 2817 | 0.606045 | 0.674905 | 0.246388 | 0.237806 | 0.616258 | 0.781683 | -0.165424 | 0.17569 | 0.275449 | 0.555231 | 0.746767 | 0.217887 |
| tossup_correctness | tier | nationals | 1542 | 0.588595 | 0.691276 | 0.215923 | 0.247567 | 0.588846 | 0.73476 | -0.145914 | 0.154906 | 0.314749 | 0.52803 | 0.719509 | 0.225649 |
| tossup_correctness | tier | regionals | 1934 | 0.620538 | 0.633827 | 0.174629 | 0.220425 | 0.648397 | 0.75698 | -0.108583 | 0.183956 | 0.3185 | 0.601529 | 0.804168 | 0.209378 |
| tossup_correctness | tier | winter | 2787 | 0.630658 | 0.637706 | 0.231022 | 0.222775 | 0.648009 | 0.786868 | -0.138859 | 0.172222 | 0.305617 | 0.576315 | 0.76653 | 0.217221 |
| tossup_correctness | category | Current Events | 125 | 0.571253 | 0.743675 | 0.254361 | 0.268802 | 0.528 | 0.704 | -0.176 | 0.155754 | 0.245815 | 0.495276 | 0.662897 | 0.225229 |
| tossup_correctness | category | Fine Arts | 1072 | 0.595514 | 0.649761 | 0.21341 | 0.228744 | 0.625933 | 0.770522 | -0.14459 | 0.167601 | 0.314957 | 0.576599 | 0.757049 | 0.21863 |
| tossup_correctness | category | Geography | 185 | 0.580699 | 0.745967 | 0.234449 | 0.271581 | 0.497297 | 0.702703 | -0.205405 | 0.1678 | 0.236302 | 0.483414 | 0.693842 | 0.220835 |
| tossup_correctness | category | History | 1443 | 0.636409 | 0.694047 | 0.26632 | 0.247837 | 0.582121 | 0.765073 | -0.182952 | 0.159226 | 0.274387 | 0.514022 | 0.693156 | 0.224645 |
| tossup_correctness | category | Literature | 1411 | 0.593935 | 0.605281 | 0.212481 | 0.207849 | 0.690999 | 0.81219 | -0.121191 | 0.167508 | 0.368389 | 0.621568 | 0.801322 | 0.211999 |
| tossup_correctness | category | Mythology | 320 | 0.585361 | 0.667733 | 0.24553 | 0.23583 | 0.6375 | 0.79375 | -0.15625 | 0.171467 | 0.310148 | 0.562984 | 0.756076 | 0.218274 |
| tossup_correctness | category | Other Academic | 64 | 0.602865 | 0.665054 | 0.233178 | 0.236484 | 0.59375 | 0.75 | -0.15625 | 0.13924 | 0.31399 | 0.555781 | 0.688469 | 0.230091 |
| tossup_correctness | category | Philosophy | 312 | 0.640129 | 0.610877 | 0.231491 | 0.211244 | 0.679487 | 0.801282 | -0.121795 | 0.167276 | 0.334431 | 0.584487 | 0.781376 | 0.217148 |
| tossup_correctness | category | Popular Culture | 104 | 0.546875 | 0.862028 | 0.402952 | 0.316606 | 0.432692 | 0.846154 | -0.413462 | 0.185913 | 0.179931 | 0.468353 | 0.680011 | 0.21221 |
| tossup_correctness | category | Religion | 358 | 0.642111 | 0.680913 | 0.221369 | 0.24223 | 0.592179 | 0.726257 | -0.134078 | 0.177114 | 0.257836 | 0.514444 | 0.730962 | 0.218598 |
| tossup_correctness | category | Science | 1431 | 0.609266 | 0.673709 | 0.229939 | 0.23745 | 0.621244 | 0.765199 | -0.143955 | 0.166249 | 0.296613 | 0.552336 | 0.737712 | 0.221118 |
| tossup_correctness | category | Social Science | 321 | 0.631799 | 0.67615 | 0.225165 | 0.238681 | 0.641745 | 0.744548 | -0.102804 | 0.164595 | 0.297461 | 0.54091 | 0.720284 | 0.222397 |
| tossup_correctness | category | Unknown | 1934 | 0.620538 | 0.633827 | 0.174629 | 0.220425 | 0.648397 | 0.75698 | -0.108583 | 0.183956 | 0.3185 | 0.601529 | 0.804168 | 0.209378 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.700721 | 0.714086 | 0.258845 | 0.255994 | 0.557292 | 0.697917 | -0.140625 | 0.16311 | 0.215005 | 0.443163 | 0.651283 | 0.219683 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.628058 | 0.713798 | 0.251518 | 0.25666 | 0.545557 | 0.733408 | -0.187852 | 0.174807 | 0.235698 | 0.492373 | 0.713213 | 0.219114 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.631399 | 0.67835 | 0.23693 | 0.239637 | 0.609502 | 0.759276 | -0.149774 | 0.174748 | 0.266025 | 0.538046 | 0.737077 | 0.218964 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.617502 | 0.646521 | 0.2322 | 0.226301 | 0.641687 | 0.789125 | -0.147438 | 0.170725 | 0.312726 | 0.57565 | 0.771234 | 0.217612 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.580409 | 0.631702 | 0.186876 | 0.220085 | 0.658904 | 0.775342 | -0.116438 | 0.165789 | 0.356977 | 0.603631 | 0.79297 | 0.214678 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | 0.632278 | 1.1419 | -2.50071 | -1.08671 | -0.172324 | 0.441205 | 1.45868 | 2.71594 | 3.88913 |
| player | theta_2 | 1133 | 0.00942177 | 0.910633 | -2.87402 | -1.3567 | -0.528271 | -0.112591 | 0.503385 | 1.71395 | 3.59761 |
| player | theta_3 | 1133 | 0.494382 | 1.32908 | -3.70927 | -1.52594 | -0.480079 | 0.303862 | 1.57836 | 2.64309 | 4.09954 |
| player | theta_norm | 1133 | 1.90592 | 0.953279 | 0.0951535 | 0.537148 | 1.1478 | 1.82013 | 2.61348 | 3.50551 | 5.45381 |
| tossup | start_difficulty_d1 | 1240 | 1.78069 | 0.67127 | -0.591936 | 0.368416 | 1.45959 | 1.90371 | 2.21944 | 2.67708 | 3.27231 |
| tossup | start_difficulty_d2 | 1240 | 0.950563 | 0.767012 | -1.45325 | -0.337438 | 0.412928 | 0.966602 | 1.56059 | 2.11254 | 3.05638 |
| tossup | start_difficulty_d3 | 1240 | 1.15964 | 1.00817 | -1.41945 | -0.34137 | 0.461183 | 1.00407 | 1.90079 | 2.84179 | 4.03187 |
| tossup | end_difficulty_d1 | 1240 | 0.548758 | 0.581474 | -2.68898 | -0.63414 | 0.352763 | 0.632805 | 0.862356 | 1.37205 | 2.33085 |
| tossup | end_difficulty_d2 | 1240 | -0.175619 | 0.792672 | -3.87203 | -1.50656 | -0.642237 | -0.173364 | 0.30708 | 1.09816 | 2.27896 |
| tossup | end_difficulty_d3 | 1240 | 0.0867453 | 0.895419 | -4.06364 | -1.4445 | -0.485638 | 0.123703 | 0.730128 | 1.41184 | 2.98423 |
| tossup | total_drop_d1 | 1240 | 1.23193 | 0.409103 | 0.481109 | 0.734801 | 0.885988 | 1.19736 | 1.49047 | 1.93188 | 4.69349 |
| tossup | total_drop_d2 | 1240 | 1.12618 | 0.506031 | 0.515504 | 0.730839 | 0.852314 | 0.94565 | 1.20562 | 2.06991 | 5.91071 |
| tossup | total_drop_d3 | 1240 | 1.0729 | 0.452534 | 0.62106 | 0.728129 | 0.821112 | 0.90748 | 1.07873 | 2.00697 | 5.00651 |
| tossup | drop_share_1_d1 | 1240 | 0.192473 | 0.0839561 | 0.0357128 | 0.0859259 | 0.120397 | 0.180116 | 0.261282 | 0.313454 | 0.66292 |
| tossup | drop_share_2_d1 | 1240 | 0.259045 | 0.0952426 | 0.0449754 | 0.10744 | 0.179459 | 0.268105 | 0.333065 | 0.376724 | 0.632592 |
| tossup | drop_share_3_d1 | 1240 | 0.548482 | 0.155357 | 0.160428 | 0.347153 | 0.403528 | 0.537511 | 0.684152 | 0.793428 | 0.919312 |
| tossup | drop_share_1_d2 | 1240 | 0.237468 | 0.071266 | 0.0344099 | 0.100872 | 0.18614 | 0.268725 | 0.289332 | 0.310123 | 0.438386 |
| tossup | drop_share_2_d2 | 1240 | 0.301092 | 0.0731108 | 0.0581877 | 0.139245 | 0.281365 | 0.334056 | 0.346795 | 0.361608 | 0.536973 |
| tossup | drop_share_3_d2 | 1240 | 0.461441 | 0.138669 | 0.171864 | 0.343914 | 0.366898 | 0.392039 | 0.528925 | 0.758787 | 0.907402 |
| tossup | drop_share_1_d3 | 1240 | 0.253758 | 0.070305 | 0.0426649 | 0.0972862 | 0.240747 | 0.27853 | 0.294573 | 0.313464 | 0.590063 |
| tossup | drop_share_2_d3 | 1240 | 0.319192 | 0.070308 | 0.052011 | 0.147353 | 0.321528 | 0.336391 | 0.346895 | 0.367547 | 0.676764 |
| tossup | drop_share_3_d3 | 1240 | 0.42705 | 0.120664 | 0.12349 | 0.338833 | 0.362224 | 0.382078 | 0.426593 | 0.736796 | 0.902524 |
| tossup | r_1 | 1240 | 0.513667 | 0.294198 | 0.0154016 | 0.0341065 | 0.243438 | 0.582779 | 0.750508 | 0.916433 | 0.95816 |
| tossup | r_2 | 1240 | 0.206471 | 0.185234 | 0.0175832 | 0.0304268 | 0.0617846 | 0.138824 | 0.306547 | 0.586548 | 0.921736 |
| tossup | r_3 | 1240 | 0.279862 | 0.285217 | 0.0199445 | 0.0342991 | 0.0660278 | 0.151732 | 0.36377 | 0.888581 | 0.951089 |
| tossup | r_norm | 1240 | 0.759194 | 0.102421 | 0.577876 | 0.608756 | 0.679339 | 0.744669 | 0.847544 | 0.926891 | 0.958618 |
