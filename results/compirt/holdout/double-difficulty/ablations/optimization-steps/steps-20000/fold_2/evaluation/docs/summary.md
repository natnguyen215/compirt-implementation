# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/optimization-steps/steps-20000/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/optimization-steps/steps-20000/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 20000 |
| pyramidal | final_loss | 275924 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.711248 |
| log_loss | 0.492184 |
| ece | 0.0119162 |
| brier | 0.159794 |
| accuracy | 0.774225 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0100465 |
| probability_std | 0.147787 |
| probability_p10 | 0.563292 |
| probability_p50 | 0.804525 |
| probability_p90 | 0.919099 |
| mean_predictive_variance | 0.156274 |
| integrated_brier_score | 0.0954624 |
| joint_tossup_event_log_loss | 6.45691 |
| buzz_position_mae | 0.139837 |
| buzz_position_median_absolute_error | 0.11782 |
| buzz_position_bias | -0.00254644 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.368586 |
| first_buzzer_mean_reciprocal_rank | 0.580313 |
| first_buzzer_log_loss | 1.62822 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.711248 |
| neg_average_precision | 0.451877 |
| neg_precision | 0.57976 |
| neg_recall | 0.154833 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.182861 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0083959 |
| no_buzz_calibration_error | -0.00471711 |
| no_buzz_brier | 0.0124044 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.711248 | 0.492184 | 0.0119162 | 0.159794 | 0.774225 | 0.764178 | 0.0100465 | 0.147787 | 0.563292 | 0.804525 | 0.919099 | 0.156274 |
| tossup_correctness | tier | fall | 2798 | 0.735102 | 0.458668 | 0.0198342 | 0.146622 | 0.794496 | 0.785204 | 0.00929235 | 0.144133 | 0.567376 | 0.811829 | 0.92011 | 0.15395 |
| tossup_correctness | tier | nationals | 1545 | 0.71367 | 0.53405 | 0.0383459 | 0.177339 | 0.743689 | 0.721036 | 0.0226537 | 0.158516 | 0.544524 | 0.793354 | 0.915975 | 0.160315 |
| tossup_correctness | tier | regionals | 2039 | 0.698874 | 0.500177 | 0.0193844 | 0.162579 | 0.769985 | 0.762138 | 0.00784698 | 0.146103 | 0.557799 | 0.797064 | 0.922013 | 0.15865 |
| tossup_correctness | tier | winter | 2875 | 0.694195 | 0.496635 | 0.0156006 | 0.16121 | 0.773913 | 0.768348 | 0.00556522 | 0.14593 | 0.577539 | 0.808213 | 0.917715 | 0.15468 |
| tossup_correctness | category | Current Events | 129 | 0.682261 | 0.612258 | 0.0808337 | 0.208002 | 0.689922 | 0.666667 | 0.0232558 | 0.160001 | 0.521091 | 0.775329 | 0.930821 | 0.163143 |
| tossup_correctness | category | Fine Arts | 1074 | 0.711216 | 0.477103 | 0.0283655 | 0.153245 | 0.791434 | 0.776536 | 0.0148976 | 0.156433 | 0.551962 | 0.792005 | 0.91655 | 0.159581 |
| tossup_correctness | category | Geography | 180 | 0.761588 | 0.562606 | 0.0809685 | 0.189925 | 0.733333 | 0.616667 | 0.116667 | 0.235407 | 0.245498 | 0.773705 | 0.907311 | 0.161736 |
| tossup_correctness | category | History | 1454 | 0.688351 | 0.512605 | 0.0219264 | 0.167605 | 0.763411 | 0.757909 | 0.00550206 | 0.14559 | 0.55558 | 0.80852 | 0.92054 | 0.155559 |
| tossup_correctness | category | Literature | 1435 | 0.725137 | 0.433313 | 0.0184585 | 0.135401 | 0.820209 | 0.810453 | 0.0097561 | 0.128344 | 0.622165 | 0.838066 | 0.929998 | 0.14075 |
| tossup_correctness | category | Mythology | 324 | 0.70248 | 0.468775 | 0.0434639 | 0.149986 | 0.780864 | 0.79321 | -0.0123457 | 0.116357 | 0.652453 | 0.828319 | 0.919616 | 0.14552 |
| tossup_correctness | category | Other Academic | 71 | 0.660131 | 0.533848 | 0.118843 | 0.173632 | 0.760563 | 0.760563 | 0 | 0.118652 | 0.583616 | 0.7977 | 0.905706 | 0.162494 |
| tossup_correctness | category | Philosophy | 310 | 0.713754 | 0.493984 | 0.0336948 | 0.16157 | 0.774194 | 0.76129 | 0.0129032 | 0.123777 | 0.608302 | 0.800575 | 0.91434 | 0.158879 |
| tossup_correctness | category | Popular Culture | 108 | 0.517361 | 0.377187 | 0.0877627 | 0.108518 | 0.87963 | 0.888889 | -0.00925926 | 0.0837319 | 0.725951 | 0.847776 | 0.914823 | 0.135184 |
| tossup_correctness | category | Religion | 361 | 0.694551 | 0.525506 | 0.0333211 | 0.173357 | 0.750693 | 0.742382 | 0.00831025 | 0.149636 | 0.499331 | 0.760989 | 0.893531 | 0.175547 |
| tossup_correctness | category | Science | 1445 | 0.71763 | 0.507762 | 0.0315846 | 0.167564 | 0.752249 | 0.746021 | 0.00622837 | 0.144202 | 0.567248 | 0.794529 | 0.91187 | 0.161022 |
| tossup_correctness | category | Social Science | 327 | 0.746438 | 0.51809 | 0.0428415 | 0.173309 | 0.730887 | 0.718654 | 0.0122324 | 0.176063 | 0.47416 | 0.765177 | 0.912738 | 0.16773 |
| tossup_correctness | category | Unknown | 2039 | 0.698874 | 0.500177 | 0.0193844 | 0.162579 | 0.769985 | 0.762138 | 0.00784698 | 0.146103 | 0.557799 | 0.797064 | 0.922013 | 0.15865 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.677253 | 0.53236 | 0.067226 | 0.177905 | 0.73224 | 0.743169 | -0.010929 | 0.157402 | 0.49006 | 0.766379 | 0.904517 | 0.171972 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.722429 | 0.522332 | 0.0234421 | 0.172231 | 0.747644 | 0.728796 | 0.0188482 | 0.15366 | 0.531789 | 0.785694 | 0.908423 | 0.16472 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.719987 | 0.497525 | 0.0205099 | 0.162403 | 0.76954 | 0.752568 | 0.0169719 | 0.146853 | 0.571664 | 0.807325 | 0.917792 | 0.155482 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.701864 | 0.473522 | 0.0106071 | 0.152334 | 0.789565 | 0.786087 | 0.00347826 | 0.135463 | 0.605001 | 0.820183 | 0.923092 | 0.149678 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.709156 | 0.494031 | 0.025409 | 0.159932 | 0.774043 | 0.764393 | 0.00965058 | 0.154948 | 0.543985 | 0.795143 | 0.919159 | 0.159535 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 0.79333 | 0.84136 | -1.50691 | -0.589003 | 0.221948 | 0.775346 | 1.33753 | 2.27771 | 3.11766 |
| player | theta_1 | 1197 | -0.385675 | 0.924667 | -2.79699 | -1.73931 | -1.01784 | -0.474624 | 0.12208 | 1.27676 | 3.75085 |
| player | theta_2 | 1197 | -0.382255 | 0.87121 | -3.12272 | -1.68932 | -0.937229 | -0.457207 | 0.118221 | 1.1669 | 2.86708 |
| player | theta_3 | 1197 | -0.395106 | 0.885975 | -2.9596 | -1.69355 | -0.972469 | -0.519222 | 0.106398 | 1.23261 | 3.48147 |
| player | theta_norm | 1197 | 1.55542 | 0.654943 | 0.134329 | 0.609069 | 1.0911 | 1.4917 | 1.94982 | 2.7627 | 4.62363 |
| tossup | start_difficulty_d1 | 1240 | -0.958054 | 0.529457 | -2.74307 | -1.71876 | -1.29531 | -1.00204 | -0.655961 | -0.0744006 | 1.90386 |
| tossup | start_difficulty_d2 | 1240 | -0.950424 | 0.503446 | -2.51943 | -1.66222 | -1.27762 | -1.00263 | -0.678701 | -0.1067 | 1.90422 |
| tossup | start_difficulty_d3 | 1240 | -0.96654 | 0.489087 | -2.76987 | -1.70083 | -1.2729 | -0.985237 | -0.652837 | -0.159885 | 1.22429 |
| tossup | end_difficulty_d1 | 1240 | -1.95461 | 0.620614 | -4.05958 | -2.86575 | -2.35409 | -1.9936 | -1.60212 | -0.916357 | 1.17496 |
| tossup | end_difficulty_d2 | 1240 | -1.94656 | 0.593637 | -3.77459 | -2.78076 | -2.3328 | -2.0062 | -1.61671 | -0.958774 | 1.27254 |
| tossup | end_difficulty_d3 | 1240 | -1.96469 | 0.572704 | -4.03848 | -2.84482 | -2.33002 | -1.97673 | -1.60563 | -1.04223 | 0.541254 |
| tossup | total_drop_d1 | 1240 | 0.996556 | 0.112785 | 0.617324 | 0.812949 | 0.924347 | 0.994152 | 1.07038 | 1.17284 | 1.52063 |
| tossup | total_drop_d2 | 1240 | 0.996135 | 0.108037 | 0.604483 | 0.820315 | 0.929859 | 0.997597 | 1.06294 | 1.16754 | 1.51063 |
| tossup | total_drop_d3 | 1240 | 0.998149 | 0.102507 | 0.636324 | 0.832402 | 0.927337 | 0.997219 | 1.06947 | 1.16664 | 1.31982 |
| tossup | drop_share_1_d1 | 1240 | 0.304652 | 0.015282 | 0.224572 | 0.280106 | 0.295351 | 0.304771 | 0.314745 | 0.327469 | 0.364787 |
| tossup | drop_share_2_d1 | 1240 | 0.346599 | 0.0114171 | 0.304767 | 0.328802 | 0.339079 | 0.346276 | 0.354258 | 0.366012 | 0.387389 |
| tossup | drop_share_3_d1 | 1240 | 0.348749 | 0.0164022 | 0.30219 | 0.323212 | 0.337694 | 0.348106 | 0.359062 | 0.374136 | 0.439962 |
| tossup | drop_share_1_d2 | 1240 | 0.304308 | 0.0140704 | 0.250077 | 0.280833 | 0.295976 | 0.304315 | 0.31279 | 0.328486 | 0.351616 |
| tossup | drop_share_2_d2 | 1240 | 0.347377 | 0.0111332 | 0.307286 | 0.329178 | 0.339873 | 0.347423 | 0.354859 | 0.366001 | 0.378743 |
| tossup | drop_share_3_d2 | 1240 | 0.348316 | 0.0152414 | 0.298858 | 0.32417 | 0.338579 | 0.347815 | 0.357304 | 0.374874 | 0.402961 |
| tossup | drop_share_1_d3 | 1240 | 0.305065 | 0.0147529 | 0.251729 | 0.280731 | 0.29599 | 0.305234 | 0.314698 | 0.328775 | 0.35982 |
| tossup | drop_share_2_d3 | 1240 | 0.346965 | 0.0110553 | 0.31068 | 0.329176 | 0.339275 | 0.346851 | 0.354187 | 0.365075 | 0.386753 |
| tossup | drop_share_3_d3 | 1240 | 0.34797 | 0.0152805 | 0.302788 | 0.32394 | 0.337834 | 0.347325 | 0.357452 | 0.373153 | 0.413632 |
| tossup | r_1 | 1240 | 0.321388 | 0.167292 | 0.0482951 | 0.1091 | 0.190749 | 0.285203 | 0.424983 | 0.656874 | 0.854279 |
| tossup | r_2 | 1240 | 0.338994 | 0.162204 | 0.0587326 | 0.123986 | 0.208774 | 0.31063 | 0.449818 | 0.645307 | 0.846165 |
| tossup | r_3 | 1240 | 0.339617 | 0.162378 | 0.0594774 | 0.126524 | 0.208899 | 0.311115 | 0.446319 | 0.654744 | 0.826321 |
| tossup | r_norm | 1240 | 0.641178 | 0.0551329 | 0.577513 | 0.581524 | 0.599583 | 0.62507 | 0.667275 | 0.750866 | 0.860578 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 8.64302 | 0.486436 | 6.47102 | 7.7528 | 8.48361 | 8.65539 | 8.85153 | 9.41019 | 10.4545 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 8.7049 | 0.504021 | 5.13881 | 7.8867 | 8.56741 | 8.69436 | 8.89256 | 9.49213 | 11.1493 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 8.6824 | 0.49746 | 4.52745 | 7.84019 | 8.56451 | 8.69014 | 8.88627 | 9.42027 | 10.5263 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 4.70377 | 4.07526 | -13.0736 | -3.34482 | 1.82085 | 7.44326 | 7.66922 | 7.96051 | 8.44276 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 5.59318 | 3.84636 | -14.8216 | -2.62797 | 3.78788 | 7.59183 | 7.76453 | 8.04968 | 8.88753 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 5.44096 | 3.83385 | -17.291 | -2.11283 | 2.93085 | 7.58895 | 7.76217 | 8.0846 | 9.36314 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.93925 | 4.11845 | 0.862511 | 0.944001 | 1.00173 | 1.05961 | 6.67727 | 12.0694 | 21.9433 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 3.11172 | 3.90763 | 0.871999 | 0.933261 | 0.978348 | 1.02213 | 4.71836 | 11.3409 | 23.7624 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 3.24144 | 3.84611 | 0.825239 | 0.932097 | 0.980814 | 1.02792 | 5.77048 | 10.665 | 26.1799 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.278186 | 0.09846 | 0.0546458 | 0.108969 | 0.242166 | 0.297212 | 0.310174 | 0.412507 | 0.795668 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.325132 | 0.0834956 | 0.0653341 | 0.149943 | 0.318095 | 0.343105 | 0.356016 | 0.445554 | 0.731384 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.396683 | 0.130871 | 0.0600803 | 0.22867 | 0.341297 | 0.355172 | 0.404459 | 0.709902 | 0.865831 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.280451 | 0.084226 | 0.0328577 | 0.114564 | 0.277908 | 0.297559 | 0.3095 | 0.339883 | 0.778751 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.328132 | 0.0717687 | 0.0575678 | 0.162102 | 0.331632 | 0.344024 | 0.353961 | 0.39274 | 0.714216 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.391417 | 0.12171 | 0.0794412 | 0.262282 | 0.343109 | 0.354548 | 0.374838 | 0.685561 | 0.905142 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.287337 | 0.0900663 | 0.0570249 | 0.108214 | 0.281947 | 0.299105 | 0.31063 | 0.425599 | 0.748067 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.327811 | 0.0689838 | 0.0843287 | 0.177642 | 0.32803 | 0.343299 | 0.354158 | 0.393151 | 0.70406 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.384851 | 0.115282 | 0.0488073 | 0.268586 | 0.341258 | 0.353342 | 0.374792 | 0.673849 | 0.858646 |
| tossup_hazard | hazard_r_1 | 1240 | 0.370653 | 0.303164 | 0.0162793 | 0.0441553 | 0.101765 | 0.232796 | 0.636659 | 0.894205 | 0.951549 |
| tossup_hazard | hazard_r_2 | 1240 | 0.308028 | 0.269049 | 0.0140812 | 0.0349991 | 0.0749982 | 0.191938 | 0.525089 | 0.833333 | 0.952905 |
| tossup_hazard | hazard_r_3 | 1240 | 0.321319 | 0.29046 | 0.0113229 | 0.0346614 | 0.0745123 | 0.189008 | 0.5882 | 0.859645 | 0.969639 |
