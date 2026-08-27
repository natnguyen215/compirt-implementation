# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/simplex-locations-terminal/gamma-relevance/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/simplex-locations-terminal/gamma-relevance/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 282596 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.717893 |
| log_loss | 0.498194 |
| ece | 0.0376258 |
| brier | 0.161159 |
| accuracy | 0.77174 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00756185 |
| probability_std | 0.186308 |
| probability_p10 | 0.477884 |
| probability_p50 | 0.777479 |
| probability_p90 | 0.950448 |
| mean_predictive_variance | 0.157522 |
| integrated_brier_score | 0.0950543 |
| joint_tossup_event_log_loss | 6.42366 |
| buzz_position_mae | 0.137071 |
| buzz_position_median_absolute_error | 0.111402 |
| buzz_position_bias | 0.0111019 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.388463 |
| first_buzzer_mean_reciprocal_rank | 0.595251 |
| first_buzzer_log_loss | 1.58862 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.717893 |
| neg_average_precision | 0.457927 |
| neg_precision | 0.533081 |
| neg_recall | 0.25836 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.195057 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0088353 |
| no_buzz_calibration_error | -0.00427771 |
| no_buzz_brier | 0.0121257 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.717893 | 0.498194 | 0.0376258 | 0.161159 | 0.77174 | 0.764178 | 0.00756185 | 0.186308 | 0.477884 | 0.777479 | 0.950448 | 0.157522 |
| tossup_correctness | tier | fall | 2798 | 0.738129 | 0.465458 | 0.038215 | 0.14842 | 0.79807 | 0.785204 | 0.0128663 | 0.184594 | 0.491414 | 0.796053 | 0.954389 | 0.152096 |
| tossup_correctness | tier | nationals | 1545 | 0.715196 | 0.538957 | 0.033017 | 0.178704 | 0.730097 | 0.721036 | 0.00906149 | 0.194928 | 0.44711 | 0.740131 | 0.946043 | 0.166683 |
| tossup_correctness | tier | regionals | 2039 | 0.702753 | 0.513326 | 0.0521092 | 0.165463 | 0.7641 | 0.762138 | 0.00196175 | 0.183806 | 0.47556 | 0.762932 | 0.955649 | 0.161529 |
| tossup_correctness | tier | winter | 2875 | 0.70664 | 0.497416 | 0.0345478 | 0.161075 | 0.773913 | 0.768348 | 0.00556522 | 0.183258 | 0.490697 | 0.789104 | 0.943293 | 0.155039 |
| tossup_correctness | category | Current Events | 129 | 0.705246 | 0.584921 | 0.0945062 | 0.202058 | 0.697674 | 0.666667 | 0.0310078 | 0.223465 | 0.363679 | 0.731943 | 0.963913 | 0.15887 |
| tossup_correctness | category | Fine Arts | 1074 | 0.694005 | 0.50884 | 0.0645485 | 0.164103 | 0.781192 | 0.776536 | 0.00465549 | 0.197225 | 0.447323 | 0.763762 | 0.953679 | 0.15804 |
| tossup_correctness | category | Geography | 180 | 0.756626 | 0.564812 | 0.0738441 | 0.191211 | 0.716667 | 0.616667 | 0.1 | 0.258367 | 0.225848 | 0.73994 | 0.93168 | 0.157583 |
| tossup_correctness | category | History | 1454 | 0.720178 | 0.501476 | 0.040148 | 0.161472 | 0.768913 | 0.757909 | 0.0110041 | 0.187029 | 0.478715 | 0.780968 | 0.952153 | 0.156288 |
| tossup_correctness | category | Literature | 1435 | 0.736505 | 0.438135 | 0.0348546 | 0.136156 | 0.811847 | 0.810453 | 0.00139373 | 0.163249 | 0.546917 | 0.829232 | 0.959937 | 0.142143 |
| tossup_correctness | category | Mythology | 324 | 0.673152 | 0.489045 | 0.053422 | 0.154332 | 0.796296 | 0.79321 | 0.00308642 | 0.154741 | 0.55416 | 0.830238 | 0.9478 | 0.146171 |
| tossup_correctness | category | Other Academic | 71 | 0.639434 | 0.550132 | 0.0821984 | 0.182221 | 0.71831 | 0.760563 | -0.0422535 | 0.151265 | 0.540565 | 0.745703 | 0.937458 | 0.166857 |
| tossup_correctness | category | Philosophy | 310 | 0.742327 | 0.488885 | 0.0482043 | 0.160408 | 0.767742 | 0.76129 | 0.00645161 | 0.190439 | 0.453998 | 0.765485 | 0.965868 | 0.159535 |
| tossup_correctness | category | Popular Culture | 108 | 0.455729 | 0.41306 | 0.114575 | 0.117353 | 0.87037 | 0.888889 | -0.0185185 | 0.113792 | 0.668855 | 0.85047 | 0.949189 | 0.130635 |
| tossup_correctness | category | Religion | 361 | 0.690098 | 0.536793 | 0.0618243 | 0.180125 | 0.722992 | 0.742382 | -0.0193906 | 0.186647 | 0.449425 | 0.715345 | 0.896895 | 0.180396 |
| tossup_correctness | category | Science | 1445 | 0.728875 | 0.501373 | 0.025958 | 0.16609 | 0.758478 | 0.746021 | 0.0124567 | 0.180878 | 0.485939 | 0.763307 | 0.93391 | 0.16377 |
| tossup_correctness | category | Social Science | 327 | 0.732516 | 0.525028 | 0.0666798 | 0.174947 | 0.755352 | 0.718654 | 0.0366972 | 0.205477 | 0.394705 | 0.736777 | 0.941978 | 0.166583 |
| tossup_correctness | category | Unknown | 2039 | 0.702753 | 0.513326 | 0.0521092 | 0.165463 | 0.7641 | 0.762138 | 0.00196175 | 0.183806 | 0.47556 | 0.762932 | 0.955649 | 0.161529 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.727785 | 0.544671 | 0.109832 | 0.183597 | 0.721311 | 0.743169 | -0.0218579 | 0.221333 | 0.331344 | 0.660403 | 0.910844 | 0.182657 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.720282 | 0.530931 | 0.0659085 | 0.173454 | 0.747644 | 0.728796 | 0.0188482 | 0.21147 | 0.394886 | 0.721636 | 0.93381 | 0.169766 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.72775 | 0.503266 | 0.0317298 | 0.163218 | 0.7682 | 0.752568 | 0.015632 | 0.189217 | 0.476368 | 0.775361 | 0.949445 | 0.15843 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.708771 | 0.475955 | 0.0302009 | 0.153897 | 0.784 | 0.786087 | -0.00208696 | 0.170403 | 0.522504 | 0.805243 | 0.957968 | 0.149802 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.716701 | 0.502458 | 0.0394929 | 0.161298 | 0.773378 | 0.764393 | 0.00898502 | 0.181845 | 0.488678 | 0.773308 | 0.949015 | 0.15881 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 1.76506 | 0.639702 | -0.74243 | 0.662164 | 1.35291 | 1.78905 | 2.14981 | 2.77711 | 4.20006 |
| player | theta_1 | 1197 | -1.5311 | 0.651561 | -3.47778 | -2.52395 | -2.0283 | -1.54772 | -1.10275 | -0.361704 | 0.261984 |
| player | theta_2 | 1197 | -1.48464 | 0.660629 | -3.34564 | -2.50764 | -1.96272 | -1.50309 | -1.05018 | -0.378451 | 0.968285 |
| player | theta_3 | 1197 | -1.55412 | 0.677043 | -3.54156 | -2.65133 | -2.02464 | -1.5486 | -1.09029 | -0.441411 | 0.270725 |
| player | theta_norm | 1197 | 2.82382 | 0.555184 | 1.11048 | 1.90733 | 2.43323 | 2.83098 | 3.2099 | 3.75679 | 4.16702 |
| tossup | start_difficulty_d1 | 1240 | -1.26214 | 0.396358 | -2.41884 | -1.87013 | -1.50796 | -1.29235 | -1.03029 | -0.569065 | 0.14391 |
| tossup | start_difficulty_d2 | 1240 | -1.25175 | 0.403439 | -2.64629 | -1.86943 | -1.50912 | -1.27019 | -1.01124 | -0.543702 | 0.352255 |
| tossup | start_difficulty_d3 | 1240 | -1.27813 | 0.397936 | -2.54995 | -1.90435 | -1.54783 | -1.29009 | -1.0323 | -0.609939 | 0.231359 |
| tossup | end_difficulty_d1 | 1240 | -2.25717 | 0.459537 | -3.53836 | -2.94392 | -2.55397 | -2.2871 | -1.99373 | -1.43558 | -0.563587 |
| tossup | end_difficulty_d2 | 1240 | -2.24001 | 0.468833 | -3.62806 | -2.94811 | -2.5411 | -2.2723 | -1.95993 | -1.4172 | -0.398428 |
| tossup | end_difficulty_d3 | 1240 | -2.274 | 0.456796 | -3.75421 | -2.98104 | -2.58578 | -2.299 | -1.99897 | -1.50072 | -0.46878 |
| tossup | total_drop_d1 | 1240 | 0.995024 | 0.135412 | 0.660032 | 0.809732 | 0.916915 | 0.98967 | 1.06575 | 1.17317 | 2.7949 |
| tossup | total_drop_d2 | 1240 | 0.988264 | 0.122911 | 0.619437 | 0.799606 | 0.914525 | 0.984749 | 1.05937 | 1.17823 | 1.87632 |
| tossup | total_drop_d3 | 1240 | 0.995867 | 0.122924 | 0.684053 | 0.817966 | 0.91727 | 0.985353 | 1.06317 | 1.19096 | 1.82201 |
| tossup | drop_share_1_d1 | 1240 | 0.304499 | 0.0198338 | 0.17434 | 0.272529 | 0.293979 | 0.304577 | 0.317186 | 0.335038 | 0.38712 |
| tossup | drop_share_2_d1 | 1240 | 0.347119 | 0.0143851 | 0.299917 | 0.326184 | 0.338772 | 0.346989 | 0.355262 | 0.367638 | 0.512648 |
| tossup | drop_share_3_d1 | 1240 | 0.348382 | 0.0210638 | 0.238073 | 0.318795 | 0.335518 | 0.34747 | 0.359905 | 0.379909 | 0.507146 |
| tossup | drop_share_1_d2 | 1240 | 0.304115 | 0.0188961 | 0.19794 | 0.274106 | 0.293124 | 0.304462 | 0.315626 | 0.333052 | 0.372341 |
| tossup | drop_share_2_d2 | 1240 | 0.346952 | 0.0132368 | 0.302231 | 0.326311 | 0.338381 | 0.346502 | 0.35498 | 0.367665 | 0.417203 |
| tossup | drop_share_3_d2 | 1240 | 0.348932 | 0.0198747 | 0.274061 | 0.319404 | 0.336643 | 0.348541 | 0.359505 | 0.379699 | 0.479769 |
| tossup | drop_share_1_d3 | 1240 | 0.304084 | 0.0196111 | 0.210621 | 0.271638 | 0.293117 | 0.3046 | 0.317458 | 0.332997 | 0.368792 |
| tossup | drop_share_2_d3 | 1240 | 0.347341 | 0.0127995 | 0.305733 | 0.327839 | 0.338981 | 0.346746 | 0.355048 | 0.368981 | 0.402829 |
| tossup | drop_share_3_d3 | 1240 | 0.348575 | 0.0200553 | 0.289712 | 0.318877 | 0.336196 | 0.347442 | 0.359816 | 0.381656 | 0.47103 |
| tossup | r_1 | 1240 | 0.658936 | 0.313451 | 0.158336 | 0.312421 | 0.434089 | 0.585926 | 0.801932 | 1.21439 | 2.55443 |
| tossup | r_2 | 1240 | 0.675832 | 0.310134 | 0.177392 | 0.31883 | 0.454472 | 0.613013 | 0.826163 | 1.28518 | 2.30323 |
| tossup | r_3 | 1240 | 0.676933 | 0.326832 | 0.203031 | 0.308916 | 0.442136 | 0.602269 | 0.819287 | 1.35816 | 2.3179 |
| tossup | r_norm | 1240 | 1.2354 | 0.352269 | 0.417781 | 0.741493 | 0.970137 | 1.19164 | 1.44911 | 1.8823 | 2.70245 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 0.634357 | 0.279103 | -0.161415 | 0.163841 | 0.430838 | 0.634279 | 0.828628 | 1.08799 | 1.33884 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 0.645375 | 0.267491 | -0.367603 | 0.186397 | 0.465423 | 0.656909 | 0.838961 | 1.06402 | 1.31705 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 0.636156 | 0.288269 | -0.483603 | 0.173633 | 0.433929 | 0.619642 | 0.830025 | 1.12416 | 1.56484 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.756377 | 0.529881 | -2.7107 | -1.63336 | -1.08664 | -0.738375 | -0.369074 | 0.0715602 | 0.506608 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.733452 | 0.502258 | -3.09572 | -1.59235 | -1.06704 | -0.700902 | -0.360357 | 0.0282333 | 0.37809 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.825031 | 0.606378 | -3.47136 | -1.78959 | -1.22527 | -0.834859 | -0.398579 | 0.156018 | 0.894127 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 1.39073 | 0.412726 | 0.732101 | 0.910844 | 1.05705 | 1.31501 | 1.61393 | 2.14859 | 3.20714 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.37883 | 0.432855 | 0.701927 | 0.906087 | 1.04868 | 1.26679 | 1.60328 | 2.22552 | 3.53902 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 1.46119 | 0.497933 | 0.670717 | 0.905662 | 1.05339 | 1.35044 | 1.75702 | 2.35027 | 4.02548 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.245957 | 0.067082 | 0.0773304 | 0.149275 | 0.203288 | 0.244872 | 0.279183 | 0.347927 | 0.750366 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.304158 | 0.0587818 | 0.0953957 | 0.194079 | 0.272859 | 0.316596 | 0.339969 | 0.382688 | 0.561503 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.449885 | 0.105267 | 0.0713429 | 0.300971 | 0.379948 | 0.43288 | 0.512832 | 0.643334 | 0.821867 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.24656 | 0.0674943 | 0.0684594 | 0.141824 | 0.206638 | 0.249694 | 0.279646 | 0.341265 | 0.737752 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.304374 | 0.0587734 | 0.0889347 | 0.189556 | 0.274658 | 0.316151 | 0.339658 | 0.381938 | 0.549755 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.449066 | 0.105408 | 0.105445 | 0.309239 | 0.382066 | 0.429674 | 0.503135 | 0.650925 | 0.823628 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.246367 | 0.0739248 | 0.0553034 | 0.137052 | 0.197219 | 0.246991 | 0.284453 | 0.370267 | 0.649669 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.302075 | 0.0592968 | 0.0985341 | 0.187426 | 0.266528 | 0.313497 | 0.339195 | 0.38278 | 0.518156 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.451559 | 0.112615 | 0.0564886 | 0.296096 | 0.378289 | 0.429255 | 0.522641 | 0.660596 | 0.827375 |
| tossup_hazard | hazard_r_1 | 1240 | 1.41731 | 0.752825 | 0.226046 | 0.513094 | 0.864026 | 1.2156 | 1.80703 | 2.98355 | 4.87204 |
| tossup_hazard | hazard_r_2 | 1240 | 1.37467 | 0.740654 | 0.229245 | 0.537014 | 0.845911 | 1.17844 | 1.71542 | 2.98442 | 5.50651 |
| tossup_hazard | hazard_r_3 | 1240 | 1.42668 | 0.703716 | 0.197396 | 0.440375 | 0.881435 | 1.35416 | 1.8462 | 2.71943 | 4.24447 |
