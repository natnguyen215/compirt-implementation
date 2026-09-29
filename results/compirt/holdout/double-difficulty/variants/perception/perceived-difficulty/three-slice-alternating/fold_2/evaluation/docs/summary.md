# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-alternating/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice-alternating/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 326441 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.58939 |
| log_loss | 0.735988 |
| ece | 0.280365 |
| brier | 0.265929 |
| accuracy | 0.549638 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.21454 |
| probability_std | 0.159897 |
| probability_p10 | 0.249921 |
| probability_p50 | 0.502203 |
| probability_p90 | 0.680833 |
| mean_predictive_variance | 0.224171 |
| integrated_brier_score | 0.0962067 |
| joint_tossup_event_log_loss | 6.88097 |
| buzz_position_mae | 0.140158 |
| buzz_position_median_absolute_error | 0.117669 |
| buzz_position_bias | -0.002582 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.359188 |
| first_buzzer_mean_reciprocal_rank | 0.569924 |
| first_buzzer_log_loss | 1.65801 |
| first_buzzer_events | 9257 |
| neg_auroc | 0.58939 |
| neg_average_precision | 0.303078 |
| neg_precision | 0.283093 |
| neg_recall | 0.593678 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.13937 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0487791 |
| no_buzz_calibration_error | 0.0356661 |
| no_buzz_brier | 0.0186069 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.58939 | 0.735988 | 0.280365 | 0.265929 | 0.549638 | 0.764178 | -0.21454 | 0.159897 | 0.249921 | 0.502203 | 0.680833 | 0.224171 |
| tossup_correctness | tier | fall | 2798 | 0.603484 | 0.781135 | 0.333101 | 0.285793 | 0.494639 | 0.785204 | -0.290565 | 0.164202 | 0.211507 | 0.463362 | 0.661599 | 0.220744 |
| tossup_correctness | tier | nationals | 1545 | 0.575648 | 0.684459 | 0.199081 | 0.244488 | 0.598058 | 0.721036 | -0.122977 | 0.136032 | 0.331886 | 0.539135 | 0.684054 | 0.231013 |
| tossup_correctness | tier | regionals | 2039 | 0.599899 | 0.72251 | 0.264624 | 0.2581 | 0.588524 | 0.762138 | -0.173615 | 0.168287 | 0.248969 | 0.52974 | 0.696586 | 0.221676 |
| tossup_correctness | tier | winter | 2875 | 0.597806 | 0.729302 | 0.284265 | 0.263671 | 0.549565 | 0.768348 | -0.218783 | 0.155396 | 0.258385 | 0.499565 | 0.678763 | 0.225599 |
| tossup_correctness | category | Current Events | 129 | 0.55814 | 0.768609 | 0.255393 | 0.281343 | 0.503876 | 0.666667 | -0.162791 | 0.167448 | 0.196721 | 0.46679 | 0.656889 | 0.219275 |
| tossup_correctness | category | Fine Arts | 1074 | 0.570803 | 0.76753 | 0.307537 | 0.279684 | 0.513035 | 0.776536 | -0.263501 | 0.164922 | 0.240697 | 0.486207 | 0.684999 | 0.221932 |
| tossup_correctness | category | Geography | 180 | 0.521347 | 0.762968 | 0.195024 | 0.279602 | 0.505556 | 0.616667 | -0.111111 | 0.15089 | 0.23953 | 0.461788 | 0.639961 | 0.224989 |
| tossup_correctness | category | History | 1454 | 0.589574 | 0.72053 | 0.2688 | 0.260156 | 0.545392 | 0.757909 | -0.212517 | 0.153983 | 0.265313 | 0.504136 | 0.679276 | 0.226171 |
| tossup_correctness | category | Literature | 1435 | 0.578315 | 0.721629 | 0.309383 | 0.259523 | 0.574216 | 0.810453 | -0.236237 | 0.153163 | 0.269999 | 0.522766 | 0.688487 | 0.22654 |
| tossup_correctness | category | Mythology | 324 | 0.593588 | 0.748798 | 0.316788 | 0.271605 | 0.527778 | 0.79321 | -0.265432 | 0.156676 | 0.25061 | 0.486291 | 0.667524 | 0.224897 |
| tossup_correctness | category | Other Academic | 71 | 0.533769 | 0.705129 | 0.281292 | 0.254764 | 0.605634 | 0.760563 | -0.15493 | 0.145917 | 0.310775 | 0.535662 | 0.697953 | 0.228486 |
| tossup_correctness | category | Philosophy | 310 | 0.613262 | 0.692683 | 0.263804 | 0.248946 | 0.577419 | 0.76129 | -0.183871 | 0.149548 | 0.305574 | 0.515448 | 0.672002 | 0.227629 |
| tossup_correctness | category | Popular Culture | 108 | 0.46875 | 0.986747 | 0.495839 | 0.372321 | 0.287037 | 0.888889 | -0.601852 | 0.155443 | 0.184308 | 0.404828 | 0.605297 | 0.214399 |
| tossup_correctness | category | Religion | 361 | 0.606363 | 0.722906 | 0.263816 | 0.261801 | 0.526316 | 0.742382 | -0.216066 | 0.149975 | 0.266896 | 0.482561 | 0.672222 | 0.227048 |
| tossup_correctness | category | Science | 1445 | 0.593735 | 0.756514 | 0.283989 | 0.275481 | 0.529412 | 0.746021 | -0.216609 | 0.15698 | 0.226788 | 0.476496 | 0.658706 | 0.223916 |
| tossup_correctness | category | Social Science | 327 | 0.620074 | 0.696452 | 0.228767 | 0.249847 | 0.565749 | 0.718654 | -0.152905 | 0.156167 | 0.254089 | 0.503347 | 0.681831 | 0.225518 |
| tossup_correctness | category | Unknown | 2039 | 0.599899 | 0.72251 | 0.264624 | 0.2581 | 0.588524 | 0.762138 | -0.173615 | 0.168287 | 0.248969 | 0.52974 | 0.696586 | 0.221676 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.651596 | 0.861909 | 0.36585 | 0.317851 | 0.431694 | 0.743169 | -0.311475 | 0.154623 | 0.138114 | 0.385445 | 0.568071 | 0.211041 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.616313 | 0.795215 | 0.311805 | 0.292563 | 0.457592 | 0.728796 | -0.271204 | 0.152896 | 0.19388 | 0.421757 | 0.620062 | 0.219732 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.610645 | 0.765506 | 0.29874 | 0.278005 | 0.520768 | 0.752568 | -0.2318 | 0.158129 | 0.217244 | 0.466818 | 0.649303 | 0.222863 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.586494 | 0.734344 | 0.298455 | 0.265411 | 0.559652 | 0.786087 | -0.226435 | 0.155288 | 0.257521 | 0.507272 | 0.680825 | 0.225733 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.564024 | 0.689077 | 0.23417 | 0.245799 | 0.598003 | 0.764393 | -0.166389 | 0.1524 | 0.307104 | 0.554169 | 0.712864 | 0.225861 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | 0.309051 | 0.941315 | -1.78846 | -1.20322 | -0.362971 | 0.277627 | 0.963076 | 1.92674 | 2.76901 |
| player | theta_2 | 1197 | 0.202337 | 0.828567 | -1.81746 | -1.10895 | -0.40118 | 0.164077 | 0.812532 | 1.52201 | 2.57012 |
| player | theta_3 | 1197 | 0.266426 | 0.930282 | -1.79211 | -1.16172 | -0.478352 | 0.219302 | 0.967115 | 1.82916 | 2.74062 |
| player | theta_norm | 1197 | 1.46542 | 0.704542 | 0.0956305 | 0.452851 | 0.927257 | 1.37997 | 1.96188 | 2.6803 | 3.80245 |
| tossup | start_difficulty_d1 | 1240 | 1.62986 | 0.352717 | -0.196539 | 1.01136 | 1.43077 | 1.64743 | 1.85625 | 2.17397 | 2.67838 |
| tossup | start_difficulty_d2 | 1240 | 1.56328 | 0.378859 | -0.499492 | 0.878465 | 1.38575 | 1.60431 | 1.81004 | 2.05327 | 2.78679 |
| tossup | start_difficulty_d3 | 1240 | 1.5534 | 0.365071 | -0.378885 | 0.900639 | 1.35121 | 1.58378 | 1.79986 | 2.08031 | 2.70842 |
| tossup | end_difficulty_d1 | 1240 | 0.458261 | 0.40472 | -1.34949 | -0.18451 | 0.244718 | 0.46954 | 0.68995 | 1.10674 | 1.96117 |
| tossup | end_difficulty_d2 | 1240 | 0.263582 | 0.431278 | -2.4327 | -0.516764 | 0.0461549 | 0.323674 | 0.543399 | 0.827753 | 1.36018 |
| tossup | end_difficulty_d3 | 1240 | 0.472792 | 0.411969 | -1.59435 | -0.227394 | 0.233654 | 0.513114 | 0.757171 | 1.06715 | 1.61423 |
| tossup | total_drop_d1 | 1240 | 1.1716 | 0.392943 | 0.562623 | 0.715044 | 0.859589 | 1.07132 | 1.43036 | 1.86968 | 3.32218 |
| tossup | total_drop_d2 | 1240 | 1.2997 | 0.475439 | 0.452752 | 0.731782 | 0.928038 | 1.19063 | 1.58141 | 2.1726 | 3.71918 |
| tossup | total_drop_d3 | 1240 | 1.08061 | 0.348327 | 0.496488 | 0.707133 | 0.84097 | 0.975203 | 1.23881 | 1.78018 | 2.82135 |
| tossup | drop_share_1_d1 | 1240 | 0.201675 | 0.0625588 | 0.0563498 | 0.106142 | 0.153615 | 0.203861 | 0.248055 | 0.294742 | 0.517508 |
| tossup | drop_share_2_d1 | 1240 | 0.273116 | 0.0696578 | 0.0614778 | 0.142537 | 0.229503 | 0.288429 | 0.321141 | 0.359483 | 0.524828 |
| tossup | drop_share_3_d1 | 1240 | 0.525209 | 0.120475 | 0.198005 | 0.369749 | 0.430009 | 0.503138 | 0.612658 | 0.747539 | 0.882172 |
| tossup | drop_share_1_d2 | 1240 | 0.195146 | 0.0666649 | 0.040823 | 0.0981282 | 0.139986 | 0.19033 | 0.251102 | 0.296807 | 0.494622 |
| tossup | drop_share_2_d2 | 1240 | 0.266877 | 0.0728921 | 0.0654545 | 0.139029 | 0.210449 | 0.28264 | 0.322854 | 0.358024 | 0.549566 |
| tossup | drop_share_3_d2 | 1240 | 0.537977 | 0.130041 | 0.0995357 | 0.367464 | 0.42302 | 0.526673 | 0.645994 | 0.759021 | 0.887605 |
| tossup | drop_share_1_d3 | 1240 | 0.216863 | 0.0556968 | 0.056896 | 0.118579 | 0.177547 | 0.226451 | 0.255564 | 0.292184 | 0.429018 |
| tossup | drop_share_2_d3 | 1240 | 0.286768 | 0.0607516 | 0.0688006 | 0.155809 | 0.261107 | 0.301555 | 0.324738 | 0.353911 | 0.573102 |
| tossup | drop_share_3_d3 | 1240 | 0.496369 | 0.106496 | 0.2204 | 0.367613 | 0.420607 | 0.4693 | 0.556511 | 0.717141 | 0.874085 |
| tossup | r_1 | 1240 | 0.37506 | 0.203964 | 0.0317762 | 0.0810036 | 0.204023 | 0.352362 | 0.535362 | 0.730949 | 0.872327 |
| tossup | r_2 | 1240 | 0.336122 | 0.1905 | 0.0233738 | 0.0553485 | 0.175278 | 0.330428 | 0.470376 | 0.677138 | 0.852387 |
| tossup | r_3 | 1240 | 0.288817 | 0.166847 | 0.0290736 | 0.0720917 | 0.15345 | 0.265558 | 0.391943 | 0.613171 | 0.872544 |
| tossup | r_norm | 1240 | 0.662596 | 0.0606425 | 0.577642 | 0.584086 | 0.613898 | 0.652504 | 0.699113 | 0.783302 | 0.878363 |
