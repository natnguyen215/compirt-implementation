# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating-10000-steps/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating-10000-steps/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 308722 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.608291 |
| log_loss | 0.669546 |
| ece | 0.223451 |
| brier | 0.236088 |
| accuracy | 0.620611 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.143567 |
| probability_std | 0.17309 |
| probability_p10 | 0.291619 |
| probability_p50 | 0.558145 |
| probability_p90 | 0.75281 |
| mean_predictive_variance | 0.218375 |
| integrated_brier_score | 0.0964814 |
| joint_tossup_event_log_loss | 6.79488 |
| buzz_position_mae | 0.1399 |
| buzz_position_median_absolute_error | 0.114613 |
| buzz_position_bias | -0.000623426 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.36729 |
| first_buzzer_mean_reciprocal_rank | 0.576756 |
| first_buzzer_log_loss | 1.6533 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.608291 |
| neg_average_precision | 0.316502 |
| neg_precision | 0.308997 |
| neg_recall | 0.492442 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.144185 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0496517 |
| no_buzz_calibration_error | 0.0365386 |
| no_buzz_brier | 0.0189605 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.608291 | 0.669546 | 0.223451 | 0.236088 | 0.620611 | 0.764178 | -0.143567 | 0.17309 | 0.291619 | 0.558145 | 0.75281 | 0.218375 |
| tossup_correctness | tier | fall | 2798 | 0.61296 | 0.681668 | 0.255041 | 0.240697 | 0.610079 | 0.785204 | -0.175125 | 0.178638 | 0.270543 | 0.551327 | 0.747909 | 0.217179 |
| tossup_correctness | tier | nationals | 1545 | 0.597045 | 0.691232 | 0.210215 | 0.247527 | 0.582524 | 0.721036 | -0.138511 | 0.150458 | 0.299936 | 0.518782 | 0.697873 | 0.227245 |
| tossup_correctness | tier | regionals | 2039 | 0.602961 | 0.66077 | 0.20019 | 0.231455 | 0.644434 | 0.762138 | -0.117705 | 0.185769 | 0.285805 | 0.584267 | 0.788162 | 0.211626 |
| tossup_correctness | tier | winter | 2875 | 0.612085 | 0.65232 | 0.21657 | 0.228743 | 0.634435 | 0.768348 | -0.133913 | 0.166505 | 0.315923 | 0.572723 | 0.751884 | 0.219558 |
| tossup_correctness | category | Current Events | 129 | 0.599784 | 0.711341 | 0.186197 | 0.25633 | 0.581395 | 0.666667 | -0.0852713 | 0.184335 | 0.229837 | 0.520961 | 0.713478 | 0.215856 |
| tossup_correctness | category | Fine Arts | 1074 | 0.584782 | 0.702177 | 0.257066 | 0.250623 | 0.564246 | 0.776536 | -0.212291 | 0.175542 | 0.282106 | 0.532171 | 0.742334 | 0.218742 |
| tossup_correctness | category | Geography | 180 | 0.546808 | 0.738166 | 0.163479 | 0.266203 | 0.522222 | 0.616667 | -0.0944444 | 0.164421 | 0.249927 | 0.507075 | 0.713014 | 0.22296 |
| tossup_correctness | category | History | 1454 | 0.606988 | 0.665686 | 0.219763 | 0.234802 | 0.627923 | 0.757909 | -0.129986 | 0.161859 | 0.307317 | 0.557187 | 0.731022 | 0.222346 |
| tossup_correctness | category | Literature | 1435 | 0.614751 | 0.633002 | 0.24258 | 0.219417 | 0.671777 | 0.810453 | -0.138676 | 0.166132 | 0.328988 | 0.590785 | 0.764222 | 0.217793 |
| tossup_correctness | category | Mythology | 324 | 0.592485 | 0.674661 | 0.247092 | 0.237693 | 0.601852 | 0.79321 | -0.191358 | 0.173809 | 0.307717 | 0.562182 | 0.760308 | 0.217663 |
| tossup_correctness | category | Other Academic | 71 | 0.521786 | 0.705571 | 0.248345 | 0.254955 | 0.577465 | 0.760563 | -0.183099 | 0.162748 | 0.326465 | 0.529325 | 0.757109 | 0.222657 |
| tossup_correctness | category | Philosophy | 310 | 0.658268 | 0.622034 | 0.209412 | 0.216548 | 0.632258 | 0.76129 | -0.129032 | 0.165918 | 0.325857 | 0.567955 | 0.746517 | 0.219755 |
| tossup_correctness | category | Popular Culture | 108 | 0.505208 | 0.88174 | 0.449828 | 0.327223 | 0.388889 | 0.888889 | -0.5 | 0.161524 | 0.220568 | 0.434146 | 0.647718 | 0.220196 |
| tossup_correctness | category | Religion | 361 | 0.643877 | 0.659158 | 0.216994 | 0.231803 | 0.614958 | 0.742382 | -0.127424 | 0.161037 | 0.306859 | 0.539301 | 0.730069 | 0.223188 |
| tossup_correctness | category | Science | 1445 | 0.614489 | 0.687177 | 0.227028 | 0.244135 | 0.607612 | 0.746021 | -0.138408 | 0.168798 | 0.276339 | 0.535216 | 0.729307 | 0.221088 |
| tossup_correctness | category | Social Science | 327 | 0.65666 | 0.636004 | 0.186752 | 0.223469 | 0.626911 | 0.718654 | -0.0917431 | 0.160455 | 0.3113 | 0.553132 | 0.730956 | 0.223173 |
| tossup_correctness | category | Unknown | 2039 | 0.602961 | 0.66077 | 0.20019 | 0.231455 | 0.644434 | 0.762138 | -0.117705 | 0.185769 | 0.285805 | 0.584267 | 0.788162 | 0.211626 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.642835 | 0.773575 | 0.302579 | 0.279954 | 0.530055 | 0.743169 | -0.213115 | 0.173646 | 0.198572 | 0.445907 | 0.664757 | 0.216317 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.624551 | 0.716854 | 0.248646 | 0.257328 | 0.557068 | 0.728796 | -0.171728 | 0.169763 | 0.242241 | 0.492962 | 0.696091 | 0.220787 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.629723 | 0.68644 | 0.234112 | 0.242818 | 0.615007 | 0.752568 | -0.137561 | 0.175182 | 0.264202 | 0.535995 | 0.737031 | 0.218971 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.612894 | 0.661166 | 0.240213 | 0.232463 | 0.622957 | 0.786087 | -0.16313 | 0.171069 | 0.304114 | 0.563472 | 0.754706 | 0.218631 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.578857 | 0.643606 | 0.186873 | 0.225121 | 0.648253 | 0.764393 | -0.11614 | 0.163929 | 0.34772 | 0.595087 | 0.778835 | 0.217044 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | 0.610021 | 1.13993 | -2.27895 | -1.08008 | -0.186779 | 0.394415 | 1.41549 | 2.6419 | 3.92465 |
| player | theta_2 | 1197 | 0.061991 | 0.843288 | -2.4816 | -1.23874 | -0.421433 | -0.0187756 | 0.514453 | 1.56962 | 3.73951 |
| player | theta_3 | 1197 | 0.58887 | 1.35437 | -3.21839 | -1.47952 | -0.452853 | 0.466614 | 1.66002 | 2.81969 | 4.69815 |
| player | theta_norm | 1197 | 1.91716 | 0.943208 | 0.0465476 | 0.565627 | 1.1505 | 1.82627 | 2.61708 | 3.5272 | 4.75353 |
| tossup | start_difficulty_d1 | 1240 | 1.66924 | 0.899896 | -0.915581 | 0.101511 | 0.947822 | 1.94278 | 2.31062 | 2.9541 | 3.88389 |
| tossup | start_difficulty_d2 | 1240 | 0.955905 | 0.67813 | -1.64838 | -0.341301 | 0.546772 | 1.04477 | 1.42441 | 1.93314 | 2.8369 |
| tossup | start_difficulty_d3 | 1240 | 1.15078 | 0.987473 | -1.38304 | -0.266517 | 0.433171 | 0.947066 | 1.99126 | 2.78073 | 3.93654 |
| tossup | end_difficulty_d1 | 1240 | 0.463889 | 0.740387 | -2.23468 | -0.972875 | 0.0323653 | 0.640785 | 0.905699 | 1.53317 | 2.64013 |
| tossup | end_difficulty_d2 | 1240 | -0.11564 | 0.64989 | -2.82025 | -1.42839 | -0.440621 | 0.0173314 | 0.297323 | 0.726099 | 2.1418 |
| tossup | end_difficulty_d3 | 1240 | 0.080255 | 0.863695 | -2.70539 | -1.29136 | -0.53463 | 0.0489591 | 0.752489 | 1.39509 | 2.43839 |
| tossup | total_drop_d1 | 1240 | 1.20535 | 0.44304 | 0.442868 | 0.705084 | 0.839309 | 1.06807 | 1.50983 | 2.01698 | 3.29503 |
| tossup | total_drop_d2 | 1240 | 1.07155 | 0.386272 | 0.51776 | 0.735022 | 0.847821 | 0.946088 | 1.17925 | 1.78874 | 4.47569 |
| tossup | total_drop_d3 | 1240 | 1.07053 | 0.438445 | 0.516039 | 0.714405 | 0.823796 | 0.908767 | 1.07799 | 1.95746 | 4.03263 |
| tossup | drop_share_1_d1 | 1240 | 0.206125 | 0.0853118 | 0.0370013 | 0.0823949 | 0.123875 | 0.224324 | 0.274337 | 0.308137 | 0.683324 |
| tossup | drop_share_2_d1 | 1240 | 0.274248 | 0.094393 | 0.0472715 | 0.10823 | 0.195534 | 0.311737 | 0.338043 | 0.370214 | 0.694135 |
| tossup | drop_share_3_d1 | 1240 | 0.519627 | 0.159572 | 0.140232 | 0.348085 | 0.38685 | 0.458983 | 0.666292 | 0.800567 | 0.915727 |
| tossup | drop_share_1_d2 | 1240 | 0.231086 | 0.0738972 | 0.0402655 | 0.100821 | 0.156212 | 0.265392 | 0.286872 | 0.308703 | 0.465555 |
| tossup | drop_share_2_d2 | 1240 | 0.294417 | 0.081339 | 0.0636563 | 0.126751 | 0.248587 | 0.332605 | 0.346135 | 0.361912 | 0.533881 |
| tossup | drop_share_3_d2 | 1240 | 0.474497 | 0.148238 | 0.139346 | 0.346441 | 0.369159 | 0.394827 | 0.593902 | 0.762813 | 0.896025 |
| tossup | drop_share_1_d3 | 1240 | 0.257291 | 0.0719476 | 0.0429152 | 0.0953251 | 0.249098 | 0.280891 | 0.294463 | 0.314427 | 0.632403 |
| tossup | drop_share_2_d3 | 1240 | 0.319063 | 0.0730825 | 0.0608213 | 0.143835 | 0.320011 | 0.33718 | 0.347993 | 0.369498 | 0.75083 |
| tossup | drop_share_3_d3 | 1240 | 0.423646 | 0.123463 | 0.117335 | 0.336958 | 0.36119 | 0.378117 | 0.419661 | 0.747521 | 0.879408 |
| tossup | r_1 | 1240 | 0.470919 | 0.315609 | 0.0174577 | 0.0341032 | 0.139648 | 0.478434 | 0.790085 | 0.897683 | 0.953387 |
| tossup | r_2 | 1240 | 0.242021 | 0.237726 | 0.0121607 | 0.0249001 | 0.0571025 | 0.130174 | 0.398433 | 0.731798 | 0.929089 |
| tossup | r_3 | 1240 | 0.28706 | 0.294102 | 0.0201799 | 0.0364395 | 0.067712 | 0.145521 | 0.403875 | 0.890248 | 0.95822 |
| tossup | r_norm | 1240 | 0.771309 | 0.101273 | 0.577729 | 0.60632 | 0.684498 | 0.778335 | 0.860414 | 0.919792 | 0.958682 |
