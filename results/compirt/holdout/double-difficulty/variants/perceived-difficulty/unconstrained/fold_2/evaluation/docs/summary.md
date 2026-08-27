# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/unconstrained/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/unconstrained/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 337589 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.6581 |
| log_loss | 0.52133 |
| ece | 0.040565 |
| brier | 0.171117 |
| accuracy | 0.763422 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.000756185 |
| probability_std | 0.141076 |
| probability_p10 | 0.529679 |
| probability_p50 | 0.759118 |
| probability_p90 | 0.892019 |
| mean_predictive_variance | 0.175642 |
| integrated_brier_score | 0.16566 |
| joint_tossup_event_log_loss | 7.59068 |
| buzz_position_mae | 0.323343 |
| buzz_position_median_absolute_error | 0.321944 |
| buzz_position_bias | -0.307388 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.354218 |
| first_buzzer_mean_reciprocal_rank | 0.565649 |
| first_buzzer_log_loss | 1.67754 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.6581 |
| neg_average_precision | 0.381889 |
| neg_precision | 0.495132 |
| neg_recall | 0.163078 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0335375 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.222787 |
| no_buzz_calibration_error | 0.209674 |
| no_buzz_brier | 0.0662907 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.6581 | 0.52133 | 0.040565 | 0.171117 | 0.763422 | 0.764178 | -0.000756185 | 0.141076 | 0.529679 | 0.759118 | 0.892019 | 0.175642 |
| tossup_correctness | tier | fall | 2798 | 0.647501 | 0.495346 | 0.0223425 | 0.159719 | 0.789135 | 0.785204 | 0.00393138 | 0.111511 | 0.629895 | 0.807859 | 0.909156 | 0.156062 |
| tossup_correctness | tier | nationals | 1545 | 0.673893 | 0.579403 | 0.104552 | 0.197779 | 0.706149 | 0.721036 | -0.0148867 | 0.156116 | 0.415021 | 0.620176 | 0.824969 | 0.212059 |
| tossup_correctness | tier | regionals | 2039 | 0.664818 | 0.522828 | 0.0487995 | 0.172002 | 0.763119 | 0.762138 | 0.000980873 | 0.13146 | 0.529112 | 0.73359 | 0.866019 | 0.187013 |
| tossup_correctness | tier | winter | 2875 | 0.653713 | 0.514349 | 0.0350089 | 0.167252 | 0.769391 | 0.768348 | 0.00104348 | 0.125285 | 0.584015 | 0.780671 | 0.900009 | 0.167064 |
| tossup_correctness | category | Current Events | 129 | 0.633856 | 0.610938 | 0.0717262 | 0.210543 | 0.705426 | 0.666667 | 0.0387597 | 0.123451 | 0.508362 | 0.705321 | 0.844153 | 0.198382 |
| tossup_correctness | category | Fine Arts | 1074 | 0.624995 | 0.522141 | 0.0507722 | 0.170905 | 0.767225 | 0.776536 | -0.00931099 | 0.132678 | 0.539104 | 0.765832 | 0.881246 | 0.175685 |
| tossup_correctness | category | Geography | 180 | 0.720721 | 0.604915 | 0.0800969 | 0.206792 | 0.705556 | 0.616667 | 0.0888889 | 0.159739 | 0.438704 | 0.723441 | 0.873913 | 0.188043 |
| tossup_correctness | category | History | 1454 | 0.664752 | 0.525158 | 0.040451 | 0.172747 | 0.757909 | 0.757909 | 0 | 0.143556 | 0.547115 | 0.786413 | 0.919529 | 0.163582 |
| tossup_correctness | category | Literature | 1435 | 0.639437 | 0.468602 | 0.0365363 | 0.147734 | 0.810453 | 0.810453 | 0 | 0.11533 | 0.629962 | 0.809966 | 0.911078 | 0.154454 |
| tossup_correctness | category | Mythology | 324 | 0.618561 | 0.502741 | 0.075055 | 0.162729 | 0.783951 | 0.79321 | -0.00925926 | 0.133767 | 0.562588 | 0.779197 | 0.898176 | 0.167553 |
| tossup_correctness | category | Other Academic | 71 | 0.374728 | 0.648384 | 0.148705 | 0.226108 | 0.647887 | 0.760563 | -0.112676 | 0.120891 | 0.481938 | 0.675253 | 0.807298 | 0.209283 |
| tossup_correctness | category | Philosophy | 310 | 0.677336 | 0.511297 | 0.0246539 | 0.168143 | 0.76129 | 0.76129 | 0 | 0.119424 | 0.584402 | 0.759726 | 0.878955 | 0.17597 |
| tossup_correctness | category | Popular Culture | 108 | 0.572049 | 0.422446 | 0.148883 | 0.127234 | 0.87037 | 0.888889 | -0.0185185 | 0.107776 | 0.604078 | 0.757874 | 0.855178 | 0.180781 |
| tossup_correctness | category | Religion | 361 | 0.640908 | 0.553426 | 0.0617839 | 0.186277 | 0.720222 | 0.742382 | -0.0221607 | 0.153027 | 0.477965 | 0.723698 | 0.87374 | 0.186549 |
| tossup_correctness | category | Science | 1445 | 0.661908 | 0.543463 | 0.0572333 | 0.181078 | 0.73564 | 0.746021 | -0.0103806 | 0.163215 | 0.460081 | 0.733396 | 0.887789 | 0.18242 |
| tossup_correctness | category | Social Science | 327 | 0.696161 | 0.542109 | 0.0856244 | 0.179388 | 0.767584 | 0.718654 | 0.0489297 | 0.135991 | 0.515164 | 0.713846 | 0.857347 | 0.192114 |
| tossup_correctness | category | Unknown | 2039 | 0.664818 | 0.522828 | 0.0487995 | 0.172002 | 0.763119 | 0.762138 | 0.000980873 | 0.13146 | 0.529112 | 0.73359 | 0.866019 | 0.187013 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.639237 | 0.554613 | 0.0803384 | 0.184407 | 0.721311 | 0.743169 | -0.0218579 | 0.135753 | 0.494075 | 0.737705 | 0.863591 | 0.187468 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.634469 | 0.569081 | 0.0293827 | 0.191433 | 0.726702 | 0.728796 | -0.00209424 | 0.136983 | 0.515182 | 0.741541 | 0.865605 | 0.185348 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.668583 | 0.524783 | 0.0311283 | 0.173162 | 0.756141 | 0.752568 | 0.00357302 | 0.135448 | 0.539177 | 0.760635 | 0.888154 | 0.176355 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.66539 | 0.495501 | 0.0474706 | 0.160165 | 0.785739 | 0.786087 | -0.000347826 | 0.141689 | 0.535505 | 0.772088 | 0.896855 | 0.171607 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.649875 | 0.526268 | 0.0496716 | 0.172805 | 0.76173 | 0.764393 | -0.00266223 | 0.14536 | 0.522311 | 0.756749 | 0.898139 | 0.175167 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | -2.00251 | 0.710059 | -4.6457 | -3.19503 | -2.48068 | -1.99782 | -1.46604 | -0.826508 | -0.323824 |
| player | theta_2 | 1197 | -1.361 | 0.738465 | -3.99636 | -2.67545 | -1.86864 | -1.29006 | -0.757647 | -0.337743 | 0.188747 |
| player | theta_3 | 1197 | -1.02872 | 0.792314 | -3.57439 | -2.65497 | -1.40065 | -0.758609 | -0.423714 | -0.172184 | 0.338179 |
| player | alpha_1 | 1197 | -0.902644 | 0.668579 | -3.00408 | -2.01889 | -1.3195 | -0.923295 | -0.44812 | 0.220923 | 0.785453 |
| player | alpha_2 | 1197 | -0.15884 | 0.98989 | -2.8147 | -1.65165 | -0.823163 | -0.25106 | 0.478074 | 1.69872 | 3.2231 |
| player | alpha_3 | 1197 | 0.277025 | 0.938014 | -2.71033 | -1.31314 | -0.296896 | 0.322278 | 0.851886 | 1.83168 | 2.9391 |
| player | beta_1 | 1197 | -2.24704 | 1.07271 | -5.90412 | -4.45655 | -2.80854 | -2.05078 | -1.45067 | -0.813427 | -0.328845 |
| player | beta_2 | 1197 | -1.51869 | 0.819265 | -4.33806 | -2.95501 | -2.07991 | -1.46045 | -0.814952 | -0.327897 | -0.0821741 |
| player | beta_3 | 1197 | -1.27844 | 1.19099 | -5.79377 | -3.96843 | -1.64213 | -0.814038 | -0.455248 | -0.185297 | 0.159456 |
| player | theta_norm | 1197 | 2.81273 | 0.828023 | 1.15504 | 1.50831 | 2.19473 | 2.75914 | 3.37935 | 4.26739 | 5.29225 |
| tossup | start_difficulty_d1 | 1240 | -2.46231 | 0.957747 | -4.85712 | -3.89953 | -3.15921 | -2.55191 | -1.75958 | -0.756958 | -0.122874 |
| tossup | start_difficulty_d2 | 1240 | -0.862317 | 1.42711 | -5.03979 | -3.89262 | -1.33562 | -0.249092 | 0.11504 | 0.465837 | 0.850942 |
| tossup | start_difficulty_d3 | 1240 | -0.667844 | 0.895327 | -2.82954 | -2.18735 | -1.36033 | -0.581285 | 0.0566964 | 0.620177 | 1.35848 |
| tossup | end_difficulty_d1 | 1240 | -3.33507 | 1.00695 | -7.4798 | -4.84552 | -3.98899 | -3.47187 | -2.59222 | -1.57796 | -0.977979 |
| tossup | end_difficulty_d2 | 1240 | -1.98576 | 1.48513 | -10.8146 | -4.64848 | -3.08844 | -1.37868 | -0.884601 | -0.479875 | -0.0593361 |
| tossup | end_difficulty_d3 | 1240 | -1.97861 | 1.38417 | -10.6351 | -4.23527 | -2.60432 | -1.70995 | -1.01706 | -0.396758 | 0.49312 |
| tossup | total_drop_d1 | 1240 | 0.872755 | 0.467137 | 0.265134 | 0.426642 | 0.613951 | 0.781331 | 0.988163 | 1.61745 | 5.33307 |
| tossup | total_drop_d2 | 1240 | 1.12344 | 0.781152 | 0.345357 | 0.459744 | 0.905392 | 1.0074 | 1.14447 | 2.11968 | 9.05374 |
| tossup | total_drop_d3 | 1240 | 1.31077 | 1.04006 | 0.674382 | 0.84354 | 0.937028 | 1.03326 | 1.25257 | 2.42778 | 11.3035 |
| tossup | drop_share_1_d1 | 1240 | 0.344429 | 0.0317663 | 0.207655 | 0.298967 | 0.32243 | 0.341358 | 0.362588 | 0.400322 | 0.474948 |
| tossup | drop_share_2_d1 | 1240 | 0.325567 | 0.0194672 | 0.265424 | 0.293168 | 0.313037 | 0.326164 | 0.338458 | 0.354441 | 0.420703 |
| tossup | drop_share_3_d1 | 1240 | 0.330004 | 0.0306867 | 0.234193 | 0.279173 | 0.310084 | 0.330259 | 0.348222 | 0.379521 | 0.461796 |
| tossup | drop_share_1_d2 | 1240 | 0.30761 | 0.032459 | 0.132575 | 0.270846 | 0.294328 | 0.304478 | 0.316319 | 0.372088 | 0.451495 |
| tossup | drop_share_2_d2 | 1240 | 0.342742 | 0.0246319 | 0.272951 | 0.294297 | 0.334685 | 0.346565 | 0.356623 | 0.374314 | 0.461971 |
| tossup | drop_share_3_d2 | 1240 | 0.349648 | 0.0299842 | 0.226596 | 0.303871 | 0.33682 | 0.34806 | 0.359032 | 0.400212 | 0.565287 |
| tossup | drop_share_1_d3 | 1240 | 0.310484 | 0.0315401 | 0.0684149 | 0.269918 | 0.299332 | 0.313139 | 0.326608 | 0.348066 | 0.415351 |
| tossup | drop_share_2_d3 | 1240 | 0.34921 | 0.0194717 | 0.185352 | 0.328163 | 0.339024 | 0.347 | 0.355099 | 0.379877 | 0.488619 |
| tossup | drop_share_3_d3 | 1240 | 0.340305 | 0.0314645 | 0.212549 | 0.304135 | 0.326602 | 0.340574 | 0.351588 | 0.366644 | 0.746233 |
| tossup | r_1 | 1240 | 0.576201 | 0.261723 | 0.0384045 | 0.089645 | 0.313125 | 0.703788 | 0.773457 | 0.841565 | 0.937987 |
| tossup | r_2 | 1240 | 0.241259 | 0.270404 | 0.0295029 | 0.0496338 | 0.0710776 | 0.108281 | 0.209622 | 0.824091 | 0.926997 |
| tossup | r_3 | 1240 | 0.18254 | 0.160049 | 0.0211651 | 0.0401809 | 0.076975 | 0.128788 | 0.217268 | 0.596731 | 0.788758 |
| tossup | r_norm | 1240 | 0.765925 | 0.0631951 | 0.609272 | 0.662296 | 0.721207 | 0.768697 | 0.809247 | 0.868266 | 0.939028 |
