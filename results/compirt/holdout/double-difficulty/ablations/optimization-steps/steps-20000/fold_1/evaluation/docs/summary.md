# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/optimization-steps/steps-20000/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/optimization-steps/steps-20000/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 20000 |
| pyramidal | final_loss | 277001 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.708619 |
| log_loss | 0.498203 |
| ece | 0.0129313 |
| brier | 0.162059 |
| accuracy | 0.772242 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0101177 |
| probability_std | 0.152276 |
| probability_p10 | 0.553869 |
| probability_p50 | 0.809278 |
| probability_p90 | 0.923975 |
| mean_predictive_variance | 0.154435 |
| integrated_brier_score | 0.0937498 |
| joint_tossup_event_log_loss | 6.45292 |
| buzz_position_mae | 0.138577 |
| buzz_position_median_absolute_error | 0.117046 |
| buzz_position_bias | -0.00711534 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.362587 |
| first_buzzer_mean_reciprocal_rank | 0.57602 |
| first_buzzer_log_loss | 1.64308 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.708619 |
| neg_average_precision | 0.443197 |
| neg_precision | 0.572555 |
| neg_recall | 0.167822 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.185309 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.00987379 |
| no_buzz_calibration_error | -0.0060353 |
| no_buzz_brier | 0.0153507 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.708619 | 0.498203 | 0.0129313 | 0.162059 | 0.772242 | 0.762125 | 0.0101177 | 0.152276 | 0.553869 | 0.809278 | 0.923975 | 0.154435 |
| tossup_correctness | tier | fall | 2842 | 0.726332 | 0.464632 | 0.0153143 | 0.149345 | 0.793103 | 0.785362 | 0.00774103 | 0.143396 | 0.569692 | 0.820234 | 0.928801 | 0.150536 |
| tossup_correctness | tier | nationals | 1564 | 0.714754 | 0.540088 | 0.0417829 | 0.17956 | 0.73977 | 0.718031 | 0.0217391 | 0.162016 | 0.530112 | 0.798713 | 0.918019 | 0.158523 |
| tossup_correctness | tier | regionals | 1937 | 0.691364 | 0.51122 | 0.0199917 | 0.167107 | 0.762003 | 0.758389 | 0.00361384 | 0.151751 | 0.553153 | 0.807249 | 0.919116 | 0.156332 |
| tossup_correctness | tier | winter | 2750 | 0.696626 | 0.499907 | 0.0147137 | 0.161688 | 0.776364 | 0.765818 | 0.0105455 | 0.154949 | 0.551979 | 0.805734 | 0.923972 | 0.154805 |
| tossup_correctness | category | Current Events | 126 | 0.724849 | 0.488875 | 0.0985532 | 0.159041 | 0.785714 | 0.769841 | 0.015873 | 0.132576 | 0.525931 | 0.760505 | 0.881745 | 0.177353 |
| tossup_correctness | category | Fine Arts | 1071 | 0.744706 | 0.472056 | 0.028639 | 0.152614 | 0.787115 | 0.766573 | 0.0205415 | 0.160475 | 0.547937 | 0.803057 | 0.924843 | 0.154761 |
| tossup_correctness | category | Geography | 185 | 0.798726 | 0.492999 | 0.0737109 | 0.162066 | 0.740541 | 0.697297 | 0.0432432 | 0.225697 | 0.329185 | 0.759579 | 0.894844 | 0.166021 |
| tossup_correctness | category | History | 1440 | 0.703127 | 0.513393 | 0.0348797 | 0.168614 | 0.759722 | 0.754167 | 0.00555556 | 0.148112 | 0.560175 | 0.810497 | 0.9281 | 0.153158 |
| tossup_correctness | category | Literature | 1422 | 0.673434 | 0.456377 | 0.0234682 | 0.143724 | 0.807314 | 0.814346 | -0.00703235 | 0.134455 | 0.61961 | 0.836525 | 0.935674 | 0.140463 |
| tossup_correctness | category | Mythology | 318 | 0.654933 | 0.488591 | 0.044212 | 0.154373 | 0.805031 | 0.789308 | 0.0157233 | 0.128649 | 0.631257 | 0.82574 | 0.931528 | 0.145873 |
| tossup_correctness | category | Other Academic | 66 | 0.795073 | 0.516045 | 0.10519 | 0.173703 | 0.727273 | 0.712121 | 0.0151515 | 0.13988 | 0.623143 | 0.804446 | 0.89573 | 0.159009 |
| tossup_correctness | category | Philosophy | 311 | 0.711971 | 0.517614 | 0.0738349 | 0.172862 | 0.733119 | 0.745981 | -0.0128617 | 0.14006 | 0.576519 | 0.816162 | 0.921136 | 0.153143 |
| tossup_correctness | category | Popular Culture | 102 | 0.526852 | 0.384992 | 0.0701233 | 0.110002 | 0.882353 | 0.882353 | 0 | 0.0828617 | 0.709722 | 0.856091 | 0.912229 | 0.13494 |
| tossup_correctness | category | Religion | 358 | 0.71285 | 0.540828 | 0.0282463 | 0.179803 | 0.73743 | 0.712291 | 0.0251397 | 0.164521 | 0.483653 | 0.775788 | 0.897083 | 0.171451 |
| tossup_correctness | category | Science | 1433 | 0.699302 | 0.526083 | 0.028643 | 0.173431 | 0.759246 | 0.738311 | 0.0209351 | 0.15256 | 0.542937 | 0.795635 | 0.918366 | 0.160012 |
| tossup_correctness | category | Social Science | 324 | 0.782094 | 0.481871 | 0.049922 | 0.156883 | 0.774691 | 0.731481 | 0.0432099 | 0.161577 | 0.488248 | 0.790261 | 0.894773 | 0.164878 |
| tossup_correctness | category | Unknown | 1937 | 0.691364 | 0.51122 | 0.0199917 | 0.167107 | 0.762003 | 0.758389 | 0.00361384 | 0.151751 | 0.553153 | 0.807249 | 0.919116 | 0.156332 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.592262 | 0.621002 | 0.090616 | 0.209206 | 0.688623 | 0.712575 | -0.0239521 | 0.137552 | 0.555845 | 0.769237 | 0.888825 | 0.173506 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.719704 | 0.524176 | 0.0212555 | 0.173272 | 0.753289 | 0.729167 | 0.0241228 | 0.167456 | 0.49923 | 0.779726 | 0.913347 | 0.164163 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.71081 | 0.504691 | 0.0266523 | 0.164963 | 0.770213 | 0.755083 | 0.01513 | 0.145144 | 0.57739 | 0.811881 | 0.92188 | 0.152828 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.69287 | 0.484178 | 0.0101906 | 0.15541 | 0.788326 | 0.780942 | 0.00738397 | 0.136934 | 0.596708 | 0.818496 | 0.924185 | 0.149777 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.720509 | 0.492301 | 0.0152274 | 0.160312 | 0.768903 | 0.762029 | 0.00687398 | 0.164012 | 0.514797 | 0.805484 | 0.927668 | 0.155939 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 0.799792 | 0.846409 | -1.6765 | -0.531515 | 0.233389 | 0.787625 | 1.34793 | 2.26442 | 3.11528 |
| player | theta_1 | 1167 | -0.412032 | 0.940356 | -2.90988 | -1.78653 | -1.02784 | -0.524509 | 0.126515 | 1.31524 | 3.7536 |
| player | theta_2 | 1167 | -0.371089 | 0.85502 | -2.9777 | -1.76338 | -0.900461 | -0.432085 | 0.130564 | 1.10667 | 2.67617 |
| player | theta_3 | 1167 | -0.377101 | 0.954328 | -3.30864 | -1.74518 | -1.00206 | -0.483772 | 0.149142 | 1.37446 | 3.09032 |
| player | theta_norm | 1167 | 1.58738 | 0.673945 | 0.105876 | 0.60192 | 1.11657 | 1.49021 | 1.98433 | 2.85733 | 4.76629 |
| tossup | start_difficulty_d1 | 1220 | -0.96635 | 0.525342 | -2.39502 | -1.71366 | -1.30506 | -1.0021 | -0.668926 | -0.153878 | 2.06355 |
| tossup | start_difficulty_d2 | 1220 | -0.965038 | 0.490948 | -2.60726 | -1.67092 | -1.29468 | -1.00867 | -0.68201 | -0.0916119 | 1.14257 |
| tossup | start_difficulty_d3 | 1220 | -0.969997 | 0.505242 | -2.83135 | -1.72406 | -1.28788 | -0.968732 | -0.670565 | -0.152994 | 1.47322 |
| tossup | end_difficulty_d1 | 1220 | -1.96323 | 0.61642 | -3.73394 | -2.8827 | -2.35654 | -2.00831 | -1.61915 | -1.00972 | 1.37494 |
| tossup | end_difficulty_d2 | 1220 | -1.96267 | 0.574452 | -3.90317 | -2.78871 | -2.35856 | -2.00747 | -1.62369 | -0.92968 | 0.299274 |
| tossup | end_difficulty_d3 | 1220 | -1.96801 | 0.593253 | -4.16191 | -2.87918 | -2.34395 | -1.96353 | -1.60712 | -1.02025 | 0.852609 |
| tossup | total_drop_d1 | 1220 | 0.996879 | 0.111301 | 0.62685 | 0.80556 | 0.924036 | 0.999419 | 1.0676 | 1.18344 | 1.43022 |
| tossup | total_drop_d2 | 1220 | 0.997635 | 0.104146 | 0.654227 | 0.823911 | 0.928382 | 0.999526 | 1.06487 | 1.16231 | 1.45446 |
| tossup | total_drop_d3 | 1220 | 0.998012 | 0.107202 | 0.611379 | 0.828592 | 0.929861 | 0.992047 | 1.06082 | 1.17837 | 1.41825 |
| tossup | drop_share_1_d1 | 1220 | 0.304626 | 0.0152813 | 0.229069 | 0.280242 | 0.29524 | 0.305153 | 0.31433 | 0.327151 | 0.349166 |
| tossup | drop_share_2_d1 | 1220 | 0.346699 | 0.0113563 | 0.304712 | 0.328658 | 0.339289 | 0.346178 | 0.35446 | 0.365785 | 0.387745 |
| tossup | drop_share_3_d1 | 1220 | 0.348675 | 0.0159853 | 0.308633 | 0.323502 | 0.337614 | 0.348391 | 0.358555 | 0.374832 | 0.432548 |
| tossup | drop_share_1_d2 | 1220 | 0.304003 | 0.0143959 | 0.23045 | 0.280075 | 0.295423 | 0.304446 | 0.312906 | 0.32753 | 0.34897 |
| tossup | drop_share_2_d2 | 1220 | 0.347293 | 0.0111359 | 0.312085 | 0.329444 | 0.339516 | 0.347165 | 0.354694 | 0.365712 | 0.410319 |
| tossup | drop_share_3_d2 | 1220 | 0.348704 | 0.0155427 | 0.309145 | 0.324621 | 0.338514 | 0.348316 | 0.357377 | 0.374999 | 0.415757 |
| tossup | drop_share_1_d3 | 1220 | 0.304981 | 0.0149479 | 0.247136 | 0.278999 | 0.296124 | 0.305022 | 0.314326 | 0.32908 | 0.359118 |
| tossup | drop_share_2_d3 | 1220 | 0.346964 | 0.0110751 | 0.307613 | 0.329349 | 0.339553 | 0.346645 | 0.354334 | 0.365081 | 0.382199 |
| tossup | drop_share_3_d3 | 1220 | 0.348055 | 0.0154389 | 0.300384 | 0.324702 | 0.337638 | 0.347421 | 0.356826 | 0.3734 | 0.414268 |
| tossup | r_1 | 1220 | 0.321471 | 0.166594 | 0.0453213 | 0.108992 | 0.183666 | 0.28899 | 0.433304 | 0.638997 | 0.87963 |
| tossup | r_2 | 1220 | 0.334034 | 0.171576 | 0.0467865 | 0.116762 | 0.202062 | 0.28978 | 0.434999 | 0.688563 | 0.859391 |
| tossup | r_3 | 1220 | 0.344495 | 0.174246 | 0.0535945 | 0.118531 | 0.2066 | 0.312477 | 0.459659 | 0.673928 | 0.859586 |
| tossup | r_norm | 1220 | 0.646267 | 0.0585089 | 0.577428 | 0.582389 | 0.602094 | 0.630231 | 0.676597 | 0.766378 | 0.883787 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 8.69043 | 0.522001 | 5.86976 | 7.81987 | 8.52563 | 8.68509 | 8.91782 | 9.54287 | 10.658 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 8.70034 | 0.478886 | 4.84757 | 7.8644 | 8.58983 | 8.71341 | 8.87835 | 9.4133 | 10.9572 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 8.72493 | 0.506193 | 4.34913 | 7.9799 | 8.59218 | 8.73118 | 8.92526 | 9.46656 | 10.466 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | 4.61731 | 3.94932 | -12.3109 | -2.6179 | 1.66888 | 7.43386 | 7.68298 | 8.01264 | 9.01679 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | 5.46302 | 3.89389 | -11.692 | -2.65416 | 2.6905 | 7.61905 | 7.77369 | 8.07891 | 8.65743 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | 5.67649 | 3.86638 | -14.9366 | -2.5817 | 4.12102 | 7.64718 | 7.83068 | 8.20421 | 8.7845 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 4.07312 | 4.01244 | 0.85619 | 0.944434 | 1.00038 | 1.07499 | 7.05669 | 11.5238 | 21.1221 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 3.23732 | 3.9302 | 0.879496 | 0.932378 | 0.979571 | 1.02541 | 5.71235 | 11.5979 | 21.1238 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 3.04843 | 3.86563 | 0.848927 | 0.923475 | 0.976213 | 1.02157 | 4.34345 | 11.2167 | 24.424 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.272275 | 0.098282 | 0.0390103 | 0.102548 | 0.219505 | 0.295281 | 0.308624 | 0.409966 | 0.737059 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.323046 | 0.0859648 | 0.0621329 | 0.148302 | 0.310671 | 0.342538 | 0.355702 | 0.446786 | 0.730606 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.404679 | 0.137652 | 0.0762035 | 0.231341 | 0.342399 | 0.357392 | 0.426992 | 0.720235 | 0.879976 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.286613 | 0.0866629 | 0.0377081 | 0.121485 | 0.283266 | 0.299324 | 0.311245 | 0.378837 | 0.75706 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.327679 | 0.0728219 | 0.0571277 | 0.16093 | 0.330267 | 0.343761 | 0.353891 | 0.402154 | 0.650113 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.385708 | 0.12035 | 0.0705439 | 0.258367 | 0.342549 | 0.353052 | 0.371334 | 0.6779 | 0.904332 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.286822 | 0.0840045 | 0.0484057 | 0.113249 | 0.280521 | 0.296943 | 0.309166 | 0.388535 | 0.727615 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.33207 | 0.0665666 | 0.0841138 | 0.18378 | 0.330952 | 0.344352 | 0.354765 | 0.399518 | 0.674377 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.381108 | 0.106944 | 0.0570241 | 0.272304 | 0.342634 | 0.355207 | 0.374588 | 0.662322 | 0.845392 |
| tossup_hazard | hazard_r_1 | 1220 | 0.38857 | 0.298953 | 0.0173252 | 0.0395688 | 0.10931 | 0.282113 | 0.6542 | 0.887409 | 0.942881 |
| tossup_hazard | hazard_r_2 | 1220 | 0.295164 | 0.275117 | 0.0117306 | 0.0298309 | 0.0690817 | 0.170376 | 0.52365 | 0.833305 | 0.941271 |
| tossup_hazard | hazard_r_3 | 1220 | 0.316265 | 0.261208 | 0.0145799 | 0.0305609 | 0.0846856 | 0.236784 | 0.493317 | 0.814596 | 0.969021 |
