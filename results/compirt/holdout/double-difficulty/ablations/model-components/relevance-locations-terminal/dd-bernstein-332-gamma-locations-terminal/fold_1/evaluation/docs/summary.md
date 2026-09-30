# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-gamma-locations-terminal/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-gamma-locations-terminal/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 283812 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.708573 |
| log_loss | 0.510577 |
| ece | 0.0464963 |
| brier | 0.163692 |
| accuracy | 0.770263 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00813813 |
| probability_std | 0.189299 |
| probability_p10 | 0.46735 |
| probability_p50 | 0.779042 |
| probability_p90 | 0.952115 |
| mean_predictive_variance | 0.156117 |
| integrated_brier_score | 0.093305 |
| joint_tossup_event_log_loss | 6.43337 |
| buzz_position_mae | 0.13501 |
| buzz_position_median_absolute_error | 0.109463 |
| buzz_position_bias | 0.00616906 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.382272 |
| first_buzzer_mean_reciprocal_rank | 0.589764 |
| first_buzzer_log_loss | 1.61473 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.708573 |
| neg_average_precision | 0.454318 |
| neg_precision | 0.534196 |
| neg_recall | 0.267221 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.195413 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.00955151 |
| no_buzz_calibration_error | -0.00635758 |
| no_buzz_brier | 0.0150834 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.708573 | 0.510577 | 0.0464963 | 0.163692 | 0.770263 | 0.762125 | 0.00813813 | 0.189299 | 0.46735 | 0.779042 | 0.952115 | 0.156117 |
| tossup_correctness | tier | fall | 2842 | 0.724961 | 0.475354 | 0.0451529 | 0.152011 | 0.787122 | 0.785362 | 0.00175932 | 0.184 | 0.493834 | 0.798692 | 0.955936 | 0.149681 |
| tossup_correctness | tier | nationals | 1564 | 0.704283 | 0.560377 | 0.0443493 | 0.181119 | 0.747442 | 0.718031 | 0.0294118 | 0.199809 | 0.430999 | 0.750888 | 0.950947 | 0.162212 |
| tossup_correctness | tier | regionals | 1937 | 0.688812 | 0.533439 | 0.0535517 | 0.169924 | 0.761487 | 0.758389 | 0.00309757 | 0.188055 | 0.463447 | 0.762544 | 0.952108 | 0.159405 |
| tossup_correctness | tier | winter | 2750 | 0.705456 | 0.502552 | 0.0503276 | 0.161462 | 0.772 | 0.765818 | 0.00618182 | 0.187843 | 0.473914 | 0.78097 | 0.94836 | 0.156986 |
| tossup_correctness | category | Current Events | 126 | 0.710274 | 0.498773 | 0.0912261 | 0.165325 | 0.761905 | 0.769841 | -0.00793651 | 0.17947 | 0.428558 | 0.704433 | 0.921069 | 0.178795 |
| tossup_correctness | category | Fine Arts | 1071 | 0.746397 | 0.472834 | 0.0353034 | 0.152758 | 0.785247 | 0.766573 | 0.0186741 | 0.192098 | 0.460398 | 0.780189 | 0.951411 | 0.15587 |
| tossup_correctness | category | Geography | 185 | 0.800249 | 0.51193 | 0.0887169 | 0.164408 | 0.778378 | 0.697297 | 0.0810811 | 0.252922 | 0.224491 | 0.705143 | 0.940572 | 0.16744 |
| tossup_correctness | category | History | 1440 | 0.719674 | 0.513184 | 0.0438502 | 0.164897 | 0.760417 | 0.754167 | 0.00625 | 0.190533 | 0.465985 | 0.786988 | 0.960147 | 0.153911 |
| tossup_correctness | category | Literature | 1422 | 0.662241 | 0.475459 | 0.0570049 | 0.148911 | 0.798875 | 0.814346 | -0.0154712 | 0.165832 | 0.547154 | 0.819908 | 0.955644 | 0.143988 |
| tossup_correctness | category | Mythology | 318 | 0.637153 | 0.511678 | 0.0761865 | 0.160475 | 0.798742 | 0.789308 | 0.00943396 | 0.163076 | 0.545481 | 0.821649 | 0.948936 | 0.145538 |
| tossup_correctness | category | Other Academic | 66 | 0.826428 | 0.475402 | 0.159748 | 0.160422 | 0.742424 | 0.712121 | 0.030303 | 0.167138 | 0.544954 | 0.774127 | 0.906794 | 0.170012 |
| tossup_correctness | category | Philosophy | 311 | 0.729703 | 0.509356 | 0.0543284 | 0.170204 | 0.736334 | 0.745981 | -0.0096463 | 0.187173 | 0.500429 | 0.793104 | 0.972592 | 0.149316 |
| tossup_correctness | category | Popular Culture | 102 | 0.496296 | 0.409363 | 0.0906035 | 0.116941 | 0.882353 | 0.882353 | 0 | 0.11513 | 0.656019 | 0.847367 | 0.936514 | 0.136387 |
| tossup_correctness | category | Religion | 358 | 0.693965 | 0.584876 | 0.0555153 | 0.191355 | 0.723464 | 0.712291 | 0.0111732 | 0.198233 | 0.39328 | 0.736339 | 0.916933 | 0.172108 |
| tossup_correctness | category | Science | 1433 | 0.701364 | 0.537809 | 0.0436866 | 0.174503 | 0.752966 | 0.738311 | 0.0146546 | 0.193642 | 0.451557 | 0.760454 | 0.949541 | 0.160982 |
| tossup_correctness | category | Social Science | 324 | 0.766332 | 0.481595 | 0.0639157 | 0.154949 | 0.79321 | 0.731481 | 0.0617284 | 0.201652 | 0.395937 | 0.75074 | 0.915695 | 0.166147 |
| tossup_correctness | category | Unknown | 1937 | 0.688812 | 0.533439 | 0.0535517 | 0.169924 | 0.761487 | 0.758389 | 0.00309757 | 0.188055 | 0.463447 | 0.762544 | 0.952108 | 0.159405 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.623074 | 0.628713 | 0.107443 | 0.208177 | 0.670659 | 0.712575 | -0.0419162 | 0.194512 | 0.409935 | 0.67184 | 0.922617 | 0.1858 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.717226 | 0.539658 | 0.0606322 | 0.178725 | 0.735746 | 0.729167 | 0.00657895 | 0.220077 | 0.363915 | 0.728702 | 0.928811 | 0.168469 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.720346 | 0.512278 | 0.0399305 | 0.163236 | 0.77305 | 0.755083 | 0.0179669 | 0.185142 | 0.484695 | 0.7773 | 0.953547 | 0.156434 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.694029 | 0.497192 | 0.0444495 | 0.158091 | 0.781646 | 0.780942 | 0.000703235 | 0.172287 | 0.532407 | 0.793994 | 0.953198 | 0.152098 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.712125 | 0.50672 | 0.0481703 | 0.162302 | 0.773486 | 0.762029 | 0.0114566 | 0.192361 | 0.450668 | 0.784957 | 0.956452 | 0.154329 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 1.75983 | 0.667584 | -0.62361 | 0.702781 | 1.33797 | 1.77167 | 2.16531 | 2.82884 | 4.37279 |
| player | theta_1 | 1167 | -1.5338 | 0.673133 | -3.33961 | -2.53798 | -2.03163 | -1.57604 | -1.08975 | -0.330403 | 0.460639 |
| player | theta_2 | 1167 | -1.45632 | 0.622899 | -3.2227 | -2.40668 | -1.90532 | -1.47361 | -1.03898 | -0.394378 | 0.673335 |
| player | theta_3 | 1167 | -1.58735 | 0.686955 | -3.91126 | -2.72055 | -2.07539 | -1.56233 | -1.10432 | -0.490375 | 0.275397 |
| player | theta_norm | 1167 | 2.82909 | 0.549091 | 0.904334 | 1.86718 | 2.47798 | 2.83322 | 3.21746 | 3.74045 | 4.19709 |
| tossup | start_difficulty_d1 | 1220 | -1.2714 | 0.393951 | -2.43828 | -1.8782 | -1.5388 | -1.29683 | -1.03672 | -0.597064 | 0.286339 |
| tossup | start_difficulty_d2 | 1220 | -1.26632 | 0.398677 | -2.65965 | -1.87569 | -1.53432 | -1.29982 | -1.02626 | -0.556279 | 0.207116 |
| tossup | start_difficulty_d3 | 1220 | -1.28343 | 0.399416 | -2.51608 | -1.92598 | -1.5562 | -1.29865 | -1.02848 | -0.59589 | 0.00243047 |
| tossup | end_difficulty_d1 | 1220 | -2.26566 | 0.458501 | -3.61749 | -2.96857 | -2.58519 | -2.3026 | -2.00639 | -1.42351 | -0.461565 |
| tossup | end_difficulty_d2 | 1220 | -2.25731 | 0.458407 | -3.58985 | -2.97396 | -2.5693 | -2.28457 | -1.98741 | -1.4192 | -0.57401 |
| tossup | end_difficulty_d3 | 1220 | -2.27858 | 0.457317 | -3.71597 | -2.99348 | -2.59347 | -2.29164 | -2.00649 | -1.46397 | -0.732094 |
| tossup | total_drop_d1 | 1220 | 0.994259 | 0.12395 | 0.64213 | 0.803467 | 0.920262 | 0.988966 | 1.06489 | 1.1793 | 1.67941 |
| tossup | total_drop_d2 | 1220 | 0.99099 | 0.117552 | 0.606581 | 0.812721 | 0.916195 | 0.986556 | 1.05513 | 1.18968 | 1.75906 |
| tossup | total_drop_d3 | 1220 | 0.995151 | 0.122663 | 0.675876 | 0.819299 | 0.915314 | 0.98707 | 1.06199 | 1.1877 | 1.74291 |
| tossup | drop_share_1_d1 | 1220 | 0.304694 | 0.0194341 | 0.214897 | 0.273231 | 0.294076 | 0.305574 | 0.316799 | 0.334256 | 0.381876 |
| tossup | drop_share_2_d1 | 1220 | 0.34721 | 0.0130429 | 0.304198 | 0.326004 | 0.33905 | 0.34714 | 0.355004 | 0.36803 | 0.420204 |
| tossup | drop_share_3_d1 | 1220 | 0.348096 | 0.0204228 | 0.286181 | 0.318306 | 0.335752 | 0.347718 | 0.358814 | 0.382475 | 0.467143 |
| tossup | drop_share_1_d2 | 1220 | 0.303826 | 0.0190305 | 0.160597 | 0.272934 | 0.29352 | 0.304898 | 0.315365 | 0.332299 | 0.36844 |
| tossup | drop_share_2_d2 | 1220 | 0.346807 | 0.0131829 | 0.277918 | 0.326247 | 0.338327 | 0.346696 | 0.355187 | 0.367679 | 0.415625 |
| tossup | drop_share_3_d2 | 1220 | 0.349367 | 0.0204364 | 0.295346 | 0.320342 | 0.336987 | 0.348345 | 0.359454 | 0.381466 | 0.561485 |
| tossup | drop_share_1_d3 | 1220 | 0.303955 | 0.0195689 | 0.20068 | 0.273492 | 0.293182 | 0.305155 | 0.316317 | 0.332769 | 0.354707 |
| tossup | drop_share_2_d3 | 1220 | 0.34724 | 0.0129766 | 0.304521 | 0.326773 | 0.33923 | 0.347082 | 0.355057 | 0.368532 | 0.421276 |
| tossup | drop_share_3_d3 | 1220 | 0.348805 | 0.0202695 | 0.297675 | 0.319326 | 0.335846 | 0.347518 | 0.359381 | 0.38177 | 0.463886 |
| tossup | r_1 | 1220 | 0.652581 | 0.312097 | 0.193841 | 0.293984 | 0.43117 | 0.579607 | 0.801661 | 1.21417 | 2.61734 |
| tossup | r_2 | 1220 | 0.675881 | 0.28839 | 0.200169 | 0.315379 | 0.464199 | 0.625926 | 0.829865 | 1.19942 | 2.52929 |
| tossup | r_3 | 1220 | 0.678177 | 0.335985 | 0.19327 | 0.311341 | 0.447235 | 0.588465 | 0.822419 | 1.31194 | 2.6654 |
| tossup | r_norm | 1220 | 1.228 | 0.357692 | 0.458326 | 0.741939 | 0.975597 | 1.19466 | 1.43452 | 1.84544 | 2.83361 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 0.631521 | 0.278922 | -0.215279 | 0.160745 | 0.432807 | 0.643801 | 0.832572 | 1.08312 | 1.39465 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 0.637251 | 0.25138 | -0.160157 | 0.195078 | 0.475653 | 0.648975 | 0.814987 | 1.03723 | 1.40655 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 0.62357 | 0.287779 | -0.476971 | 0.156392 | 0.431267 | 0.621818 | 0.81721 | 1.10657 | 1.37636 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | -0.763813 | 0.526268 | -2.70944 | -1.59894 | -1.10915 | -0.774577 | -0.386583 | 0.0833665 | 0.437733 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | -0.744729 | 0.480109 | -2.41336 | -1.58974 | -1.05339 | -0.713336 | -0.401816 | -0.0187426 | 0.316765 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | -0.864572 | 0.595978 | -3.18603 | -1.75256 | -1.23022 | -0.922675 | -0.442914 | 0.130989 | 0.469217 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 1.39533 | 0.407795 | 0.66846 | 0.910864 | 1.06305 | 1.33945 | 1.62054 | 2.15245 | 3.33565 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 1.38198 | 0.425837 | 0.700852 | 0.91206 | 1.05406 | 1.27171 | 1.5988 | 2.20454 | 3.27228 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 1.48814 | 0.488364 | 0.675826 | 0.907424 | 1.09479 | 1.40607 | 1.77628 | 2.35582 | 3.68194 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.247036 | 0.0689608 | 0.0774262 | 0.148788 | 0.201901 | 0.245042 | 0.28156 | 0.353375 | 0.694355 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.302758 | 0.0598888 | 0.0888364 | 0.18843 | 0.265215 | 0.315426 | 0.342109 | 0.383404 | 0.524569 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.450205 | 0.106602 | 0.103287 | 0.301443 | 0.377377 | 0.43307 | 0.516935 | 0.642165 | 0.833737 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.245109 | 0.061909 | 0.0825164 | 0.141781 | 0.206344 | 0.249594 | 0.279406 | 0.335039 | 0.57373 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.30681 | 0.0561814 | 0.0814687 | 0.199922 | 0.277606 | 0.317134 | 0.340656 | 0.383154 | 0.548766 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.448081 | 0.10243 | 0.107206 | 0.314728 | 0.380879 | 0.428939 | 0.500396 | 0.644372 | 0.836015 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.245152 | 0.076379 | 0.0586278 | 0.132267 | 0.193304 | 0.241279 | 0.285931 | 0.375103 | 0.68375 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.299731 | 0.0615697 | 0.0912973 | 0.186778 | 0.263851 | 0.311674 | 0.340171 | 0.386204 | 0.510194 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.455117 | 0.115805 | 0.0738755 | 0.291694 | 0.375051 | 0.436031 | 0.531952 | 0.665324 | 0.850075 |
| tossup_hazard | hazard_r_1 | 1220 | 1.46102 | 0.773521 | 0.252524 | 0.481528 | 0.842546 | 1.28207 | 1.96215 | 2.91841 | 4.14179 |
| tossup_hazard | hazard_r_2 | 1220 | 1.28381 | 0.654551 | 0.238918 | 0.539879 | 0.828801 | 1.10499 | 1.55687 | 2.62548 | 4.78006 |
| tossup_hazard | hazard_r_3 | 1220 | 1.49307 | 0.71446 | 0.175447 | 0.420961 | 0.935925 | 1.47264 | 1.97701 | 2.74656 | 4.01471 |
