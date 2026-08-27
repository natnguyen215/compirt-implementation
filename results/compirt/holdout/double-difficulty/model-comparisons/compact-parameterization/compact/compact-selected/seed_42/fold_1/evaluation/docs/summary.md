# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/compact-vs-332/compact/compact-selected/seed_42/fold_1/evaluation`
Result root: `results/compirt/holdout/compact-vs-332/compact/compact-selected/seed_42/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 279259 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.69394 |
| log_loss | 0.533138 |
| ece | 0.062714 |
| brier | 0.172199 |
| accuracy | 0.759815 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00230947 |
| probability_std | 0.214429 |
| probability_p10 | 0.418627 |
| probability_p50 | 0.824146 |
| probability_p90 | 0.95748 |
| mean_predictive_variance | 0.139777 |
| integrated_brier_score | 0.094299 |
| joint_tossup_event_log_loss | 6.44195 |
| buzz_position_mae | 0.140845 |
| buzz_position_median_absolute_error | 0.119811 |
| buzz_position_bias | -0.0295804 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.386891 |
| first_buzzer_mean_reciprocal_rank | 0.595039 |
| first_buzzer_log_loss | 1.58928 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.69394 |
| neg_average_precision | 0.417458 |
| neg_precision | 0.491633 |
| neg_recall | 0.285252 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.179092 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.00909266 |
| no_buzz_calibration_error | -0.00681643 |
| no_buzz_brier | 0.0150279 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.69394 | 0.533138 | 0.062714 | 0.172199 | 0.759815 | 0.762125 | -0.00230947 | 0.214429 | 0.418627 | 0.824146 | 0.95748 | 0.139777 |
| tossup_correctness | tier | fall | 2842 | 0.700867 | 0.498023 | 0.0552433 | 0.160637 | 0.777973 | 0.785362 | -0.00738916 | 0.199376 | 0.471429 | 0.838901 | 0.959086 | 0.136208 |
| tossup_correctness | tier | nationals | 1564 | 0.694102 | 0.579127 | 0.0759708 | 0.189548 | 0.735934 | 0.718031 | 0.0179028 | 0.222829 | 0.380602 | 0.810289 | 0.953225 | 0.14413 |
| tossup_correctness | tier | regionals | 1937 | 0.693003 | 0.540369 | 0.0609106 | 0.173186 | 0.758389 | 0.758389 | 0 | 0.217591 | 0.417963 | 0.831839 | 0.957577 | 0.13717 |
| tossup_correctness | tier | winter | 2750 | 0.686015 | 0.538178 | 0.0706098 | 0.173586 | 0.755636 | 0.765818 | -0.0101818 | 0.220714 | 0.394654 | 0.810434 | 0.957382 | 0.142827 |
| tossup_correctness | category | Current Events | 126 | 0.713118 | 0.508199 | 0.0680351 | 0.167712 | 0.753968 | 0.769841 | -0.015873 | 0.200127 | 0.416356 | 0.767762 | 0.938407 | 0.162407 |
| tossup_correctness | category | Fine Arts | 1071 | 0.732395 | 0.486399 | 0.0397484 | 0.158208 | 0.776844 | 0.766573 | 0.0102708 | 0.204644 | 0.476202 | 0.821495 | 0.955095 | 0.141189 |
| tossup_correctness | category | Geography | 185 | 0.776301 | 0.507379 | 0.0565339 | 0.167962 | 0.745946 | 0.697297 | 0.0486486 | 0.252533 | 0.246961 | 0.707522 | 0.937102 | 0.160738 |
| tossup_correctness | category | History | 1440 | 0.678242 | 0.554076 | 0.0705086 | 0.181095 | 0.7375 | 0.754167 | -0.0166667 | 0.210333 | 0.443592 | 0.815981 | 0.959661 | 0.142659 |
| tossup_correctness | category | Literature | 1422 | 0.662339 | 0.514382 | 0.0898503 | 0.161301 | 0.784107 | 0.814346 | -0.0302391 | 0.217138 | 0.436383 | 0.860434 | 0.970019 | 0.124405 |
| tossup_correctness | category | Mythology | 318 | 0.625201 | 0.515553 | 0.0537063 | 0.16349 | 0.779874 | 0.789308 | -0.00943396 | 0.156246 | 0.557456 | 0.857178 | 0.946642 | 0.133423 |
| tossup_correctness | category | Other Academic | 66 | 0.792833 | 0.499026 | 0.0608794 | 0.166894 | 0.742424 | 0.712121 | 0.030303 | 0.18399 | 0.472148 | 0.83774 | 0.934454 | 0.149868 |
| tossup_correctness | category | Philosophy | 311 | 0.751691 | 0.498672 | 0.0527767 | 0.167287 | 0.745981 | 0.745981 | 0 | 0.193136 | 0.475544 | 0.80985 | 0.948535 | 0.144137 |
| tossup_correctness | category | Popular Culture | 102 | 0.473148 | 0.390388 | 0.0544392 | 0.111442 | 0.882353 | 0.882353 | 0 | 0.0743073 | 0.766488 | 0.884055 | 0.939951 | 0.108178 |
| tossup_correctness | category | Religion | 358 | 0.68795 | 0.579377 | 0.107722 | 0.191117 | 0.726257 | 0.712291 | 0.0139665 | 0.208343 | 0.402329 | 0.774957 | 0.934849 | 0.161107 |
| tossup_correctness | category | Science | 1433 | 0.676509 | 0.577016 | 0.0884247 | 0.18771 | 0.743894 | 0.738311 | 0.00558269 | 0.230034 | 0.353804 | 0.809977 | 0.958198 | 0.142788 |
| tossup_correctness | category | Social Science | 324 | 0.734468 | 0.515142 | 0.0526947 | 0.168969 | 0.780864 | 0.731481 | 0.0493827 | 0.207047 | 0.398821 | 0.789426 | 0.92758 | 0.157649 |
| tossup_correctness | category | Unknown | 1937 | 0.693003 | 0.540369 | 0.0609106 | 0.173186 | 0.758389 | 0.758389 | 0 | 0.217591 | 0.417963 | 0.831839 | 0.957577 | 0.13717 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.658964 | 0.606287 | 0.114775 | 0.202232 | 0.694611 | 0.712575 | -0.0179641 | 0.173812 | 0.539689 | 0.804273 | 0.947198 | 0.14443 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.711096 | 0.553869 | 0.0643343 | 0.17867 | 0.745614 | 0.729167 | 0.0164474 | 0.219762 | 0.408871 | 0.824289 | 0.963382 | 0.138735 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.696146 | 0.536135 | 0.0682749 | 0.172989 | 0.759338 | 0.755083 | 0.00425532 | 0.197472 | 0.482959 | 0.847844 | 0.962478 | 0.132985 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.678926 | 0.520279 | 0.0640627 | 0.165835 | 0.771449 | 0.780942 | -0.00949367 | 0.200502 | 0.471007 | 0.838561 | 0.956551 | 0.136577 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.705405 | 0.532846 | 0.0777695 | 0.174003 | 0.757119 | 0.762029 | -0.00490998 | 0.233304 | 0.342738 | 0.792474 | 0.952405 | 0.147515 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 2.03198 | 0.578082 | -0.135508 | 1.10261 | 1.61153 | 2.04469 | 2.43413 | 2.94828 | 4.03097 |
| player | theta_1 | 1167 | -1.39434 | 0.677522 | -3.44278 | -2.46996 | -1.87578 | -1.38683 | -0.915332 | -0.292008 | 0.302287 |
| player | theta_2 | 1167 | -1.30538 | 0.645229 | -2.9615 | -2.28439 | -1.81995 | -1.31237 | -0.841238 | -0.237073 | 0.503189 |
| player | theta_3 | 1167 | -1.28697 | 0.656641 | -3.05037 | -2.32694 | -1.7831 | -1.29831 | -0.804187 | -0.192455 | 0.608214 |
| player | theta_norm | 1167 | 2.4972 | 0.611741 | 0.812948 | 1.49176 | 2.05431 | 2.48702 | 2.9476 | 3.52344 | 4.27355 |
| tossup | start_difficulty | 1220 | -3.24595 | 0.803942 | -5.21893 | -4.57554 | -3.79213 | -3.25644 | -2.70257 | -1.89571 | -0.848437 |
| tossup | end_difficulty | 1220 | -4.27844 | 0.977539 | -7.26677 | -5.94585 | -4.93628 | -4.25145 | -3.59259 | -2.72343 | -1.54939 |
| tossup | total_drop | 1220 | 1.03249 | 0.302198 | 0.607363 | 0.724202 | 0.854559 | 0.969727 | 1.12039 | 1.54084 | 3.5903 |
| tossup | drop_share_1 | 1220 | 0.294005 | 0.0292211 | 0.131569 | 0.243066 | 0.280356 | 0.297523 | 0.3125 | 0.335112 | 0.383298 |
| tossup | drop_share_2 | 1220 | 0.347968 | 0.017304 | 0.240336 | 0.32242 | 0.337873 | 0.346929 | 0.356972 | 0.373779 | 0.465193 |
| tossup | drop_share_3 | 1220 | 0.358027 | 0.033275 | 0.271449 | 0.314173 | 0.338086 | 0.35412 | 0.372768 | 0.410259 | 0.628095 |
| tossup | r_1 | 1220 | 0.993407 | 0.769193 | 0.0452709 | 0.126762 | 0.378156 | 0.778147 | 1.38531 | 2.57313 | 4.20654 |
| tossup | r_2 | 1220 | 0.796118 | 0.620233 | 0.0461685 | 0.122243 | 0.289385 | 0.624449 | 1.15368 | 2.01262 | 3.13245 |
| tossup | r_3 | 1220 | 0.810689 | 0.685855 | 0.0463644 | 0.114709 | 0.299016 | 0.60008 | 1.08531 | 2.33384 | 3.66974 |
| tossup | r_norm | 1220 | 1.82503 | 0.626926 | 0.420412 | 0.911845 | 1.35765 | 1.79684 | 2.21867 | 2.95695 | 4.23489 |
| tossup_hazard | hazard_start_difficulty | 1220 | 3.78524 | 0.612683 | 1.70744 | 2.77174 | 3.37034 | 3.78932 | 4.22991 | 4.80935 | 5.62727 |
| tossup_hazard | hazard_end_difficulty | 1220 | -1.17815 | 1.525 | -7.63007 | -3.63517 | -2.131 | -1.22595 | -0.209494 | 1.3943 | 3.4582 |
| tossup_hazard | hazard_total_drop | 1220 | 4.96339 | 1.49567 | 0.968657 | 2.41786 | 4.04887 | 4.96935 | 5.84444 | 7.31549 | 11.9407 |
| tossup_hazard | hazard_drop_share_1 | 1220 | 0.158682 | 0.0872635 | 0.0367235 | 0.0680109 | 0.0996919 | 0.135457 | 0.19473 | 0.327973 | 0.581472 |
| tossup_hazard | hazard_drop_share_2 | 1220 | 0.315626 | 0.136031 | 0.0513339 | 0.118658 | 0.206388 | 0.305771 | 0.408037 | 0.569281 | 0.728632 |
| tossup_hazard | hazard_drop_share_3 | 1220 | 0.525692 | 0.186831 | 0.0738339 | 0.207553 | 0.376768 | 0.531332 | 0.680579 | 0.802824 | 0.905468 |
