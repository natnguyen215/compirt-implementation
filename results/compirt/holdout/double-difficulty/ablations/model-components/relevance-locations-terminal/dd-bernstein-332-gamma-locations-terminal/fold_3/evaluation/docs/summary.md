# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-gamma-locations-terminal/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-gamma-locations-terminal/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 284123 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.714609 |
| log_loss | 0.495748 |
| ece | 0.0426126 |
| brier | 0.158427 |
| accuracy | 0.782048 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0120044 |
| probability_std | 0.186289 |
| probability_p10 | 0.484836 |
| probability_p50 | 0.786782 |
| probability_p90 | 0.952541 |
| mean_predictive_variance | 0.154282 |
| integrated_brier_score | 0.0927023 |
| joint_tossup_event_log_loss | 6.36831 |
| buzz_position_mae | 0.134332 |
| buzz_position_median_absolute_error | 0.107694 |
| buzz_position_bias | 0.00336961 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.396366 |
| first_buzzer_mean_reciprocal_rank | 0.599602 |
| first_buzzer_log_loss | 1.58445 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.714609 |
| neg_average_precision | 0.458699 |
| neg_precision | 0.554014 |
| neg_recall | 0.26772 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.186064 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.00881237 |
| no_buzz_calibration_error | -0.00637201 |
| no_buzz_brier | 0.0131426 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.714609 | 0.495748 | 0.0426126 | 0.158427 | 0.782048 | 0.770044 | 0.0120044 | 0.186289 | 0.484836 | 0.786782 | 0.952541 | 0.154282 |
| tossup_correctness | tier | fall | 2817 | 0.708421 | 0.491571 | 0.045712 | 0.154196 | 0.791267 | 0.781683 | 0.00958466 | 0.183671 | 0.49822 | 0.810854 | 0.960987 | 0.14632 |
| tossup_correctness | tier | nationals | 1542 | 0.722223 | 0.52669 | 0.0405911 | 0.17332 | 0.747082 | 0.73476 | 0.0123217 | 0.196683 | 0.440122 | 0.744973 | 0.949119 | 0.164278 |
| tossup_correctness | tier | regionals | 1934 | 0.708007 | 0.510417 | 0.0470585 | 0.164925 | 0.775595 | 0.75698 | 0.0186143 | 0.18284 | 0.48257 | 0.768807 | 0.946124 | 0.160125 |
| tossup_correctness | tier | winter | 2787 | 0.712706 | 0.472671 | 0.053582 | 0.149954 | 0.796555 | 0.786868 | 0.00968784 | 0.182922 | 0.496366 | 0.79562 | 0.948316 | 0.152744 |
| tossup_correctness | category | Current Events | 125 | 0.758907 | 0.507797 | 0.0566927 | 0.17061 | 0.728 | 0.704 | 0.024 | 0.189235 | 0.451714 | 0.720911 | 0.946881 | 0.169672 |
| tossup_correctness | category | Fine Arts | 1072 | 0.730462 | 0.486397 | 0.0410436 | 0.154742 | 0.781716 | 0.770522 | 0.011194 | 0.187139 | 0.487589 | 0.791006 | 0.955351 | 0.152238 |
| tossup_correctness | category | Geography | 185 | 0.765315 | 0.509559 | 0.0856686 | 0.16852 | 0.762162 | 0.702703 | 0.0594595 | 0.230918 | 0.350101 | 0.71665 | 0.924484 | 0.170449 |
| tossup_correctness | category | History | 1443 | 0.724843 | 0.49585 | 0.043816 | 0.160104 | 0.775468 | 0.765073 | 0.010395 | 0.196892 | 0.456361 | 0.778783 | 0.950784 | 0.15549 |
| tossup_correctness | category | Literature | 1411 | 0.675314 | 0.470216 | 0.0468546 | 0.146257 | 0.807229 | 0.81219 | -0.00496102 | 0.162768 | 0.550143 | 0.840871 | 0.961618 | 0.136711 |
| tossup_correctness | category | Mythology | 320 | 0.665772 | 0.51358 | 0.0591356 | 0.155136 | 0.803125 | 0.79375 | 0.009375 | 0.159999 | 0.549642 | 0.813776 | 0.958143 | 0.144995 |
| tossup_correctness | category | Other Academic | 64 | 0.64974 | 0.586662 | 0.089348 | 0.181884 | 0.734375 | 0.75 | -0.015625 | 0.143985 | 0.556912 | 0.757578 | 0.936154 | 0.163967 |
| tossup_correctness | category | Philosophy | 312 | 0.699355 | 0.460196 | 0.072749 | 0.147936 | 0.801282 | 0.801282 | 0 | 0.170322 | 0.533766 | 0.797655 | 0.971811 | 0.147985 |
| tossup_correctness | category | Popular Culture | 104 | 0.617188 | 0.433638 | 0.0500205 | 0.128196 | 0.836538 | 0.846154 | -0.00961538 | 0.102401 | 0.692518 | 0.862281 | 0.957443 | 0.120499 |
| tossup_correctness | category | Religion | 358 | 0.730887 | 0.51748 | 0.0667471 | 0.171546 | 0.756983 | 0.726257 | 0.0307263 | 0.179156 | 0.440024 | 0.711296 | 0.904237 | 0.179957 |
| tossup_correctness | category | Science | 1431 | 0.71264 | 0.500523 | 0.0513969 | 0.1602 | 0.777778 | 0.765199 | 0.0125786 | 0.188888 | 0.471495 | 0.771407 | 0.94964 | 0.159052 |
| tossup_correctness | category | Social Science | 321 | 0.744515 | 0.510975 | 0.065893 | 0.163034 | 0.772586 | 0.744548 | 0.0280374 | 0.21572 | 0.396018 | 0.773208 | 0.956689 | 0.156885 |
| tossup_correctness | category | Unknown | 1934 | 0.708007 | 0.510417 | 0.0470585 | 0.164925 | 0.775595 | 0.75698 | 0.0186143 | 0.18284 | 0.48257 | 0.768807 | 0.946124 | 0.160125 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.738806 | 0.54821 | 0.0745776 | 0.185034 | 0.744792 | 0.697917 | 0.046875 | 0.213729 | 0.327345 | 0.655311 | 0.881509 | 0.188357 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.760413 | 0.490717 | 0.0350871 | 0.160451 | 0.762655 | 0.733408 | 0.0292463 | 0.204211 | 0.430216 | 0.741294 | 0.936611 | 0.165892 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.692656 | 0.528681 | 0.050657 | 0.168753 | 0.766516 | 0.759276 | 0.00723982 | 0.190334 | 0.475483 | 0.788907 | 0.955188 | 0.153335 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.693169 | 0.484497 | 0.0410109 | 0.152839 | 0.798536 | 0.789125 | 0.00941094 | 0.168415 | 0.541794 | 0.807832 | 0.961434 | 0.146305 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.730549 | 0.47996 | 0.0492018 | 0.153736 | 0.785959 | 0.775342 | 0.0106164 | 0.186233 | 0.477675 | 0.78264 | 0.947284 | 0.15706 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 1.76034 | 0.651441 | -0.424135 | 0.691287 | 1.36524 | 1.76226 | 2.15449 | 2.8237 | 4.24185 |
| player | theta_1 | 1133 | -1.53509 | 0.638511 | -3.07948 | -2.51242 | -2.00456 | -1.56736 | -1.11442 | -0.387785 | 0.346109 |
| player | theta_2 | 1133 | -1.46901 | 0.655676 | -3.2837 | -2.46236 | -1.9332 | -1.49318 | -1.03136 | -0.335883 | 0.694565 |
| player | theta_3 | 1133 | -1.55698 | 0.670785 | -3.99119 | -2.62926 | -2.04223 | -1.58123 | -1.08026 | -0.462618 | 0.258136 |
| player | theta_norm | 1133 | 2.81261 | 0.560901 | 0.984951 | 1.8961 | 2.41918 | 2.83934 | 3.21004 | 3.69319 | 4.48369 |
| tossup | start_difficulty_d1 | 1240 | -1.25846 | 0.398406 | -2.49712 | -1.8798 | -1.51192 | -1.28778 | -1.02482 | -0.543971 | 0.240036 |
| tossup | start_difficulty_d2 | 1240 | -1.25022 | 0.405548 | -2.69886 | -1.87664 | -1.51524 | -1.27121 | -1.01313 | -0.519323 | 0.34329 |
| tossup | start_difficulty_d3 | 1240 | -1.27478 | 0.40007 | -2.52698 | -1.91131 | -1.53675 | -1.29457 | -1.02156 | -0.582139 | 0.0853207 |
| tossup | end_difficulty_d1 | 1240 | -2.25454 | 0.465214 | -3.71551 | -2.96172 | -2.55367 | -2.29045 | -1.98975 | -1.41809 | -0.43352 |
| tossup | end_difficulty_d2 | 1240 | -2.23846 | 0.470251 | -3.62952 | -2.97414 | -2.54786 | -2.27544 | -1.96533 | -1.39097 | -0.353921 |
| tossup | end_difficulty_d3 | 1240 | -2.26914 | 0.457246 | -3.73265 | -3.01348 | -2.57553 | -2.28892 | -2.00262 | -1.47773 | -0.60957 |
| tossup | total_drop_d1 | 1240 | 0.996083 | 0.131716 | 0.620278 | 0.814871 | 0.917863 | 0.989808 | 1.05914 | 1.19359 | 2.19287 |
| tossup | total_drop_d2 | 1240 | 0.988242 | 0.123231 | 0.642924 | 0.802135 | 0.912628 | 0.988724 | 1.05233 | 1.17392 | 1.96486 |
| tossup | total_drop_d3 | 1240 | 0.994363 | 0.117914 | 0.640433 | 0.822929 | 0.916041 | 0.992404 | 1.05692 | 1.18893 | 1.76109 |
| tossup | drop_share_1_d1 | 1240 | 0.304394 | 0.0200009 | 0.1933 | 0.272895 | 0.294532 | 0.305113 | 0.316593 | 0.33368 | 0.380691 |
| tossup | drop_share_2_d1 | 1240 | 0.347122 | 0.0135716 | 0.287368 | 0.325789 | 0.338581 | 0.346785 | 0.355552 | 0.368135 | 0.441868 |
| tossup | drop_share_3_d1 | 1240 | 0.348484 | 0.0213947 | 0.285471 | 0.317114 | 0.335895 | 0.347443 | 0.359923 | 0.381914 | 0.512086 |
| tossup | drop_share_1_d2 | 1240 | 0.304117 | 0.0187396 | 0.198315 | 0.275568 | 0.293815 | 0.304698 | 0.315241 | 0.332969 | 0.366943 |
| tossup | drop_share_2_d2 | 1240 | 0.347051 | 0.0132137 | 0.296702 | 0.326822 | 0.338315 | 0.346545 | 0.355201 | 0.368762 | 0.4573 |
| tossup | drop_share_3_d2 | 1240 | 0.348832 | 0.0196671 | 0.282839 | 0.318166 | 0.336966 | 0.348698 | 0.359771 | 0.378853 | 0.473652 |
| tossup | drop_share_1_d3 | 1240 | 0.304007 | 0.0194514 | 0.192066 | 0.2722 | 0.293644 | 0.304954 | 0.316569 | 0.332336 | 0.374182 |
| tossup | drop_share_2_d3 | 1240 | 0.347143 | 0.0128406 | 0.306938 | 0.326134 | 0.339237 | 0.346883 | 0.354973 | 0.367707 | 0.410278 |
| tossup | drop_share_3_d3 | 1240 | 0.34885 | 0.0204177 | 0.292826 | 0.319769 | 0.336053 | 0.347694 | 0.358795 | 0.381172 | 0.495431 |
| tossup | r_1 | 1240 | 0.661922 | 0.313167 | 0.205426 | 0.315566 | 0.438404 | 0.5878 | 0.79511 | 1.26358 | 2.63948 |
| tossup | r_2 | 1240 | 0.675959 | 0.312183 | 0.148207 | 0.310116 | 0.462066 | 0.604332 | 0.817686 | 1.28226 | 2.37516 |
| tossup | r_3 | 1240 | 0.65988 | 0.307305 | 0.212963 | 0.314539 | 0.442546 | 0.57982 | 0.803317 | 1.29554 | 2.50415 |
| tossup | r_norm | 1240 | 1.22207 | 0.356192 | 0.463874 | 0.734324 | 0.946866 | 1.17991 | 1.45145 | 1.88902 | 2.71395 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 0.637064 | 0.277998 | -0.250455 | 0.185016 | 0.437115 | 0.640643 | 0.835488 | 1.09776 | 1.3225 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 0.646898 | 0.265863 | -0.28495 | 0.200464 | 0.465164 | 0.667879 | 0.845112 | 1.05963 | 1.39252 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 0.635051 | 0.287619 | -0.408586 | 0.154552 | 0.433616 | 0.628716 | 0.829006 | 1.11677 | 1.44829 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.753565 | 0.522067 | -3.15179 | -1.60484 | -1.08449 | -0.751361 | -0.380711 | 0.093932 | 0.3412 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.725234 | 0.489656 | -3.20141 | -1.56113 | -1.06029 | -0.708653 | -0.354905 | 0.00450829 | 0.351028 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.826363 | 0.597761 | -3.27525 | -1.795 | -1.22345 | -0.823369 | -0.394349 | 0.146196 | 0.580213 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 1.39063 | 0.410021 | 0.647984 | 0.904816 | 1.062 | 1.31497 | 1.60539 | 2.15403 | 3.3143 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.37213 | 0.422202 | 0.609358 | 0.91503 | 1.05074 | 1.26372 | 1.58268 | 2.17969 | 4.06238 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 1.46141 | 0.492292 | 0.642382 | 0.908148 | 1.06007 | 1.3474 | 1.75293 | 2.36349 | 3.72059 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.245372 | 0.0641776 | 0.0854246 | 0.147276 | 0.20429 | 0.245635 | 0.279981 | 0.336451 | 0.662722 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.304677 | 0.0576278 | 0.103806 | 0.189765 | 0.274608 | 0.316418 | 0.34101 | 0.378467 | 0.535615 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.449951 | 0.103314 | 0.0917375 | 0.309317 | 0.380761 | 0.43373 | 0.512772 | 0.642717 | 0.807937 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.247225 | 0.0647755 | 0.076615 | 0.141906 | 0.210274 | 0.248924 | 0.280763 | 0.345317 | 0.695731 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.305793 | 0.058067 | 0.076704 | 0.192077 | 0.278097 | 0.31667 | 0.340747 | 0.37736 | 0.580376 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.446982 | 0.103458 | 0.137563 | 0.307227 | 0.382345 | 0.4286 | 0.499339 | 0.644571 | 0.846681 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.246941 | 0.0738743 | 0.0583212 | 0.136371 | 0.199394 | 0.247894 | 0.284227 | 0.372792 | 0.636249 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.302576 | 0.0597947 | 0.104682 | 0.191464 | 0.267259 | 0.315118 | 0.339934 | 0.384995 | 0.528792 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.450483 | 0.112633 | 0.0735242 | 0.288925 | 0.376938 | 0.429594 | 0.516621 | 0.665832 | 0.826489 |
| tossup_hazard | hazard_r_1 | 1240 | 1.41236 | 0.746297 | 0.215191 | 0.525026 | 0.876156 | 1.1912 | 1.82447 | 2.89896 | 4.24264 |
| tossup_hazard | hazard_r_2 | 1240 | 1.36448 | 0.73608 | 0.238559 | 0.529943 | 0.855151 | 1.15172 | 1.66144 | 2.96784 | 4.6212 |
| tossup_hazard | hazard_r_3 | 1240 | 1.43325 | 0.712524 | 0.166048 | 0.459877 | 0.903307 | 1.32648 | 1.88878 | 2.75467 | 5.25974 |
