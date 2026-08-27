# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-330p67-simplex-locations-terminal/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-330p67-simplex-locations-terminal/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 283266 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.717208 |
| log_loss | 0.488918 |
| ece | 0.0109146 |
| brier | 0.158905 |
| accuracy | 0.776547 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0112964 |
| probability_std | 0.140958 |
| probability_p10 | 0.575977 |
| probability_p50 | 0.8129 |
| probability_p90 | 0.916634 |
| mean_predictive_variance | 0.154817 |
| integrated_brier_score | 0.101528 |
| joint_tossup_event_log_loss | 6.6213 |
| buzz_position_mae | 0.150281 |
| buzz_position_median_absolute_error | 0.133162 |
| buzz_position_bias | -0.0359489 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.352663 |
| first_buzzer_mean_reciprocal_rank | 0.566423 |
| first_buzzer_log_loss | 1.6687 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.717208 |
| neg_average_precision | 0.450046 |
| neg_precision | 0.59962 |
| neg_recall | 0.144821 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.196489 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0164849 |
| no_buzz_calibration_error | 0.00321531 |
| no_buzz_brier | 0.0132672 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.717208 | 0.488918 | 0.0109146 | 0.158905 | 0.776547 | 0.76525 | 0.0112964 | 0.140958 | 0.575977 | 0.8129 | 0.916634 | 0.154817 |
| tossup_correctness | tier | fall | 2933 | 0.71388 | 0.461859 | 0.0126913 | 0.147746 | 0.798159 | 0.791681 | 0.00647801 | 0.142359 | 0.575142 | 0.819695 | 0.921654 | 0.151226 |
| tossup_correctness | tier | nationals | 1584 | 0.711617 | 0.531064 | 0.039675 | 0.175557 | 0.748737 | 0.724747 | 0.0239899 | 0.147253 | 0.549096 | 0.806138 | 0.910606 | 0.159408 |
| tossup_correctness | tier | regionals | 1886 | 0.712447 | 0.514484 | 0.0247751 | 0.170183 | 0.755567 | 0.746023 | 0.00954401 | 0.134118 | 0.579947 | 0.797135 | 0.906999 | 0.161129 |
| tossup_correctness | tier | winter | 2892 | 0.72294 | 0.476603 | 0.0174708 | 0.153748 | 0.783541 | 0.773167 | 0.0103734 | 0.139673 | 0.592814 | 0.816761 | 0.918349 | 0.151828 |
| tossup_correctness | category | Current Events | 124 | 0.674644 | 0.525515 | 0.09827 | 0.170041 | 0.774194 | 0.75 | 0.0241935 | 0.158002 | 0.542816 | 0.763112 | 0.919028 | 0.166857 |
| tossup_correctness | category | Fine Arts | 1103 | 0.711262 | 0.496211 | 0.0178864 | 0.16113 | 0.776065 | 0.759746 | 0.0163191 | 0.146101 | 0.582201 | 0.818119 | 0.920808 | 0.15216 |
| tossup_correctness | category | Geography | 197 | 0.784848 | 0.519258 | 0.0648072 | 0.171452 | 0.741117 | 0.670051 | 0.071066 | 0.209603 | 0.39863 | 0.738564 | 0.909571 | 0.169837 |
| tossup_correctness | category | History | 1491 | 0.728798 | 0.460617 | 0.0201263 | 0.147898 | 0.790744 | 0.787391 | 0.00335345 | 0.13444 | 0.584481 | 0.812781 | 0.919581 | 0.154132 |
| tossup_correctness | category | Literature | 1472 | 0.731193 | 0.436812 | 0.0276365 | 0.137425 | 0.8125 | 0.804348 | 0.00815217 | 0.116204 | 0.651811 | 0.846166 | 0.923121 | 0.138414 |
| tossup_correctness | category | Mythology | 332 | 0.688172 | 0.448829 | 0.0135909 | 0.141316 | 0.813253 | 0.813253 | 0 | 0.113461 | 0.640315 | 0.829305 | 0.913337 | 0.146083 |
| tossup_correctness | category | Other Academic | 69 | 0.692308 | 0.50667 | 0.0745669 | 0.166762 | 0.782609 | 0.753623 | 0.0289855 | 0.101029 | 0.641654 | 0.780076 | 0.894799 | 0.165228 |
| tossup_correctness | category | Philosophy | 324 | 0.695099 | 0.462788 | 0.0251475 | 0.147841 | 0.79321 | 0.799383 | -0.00617284 | 0.12316 | 0.609471 | 0.815377 | 0.920313 | 0.153146 |
| tossup_correctness | category | Popular Culture | 102 | 0.431142 | 0.483729 | 0.0565108 | 0.148099 | 0.823529 | 0.833333 | -0.00980392 | 0.0781629 | 0.739084 | 0.846852 | 0.904458 | 0.131964 |
| tossup_correctness | category | Religion | 372 | 0.720504 | 0.54064 | 0.0464437 | 0.182544 | 0.728495 | 0.709677 | 0.0188172 | 0.147629 | 0.527233 | 0.76501 | 0.905844 | 0.17081 |
| tossup_correctness | category | Science | 1487 | 0.690162 | 0.514327 | 0.0260806 | 0.168986 | 0.765299 | 0.752522 | 0.0127774 | 0.150365 | 0.538615 | 0.800879 | 0.914395 | 0.160141 |
| tossup_correctness | category | Social Science | 336 | 0.730127 | 0.537053 | 0.0479165 | 0.178718 | 0.732143 | 0.702381 | 0.0297619 | 0.176933 | 0.480213 | 0.787622 | 0.914373 | 0.163537 |
| tossup_correctness | category | Unknown | 1886 | 0.712447 | 0.514484 | 0.0247751 | 0.170183 | 0.755567 | 0.746023 | 0.00954401 | 0.134118 | 0.579947 | 0.797135 | 0.906999 | 0.161129 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.68992 | 0.52451 | 0.076157 | 0.16794 | 0.781726 | 0.736041 | 0.0456853 | 0.144155 | 0.532666 | 0.754142 | 0.887505 | 0.175902 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.717422 | 0.519235 | 0.026941 | 0.172247 | 0.744162 | 0.735025 | 0.00913706 | 0.143966 | 0.551858 | 0.793957 | 0.903236 | 0.163799 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.703333 | 0.493777 | 0.0169879 | 0.160624 | 0.773878 | 0.769436 | 0.00444247 | 0.138727 | 0.591627 | 0.813087 | 0.915875 | 0.153862 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.704534 | 0.474535 | 0.0116889 | 0.152466 | 0.794487 | 0.78402 | 0.0104676 | 0.132289 | 0.606636 | 0.826911 | 0.920773 | 0.148974 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.737728 | 0.486718 | 0.0221145 | 0.158794 | 0.771696 | 0.756008 | 0.0156876 | 0.147528 | 0.553902 | 0.810282 | 0.916265 | 0.156784 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 2.64789 | 0.734379 | 0.496445 | 1.45073 | 2.1523 | 2.63597 | 3.11228 | 3.92195 | 4.61044 |
| player | theta_1 | 1186 | -1.19493 | 0.844211 | -3.62584 | -2.5216 | -1.7255 | -1.25921 | -0.708101 | 0.318858 | 1.93058 |
| player | theta_2 | 1186 | -1.00739 | 0.657681 | -3.57169 | -2.0256 | -1.42778 | -1.0374 | -0.590768 | 0.0962935 | 1.12479 |
| player | theta_3 | 1186 | -1.09084 | 0.774046 | -3.28481 | -2.26199 | -1.60965 | -1.13949 | -0.622181 | 0.277932 | 2.32347 |
| player | theta_norm | 1186 | 2.23903 | 0.602153 | 0.169609 | 1.3388 | 1.83299 | 2.1924 | 2.61168 | 3.27946 | 4.36476 |
| tossup | start_difficulty_d1 | 1240 | -1.77157 | 0.54776 | -3.69875 | -2.51773 | -2.14966 | -1.83617 | -1.44901 | -0.832483 | 1.11019 |
| tossup | start_difficulty_d2 | 1240 | -1.76496 | 0.511325 | -3.21751 | -2.52451 | -2.11152 | -1.821 | -1.44297 | -0.801042 | 0.372042 |
| tossup | start_difficulty_d3 | 1240 | -1.76116 | 0.511686 | -3.57753 | -2.54932 | -2.12059 | -1.79761 | -1.43307 | -0.89711 | 1.14975 |
| tossup | end_difficulty_d1 | 1240 | -2.75924 | 0.637615 | -4.90629 | -3.6392 | -3.19856 | -2.84025 | -2.38723 | -1.66528 | 0.514941 |
| tossup | end_difficulty_d2 | 1240 | -2.75031 | 0.598175 | -4.5338 | -3.67648 | -3.15043 | -2.80594 | -2.37161 | -1.64981 | -0.269021 |
| tossup | end_difficulty_d3 | 1240 | -2.7439 | 0.595491 | -4.87109 | -3.68296 | -3.15963 | -2.77044 | -2.35344 | -1.76544 | 0.427283 |
| tossup | total_drop_d1 | 1240 | 0.987675 | 0.110634 | 0.59525 | 0.801949 | 0.91668 | 0.993221 | 1.06212 | 1.15099 | 1.47656 |
| tossup | total_drop_d2 | 1240 | 0.985347 | 0.102551 | 0.641063 | 0.818205 | 0.916395 | 0.988235 | 1.05413 | 1.1519 | 1.31629 |
| tossup | total_drop_d3 | 1240 | 0.982742 | 0.10252 | 0.62554 | 0.817526 | 0.91224 | 0.984998 | 1.04903 | 1.15479 | 1.36084 |
| tossup | drop_share_1_d1 | 1240 | 0.248877 | 0.0315352 | 0.103534 | 0.197058 | 0.230856 | 0.249681 | 0.269294 | 0.296434 | 0.391509 |
| tossup | drop_share_2_d1 | 1240 | 0.372597 | 0.0220245 | 0.274693 | 0.336467 | 0.358202 | 0.373196 | 0.387927 | 0.405289 | 0.495332 |
| tossup | drop_share_3_d1 | 1240 | 0.378525 | 0.0400259 | 0.249508 | 0.318821 | 0.351597 | 0.376413 | 0.402538 | 0.446906 | 0.589813 |
| tossup | drop_share_1_d2 | 1240 | 0.248047 | 0.0284684 | 0.150178 | 0.197818 | 0.230399 | 0.248409 | 0.267007 | 0.293466 | 0.343454 |
| tossup | drop_share_2_d2 | 1240 | 0.371927 | 0.0209593 | 0.280294 | 0.336855 | 0.358941 | 0.372459 | 0.385102 | 0.405663 | 0.451866 |
| tossup | drop_share_3_d2 | 1240 | 0.380025 | 0.0370034 | 0.260721 | 0.32217 | 0.355023 | 0.379175 | 0.402887 | 0.44299 | 0.540049 |
| tossup | drop_share_1_d3 | 1240 | 0.247968 | 0.030194 | 0.131931 | 0.199065 | 0.229405 | 0.248206 | 0.267366 | 0.295491 | 0.408254 |
| tossup | drop_share_2_d3 | 1240 | 0.37229 | 0.0207764 | 0.264499 | 0.340133 | 0.359077 | 0.372507 | 0.386452 | 0.405339 | 0.453142 |
| tossup | drop_share_3_d3 | 1240 | 0.379741 | 0.0377375 | 0.264083 | 0.32381 | 0.354652 | 0.377558 | 0.401643 | 0.444737 | 0.60357 |
| tossup | r_1 | 1240 | 0.320619 | 0.141295 | 0.0734791 | 0.134841 | 0.213513 | 0.293341 | 0.403564 | 0.585029 | 0.814358 |
| tossup | r_2 | 1240 | 0.33479 | 0.118902 | 0.0638417 | 0.158467 | 0.250601 | 0.322963 | 0.40128 | 0.548692 | 0.79537 |
| tossup | r_3 | 1240 | 0.344591 | 0.124662 | 0.0722749 | 0.155609 | 0.252911 | 0.33516 | 0.415215 | 0.58614 | 0.818584 |
| tossup | r_norm | 1240 | 0.617661 | 0.0415133 | 0.577361 | 0.579389 | 0.588048 | 0.604394 | 0.631906 | 0.705479 | 0.828744 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.42787 | 0.476149 | 1.88296 | 3.71622 | 4.16122 | 4.38926 | 4.67678 | 5.3151 | 6.27976 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.39723 | 0.426709 | 2.39616 | 3.71762 | 4.17354 | 4.37278 | 4.60315 | 5.10292 | 6.61313 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.42196 | 0.421398 | 2.53061 | 3.72472 | 4.19203 | 4.41233 | 4.64464 | 5.09453 | 6.3544 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.65441 | 2.40922 | -11.208 | -3.45213 | 0.480296 | 2.81327 | 3.25507 | 3.62229 | 4.22357 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.11408 | 2.24781 | -9.35664 | -3.32367 | 2.193 | 3.08171 | 3.34335 | 3.64326 | 4.29725 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.17607 | 2.26542 | -11.1739 | -3.06645 | 2.35003 | 3.1075 | 3.37276 | 3.69063 | 4.14689 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.77346 | 2.55589 | 0.899316 | 0.983935 | 1.05103 | 1.34884 | 4.12226 | 8.11729 | 15.9931 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.28315 | 2.38773 | 0.890158 | 0.963099 | 1.02488 | 1.16289 | 1.96609 | 8.03268 | 14.4795 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.24589 | 2.38036 | 0.856559 | 0.968192 | 1.02758 | 1.17143 | 1.86579 | 7.58599 | 16.3724 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.158212 | 0.0821469 | 0.0145554 | 0.0319724 | 0.0831516 | 0.174311 | 0.215275 | 0.270532 | 0.683809 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.327085 | 0.121898 | 0.0203832 | 0.0882719 | 0.28835 | 0.343841 | 0.377939 | 0.499619 | 0.866259 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.514703 | 0.173516 | 0.0750517 | 0.295307 | 0.405722 | 0.47135 | 0.593298 | 0.872342 | 0.965061 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.173578 | 0.0751854 | 0.0106903 | 0.0324274 | 0.127625 | 0.190198 | 0.223014 | 0.268024 | 0.707857 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.338541 | 0.105818 | 0.0242248 | 0.102115 | 0.311701 | 0.344725 | 0.376419 | 0.498949 | 0.856782 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.48788 | 0.148753 | 0.0513877 | 0.3099 | 0.40719 | 0.452588 | 0.528794 | 0.855341 | 0.960672 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.171314 | 0.0725099 | 0.012774 | 0.0341835 | 0.127198 | 0.185039 | 0.21927 | 0.263879 | 0.650895 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.33939 | 0.104072 | 0.035022 | 0.130217 | 0.308935 | 0.344622 | 0.376399 | 0.499899 | 0.850294 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.489296 | 0.143874 | 0.0687714 | 0.31782 | 0.407273 | 0.460467 | 0.532792 | 0.826766 | 0.952204 |
| tossup_hazard | hazard_r_1 | 1240 | 0.385971 | 0.269051 | 0.0336594 | 0.0608627 | 0.136136 | 0.322466 | 0.611676 | 0.855943 | 0.932846 |
| tossup_hazard | hazard_r_2 | 1240 | 0.301191 | 0.215026 | 0.0244261 | 0.0546712 | 0.121959 | 0.234218 | 0.469365 | 0.709925 | 0.854253 |
| tossup_hazard | hazard_r_3 | 1240 | 0.312838 | 0.225061 | 0.0245135 | 0.0490197 | 0.130734 | 0.253286 | 0.446626 | 0.771587 | 0.937428 |
