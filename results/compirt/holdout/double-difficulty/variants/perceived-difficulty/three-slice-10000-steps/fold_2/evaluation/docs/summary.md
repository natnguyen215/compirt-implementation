# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-10000-steps/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-10000-steps/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 304889 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.616626 |
| log_loss | 0.64184 |
| ece | 0.199425 |
| brier | 0.223618 |
| accuracy | 0.651075 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.113104 |
| probability_std | 0.169253 |
| probability_p10 | 0.319326 |
| probability_p50 | 0.589267 |
| probability_p90 | 0.765998 |
| mean_predictive_variance | 0.21716 |
| integrated_brier_score | 0.0952519 |
| joint_tossup_event_log_loss | 6.71613 |
| buzz_position_mae | 0.138938 |
| buzz_position_median_absolute_error | 0.115595 |
| buzz_position_bias | 0.0020665 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.365021 |
| first_buzzer_mean_reciprocal_rank | 0.575228 |
| first_buzzer_log_loss | 1.64079 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.616626 |
| neg_average_precision | 0.321357 |
| neg_precision | 0.323202 |
| neg_recall | 0.438388 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.145732 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0488143 |
| no_buzz_calibration_error | 0.0357013 |
| no_buzz_brier | 0.01835 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.616626 | 0.64184 | 0.199425 | 0.223618 | 0.651075 | 0.764178 | -0.113104 | 0.169253 | 0.319326 | 0.589267 | 0.765998 | 0.21716 |
| tossup_correctness | tier | fall | 2798 | 0.633141 | 0.637983 | 0.223482 | 0.221487 | 0.652609 | 0.785204 | -0.132595 | 0.174979 | 0.304359 | 0.58967 | 0.765611 | 0.215573 |
| tossup_correctness | tier | nationals | 1545 | 0.590112 | 0.636957 | 0.137977 | 0.222742 | 0.646602 | 0.721036 | -0.0744337 | 0.152527 | 0.369038 | 0.601016 | 0.772029 | 0.219464 |
| tossup_correctness | tier | regionals | 2039 | 0.621297 | 0.644936 | 0.201681 | 0.225705 | 0.642472 | 0.762138 | -0.119667 | 0.175552 | 0.299961 | 0.581415 | 0.772492 | 0.215526 |
| tossup_correctness | tier | winter | 2875 | 0.61904 | 0.646022 | 0.209142 | 0.224682 | 0.658087 | 0.768348 | -0.110261 | 0.166753 | 0.314275 | 0.585545 | 0.756279 | 0.218627 |
| tossup_correctness | category | Current Events | 129 | 0.579502 | 0.686555 | 0.161885 | 0.243536 | 0.581395 | 0.666667 | -0.0852713 | 0.196124 | 0.268215 | 0.615245 | 0.801152 | 0.207445 |
| tossup_correctness | category | Fine Arts | 1074 | 0.595768 | 0.661701 | 0.223392 | 0.232178 | 0.628492 | 0.776536 | -0.148045 | 0.172226 | 0.305021 | 0.578959 | 0.756428 | 0.217385 |
| tossup_correctness | category | Geography | 180 | 0.632589 | 0.673956 | 0.100699 | 0.237514 | 0.616667 | 0.616667 | 0 | 0.161921 | 0.294668 | 0.546152 | 0.729941 | 0.22315 |
| tossup_correctness | category | History | 1454 | 0.612043 | 0.617594 | 0.165253 | 0.212545 | 0.689133 | 0.757909 | -0.0687758 | 0.162705 | 0.36118 | 0.622185 | 0.781522 | 0.214942 |
| tossup_correctness | category | Literature | 1435 | 0.595825 | 0.62724 | 0.235486 | 0.216806 | 0.671777 | 0.810453 | -0.138676 | 0.154904 | 0.347048 | 0.597107 | 0.755434 | 0.220385 |
| tossup_correctness | category | Mythology | 324 | 0.6041 | 0.630084 | 0.206893 | 0.21747 | 0.648148 | 0.79321 | -0.145062 | 0.169334 | 0.352293 | 0.618591 | 0.77433 | 0.213876 |
| tossup_correctness | category | Other Academic | 71 | 0.535948 | 0.63037 | 0.202493 | 0.219871 | 0.647887 | 0.760563 | -0.112676 | 0.15495 | 0.409236 | 0.595443 | 0.785678 | 0.217567 |
| tossup_correctness | category | Philosophy | 310 | 0.668003 | 0.591468 | 0.174798 | 0.201784 | 0.690323 | 0.76129 | -0.0709677 | 0.155956 | 0.381201 | 0.605955 | 0.772065 | 0.218197 |
| tossup_correctness | category | Popular Culture | 108 | 0.489583 | 0.843603 | 0.425577 | 0.310864 | 0.444444 | 0.888889 | -0.444444 | 0.174492 | 0.24242 | 0.457013 | 0.692362 | 0.218207 |
| tossup_correctness | category | Religion | 361 | 0.646485 | 0.618618 | 0.169488 | 0.213941 | 0.67036 | 0.742382 | -0.0720222 | 0.158315 | 0.349108 | 0.593343 | 0.761631 | 0.219552 |
| tossup_correctness | category | Science | 1445 | 0.631174 | 0.665417 | 0.208304 | 0.233745 | 0.628374 | 0.746021 | -0.117647 | 0.173723 | 0.297121 | 0.552032 | 0.759263 | 0.218398 |
| tossup_correctness | category | Social Science | 327 | 0.666374 | 0.610564 | 0.145053 | 0.210821 | 0.678899 | 0.718654 | -0.0397554 | 0.166862 | 0.342445 | 0.601036 | 0.77135 | 0.216596 |
| tossup_correctness | category | Unknown | 2039 | 0.621297 | 0.644936 | 0.201681 | 0.225705 | 0.642472 | 0.762138 | -0.119667 | 0.175552 | 0.299961 | 0.581415 | 0.772492 | 0.215526 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.649718 | 0.726337 | 0.268889 | 0.259267 | 0.579235 | 0.743169 | -0.163934 | 0.175532 | 0.193033 | 0.495404 | 0.680561 | 0.218527 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.630375 | 0.690353 | 0.225168 | 0.245383 | 0.589529 | 0.728796 | -0.139267 | 0.168117 | 0.261334 | 0.523515 | 0.712555 | 0.221724 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.638389 | 0.661861 | 0.216021 | 0.232101 | 0.632425 | 0.752568 | -0.120143 | 0.173233 | 0.284434 | 0.559226 | 0.74243 | 0.218655 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.616185 | 0.630842 | 0.214089 | 0.218758 | 0.667478 | 0.786087 | -0.118609 | 0.163453 | 0.346296 | 0.594657 | 0.767931 | 0.218099 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.592732 | 0.616881 | 0.160619 | 0.212858 | 0.673211 | 0.764393 | -0.0911814 | 0.160048 | 0.374739 | 0.627711 | 0.790912 | 0.213616 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | 0.0810425 | 0.871235 | -2.8681 | -1.27084 | -0.416851 | -0.0039984 | 0.55613 | 1.72181 | 3.46521 |
| player | theta_2 | 1197 | -0.0314307 | 1.01961 | -3.80998 | -1.4923 | -0.587417 | -0.162891 | 0.466047 | 1.81158 | 4.4837 |
| player | theta_3 | 1197 | 1.14806 | 1.36884 | -4.20432 | -1.22163 | 0.117028 | 1.36471 | 2.2455 | 3.00032 | 4.20056 |
| player | theta_norm | 1197 | 2.01045 | 0.97664 | 0.178545 | 0.57809 | 1.22342 | 1.93419 | 2.70975 | 3.73482 | 5.57113 |
| tossup | start_difficulty_d1 | 1240 | 1.24664 | 0.714472 | -1.04407 | 0.00254319 | 0.710743 | 1.38268 | 1.79028 | 2.2814 | 2.83184 |
| tossup | start_difficulty_d2 | 1240 | 0.469396 | 0.640545 | -1.74587 | -0.574993 | 0.0994363 | 0.453576 | 0.837808 | 1.56702 | 2.90222 |
| tossup | start_difficulty_d3 | 1240 | 1.57897 | 1.11386 | -1.31606 | 0.0134152 | 0.598094 | 1.35171 | 2.64135 | 3.1466 | 4.17408 |
| tossup | end_difficulty_d1 | 1240 | 0.100309 | 0.546205 | -1.97959 | -0.959862 | -0.21006 | 0.268527 | 0.484688 | 0.755694 | 1.16756 |
| tossup | end_difficulty_d2 | 1240 | -0.459888 | 0.719408 | -2.88976 | -1.67405 | -0.877601 | -0.484708 | -0.0422178 | 0.760472 | 2.17274 |
| tossup | end_difficulty_d3 | 1240 | 0.326671 | 0.803278 | -2.98572 | -0.947695 | -0.316109 | 0.369041 | 1.0259 | 1.42419 | 2.23178 |
| tossup | total_drop_d1 | 1240 | 1.14633 | 0.335844 | 0.320326 | 0.777464 | 0.898727 | 1.03555 | 1.3582 | 1.76007 | 2.92425 |
| tossup | total_drop_d2 | 1240 | 0.929284 | 0.125943 | 0.64589 | 0.760379 | 0.864532 | 0.920776 | 0.97966 | 1.09974 | 2.57234 |
| tossup | total_drop_d3 | 1240 | 1.2523 | 0.512387 | 0.546853 | 0.747569 | 0.867086 | 0.986334 | 1.59468 | 2.23118 | 3.31079 |
| tossup | drop_share_1_d1 | 1240 | 0.20607 | 0.0862783 | 0.0488708 | 0.0880215 | 0.125721 | 0.200871 | 0.284551 | 0.311133 | 0.635832 |
| tossup | drop_share_2_d1 | 1240 | 0.266938 | 0.0966031 | 0.069642 | 0.111196 | 0.17775 | 0.315679 | 0.34411 | 0.365373 | 0.701488 |
| tossup | drop_share_3_d1 | 1240 | 0.526992 | 0.168426 | 0.139511 | 0.344871 | 0.370882 | 0.479996 | 0.690399 | 0.791555 | 0.879891 |
| tossup | drop_share_1_d2 | 1240 | 0.286695 | 0.0234276 | 0.126917 | 0.245017 | 0.278029 | 0.290665 | 0.301117 | 0.314724 | 0.336361 |
| tossup | drop_share_2_d2 | 1240 | 0.341775 | 0.0162007 | 0.170669 | 0.319511 | 0.334736 | 0.34315 | 0.351075 | 0.361486 | 0.409553 |
| tossup | drop_share_3_d2 | 1240 | 0.37153 | 0.0327495 | 0.311495 | 0.340104 | 0.353811 | 0.364266 | 0.379299 | 0.429498 | 0.698187 |
| tossup | drop_share_1_d3 | 1240 | 0.233336 | 0.0963125 | 0.0386136 | 0.0767878 | 0.140353 | 0.272471 | 0.294383 | 0.325886 | 0.679864 |
| tossup | drop_share_2_d3 | 1240 | 0.295232 | 0.100155 | 0.0434806 | 0.112592 | 0.226992 | 0.333215 | 0.347309 | 0.42224 | 0.767636 |
| tossup | drop_share_3_d3 | 1240 | 0.471432 | 0.166525 | 0.0611781 | 0.323421 | 0.362962 | 0.386795 | 0.581264 | 0.799455 | 0.917906 |
| tossup | r_1 | 1240 | 0.375218 | 0.298946 | 0.0149632 | 0.020727 | 0.0510898 | 0.450376 | 0.630173 | 0.836023 | 0.926334 |
| tossup | r_2 | 1240 | 0.142156 | 0.123233 | 0.0134119 | 0.0230342 | 0.0536493 | 0.100411 | 0.184134 | 0.42582 | 0.591895 |
| tossup | r_3 | 1240 | 0.482626 | 0.341404 | 0.0283437 | 0.0526071 | 0.128479 | 0.399594 | 0.846901 | 0.931315 | 0.96008 |
| tossup | r_norm | 1240 | 0.777453 | 0.102143 | 0.59032 | 0.633109 | 0.677926 | 0.774893 | 0.871874 | 0.932631 | 0.960509 |
