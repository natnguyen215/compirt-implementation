# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/unconstrained/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/unconstrained/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 341222 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.653021 |
| log_loss | 0.523943 |
| ece | 0.029309 |
| brier | 0.171912 |
| accuracy | 0.765314 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00318927 |
| probability_std | 0.129878 |
| probability_p10 | 0.556782 |
| probability_p50 | 0.762264 |
| probability_p90 | 0.891555 |
| mean_predictive_variance | 0.175 |
| integrated_brier_score | 0.169461 |
| joint_tossup_event_log_loss | 7.6164 |
| buzz_position_mae | 0.333751 |
| buzz_position_median_absolute_error | 0.33794 |
| buzz_position_bias | -0.320288 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.34928 |
| first_buzzer_mean_reciprocal_rank | 0.561948 |
| first_buzzer_log_loss | 1.68307 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.653021 |
| neg_average_precision | 0.378498 |
| neg_precision | 0.530786 |
| neg_recall | 0.11558 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0316161 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.224212 |
| no_buzz_calibration_error | 0.208303 |
| no_buzz_brier | 0.0685025 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.653021 | 0.523943 | 0.029309 | 0.171912 | 0.765314 | 0.762125 | 0.00318927 | 0.129878 | 0.556782 | 0.762264 | 0.891555 | 0.175 |
| tossup_correctness | tier | fall | 2842 | 0.682925 | 0.483299 | 0.0138904 | 0.155266 | 0.788881 | 0.785362 | 0.00351865 | 0.105218 | 0.640011 | 0.808564 | 0.905542 | 0.155726 |
| tossup_correctness | tier | nationals | 1564 | 0.672627 | 0.580169 | 0.095886 | 0.196324 | 0.719309 | 0.718031 | 0.00127877 | 0.139824 | 0.445622 | 0.631578 | 0.801035 | 0.214589 |
| tossup_correctness | tier | regionals | 1937 | 0.619959 | 0.542809 | 0.0491588 | 0.179766 | 0.758389 | 0.758389 | 0 | 0.116658 | 0.551419 | 0.72313 | 0.857145 | 0.190922 |
| tossup_correctness | tier | winter | 2750 | 0.642587 | 0.520681 | 0.0239106 | 0.169699 | 0.772 | 0.765818 | 0.00618182 | 0.109143 | 0.628758 | 0.797597 | 0.898438 | 0.161187 |
| tossup_correctness | category | Current Events | 126 | 0.693566 | 0.518152 | 0.081094 | 0.171289 | 0.738095 | 0.769841 | -0.031746 | 0.131556 | 0.51836 | 0.692001 | 0.848069 | 0.197068 |
| tossup_correctness | category | Fine Arts | 1071 | 0.667357 | 0.509946 | 0.0410773 | 0.165757 | 0.786181 | 0.766573 | 0.0196078 | 0.126639 | 0.560592 | 0.767774 | 0.885341 | 0.175667 |
| tossup_correctness | category | Geography | 185 | 0.674972 | 0.57196 | 0.0818156 | 0.192774 | 0.745946 | 0.697297 | 0.0486486 | 0.153153 | 0.48944 | 0.734384 | 0.868484 | 0.185851 |
| tossup_correctness | category | History | 1440 | 0.66907 | 0.525287 | 0.0266141 | 0.172582 | 0.757639 | 0.754167 | 0.00347222 | 0.135121 | 0.565112 | 0.800165 | 0.913211 | 0.160721 |
| tossup_correctness | category | Literature | 1422 | 0.624516 | 0.472676 | 0.0358256 | 0.149138 | 0.805204 | 0.814346 | -0.00914205 | 0.115367 | 0.626138 | 0.821456 | 0.910353 | 0.150516 |
| tossup_correctness | category | Mythology | 318 | 0.665755 | 0.494828 | 0.0754341 | 0.158664 | 0.798742 | 0.789308 | 0.00943396 | 0.124166 | 0.569379 | 0.764944 | 0.888558 | 0.176228 |
| tossup_correctness | category | Other Academic | 66 | 0.591265 | 0.609617 | 0.0619776 | 0.210811 | 0.666667 | 0.712121 | -0.0454545 | 0.125803 | 0.466046 | 0.681926 | 0.822101 | 0.211631 |
| tossup_correctness | category | Philosophy | 311 | 0.650589 | 0.543248 | 0.058439 | 0.181278 | 0.736334 | 0.745981 | -0.0096463 | 0.11739 | 0.591084 | 0.776352 | 0.885512 | 0.169986 |
| tossup_correctness | category | Popular Culture | 102 | 0.616667 | 0.412374 | 0.134146 | 0.123104 | 0.872549 | 0.882353 | -0.00980392 | 0.10524 | 0.612308 | 0.752621 | 0.873057 | 0.177318 |
| tossup_correctness | category | Religion | 358 | 0.638835 | 0.584903 | 0.0677845 | 0.199572 | 0.678771 | 0.712291 | -0.0335196 | 0.133711 | 0.522767 | 0.755208 | 0.873503 | 0.18058 |
| tossup_correctness | category | Science | 1433 | 0.664376 | 0.541939 | 0.0353667 | 0.179867 | 0.749477 | 0.738311 | 0.0111654 | 0.136712 | 0.527671 | 0.747471 | 0.875902 | 0.18331 |
| tossup_correctness | category | Social Science | 324 | 0.690237 | 0.53206 | 0.0461285 | 0.176319 | 0.765432 | 0.731481 | 0.0339506 | 0.124681 | 0.556697 | 0.738826 | 0.867978 | 0.186236 |
| tossup_correctness | category | Unknown | 1937 | 0.619959 | 0.542809 | 0.0491588 | 0.179766 | 0.758389 | 0.758389 | 0 | 0.116658 | 0.551419 | 0.72313 | 0.857145 | 0.190922 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.643207 | 0.576532 | 0.0629054 | 0.193708 | 0.718563 | 0.712575 | 0.00598802 | 0.118907 | 0.549894 | 0.74549 | 0.852678 | 0.186855 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.646586 | 0.559416 | 0.0300448 | 0.187181 | 0.736842 | 0.729167 | 0.00767544 | 0.12809 | 0.541564 | 0.734158 | 0.871228 | 0.185056 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.666433 | 0.524821 | 0.0150839 | 0.172794 | 0.758865 | 0.755083 | 0.00378251 | 0.125899 | 0.5632 | 0.764797 | 0.887069 | 0.175193 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.64629 | 0.508341 | 0.0378866 | 0.165576 | 0.776723 | 0.780942 | -0.00421941 | 0.127416 | 0.565244 | 0.771262 | 0.889852 | 0.173172 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.650843 | 0.524396 | 0.0414829 | 0.17145 | 0.770213 | 0.762029 | 0.00818331 | 0.135171 | 0.55167 | 0.76217 | 0.900002 | 0.172917 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | -1.84944 | 0.735727 | -3.9508 | -3.06585 | -2.35412 | -1.88855 | -1.32321 | -0.588016 | 0.0522366 |
| player | theta_2 | 1167 | -1.60875 | 0.609336 | -3.68332 | -2.73109 | -2.01009 | -1.56811 | -1.1757 | -0.677859 | -0.3016 |
| player | theta_3 | 1167 | -1.15314 | 0.968891 | -4.06204 | -2.95448 | -1.93251 | -0.745435 | -0.326237 | -0.113464 | 0.505253 |
| player | alpha_1 | 1167 | -0.79881 | 0.681786 | -3.09993 | -2.04141 | -1.19935 | -0.744789 | -0.368334 | 0.239751 | 1.44011 |
| player | alpha_2 | 1167 | -0.488467 | 0.933081 | -3.15124 | -2.04087 | -1.0385 | -0.553381 | 0.00309176 | 1.30831 | 2.55256 |
| player | alpha_3 | 1167 | 0.166798 | 1.13063 | -3.06541 | -2.05613 | -0.537944 | 0.373349 | 0.88227 | 1.7893 | 3.12943 |
| player | beta_1 | 1167 | -2.07668 | 1.02473 | -5.61939 | -4.08386 | -2.63145 | -1.97423 | -1.37394 | -0.595026 | -0.0770898 |
| player | beta_2 | 1167 | -1.7708 | 0.693339 | -3.97966 | -3.06218 | -2.20504 | -1.72098 | -1.25982 | -0.729597 | -0.416349 |
| player | beta_3 | 1167 | -1.40551 | 1.30318 | -5.55433 | -3.9788 | -2.3354 | -0.797215 | -0.337641 | -0.12165 | 0.199731 |
| player | theta_norm | 1167 | 2.90852 | 0.853876 | 0.901915 | 1.52919 | 2.27332 | 2.9052 | 3.46621 | 4.39508 | 5.31612 |
| tossup | start_difficulty_d1 | 1220 | -2.21822 | 0.986157 | -4.34863 | -3.76327 | -2.97177 | -2.23976 | -1.51206 | -0.506592 | 0.242653 |
| tossup | start_difficulty_d2 | 1220 | -1.27112 | 1.42929 | -4.61509 | -3.73667 | -2.63228 | -0.714512 | -0.044862 | 0.403148 | 0.929686 |
| tossup | start_difficulty_d3 | 1220 | -1.00693 | 1.19873 | -3.86129 | -3.0502 | -2.02744 | -0.735339 | 0.0557795 | 0.536007 | 0.950784 |
| tossup | end_difficulty_d1 | 1220 | -3.03952 | 0.9442 | -5.47895 | -4.40016 | -3.78334 | -3.13038 | -2.36935 | -1.3702 | -0.522855 |
| tossup | end_difficulty_d2 | 1220 | -2.28489 | 1.32337 | -8.19481 | -4.38029 | -3.40597 | -2.16061 | -1.07027 | -0.52088 | 0.0476785 |
| tossup | end_difficulty_d3 | 1220 | -2.17682 | 1.3903 | -11.0147 | -4.56212 | -3.13115 | -1.95648 | -1.01251 | -0.450178 | -0.0178265 |
| tossup | total_drop_d1 | 1220 | 0.821305 | 0.243074 | 0.299147 | 0.445898 | 0.676912 | 0.833371 | 0.945627 | 1.20149 | 2.29551 |
| tossup | total_drop_d2 | 1220 | 1.01377 | 0.517112 | 0.314388 | 0.43588 | 0.77757 | 0.962123 | 1.13976 | 1.79378 | 9.00821 |
| tossup | total_drop_d3 | 1220 | 1.16989 | 0.674205 | 0.547881 | 0.732161 | 0.901293 | 1.01514 | 1.1621 | 2.09421 | 9.18822 |
| tossup | drop_share_1_d1 | 1220 | 0.341414 | 0.0257318 | 0.25335 | 0.303544 | 0.323847 | 0.339314 | 0.355816 | 0.385436 | 0.45596 |
| tossup | drop_share_2_d1 | 1220 | 0.326127 | 0.0161877 | 0.27233 | 0.295339 | 0.316388 | 0.328525 | 0.338189 | 0.348208 | 0.366572 |
| tossup | drop_share_3_d1 | 1220 | 0.332459 | 0.0250577 | 0.244079 | 0.292444 | 0.316324 | 0.331356 | 0.346852 | 0.372805 | 0.447362 |
| tossup | drop_share_1_d2 | 1220 | 0.315395 | 0.033579 | 0.0841148 | 0.271294 | 0.297576 | 0.309642 | 0.330992 | 0.375494 | 0.46368 |
| tossup | drop_share_2_d2 | 1220 | 0.338112 | 0.0240069 | 0.269835 | 0.293035 | 0.32508 | 0.341586 | 0.353455 | 0.370979 | 0.424035 |
| tossup | drop_share_3_d2 | 1220 | 0.346493 | 0.0307338 | 0.238804 | 0.298405 | 0.330349 | 0.346317 | 0.359484 | 0.401874 | 0.631803 |
| tossup | drop_share_1_d3 | 1220 | 0.320873 | 0.0304441 | 0.178496 | 0.282335 | 0.300292 | 0.317792 | 0.340086 | 0.37404 | 0.431771 |
| tossup | drop_share_2_d3 | 1220 | 0.345936 | 0.0208641 | 0.300807 | 0.319118 | 0.333991 | 0.344458 | 0.354402 | 0.373588 | 0.502786 |
| tossup | drop_share_3_d3 | 1220 | 0.333191 | 0.0250439 | 0.207744 | 0.287552 | 0.319661 | 0.337351 | 0.350071 | 0.364751 | 0.503949 |
| tossup | r_1 | 1220 | 0.457716 | 0.258178 | 0.0373713 | 0.0652518 | 0.221415 | 0.46761 | 0.682764 | 0.840247 | 0.908428 |
| tossup | r_2 | 1220 | 0.282805 | 0.27687 | 0.0396316 | 0.0544262 | 0.0842038 | 0.158061 | 0.306488 | 0.844144 | 0.932772 |
| tossup | r_3 | 1220 | 0.259478 | 0.230253 | 0.0132665 | 0.0313652 | 0.0660828 | 0.148307 | 0.425769 | 0.715664 | 0.832501 |
| tossup | r_norm | 1220 | 0.739239 | 0.0806943 | 0.578255 | 0.614526 | 0.669165 | 0.736891 | 0.805227 | 0.870739 | 0.933998 |
