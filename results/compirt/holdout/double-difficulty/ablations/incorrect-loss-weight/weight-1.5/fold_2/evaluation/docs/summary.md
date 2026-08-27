# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-1.5/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-1.5/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 287834 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.713353 |
| log_loss | 0.502237 |
| ece | 0.0596247 |
| brier | 0.164236 |
| accuracy | 0.769688 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00550934 |
| probability_std | 0.170614 |
| probability_p10 | 0.459625 |
| probability_p50 | 0.74113 |
| probability_p90 | 0.894364 |
| mean_predictive_variance | 0.178981 |
| integrated_brier_score | 0.102549 |
| joint_tossup_event_log_loss | 6.63349 |
| buzz_position_mae | 0.152309 |
| buzz_position_median_absolute_error | 0.133877 |
| buzz_position_bias | -0.0432211 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.35411 |
| first_buzzer_mean_reciprocal_rank | 0.568365 |
| first_buzzer_log_loss | 1.66277 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.713353 |
| neg_average_precision | 0.449042 |
| neg_precision | 0.520782 |
| neg_recall | 0.292716 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.190416 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0138288 |
| no_buzz_calibration_error | 0.000715765 |
| no_buzz_brier | 0.0128386 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.713353 | 0.502237 | 0.0596247 | 0.164236 | 0.769688 | 0.764178 | 0.00550934 | 0.170614 | 0.459625 | 0.74113 | 0.894364 | 0.178981 |
| tossup_correctness | tier | fall | 2798 | 0.74062 | 0.471119 | 0.0708139 | 0.151549 | 0.791994 | 0.785204 | 0.00679056 | 0.171015 | 0.463506 | 0.757819 | 0.900203 | 0.174701 |
| tossup_correctness | tier | nationals | 1545 | 0.713399 | 0.535466 | 0.038862 | 0.178341 | 0.733981 | 0.721036 | 0.012945 | 0.176199 | 0.434947 | 0.716219 | 0.887436 | 0.184984 |
| tossup_correctness | tier | regionals | 2039 | 0.705944 | 0.508175 | 0.06149 | 0.166729 | 0.7641 | 0.762138 | 0.00196175 | 0.166415 | 0.453045 | 0.731619 | 0.892564 | 0.182046 |
| tossup_correctness | tier | winter | 2875 | 0.688488 | 0.510454 | 0.0615856 | 0.167235 | 0.77113 | 0.768348 | 0.00278261 | 0.169086 | 0.474041 | 0.744166 | 0.891505 | 0.177746 |
| tossup_correctness | category | Current Events | 129 | 0.700919 | 0.581807 | 0.0562548 | 0.200461 | 0.674419 | 0.666667 | 0.00775194 | 0.185917 | 0.387723 | 0.717099 | 0.910715 | 0.182287 |
| tossup_correctness | category | Fine Arts | 1074 | 0.709123 | 0.4967 | 0.0835989 | 0.161548 | 0.790503 | 0.776536 | 0.0139665 | 0.178908 | 0.449981 | 0.731629 | 0.895749 | 0.180499 |
| tossup_correctness | category | Geography | 180 | 0.75284 | 0.549672 | 0.101706 | 0.185895 | 0.705556 | 0.616667 | 0.0888889 | 0.243493 | 0.164685 | 0.689283 | 0.888545 | 0.177205 |
| tossup_correctness | category | History | 1454 | 0.696925 | 0.515996 | 0.0542151 | 0.170095 | 0.755158 | 0.757909 | -0.00275103 | 0.171914 | 0.448009 | 0.744441 | 0.898002 | 0.178 |
| tossup_correctness | category | Literature | 1435 | 0.727224 | 0.445102 | 0.063837 | 0.139348 | 0.818815 | 0.810453 | 0.00836237 | 0.151065 | 0.520369 | 0.785505 | 0.905792 | 0.165938 |
| tossup_correctness | category | Mythology | 324 | 0.676694 | 0.485308 | 0.0675514 | 0.155666 | 0.799383 | 0.79321 | 0.00617284 | 0.143473 | 0.542448 | 0.777013 | 0.89397 | 0.1686 |
| tossup_correctness | category | Other Academic | 71 | 0.59695 | 0.56106 | 0.129799 | 0.183705 | 0.746479 | 0.760563 | -0.0140845 | 0.143295 | 0.489312 | 0.738365 | 0.88161 | 0.187885 |
| tossup_correctness | category | Philosophy | 310 | 0.726924 | 0.495295 | 0.055643 | 0.162146 | 0.764516 | 0.76129 | 0.00322581 | 0.150322 | 0.505871 | 0.731668 | 0.889182 | 0.184807 |
| tossup_correctness | category | Popular Culture | 108 | 0.478299 | 0.407083 | 0.102164 | 0.119509 | 0.87963 | 0.888889 | -0.00925926 | 0.0985769 | 0.676189 | 0.79916 | 0.891172 | 0.158071 |
| tossup_correctness | category | Religion | 361 | 0.673166 | 0.556123 | 0.0883356 | 0.187756 | 0.731302 | 0.742382 | -0.0110803 | 0.167405 | 0.414081 | 0.667357 | 0.8496 | 0.197701 |
| tossup_correctness | category | Science | 1445 | 0.719705 | 0.515844 | 0.0513478 | 0.170936 | 0.749481 | 0.746021 | 0.00346021 | 0.168093 | 0.452908 | 0.727572 | 0.881472 | 0.183795 |
| tossup_correctness | category | Social Science | 327 | 0.734968 | 0.537848 | 0.0607423 | 0.179916 | 0.733945 | 0.718654 | 0.0152905 | 0.202259 | 0.35256 | 0.697235 | 0.888176 | 0.183942 |
| tossup_correctness | category | Unknown | 2039 | 0.705944 | 0.508175 | 0.06149 | 0.166729 | 0.7641 | 0.762138 | 0.00196175 | 0.166415 | 0.453045 | 0.731619 | 0.892564 | 0.182046 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.661765 | 0.556712 | 0.0915824 | 0.188906 | 0.726776 | 0.743169 | -0.0163934 | 0.17439 | 0.383134 | 0.69408 | 0.868738 | 0.192239 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.722174 | 0.525977 | 0.0438424 | 0.174268 | 0.748691 | 0.728796 | 0.0198953 | 0.173511 | 0.428726 | 0.715023 | 0.884742 | 0.185621 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.728561 | 0.500138 | 0.0467532 | 0.16348 | 0.769987 | 0.752568 | 0.0174185 | 0.171181 | 0.461898 | 0.743041 | 0.892316 | 0.178245 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.707785 | 0.482407 | 0.0594122 | 0.156142 | 0.790957 | 0.786087 | 0.00486957 | 0.158106 | 0.502206 | 0.761043 | 0.900577 | 0.17359 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.705176 | 0.511912 | 0.0733276 | 0.167853 | 0.758403 | 0.764393 | -0.00599002 | 0.177878 | 0.432203 | 0.729707 | 0.892748 | 0.181768 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 2.65697 | 0.757447 | 0.525656 | 1.42471 | 2.1488 | 2.63258 | 3.18071 | 3.92688 | 4.63484 |
| player | theta_1 | 1197 | -1.21233 | 0.881821 | -3.64073 | -2.54738 | -1.80374 | -1.26557 | -0.70852 | 0.329197 | 2.02284 |
| player | theta_2 | 1197 | -1.01549 | 0.6684 | -3.21333 | -2.134 | -1.4377 | -1.00935 | -0.582302 | 0.0366873 | 1.54873 |
| player | theta_3 | 1197 | -1.10891 | 0.790879 | -3.28475 | -2.31157 | -1.63042 | -1.18269 | -0.640009 | 0.289291 | 2.04072 |
| player | theta_norm | 1197 | 2.26241 | 0.678837 | 0.304461 | 1.23884 | 1.7789 | 2.2231 | 2.73343 | 3.39773 | 4.52905 |
| tossup | start_difficulty_d1 | 1240 | -1.39266 | 0.596009 | -3.53866 | -2.25722 | -1.78191 | -1.45007 | -1.0623 | -0.341287 | 1.48583 |
| tossup | start_difficulty_d2 | 1240 | -1.38344 | 0.546404 | -3.3424 | -2.21955 | -1.74547 | -1.40558 | -1.03006 | -0.458234 | 0.834546 |
| tossup | start_difficulty_d3 | 1240 | -1.38631 | 0.554672 | -3.49196 | -2.26355 | -1.76071 | -1.40508 | -1.03382 | -0.45606 | 0.687308 |
| tossup | end_difficulty_d1 | 1240 | -2.38165 | 0.696296 | -4.64931 | -3.39002 | -2.84094 | -2.44396 | -1.99318 | -1.17836 | 0.786848 |
| tossup | end_difficulty_d2 | 1240 | -2.36983 | 0.641737 | -4.80428 | -3.37146 | -2.78217 | -2.39247 | -1.96691 | -1.3153 | 0.182152 |
| tossup | end_difficulty_d3 | 1240 | -2.3707 | 0.646312 | -4.8602 | -3.41299 | -2.79632 | -2.3942 | -1.95319 | -1.296 | -0.0432994 |
| tossup | total_drop_d1 | 1240 | 0.988994 | 0.13166 | 0.583399 | 0.777467 | 0.900531 | 0.988775 | 1.06851 | 1.18552 | 2.17021 |
| tossup | total_drop_d2 | 1240 | 0.986391 | 0.117179 | 0.613866 | 0.811776 | 0.90688 | 0.982156 | 1.05795 | 1.19221 | 1.46188 |
| tossup | total_drop_d3 | 1240 | 0.984393 | 0.114921 | 0.633373 | 0.801311 | 0.901915 | 0.982806 | 1.05572 | 1.18609 | 1.36824 |
| tossup | drop_share_1_d1 | 1240 | 0.303199 | 0.0175953 | 0.21072 | 0.275121 | 0.293229 | 0.303207 | 0.315066 | 0.32971 | 0.372276 |
| tossup | drop_share_2_d1 | 1240 | 0.347023 | 0.0120842 | 0.305333 | 0.326899 | 0.339132 | 0.347274 | 0.354908 | 0.365874 | 0.414822 |
| tossup | drop_share_3_d1 | 1240 | 0.349778 | 0.0187513 | 0.295412 | 0.321648 | 0.337503 | 0.349083 | 0.36075 | 0.379979 | 0.445069 |
| tossup | drop_share_1_d2 | 1240 | 0.303058 | 0.015528 | 0.226116 | 0.276864 | 0.293519 | 0.302952 | 0.313108 | 0.328809 | 0.357777 |
| tossup | drop_share_2_d2 | 1240 | 0.346981 | 0.01169 | 0.310543 | 0.327809 | 0.339326 | 0.346757 | 0.355061 | 0.366783 | 0.385547 |
| tossup | drop_share_3_d2 | 1240 | 0.349961 | 0.0166886 | 0.294873 | 0.323648 | 0.338579 | 0.34998 | 0.360459 | 0.376687 | 0.435988 |
| tossup | drop_share_1_d3 | 1240 | 0.302953 | 0.0162525 | 0.237904 | 0.274974 | 0.292662 | 0.302911 | 0.313975 | 0.328363 | 0.36792 |
| tossup | drop_share_2_d3 | 1240 | 0.347176 | 0.0115053 | 0.308573 | 0.328705 | 0.339659 | 0.346987 | 0.35467 | 0.366406 | 0.390126 |
| tossup | drop_share_3_d3 | 1240 | 0.34987 | 0.0169932 | 0.300818 | 0.322378 | 0.338023 | 0.349452 | 0.360448 | 0.378858 | 0.420439 |
| tossup | r_1 | 1240 | 0.331311 | 0.177032 | 0.0539429 | 0.10416 | 0.190197 | 0.289491 | 0.446429 | 0.682785 | 0.860472 |
| tossup | r_2 | 1240 | 0.328708 | 0.143776 | 0.0632419 | 0.128215 | 0.226819 | 0.310872 | 0.406761 | 0.61528 | 0.797905 |
| tossup | r_3 | 1240 | 0.339981 | 0.152248 | 0.0600376 | 0.127227 | 0.222919 | 0.322856 | 0.437945 | 0.618936 | 0.844293 |
| tossup | r_norm | 1240 | 0.636813 | 0.0548239 | 0.577449 | 0.58097 | 0.595561 | 0.618938 | 0.661564 | 0.755251 | 0.866109 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.47519 | 0.48895 | 2.00473 | 3.73889 | 4.20178 | 4.4359 | 4.70935 | 5.37832 | 6.19366 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.45798 | 0.434069 | 2.19009 | 3.7929 | 4.21773 | 4.42836 | 4.67198 | 5.17201 | 6.71356 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.4553 | 0.438337 | 2.5165 | 3.75885 | 4.21475 | 4.43748 | 4.68984 | 5.25512 | 6.08491 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.76621 | 2.32704 | -11.4528 | -3.12463 | 0.666747 | 2.87819 | 3.30484 | 3.64557 | 4.34037 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.32616 | 1.95057 | -8.05508 | -2.41957 | 2.36815 | 3.07834 | 3.38743 | 3.71843 | 4.30399 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.14695 | 2.20092 | -10.9626 | -2.67149 | 2.08928 | 3.07224 | 3.37794 | 3.72347 | 4.1532 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.70898 | 2.49198 | 0.902602 | 0.984308 | 1.06035 | 1.32666 | 3.92061 | 8.09705 | 15.9741 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.13182 | 2.1074 | 0.881074 | 0.959441 | 1.02343 | 1.18188 | 1.85535 | 6.99504 | 13.4826 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.30836 | 2.34084 | 0.857907 | 0.968436 | 1.03433 | 1.19578 | 2.18508 | 7.40061 | 15.6539 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.237205 | 0.0792567 | 0.0441149 | 0.0816326 | 0.183565 | 0.270431 | 0.293951 | 0.315954 | 0.550983 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.344188 | 0.0747542 | 0.0680192 | 0.189485 | 0.336178 | 0.351574 | 0.366147 | 0.443506 | 0.680663 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.418607 | 0.12744 | 0.103022 | 0.307377 | 0.348091 | 0.368807 | 0.437781 | 0.718042 | 0.882168 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.25274 | 0.0695107 | 0.0280115 | 0.0956284 | 0.23221 | 0.279117 | 0.295876 | 0.31458 | 0.61739 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.347421 | 0.0623684 | 0.0641922 | 0.227134 | 0.339912 | 0.351287 | 0.363551 | 0.4092 | 0.685801 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.399839 | 0.106903 | 0.103698 | 0.318596 | 0.350244 | 0.364782 | 0.400274 | 0.658876 | 0.89007 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.249701 | 0.0708937 | 0.0405957 | 0.0900429 | 0.227471 | 0.276272 | 0.296682 | 0.313629 | 0.540068 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.348355 | 0.0587819 | 0.0890743 | 0.228294 | 0.340061 | 0.351202 | 0.36566 | 0.427026 | 0.70596 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.401944 | 0.106938 | 0.0607635 | 0.31891 | 0.349755 | 0.367852 | 0.401861 | 0.673142 | 0.864923 |
| tossup_hazard | hazard_r_1 | 1240 | 0.379318 | 0.278022 | 0.0304822 | 0.0647911 | 0.131781 | 0.28496 | 0.617008 | 0.870645 | 0.948206 |
| tossup_hazard | hazard_r_2 | 1240 | 0.29705 | 0.211595 | 0.0237562 | 0.0563616 | 0.121052 | 0.225378 | 0.464971 | 0.697848 | 0.842911 |
| tossup_hazard | hazard_r_3 | 1240 | 0.323633 | 0.239987 | 0.022496 | 0.0523861 | 0.122579 | 0.24157 | 0.50509 | 0.773384 | 0.921424 |
