# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-3/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-3/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 297607 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.709685 |
| log_loss | 0.590703 |
| ece | 0.187329 |
| brier | 0.20248 |
| accuracy | 0.689964 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0742141 |
| probability_std | 0.21318 |
| probability_p10 | 0.272286 |
| probability_p50 | 0.597937 |
| probability_p90 | 0.84918 |
| mean_predictive_variance | 0.198648 |
| integrated_brier_score | 0.102513 |
| joint_tossup_event_log_loss | 6.72128 |
| buzz_position_mae | 0.152093 |
| buzz_position_median_absolute_error | 0.133384 |
| buzz_position_bias | -0.0432934 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.358431 |
| first_buzzer_mean_reciprocal_rank | 0.569125 |
| first_buzzer_log_loss | 1.66558 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.709685 |
| neg_average_precision | 0.447593 |
| neg_precision | 0.394145 |
| neg_recall | 0.585891 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.190318 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.013754 |
| no_buzz_calibration_error | 0.000641 |
| no_buzz_brier | 0.0128588 |
| full_pmf_max_mass_error | 1.11022e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.709685 | 0.590703 | 0.187329 | 0.20248 | 0.689964 | 0.764178 | -0.0742141 | 0.21318 | 0.272286 | 0.597937 | 0.84918 | 0.198648 |
| tossup_correctness | tier | fall | 2798 | 0.73457 | 0.562489 | 0.192961 | 0.190054 | 0.716226 | 0.785204 | -0.0689778 | 0.214066 | 0.281495 | 0.62186 | 0.859618 | 0.195667 |
| tossup_correctness | tier | nationals | 1545 | 0.70607 | 0.619609 | 0.175359 | 0.214991 | 0.658252 | 0.721036 | -0.0627832 | 0.217002 | 0.241283 | 0.553883 | 0.831086 | 0.200824 |
| tossup_correctness | tier | regionals | 2039 | 0.703731 | 0.598925 | 0.192016 | 0.206732 | 0.682688 | 0.762138 | -0.0794507 | 0.211728 | 0.273371 | 0.588541 | 0.846977 | 0.200254 |
| tossup_correctness | tier | winter | 2875 | 0.687638 | 0.596795 | 0.185665 | 0.204835 | 0.686609 | 0.768348 | -0.0817391 | 0.209294 | 0.288219 | 0.600958 | 0.848418 | 0.199242 |
| tossup_correctness | category | Current Events | 129 | 0.709843 | 0.615172 | 0.121424 | 0.215732 | 0.689922 | 0.666667 | 0.0232558 | 0.232818 | 0.230864 | 0.538324 | 0.879632 | 0.193311 |
| tossup_correctness | category | Fine Arts | 1074 | 0.704007 | 0.601852 | 0.209988 | 0.207879 | 0.670391 | 0.776536 | -0.106145 | 0.216603 | 0.271251 | 0.581089 | 0.849063 | 0.198655 |
| tossup_correctness | category | Geography | 180 | 0.741611 | 0.602267 | 0.133889 | 0.208573 | 0.633333 | 0.616667 | 0.0166667 | 0.255175 | 0.0974429 | 0.526547 | 0.826429 | 0.184847 |
| tossup_correctness | category | History | 1454 | 0.694458 | 0.601648 | 0.180218 | 0.207167 | 0.671939 | 0.757909 | -0.0859697 | 0.216014 | 0.263945 | 0.599452 | 0.853998 | 0.19726 |
| tossup_correctness | category | Literature | 1435 | 0.72355 | 0.53019 | 0.186511 | 0.175412 | 0.752613 | 0.810453 | -0.0578397 | 0.202032 | 0.327692 | 0.65257 | 0.868287 | 0.192984 |
| tossup_correctness | category | Mythology | 324 | 0.687613 | 0.55208 | 0.164724 | 0.184985 | 0.743827 | 0.79321 | -0.0493827 | 0.193418 | 0.341026 | 0.659517 | 0.85306 | 0.195534 |
| tossup_correctness | category | Other Academic | 71 | 0.59695 | 0.666524 | 0.255753 | 0.233032 | 0.676056 | 0.760563 | -0.084507 | 0.185324 | 0.320106 | 0.600056 | 0.80516 | 0.211506 |
| tossup_correctness | category | Philosophy | 310 | 0.725378 | 0.577101 | 0.186045 | 0.198006 | 0.687097 | 0.76129 | -0.0741935 | 0.197736 | 0.309551 | 0.570877 | 0.843252 | 0.205238 |
| tossup_correctness | category | Popular Culture | 108 | 0.4375 | 0.519974 | 0.217534 | 0.168744 | 0.805556 | 0.888889 | -0.0833333 | 0.145649 | 0.499404 | 0.684965 | 0.856985 | 0.19666 |
| tossup_correctness | category | Religion | 361 | 0.674691 | 0.666101 | 0.226974 | 0.235917 | 0.614958 | 0.742382 | -0.127424 | 0.201913 | 0.242636 | 0.518826 | 0.78574 | 0.208964 |
| tossup_correctness | category | Science | 1445 | 0.711558 | 0.602916 | 0.183215 | 0.207415 | 0.684429 | 0.746021 | -0.0615917 | 0.209086 | 0.267288 | 0.583373 | 0.825923 | 0.202339 |
| tossup_correctness | category | Social Science | 327 | 0.733626 | 0.624532 | 0.192202 | 0.214968 | 0.657492 | 0.718654 | -0.0611621 | 0.22982 | 0.198254 | 0.537836 | 0.828439 | 0.196354 |
| tossup_correctness | category | Unknown | 2039 | 0.703731 | 0.598925 | 0.192016 | 0.206732 | 0.682688 | 0.762138 | -0.0794507 | 0.211728 | 0.273371 | 0.588541 | 0.846977 | 0.200254 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.667397 | 0.65629 | 0.219727 | 0.231544 | 0.628415 | 0.743169 | -0.114754 | 0.218995 | 0.204571 | 0.54744 | 0.824543 | 0.200854 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.723694 | 0.596868 | 0.168824 | 0.205075 | 0.685864 | 0.728796 | -0.0429319 | 0.216799 | 0.254318 | 0.568815 | 0.839863 | 0.199401 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.722542 | 0.576763 | 0.171224 | 0.196459 | 0.698079 | 0.752568 | -0.0544886 | 0.211988 | 0.273452 | 0.606952 | 0.847154 | 0.19841 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.704748 | 0.570057 | 0.18553 | 0.193885 | 0.70713 | 0.786087 | -0.0789565 | 0.205772 | 0.307816 | 0.622203 | 0.859884 | 0.197546 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.701958 | 0.614888 | 0.20678 | 0.212596 | 0.672546 | 0.764393 | -0.0918469 | 0.21693 | 0.251462 | 0.575566 | 0.839675 | 0.199507 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 2.65765 | 0.789569 | 0.43798 | 1.38089 | 2.11501 | 2.63254 | 3.19524 | 3.98236 | 4.76589 |
| player | theta_1 | 1197 | -1.24205 | 0.974435 | -3.87958 | -2.72377 | -1.87564 | -1.29965 | -0.696123 | 0.506773 | 2.18638 |
| player | theta_2 | 1197 | -1.04689 | 0.804891 | -3.60194 | -2.41459 | -1.56688 | -1.05317 | -0.509552 | 0.27697 | 1.47914 |
| player | theta_3 | 1197 | -1.09992 | 0.844325 | -3.28398 | -2.40556 | -1.65504 | -1.14374 | -0.590932 | 0.386116 | 2.20891 |
| player | theta_norm | 1197 | 2.36394 | 0.754382 | 0.240008 | 1.21612 | 1.84082 | 2.31025 | 2.91395 | 3.65665 | 4.76397 |
| tossup | start_difficulty_d1 | 1240 | -0.740229 | 0.66635 | -3.41693 | -1.72844 | -1.1282 | -0.782557 | -0.37639 | 0.390677 | 2.23474 |
| tossup | start_difficulty_d2 | 1240 | -0.731465 | 0.614981 | -3.24618 | -1.70891 | -1.09318 | -0.749854 | -0.382067 | 0.314144 | 1.71573 |
| tossup | start_difficulty_d3 | 1240 | -0.725438 | 0.612629 | -3.36808 | -1.72771 | -1.08907 | -0.741607 | -0.374789 | 0.351824 | 1.84277 |
| tossup | end_difficulty_d1 | 1240 | -1.73947 | 0.782458 | -4.73028 | -2.95111 | -2.18548 | -1.76423 | -1.30412 | -0.466366 | 1.65064 |
| tossup | end_difficulty_d2 | 1240 | -1.72875 | 0.733232 | -5.0212 | -2.91312 | -2.1506 | -1.74478 | -1.29868 | -0.507341 | 1.1027 |
| tossup | end_difficulty_d3 | 1240 | -1.71438 | 0.714249 | -4.93133 | -2.90837 | -2.13069 | -1.72776 | -1.29447 | -0.510067 | 1.16771 |
| tossup | total_drop_d1 | 1240 | 0.999242 | 0.188695 | 0.559436 | 0.746085 | 0.894255 | 0.987388 | 1.0742 | 1.28651 | 3.20853 |
| tossup | total_drop_d2 | 1240 | 0.997285 | 0.193792 | 0.569922 | 0.77352 | 0.905806 | 0.982068 | 1.06216 | 1.25526 | 5.18004 |
| tossup | total_drop_d3 | 1240 | 0.988939 | 0.14369 | 0.612026 | 0.775877 | 0.895209 | 0.981911 | 1.0584 | 1.23879 | 2.13308 |
| tossup | drop_share_1_d1 | 1240 | 0.301294 | 0.023129 | 0.139521 | 0.266312 | 0.289858 | 0.302254 | 0.315395 | 0.333815 | 0.391386 |
| tossup | drop_share_2_d1 | 1240 | 0.346996 | 0.0135462 | 0.295799 | 0.325321 | 0.338337 | 0.347225 | 0.355141 | 0.367308 | 0.425133 |
| tossup | drop_share_3_d1 | 1240 | 0.35171 | 0.0246515 | 0.276971 | 0.318395 | 0.336934 | 0.350124 | 0.363762 | 0.388888 | 0.520049 |
| tossup | drop_share_1_d2 | 1240 | 0.301369 | 0.0198085 | 0.135764 | 0.271827 | 0.291234 | 0.301997 | 0.313474 | 0.330853 | 0.382591 |
| tossup | drop_share_2_d2 | 1240 | 0.347175 | 0.0140514 | 0.306995 | 0.326896 | 0.338875 | 0.346806 | 0.355507 | 0.369047 | 0.552556 |
| tossup | drop_share_3_d2 | 1240 | 0.351456 | 0.0208427 | 0.273802 | 0.321092 | 0.338571 | 0.351249 | 0.362124 | 0.383 | 0.497977 |
| tossup | drop_share_1_d3 | 1240 | 0.30139 | 0.0200588 | 0.209954 | 0.267676 | 0.290629 | 0.302337 | 0.313826 | 0.331371 | 0.390717 |
| tossup | drop_share_2_d3 | 1240 | 0.347164 | 0.0126433 | 0.299711 | 0.327449 | 0.338561 | 0.346752 | 0.35501 | 0.368891 | 0.401726 |
| tossup | drop_share_3_d3 | 1240 | 0.351447 | 0.0209469 | 0.28327 | 0.319757 | 0.338194 | 0.350514 | 0.362435 | 0.386479 | 0.478893 |
| tossup | r_1 | 1240 | 0.346749 | 0.229719 | 0.0306501 | 0.0715231 | 0.146873 | 0.287788 | 0.537255 | 0.768874 | 0.875493 |
| tossup | r_2 | 1240 | 0.324697 | 0.208986 | 0.0307801 | 0.0809769 | 0.155295 | 0.265173 | 0.461236 | 0.743091 | 0.885118 |
| tossup | r_3 | 1240 | 0.328555 | 0.208713 | 0.0397197 | 0.0836171 | 0.156664 | 0.276203 | 0.460342 | 0.74295 | 0.886008 |
| tossup | r_norm | 1240 | 0.683851 | 0.0765327 | 0.577588 | 0.584708 | 0.622173 | 0.66811 | 0.734277 | 0.83165 | 0.889861 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.47395 | 0.492908 | 2.02667 | 3.71712 | 4.19135 | 4.43274 | 4.70695 | 5.3574 | 6.22668 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.44631 | 0.440336 | 2.12406 | 3.78068 | 4.20584 | 4.41205 | 4.65356 | 5.18502 | 6.72623 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.44085 | 0.42704 | 2.63903 | 3.73859 | 4.21923 | 4.42607 | 4.66062 | 5.2299 | 6.08668 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.76366 | 2.29411 | -11.9236 | -3.16173 | 0.739839 | 2.86155 | 3.3022 | 3.62319 | 4.2416 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.25445 | 1.98716 | -10.3307 | -2.11346 | 2.23247 | 3.06029 | 3.35825 | 3.69225 | 4.19392 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.13805 | 2.2926 | -10.686 | -2.9842 | 2.1724 | 3.12226 | 3.38605 | 3.71191 | 4.15128 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.71028 | 2.45225 | 0.902194 | 0.984681 | 1.06074 | 1.33735 | 3.95893 | 7.9434 | 16.4199 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.19186 | 2.16014 | 0.866138 | 0.961386 | 1.02335 | 1.17955 | 2.03357 | 6.93958 | 15.6466 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.30279 | 2.41988 | 0.874211 | 0.96791 | 1.02769 | 1.16378 | 1.95514 | 7.65614 | 15.3466 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.236086 | 0.0795564 | 0.0439151 | 0.0815556 | 0.181466 | 0.2697 | 0.293702 | 0.315391 | 0.559651 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.343632 | 0.0750286 | 0.0677997 | 0.187098 | 0.335813 | 0.351013 | 0.366114 | 0.439126 | 0.696949 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.420282 | 0.128358 | 0.0974718 | 0.305125 | 0.348459 | 0.369984 | 0.443486 | 0.718365 | 0.882941 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.250769 | 0.0708157 | 0.0279652 | 0.0950326 | 0.227856 | 0.278704 | 0.29609 | 0.315167 | 0.624501 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.347036 | 0.0623663 | 0.065395 | 0.226478 | 0.339577 | 0.350968 | 0.364108 | 0.414973 | 0.699755 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.402195 | 0.108547 | 0.114396 | 0.318793 | 0.349914 | 0.364727 | 0.401379 | 0.672318 | 0.888496 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.252674 | 0.0706304 | 0.03987 | 0.090401 | 0.237273 | 0.278364 | 0.296731 | 0.314096 | 0.572575 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.349183 | 0.0600164 | 0.0890019 | 0.233076 | 0.340369 | 0.351291 | 0.364177 | 0.424256 | 0.692533 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.398143 | 0.105256 | 0.0624271 | 0.319732 | 0.349266 | 0.365629 | 0.395712 | 0.659954 | 0.865569 |
| tossup_hazard | hazard_r_1 | 1240 | 0.387606 | 0.276062 | 0.0311056 | 0.0591551 | 0.135301 | 0.316759 | 0.622189 | 0.867428 | 0.946462 |
| tossup_hazard | hazard_r_2 | 1240 | 0.307529 | 0.217792 | 0.023164 | 0.0512439 | 0.121433 | 0.245875 | 0.47218 | 0.714744 | 0.840445 |
| tossup_hazard | hazard_r_3 | 1240 | 0.304865 | 0.22764 | 0.0261997 | 0.0579325 | 0.119677 | 0.221926 | 0.460606 | 0.757787 | 0.916083 |
