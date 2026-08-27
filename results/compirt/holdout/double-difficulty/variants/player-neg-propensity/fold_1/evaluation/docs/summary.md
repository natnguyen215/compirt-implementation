# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/player-neg-propensity/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/player-neg-propensity/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 283572 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.710264 |
| log_loss | 0.496537 |
| ece | 0.0160277 |
| brier | 0.161333 |
| accuracy | 0.774552 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0124271 |
| probability_std | 0.146847 |
| probability_p10 | 0.571154 |
| probability_p50 | 0.815186 |
| probability_p90 | 0.924707 |
| mean_predictive_variance | 0.151701 |
| integrated_brier_score | 0.100022 |
| joint_tossup_event_log_loss | 6.56931 |
| buzz_position_mae | 0.150432 |
| buzz_position_median_absolute_error | 0.132862 |
| buzz_position_bias | -0.0467924 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.359507 |
| first_buzzer_mean_reciprocal_rank | 0.570719 |
| first_buzzer_log_loss | 1.66321 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.710264 |
| neg_average_precision | 0.451168 |
| neg_precision | 0.602541 |
| neg_recall | 0.153491 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.189999 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0146661 |
| no_buzz_calibration_error | -0.00124302 |
| no_buzz_brier | 0.0150808 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.710264 | 0.496537 | 0.0160277 | 0.161333 | 0.774552 | 0.762125 | 0.0124271 | 0.146847 | 0.571154 | 0.815186 | 0.924707 | 0.151701 |
| tossup_correctness | tier | fall | 2842 | 0.732812 | 0.461941 | 0.0143388 | 0.148386 | 0.795215 | 0.785362 | 0.00985222 | 0.144491 | 0.581295 | 0.826935 | 0.933232 | 0.14655 |
| tossup_correctness | tier | nationals | 1564 | 0.718379 | 0.536442 | 0.0438202 | 0.178104 | 0.73977 | 0.718031 | 0.0217391 | 0.150382 | 0.548898 | 0.796523 | 0.917543 | 0.159688 |
| tossup_correctness | tier | regionals | 1937 | 0.690665 | 0.511384 | 0.0250017 | 0.166873 | 0.762519 | 0.758389 | 0.0041301 | 0.143932 | 0.565301 | 0.812466 | 0.919321 | 0.154209 |
| tossup_correctness | tier | winter | 2750 | 0.691538 | 0.499138 | 0.0206944 | 0.161275 | 0.781455 | 0.765818 | 0.0156364 | 0.148304 | 0.575766 | 0.817547 | 0.923197 | 0.150714 |
| tossup_correctness | category | Current Events | 126 | 0.71134 | 0.491876 | 0.0654061 | 0.159607 | 0.801587 | 0.769841 | 0.031746 | 0.129633 | 0.541204 | 0.756982 | 0.892968 | 0.177564 |
| tossup_correctness | category | Fine Arts | 1071 | 0.747415 | 0.470466 | 0.0174928 | 0.152069 | 0.784314 | 0.766573 | 0.0177404 | 0.156268 | 0.550175 | 0.815548 | 0.928961 | 0.150838 |
| tossup_correctness | category | Geography | 185 | 0.803156 | 0.492451 | 0.0736699 | 0.161172 | 0.756757 | 0.697297 | 0.0594595 | 0.215818 | 0.305555 | 0.738222 | 0.88177 | 0.170319 |
| tossup_correctness | category | History | 1440 | 0.705848 | 0.510422 | 0.0286223 | 0.167326 | 0.764583 | 0.754167 | 0.0104167 | 0.141408 | 0.571669 | 0.812381 | 0.926042 | 0.153252 |
| tossup_correctness | category | Literature | 1422 | 0.684036 | 0.448707 | 0.0186902 | 0.141258 | 0.815049 | 0.814346 | 0.000703235 | 0.126006 | 0.633164 | 0.846477 | 0.937624 | 0.136713 |
| tossup_correctness | category | Mythology | 318 | 0.685497 | 0.47149 | 0.0326673 | 0.148933 | 0.805031 | 0.789308 | 0.0157233 | 0.122025 | 0.6489 | 0.833537 | 0.926389 | 0.143708 |
| tossup_correctness | category | Other Academic | 66 | 0.797312 | 0.509173 | 0.118884 | 0.171641 | 0.742424 | 0.712121 | 0.030303 | 0.146531 | 0.580119 | 0.809875 | 0.907052 | 0.159875 |
| tossup_correctness | category | Philosophy | 311 | 0.707715 | 0.520615 | 0.0528047 | 0.173374 | 0.745981 | 0.745981 | 0 | 0.13452 | 0.588248 | 0.818261 | 0.929523 | 0.148051 |
| tossup_correctness | category | Popular Culture | 102 | 0.587037 | 0.370278 | 0.0424023 | 0.106078 | 0.882353 | 0.882353 | 0 | 0.0770697 | 0.726675 | 0.860967 | 0.919066 | 0.125989 |
| tossup_correctness | category | Religion | 358 | 0.710223 | 0.544786 | 0.0646646 | 0.181111 | 0.748603 | 0.712291 | 0.0363128 | 0.159908 | 0.513129 | 0.786357 | 0.907528 | 0.166891 |
| tossup_correctness | category | Science | 1433 | 0.695902 | 0.52878 | 0.034332 | 0.173933 | 0.755757 | 0.738311 | 0.0174459 | 0.150722 | 0.568713 | 0.804568 | 0.921109 | 0.155252 |
| tossup_correctness | category | Social Science | 324 | 0.767787 | 0.489045 | 0.0401612 | 0.15941 | 0.762346 | 0.731481 | 0.0308642 | 0.160329 | 0.515754 | 0.799045 | 0.905464 | 0.163043 |
| tossup_correctness | category | Unknown | 1937 | 0.690665 | 0.511384 | 0.0250017 | 0.166873 | 0.762519 | 0.758389 | 0.0041301 | 0.143932 | 0.565301 | 0.812466 | 0.919321 | 0.154209 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.618522 | 0.600876 | 0.0783061 | 0.204277 | 0.694611 | 0.712575 | -0.0179641 | 0.130672 | 0.582794 | 0.779931 | 0.891077 | 0.168886 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.719868 | 0.521214 | 0.0260313 | 0.17229 | 0.757675 | 0.729167 | 0.0285088 | 0.16133 | 0.506562 | 0.790408 | 0.911089 | 0.163246 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.722529 | 0.498925 | 0.0301269 | 0.162748 | 0.773522 | 0.755083 | 0.0184397 | 0.136586 | 0.599484 | 0.813404 | 0.925152 | 0.150655 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.693019 | 0.484625 | 0.0175912 | 0.155641 | 0.78692 | 0.780942 | 0.0059775 | 0.133078 | 0.611355 | 0.828326 | 0.925908 | 0.145907 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.71658 | 0.492904 | 0.0173463 | 0.160035 | 0.773159 | 0.762029 | 0.0111293 | 0.159262 | 0.532201 | 0.810677 | 0.927232 | 0.153433 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 2.69806 | 0.698079 | 0.824429 | 1.60377 | 2.21871 | 2.68089 | 3.13803 | 3.92504 | 4.70289 |
| player | theta_1 | 1167 | -1.23062 | 0.778557 | -3.35139 | -2.42119 | -1.73129 | -1.30659 | -0.777717 | 0.200245 | 1.50211 |
| player | theta_2 | 1167 | -1.07628 | 0.761928 | -2.92627 | -2.23457 | -1.56766 | -1.17516 | -0.64756 | 0.364027 | 2.07279 |
| player | theta_3 | 1167 | -0.930538 | 0.69114 | -3.02097 | -2.00371 | -1.40721 | -0.986835 | -0.498111 | 0.278343 | 2.20216 |
| player | theta_norm | 1167 | 2.22427 | 0.504465 | 0.927585 | 1.42437 | 1.86706 | 2.21229 | 2.55263 | 3.1039 | 3.77934 |
| tossup | start_difficulty_d1 | 1220 | -1.7779 | 0.55757 | -3.54963 | -2.5565 | -2.16737 | -1.8303 | -1.45651 | -0.745464 | 1.18105 |
| tossup | start_difficulty_d2 | 1220 | -1.77044 | 0.50879 | -3.60113 | -2.5323 | -2.11979 | -1.79831 | -1.43245 | -0.903146 | 0.0751886 |
| tossup | start_difficulty_d3 | 1220 | -1.7746 | 0.505627 | -3.21718 | -2.53573 | -2.13168 | -1.80434 | -1.45389 | -0.884407 | 0.231666 |
| tossup | end_difficulty_d1 | 1220 | -2.7696 | 0.648023 | -4.91556 | -3.6776 | -3.22994 | -2.8247 | -2.39593 | -1.6017 | 0.471819 |
| tossup | end_difficulty_d2 | 1220 | -2.76032 | 0.595652 | -4.89041 | -3.67028 | -3.17928 | -2.79379 | -2.36935 | -1.76711 | -0.565253 |
| tossup | end_difficulty_d3 | 1220 | -2.76474 | 0.592164 | -4.38049 | -3.68156 | -3.18582 | -2.79484 | -2.37745 | -1.74443 | -0.437653 |
| tossup | total_drop_d1 | 1220 | 0.991702 | 0.110951 | 0.642442 | 0.801418 | 0.917843 | 0.992179 | 1.068 | 1.16503 | 1.5033 |
| tossup | total_drop_d2 | 1220 | 0.989877 | 0.106646 | 0.640442 | 0.81777 | 0.916559 | 0.987114 | 1.05902 | 1.16926 | 1.43517 |
| tossup | total_drop_d3 | 1220 | 0.990144 | 0.103663 | 0.665536 | 0.822355 | 0.918315 | 0.988485 | 1.06023 | 1.16874 | 1.34523 |
| tossup | drop_share_1_d1 | 1220 | 0.303896 | 0.0156512 | 0.212234 | 0.2783 | 0.294628 | 0.304383 | 0.314579 | 0.327496 | 0.357399 |
| tossup | drop_share_2_d1 | 1220 | 0.347183 | 0.0119905 | 0.307479 | 0.32829 | 0.339357 | 0.346896 | 0.354923 | 0.367239 | 0.436865 |
| tossup | drop_share_3_d1 | 1220 | 0.348921 | 0.0164354 | 0.299308 | 0.324317 | 0.337499 | 0.347667 | 0.358853 | 0.376129 | 0.444933 |
| tossup | drop_share_1_d2 | 1220 | 0.30407 | 0.0146378 | 0.251215 | 0.280416 | 0.294552 | 0.30475 | 0.313868 | 0.32728 | 0.357976 |
| tossup | drop_share_2_d2 | 1220 | 0.347075 | 0.0113934 | 0.308868 | 0.328506 | 0.339185 | 0.347605 | 0.354533 | 0.365445 | 0.380013 |
| tossup | drop_share_3_d2 | 1220 | 0.348855 | 0.0153724 | 0.288566 | 0.325057 | 0.33827 | 0.348618 | 0.358303 | 0.373705 | 0.417446 |
| tossup | drop_share_1_d3 | 1220 | 0.304102 | 0.0140818 | 0.241403 | 0.281317 | 0.294928 | 0.30444 | 0.313328 | 0.326402 | 0.348457 |
| tossup | drop_share_2_d3 | 1220 | 0.347245 | 0.0112689 | 0.30549 | 0.328891 | 0.339801 | 0.347408 | 0.355005 | 0.365422 | 0.387983 |
| tossup | drop_share_3_d3 | 1220 | 0.348653 | 0.015018 | 0.308361 | 0.325316 | 0.338061 | 0.347398 | 0.35881 | 0.373371 | 0.420957 |
| tossup | r_1 | 1220 | 0.318278 | 0.147437 | 0.0624931 | 0.132683 | 0.208011 | 0.285629 | 0.40234 | 0.627022 | 0.827505 |
| tossup | r_2 | 1220 | 0.343607 | 0.131038 | 0.0718227 | 0.152205 | 0.251281 | 0.332239 | 0.42151 | 0.598345 | 0.80964 |
| tossup | r_3 | 1220 | 0.338115 | 0.121938 | 0.0723477 | 0.158195 | 0.251668 | 0.328991 | 0.412853 | 0.552195 | 0.837131 |
| tossup | r_norm | 1220 | 0.620865 | 0.0441631 | 0.577423 | 0.579461 | 0.589801 | 0.607369 | 0.634323 | 0.713949 | 0.845398 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 4.5164 | 0.507194 | 1.86334 | 3.74072 | 4.23498 | 4.48017 | 4.78118 | 5.40582 | 6.5844 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 4.50762 | 0.435968 | 1.95864 | 3.84298 | 4.26491 | 4.47738 | 4.72566 | 5.30016 | 6.52009 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 4.48371 | 0.398632 | 2.776 | 3.9167 | 4.27791 | 4.45981 | 4.63442 | 5.15239 | 6.60201 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | 1.52348 | 2.35935 | -8.32384 | -3.16913 | 0.0607977 | 2.69609 | 3.29476 | 3.6897 | 4.28393 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | 2.2428 | 2.21454 | -12.5818 | -2.89955 | 2.20268 | 3.18077 | 3.4454 | 3.76612 | 4.54785 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | 2.45569 | 1.97557 | -12.8935 | -2.24853 | 2.5429 | 3.22072 | 3.46502 | 3.72069 | 4.23163 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 2.99292 | 2.53532 | 0.920872 | 0.984154 | 1.06182 | 1.49231 | 4.84274 | 7.96312 | 13.7262 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 2.26482 | 2.32607 | 0.882804 | 0.968899 | 1.02431 | 1.15398 | 2.06636 | 7.52345 | 17.6265 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 2.02802 | 2.13534 | 0.885239 | 0.964755 | 1.01582 | 1.10288 | 1.64945 | 7.48127 | 18.1289 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.23016 | 0.083097 | 0.043222 | 0.0819685 | 0.157532 | 0.26469 | 0.293099 | 0.316669 | 0.520121 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.344386 | 0.079196 | 0.0666503 | 0.178179 | 0.3328 | 0.350493 | 0.367511 | 0.476333 | 0.679403 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.425454 | 0.133715 | 0.0734243 | 0.296869 | 0.348392 | 0.371072 | 0.466997 | 0.729992 | 0.884631 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.24982 | 0.0714159 | 0.0329224 | 0.0908412 | 0.226254 | 0.277888 | 0.295713 | 0.313323 | 0.605534 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.346375 | 0.0622258 | 0.0777587 | 0.21883 | 0.34044 | 0.350541 | 0.362054 | 0.416672 | 0.703507 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.403805 | 0.109045 | 0.136853 | 0.320073 | 0.349878 | 0.367452 | 0.40481 | 0.670813 | 0.881817 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.25641 | 0.0672906 | 0.0378021 | 0.0862801 | 0.244755 | 0.282295 | 0.296397 | 0.314511 | 0.442213 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.347264 | 0.0573179 | 0.0539648 | 0.246497 | 0.340261 | 0.350988 | 0.360846 | 0.406943 | 0.657732 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.396326 | 0.1009 | 0.18911 | 0.32749 | 0.349829 | 0.365532 | 0.393122 | 0.641516 | 0.907522 |
| tossup_hazard | hazard_r_1 | 1220 | 0.405693 | 0.283855 | 0.0214885 | 0.0573824 | 0.138739 | 0.349508 | 0.683826 | 0.86474 | 0.939609 |
| tossup_hazard | hazard_r_2 | 1220 | 0.314645 | 0.246718 | 0.0245905 | 0.0516993 | 0.107628 | 0.220674 | 0.508052 | 0.789416 | 0.925599 |
| tossup_hazard | hazard_r_3 | 1220 | 0.279662 | 0.235057 | 0.0328425 | 0.0566762 | 0.10306 | 0.174324 | 0.405408 | 0.78127 | 0.940938 |
