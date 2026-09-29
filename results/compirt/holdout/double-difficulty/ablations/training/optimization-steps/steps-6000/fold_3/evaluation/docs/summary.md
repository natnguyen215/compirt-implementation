# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/optimization-steps/steps-6000/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/optimization-steps/steps-6000/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 6000 |
| pyramidal | final_loss | 279364 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.710089 |
| log_loss | 0.485884 |
| ece | 0.0101994 |
| brier | 0.157034 |
| accuracy | 0.786233 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0161894 |
| probability_std | 0.14651 |
| probability_p10 | 0.570171 |
| probability_p50 | 0.811429 |
| probability_p90 | 0.919877 |
| mean_predictive_variance | 0.153504 |
| integrated_brier_score | 0.0965134 |
| joint_tossup_event_log_loss | 6.48261 |
| buzz_position_mae | 0.144199 |
| buzz_position_median_absolute_error | 0.124756 |
| buzz_position_bias | -0.029509 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.356388 |
| first_buzzer_mean_reciprocal_rank | 0.572565 |
| first_buzzer_log_loss | 1.65089 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.710089 |
| neg_average_precision | 0.449192 |
| neg_precision | 0.640535 |
| neg_recall | 0.160441 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.177644 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0124632 |
| no_buzz_calibration_error | -0.00272119 |
| no_buzz_brier | 0.0137387 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.710089 | 0.485884 | 0.0101994 | 0.157034 | 0.786233 | 0.770044 | 0.0161894 | 0.14651 | 0.570171 | 0.811429 | 0.919877 | 0.153504 |
| tossup_correctness | tier | fall | 2817 | 0.70226 | 0.478172 | 0.0128125 | 0.153369 | 0.793397 | 0.781683 | 0.0117146 | 0.143201 | 0.569035 | 0.819952 | 0.921984 | 0.151267 |
| tossup_correctness | tier | nationals | 1542 | 0.726379 | 0.513146 | 0.0256931 | 0.169455 | 0.759403 | 0.73476 | 0.0246433 | 0.153709 | 0.544451 | 0.796493 | 0.914247 | 0.15894 |
| tossup_correctness | tier | regionals | 1934 | 0.717172 | 0.496535 | 0.02032 | 0.161735 | 0.774043 | 0.75698 | 0.0170631 | 0.14252 | 0.574441 | 0.806711 | 0.918079 | 0.154587 |
| tossup_correctness | tier | winter | 2787 | 0.699518 | 0.471205 | 0.0227626 | 0.150604 | 0.802296 | 0.786868 | 0.0154288 | 0.14795 | 0.5835 | 0.814066 | 0.92171 | 0.152005 |
| tossup_correctness | category | Current Events | 125 | 0.754607 | 0.528031 | 0.0643159 | 0.17868 | 0.728 | 0.704 | 0.024 | 0.151745 | 0.520895 | 0.774625 | 0.909336 | 0.169025 |
| tossup_correctness | category | Fine Arts | 1072 | 0.729429 | 0.472016 | 0.0113531 | 0.151594 | 0.79291 | 0.770522 | 0.0223881 | 0.152878 | 0.563486 | 0.815851 | 0.920573 | 0.153438 |
| tossup_correctness | category | Geography | 185 | 0.78042 | 0.489866 | 0.0568138 | 0.159942 | 0.772973 | 0.702703 | 0.0702703 | 0.213125 | 0.385368 | 0.751879 | 0.905617 | 0.169005 |
| tossup_correctness | category | History | 1443 | 0.723259 | 0.488166 | 0.0226117 | 0.159997 | 0.775468 | 0.765073 | 0.010395 | 0.151938 | 0.543176 | 0.801493 | 0.91633 | 0.158163 |
| tossup_correctness | category | Literature | 1411 | 0.661217 | 0.459492 | 0.0302238 | 0.14458 | 0.812899 | 0.81219 | 0.000708717 | 0.119195 | 0.657307 | 0.841129 | 0.928803 | 0.138187 |
| tossup_correctness | category | Mythology | 320 | 0.656407 | 0.484838 | 0.0429158 | 0.152485 | 0.8 | 0.79375 | 0.00625 | 0.115549 | 0.633686 | 0.828463 | 0.926782 | 0.146009 |
| tossup_correctness | category | Other Academic | 64 | 0.639323 | 0.566639 | 0.117602 | 0.190544 | 0.71875 | 0.75 | -0.03125 | 0.112413 | 0.649349 | 0.801608 | 0.906073 | 0.152789 |
| tossup_correctness | category | Philosophy | 312 | 0.658 | 0.468367 | 0.0316985 | 0.148697 | 0.814103 | 0.801282 | 0.0128205 | 0.113287 | 0.644132 | 0.815253 | 0.911893 | 0.152888 |
| tossup_correctness | category | Popular Culture | 104 | 0.620739 | 0.418735 | 0.0546102 | 0.125255 | 0.846154 | 0.846154 | 0 | 0.0698759 | 0.735072 | 0.855474 | 0.918833 | 0.128008 |
| tossup_correctness | category | Religion | 358 | 0.712637 | 0.536365 | 0.0397747 | 0.179583 | 0.74581 | 0.726257 | 0.0195531 | 0.146048 | 0.551047 | 0.771123 | 0.897416 | 0.169685 |
| tossup_correctness | category | Science | 1431 | 0.701797 | 0.490798 | 0.0282717 | 0.158686 | 0.791055 | 0.765199 | 0.025856 | 0.151281 | 0.551433 | 0.801875 | 0.914707 | 0.157545 |
| tossup_correctness | category | Social Science | 321 | 0.724615 | 0.500593 | 0.0308644 | 0.161936 | 0.775701 | 0.744548 | 0.0311526 | 0.18091 | 0.502367 | 0.790474 | 0.920867 | 0.159011 |
| tossup_correctness | category | Unknown | 1934 | 0.717172 | 0.496535 | 0.02032 | 0.161735 | 0.774043 | 0.75698 | 0.0170631 | 0.14252 | 0.574441 | 0.806711 | 0.918079 | 0.154587 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.747813 | 0.540535 | 0.0570462 | 0.18297 | 0.723958 | 0.697917 | 0.0260417 | 0.165239 | 0.464448 | 0.747073 | 0.872791 | 0.178765 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.749223 | 0.498182 | 0.0276371 | 0.163323 | 0.773903 | 0.733408 | 0.0404949 | 0.151384 | 0.535855 | 0.788472 | 0.907916 | 0.163009 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.684859 | 0.514977 | 0.0307157 | 0.168023 | 0.768326 | 0.759276 | 0.00904977 | 0.145859 | 0.57821 | 0.813301 | 0.921265 | 0.151948 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.694506 | 0.470943 | 0.0184255 | 0.150755 | 0.800976 | 0.789125 | 0.0118508 | 0.129863 | 0.609946 | 0.825165 | 0.92289 | 0.147325 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.726726 | 0.471208 | 0.0167694 | 0.151267 | 0.793151 | 0.775342 | 0.0178082 | 0.156291 | 0.544423 | 0.803789 | 0.918921 | 0.156197 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 1.91239 | 0.772838 | -0.138783 | 0.640476 | 1.3632 | 1.91958 | 2.41935 | 3.25987 | 3.99548 |
| player | theta_1 | 1133 | -0.790386 | 0.912992 | -3.34041 | -2.09639 | -1.40365 | -0.899899 | -0.304723 | 1.00904 | 3.62989 |
| player | theta_2 | 1133 | -0.644931 | 0.717427 | -3.0474 | -1.88171 | -1.07872 | -0.670106 | -0.1592 | 0.519455 | 2.0393 |
| player | theta_3 | 1133 | -0.788116 | 0.843965 | -3.04075 | -2.04648 | -1.35929 | -0.880656 | -0.274346 | 0.745169 | 2.01303 |
| player | theta_norm | 1133 | 1.82027 | 0.638341 | 0.308245 | 0.80858 | 1.37505 | 1.79307 | 2.22986 | 2.86588 | 4.52239 |
| tossup | start_difficulty_d1 | 1240 | -1.35115 | 0.548189 | -3.1957 | -2.10099 | -1.7101 | -1.41683 | -1.0645 | -0.360907 | 1.77388 |
| tossup | start_difficulty_d2 | 1240 | -1.36203 | 0.486958 | -3.35037 | -2.10902 | -1.68878 | -1.38267 | -1.06455 | -0.549126 | 1.13315 |
| tossup | start_difficulty_d3 | 1240 | -1.36016 | 0.499105 | -3.06013 | -2.13544 | -1.6859 | -1.38077 | -1.0414 | -0.513871 | 0.828011 |
| tossup | end_difficulty_d1 | 1240 | -2.34434 | 0.641544 | -4.76404 | -3.23439 | -2.75933 | -2.41022 | -1.9889 | -1.21142 | 1.10815 |
| tossup | end_difficulty_d2 | 1240 | -2.35426 | 0.572866 | -4.65276 | -3.23358 | -2.73641 | -2.36385 | -1.99421 | -1.40248 | 0.459131 |
| tossup | end_difficulty_d3 | 1240 | -2.35304 | 0.585606 | -4.36987 | -3.27987 | -2.73235 | -2.36974 | -1.97902 | -1.38847 | 0.0606619 |
| tossup | total_drop_d1 | 1240 | 0.993192 | 0.113793 | 0.594508 | 0.800742 | 0.926677 | 0.992667 | 1.06517 | 1.16969 | 1.56834 |
| tossup | total_drop_d2 | 1240 | 0.992225 | 0.102401 | 0.66881 | 0.82723 | 0.925478 | 0.989722 | 1.05787 | 1.16668 | 1.33946 |
| tossup | total_drop_d3 | 1240 | 0.992876 | 0.107819 | 0.618208 | 0.822133 | 0.92218 | 0.987683 | 1.06271 | 1.16851 | 1.65323 |
| tossup | drop_share_1_d1 | 1240 | 0.303416 | 0.0154226 | 0.234251 | 0.278541 | 0.294515 | 0.304212 | 0.313429 | 0.327585 | 0.35535 |
| tossup | drop_share_2_d1 | 1240 | 0.347468 | 0.0113326 | 0.312325 | 0.329542 | 0.340104 | 0.347175 | 0.35448 | 0.366843 | 0.386071 |
| tossup | drop_share_3_d1 | 1240 | 0.349116 | 0.0165015 | 0.299048 | 0.324283 | 0.338066 | 0.348653 | 0.358289 | 0.377171 | 0.417791 |
| tossup | drop_share_1_d2 | 1240 | 0.304412 | 0.0142251 | 0.236741 | 0.281781 | 0.295127 | 0.305079 | 0.313651 | 0.326845 | 0.375493 |
| tossup | drop_share_2_d2 | 1240 | 0.346968 | 0.0111616 | 0.311961 | 0.329107 | 0.339813 | 0.347042 | 0.353715 | 0.365534 | 0.385574 |
| tossup | drop_share_3_d2 | 1240 | 0.34862 | 0.0153667 | 0.292265 | 0.324832 | 0.33814 | 0.347949 | 0.358356 | 0.374284 | 0.404184 |
| tossup | drop_share_1_d3 | 1240 | 0.303545 | 0.0148325 | 0.219437 | 0.280551 | 0.29434 | 0.303856 | 0.312893 | 0.327589 | 0.348903 |
| tossup | drop_share_2_d3 | 1240 | 0.347228 | 0.0111937 | 0.314467 | 0.32952 | 0.339094 | 0.347257 | 0.354535 | 0.365448 | 0.408801 |
| tossup | drop_share_3_d3 | 1240 | 0.349228 | 0.0153717 | 0.30394 | 0.325156 | 0.339536 | 0.348486 | 0.358225 | 0.375024 | 0.441457 |
| tossup | r_1 | 1240 | 0.321718 | 0.160241 | 0.0455957 | 0.113898 | 0.198806 | 0.292132 | 0.425064 | 0.630571 | 0.872519 |
| tossup | r_2 | 1240 | 0.335527 | 0.145777 | 0.0680689 | 0.13333 | 0.230774 | 0.314705 | 0.42479 | 0.619098 | 0.865216 |
| tossup | r_3 | 1240 | 0.342755 | 0.154083 | 0.0579395 | 0.134633 | 0.229405 | 0.31496 | 0.428804 | 0.648436 | 0.826535 |
| tossup | r_norm | 1240 | 0.63334 | 0.0552945 | 0.577438 | 0.58053 | 0.592677 | 0.614084 | 0.655673 | 0.753526 | 0.877201 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 6.15486 | 0.529594 | 3.4408 | 5.29022 | 5.92744 | 6.11105 | 6.35025 | 7.16719 | 8.08526 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 6.18844 | 0.469324 | 3.67784 | 5.51448 | 6.00235 | 6.13049 | 6.31499 | 7.04822 | 8.65073 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 6.1793 | 0.515123 | 3.61345 | 5.34438 | 5.97893 | 6.14394 | 6.36717 | 7.14496 | 8.40242 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 2.98058 | 3.00948 | -10.6325 | -3.04278 | 1.02636 | 4.79592 | 5.08818 | 5.3584 | 6.2103 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 3.77583 | 2.66159 | -11.3524 | -2.36007 | 3.88013 | 5.015 | 5.17281 | 5.48419 | 6.23298 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 3.41536 | 2.70691 | -8.91198 | -2.25383 | 1.8209 | 4.94912 | 5.16482 | 5.47505 | 6.12605 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.17427 | 3.13462 | 0.829176 | 0.95986 | 1.01848 | 1.10786 | 5.32356 | 9.52679 | 17.0436 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.41261 | 2.81205 | 0.889782 | 0.947182 | 0.99405 | 1.0391 | 1.55637 | 8.94379 | 17.3489 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.76394 | 2.81876 | 0.862521 | 0.944229 | 0.999995 | 1.05556 | 4.69177 | 8.69027 | 15.274 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.250206 | 0.0893259 | 0.0354315 | 0.0847438 | 0.184555 | 0.28909 | 0.303948 | 0.322853 | 0.629563 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.334462 | 0.0844655 | 0.0611305 | 0.161908 | 0.331472 | 0.346799 | 0.359856 | 0.451417 | 0.738717 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.415332 | 0.142841 | 0.0919432 | 0.275894 | 0.343459 | 0.358574 | 0.432921 | 0.742386 | 0.893196 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.263416 | 0.0772504 | 0.038668 | 0.0900059 | 0.267771 | 0.292927 | 0.305178 | 0.319511 | 0.670544 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.33985 | 0.0711073 | 0.0537607 | 0.169114 | 0.336752 | 0.348052 | 0.357973 | 0.418161 | 0.719769 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.396733 | 0.122051 | 0.162882 | 0.318624 | 0.343725 | 0.356264 | 0.376366 | 0.720563 | 0.904321 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.254706 | 0.0819032 | 0.0349499 | 0.0830499 | 0.212309 | 0.290119 | 0.303078 | 0.321786 | 0.662272 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.340655 | 0.078156 | 0.0709195 | 0.170085 | 0.335304 | 0.3489 | 0.360087 | 0.454573 | 0.709218 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.404639 | 0.129838 | 0.0661785 | 0.294264 | 0.343825 | 0.357654 | 0.391646 | 0.734805 | 0.894131 |
| tossup_hazard | hazard_r_1 | 1240 | 0.367405 | 0.300985 | 0.0176302 | 0.0431396 | 0.0995396 | 0.245065 | 0.609268 | 0.909272 | 0.958569 |
| tossup_hazard | hazard_r_2 | 1240 | 0.279993 | 0.25605 | 0.0195776 | 0.0365242 | 0.0780064 | 0.164509 | 0.455639 | 0.806574 | 0.918849 |
| tossup_hazard | hazard_r_3 | 1240 | 0.352602 | 0.2932 | 0.0185723 | 0.0394936 | 0.0945183 | 0.231719 | 0.621151 | 0.86411 | 0.961137 |
