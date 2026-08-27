# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 283002 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.716142 |
| log_loss | 0.48962 |
| ece | 0.0133403 |
| brier | 0.159161 |
| accuracy | 0.776439 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0111888 |
| probability_std | 0.139301 |
| probability_p10 | 0.58301 |
| probability_p50 | 0.815306 |
| probability_p90 | 0.916788 |
| mean_predictive_variance | 0.1538 |
| integrated_brier_score | 0.102139 |
| joint_tossup_event_log_loss | 6.62402 |
| buzz_position_mae | 0.152571 |
| buzz_position_median_absolute_error | 0.135821 |
| buzz_position_bias | -0.0425869 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.354492 |
| first_buzzer_mean_reciprocal_rank | 0.567756 |
| first_buzzer_log_loss | 1.66891 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.716142 |
| neg_average_precision | 0.448805 |
| neg_precision | 0.602767 |
| neg_recall | 0.13978 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.188776 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0159887 |
| no_buzz_calibration_error | 0.00271904 |
| no_buzz_brier | 0.0131148 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.716142 | 0.48962 | 0.0133403 | 0.159161 | 0.776439 | 0.76525 | 0.0111888 | 0.139301 | 0.58301 | 0.815306 | 0.916788 | 0.1538 |
| tossup_correctness | tier | fall | 2933 | 0.712571 | 0.462227 | 0.0112251 | 0.147846 | 0.797477 | 0.791681 | 0.00579611 | 0.140667 | 0.585051 | 0.823343 | 0.922275 | 0.150106 |
| tossup_correctness | tier | nationals | 1584 | 0.711483 | 0.531811 | 0.0414397 | 0.175851 | 0.748737 | 0.724747 | 0.0239899 | 0.145671 | 0.55518 | 0.808101 | 0.910848 | 0.158636 |
| tossup_correctness | tier | regionals | 1886 | 0.711517 | 0.515254 | 0.0271974 | 0.170457 | 0.755567 | 0.746023 | 0.00954401 | 0.132729 | 0.585307 | 0.801707 | 0.90745 | 0.160039 |
| tossup_correctness | tier | winter | 2892 | 0.721437 | 0.477577 | 0.0141196 | 0.15413 | 0.783887 | 0.773167 | 0.0107192 | 0.137807 | 0.600287 | 0.818951 | 0.919169 | 0.150829 |
| tossup_correctness | category | Current Events | 124 | 0.676032 | 0.52432 | 0.103316 | 0.169467 | 0.758065 | 0.75 | 0.00806452 | 0.155166 | 0.548147 | 0.767729 | 0.918311 | 0.166538 |
| tossup_correctness | category | Fine Arts | 1103 | 0.709997 | 0.497223 | 0.0212368 | 0.161489 | 0.773345 | 0.759746 | 0.0135993 | 0.14448 | 0.593883 | 0.820852 | 0.921314 | 0.150945 |
| tossup_correctness | category | Geography | 197 | 0.787179 | 0.520246 | 0.0760247 | 0.171724 | 0.741117 | 0.670051 | 0.071066 | 0.20732 | 0.404722 | 0.743717 | 0.90902 | 0.169605 |
| tossup_correctness | category | History | 1491 | 0.727094 | 0.461459 | 0.021979 | 0.148166 | 0.790744 | 0.787391 | 0.00335345 | 0.132353 | 0.594036 | 0.815662 | 0.919998 | 0.153161 |
| tossup_correctness | category | Literature | 1472 | 0.730607 | 0.43733 | 0.0300489 | 0.137627 | 0.813179 | 0.804348 | 0.00883152 | 0.115289 | 0.654298 | 0.848067 | 0.923449 | 0.137508 |
| tossup_correctness | category | Mythology | 332 | 0.693608 | 0.447439 | 0.0139834 | 0.140843 | 0.813253 | 0.813253 | 0 | 0.111206 | 0.642874 | 0.831867 | 0.915233 | 0.145049 |
| tossup_correctness | category | Other Academic | 69 | 0.70362 | 0.506584 | 0.060565 | 0.166727 | 0.782609 | 0.753623 | 0.0289855 | 0.100026 | 0.643762 | 0.789124 | 0.897878 | 0.163757 |
| tossup_correctness | category | Philosophy | 324 | 0.692664 | 0.463162 | 0.0293709 | 0.147901 | 0.79321 | 0.799383 | -0.00617284 | 0.121331 | 0.61279 | 0.816807 | 0.920369 | 0.152202 |
| tossup_correctness | category | Popular Culture | 102 | 0.431834 | 0.483678 | 0.0526914 | 0.148114 | 0.823529 | 0.833333 | -0.00980392 | 0.0780654 | 0.73781 | 0.85083 | 0.907905 | 0.130401 |
| tossup_correctness | category | Religion | 372 | 0.718996 | 0.541918 | 0.0491465 | 0.183004 | 0.733871 | 0.709677 | 0.0241935 | 0.14587 | 0.530344 | 0.769954 | 0.906051 | 0.169794 |
| tossup_correctness | category | Science | 1487 | 0.688799 | 0.515349 | 0.0272721 | 0.169422 | 0.765972 | 0.752522 | 0.0134499 | 0.148787 | 0.538498 | 0.802951 | 0.91498 | 0.159066 |
| tossup_correctness | category | Social Science | 336 | 0.729788 | 0.537812 | 0.0506844 | 0.179035 | 0.732143 | 0.702381 | 0.0297619 | 0.17467 | 0.483816 | 0.791908 | 0.914071 | 0.16264 |
| tossup_correctness | category | Unknown | 1886 | 0.711517 | 0.515254 | 0.0271974 | 0.170457 | 0.755567 | 0.746023 | 0.00954401 | 0.132729 | 0.585307 | 0.801707 | 0.90745 | 0.160039 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.691379 | 0.523192 | 0.069003 | 0.167566 | 0.786802 | 0.736041 | 0.0507614 | 0.143046 | 0.537098 | 0.758725 | 0.887917 | 0.175376 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.717047 | 0.519918 | 0.027369 | 0.172452 | 0.747208 | 0.735025 | 0.0121827 | 0.142244 | 0.563295 | 0.796357 | 0.905199 | 0.162362 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.70037 | 0.495315 | 0.0195998 | 0.161179 | 0.77299 | 0.769436 | 0.00355398 | 0.135867 | 0.601337 | 0.817086 | 0.916265 | 0.15224 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.70366 | 0.475045 | 0.0144652 | 0.152648 | 0.794138 | 0.78402 | 0.0101186 | 0.130526 | 0.612003 | 0.828674 | 0.921854 | 0.147833 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.737426 | 0.487116 | 0.0236665 | 0.158955 | 0.771028 | 0.756008 | 0.01502 | 0.146666 | 0.557874 | 0.811925 | 0.916038 | 0.156447 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 2.67573 | 0.734419 | 0.489192 | 1.46918 | 2.17765 | 2.67098 | 3.13825 | 3.96047 | 4.61538 |
| player | theta_1 | 1186 | -1.19697 | 0.821005 | -3.64376 | -2.46936 | -1.71268 | -1.24937 | -0.708966 | 0.247685 | 1.89803 |
| player | theta_2 | 1186 | -1.01513 | 0.659043 | -3.48247 | -2.0461 | -1.44581 | -1.05207 | -0.599973 | 0.0883582 | 1.45037 |
| player | theta_3 | 1186 | -1.11427 | 0.774533 | -3.32652 | -2.28755 | -1.64767 | -1.16623 | -0.638988 | 0.252877 | 2.23461 |
| player | theta_norm | 1186 | 2.24684 | 0.603073 | 0.0803886 | 1.34651 | 1.82655 | 2.20586 | 2.61442 | 3.28467 | 4.3933 |
| tossup | start_difficulty_d1 | 1240 | -1.77854 | 0.550014 | -3.74795 | -2.53132 | -2.15589 | -1.84237 | -1.45603 | -0.823127 | 1.10407 |
| tossup | start_difficulty_d2 | 1240 | -1.76857 | 0.511835 | -3.25979 | -2.51996 | -2.11956 | -1.82667 | -1.44382 | -0.828961 | 0.312983 |
| tossup | start_difficulty_d3 | 1240 | -1.76759 | 0.515098 | -3.61495 | -2.55527 | -2.12803 | -1.80681 | -1.43926 | -0.899699 | 1.26066 |
| tossup | end_difficulty_d1 | 1240 | -2.7675 | 0.640706 | -4.94581 | -3.66016 | -3.21255 | -2.84885 | -2.39045 | -1.68116 | 0.508415 |
| tossup | end_difficulty_d2 | 1240 | -2.75473 | 0.599459 | -4.58928 | -3.67997 | -3.16035 | -2.80563 | -2.37863 | -1.65846 | -0.331473 |
| tossup | end_difficulty_d3 | 1240 | -2.75158 | 0.60023 | -4.90174 | -3.68965 | -3.17039 | -2.78205 | -2.36519 | -1.75586 | 0.557 |
| tossup | total_drop_d1 | 1240 | 0.988962 | 0.110928 | 0.59566 | 0.800418 | 0.916275 | 0.994044 | 1.06189 | 1.1524 | 1.44934 |
| tossup | total_drop_d2 | 1240 | 0.986159 | 0.103121 | 0.644456 | 0.815317 | 0.916015 | 0.989037 | 1.05627 | 1.15578 | 1.32949 |
| tossup | total_drop_d3 | 1240 | 0.983989 | 0.103433 | 0.619088 | 0.818215 | 0.912658 | 0.986298 | 1.05073 | 1.15927 | 1.3727 |
| tossup | drop_share_1_d1 | 1240 | 0.304116 | 0.0154146 | 0.231287 | 0.278948 | 0.294409 | 0.304489 | 0.31408 | 0.327859 | 0.365488 |
| tossup | drop_share_2_d1 | 1240 | 0.347127 | 0.0114593 | 0.310384 | 0.327722 | 0.339488 | 0.347126 | 0.354904 | 0.365 | 0.400689 |
| tossup | drop_share_3_d1 | 1240 | 0.348757 | 0.0163909 | 0.296582 | 0.32408 | 0.337667 | 0.348017 | 0.359164 | 0.375572 | 0.416515 |
| tossup | drop_share_1_d2 | 1240 | 0.303653 | 0.0140008 | 0.25396 | 0.279161 | 0.294743 | 0.303932 | 0.313276 | 0.326606 | 0.342364 |
| tossup | drop_share_2_d2 | 1240 | 0.346937 | 0.0114247 | 0.309442 | 0.327574 | 0.339301 | 0.346667 | 0.354781 | 0.365443 | 0.386157 |
| tossup | drop_share_3_d2 | 1240 | 0.34941 | 0.0155335 | 0.303273 | 0.3251 | 0.338858 | 0.349663 | 0.359472 | 0.375778 | 0.41725 |
| tossup | drop_share_1_d3 | 1240 | 0.303551 | 0.014904 | 0.242704 | 0.278715 | 0.29396 | 0.303739 | 0.313973 | 0.32673 | 0.357669 |
| tossup | drop_share_2_d3 | 1240 | 0.347137 | 0.0111803 | 0.306397 | 0.329116 | 0.340032 | 0.347014 | 0.354428 | 0.365595 | 0.385742 |
| tossup | drop_share_3_d3 | 1240 | 0.349312 | 0.0157878 | 0.303312 | 0.325431 | 0.338629 | 0.348882 | 0.358629 | 0.376296 | 0.438182 |
| tossup | r_1 | 1240 | 0.319818 | 0.139073 | 0.0743211 | 0.137081 | 0.216683 | 0.295846 | 0.401294 | 0.582118 | 0.817258 |
| tossup | r_2 | 1240 | 0.334551 | 0.1171 | 0.0630008 | 0.1598 | 0.253744 | 0.324036 | 0.400037 | 0.551488 | 0.802424 |
| tossup | r_3 | 1240 | 0.345631 | 0.125473 | 0.0753938 | 0.158912 | 0.255317 | 0.33893 | 0.414871 | 0.58512 | 0.821107 |
| tossup | r_norm | 1240 | 0.61701 | 0.041553 | 0.577437 | 0.579155 | 0.588079 | 0.603804 | 0.630916 | 0.700042 | 0.830866 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.48985 | 0.483225 | 1.82438 | 3.78403 | 4.21326 | 4.44323 | 4.7406 | 5.38026 | 6.36094 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.44798 | 0.433212 | 2.30867 | 3.7488 | 4.22637 | 4.43119 | 4.65866 | 5.17756 | 6.59846 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.48002 | 0.438492 | 2.58744 | 3.75954 | 4.2399 | 4.47055 | 4.71835 | 5.19616 | 6.22576 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.80757 | 2.25965 | -10.6455 | -3.18465 | 0.783529 | 2.86703 | 3.30113 | 3.67241 | 4.38645 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.2278 | 2.13821 | -8.25165 | -2.84731 | 2.29125 | 3.12117 | 3.39043 | 3.71285 | 4.27904 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.22515 | 2.1795 | -10.2792 | -2.85043 | 2.25964 | 3.11609 | 3.40525 | 3.74963 | 4.26315 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.68228 | 2.43497 | 0.891265 | 0.98361 | 1.05747 | 1.34464 | 3.83191 | 8.04218 | 15.368 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.22019 | 2.27858 | 0.894521 | 0.962321 | 1.02772 | 1.17338 | 1.92018 | 7.67613 | 13.1574 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.25487 | 2.31591 | 0.855641 | 0.968555 | 1.02973 | 1.19619 | 1.93201 | 7.47565 | 14.8339 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.23675 | 0.0785963 | 0.0422566 | 0.0840267 | 0.180073 | 0.268302 | 0.294089 | 0.316495 | 0.529931 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.343344 | 0.0710882 | 0.0606077 | 0.193423 | 0.3355 | 0.351495 | 0.365913 | 0.442646 | 0.71838 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.419906 | 0.125005 | 0.133763 | 0.310474 | 0.348851 | 0.369719 | 0.442823 | 0.704164 | 0.895062 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.253102 | 0.069955 | 0.0298721 | 0.087291 | 0.232872 | 0.279201 | 0.296138 | 0.315274 | 0.593042 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.348391 | 0.06284 | 0.0671078 | 0.221038 | 0.340712 | 0.351534 | 0.363834 | 0.427984 | 0.696926 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.398506 | 0.107572 | 0.101865 | 0.317331 | 0.350126 | 0.36523 | 0.3956 | 0.680308 | 0.888467 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.25011 | 0.069986 | 0.0360692 | 0.0868553 | 0.229458 | 0.275462 | 0.296188 | 0.314607 | 0.572473 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.349437 | 0.0623145 | 0.0914083 | 0.236917 | 0.339527 | 0.351489 | 0.364341 | 0.431006 | 0.704972 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.400453 | 0.10528 | 0.130994 | 0.316922 | 0.349775 | 0.367598 | 0.402208 | 0.67286 | 0.871268 |
| tossup_hazard | hazard_r_1 | 1240 | 0.380424 | 0.269586 | 0.0305374 | 0.0616555 | 0.135478 | 0.309217 | 0.60612 | 0.857723 | 0.936685 |
| tossup_hazard | hazard_r_2 | 1240 | 0.29932 | 0.215686 | 0.0236042 | 0.0551576 | 0.119175 | 0.229197 | 0.461632 | 0.715255 | 0.843344 |
| tossup_hazard | hazard_r_3 | 1240 | 0.320256 | 0.230917 | 0.0221366 | 0.0476683 | 0.131353 | 0.263489 | 0.470661 | 0.782093 | 0.940436 |
