# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/three-slice/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 318323 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.589948 |
| log_loss | 0.710169 |
| ece | 0.254507 |
| brier | 0.254219 |
| accuracy | 0.578577 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.183548 |
| probability_std | 0.164729 |
| probability_p10 | 0.27114 |
| probability_p50 | 0.527048 |
| probability_p90 | 0.709532 |
| mean_predictive_variance | 0.222806 |
| integrated_brier_score | 0.0936081 |
| joint_tossup_event_log_loss | 6.82661 |
| buzz_position_mae | 0.137959 |
| buzz_position_median_absolute_error | 0.115909 |
| buzz_position_bias | -0.00543226 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.367535 |
| first_buzzer_mean_reciprocal_rank | 0.577356 |
| first_buzzer_log_loss | 1.64846 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.589948 |
| neg_average_precision | 0.30155 |
| neg_precision | 0.290168 |
| neg_recall | 0.533518 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.139094 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0539502 |
| no_buzz_calibration_error | 0.0380412 |
| no_buzz_brier | 0.0222478 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.589948 | 0.710169 | 0.254507 | 0.254219 | 0.578577 | 0.762125 | -0.183548 | 0.164729 | 0.27114 | 0.527048 | 0.709532 | 0.222806 |
| tossup_correctness | tier | fall | 2842 | 0.603102 | 0.720801 | 0.291509 | 0.259476 | 0.55841 | 0.785362 | -0.226953 | 0.162576 | 0.267498 | 0.50453 | 0.701241 | 0.223531 |
| tossup_correctness | tier | nationals | 1564 | 0.585995 | 0.662054 | 0.174391 | 0.234222 | 0.618286 | 0.718031 | -0.0997442 | 0.141947 | 0.340959 | 0.566568 | 0.716125 | 0.227909 |
| tossup_correctness | tier | regionals | 1937 | 0.601817 | 0.702568 | 0.244916 | 0.249989 | 0.601446 | 0.758389 | -0.156944 | 0.168276 | 0.262091 | 0.544891 | 0.710048 | 0.221502 |
| tossup_correctness | tier | winter | 2750 | 0.586517 | 0.731899 | 0.268828 | 0.263139 | 0.560727 | 0.765818 | -0.205091 | 0.172966 | 0.243335 | 0.51703 | 0.713199 | 0.220074 |
| tossup_correctness | category | Current Events | 126 | 0.529684 | 0.807068 | 0.316338 | 0.297801 | 0.507937 | 0.769841 | -0.261905 | 0.15987 | 0.222987 | 0.478578 | 0.646885 | 0.22228 |
| tossup_correctness | category | Fine Arts | 1071 | 0.605442 | 0.713462 | 0.265963 | 0.255576 | 0.583567 | 0.766573 | -0.183007 | 0.171317 | 0.253736 | 0.523597 | 0.706023 | 0.22065 |
| tossup_correctness | category | Geography | 185 | 0.569352 | 0.771253 | 0.253091 | 0.283337 | 0.502703 | 0.697297 | -0.194595 | 0.159201 | 0.223841 | 0.456267 | 0.647354 | 0.221638 |
| tossup_correctness | category | History | 1440 | 0.568879 | 0.715612 | 0.250993 | 0.258394 | 0.546528 | 0.754167 | -0.207639 | 0.158358 | 0.289486 | 0.508686 | 0.706439 | 0.224912 |
| tossup_correctness | category | Literature | 1422 | 0.573487 | 0.694946 | 0.285008 | 0.24623 | 0.610408 | 0.814346 | -0.203938 | 0.162619 | 0.295453 | 0.54947 | 0.728938 | 0.222694 |
| tossup_correctness | category | Mythology | 318 | 0.558066 | 0.718584 | 0.276669 | 0.257726 | 0.566038 | 0.789308 | -0.22327 | 0.159441 | 0.285328 | 0.536264 | 0.698705 | 0.224419 |
| tossup_correctness | category | Other Academic | 66 | 0.740202 | 0.624722 | 0.214788 | 0.217044 | 0.606061 | 0.712121 | -0.106061 | 0.151285 | 0.309172 | 0.507354 | 0.681752 | 0.227113 |
| tossup_correctness | category | Philosophy | 311 | 0.600447 | 0.694461 | 0.22576 | 0.247762 | 0.575563 | 0.745981 | -0.170418 | 0.166339 | 0.28882 | 0.542506 | 0.71879 | 0.221922 |
| tossup_correctness | category | Popular Culture | 102 | 0.475 | 0.916992 | 0.460859 | 0.343044 | 0.421569 | 0.882353 | -0.460784 | 0.163836 | 0.187154 | 0.448871 | 0.641575 | 0.217421 |
| tossup_correctness | category | Religion | 358 | 0.582905 | 0.704078 | 0.205085 | 0.252513 | 0.578212 | 0.712291 | -0.134078 | 0.162662 | 0.270451 | 0.524555 | 0.708845 | 0.223489 |
| tossup_correctness | category | Science | 1433 | 0.600996 | 0.705019 | 0.233395 | 0.251889 | 0.576413 | 0.738311 | -0.161898 | 0.163232 | 0.277131 | 0.523495 | 0.709162 | 0.223331 |
| tossup_correctness | category | Social Science | 324 | 0.597847 | 0.703413 | 0.235355 | 0.252507 | 0.567901 | 0.731481 | -0.16358 | 0.152496 | 0.290927 | 0.515307 | 0.679651 | 0.226745 |
| tossup_correctness | category | Unknown | 1937 | 0.601817 | 0.702568 | 0.244916 | 0.249989 | 0.601446 | 0.758389 | -0.156944 | 0.168276 | 0.262091 | 0.544891 | 0.710048 | 0.221502 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.551996 | 0.805038 | 0.294295 | 0.296368 | 0.502994 | 0.712575 | -0.209581 | 0.158892 | 0.192817 | 0.450137 | 0.630887 | 0.220176 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.588585 | 0.778474 | 0.286111 | 0.284231 | 0.505482 | 0.729167 | -0.223684 | 0.157502 | 0.220869 | 0.455457 | 0.640106 | 0.221951 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.622868 | 0.72756 | 0.274423 | 0.260977 | 0.564539 | 0.755083 | -0.190544 | 0.16062 | 0.241762 | 0.498842 | 0.678492 | 0.223827 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.574465 | 0.714189 | 0.269629 | 0.25592 | 0.574895 | 0.780942 | -0.206048 | 0.162466 | 0.273155 | 0.533763 | 0.707143 | 0.223477 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.585837 | 0.668811 | 0.215799 | 0.236694 | 0.617676 | 0.762029 | -0.144354 | 0.161209 | 0.311439 | 0.572429 | 0.737722 | 0.221874 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | 0.223789 | 0.985243 | -2.0349 | -1.16565 | -0.564084 | 0.0607828 | 0.925741 | 1.94455 | 3.04929 |
| player | theta_2 | 1167 | 0.200024 | 0.873942 | -1.8777 | -1.12357 | -0.394135 | 0.0836641 | 0.751928 | 1.86219 | 3.14985 |
| player | theta_3 | 1167 | 0.604789 | 1.14538 | -1.97452 | -1.1744 | -0.305683 | 0.592498 | 1.46377 | 2.47924 | 3.30577 |
| player | theta_norm | 1167 | 1.70123 | 0.778431 | 0.175109 | 0.558849 | 1.08303 | 1.63923 | 2.22984 | 3.0672 | 4.10872 |
| tossup | start_difficulty_d1 | 1220 | 1.56952 | 0.368143 | -0.260896 | 0.882892 | 1.4023 | 1.62274 | 1.80505 | 2.06904 | 2.52958 |
| tossup | start_difficulty_d2 | 1220 | 1.45952 | 0.451207 | -0.526692 | 0.577401 | 1.23293 | 1.51165 | 1.75143 | 2.10561 | 2.5802 |
| tossup | start_difficulty_d3 | 1220 | 1.66718 | 0.471172 | -0.391397 | 0.783592 | 1.40072 | 1.73896 | 2.00323 | 2.30726 | 2.94722 |
| tossup | end_difficulty_d1 | 1220 | 0.343153 | 0.477292 | -2.20034 | -0.511494 | 0.0974687 | 0.393345 | 0.665187 | 0.981193 | 1.75414 |
| tossup | end_difficulty_d2 | 1220 | 0.294328 | 0.543964 | -2.06582 | -0.703712 | 0.0308817 | 0.350647 | 0.641204 | 1.09693 | 1.82441 |
| tossup | end_difficulty_d3 | 1220 | 0.598966 | 0.548023 | -2.13564 | -0.35267 | 0.313296 | 0.636756 | 0.925867 | 1.44803 | 2.35738 |
| tossup | total_drop_d1 | 1220 | 1.22637 | 0.400861 | 0.535266 | 0.726315 | 0.920653 | 1.1588 | 1.47442 | 1.94405 | 3.56779 |
| tossup | total_drop_d2 | 1220 | 1.16519 | 0.428154 | 0.455842 | 0.709977 | 0.86047 | 1.02511 | 1.37849 | 1.98089 | 3.59262 |
| tossup | total_drop_d3 | 1220 | 1.06822 | 0.38568 | 0.423256 | 0.656643 | 0.787551 | 0.939539 | 1.27439 | 1.82121 | 3.22805 |
| tossup | drop_share_1_d1 | 1220 | 0.187212 | 0.0645879 | 0.0531218 | 0.0960658 | 0.135192 | 0.175791 | 0.240971 | 0.296594 | 0.433613 |
| tossup | drop_share_2_d1 | 1220 | 0.264539 | 0.076088 | 0.0824621 | 0.133287 | 0.204511 | 0.272908 | 0.32551 | 0.367166 | 0.606747 |
| tossup | drop_share_3_d1 | 1220 | 0.54825 | 0.131296 | 0.233939 | 0.359837 | 0.432744 | 0.547426 | 0.655838 | 0.765892 | 0.864416 |
| tossup | drop_share_1_d2 | 1220 | 0.206677 | 0.0645906 | 0.0530944 | 0.0978618 | 0.155243 | 0.21277 | 0.259207 | 0.299309 | 0.372631 |
| tossup | drop_share_2_d2 | 1220 | 0.279714 | 0.0692135 | 0.0844736 | 0.137188 | 0.234122 | 0.301722 | 0.331085 | 0.358677 | 0.492339 |
| tossup | drop_share_3_d2 | 1220 | 0.513609 | 0.12653 | 0.177657 | 0.361794 | 0.40829 | 0.481807 | 0.607866 | 0.75792 | 0.848312 |
| tossup | drop_share_1_d3 | 1220 | 0.208623 | 0.0696187 | 0.0391516 | 0.0901771 | 0.151722 | 0.227778 | 0.263919 | 0.292546 | 0.447646 |
| tossup | drop_share_2_d3 | 1220 | 0.284709 | 0.074919 | 0.0549371 | 0.12934 | 0.247654 | 0.310302 | 0.331041 | 0.365153 | 0.584236 |
| tossup | drop_share_3_d3 | 1220 | 0.506668 | 0.131852 | 0.224504 | 0.368384 | 0.406695 | 0.457481 | 0.590501 | 0.774423 | 0.905911 |
| tossup | r_1 | 1220 | 0.369529 | 0.212206 | 0.0214001 | 0.0557152 | 0.184542 | 0.371249 | 0.524192 | 0.743617 | 0.894813 |
| tossup | r_2 | 1220 | 0.260826 | 0.170064 | 0.0223388 | 0.0490775 | 0.123731 | 0.226056 | 0.36902 | 0.592785 | 0.83466 |
| tossup | r_3 | 1220 | 0.369645 | 0.23262 | 0.0392806 | 0.0675665 | 0.153984 | 0.33725 | 0.554049 | 0.775812 | 0.872642 |
| tossup | r_norm | 1220 | 0.681554 | 0.068322 | 0.577372 | 0.589713 | 0.629719 | 0.668711 | 0.726683 | 0.813217 | 0.897913 |
