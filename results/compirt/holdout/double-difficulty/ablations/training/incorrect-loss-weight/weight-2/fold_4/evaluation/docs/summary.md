# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-2/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-2/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 291297 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.721968 |
| log_loss | 0.517113 |
| ece | 0.119682 |
| brier | 0.170865 |
| accuracy | 0.753398 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0199569 |
| probability_std | 0.189061 |
| probability_p10 | 0.379165 |
| probability_p50 | 0.685702 |
| probability_p90 | 0.875487 |
| mean_predictive_variance | 0.190641 |
| integrated_brier_score | 0.10125 |
| joint_tossup_event_log_loss | 6.64564 |
| buzz_position_mae | 0.150678 |
| buzz_position_median_absolute_error | 0.133454 |
| buzz_position_bias | -0.043339 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.349946 |
| first_buzzer_mean_reciprocal_rank | 0.561904 |
| first_buzzer_log_loss | 1.68465 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.721968 |
| neg_average_precision | 0.451556 |
| neg_precision | 0.451494 |
| neg_recall | 0.409805 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.185394 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0134811 |
| no_buzz_calibration_error | 0.00175403 |
| no_buzz_brier | 0.0110436 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.721968 | 0.517113 | 0.119682 | 0.170865 | 0.753398 | 0.773355 | -0.0199569 | 0.189061 | 0.379165 | 0.685702 | 0.875487 | 0.190641 |
| tossup_correctness | tier | fall | 2876 | 0.723498 | 0.496419 | 0.119125 | 0.162444 | 0.770167 | 0.793115 | -0.0229485 | 0.188239 | 0.395763 | 0.706805 | 0.890027 | 0.184293 |
| tossup_correctness | tier | nationals | 1579 | 0.714896 | 0.54949 | 0.0977313 | 0.184342 | 0.726409 | 0.729576 | -0.00316656 | 0.198135 | 0.347255 | 0.664184 | 0.866376 | 0.193314 |
| tossup_correctness | tier | regionals | 1990 | 0.734949 | 0.522796 | 0.12831 | 0.173354 | 0.747236 | 0.765829 | -0.018593 | 0.186672 | 0.365219 | 0.663099 | 0.860099 | 0.196242 |
| tossup_correctness | tier | winter | 2825 | 0.711404 | 0.516079 | 0.126536 | 0.170152 | 0.755752 | 0.783009 | -0.0272566 | 0.183994 | 0.398588 | 0.685886 | 0.874131 | 0.191662 |
| tossup_correctness | category | Current Events | 123 | 0.746882 | 0.526816 | 0.15134 | 0.178321 | 0.731707 | 0.764228 | -0.0325203 | 0.191969 | 0.369229 | 0.59437 | 0.876883 | 0.199688 |
| tossup_correctness | category | Fine Arts | 1093 | 0.736533 | 0.500488 | 0.105072 | 0.163324 | 0.773102 | 0.769442 | 0.00365965 | 0.188965 | 0.396303 | 0.699425 | 0.881736 | 0.187226 |
| tossup_correctness | category | Geography | 191 | 0.789676 | 0.535152 | 0.128393 | 0.178145 | 0.743455 | 0.691099 | 0.052356 | 0.225605 | 0.273981 | 0.608586 | 0.826452 | 0.194363 |
| tossup_correctness | category | History | 1469 | 0.712881 | 0.532389 | 0.10509 | 0.177995 | 0.734513 | 0.758339 | -0.0238257 | 0.194204 | 0.373395 | 0.683918 | 0.883289 | 0.1888 |
| tossup_correctness | category | Literature | 1436 | 0.701273 | 0.477534 | 0.112486 | 0.153515 | 0.791783 | 0.81546 | -0.0236769 | 0.171961 | 0.449757 | 0.745422 | 0.891985 | 0.179231 |
| tossup_correctness | category | Mythology | 325 | 0.687205 | 0.476414 | 0.151516 | 0.152807 | 0.790769 | 0.843077 | -0.0523077 | 0.153165 | 0.481546 | 0.707279 | 0.873778 | 0.189845 |
| tossup_correctness | category | Other Academic | 67 | 0.708895 | 0.563427 | 0.18709 | 0.190598 | 0.716418 | 0.791045 | -0.0746269 | 0.180355 | 0.372834 | 0.613839 | 0.83742 | 0.206665 |
| tossup_correctness | category | Philosophy | 322 | 0.672681 | 0.532371 | 0.121624 | 0.178494 | 0.723602 | 0.785714 | -0.0621118 | 0.18109 | 0.420667 | 0.686248 | 0.906798 | 0.187725 |
| tossup_correctness | category | Popular Culture | 100 | 0.545455 | 0.425326 | 0.143023 | 0.129521 | 0.87 | 0.89 | -0.02 | 0.106039 | 0.611516 | 0.761024 | 0.876293 | 0.177758 |
| tossup_correctness | category | Religion | 365 | 0.656616 | 0.586321 | 0.101808 | 0.200953 | 0.682192 | 0.723288 | -0.0410959 | 0.192695 | 0.36151 | 0.664751 | 0.867471 | 0.195667 |
| tossup_correctness | category | Science | 1456 | 0.725717 | 0.529046 | 0.133098 | 0.175601 | 0.745192 | 0.76717 | -0.021978 | 0.190021 | 0.358917 | 0.666152 | 0.860739 | 0.195917 |
| tossup_correctness | category | Social Science | 333 | 0.740375 | 0.54224 | 0.131255 | 0.182184 | 0.735736 | 0.72973 | 0.00600601 | 0.207884 | 0.298846 | 0.637731 | 0.859011 | 0.195885 |
| tossup_correctness | category | Unknown | 1990 | 0.734949 | 0.522796 | 0.12831 | 0.173354 | 0.747236 | 0.765829 | -0.018593 | 0.186672 | 0.365219 | 0.663099 | 0.860099 | 0.196242 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.747927 | 0.545678 | 0.152358 | 0.183758 | 0.73743 | 0.748603 | -0.0111732 | 0.192745 | 0.333358 | 0.630872 | 0.825746 | 0.203477 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.699817 | 0.545657 | 0.121522 | 0.183041 | 0.735632 | 0.754441 | -0.0188088 | 0.187188 | 0.356587 | 0.654645 | 0.859767 | 0.19711 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.723225 | 0.518634 | 0.110767 | 0.171755 | 0.747163 | 0.766682 | -0.0195188 | 0.187722 | 0.384177 | 0.688118 | 0.874025 | 0.190451 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.710356 | 0.503717 | 0.116506 | 0.164911 | 0.771659 | 0.787441 | -0.0157824 | 0.179208 | 0.420885 | 0.701147 | 0.878675 | 0.188665 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.735359 | 0.518505 | 0.127216 | 0.171479 | 0.74636 | 0.771758 | -0.0253979 | 0.19801 | 0.349198 | 0.677955 | 0.876481 | 0.1899 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 2.68567 | 0.76669 | 0.389793 | 1.42622 | 2.16723 | 2.68477 | 3.1986 | 4.02812 | 4.69137 |
| player | theta_1 | 1196 | -1.22687 | 0.90932 | -3.687 | -2.61922 | -1.8268 | -1.28271 | -0.702333 | 0.386277 | 2.33078 |
| player | theta_2 | 1196 | -1.02764 | 0.735201 | -3.4586 | -2.28186 | -1.48597 | -1.00402 | -0.560609 | 0.161557 | 1.60693 |
| player | theta_3 | 1196 | -1.12744 | 0.805526 | -3.76993 | -2.38521 | -1.64672 | -1.17842 | -0.662377 | 0.320766 | 2.0823 |
| player | theta_norm | 1196 | 2.31445 | 0.700467 | 0.0978726 | 1.2458 | 1.81156 | 2.26644 | 2.76758 | 3.49272 | 4.53629 |
| tossup | start_difficulty_d1 | 1240 | -1.11468 | 0.628778 | -3.40222 | -2.03781 | -1.5213 | -1.14324 | -0.775802 | 0.0172463 | 2.18035 |
| tossup | start_difficulty_d2 | 1240 | -1.09799 | 0.577589 | -3.21575 | -1.98267 | -1.48269 | -1.11703 | -0.729446 | -0.109444 | 0.856901 |
| tossup | start_difficulty_d3 | 1240 | -1.09804 | 0.576102 | -3.4918 | -2.01175 | -1.49619 | -1.12199 | -0.730924 | -0.112664 | 1.46794 |
| tossup | end_difficulty_d1 | 1240 | -2.10938 | 0.729501 | -4.55702 | -3.20541 | -2.58948 | -2.15042 | -1.69541 | -0.838128 | 1.50759 |
| tossup | end_difficulty_d2 | 1240 | -2.0864 | 0.679822 | -4.63386 | -3.16937 | -2.52761 | -2.09245 | -1.65554 | -0.934916 | 0.169953 |
| tossup | end_difficulty_d3 | 1240 | -2.08526 | 0.672936 | -4.92637 | -3.19026 | -2.54098 | -2.10093 | -1.66603 | -0.97077 | 0.813432 |
| tossup | total_drop_d1 | 1240 | 0.994699 | 0.164697 | 0.582674 | 0.759534 | 0.898987 | 0.986942 | 1.0716 | 1.23147 | 3.73392 |
| tossup | total_drop_d2 | 1240 | 0.988408 | 0.13538 | 0.560231 | 0.779422 | 0.905156 | 0.982779 | 1.06049 | 1.20729 | 2.48232 |
| tossup | total_drop_d3 | 1240 | 0.987221 | 0.127234 | 0.654504 | 0.790384 | 0.903041 | 0.979208 | 1.06012 | 1.20917 | 1.6943 |
| tossup | drop_share_1_d1 | 1240 | 0.302481 | 0.0201491 | 0.137964 | 0.271766 | 0.292069 | 0.303611 | 0.31535 | 0.331586 | 0.380785 |
| tossup | drop_share_2_d1 | 1240 | 0.347282 | 0.0136388 | 0.295887 | 0.326892 | 0.338868 | 0.347186 | 0.35528 | 0.367176 | 0.543319 |
| tossup | drop_share_3_d1 | 1240 | 0.350238 | 0.0211145 | 0.291456 | 0.318698 | 0.336737 | 0.349128 | 0.361672 | 0.384976 | 0.49294 |
| tossup | drop_share_1_d2 | 1240 | 0.302453 | 0.0174598 | 0.15282 | 0.274309 | 0.292534 | 0.302862 | 0.31359 | 0.32984 | 0.366475 |
| tossup | drop_share_2_d2 | 1240 | 0.346945 | 0.0121103 | 0.307159 | 0.327398 | 0.338624 | 0.346766 | 0.354927 | 0.366928 | 0.395275 |
| tossup | drop_share_3_d2 | 1240 | 0.350602 | 0.0188053 | 0.293171 | 0.321611 | 0.33806 | 0.350328 | 0.360882 | 0.382774 | 0.508334 |
| tossup | drop_share_1_d3 | 1240 | 0.302202 | 0.0181568 | 0.203186 | 0.27348 | 0.292372 | 0.302531 | 0.313764 | 0.329378 | 0.379201 |
| tossup | drop_share_2_d3 | 1240 | 0.347085 | 0.0118054 | 0.3026 | 0.327475 | 0.339582 | 0.347113 | 0.354666 | 0.366393 | 0.386963 |
| tossup | drop_share_3_d3 | 1240 | 0.350713 | 0.0193478 | 0.2922 | 0.322026 | 0.338129 | 0.350067 | 0.36147 | 0.382983 | 0.486253 |
| tossup | r_1 | 1240 | 0.337316 | 0.195975 | 0.0453365 | 0.0896745 | 0.1746 | 0.291994 | 0.470834 | 0.70466 | 0.869798 |
| tossup | r_2 | 1240 | 0.330582 | 0.172078 | 0.039552 | 0.106585 | 0.195815 | 0.304088 | 0.43608 | 0.677858 | 0.878253 |
| tossup | r_3 | 1240 | 0.332102 | 0.175026 | 0.065614 | 0.107184 | 0.191704 | 0.303482 | 0.435448 | 0.672294 | 0.905499 |
| tossup | r_norm | 1240 | 0.654063 | 0.0642989 | 0.577455 | 0.581928 | 0.603175 | 0.638283 | 0.687314 | 0.781086 | 0.908026 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.46984 | 0.493797 | 1.78541 | 3.74795 | 4.20607 | 4.42471 | 4.68813 | 5.39817 | 6.38357 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.45649 | 0.43659 | 2.03956 | 3.79488 | 4.22392 | 4.42549 | 4.66793 | 5.21314 | 6.64069 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.45442 | 0.434463 | 2.52815 | 3.75901 | 4.21586 | 4.42259 | 4.70342 | 5.18791 | 6.21787 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.76784 | 2.33254 | -12.0125 | -3.12028 | 0.702322 | 2.9336 | 3.31706 | 3.64178 | 4.3834 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.27415 | 2.06811 | -9.50151 | -2.67137 | 2.39297 | 3.13668 | 3.36948 | 3.69613 | 4.27941 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.14964 | 2.0974 | -10.5064 | -2.37624 | 1.84788 | 3.08416 | 3.36122 | 3.73421 | 4.2584 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.702 | 2.50059 | 0.859917 | 0.981319 | 1.05271 | 1.26463 | 4.01548 | 7.80844 | 16.783 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.18234 | 2.24052 | 0.899109 | 0.958561 | 1.02172 | 1.16379 | 1.88475 | 7.39428 | 14.3547 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.30478 | 2.23004 | 0.850515 | 0.967624 | 1.02551 | 1.17062 | 2.57389 | 7.21917 | 14.9303 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.238451 | 0.0807832 | 0.0360578 | 0.0837131 | 0.180351 | 0.274154 | 0.293897 | 0.3161 | 0.552253 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.342482 | 0.0760733 | 0.0548218 | 0.17827 | 0.336292 | 0.351002 | 0.36497 | 0.449872 | 0.690255 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.419067 | 0.130346 | 0.119365 | 0.297005 | 0.348248 | 0.368223 | 0.433399 | 0.733871 | 0.902255 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.252575 | 0.0716479 | 0.0307894 | 0.0895404 | 0.235287 | 0.280152 | 0.297066 | 0.315318 | 0.662353 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.346515 | 0.0616932 | 0.0603777 | 0.221554 | 0.340069 | 0.350472 | 0.362381 | 0.413847 | 0.679006 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.40091 | 0.108176 | 0.092401 | 0.320743 | 0.349043 | 0.365418 | 0.398772 | 0.678376 | 0.896356 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.249246 | 0.0714514 | 0.038881 | 0.0927009 | 0.224305 | 0.277969 | 0.29689 | 0.315741 | 0.561753 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.348784 | 0.061566 | 0.0825207 | 0.234987 | 0.338147 | 0.350582 | 0.363927 | 0.436549 | 0.716726 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.40197 | 0.107947 | 0.0744995 | 0.316383 | 0.348687 | 0.366271 | 0.405845 | 0.659906 | 0.877664 |
| tossup_hazard | hazard_r_1 | 1240 | 0.377967 | 0.28329 | 0.0309204 | 0.0623801 | 0.130615 | 0.263565 | 0.625844 | 0.878543 | 0.950056 |
| tossup_hazard | hazard_r_2 | 1240 | 0.29488 | 0.222809 | 0.0238247 | 0.0546859 | 0.116476 | 0.211161 | 0.45278 | 0.734111 | 0.879398 |
| tossup_hazard | hazard_r_3 | 1240 | 0.327153 | 0.248909 | 0.026119 | 0.0517514 | 0.115749 | 0.232894 | 0.539415 | 0.776367 | 0.926115 |
