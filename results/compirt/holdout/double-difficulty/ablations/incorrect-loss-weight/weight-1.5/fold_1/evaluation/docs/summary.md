# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-1.5/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-1.5/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 288891 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.709817 |
| log_loss | 0.50685 |
| ece | 0.0595295 |
| brier | 0.165882 |
| accuracy | 0.765754 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00362917 |
| probability_std | 0.175148 |
| probability_p10 | 0.451131 |
| probability_p50 | 0.744316 |
| probability_p90 | 0.89757 |
| mean_predictive_variance | 0.176985 |
| integrated_brier_score | 0.100796 |
| joint_tossup_event_log_loss | 6.61288 |
| buzz_position_mae | 0.151258 |
| buzz_position_median_absolute_error | 0.133607 |
| buzz_position_bias | -0.0478597 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.34961 |
| first_buzzer_mean_reciprocal_rank | 0.563586 |
| first_buzzer_log_loss | 1.67955 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.709817 |
| neg_average_precision | 0.445967 |
| neg_precision | 0.513274 |
| neg_recall | 0.294961 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.190406 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.015123 |
| no_buzz_calibration_error | -0.000786131 |
| no_buzz_brier | 0.0154591 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.709817 | 0.50685 | 0.0595295 | 0.165882 | 0.765754 | 0.762125 | 0.00362917 | 0.175148 | 0.451131 | 0.744316 | 0.89757 | 0.176985 |
| tossup_correctness | tier | fall | 2842 | 0.727957 | 0.476501 | 0.0619696 | 0.15387 | 0.785362 | 0.785362 | 0 | 0.172925 | 0.46995 | 0.766448 | 0.912917 | 0.170193 |
| tossup_correctness | tier | nationals | 1564 | 0.715156 | 0.536636 | 0.0398234 | 0.178317 | 0.73913 | 0.718031 | 0.0210997 | 0.177583 | 0.426356 | 0.724251 | 0.885721 | 0.18389 |
| tossup_correctness | tier | regionals | 1937 | 0.686865 | 0.523434 | 0.0621666 | 0.172268 | 0.757873 | 0.758389 | -0.000516262 | 0.169496 | 0.451842 | 0.736565 | 0.889579 | 0.180782 |
| tossup_correctness | tier | winter | 2750 | 0.70003 | 0.509594 | 0.0677087 | 0.166726 | 0.766182 | 0.765818 | 0.000363636 | 0.178288 | 0.444719 | 0.745013 | 0.896004 | 0.177405 |
| tossup_correctness | category | Current Events | 126 | 0.719517 | 0.517 | 0.119414 | 0.170507 | 0.746032 | 0.769841 | -0.0238095 | 0.16236 | 0.417124 | 0.678817 | 0.857988 | 0.196373 |
| tossup_correctness | category | Fine Arts | 1071 | 0.749452 | 0.481502 | 0.0673684 | 0.156217 | 0.782446 | 0.766573 | 0.015873 | 0.186406 | 0.421848 | 0.74296 | 0.902077 | 0.17557 |
| tossup_correctness | category | Geography | 185 | 0.792774 | 0.520991 | 0.114087 | 0.170946 | 0.756757 | 0.697297 | 0.0594595 | 0.230204 | 0.252653 | 0.660979 | 0.862472 | 0.185142 |
| tossup_correctness | category | History | 1440 | 0.707458 | 0.515799 | 0.0489481 | 0.1703 | 0.749306 | 0.754167 | -0.00486111 | 0.17515 | 0.455363 | 0.74946 | 0.907518 | 0.174634 |
| tossup_correctness | category | Literature | 1422 | 0.6782 | 0.468112 | 0.0734285 | 0.149356 | 0.798172 | 0.814346 | -0.0161744 | 0.155452 | 0.524429 | 0.784521 | 0.913113 | 0.165348 |
| tossup_correctness | category | Mythology | 318 | 0.665814 | 0.493664 | 0.0864328 | 0.157364 | 0.792453 | 0.789308 | 0.00314465 | 0.157117 | 0.537209 | 0.7727 | 0.908184 | 0.168841 |
| tossup_correctness | category | Other Academic | 66 | 0.81299 | 0.500371 | 0.162526 | 0.164343 | 0.772727 | 0.712121 | 0.0606061 | 0.165151 | 0.447474 | 0.727237 | 0.869311 | 0.185504 |
| tossup_correctness | category | Philosophy | 311 | 0.721846 | 0.508549 | 0.0531433 | 0.168955 | 0.762058 | 0.745981 | 0.0160772 | 0.163434 | 0.48061 | 0.751132 | 0.891252 | 0.178345 |
| tossup_correctness | category | Popular Culture | 102 | 0.533333 | 0.404488 | 0.105753 | 0.117931 | 0.872549 | 0.882353 | -0.00980392 | 0.0980465 | 0.650925 | 0.810824 | 0.887281 | 0.15804 |
| tossup_correctness | category | Religion | 358 | 0.714182 | 0.54697 | 0.062373 | 0.182428 | 0.74581 | 0.712291 | 0.0335196 | 0.185901 | 0.3799 | 0.713298 | 0.864668 | 0.190352 |
| tossup_correctness | category | Science | 1433 | 0.696106 | 0.532861 | 0.0483852 | 0.176969 | 0.741103 | 0.738311 | 0.00279135 | 0.177988 | 0.432303 | 0.730691 | 0.892609 | 0.181272 |
| tossup_correctness | category | Social Science | 324 | 0.778214 | 0.495206 | 0.0744144 | 0.161362 | 0.774691 | 0.731481 | 0.0432099 | 0.183936 | 0.388664 | 0.717682 | 0.871883 | 0.185486 |
| tossup_correctness | category | Unknown | 1937 | 0.686865 | 0.523434 | 0.0621666 | 0.172268 | 0.757873 | 0.758389 | -0.000516262 | 0.169496 | 0.451842 | 0.736565 | 0.889579 | 0.180782 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.619048 | 0.611954 | 0.09184 | 0.208042 | 0.664671 | 0.712575 | -0.0479042 | 0.167825 | 0.426474 | 0.703466 | 0.868856 | 0.192402 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.723235 | 0.529628 | 0.0554502 | 0.176552 | 0.748904 | 0.729167 | 0.0197368 | 0.188801 | 0.395399 | 0.711777 | 0.886268 | 0.183965 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.712891 | 0.506749 | 0.0464387 | 0.165651 | 0.767376 | 0.755083 | 0.0122931 | 0.167885 | 0.476474 | 0.748388 | 0.898779 | 0.176004 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.693008 | 0.49449 | 0.0611699 | 0.160139 | 0.77602 | 0.780942 | -0.00492264 | 0.160394 | 0.494835 | 0.758507 | 0.899823 | 0.173945 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.720289 | 0.505882 | 0.0688355 | 0.165898 | 0.76563 | 0.762029 | 0.00360065 | 0.186543 | 0.408721 | 0.736282 | 0.901313 | 0.177568 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 2.68134 | 0.760805 | 0.45761 | 1.47761 | 2.16811 | 2.67563 | 3.19143 | 3.97444 | 4.64738 |
| player | theta_1 | 1167 | -1.23886 | 0.870059 | -3.65755 | -2.60193 | -1.79453 | -1.32322 | -0.731825 | 0.279165 | 1.7543 |
| player | theta_2 | 1167 | -1.03591 | 0.730769 | -3.58337 | -2.17188 | -1.48166 | -1.075 | -0.628467 | 0.249398 | 1.94736 |
| player | theta_3 | 1167 | -1.07607 | 0.789788 | -3.54638 | -2.32182 | -1.58166 | -1.11386 | -0.61429 | 0.365638 | 1.93657 |
| player | theta_norm | 1167 | 2.28882 | 0.663818 | 0.396637 | 1.2796 | 1.8221 | 2.24616 | 2.69873 | 3.47536 | 4.44339 |
| tossup | start_difficulty_d1 | 1220 | -1.40572 | 0.603136 | -3.29086 | -2.29631 | -1.81396 | -1.44667 | -1.05847 | -0.416052 | 1.66996 |
| tossup | start_difficulty_d2 | 1220 | -1.39048 | 0.561744 | -3.34865 | -2.23477 | -1.77511 | -1.42035 | -1.03275 | -0.397341 | 0.727583 |
| tossup | start_difficulty_d3 | 1220 | -1.38893 | 0.556063 | -3.52263 | -2.24225 | -1.78689 | -1.40023 | -1.03551 | -0.431967 | 0.661134 |
| tossup | end_difficulty_d1 | 1220 | -2.39656 | 0.703247 | -4.7398 | -3.45453 | -2.87242 | -2.42977 | -1.97451 | -1.28603 | 1.00903 |
| tossup | end_difficulty_d2 | 1220 | -2.37767 | 0.656647 | -4.87702 | -3.39463 | -2.82118 | -2.39962 | -1.96844 | -1.24469 | 0.0124534 |
| tossup | end_difficulty_d3 | 1220 | -2.37319 | 0.648255 | -4.87689 | -3.39974 | -2.82432 | -2.37229 | -1.96033 | -1.27708 | -0.0347347 |
| tossup | total_drop_d1 | 1220 | 0.990846 | 0.130099 | 0.60496 | 0.778799 | 0.903139 | 0.989251 | 1.07069 | 1.20204 | 1.5628 |
| tossup | total_drop_d2 | 1220 | 0.987185 | 0.117725 | 0.638377 | 0.806012 | 0.911673 | 0.984024 | 1.05537 | 1.18644 | 1.52837 |
| tossup | total_drop_d3 | 1220 | 0.984258 | 0.115274 | 0.663881 | 0.805133 | 0.906891 | 0.981114 | 1.05753 | 1.1843 | 1.42725 |
| tossup | drop_share_1_d1 | 1220 | 0.303245 | 0.0176964 | 0.189392 | 0.275059 | 0.292788 | 0.304106 | 0.314872 | 0.329182 | 0.365229 |
| tossup | drop_share_2_d1 | 1220 | 0.34718 | 0.011812 | 0.31212 | 0.327114 | 0.339517 | 0.347255 | 0.355256 | 0.366237 | 0.387679 |
| tossup | drop_share_3_d1 | 1220 | 0.349575 | 0.0187258 | 0.292875 | 0.320828 | 0.337343 | 0.349061 | 0.360502 | 0.380156 | 0.475754 |
| tossup | drop_share_1_d2 | 1220 | 0.302855 | 0.0159197 | 0.23007 | 0.276041 | 0.293036 | 0.303588 | 0.313047 | 0.328059 | 0.359235 |
| tossup | drop_share_2_d2 | 1220 | 0.34686 | 0.0118382 | 0.310375 | 0.327647 | 0.338924 | 0.346672 | 0.354737 | 0.365861 | 0.403297 |
| tossup | drop_share_3_d2 | 1220 | 0.350285 | 0.0170979 | 0.286846 | 0.324303 | 0.339046 | 0.350355 | 0.360585 | 0.377665 | 0.433766 |
| tossup | drop_share_1_d3 | 1220 | 0.302809 | 0.0163874 | 0.225962 | 0.27615 | 0.293086 | 0.30347 | 0.313512 | 0.328698 | 0.367937 |
| tossup | drop_share_2_d3 | 1220 | 0.347088 | 0.0114913 | 0.308873 | 0.32809 | 0.339604 | 0.347075 | 0.35454 | 0.366235 | 0.386937 |
| tossup | drop_share_3_d3 | 1220 | 0.350102 | 0.017352 | 0.300942 | 0.323566 | 0.33868 | 0.349245 | 0.360265 | 0.379732 | 0.427442 |
| tossup | r_1 | 1220 | 0.333207 | 0.174617 | 0.0531998 | 0.110395 | 0.19077 | 0.293937 | 0.454779 | 0.665484 | 0.864106 |
| tossup | r_2 | 1220 | 0.331927 | 0.147602 | 0.0490228 | 0.123818 | 0.222745 | 0.313681 | 0.419125 | 0.625791 | 0.858046 |
| tossup | r_3 | 1220 | 0.334866 | 0.150198 | 0.0695191 | 0.127957 | 0.221266 | 0.313644 | 0.426403 | 0.625741 | 0.839712 |
| tossup | r_norm | 1220 | 0.636439 | 0.0553228 | 0.577378 | 0.580729 | 0.594851 | 0.619618 | 0.660333 | 0.758035 | 0.869456 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 4.50056 | 0.483351 | 1.82878 | 3.80902 | 4.21913 | 4.44475 | 4.74703 | 5.39205 | 6.39387 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 4.44233 | 0.430901 | 1.92958 | 3.78168 | 4.20846 | 4.42063 | 4.64477 | 5.19038 | 6.58658 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 4.4541 | 0.420912 | 2.16633 | 3.79359 | 4.2269 | 4.44763 | 4.67989 | 5.16999 | 6.0221 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | 1.7071 | 2.33108 | -11.159 | -3.32768 | 0.646797 | 2.81522 | 3.28718 | 3.64968 | 4.35846 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | 2.18192 | 2.12229 | -9.63796 | -2.57476 | 2.17676 | 3.09171 | 3.36753 | 3.71255 | 4.05004 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | 2.25415 | 2.15497 | -9.49391 | -2.90898 | 2.32873 | 3.16654 | 3.41113 | 3.74143 | 4.46482 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 2.79345 | 2.50191 | 0.907754 | 0.983464 | 1.05905 | 1.39675 | 4.01609 | 8.14675 | 15.7325 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 2.26041 | 2.26856 | 0.901458 | 0.96236 | 1.02723 | 1.19144 | 2.02772 | 7.40204 | 14.2956 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 2.19995 | 2.27553 | 0.869628 | 0.968651 | 1.02352 | 1.1596 | 1.8313 | 7.52179 | 14.0585 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.232757 | 0.0802544 | 0.0430875 | 0.0819064 | 0.172223 | 0.265955 | 0.294447 | 0.314929 | 0.52952 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.34258 | 0.0760714 | 0.0570489 | 0.175855 | 0.335278 | 0.351079 | 0.366578 | 0.442601 | 0.674995 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.424663 | 0.130189 | 0.112545 | 0.310239 | 0.348645 | 0.371696 | 0.452957 | 0.730246 | 0.899864 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.251069 | 0.0709686 | 0.0315952 | 0.0907768 | 0.231608 | 0.278702 | 0.29607 | 0.313849 | 0.534593 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.34794 | 0.0646334 | 0.0657114 | 0.218402 | 0.340325 | 0.351248 | 0.36488 | 0.419412 | 0.707594 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.400991 | 0.109774 | 0.0944533 | 0.316999 | 0.35036 | 0.364633 | 0.401015 | 0.672427 | 0.887998 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.253294 | 0.0683183 | 0.0394119 | 0.0934576 | 0.235744 | 0.278169 | 0.296419 | 0.313684 | 0.574761 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.350429 | 0.0571529 | 0.0828757 | 0.252091 | 0.340555 | 0.351466 | 0.364291 | 0.416424 | 0.681032 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.396277 | 0.10006 | 0.0722568 | 0.321002 | 0.34987 | 0.367209 | 0.396853 | 0.635115 | 0.869248 |
| tossup_hazard | hazard_r_1 | 1220 | 0.394609 | 0.279059 | 0.0315995 | 0.0604662 | 0.130185 | 0.325526 | 0.651435 | 0.870904 | 0.941009 |
| tossup_hazard | hazard_r_2 | 1220 | 0.301948 | 0.225758 | 0.0229017 | 0.0537921 | 0.11735 | 0.220504 | 0.464559 | 0.748835 | 0.875504 |
| tossup_hazard | hazard_r_3 | 1220 | 0.303442 | 0.22484 | 0.0227791 | 0.0509089 | 0.1238 | 0.232109 | 0.452888 | 0.757275 | 0.919568 |
