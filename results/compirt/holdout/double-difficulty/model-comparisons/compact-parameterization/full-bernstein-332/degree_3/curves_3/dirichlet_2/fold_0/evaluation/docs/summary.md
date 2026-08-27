# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/compact-vs-332/bernstein332/degree_3/curves_3/dirichlet_2/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/compact-vs-332/bernstein332/degree_3/curves_3/dirichlet_2/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 286419 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.714173 |
| log_loss | 0.508628 |
| ece | 0.0684723 |
| brier | 0.165719 |
| accuracy | 0.760194 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.00505648 |
| probability_std | 0.202362 |
| probability_p10 | 0.416791 |
| probability_p50 | 0.750111 |
| probability_p90 | 0.945069 |
| mean_predictive_variance | 0.164328 |
| integrated_brier_score | 0.0946731 |
| joint_tossup_event_log_loss | 6.45348 |
| buzz_position_mae | 0.137196 |
| buzz_position_median_absolute_error | 0.111077 |
| buzz_position_bias | 0.00855097 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.382571 |
| first_buzzer_mean_reciprocal_rank | 0.589728 |
| first_buzzer_log_loss | 1.61719 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.714173 |
| neg_average_precision | 0.451851 |
| neg_precision | 0.484984 |
| neg_recall | 0.347846 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.188906 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00913144 |
| no_buzz_calibration_error | -0.0041382 |
| no_buzz_brier | 0.0123741 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.714173 | 0.508628 | 0.0684723 | 0.165719 | 0.760194 | 0.76525 | -0.00505648 | 0.202362 | 0.416791 | 0.750111 | 0.945069 | 0.164328 |
| tossup_correctness | tier | fall | 2933 | 0.706102 | 0.487491 | 0.0757304 | 0.15616 | 0.776338 | 0.791681 | -0.0153427 | 0.195219 | 0.442159 | 0.777695 | 0.953966 | 0.156574 |
| tossup_correctness | tier | nationals | 1584 | 0.709711 | 0.549509 | 0.0731964 | 0.18395 | 0.724116 | 0.724747 | -0.000631313 | 0.21415 | 0.359756 | 0.690995 | 0.923371 | 0.176911 |
| tossup_correctness | tier | regionals | 1886 | 0.716275 | 0.526702 | 0.0680026 | 0.173666 | 0.742842 | 0.746023 | -0.00318134 | 0.202835 | 0.402481 | 0.717933 | 0.93926 | 0.172557 |
| tossup_correctness | tier | winter | 2892 | 0.713516 | 0.495888 | 0.0645077 | 0.160246 | 0.774896 | 0.773167 | 0.00172891 | 0.196852 | 0.447918 | 0.768447 | 0.944846 | 0.159932 |
| tossup_correctness | category | Current Events | 124 | 0.654873 | 0.581613 | 0.132091 | 0.189253 | 0.733871 | 0.75 | -0.016129 | 0.221965 | 0.362663 | 0.703269 | 0.979965 | 0.165385 |
| tossup_correctness | category | Fine Arts | 1103 | 0.700428 | 0.516957 | 0.0725354 | 0.16714 | 0.773345 | 0.759746 | 0.0135993 | 0.197293 | 0.434485 | 0.772997 | 0.946901 | 0.160437 |
| tossup_correctness | category | Geography | 197 | 0.784149 | 0.542254 | 0.0851723 | 0.175583 | 0.751269 | 0.670051 | 0.0812183 | 0.263514 | 0.181876 | 0.64182 | 0.938953 | 0.169707 |
| tossup_correctness | category | History | 1491 | 0.726095 | 0.482486 | 0.075686 | 0.157629 | 0.764588 | 0.787391 | -0.0228035 | 0.202195 | 0.417559 | 0.753657 | 0.944695 | 0.16383 |
| tossup_correctness | category | Literature | 1472 | 0.715595 | 0.457196 | 0.0622198 | 0.143491 | 0.809103 | 0.804348 | 0.00475543 | 0.17705 | 0.497082 | 0.809506 | 0.953946 | 0.149317 |
| tossup_correctness | category | Mythology | 332 | 0.654898 | 0.487954 | 0.10148 | 0.15428 | 0.786145 | 0.813253 | -0.0271084 | 0.172777 | 0.486167 | 0.770017 | 0.93149 | 0.163093 |
| tossup_correctness | category | Other Academic | 69 | 0.7681 | 0.489071 | 0.134753 | 0.165011 | 0.695652 | 0.753623 | -0.057971 | 0.187266 | 0.458067 | 0.713314 | 0.912215 | 0.180905 |
| tossup_correctness | category | Philosophy | 324 | 0.689813 | 0.481703 | 0.0840454 | 0.159425 | 0.780864 | 0.799383 | -0.0185185 | 0.192942 | 0.45788 | 0.763083 | 0.953793 | 0.158195 |
| tossup_correctness | category | Popular Culture | 102 | 0.432526 | 0.539381 | 0.138344 | 0.160625 | 0.833333 | 0.833333 | 0 | 0.134374 | 0.611167 | 0.855261 | 0.95397 | 0.13047 |
| tossup_correctness | category | Religion | 372 | 0.677153 | 0.577423 | 0.0814839 | 0.197094 | 0.693548 | 0.709677 | -0.016129 | 0.197812 | 0.41609 | 0.677223 | 0.93014 | 0.179511 |
| tossup_correctness | category | Science | 1487 | 0.702214 | 0.531945 | 0.0730451 | 0.17579 | 0.731002 | 0.752522 | -0.0215198 | 0.208096 | 0.394453 | 0.725208 | 0.943411 | 0.169032 |
| tossup_correctness | category | Social Science | 336 | 0.74678 | 0.536237 | 0.0804075 | 0.175024 | 0.744048 | 0.702381 | 0.0416667 | 0.227543 | 0.30375 | 0.704762 | 0.938079 | 0.171712 |
| tossup_correctness | category | Unknown | 1886 | 0.716275 | 0.526702 | 0.0680026 | 0.173666 | 0.742842 | 0.746023 | -0.00318134 | 0.202835 | 0.402481 | 0.717933 | 0.93926 | 0.172557 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.716578 | 0.586079 | 0.206325 | 0.19487 | 0.715736 | 0.736041 | -0.0203046 | 0.222517 | 0.263536 | 0.588888 | 0.881482 | 0.193114 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.720121 | 0.541453 | 0.0834266 | 0.182046 | 0.71269 | 0.735025 | -0.022335 | 0.220022 | 0.346798 | 0.679759 | 0.92235 | 0.177608 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.695588 | 0.522647 | 0.0837399 | 0.171285 | 0.746779 | 0.769436 | -0.0226566 | 0.203779 | 0.409158 | 0.741494 | 0.939321 | 0.16693 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.698473 | 0.498314 | 0.0708587 | 0.160095 | 0.772854 | 0.78402 | -0.0111654 | 0.191471 | 0.450109 | 0.770661 | 0.952826 | 0.158633 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.739614 | 0.492079 | 0.0423467 | 0.159634 | 0.776702 | 0.756008 | 0.0206943 | 0.197141 | 0.437618 | 0.767666 | 0.94841 | 0.16156 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 1.8998 | 0.635641 | -0.442039 | 0.870265 | 1.50443 | 1.88306 | 2.27417 | 3.04286 | 4.46755 |
| player | theta_1 | 1186 | -1.48121 | 0.618459 | -3.47607 | -2.41035 | -1.92315 | -1.49925 | -1.08974 | -0.391537 | 0.412636 |
| player | theta_2 | 1186 | -1.3926 | 0.637733 | -3.1116 | -2.42888 | -1.8544 | -1.38272 | -0.940221 | -0.349276 | 0.483068 |
| player | theta_3 | 1186 | -1.43257 | 0.627405 | -3.325 | -2.4161 | -1.89345 | -1.41947 | -0.976712 | -0.42014 | 0.508231 |
| player | theta_norm | 1186 | 2.6562 | 0.558787 | 0.895436 | 1.73897 | 2.27324 | 2.65759 | 3.04513 | 3.59693 | 4.14136 |
| tossup | start_difficulty_d1 | 1240 | -0.780069 | 0.4069 | -2.57605 | -1.44796 | -1.03752 | -0.795964 | -0.506808 | -0.12961 | 0.493354 |
| tossup | start_difficulty_d2 | 1240 | -0.797466 | 0.414694 | -2.45355 | -1.48187 | -1.06062 | -0.791293 | -0.545358 | -0.11493 | 0.590229 |
| tossup | start_difficulty_d3 | 1240 | -0.818066 | 0.431487 | -2.31294 | -1.55916 | -1.07351 | -0.795531 | -0.537141 | -0.15227 | 0.632244 |
| tossup | end_difficulty_d1 | 1240 | -1.89876 | 0.483463 | -3.48401 | -2.69154 | -2.21659 | -1.91643 | -1.57532 | -1.1009 | -0.330973 |
| tossup | end_difficulty_d2 | 1240 | -1.91564 | 0.489616 | -3.53124 | -2.73367 | -2.24039 | -1.92722 | -1.62273 | -1.08357 | -0.228558 |
| tossup | end_difficulty_d3 | 1240 | -1.95019 | 0.506744 | -3.82852 | -2.80398 | -2.27903 | -1.93369 | -1.61327 | -1.11582 | -0.149987 |
| tossup | total_drop_d1 | 1240 | 1.11869 | 0.157452 | 0.62098 | 0.904083 | 1.02216 | 1.10883 | 1.19457 | 1.37679 | 2.11242 |
| tossup | total_drop_d2 | 1240 | 1.11818 | 0.159497 | 0.728416 | 0.894489 | 1.01193 | 1.10163 | 1.20193 | 1.37454 | 2.3728 |
| tossup | total_drop_d3 | 1240 | 1.13213 | 0.178432 | 0.578248 | 0.902695 | 1.02 | 1.11164 | 1.21388 | 1.41231 | 2.88261 |
| tossup | drop_share_1_d1 | 1240 | 0.316032 | 0.02083 | 0.209786 | 0.281618 | 0.304349 | 0.315876 | 0.328587 | 0.349436 | 0.417322 |
| tossup | drop_share_2_d1 | 1240 | 0.348936 | 0.0135516 | 0.306865 | 0.328491 | 0.340464 | 0.34826 | 0.356868 | 0.371338 | 0.405935 |
| tossup | drop_share_3_d1 | 1240 | 0.335032 | 0.020672 | 0.25069 | 0.302878 | 0.322216 | 0.335189 | 0.346993 | 0.36865 | 0.431331 |
| tossup | drop_share_1_d2 | 1240 | 0.315854 | 0.0215979 | 0.202943 | 0.282317 | 0.302269 | 0.31562 | 0.328768 | 0.35099 | 0.396273 |
| tossup | drop_share_2_d2 | 1240 | 0.348781 | 0.01405 | 0.291069 | 0.327859 | 0.339915 | 0.348414 | 0.356248 | 0.373036 | 0.428422 |
| tossup | drop_share_3_d2 | 1240 | 0.335365 | 0.0225699 | 0.269279 | 0.298632 | 0.322261 | 0.335187 | 0.347902 | 0.369719 | 0.494191 |
| tossup | drop_share_1_d3 | 1240 | 0.316467 | 0.0228227 | 0.197096 | 0.282259 | 0.304278 | 0.316757 | 0.330136 | 0.35246 | 0.403754 |
| tossup | drop_share_2_d3 | 1240 | 0.348108 | 0.0149032 | 0.282241 | 0.326891 | 0.338944 | 0.347506 | 0.355931 | 0.369252 | 0.463351 |
| tossup | drop_share_3_d3 | 1240 | 0.335425 | 0.0232486 | 0.241368 | 0.301805 | 0.32156 | 0.33511 | 0.347691 | 0.370347 | 0.520663 |
| tossup | r_1 | 1240 | 0.691481 | 0.361904 | 0.169233 | 0.284151 | 0.430437 | 0.604299 | 0.859652 | 1.42551 | 2.50867 |
| tossup | r_2 | 1240 | 0.739717 | 0.369152 | 0.19809 | 0.309454 | 0.475293 | 0.649979 | 0.911689 | 1.4205 | 2.52351 |
| tossup | r_3 | 1240 | 0.742716 | 0.389888 | 0.182945 | 0.321905 | 0.460218 | 0.627695 | 0.923481 | 1.53532 | 2.77819 |
| tossup | r_norm | 1240 | 1.35525 | 0.399114 | 0.378866 | 0.78431 | 1.05699 | 1.31178 | 1.60975 | 2.07421 | 2.90795 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 0.468009 | 0.226837 | -0.281004 | 0.0939901 | 0.31425 | 0.476232 | 0.621136 | 0.820905 | 1.37737 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 0.467946 | 0.223033 | -0.345883 | 0.0969887 | 0.317023 | 0.484166 | 0.613632 | 0.812767 | 1.38118 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 0.466429 | 0.21868 | -0.386448 | 0.105392 | 0.320338 | 0.469225 | 0.614037 | 0.817218 | 1.07963 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.825203 | 0.389487 | -2.43039 | -1.48196 | -1.05472 | -0.817382 | -0.567444 | -0.174217 | 0.674087 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.815871 | 0.391034 | -2.77385 | -1.44469 | -1.03375 | -0.792268 | -0.541516 | -0.244619 | 0.693932 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.878709 | 0.426458 | -3.0724 | -1.6122 | -1.11716 | -0.844199 | -0.59151 | -0.236075 | 0.30424 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 1.29321 | 0.346752 | 0.643397 | 0.876286 | 1.03185 | 1.22766 | 1.47104 | 1.97373 | 2.79858 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.28382 | 0.369755 | 0.576988 | 0.881057 | 1.01065 | 1.19603 | 1.45959 | 1.95196 | 3.29401 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 1.34514 | 0.412139 | 0.611441 | 0.874722 | 1.0272 | 1.25622 | 1.57042 | 2.10835 | 3.41308 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.236201 | 0.0621863 | 0.0677275 | 0.13822 | 0.195561 | 0.237607 | 0.273269 | 0.336843 | 0.584529 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.299893 | 0.0606889 | 0.0863283 | 0.183024 | 0.265837 | 0.309323 | 0.337322 | 0.387143 | 0.566143 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.463906 | 0.108456 | 0.110303 | 0.316395 | 0.38854 | 0.447429 | 0.53269 | 0.670969 | 0.840887 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.241538 | 0.0623993 | 0.0837302 | 0.143292 | 0.203638 | 0.242891 | 0.274509 | 0.34548 | 0.682302 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.303287 | 0.0569749 | 0.106237 | 0.200075 | 0.269938 | 0.311983 | 0.339055 | 0.381856 | 0.606478 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.455175 | 0.102165 | 0.12327 | 0.310731 | 0.387725 | 0.43649 | 0.514334 | 0.64681 | 0.791611 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.239208 | 0.0674101 | 0.0629859 | 0.13545 | 0.195945 | 0.238643 | 0.276494 | 0.343418 | 0.64727 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.301533 | 0.060118 | 0.0874749 | 0.190351 | 0.268668 | 0.31265 | 0.338211 | 0.387218 | 0.552354 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.459259 | 0.109569 | 0.137358 | 0.302109 | 0.387852 | 0.439532 | 0.524772 | 0.666506 | 0.843271 |
| tossup_hazard | hazard_r_1 | 1240 | 1.61676 | 0.853267 | 0.220928 | 0.557644 | 0.969001 | 1.43558 | 2.01915 | 3.29281 | 5.22068 |
| tossup_hazard | hazard_r_2 | 1240 | 1.48006 | 0.702615 | 0.236586 | 0.555779 | 0.952009 | 1.38596 | 1.87056 | 2.81933 | 4.67267 |
| tossup_hazard | hazard_r_3 | 1240 | 1.5105 | 0.685034 | 0.211354 | 0.538329 | 1.01123 | 1.4088 | 1.94073 | 2.76833 | 4.25327 |
