# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/perceived-logit-grid/perceived-logit/dim_6/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/perceived-logit-grid/perceived-logit/dim_6/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 323777 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.601724 |
| log_loss | 0.5724 |
| ece | 0.10975 |
| brier | 0.187651 |
| accuracy | 0.739914 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0334412 |
| probability_std | 0.167456 |
| probability_p10 | 0.467913 |
| probability_p50 | 0.708582 |
| probability_p90 | 0.913327 |
| mean_predictive_variance | 0.183401 |
| integrated_brier_score | 0.114812 |
| joint_tossup_event_log_loss | 6.90413 |
| buzz_position_mae | 0.188362 |
| buzz_position_median_absolute_error | 0.165352 |
| buzz_position_bias | -0.122933 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.38986 |
| first_buzzer_mean_reciprocal_rank | 0.59325 |
| first_buzzer_log_loss | 1.61829 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.647033 |
| tossup_scorer_player_top1_accuracy | 0.296908 |
| tossup_scorer_team_top1_accuracy | 0.451919 |
| tossup_game_winner_accuracy | 0.778993 |
| tossup_game_margin_mae | 39.0175 |
| tournament_player_ppg_spearman | 0.596783 |
| tournament_player_ppg_mae | 11.0756 |
| tournament_player_ppg_top10_overlap | 0.641379 |
| neg_auroc | 0.601724 |
| neg_average_precision | 0.312435 |
| neg_precision | 0.374798 |
| neg_recall | 0.220847 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0985463 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0931208 |
| no_buzz_calibration_error | 0.0813937 |
| no_buzz_brier | 0.0270519 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.601724 | 0.5724 | 0.10975 | 0.187651 | 0.739914 | 0.773355 | -0.0334412 | 0.167456 | 0.467913 | 0.708582 | 0.913327 | 0.183401 |
| tossup_correctness | tier | fall | 2876 | 0.579056 | 0.551898 | 0.0970881 | 0.172972 | 0.783032 | 0.793115 | -0.0100834 | 0.151602 | 0.543526 | 0.765728 | 0.946667 | 0.162944 |
| tossup_correctness | tier | nationals | 1579 | 0.617289 | 0.605315 | 0.105806 | 0.209462 | 0.671311 | 0.729576 | -0.0582647 | 0.170767 | 0.386907 | 0.643719 | 0.8359 | 0.205371 |
| tossup_correctness | tier | regionals | 1990 | 0.615245 | 0.577004 | 0.117981 | 0.193293 | 0.715578 | 0.765829 | -0.0502513 | 0.166274 | 0.42994 | 0.68088 | 0.86301 | 0.196225 |
| tossup_correctness | tier | winter | 2825 | 0.580978 | 0.57163 | 0.125648 | 0.186429 | 0.751504 | 0.783009 | -0.0315044 | 0.160527 | 0.488014 | 0.706439 | 0.924273 | 0.182914 |
| tossup_correctness | category | Current Events | 123 | 0.590242 | 0.584238 | 0.12296 | 0.198346 | 0.699187 | 0.764228 | -0.0650407 | 0.16714 | 0.449924 | 0.682432 | 0.89596 | 0.189915 |
| tossup_correctness | category | Fine Arts | 1093 | 0.602759 | 0.581093 | 0.122506 | 0.188699 | 0.761208 | 0.769442 | -0.00823422 | 0.170924 | 0.466403 | 0.705174 | 0.931075 | 0.180805 |
| tossup_correctness | category | Geography | 191 | 0.666025 | 0.595117 | 0.0663994 | 0.200377 | 0.691099 | 0.691099 | 0 | 0.173496 | 0.451964 | 0.669585 | 0.915835 | 0.187265 |
| tossup_correctness | category | History | 1469 | 0.629484 | 0.562104 | 0.0798511 | 0.18405 | 0.748809 | 0.758339 | -0.00953029 | 0.159559 | 0.493903 | 0.717066 | 0.905708 | 0.182038 |
| tossup_correctness | category | Literature | 1436 | 0.533236 | 0.566353 | 0.142213 | 0.180076 | 0.763231 | 0.81546 | -0.0522284 | 0.169321 | 0.47988 | 0.745018 | 0.938976 | 0.170761 |
| tossup_correctness | category | Mythology | 325 | 0.527694 | 0.543587 | 0.170959 | 0.176669 | 0.750769 | 0.843077 | -0.0923077 | 0.169073 | 0.465214 | 0.694047 | 0.937904 | 0.181623 |
| tossup_correctness | category | Other Academic | 67 | 0.619946 | 0.607988 | 0.198585 | 0.212721 | 0.671642 | 0.791045 | -0.119403 | 0.195228 | 0.298583 | 0.615921 | 0.857979 | 0.203337 |
| tossup_correctness | category | Philosophy | 322 | 0.560635 | 0.590082 | 0.143352 | 0.186757 | 0.757764 | 0.785714 | -0.0279503 | 0.171424 | 0.472325 | 0.736515 | 0.94604 | 0.174672 |
| tossup_correctness | category | Popular Culture | 100 | 0.53524 | 0.480912 | 0.183535 | 0.153288 | 0.8 | 0.89 | -0.09 | 0.162389 | 0.493342 | 0.69241 | 0.90679 | 0.180424 |
| tossup_correctness | category | Religion | 365 | 0.642327 | 0.592295 | 0.0797565 | 0.19491 | 0.715068 | 0.723288 | -0.00821918 | 0.169124 | 0.485774 | 0.717607 | 0.933549 | 0.17865 |
| tossup_correctness | category | Science | 1456 | 0.591972 | 0.571907 | 0.101007 | 0.18778 | 0.741071 | 0.76717 | -0.0260989 | 0.156777 | 0.496981 | 0.714649 | 0.918513 | 0.182482 |
| tossup_correctness | category | Social Science | 333 | 0.644947 | 0.582123 | 0.0939158 | 0.196133 | 0.708709 | 0.72973 | -0.021021 | 0.174286 | 0.466208 | 0.688228 | 0.917365 | 0.187468 |
| tossup_correctness | category | Unknown | 1990 | 0.615245 | 0.577004 | 0.117981 | 0.193293 | 0.715578 | 0.765829 | -0.0502513 | 0.166274 | 0.42994 | 0.68088 | 0.86301 | 0.196225 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.515755 | 0.714924 | 0.25712 | 0.254804 | 0.558659 | 0.748603 | -0.189944 | 0.19556 | 0.317543 | 0.567462 | 0.819094 | 0.207503 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.566464 | 0.649506 | 0.193918 | 0.22468 | 0.649948 | 0.754441 | -0.104493 | 0.182625 | 0.368677 | 0.607828 | 0.865078 | 0.204917 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.598106 | 0.600037 | 0.151427 | 0.201677 | 0.710395 | 0.766682 | -0.0562869 | 0.17256 | 0.419213 | 0.643317 | 0.889542 | 0.198587 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.637524 | 0.535311 | 0.115532 | 0.173545 | 0.77233 | 0.787441 | -0.0151108 | 0.1563 | 0.491071 | 0.706158 | 0.916918 | 0.185066 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.611108 | 0.555557 | 0.0512329 | 0.175341 | 0.769387 | 0.771758 | -0.00237047 | 0.134143 | 0.584133 | 0.775092 | 0.948001 | 0.161959 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1196 | 0.566967 | 1.49969 | -3.31905 | -2.06994 | -0.83561 | 1.38095 | 1.8015 | 2.12313 | 2.71355 |
| player | beta | 1196 | -5.49909 | 1.2668 | -7.94803 | -6.98987 | -6.42171 | -5.86086 | -4.80789 | -2.80117 | -2.11103 |
| player | theta_1 | 1196 | -0.533931 | 1.27742 | -4.01839 | -2.54794 | -1.55459 | -0.593312 | 0.442039 | 1.64511 | 2.92907 |
| player | theta_2 | 1196 | -0.605766 | 1.44262 | -3.82502 | -2.70782 | -1.7875 | -0.84227 | 0.729015 | 1.65944 | 2.77437 |
| player | theta_3 | 1196 | -0.873534 | 1.97251 | -4.68946 | -3.60075 | -2.62046 | -1.24045 | 1.13148 | 2.02195 | 3.81695 |
| player | theta_4 | 1196 | -0.517886 | 1.2236 | -3.67356 | -2.48449 | -1.4343 | -0.564331 | 0.377566 | 1.50888 | 2.7043 |
| player | theta_5 | 1196 | -0.471339 | 0.894667 | -3.62609 | -2.05606 | -1.07009 | -0.373342 | 0.253901 | 0.72455 | 2.06003 |
| player | theta_6 | 1196 | -0.444583 | 0.935919 | -3.00754 | -1.99493 | -1.1929 | -0.411247 | 0.325483 | 0.834478 | 2.76243 |
| player | theta_norm | 1196 | 3.37548 | 1.21605 | 0.173064 | 1.3661 | 2.4821 | 3.37816 | 4.29154 | 5.29145 | 6.33748 |
| tossup | start_difficulty_d1 | 1240 | -0.0621709 | 0.551139 | -1.74286 | -1.28136 | -0.278412 | 0.0603212 | 0.291477 | 0.613953 | 1.44479 |
| tossup | start_difficulty_d2 | 1240 | -0.0976471 | 0.653085 | -2.47593 | -1.50273 | -0.332475 | 0.0728386 | 0.303022 | 0.660127 | 1.47413 |
| tossup | start_difficulty_d3 | 1240 | -0.172701 | 0.746503 | -2.55126 | -1.73175 | -0.49025 | 0.00175246 | 0.331536 | 0.76465 | 1.77486 |
| tossup | start_difficulty_d4 | 1240 | 0.0240169 | 0.60567 | -2.27975 | -1.56881 | -0.152276 | 0.208497 | 0.36851 | 0.671915 | 1.27792 |
| tossup | start_difficulty_d5 | 1240 | 0.168084 | 0.372779 | -1.99878 | -0.480929 | 0.0367456 | 0.225068 | 0.375709 | 0.655447 | 1.73322 |
| tossup | start_difficulty_d6 | 1240 | 0.148248 | 0.393925 | -1.98651 | -0.592703 | 0.0102115 | 0.221623 | 0.379836 | 0.648315 | 1.2544 |
| tossup | end_difficulty_d1 | 1240 | -1.52677 | 1.52655 | -10.0514 | -5.33026 | -1.5132 | -0.977112 | -0.709771 | -0.342938 | 0.261821 |
| tossup | end_difficulty_d2 | 1240 | -1.87213 | 1.8744 | -11.4253 | -5.89126 | -2.17753 | -1.04497 | -0.71146 | -0.4013 | 0.428246 |
| tossup | end_difficulty_d3 | 1240 | -2.45687 | 2.33797 | -11.6603 | -6.97372 | -4.49685 | -1.28244 | -0.754343 | -0.345403 | 0.595391 |
| tossup | end_difficulty_d4 | 1240 | -1.45896 | 1.72623 | -11.753 | -5.9158 | -1.33945 | -0.789917 | -0.596406 | -0.317268 | 0.416229 |
| tossup | end_difficulty_d5 | 1240 | -1.21936 | 1.61829 | -13.3427 | -4.84239 | -1.08188 | -0.775101 | -0.601456 | -0.325656 | 0.108456 |
| tossup | end_difficulty_d6 | 1240 | -1.00426 | 1.05162 | -12.1285 | -2.12342 | -1.05486 | -0.758762 | -0.584873 | -0.28223 | 0.43389 |
| tossup | total_drop_d1 | 1240 | 1.4646 | 1.27492 | 0.828939 | 0.903116 | 0.961327 | 1.01089 | 1.13387 | 4.5103 | 11.4962 |
| tossup | total_drop_d2 | 1240 | 1.77448 | 1.68396 | 0.800738 | 0.90603 | 0.961425 | 1.02042 | 1.32009 | 5.62448 | 10.9402 |
| tossup | total_drop_d3 | 1240 | 2.28417 | 2.121 | 0.803808 | 0.90773 | 0.975491 | 1.06172 | 3.50432 | 6.87055 | 10.9657 |
| tossup | total_drop_d4 | 1240 | 1.48297 | 1.44381 | 0.788663 | 0.890668 | 0.943968 | 0.985017 | 1.0888 | 5.18169 | 10.5395 |
| tossup | total_drop_d5 | 1240 | 1.38745 | 1.63945 | 0.82244 | 0.897401 | 0.944266 | 0.982134 | 1.04555 | 5.21391 | 14.9898 |
| tossup | total_drop_d6 | 1240 | 1.15251 | 0.932786 | 0.820514 | 0.888329 | 0.937634 | 0.980592 | 1.038 | 1.34653 | 12.0118 |
| tossup | drop_share_1_d1 | 1240 | 0.272641 | 0.0540975 | 0.039503 | 0.121226 | 0.273925 | 0.288429 | 0.299153 | 0.317432 | 0.366531 |
| tossup | drop_share_2_d1 | 1240 | 0.335573 | 0.0477805 | 0.0752376 | 0.223681 | 0.33408 | 0.344701 | 0.353855 | 0.371072 | 0.501334 |
| tossup | drop_share_3_d1 | 1240 | 0.391785 | 0.0944808 | 0.205681 | 0.334045 | 0.352641 | 0.364595 | 0.3814 | 0.644205 | 0.873712 |
| tossup | drop_share_1_d2 | 1240 | 0.261175 | 0.0676182 | 0.0532345 | 0.10316 | 0.267036 | 0.289095 | 0.300349 | 0.316441 | 0.38577 |
| tossup | drop_share_2_d2 | 1240 | 0.325151 | 0.0616307 | 0.075155 | 0.156782 | 0.330867 | 0.343604 | 0.352968 | 0.36921 | 0.553722 |
| tossup | drop_share_3_d2 | 1240 | 0.413674 | 0.122284 | 0.256147 | 0.33158 | 0.351297 | 0.36544 | 0.388524 | 0.73926 | 0.858928 |
| tossup | drop_share_1_d3 | 1240 | 0.24786 | 0.0774628 | 0.0357016 | 0.0899443 | 0.20467 | 0.284237 | 0.298444 | 0.315548 | 0.549195 |
| tossup | drop_share_2_d3 | 1240 | 0.310767 | 0.0773186 | 0.0463492 | 0.134375 | 0.312484 | 0.340554 | 0.352816 | 0.370457 | 0.59315 |
| tossup | drop_share_3_d3 | 1240 | 0.441373 | 0.146306 | 0.179346 | 0.331526 | 0.353377 | 0.371246 | 0.477565 | 0.775927 | 0.911199 |
| tossup | drop_share_1_d4 | 1240 | 0.278318 | 0.0501377 | 0.0611096 | 0.14178 | 0.280443 | 0.292661 | 0.301737 | 0.31559 | 0.502789 |
| tossup | drop_share_2_d4 | 1240 | 0.338193 | 0.0435787 | 0.0898524 | 0.260769 | 0.33507 | 0.344399 | 0.353937 | 0.370729 | 0.523998 |
| tossup | drop_share_3_d4 | 1240 | 0.383489 | 0.0837039 | 0.236395 | 0.334646 | 0.351228 | 0.361734 | 0.374958 | 0.589425 | 0.849038 |
| tossup | drop_share_1_d5 | 1240 | 0.284547 | 0.0443117 | 0.0299232 | 0.19701 | 0.284284 | 0.293758 | 0.302782 | 0.316262 | 0.364043 |
| tossup | drop_share_2_d5 | 1240 | 0.339295 | 0.041318 | 0.0478354 | 0.317282 | 0.336917 | 0.345661 | 0.354249 | 0.367692 | 0.605956 |
| tossup | drop_share_3_d5 | 1240 | 0.376157 | 0.0804798 | 0.24944 | 0.334315 | 0.35003 | 0.358959 | 0.370376 | 0.472475 | 0.922241 |
| tossup | drop_share_1_d6 | 1240 | 0.288968 | 0.0330587 | 0.0563198 | 0.246845 | 0.28504 | 0.294941 | 0.303373 | 0.315461 | 0.37175 |
| tossup | drop_share_2_d6 | 1240 | 0.341731 | 0.0260891 | 0.102102 | 0.320672 | 0.336692 | 0.344956 | 0.35319 | 0.364465 | 0.397582 |
| tossup | drop_share_3_d6 | 1240 | 0.369301 | 0.0541015 | 0.307438 | 0.335167 | 0.349973 | 0.359592 | 0.370167 | 0.414788 | 0.816694 |
| tossup | r_1 | 1240 | 0.174526 | 0.136463 | 0.0287279 | 0.0550851 | 0.0861218 | 0.123976 | 0.201567 | 0.510729 | 0.653117 |
| tossup | r_2 | 1240 | 0.205175 | 0.178281 | 0.035085 | 0.057485 | 0.0851418 | 0.12171 | 0.253203 | 0.589153 | 0.715719 |
| tossup | r_3 | 1240 | 0.243673 | 0.189535 | 0.0286661 | 0.0628659 | 0.0998419 | 0.146934 | 0.38922 | 0.614418 | 0.773149 |
| tossup | r_4 | 1240 | 0.148093 | 0.132731 | 0.0299813 | 0.0472657 | 0.0680291 | 0.0948387 | 0.154247 | 0.469352 | 0.690151 |
| tossup | r_5 | 1240 | 0.116029 | 0.0865497 | 0.0254452 | 0.043725 | 0.0649864 | 0.0885025 | 0.128425 | 0.334534 | 0.575824 |
| tossup | r_6 | 1240 | 0.112503 | 0.0839199 | 0.0303175 | 0.045518 | 0.0655808 | 0.0868227 | 0.122953 | 0.305409 | 0.638775 |
| tossup | r_norm | 1240 | 0.541688 | 0.0703381 | 0.41257 | 0.439003 | 0.487021 | 0.531029 | 0.589405 | 0.666074 | 0.779965 |
