# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/simplex-locations-terminal/reference/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/simplex-locations-terminal/reference/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 282872 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.726482 |
| log_loss | 0.474423 |
| ece | 0.0131926 |
| brier | 0.153163 |
| accuracy | 0.789428 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0160734 |
| probability_std | 0.138997 |
| probability_p10 | 0.583669 |
| probability_p50 | 0.810533 |
| probability_p90 | 0.917103 |
| mean_predictive_variance | 0.154731 |
| integrated_brier_score | 0.101471 |
| joint_tossup_event_log_loss | 6.61071 |
| buzz_position_mae | 0.150931 |
| buzz_position_median_absolute_error | 0.133605 |
| buzz_position_bias | -0.0437156 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.352535 |
| first_buzzer_mean_reciprocal_rank | 0.563507 |
| first_buzzer_log_loss | 1.68759 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.726482 |
| neg_average_precision | 0.458837 |
| neg_precision | 0.648703 |
| neg_recall | 0.154688 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.186567 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0137376 |
| no_buzz_calibration_error | 0.00201057 |
| no_buzz_brier | 0.01105 |
| full_pmf_max_mass_error | 1.55431e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.726482 | 0.474423 | 0.0131926 | 0.153163 | 0.789428 | 0.773355 | 0.0160734 | 0.138997 | 0.583669 | 0.810533 | 0.917103 | 0.154731 |
| tossup_correctness | tier | fall | 2876 | 0.730007 | 0.451044 | 0.0117095 | 0.14389 | 0.804937 | 0.793115 | 0.011822 | 0.136749 | 0.592714 | 0.821353 | 0.924501 | 0.149156 |
| tossup_correctness | tier | nationals | 1579 | 0.720913 | 0.523254 | 0.0360473 | 0.173181 | 0.747942 | 0.729576 | 0.0183661 | 0.148406 | 0.560535 | 0.800633 | 0.910645 | 0.159002 |
| tossup_correctness | tier | regionals | 1990 | 0.732062 | 0.480146 | 0.0241436 | 0.155851 | 0.78593 | 0.765829 | 0.0201005 | 0.138284 | 0.572342 | 0.79872 | 0.908974 | 0.160187 |
| tossup_correctness | tier | winter | 2825 | 0.719405 | 0.466898 | 0.0174357 | 0.14952 | 0.799292 | 0.783009 | 0.0162832 | 0.135229 | 0.591721 | 0.811692 | 0.915992 | 0.154178 |
| tossup_correctness | category | Current Events | 123 | 0.764857 | 0.464414 | 0.0636815 | 0.151037 | 0.772358 | 0.764228 | 0.00813008 | 0.134309 | 0.567733 | 0.75334 | 0.912374 | 0.172222 |
| tossup_correctness | category | Fine Arts | 1093 | 0.738871 | 0.468852 | 0.0234316 | 0.150441 | 0.796889 | 0.769442 | 0.0274474 | 0.141481 | 0.588644 | 0.823786 | 0.919811 | 0.150937 |
| tossup_correctness | category | Geography | 191 | 0.797252 | 0.489695 | 0.0807473 | 0.159267 | 0.764398 | 0.691099 | 0.0732984 | 0.199398 | 0.445139 | 0.770725 | 0.895025 | 0.168119 |
| tossup_correctness | category | History | 1469 | 0.72095 | 0.497485 | 0.0302988 | 0.16351 | 0.770592 | 0.758339 | 0.0122532 | 0.140712 | 0.57763 | 0.809951 | 0.920046 | 0.154787 |
| tossup_correctness | category | Literature | 1436 | 0.714587 | 0.432591 | 0.0168537 | 0.135681 | 0.817549 | 0.81546 | 0.00208914 | 0.117335 | 0.650443 | 0.845913 | 0.927517 | 0.138782 |
| tossup_correctness | category | Mythology | 325 | 0.688207 | 0.412229 | 0.0598518 | 0.127248 | 0.84 | 0.843077 | -0.00307692 | 0.100009 | 0.670086 | 0.820423 | 0.912536 | 0.147188 |
| tossup_correctness | category | Other Academic | 67 | 0.673854 | 0.487071 | 0.0724296 | 0.157462 | 0.80597 | 0.791045 | 0.0149254 | 0.132859 | 0.592527 | 0.774929 | 0.890751 | 0.171143 |
| tossup_correctness | category | Philosophy | 322 | 0.683279 | 0.487599 | 0.0475642 | 0.15916 | 0.770186 | 0.785714 | -0.015528 | 0.124356 | 0.614824 | 0.814359 | 0.931578 | 0.150458 |
| tossup_correctness | category | Popular Culture | 100 | 0.531154 | 0.364426 | 0.0648038 | 0.105013 | 0.89 | 0.89 | 0 | 0.0653434 | 0.759012 | 0.85554 | 0.920125 | 0.126485 |
| tossup_correctness | category | Religion | 365 | 0.670642 | 0.555596 | 0.0461894 | 0.185732 | 0.742466 | 0.723288 | 0.0191781 | 0.141559 | 0.559474 | 0.788046 | 0.912319 | 0.162979 |
| tossup_correctness | category | Science | 1456 | 0.726517 | 0.480654 | 0.0163406 | 0.155463 | 0.784341 | 0.76717 | 0.0171703 | 0.143104 | 0.567573 | 0.796771 | 0.907284 | 0.161236 |
| tossup_correctness | category | Social Science | 333 | 0.749657 | 0.494323 | 0.0479768 | 0.160391 | 0.777778 | 0.72973 | 0.048048 | 0.16015 | 0.49924 | 0.780099 | 0.910894 | 0.168171 |
| tossup_correctness | category | Unknown | 1990 | 0.732062 | 0.480146 | 0.0241436 | 0.155851 | 0.78593 | 0.765829 | 0.0201005 | 0.138284 | 0.572342 | 0.79872 | 0.908974 | 0.160187 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.763847 | 0.484414 | 0.0749034 | 0.158483 | 0.765363 | 0.748603 | 0.0167598 | 0.147622 | 0.524164 | 0.772286 | 0.878306 | 0.175076 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.7029 | 0.501922 | 0.01986 | 0.163683 | 0.779519 | 0.754441 | 0.0250784 | 0.139118 | 0.557595 | 0.784683 | 0.901941 | 0.165432 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.72524 | 0.483293 | 0.0283803 | 0.157052 | 0.784385 | 0.766682 | 0.0177031 | 0.136696 | 0.591536 | 0.809288 | 0.915677 | 0.155796 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.716029 | 0.462222 | 0.0153248 | 0.147802 | 0.802216 | 0.787441 | 0.014775 | 0.128608 | 0.620134 | 0.821701 | 0.919755 | 0.14901 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.74016 | 0.470592 | 0.0181076 | 0.151935 | 0.784964 | 0.771758 | 0.0132069 | 0.148071 | 0.550874 | 0.811366 | 0.919762 | 0.155006 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 2.68168 | 0.735342 | 0.441308 | 1.45891 | 2.19509 | 2.68227 | 3.15865 | 3.95901 | 4.63498 |
| player | theta_1 | 1196 | -1.20939 | 0.841782 | -3.75191 | -2.49468 | -1.76263 | -1.28482 | -0.737964 | 0.306515 | 2.01309 |
| player | theta_2 | 1196 | -0.990083 | 0.642721 | -3.28101 | -2.08305 | -1.36682 | -0.996594 | -0.573729 | 0.046696 | 1.38476 |
| player | theta_3 | 1196 | -1.11338 | 0.764277 | -3.31364 | -2.33613 | -1.59234 | -1.17118 | -0.664019 | 0.272053 | 2.04431 |
| player | theta_norm | 1196 | 2.23923 | 0.610798 | 0.525739 | 1.31419 | 1.81015 | 2.19329 | 2.62615 | 3.28967 | 4.29514 |
| tossup | start_difficulty_d1 | 1240 | -1.76693 | 0.546108 | -3.46969 | -2.54474 | -2.13577 | -1.81331 | -1.46588 | -0.783017 | 1.44373 |
| tossup | start_difficulty_d2 | 1240 | -1.75462 | 0.502491 | -3.39148 | -2.50638 | -2.11608 | -1.77973 | -1.43972 | -0.835405 | -0.149014 |
| tossup | start_difficulty_d3 | 1240 | -1.75571 | 0.510382 | -3.59348 | -2.53215 | -2.12281 | -1.78905 | -1.42336 | -0.85817 | 0.674013 |
| tossup | end_difficulty_d1 | 1240 | -2.75522 | 0.636109 | -4.63597 | -3.65827 | -3.20504 | -2.81797 | -2.39533 | -1.61448 | 0.76717 |
| tossup | end_difficulty_d2 | 1240 | -2.7405 | 0.589467 | -4.72664 | -3.63165 | -3.15594 | -2.75946 | -2.36344 | -1.67481 | -0.859417 |
| tossup | end_difficulty_d3 | 1240 | -2.74076 | 0.59483 | -4.88375 | -3.64956 | -3.17009 | -2.77292 | -2.34927 | -1.70849 | 0.00552398 |
| tossup | total_drop_d1 | 1240 | 0.988292 | 0.111118 | 0.588927 | 0.797792 | 0.914006 | 0.992855 | 1.06308 | 1.16603 | 1.38153 |
| tossup | total_drop_d2 | 1240 | 0.985875 | 0.103893 | 0.681534 | 0.81787 | 0.916809 | 0.984958 | 1.05282 | 1.16137 | 1.33516 |
| tossup | total_drop_d3 | 1240 | 0.98505 | 0.104124 | 0.637936 | 0.818392 | 0.914053 | 0.984635 | 1.05439 | 1.16261 | 1.42868 |
| tossup | drop_share_1_d1 | 1240 | 0.304142 | 0.0154955 | 0.229492 | 0.279424 | 0.294747 | 0.304289 | 0.314605 | 0.32811 | 0.365661 |
| tossup | drop_share_2_d1 | 1240 | 0.347109 | 0.0114096 | 0.310017 | 0.328058 | 0.339532 | 0.347228 | 0.355096 | 0.365164 | 0.388064 |
| tossup | drop_share_3_d1 | 1240 | 0.348749 | 0.0165755 | 0.296995 | 0.323132 | 0.337606 | 0.348502 | 0.359598 | 0.377047 | 0.417495 |
| tossup | drop_share_1_d2 | 1240 | 0.303643 | 0.0143097 | 0.248134 | 0.279957 | 0.294421 | 0.303805 | 0.313267 | 0.326398 | 0.345692 |
| tossup | drop_share_2_d2 | 1240 | 0.34694 | 0.0113605 | 0.307757 | 0.32799 | 0.339185 | 0.346682 | 0.354612 | 0.365454 | 0.385425 |
| tossup | drop_share_3_d2 | 1240 | 0.349417 | 0.0154332 | 0.302892 | 0.324738 | 0.338651 | 0.349557 | 0.358856 | 0.37523 | 0.413402 |
| tossup | drop_share_1_d3 | 1240 | 0.303457 | 0.0151265 | 0.24066 | 0.277653 | 0.294098 | 0.303813 | 0.313561 | 0.32683 | 0.359212 |
| tossup | drop_share_2_d3 | 1240 | 0.347147 | 0.0112235 | 0.311264 | 0.328774 | 0.339896 | 0.346924 | 0.354334 | 0.365304 | 0.38429 |
| tossup | drop_share_3_d3 | 1240 | 0.349396 | 0.015897 | 0.307257 | 0.325251 | 0.338588 | 0.348952 | 0.359081 | 0.377448 | 0.418386 |
| tossup | r_1 | 1240 | 0.3209 | 0.14446 | 0.0588393 | 0.12973 | 0.212154 | 0.293224 | 0.410046 | 0.598906 | 0.859487 |
| tossup | r_2 | 1240 | 0.33581 | 0.112597 | 0.0569686 | 0.162338 | 0.25893 | 0.331988 | 0.402087 | 0.535397 | 0.829886 |
| tossup | r_3 | 1240 | 0.34329 | 0.12492 | 0.0732391 | 0.160734 | 0.255631 | 0.331756 | 0.415931 | 0.569158 | 0.83863 |
| tossup | r_norm | 1240 | 0.617167 | 0.0425586 | 0.577367 | 0.579306 | 0.587911 | 0.603014 | 0.630214 | 0.70148 | 0.865221 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.48683 | 0.488688 | 2.20265 | 3.78496 | 4.21848 | 4.4425 | 4.71105 | 5.42792 | 6.38192 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.45963 | 0.431805 | 2.15281 | 3.77009 | 4.23209 | 4.44764 | 4.65925 | 5.18614 | 6.63596 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.47312 | 0.437454 | 2.34354 | 3.78099 | 4.2328 | 4.44443 | 4.71487 | 5.20639 | 6.25296 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.7931 | 2.32537 | -11.571 | -3.15189 | 0.798661 | 2.92519 | 3.32205 | 3.64319 | 4.37698 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.27444 | 2.10344 | -9.62564 | -2.62285 | 2.40248 | 3.13494 | 3.40515 | 3.71179 | 4.26307 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.1764 | 2.06747 | -11.3273 | -2.27547 | 1.86744 | 3.06725 | 3.37147 | 3.73442 | 4.27496 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.69373 | 2.49706 | 0.861765 | 0.981617 | 1.05893 | 1.28502 | 3.92597 | 7.96537 | 16.3669 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.18519 | 2.26024 | 0.906421 | 0.961289 | 1.02235 | 1.16744 | 1.79086 | 7.37863 | 14.4971 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.29672 | 2.19768 | 0.851192 | 0.967162 | 1.02942 | 1.20025 | 2.48195 | 7.14998 | 15.7912 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.237748 | 0.0799857 | 0.0363655 | 0.0833425 | 0.186456 | 0.272138 | 0.293332 | 0.316416 | 0.558355 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.342831 | 0.0754703 | 0.0552075 | 0.174969 | 0.336414 | 0.351453 | 0.365762 | 0.447709 | 0.693701 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.419421 | 0.129464 | 0.120151 | 0.300594 | 0.347962 | 0.369496 | 0.435477 | 0.734756 | 0.901469 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.253727 | 0.0704616 | 0.0312711 | 0.0912549 | 0.238901 | 0.280193 | 0.296597 | 0.31519 | 0.651752 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.347917 | 0.060633 | 0.0606291 | 0.23068 | 0.340178 | 0.350941 | 0.363418 | 0.411585 | 0.692617 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.398355 | 0.105264 | 0.0939289 | 0.318907 | 0.349231 | 0.365564 | 0.397578 | 0.653482 | 0.895698 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.248038 | 0.0706988 | 0.0390929 | 0.0934615 | 0.217271 | 0.275368 | 0.296176 | 0.31507 | 0.552219 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.349086 | 0.0613975 | 0.0821414 | 0.232892 | 0.338609 | 0.350911 | 0.364519 | 0.436246 | 0.715968 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.402876 | 0.107282 | 0.0738868 | 0.316297 | 0.349012 | 0.367786 | 0.40806 | 0.656685 | 0.878136 |
| tossup_hazard | hazard_r_1 | 1240 | 0.377335 | 0.277988 | 0.0327259 | 0.0638019 | 0.134728 | 0.276595 | 0.605563 | 0.877777 | 0.948859 |
| tossup_hazard | hazard_r_2 | 1240 | 0.290713 | 0.210142 | 0.0203535 | 0.0513504 | 0.119751 | 0.227776 | 0.42421 | 0.705949 | 0.862445 |
| tossup_hazard | hazard_r_3 | 1240 | 0.331951 | 0.247057 | 0.0227229 | 0.0475609 | 0.121036 | 0.248179 | 0.542524 | 0.777643 | 0.923045 |
