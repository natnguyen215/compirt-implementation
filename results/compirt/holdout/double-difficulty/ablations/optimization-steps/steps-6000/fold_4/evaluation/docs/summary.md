# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/optimization-steps/steps-6000/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/optimization-steps/steps-6000/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 6000 |
| pyramidal | final_loss | 277511 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.725409 |
| log_loss | 0.475582 |
| ece | 0.00982917 |
| brier | 0.153641 |
| accuracy | 0.786516 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0131607 |
| probability_std | 0.146415 |
| probability_p10 | 0.569671 |
| probability_p50 | 0.809007 |
| probability_p90 | 0.919779 |
| mean_predictive_variance | 0.154673 |
| integrated_brier_score | 0.0964467 |
| joint_tossup_event_log_loss | 6.50353 |
| buzz_position_mae | 0.143001 |
| buzz_position_median_absolute_error | 0.123169 |
| buzz_position_bias | -0.0240573 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.363107 |
| first_buzzer_mean_reciprocal_rank | 0.572075 |
| first_buzzer_log_loss | 1.66163 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.725409 |
| neg_average_precision | 0.453115 |
| neg_precision | 0.607018 |
| neg_recall | 0.164683 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.180432 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0110406 |
| no_buzz_calibration_error | -0.00068652 |
| no_buzz_brier | 0.011107 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.725409 | 0.475582 | 0.00982917 | 0.153641 | 0.786516 | 0.773355 | 0.0131607 | 0.146415 | 0.569671 | 0.809007 | 0.919779 | 0.154673 |
| tossup_correctness | tier | fall | 2876 | 0.733139 | 0.450125 | 0.0151019 | 0.143553 | 0.802156 | 0.793115 | 0.00904033 | 0.141535 | 0.578824 | 0.817752 | 0.925841 | 0.150741 |
| tossup_correctness | tier | nationals | 1579 | 0.713901 | 0.527375 | 0.0328081 | 0.174325 | 0.753008 | 0.729576 | 0.0234326 | 0.159697 | 0.546825 | 0.806046 | 0.914437 | 0.156391 |
| tossup_correctness | tier | regionals | 1990 | 0.736147 | 0.479358 | 0.0168094 | 0.155802 | 0.780905 | 0.765829 | 0.0150754 | 0.147243 | 0.558979 | 0.798783 | 0.915856 | 0.158647 |
| tossup_correctness | tier | winter | 2825 | 0.715048 | 0.469888 | 0.016278 | 0.150829 | 0.793274 | 0.783009 | 0.0102655 | 0.142187 | 0.582634 | 0.809369 | 0.918365 | 0.154918 |
| tossup_correctness | category | Current Events | 123 | 0.801174 | 0.44671 | 0.0669279 | 0.144082 | 0.788618 | 0.764228 | 0.0243902 | 0.137078 | 0.573217 | 0.745397 | 0.912098 | 0.171552 |
| tossup_correctness | category | Fine Arts | 1093 | 0.744262 | 0.465905 | 0.0157326 | 0.149412 | 0.797804 | 0.769442 | 0.0283623 | 0.149304 | 0.569572 | 0.821133 | 0.92457 | 0.15124 |
| tossup_correctness | category | Geography | 191 | 0.791602 | 0.485421 | 0.0640935 | 0.15707 | 0.78534 | 0.691099 | 0.0942408 | 0.206917 | 0.383176 | 0.763797 | 0.899317 | 0.168352 |
| tossup_correctness | category | History | 1469 | 0.713617 | 0.502228 | 0.0309516 | 0.165252 | 0.765827 | 0.758339 | 0.00748809 | 0.146098 | 0.562199 | 0.804498 | 0.921165 | 0.155903 |
| tossup_correctness | category | Literature | 1436 | 0.707626 | 0.435648 | 0.0135151 | 0.136593 | 0.816852 | 0.81546 | 0.00139276 | 0.123665 | 0.648791 | 0.844166 | 0.930134 | 0.138602 |
| tossup_correctness | category | Mythology | 325 | 0.667096 | 0.420961 | 0.0669774 | 0.1305 | 0.843077 | 0.843077 | 0 | 0.10521 | 0.660348 | 0.816258 | 0.911068 | 0.149861 |
| tossup_correctness | category | Other Academic | 67 | 0.685984 | 0.494231 | 0.0556699 | 0.160462 | 0.776119 | 0.791045 | -0.0149254 | 0.14077 | 0.544817 | 0.779747 | 0.90039 | 0.168729 |
| tossup_correctness | category | Philosophy | 322 | 0.691528 | 0.484647 | 0.027998 | 0.158222 | 0.773292 | 0.785714 | -0.0124224 | 0.12903 | 0.603983 | 0.806962 | 0.931821 | 0.152006 |
| tossup_correctness | category | Popular Culture | 100 | 0.546476 | 0.363063 | 0.0572428 | 0.105174 | 0.89 | 0.89 | 0 | 0.0717239 | 0.755252 | 0.849576 | 0.922036 | 0.127018 |
| tossup_correctness | category | Religion | 365 | 0.666067 | 0.558961 | 0.0654956 | 0.18672 | 0.723288 | 0.723288 | 0 | 0.15094 | 0.537545 | 0.786467 | 0.914405 | 0.163168 |
| tossup_correctness | category | Science | 1456 | 0.721551 | 0.48261 | 0.01551 | 0.156196 | 0.783654 | 0.76717 | 0.0164835 | 0.150547 | 0.552646 | 0.796835 | 0.909636 | 0.161124 |
| tossup_correctness | category | Social Science | 333 | 0.751257 | 0.496903 | 0.0407482 | 0.16239 | 0.753754 | 0.72973 | 0.024024 | 0.173464 | 0.467902 | 0.777454 | 0.911939 | 0.167232 |
| tossup_correctness | category | Unknown | 1990 | 0.736147 | 0.479358 | 0.0168094 | 0.155802 | 0.780905 | 0.765829 | 0.0150754 | 0.147243 | 0.558979 | 0.798783 | 0.915856 | 0.158647 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.768988 | 0.485391 | 0.0761893 | 0.159293 | 0.75419 | 0.748603 | 0.00558659 | 0.158481 | 0.514339 | 0.761238 | 0.88801 | 0.175052 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.70732 | 0.499881 | 0.0112512 | 0.162996 | 0.77116 | 0.754441 | 0.0167189 | 0.145502 | 0.544279 | 0.783883 | 0.903629 | 0.165381 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.727615 | 0.481926 | 0.0226407 | 0.156428 | 0.783931 | 0.766682 | 0.0172492 | 0.144255 | 0.581175 | 0.806555 | 0.918919 | 0.155227 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.714165 | 0.463485 | 0.00963046 | 0.148134 | 0.801209 | 0.787441 | 0.0137676 | 0.13618 | 0.608548 | 0.820299 | 0.921644 | 0.149566 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.735114 | 0.474578 | 0.0150876 | 0.153742 | 0.780562 | 0.771758 | 0.00880461 | 0.155501 | 0.534601 | 0.811495 | 0.922968 | 0.154706 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 1.93112 | 0.762743 | -0.386044 | 0.683643 | 1.41378 | 1.93038 | 2.4238 | 3.27727 | 3.97558 |
| player | theta_1 | 1196 | -0.777204 | 0.899491 | -3.62731 | -2.08603 | -1.36361 | -0.884644 | -0.278574 | 0.858828 | 3.16084 |
| player | theta_2 | 1196 | -0.666757 | 0.801619 | -2.81229 | -1.92432 | -1.19767 | -0.731299 | -0.194746 | 0.757875 | 2.18992 |
| player | theta_3 | 1196 | -0.772989 | 0.837695 | -3.04378 | -2.08234 | -1.3002 | -0.865209 | -0.27189 | 0.741955 | 2.4891 |
| player | theta_norm | 1196 | 1.84931 | 0.614887 | 0.25147 | 0.901935 | 1.42054 | 1.79947 | 2.25292 | 2.96041 | 4.12187 |
| tossup | start_difficulty_d1 | 1240 | -1.34037 | 0.535938 | -2.97775 | -2.09186 | -1.69597 | -1.37636 | -1.04466 | -0.437597 | 1.84036 |
| tossup | start_difficulty_d2 | 1240 | -1.34107 | 0.492536 | -3.22526 | -2.06273 | -1.67117 | -1.36452 | -1.03521 | -0.518985 | 0.79286 |
| tossup | start_difficulty_d3 | 1240 | -1.34246 | 0.500035 | -3.15845 | -2.11455 | -1.67483 | -1.37305 | -1.04421 | -0.521717 | 1.24294 |
| tossup | end_difficulty_d1 | 1240 | -2.33287 | 0.624932 | -4.14561 | -3.22183 | -2.74912 | -2.37147 | -1.97677 | -1.31243 | 1.14983 |
| tossup | end_difficulty_d2 | 1240 | -2.33255 | 0.577192 | -4.4977 | -3.20144 | -2.71576 | -2.35313 | -1.98537 | -1.38134 | -0.0662338 |
| tossup | end_difficulty_d3 | 1240 | -2.33729 | 0.584875 | -4.48113 | -3.24006 | -2.72614 | -2.35175 | -1.97118 | -1.38434 | 0.548229 |
| tossup | total_drop_d1 | 1240 | 0.992504 | 0.110538 | 0.593631 | 0.811633 | 0.924785 | 0.990542 | 1.06515 | 1.17148 | 1.43118 |
| tossup | total_drop_d2 | 1240 | 0.991479 | 0.102212 | 0.621794 | 0.824377 | 0.926192 | 0.991209 | 1.05688 | 1.16192 | 1.3597 |
| tossup | total_drop_d3 | 1240 | 0.994837 | 0.116358 | 0.619458 | 0.821211 | 0.922606 | 0.99204 | 1.06183 | 1.16116 | 2.66221 |
| tossup | drop_share_1_d1 | 1240 | 0.30356 | 0.0150963 | 0.2263 | 0.279341 | 0.294609 | 0.303999 | 0.313725 | 0.32719 | 0.343564 |
| tossup | drop_share_2_d1 | 1240 | 0.34745 | 0.0112343 | 0.314064 | 0.329647 | 0.34018 | 0.347185 | 0.354812 | 0.366374 | 0.385172 |
| tossup | drop_share_3_d1 | 1240 | 0.34899 | 0.0162081 | 0.296566 | 0.324621 | 0.338563 | 0.347953 | 0.358029 | 0.376207 | 0.434143 |
| tossup | drop_share_1_d2 | 1240 | 0.304248 | 0.0146816 | 0.240403 | 0.27948 | 0.295514 | 0.304869 | 0.313264 | 0.32799 | 0.355827 |
| tossup | drop_share_2_d2 | 1240 | 0.346968 | 0.0111675 | 0.31007 | 0.329015 | 0.339588 | 0.346977 | 0.353764 | 0.365707 | 0.38209 |
| tossup | drop_share_3_d2 | 1240 | 0.348784 | 0.015728 | 0.297786 | 0.324176 | 0.338791 | 0.347804 | 0.35859 | 0.376399 | 0.408787 |
| tossup | drop_share_1_d3 | 1240 | 0.303404 | 0.0148361 | 0.17862 | 0.280636 | 0.293925 | 0.303989 | 0.312858 | 0.326764 | 0.350845 |
| tossup | drop_share_2_d3 | 1240 | 0.347282 | 0.0115482 | 0.314289 | 0.329687 | 0.339096 | 0.347321 | 0.354332 | 0.365288 | 0.475789 |
| tossup | drop_share_3_d3 | 1240 | 0.349314 | 0.0152105 | 0.299822 | 0.325858 | 0.339102 | 0.348748 | 0.358742 | 0.373068 | 0.42717 |
| tossup | r_1 | 1240 | 0.319058 | 0.162233 | 0.0421218 | 0.108381 | 0.193896 | 0.287732 | 0.420322 | 0.634269 | 0.884634 |
| tossup | r_2 | 1240 | 0.340262 | 0.159375 | 0.0587565 | 0.12386 | 0.218923 | 0.315636 | 0.444928 | 0.646691 | 0.839205 |
| tossup | r_3 | 1240 | 0.34068 | 0.15983 | 0.0566098 | 0.131455 | 0.221766 | 0.310962 | 0.442437 | 0.655125 | 0.875873 |
| tossup | r_norm | 1240 | 0.638489 | 0.0563635 | 0.57743 | 0.580504 | 0.596599 | 0.621967 | 0.661987 | 0.75133 | 0.888388 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 6.16123 | 0.514843 | 4.18353 | 5.33315 | 5.95683 | 6.11722 | 6.3341 | 7.18052 | 8.07104 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 6.21028 | 0.488886 | 3.18623 | 5.56139 | 6.02147 | 6.14653 | 6.35928 | 7.09716 | 8.69175 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 6.20003 | 0.515885 | 2.87276 | 5.43104 | 6.00477 | 6.15338 | 6.38252 | 7.20398 | 8.49035 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 3.04661 | 3.02005 | -13.6151 | -3.13831 | 1.21082 | 4.86889 | 5.10848 | 5.38866 | 6.08487 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 3.58044 | 2.99582 | -11.242 | -3.26379 | 3.40293 | 5.01814 | 5.17853 | 5.4829 | 6.31014 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 3.47099 | 2.77852 | -17.4828 | -1.77835 | 1.79704 | 4.98373 | 5.18118 | 5.51078 | 6.60953 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.11462 | 3.14126 | 0.843914 | 0.960321 | 1.01538 | 1.08853 | 5.16689 | 9.34214 | 20.3045 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.62984 | 3.13564 | 0.863998 | 0.946269 | 0.995882 | 1.04179 | 2.49099 | 9.60831 | 17.669 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.72903 | 2.89146 | 0.844728 | 0.942653 | 0.998627 | 1.04991 | 4.64811 | 8.44567 | 23.7343 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.25074 | 0.0883099 | 0.0451908 | 0.0841084 | 0.18701 | 0.28961 | 0.303778 | 0.323607 | 0.697938 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.336199 | 0.0849958 | 0.0569776 | 0.158213 | 0.332271 | 0.347136 | 0.360053 | 0.462201 | 0.719681 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.413061 | 0.140882 | 0.11257 | 0.270369 | 0.343573 | 0.357352 | 0.423648 | 0.742777 | 0.896554 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.260676 | 0.0814495 | 0.0350619 | 0.0868939 | 0.255898 | 0.292468 | 0.304064 | 0.320301 | 0.727919 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.340126 | 0.0747436 | 0.0603716 | 0.185206 | 0.335707 | 0.347867 | 0.358403 | 0.445381 | 0.70371 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.399198 | 0.125327 | 0.0853681 | 0.312072 | 0.344008 | 0.356484 | 0.379672 | 0.711458 | 0.893213 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.256803 | 0.0817044 | 0.0329829 | 0.0856251 | 0.221739 | 0.290819 | 0.304265 | 0.323113 | 0.657109 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.339333 | 0.0769766 | 0.0634633 | 0.172 | 0.335809 | 0.349077 | 0.359758 | 0.448174 | 0.73189 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.403865 | 0.132366 | 0.0695009 | 0.300104 | 0.34399 | 0.35633 | 0.38793 | 0.736594 | 0.903554 |
| tossup_hazard | hazard_r_1 | 1240 | 0.36305 | 0.302088 | 0.0193618 | 0.0417151 | 0.094911 | 0.240273 | 0.625964 | 0.896226 | 0.961647 |
| tossup_hazard | hazard_r_2 | 1240 | 0.298216 | 0.267106 | 0.0155301 | 0.0364895 | 0.0798557 | 0.177691 | 0.484348 | 0.851118 | 0.945405 |
| tossup_hazard | hazard_r_3 | 1240 | 0.338734 | 0.294471 | 0.0124737 | 0.0353919 | 0.0790918 | 0.20699 | 0.622078 | 0.8584 | 0.951095 |
