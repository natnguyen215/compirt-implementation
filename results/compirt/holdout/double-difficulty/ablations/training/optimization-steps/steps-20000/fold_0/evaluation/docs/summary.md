# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/optimization-steps/steps-20000/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/optimization-steps/steps-20000/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 20000 |
| pyramidal | final_loss | 275902 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.711173 |
| log_loss | 0.491654 |
| ece | 0.00925042 |
| brier | 0.159834 |
| accuracy | 0.777084 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0118343 |
| probability_std | 0.149566 |
| probability_p10 | 0.559445 |
| probability_p50 | 0.810282 |
| probability_p90 | 0.921223 |
| mean_predictive_variance | 0.154247 |
| integrated_brier_score | 0.0950597 |
| joint_tossup_event_log_loss | 6.44001 |
| buzz_position_mae | 0.140167 |
| buzz_position_median_absolute_error | 0.11763 |
| buzz_position_bias | -0.00259543 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.376116 |
| first_buzzer_mean_reciprocal_rank | 0.584831 |
| first_buzzer_log_loss | 1.6217 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.711173 |
| neg_average_precision | 0.445664 |
| neg_precision | 0.589869 |
| neg_recall | 0.165445 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.181142 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00996735 |
| no_buzz_calibration_error | -0.00330229 |
| no_buzz_brier | 0.0128541 |
| full_pmf_max_mass_error | 1.44329e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.711173 | 0.491654 | 0.00925042 | 0.159834 | 0.777084 | 0.76525 | 0.0118343 | 0.149566 | 0.559445 | 0.810282 | 0.921223 | 0.154247 |
| tossup_correctness | tier | fall | 2933 | 0.712083 | 0.462936 | 0.0165286 | 0.148303 | 0.799523 | 0.791681 | 0.0078418 | 0.145377 | 0.561371 | 0.815454 | 0.921754 | 0.153015 |
| tossup_correctness | tier | nationals | 1584 | 0.696714 | 0.541264 | 0.0381553 | 0.179029 | 0.744949 | 0.724747 | 0.020202 | 0.165783 | 0.510008 | 0.807385 | 0.918904 | 0.156685 |
| tossup_correctness | tier | regionals | 1886 | 0.707529 | 0.515574 | 0.0204834 | 0.170253 | 0.757688 | 0.746023 | 0.0116649 | 0.146704 | 0.559305 | 0.796681 | 0.917454 | 0.159044 |
| tossup_correctness | tier | winter | 2892 | 0.719072 | 0.478008 | 0.0150354 | 0.154221 | 0.784578 | 0.773167 | 0.0114108 | 0.145402 | 0.584156 | 0.815019 | 0.922427 | 0.151033 |
| tossup_correctness | category | Current Events | 124 | 0.693028 | 0.516411 | 0.0864141 | 0.167345 | 0.782258 | 0.75 | 0.0322581 | 0.163016 | 0.505617 | 0.752713 | 0.923328 | 0.16857 |
| tossup_correctness | category | Fine Arts | 1103 | 0.710353 | 0.495509 | 0.0221931 | 0.160261 | 0.780598 | 0.759746 | 0.0208522 | 0.152485 | 0.57853 | 0.81955 | 0.92356 | 0.151523 |
| tossup_correctness | category | Geography | 197 | 0.793124 | 0.512108 | 0.0722593 | 0.169202 | 0.746193 | 0.670051 | 0.0761421 | 0.21865 | 0.366797 | 0.73927 | 0.908855 | 0.167147 |
| tossup_correctness | category | History | 1491 | 0.71564 | 0.466448 | 0.022963 | 0.150353 | 0.791415 | 0.787391 | 0.00402414 | 0.139785 | 0.571259 | 0.809052 | 0.918787 | 0.155169 |
| tossup_correctness | category | Literature | 1472 | 0.730413 | 0.436828 | 0.0239699 | 0.13742 | 0.814538 | 0.804348 | 0.0101902 | 0.127279 | 0.634253 | 0.844301 | 0.930041 | 0.138085 |
| tossup_correctness | category | Mythology | 332 | 0.684588 | 0.453037 | 0.0416527 | 0.143095 | 0.813253 | 0.813253 | 0 | 0.122156 | 0.627955 | 0.827818 | 0.915448 | 0.147522 |
| tossup_correctness | category | Other Academic | 69 | 0.713801 | 0.510585 | 0.0984355 | 0.170523 | 0.73913 | 0.753623 | -0.0144928 | 0.120334 | 0.634361 | 0.797283 | 0.902181 | 0.16024 |
| tossup_correctness | category | Philosophy | 324 | 0.672824 | 0.472138 | 0.0277955 | 0.150764 | 0.790123 | 0.799383 | -0.00925926 | 0.129789 | 0.608381 | 0.815294 | 0.920411 | 0.15226 |
| tossup_correctness | category | Popular Culture | 102 | 0.441522 | 0.486479 | 0.0817795 | 0.149613 | 0.823529 | 0.833333 | -0.00980392 | 0.0806374 | 0.720946 | 0.842153 | 0.91211 | 0.13608 |
| tossup_correctness | category | Religion | 372 | 0.714191 | 0.546703 | 0.0441663 | 0.184819 | 0.72043 | 0.709677 | 0.0107527 | 0.154691 | 0.520968 | 0.762714 | 0.909267 | 0.169256 |
| tossup_correctness | category | Science | 1487 | 0.679819 | 0.521375 | 0.0272843 | 0.171558 | 0.761937 | 0.752522 | 0.00941493 | 0.159957 | 0.519059 | 0.798551 | 0.918716 | 0.159478 |
| tossup_correctness | category | Social Science | 336 | 0.724831 | 0.537835 | 0.0340912 | 0.178601 | 0.738095 | 0.702381 | 0.0357143 | 0.182658 | 0.471658 | 0.784284 | 0.920396 | 0.163203 |
| tossup_correctness | category | Unknown | 1886 | 0.707529 | 0.515574 | 0.0204834 | 0.170253 | 0.757688 | 0.746023 | 0.0116649 | 0.146704 | 0.559305 | 0.796681 | 0.917454 | 0.159044 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.696817 | 0.517907 | 0.0561357 | 0.168713 | 0.766497 | 0.736041 | 0.0304569 | 0.152199 | 0.524972 | 0.753682 | 0.884825 | 0.176083 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.71847 | 0.518133 | 0.0239895 | 0.17185 | 0.754315 | 0.735025 | 0.0192893 | 0.150597 | 0.54099 | 0.793352 | 0.912226 | 0.16185 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.692248 | 0.499529 | 0.0249746 | 0.162229 | 0.770769 | 0.769436 | 0.00133274 | 0.145664 | 0.584486 | 0.812124 | 0.922711 | 0.151895 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.696232 | 0.479482 | 0.016515 | 0.154581 | 0.789951 | 0.78402 | 0.00593161 | 0.143335 | 0.590531 | 0.822861 | 0.925819 | 0.148699 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.73425 | 0.486949 | 0.0106021 | 0.158526 | 0.777704 | 0.756008 | 0.0216956 | 0.155968 | 0.526821 | 0.805215 | 0.916252 | 0.157385 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 0.801109 | 0.838095 | -1.56055 | -0.55978 | 0.23154 | 0.787544 | 1.33745 | 2.28442 | 3.00826 |
| player | theta_1 | 1186 | -0.378485 | 0.938635 | -2.85328 | -1.78247 | -0.977975 | -0.471227 | 0.138143 | 1.28622 | 4.10429 |
| player | theta_2 | 1186 | -0.381095 | 0.844295 | -3.09862 | -1.68901 | -0.927337 | -0.463388 | 0.11683 | 1.11182 | 2.68847 |
| player | theta_3 | 1186 | -0.43285 | 0.94107 | -3.26954 | -1.74104 | -1.02668 | -0.551375 | 0.0977392 | 1.30743 | 3.15457 |
| player | theta_norm | 1186 | 1.58978 | 0.652848 | 0.0871665 | 0.650488 | 1.12544 | 1.4949 | 1.98025 | 2.76022 | 5.26452 |
| tossup | start_difficulty_d1 | 1240 | -0.955495 | 0.54321 | -2.7591 | -1.68486 | -1.29721 | -1.00991 | -0.672354 | -0.0755838 | 2.27153 |
| tossup | start_difficulty_d2 | 1240 | -0.967357 | 0.487182 | -2.92424 | -1.68395 | -1.28093 | -1.01434 | -0.677671 | -0.0730695 | 1.09202 |
| tossup | start_difficulty_d3 | 1240 | -0.969152 | 0.501977 | -2.82732 | -1.74633 | -1.28356 | -0.989837 | -0.661468 | -0.198912 | 1.5467 |
| tossup | end_difficulty_d1 | 1240 | -1.95267 | 0.632654 | -4.00584 | -2.84168 | -2.34979 | -2.00352 | -1.59359 | -0.908056 | 1.53926 |
| tossup | end_difficulty_d2 | 1240 | -1.96535 | 0.573024 | -4.15104 | -2.82957 | -2.3437 | -2.01744 | -1.63028 | -0.984531 | 0.379183 |
| tossup | end_difficulty_d3 | 1240 | -1.96713 | 0.59034 | -4.09224 | -2.87016 | -2.3512 | -1.97981 | -1.61015 | -1.03952 | 0.912859 |
| tossup | total_drop_d1 | 1240 | 0.997174 | 0.11175 | 0.628499 | 0.816132 | 0.926893 | 0.997586 | 1.06544 | 1.17312 | 1.50938 |
| tossup | total_drop_d2 | 1240 | 0.99799 | 0.103159 | 0.662603 | 0.819669 | 0.931627 | 1.00048 | 1.06481 | 1.16048 | 1.44142 |
| tossup | total_drop_d3 | 1240 | 0.997981 | 0.107252 | 0.607868 | 0.826646 | 0.930272 | 0.997898 | 1.06477 | 1.16333 | 1.44755 |
| tossup | drop_share_1_d1 | 1240 | 0.304514 | 0.0153702 | 0.22478 | 0.280492 | 0.295262 | 0.304591 | 0.314736 | 0.32757 | 0.354151 |
| tossup | drop_share_2_d1 | 1240 | 0.346709 | 0.0114937 | 0.305127 | 0.328841 | 0.339375 | 0.346248 | 0.354276 | 0.366047 | 0.399611 |
| tossup | drop_share_3_d1 | 1240 | 0.348777 | 0.016424 | 0.308354 | 0.323965 | 0.337418 | 0.348169 | 0.358571 | 0.376234 | 0.44117 |
| tossup | drop_share_1_d2 | 1240 | 0.304204 | 0.0141552 | 0.249086 | 0.280531 | 0.295972 | 0.30415 | 0.31313 | 0.328198 | 0.36492 |
| tossup | drop_share_2_d2 | 1240 | 0.347321 | 0.0110435 | 0.311711 | 0.329169 | 0.339779 | 0.347332 | 0.354743 | 0.365949 | 0.384255 |
| tossup | drop_share_3_d2 | 1240 | 0.348475 | 0.0152831 | 0.30268 | 0.324498 | 0.33889 | 0.34765 | 0.357537 | 0.375266 | 0.406762 |
| tossup | drop_share_1_d3 | 1240 | 0.305204 | 0.014806 | 0.234167 | 0.280925 | 0.296411 | 0.305386 | 0.31506 | 0.329583 | 0.358029 |
| tossup | drop_share_2_d3 | 1240 | 0.346998 | 0.0110822 | 0.311352 | 0.328955 | 0.339563 | 0.346846 | 0.35459 | 0.365506 | 0.38292 |
| tossup | drop_share_3_d3 | 1240 | 0.347798 | 0.015386 | 0.296747 | 0.323743 | 0.337642 | 0.346975 | 0.357175 | 0.373153 | 0.408387 |
| tossup | r_1 | 1240 | 0.320726 | 0.166252 | 0.0546737 | 0.109602 | 0.189188 | 0.287995 | 0.429311 | 0.64224 | 0.873099 |
| tossup | r_2 | 1240 | 0.330925 | 0.169621 | 0.0562088 | 0.120703 | 0.198782 | 0.295694 | 0.434947 | 0.67985 | 0.831474 |
| tossup | r_3 | 1240 | 0.348349 | 0.173784 | 0.0545587 | 0.11439 | 0.210873 | 0.319772 | 0.462359 | 0.678131 | 0.864611 |
| tossup | r_norm | 1240 | 0.645661 | 0.0582209 | 0.5774 | 0.581628 | 0.600425 | 0.628266 | 0.675788 | 0.763119 | 0.877698 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 8.65636 | 0.517641 | 4.79095 | 7.70736 | 8.51009 | 8.67021 | 8.87981 | 9.4835 | 10.4194 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 8.68175 | 0.506757 | 5.2557 | 7.7708 | 8.56904 | 8.69954 | 8.87642 | 9.42552 | 10.755 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 8.73578 | 0.487598 | 5.4235 | 7.96189 | 8.57461 | 8.71844 | 8.93688 | 9.5166 | 10.7574 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 4.88543 | 3.94569 | -11.8607 | -2.77664 | 2.18374 | 7.48594 | 7.68095 | 7.98447 | 8.77112 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 5.35862 | 4.02323 | -10.7227 | -3.24783 | 2.71954 | 7.59972 | 7.75978 | 8.07095 | 9.1013 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 5.42023 | 3.98235 | -16.114 | -2.92987 | 3.30385 | 7.59666 | 7.77844 | 8.1858 | 9.0961 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.77093 | 4.00398 | 0.871149 | 0.944658 | 0.999625 | 1.05713 | 6.41742 | 11.9472 | 20.8188 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 3.32313 | 4.05485 | 0.850619 | 0.931781 | 0.979632 | 1.02468 | 5.68247 | 12.0636 | 20.1273 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 3.31555 | 4.02638 | 0.862161 | 0.928394 | 0.981941 | 1.03072 | 5.4654 | 11.892 | 25.0303 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.277211 | 0.0950009 | 0.0560622 | 0.108328 | 0.254013 | 0.295958 | 0.308782 | 0.416646 | 0.742765 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.325499 | 0.0796986 | 0.0582511 | 0.157788 | 0.319644 | 0.343935 | 0.355961 | 0.440001 | 0.728389 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.39729 | 0.128813 | 0.090113 | 0.246975 | 0.342124 | 0.354726 | 0.397329 | 0.699004 | 0.874245 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.28671 | 0.087355 | 0.0389562 | 0.117008 | 0.280726 | 0.29932 | 0.310865 | 0.413147 | 0.754811 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.32844 | 0.0714097 | 0.0592148 | 0.167158 | 0.330459 | 0.343882 | 0.354395 | 0.393842 | 0.640484 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.384849 | 0.118881 | 0.0768253 | 0.249412 | 0.342149 | 0.352861 | 0.374212 | 0.672386 | 0.901829 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.280659 | 0.0860303 | 0.03928 | 0.113409 | 0.273303 | 0.296348 | 0.309192 | 0.388346 | 0.752525 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.331077 | 0.0733293 | 0.0680758 | 0.176491 | 0.329497 | 0.344236 | 0.355223 | 0.421781 | 0.694559 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.388265 | 0.117001 | 0.0885787 | 0.262274 | 0.342031 | 0.35503 | 0.379849 | 0.681948 | 0.889235 |
| tossup_hazard | hazard_r_1 | 1240 | 0.364921 | 0.29711 | 0.0142862 | 0.0390449 | 0.10083 | 0.232002 | 0.610108 | 0.886565 | 0.947941 |
| tossup_hazard | hazard_r_2 | 1240 | 0.305161 | 0.271586 | 0.0132283 | 0.0309045 | 0.0727347 | 0.176883 | 0.536343 | 0.811463 | 0.928542 |
| tossup_hazard | hazard_r_3 | 1240 | 0.329918 | 0.272273 | 0.0125079 | 0.0342561 | 0.0885405 | 0.240611 | 0.540359 | 0.854893 | 0.972171 |
