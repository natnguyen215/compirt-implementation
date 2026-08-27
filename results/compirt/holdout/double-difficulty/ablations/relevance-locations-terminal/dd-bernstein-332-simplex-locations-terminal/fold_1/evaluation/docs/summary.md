# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 283993 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.709354 |
| log_loss | 0.497356 |
| ece | 0.0158633 |
| brier | 0.161796 |
| accuracy | 0.773342 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0112174 |
| probability_std | 0.143637 |
| probability_p10 | 0.574783 |
| probability_p50 | 0.812538 |
| probability_p90 | 0.920443 |
| mean_predictive_variance | 0.153529 |
| integrated_brier_score | 0.100668 |
| joint_tossup_event_log_loss | 6.60058 |
| buzz_position_mae | 0.151074 |
| buzz_position_median_absolute_error | 0.133607 |
| buzz_position_bias | -0.0475397 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.351479 |
| first_buzzer_mean_reciprocal_rank | 0.564805 |
| first_buzzer_log_loss | 1.67763 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.709354 |
| neg_average_precision | 0.445715 |
| neg_precision | 0.595149 |
| neg_recall | 0.14748 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.190544 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0149294 |
| no_buzz_calibration_error | -0.000979641 |
| no_buzz_brier | 0.0154922 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.709354 | 0.497356 | 0.0158633 | 0.161796 | 0.773342 | 0.762125 | 0.0112174 | 0.143637 | 0.574783 | 0.812538 | 0.920443 | 0.153529 |
| tossup_correctness | tier | fall | 2842 | 0.729304 | 0.463707 | 0.0133547 | 0.149024 | 0.79064 | 0.785362 | 0.00527797 | 0.140657 | 0.587005 | 0.826202 | 0.928686 | 0.148115 |
| tossup_correctness | tier | nationals | 1564 | 0.713781 | 0.540469 | 0.0461838 | 0.179767 | 0.741688 | 0.718031 | 0.0236573 | 0.145415 | 0.559773 | 0.800118 | 0.913511 | 0.159661 |
| tossup_correctness | tier | regionals | 1937 | 0.686238 | 0.513301 | 0.0227995 | 0.167633 | 0.765101 | 0.758389 | 0.00671141 | 0.138811 | 0.580497 | 0.808627 | 0.914791 | 0.156106 |
| tossup_correctness | tier | winter | 2750 | 0.699462 | 0.49638 | 0.0187113 | 0.160662 | 0.779273 | 0.765818 | 0.0134545 | 0.148149 | 0.567719 | 0.811691 | 0.919636 | 0.15382 |
| tossup_correctness | category | Current Events | 126 | 0.719517 | 0.491915 | 0.0680989 | 0.160134 | 0.769841 | 0.769841 | 0 | 0.127837 | 0.549436 | 0.764478 | 0.883804 | 0.174782 |
| tossup_correctness | category | Fine Arts | 1071 | 0.750857 | 0.468332 | 0.0241176 | 0.151362 | 0.786181 | 0.766573 | 0.0196078 | 0.155742 | 0.541329 | 0.810335 | 0.924213 | 0.153914 |
| tossup_correctness | category | Geography | 185 | 0.796373 | 0.495358 | 0.0755367 | 0.16233 | 0.745946 | 0.697297 | 0.0486486 | 0.21797 | 0.366029 | 0.756592 | 0.894109 | 0.168053 |
| tossup_correctness | category | History | 1440 | 0.707533 | 0.511356 | 0.0293542 | 0.167925 | 0.761806 | 0.754167 | 0.00763889 | 0.140512 | 0.581962 | 0.816186 | 0.9262 | 0.151584 |
| tossup_correctness | category | Literature | 1422 | 0.678024 | 0.45134 | 0.0142181 | 0.14224 | 0.811533 | 0.814346 | -0.00281294 | 0.123411 | 0.638715 | 0.839088 | 0.930963 | 0.140028 |
| tossup_correctness | category | Mythology | 318 | 0.664447 | 0.482555 | 0.0323433 | 0.152076 | 0.805031 | 0.789308 | 0.0157233 | 0.122624 | 0.643023 | 0.830822 | 0.928125 | 0.143917 |
| tossup_correctness | category | Other Academic | 66 | 0.805151 | 0.520361 | 0.173253 | 0.176041 | 0.727273 | 0.712121 | 0.0151515 | 0.136231 | 0.581755 | 0.797922 | 0.889423 | 0.161188 |
| tossup_correctness | category | Philosophy | 311 | 0.724192 | 0.509559 | 0.0927118 | 0.169767 | 0.742765 | 0.745981 | -0.00321543 | 0.130954 | 0.609174 | 0.815753 | 0.916921 | 0.152891 |
| tossup_correctness | category | Popular Culture | 102 | 0.52037 | 0.37793 | 0.0500011 | 0.107785 | 0.882353 | 0.882353 | 0 | 0.0694975 | 0.755476 | 0.852117 | 0.915522 | 0.129098 |
| tossup_correctness | category | Religion | 358 | 0.714144 | 0.541442 | 0.032533 | 0.180104 | 0.740223 | 0.712291 | 0.027933 | 0.154635 | 0.498876 | 0.784558 | 0.899742 | 0.170124 |
| tossup_correctness | category | Science | 1433 | 0.695014 | 0.528616 | 0.0353074 | 0.174348 | 0.757153 | 0.738311 | 0.0188416 | 0.145559 | 0.553374 | 0.802433 | 0.91715 | 0.158777 |
| tossup_correctness | category | Social Science | 324 | 0.776226 | 0.489719 | 0.0562862 | 0.160548 | 0.762346 | 0.731481 | 0.0308642 | 0.155249 | 0.505512 | 0.796179 | 0.899671 | 0.162807 |
| tossup_correctness | category | Unknown | 1937 | 0.686238 | 0.513301 | 0.0227995 | 0.167633 | 0.765101 | 0.758389 | 0.00671141 | 0.138811 | 0.580497 | 0.808627 | 0.914791 | 0.156106 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.618172 | 0.603778 | 0.0771567 | 0.203809 | 0.676647 | 0.712575 | -0.0359281 | 0.135175 | 0.558892 | 0.778001 | 0.886588 | 0.17221 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.722042 | 0.521383 | 0.0233649 | 0.172825 | 0.743421 | 0.729167 | 0.0142544 | 0.157685 | 0.514454 | 0.782088 | 0.905778 | 0.165013 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.714156 | 0.502459 | 0.0280159 | 0.163885 | 0.77305 | 0.755083 | 0.0179669 | 0.136074 | 0.600602 | 0.813913 | 0.91921 | 0.152265 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.693222 | 0.484155 | 0.0171101 | 0.155662 | 0.78903 | 0.780942 | 0.0080872 | 0.127955 | 0.61592 | 0.825027 | 0.92206 | 0.14827 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.717758 | 0.493123 | 0.0117173 | 0.16047 | 0.773159 | 0.762029 | 0.0111293 | 0.155662 | 0.534279 | 0.809327 | 0.924299 | 0.154848 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 2.68588 | 0.738872 | 0.515438 | 1.50939 | 2.18334 | 2.68124 | 3.18321 | 3.95855 | 4.66587 |
| player | theta_1 | 1167 | -1.23755 | 0.828455 | -3.60346 | -2.51166 | -1.77853 | -1.309 | -0.73218 | 0.20854 | 1.51995 |
| player | theta_2 | 1167 | -1.01858 | 0.70861 | -3.45667 | -2.09905 | -1.46352 | -1.06568 | -0.603077 | 0.24774 | 1.84555 |
| player | theta_3 | 1167 | -1.05633 | 0.762749 | -3.34424 | -2.20291 | -1.54237 | -1.09128 | -0.621714 | 0.349716 | 1.88352 |
| player | theta_norm | 1167 | 2.25565 | 0.604959 | 0.403746 | 1.32737 | 1.85039 | 2.22749 | 2.62996 | 3.31431 | 4.26615 |
| tossup | start_difficulty_d1 | 1220 | -1.79072 | 0.549117 | -3.31974 | -2.55648 | -2.17651 | -1.83657 | -1.47973 | -0.886201 | 1.2724 |
| tossup | start_difficulty_d2 | 1220 | -1.77932 | 0.516945 | -3.40049 | -2.55109 | -2.15102 | -1.81964 | -1.44973 | -0.844666 | 0.217714 |
| tossup | start_difficulty_d3 | 1220 | -1.77599 | 0.510714 | -3.60249 | -2.5394 | -2.14898 | -1.79461 | -1.44449 | -0.902741 | 0.17774 |
| tossup | end_difficulty_d1 | 1220 | -2.77964 | 0.640429 | -4.6202 | -3.70177 | -3.21144 | -2.82717 | -2.39687 | -1.73905 | 0.609622 |
| tossup | end_difficulty_d2 | 1220 | -2.76628 | 0.604044 | -4.78196 | -3.6823 | -3.19679 | -2.80266 | -2.38425 | -1.69083 | -0.516752 |
| tossup | end_difficulty_d3 | 1220 | -2.76003 | 0.594924 | -4.88839 | -3.67827 | -3.18695 | -2.77511 | -2.37614 | -1.76986 | -0.522538 |
| tossup | total_drop_d1 | 1220 | 0.988922 | 0.111986 | 0.624589 | 0.802726 | 0.913758 | 0.991964 | 1.06379 | 1.16122 | 1.33997 |
| tossup | total_drop_d2 | 1220 | 0.986966 | 0.104204 | 0.665061 | 0.820107 | 0.917603 | 0.985695 | 1.05161 | 1.16231 | 1.38147 |
| tossup | total_drop_d3 | 1220 | 0.984041 | 0.102146 | 0.685115 | 0.819858 | 0.91242 | 0.983267 | 1.05178 | 1.15766 | 1.32043 |
| tossup | drop_share_1_d1 | 1220 | 0.304106 | 0.0154845 | 0.220762 | 0.279362 | 0.294596 | 0.304337 | 0.31463 | 0.32783 | 0.357833 |
| tossup | drop_share_2_d1 | 1220 | 0.347152 | 0.0113349 | 0.311752 | 0.327951 | 0.339767 | 0.347364 | 0.355123 | 0.364911 | 0.386627 |
| tossup | drop_share_3_d1 | 1220 | 0.348742 | 0.0163934 | 0.295892 | 0.322773 | 0.337545 | 0.348525 | 0.358987 | 0.375528 | 0.429702 |
| tossup | drop_share_1_d2 | 1220 | 0.303555 | 0.0143673 | 0.25754 | 0.278943 | 0.294115 | 0.304152 | 0.312866 | 0.327382 | 0.347154 |
| tossup | drop_share_2_d2 | 1220 | 0.346872 | 0.0114148 | 0.310522 | 0.328033 | 0.339148 | 0.346742 | 0.354458 | 0.365047 | 0.390108 |
| tossup | drop_share_3_d2 | 1220 | 0.349573 | 0.0154544 | 0.300024 | 0.325642 | 0.339361 | 0.349281 | 0.35933 | 0.374644 | 0.417501 |
| tossup | drop_share_1_d3 | 1220 | 0.303477 | 0.0149033 | 0.240044 | 0.279357 | 0.29427 | 0.303911 | 0.313536 | 0.327119 | 0.358065 |
| tossup | drop_share_2_d3 | 1220 | 0.347094 | 0.011154 | 0.311024 | 0.328746 | 0.339839 | 0.346856 | 0.354244 | 0.365789 | 0.383462 |
| tossup | drop_share_3_d3 | 1220 | 0.349429 | 0.0156498 | 0.308769 | 0.325755 | 0.338733 | 0.348949 | 0.358951 | 0.376818 | 0.417824 |
| tossup | r_1 | 1220 | 0.322701 | 0.143703 | 0.0643321 | 0.136115 | 0.212698 | 0.295478 | 0.409219 | 0.590879 | 0.844823 |
| tossup | r_2 | 1220 | 0.337141 | 0.122153 | 0.0560306 | 0.152551 | 0.253321 | 0.328094 | 0.409232 | 0.554065 | 0.813156 |
| tossup | r_3 | 1220 | 0.340158 | 0.123451 | 0.0729776 | 0.155356 | 0.254906 | 0.328608 | 0.411059 | 0.565547 | 0.774809 |
| tossup | r_norm | 1220 | 0.618324 | 0.0442215 | 0.577388 | 0.579056 | 0.588377 | 0.603264 | 0.630701 | 0.717081 | 0.851931 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 4.51248 | 0.48404 | 1.79144 | 3.79909 | 4.22351 | 4.45568 | 4.7662 | 5.40154 | 6.38814 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 4.44548 | 0.426477 | 1.95797 | 3.7713 | 4.21622 | 4.42431 | 4.64758 | 5.17745 | 6.56915 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 4.46211 | 0.416987 | 2.17932 | 3.80131 | 4.23231 | 4.45469 | 4.68284 | 5.18535 | 6.04583 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | 1.70904 | 2.29855 | -10.9299 | -3.25729 | 0.675219 | 2.80763 | 3.2903 | 3.65464 | 4.42524 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | 2.16854 | 2.15175 | -9.5243 | -2.51397 | 2.14213 | 3.11569 | 3.3746 | 3.70388 | 4.08037 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | 2.2901 | 2.13877 | -9.28561 | -2.8421 | 2.40676 | 3.18813 | 3.42992 | 3.74334 | 4.44013 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 2.80344 | 2.47416 | 0.908228 | 0.984378 | 1.05497 | 1.41832 | 4.06954 | 8.13934 | 15.5103 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 2.27694 | 2.29563 | 0.90158 | 0.963941 | 1.02844 | 1.1735 | 2.03567 | 7.41595 | 14.0698 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 2.17201 | 2.25482 | 0.870295 | 0.969089 | 1.02309 | 1.15181 | 1.79806 | 7.54545 | 13.8608 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.231756 | 0.0804534 | 0.0433168 | 0.0826174 | 0.167926 | 0.264828 | 0.293861 | 0.314917 | 0.524888 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.342498 | 0.0770183 | 0.0573133 | 0.175805 | 0.334463 | 0.35126 | 0.366473 | 0.438964 | 0.677509 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.425747 | 0.131067 | 0.111333 | 0.310558 | 0.348675 | 0.372099 | 0.456966 | 0.737351 | 0.89937 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.251254 | 0.071282 | 0.0317585 | 0.0914733 | 0.230964 | 0.279606 | 0.296577 | 0.314043 | 0.534925 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.348049 | 0.0644576 | 0.065785 | 0.226739 | 0.339826 | 0.351052 | 0.364227 | 0.431921 | 0.708429 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.400697 | 0.109345 | 0.0946804 | 0.317793 | 0.350234 | 0.364467 | 0.400988 | 0.670787 | 0.887676 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.254016 | 0.0678616 | 0.0395638 | 0.0927437 | 0.237668 | 0.278752 | 0.296053 | 0.313593 | 0.57278 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.349905 | 0.0554491 | 0.0826945 | 0.252409 | 0.340343 | 0.351297 | 0.363553 | 0.409894 | 0.639199 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.396079 | 0.0990709 | 0.0722479 | 0.322716 | 0.349982 | 0.366638 | 0.395021 | 0.633059 | 0.869846 |
| tossup_hazard | hazard_r_1 | 1220 | 0.399619 | 0.279977 | 0.0328364 | 0.0614474 | 0.128716 | 0.337938 | 0.660887 | 0.859612 | 0.940399 |
| tossup_hazard | hazard_r_2 | 1220 | 0.301392 | 0.229959 | 0.0222999 | 0.0557013 | 0.116701 | 0.211187 | 0.461688 | 0.765412 | 0.888622 |
| tossup_hazard | hazard_r_3 | 1220 | 0.298989 | 0.224939 | 0.0246628 | 0.0522068 | 0.120994 | 0.220496 | 0.442079 | 0.762426 | 0.926744 |
