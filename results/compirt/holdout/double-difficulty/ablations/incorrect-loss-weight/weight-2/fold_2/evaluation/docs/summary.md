# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-2/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-2/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 291596 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.711698 |
| log_loss | 0.528724 |
| ece | 0.112461 |
| brier | 0.175539 |
| accuracy | 0.746894 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0172842 |
| probability_std | 0.190221 |
| probability_p10 | 0.373701 |
| probability_p50 | 0.684575 |
| probability_p90 | 0.876791 |
| mean_predictive_variance | 0.190798 |
| integrated_brier_score | 0.102507 |
| joint_tossup_event_log_loss | 6.65697 |
| buzz_position_mae | 0.15226 |
| buzz_position_median_absolute_error | 0.13432 |
| buzz_position_bias | -0.0431706 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.356163 |
| first_buzzer_mean_reciprocal_rank | 0.569805 |
| first_buzzer_log_loss | 1.66183 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.711698 |
| neg_average_precision | 0.448483 |
| neg_precision | 0.460278 |
| neg_recall | 0.424645 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.190025 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0136924 |
| no_buzz_calibration_error | 0.000579347 |
| no_buzz_brier | 0.0128455 |
| full_pmf_max_mass_error | 1.55431e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.711698 | 0.528724 | 0.112461 | 0.175539 | 0.746894 | 0.764178 | -0.0172842 | 0.190221 | 0.373701 | 0.684575 | 0.876791 | 0.190798 |
| tossup_correctness | tier | fall | 2798 | 0.738972 | 0.498895 | 0.12093 | 0.162987 | 0.767691 | 0.785204 | -0.0175125 | 0.190783 | 0.380699 | 0.704981 | 0.884433 | 0.186616 |
| tossup_correctness | tier | nationals | 1545 | 0.711929 | 0.5573 | 0.0943851 | 0.187852 | 0.721036 | 0.721036 | 0 | 0.19601 | 0.35015 | 0.652546 | 0.867796 | 0.19554 |
| tossup_correctness | tier | regionals | 2039 | 0.704109 | 0.535684 | 0.115906 | 0.178866 | 0.738107 | 0.762138 | -0.0240314 | 0.187797 | 0.365415 | 0.676529 | 0.874722 | 0.193348 |
| tossup_correctness | tier | winter | 2875 | 0.686612 | 0.537463 | 0.111488 | 0.178777 | 0.746783 | 0.768348 | -0.0215652 | 0.186775 | 0.395336 | 0.687092 | 0.873364 | 0.19051 |
| tossup_correctness | category | Current Events | 129 | 0.698756 | 0.58585 | 0.0889071 | 0.202742 | 0.705426 | 0.666667 | 0.0387597 | 0.207673 | 0.306599 | 0.646577 | 0.898586 | 0.190477 |
| tossup_correctness | category | Fine Arts | 1074 | 0.706585 | 0.530492 | 0.135615 | 0.176256 | 0.752328 | 0.776536 | -0.0242086 | 0.195605 | 0.368015 | 0.669021 | 0.876173 | 0.19188 |
| tossup_correctness | category | Geography | 180 | 0.751926 | 0.558928 | 0.0922674 | 0.190159 | 0.727778 | 0.616667 | 0.111111 | 0.250425 | 0.131313 | 0.622054 | 0.867809 | 0.183207 |
| tossup_correctness | category | History | 1454 | 0.697665 | 0.539661 | 0.105011 | 0.180501 | 0.734525 | 0.757909 | -0.0233838 | 0.192525 | 0.36218 | 0.688366 | 0.881913 | 0.189521 |
| tossup_correctness | category | Literature | 1435 | 0.725678 | 0.471048 | 0.113518 | 0.149717 | 0.802091 | 0.810453 | -0.00836237 | 0.173315 | 0.434084 | 0.735903 | 0.890004 | 0.180683 |
| tossup_correctness | category | Mythology | 324 | 0.673152 | 0.508249 | 0.0962979 | 0.165101 | 0.768519 | 0.79321 | -0.0246914 | 0.164835 | 0.462567 | 0.728379 | 0.877844 | 0.183337 |
| tossup_correctness | category | Other Academic | 71 | 0.602397 | 0.588902 | 0.167933 | 0.197373 | 0.732394 | 0.760563 | -0.028169 | 0.166342 | 0.372237 | 0.686311 | 0.845305 | 0.201173 |
| tossup_correctness | category | Philosophy | 310 | 0.726638 | 0.51919 | 0.110868 | 0.172333 | 0.76129 | 0.76129 | 0 | 0.171059 | 0.426451 | 0.667293 | 0.87315 | 0.197731 |
| tossup_correctness | category | Popular Culture | 108 | 0.460937 | 0.445053 | 0.148997 | 0.135407 | 0.851852 | 0.888889 | -0.037037 | 0.118343 | 0.608904 | 0.749427 | 0.877079 | 0.176067 |
| tossup_correctness | category | Religion | 361 | 0.669917 | 0.592669 | 0.147457 | 0.203886 | 0.689751 | 0.742382 | -0.0526316 | 0.183369 | 0.347813 | 0.612982 | 0.819983 | 0.207002 |
| tossup_correctness | category | Science | 1445 | 0.716283 | 0.541187 | 0.106215 | 0.181389 | 0.726644 | 0.746021 | -0.0193772 | 0.187817 | 0.367791 | 0.668823 | 0.861322 | 0.195079 |
| tossup_correctness | category | Social Science | 327 | 0.735014 | 0.563068 | 0.11353 | 0.189659 | 0.70948 | 0.718654 | -0.00917431 | 0.215907 | 0.279712 | 0.640866 | 0.863922 | 0.192333 |
| tossup_correctness | category | Unknown | 2039 | 0.704109 | 0.535684 | 0.115906 | 0.178866 | 0.738107 | 0.762138 | -0.0240314 | 0.187797 | 0.365415 | 0.676529 | 0.874722 | 0.193348 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.659887 | 0.588584 | 0.132046 | 0.202855 | 0.699454 | 0.743169 | -0.0437158 | 0.194134 | 0.297172 | 0.643817 | 0.849229 | 0.199964 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.72223 | 0.546025 | 0.0960306 | 0.182784 | 0.740314 | 0.728796 | 0.0115183 | 0.193026 | 0.349089 | 0.659501 | 0.86886 | 0.195114 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.726664 | 0.522059 | 0.0980676 | 0.172629 | 0.749888 | 0.752568 | -0.00267977 | 0.189959 | 0.373936 | 0.687749 | 0.874211 | 0.190045 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.705955 | 0.508592 | 0.111185 | 0.167189 | 0.763478 | 0.786087 | -0.0226087 | 0.179473 | 0.412338 | 0.706163 | 0.883486 | 0.187199 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.703807 | 0.543808 | 0.128702 | 0.181729 | 0.733777 | 0.764393 | -0.0306156 | 0.196579 | 0.352241 | 0.669317 | 0.873853 | 0.192872 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 2.65937 | 0.770329 | 0.483034 | 1.41291 | 2.13787 | 2.63318 | 3.17882 | 3.93597 | 4.69215 |
| player | theta_1 | 1197 | -1.21973 | 0.916814 | -3.74281 | -2.62838 | -1.84672 | -1.29266 | -0.698578 | 0.379585 | 2.11622 |
| player | theta_2 | 1197 | -1.03335 | 0.715704 | -3.33138 | -2.27431 | -1.47371 | -1.02501 | -0.548048 | 0.0867711 | 1.53835 |
| player | theta_3 | 1197 | -1.11112 | 0.812629 | -3.27828 | -2.35211 | -1.64027 | -1.17775 | -0.633718 | 0.326725 | 2.13915 |
| player | theta_norm | 1197 | 2.29996 | 0.715717 | 0.226493 | 1.20815 | 1.80022 | 2.24842 | 2.79612 | 3.50994 | 4.63891 |
| tossup | start_difficulty_d1 | 1240 | -1.12188 | 0.627249 | -3.50449 | -2.04745 | -1.52238 | -1.17218 | -0.776497 | -0.0304833 | 1.7805 |
| tossup | start_difficulty_d2 | 1240 | -1.11312 | 0.576157 | -3.32224 | -2.01288 | -1.47749 | -1.12788 | -0.752743 | -0.127422 | 1.24747 |
| tossup | start_difficulty_d3 | 1240 | -1.11404 | 0.581563 | -3.43935 | -2.04199 | -1.49216 | -1.12837 | -0.754672 | -0.114865 | 1.14591 |
| tossup | end_difficulty_d1 | 1240 | -2.11399 | 0.734359 | -4.60525 | -3.17855 | -2.57412 | -2.16019 | -1.69937 | -0.86571 | 1.08172 |
| tossup | end_difficulty_d2 | 1240 | -2.10149 | 0.6778 | -4.90495 | -3.17693 | -2.51787 | -2.11419 | -1.67773 | -0.975427 | 0.637484 |
| tossup | end_difficulty_d3 | 1240 | -2.09982 | 0.67755 | -4.87548 | -3.21822 | -2.53239 | -2.11489 | -1.6759 | -0.964183 | 0.438432 |
| tossup | total_drop_d1 | 1240 | 0.99211 | 0.154219 | 0.572675 | 0.761544 | 0.897107 | 0.990655 | 1.07236 | 1.21323 | 2.93875 |
| tossup | total_drop_d2 | 1240 | 0.988374 | 0.129464 | 0.587133 | 0.799043 | 0.903806 | 0.981959 | 1.05777 | 1.22053 | 1.58271 |
| tossup | total_drop_d3 | 1240 | 0.985782 | 0.124717 | 0.625552 | 0.787655 | 0.901155 | 0.980121 | 1.05705 | 1.20429 | 1.47723 |
| tossup | drop_share_1_d1 | 1240 | 0.30245 | 0.0196572 | 0.194246 | 0.272414 | 0.291753 | 0.302775 | 0.315113 | 0.3316 | 0.379082 |
| tossup | drop_share_2_d1 | 1240 | 0.34705 | 0.0128436 | 0.304447 | 0.326359 | 0.338915 | 0.347356 | 0.354995 | 0.366795 | 0.457006 |
| tossup | drop_share_3_d1 | 1240 | 0.350499 | 0.0208263 | 0.293604 | 0.320354 | 0.33664 | 0.34961 | 0.361972 | 0.383777 | 0.4698 |
| tossup | drop_share_1_d2 | 1240 | 0.30249 | 0.0169359 | 0.207797 | 0.274322 | 0.292551 | 0.302474 | 0.313133 | 0.330004 | 0.367445 |
| tossup | drop_share_2_d2 | 1240 | 0.347009 | 0.0120566 | 0.310432 | 0.327454 | 0.339204 | 0.346793 | 0.355288 | 0.367428 | 0.386342 |
| tossup | drop_share_3_d2 | 1240 | 0.350501 | 0.018145 | 0.286197 | 0.323101 | 0.338443 | 0.35023 | 0.361254 | 0.377948 | 0.459477 |
| tossup | drop_share_1_d3 | 1240 | 0.302391 | 0.0175717 | 0.233581 | 0.272302 | 0.292085 | 0.302831 | 0.314062 | 0.329866 | 0.376191 |
| tossup | drop_share_2_d3 | 1240 | 0.347189 | 0.0118454 | 0.307063 | 0.328508 | 0.339429 | 0.346697 | 0.354956 | 0.367404 | 0.394493 |
| tossup | drop_share_3_d3 | 1240 | 0.350419 | 0.0183929 | 0.294294 | 0.322049 | 0.33812 | 0.350035 | 0.361051 | 0.381256 | 0.425561 |
| tossup | r_1 | 1240 | 0.337928 | 0.199601 | 0.0413262 | 0.0912764 | 0.172417 | 0.282096 | 0.483577 | 0.723491 | 0.857322 |
| tossup | r_2 | 1240 | 0.326287 | 0.171117 | 0.0474725 | 0.1086 | 0.195162 | 0.293859 | 0.425455 | 0.683791 | 0.845875 |
| tossup | r_3 | 1240 | 0.335785 | 0.175679 | 0.0525914 | 0.106314 | 0.193524 | 0.304933 | 0.452868 | 0.671881 | 0.87977 |
| tossup | r_norm | 1240 | 0.655114 | 0.0643678 | 0.577413 | 0.582677 | 0.604254 | 0.635346 | 0.690684 | 0.786153 | 0.883961 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.47111 | 0.48999 | 2.01259 | 3.72102 | 4.19007 | 4.4308 | 4.69179 | 5.37829 | 6.19764 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.45606 | 0.438609 | 2.12827 | 3.78725 | 4.21311 | 4.42385 | 4.6661 | 5.19422 | 6.71659 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.4465 | 0.436623 | 2.63171 | 3.73475 | 4.20856 | 4.4248 | 4.67947 | 5.24824 | 6.09234 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.77056 | 2.35031 | -11.7626 | -3.1489 | 0.807691 | 2.90571 | 3.30439 | 3.6315 | 4.32841 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.31466 | 1.9354 | -8.57961 | -2.21121 | 2.31337 | 3.07879 | 3.38546 | 3.70418 | 4.2991 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.12068 | 2.22979 | -10.9466 | -2.6168 | 1.99834 | 3.08478 | 3.38083 | 3.71125 | 4.12664 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.70055 | 2.5117 | 0.904864 | 0.98199 | 1.05874 | 1.32193 | 3.88533 | 8.11501 | 16.2751 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.14141 | 2.09984 | 0.881118 | 0.959412 | 1.02299 | 1.17855 | 1.93253 | 7.04744 | 13.9804 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.32582 | 2.36851 | 0.85981 | 0.969308 | 1.03142 | 1.18246 | 2.17571 | 7.5186 | 15.6247 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.237663 | 0.079361 | 0.0440919 | 0.0818843 | 0.185515 | 0.271244 | 0.294347 | 0.315691 | 0.555444 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.343894 | 0.0746608 | 0.0680912 | 0.188356 | 0.335816 | 0.351166 | 0.36624 | 0.440338 | 0.688143 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.418443 | 0.127515 | 0.100088 | 0.307106 | 0.347521 | 0.369235 | 0.435889 | 0.716326 | 0.882118 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.252182 | 0.0702012 | 0.0278898 | 0.0951857 | 0.226973 | 0.279094 | 0.295682 | 0.315264 | 0.621278 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.346862 | 0.0622095 | 0.0642471 | 0.227958 | 0.339689 | 0.351172 | 0.363579 | 0.409328 | 0.687336 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.400955 | 0.108015 | 0.104018 | 0.317121 | 0.349818 | 0.365141 | 0.401904 | 0.659 | 0.890092 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.250217 | 0.0712101 | 0.0405766 | 0.0900516 | 0.229238 | 0.277978 | 0.296756 | 0.313975 | 0.539827 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.348594 | 0.0601744 | 0.0892237 | 0.224582 | 0.340158 | 0.351142 | 0.365276 | 0.427292 | 0.704623 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.401189 | 0.10752 | 0.0609893 | 0.318045 | 0.349581 | 0.366622 | 0.399053 | 0.673307 | 0.863431 |
| tossup_hazard | hazard_r_1 | 1240 | 0.378649 | 0.278295 | 0.0304109 | 0.0633932 | 0.129492 | 0.28697 | 0.610884 | 0.872903 | 0.948708 |
| tossup_hazard | hazard_r_2 | 1240 | 0.300388 | 0.216023 | 0.0236342 | 0.0548135 | 0.120942 | 0.225076 | 0.474833 | 0.703763 | 0.848462 |
| tossup_hazard | hazard_r_3 | 1240 | 0.320963 | 0.240146 | 0.0240362 | 0.0541494 | 0.119301 | 0.241198 | 0.501166 | 0.769611 | 0.919648 |
