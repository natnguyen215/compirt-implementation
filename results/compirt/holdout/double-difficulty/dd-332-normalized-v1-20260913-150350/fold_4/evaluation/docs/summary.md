# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-20260913-150350/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-20260913-150350/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 284403 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.726677 |
| log_loss | 0.474419 |
| ece | 0.0120256 |
| brier | 0.153183 |
| accuracy | 0.789105 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0157497 |
| probability_std | 0.139147 |
| probability_p10 | 0.581331 |
| probability_p50 | 0.810531 |
| probability_p90 | 0.917042 |
| mean_predictive_variance | 0.154702 |
| integrated_brier_score | 0.101581 |
| joint_tossup_event_log_loss | 6.60374 |
| buzz_position_mae | 0.15319 |
| buzz_position_median_absolute_error | 0.136227 |
| buzz_position_bias | -0.0482858 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.35329 |
| first_buzzer_mean_reciprocal_rank | 0.564422 |
| first_buzzer_log_loss | 1.68275 |
| first_buzzer_events | 9270 |
| first_buzzer_player_replay_accuracy | 0.178317 |
| first_buzzer_team_replay_accuracy | 0.412513 |
| tossup_scorer_player_replay_accuracy | 0.208742 |
| tossup_scorer_team_replay_accuracy | 0.403625 |
| tossup_game_winner_accuracy | 0.641921 |
| tossup_model_official_winner_accuracy | 0.663793 |
| tossup_game_margin_mae | 49.2004 |
| tossup_game_zero_margin_mae | 58.0704 |
| tournament_player_ppg_spearman | 0.573974 |
| tournament_player_ppg_mae | 13.2307 |
| tournament_player_ppg_top10_overlap | 0.631034 |
| tournament_player_ppg_top10_random_overlap | 0.291672 |
| tournament_player_ppg_top10_adjusted_overlap | 0.475374 |
| neg_auroc | 0.726677 |
| neg_average_precision | 0.458391 |
| neg_precision | 0.647177 |
| neg_recall | 0.152784 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.174227 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0295295 |
| no_buzz_calibration_error | 0.0178024 |
| no_buzz_brier | 0.0129018 |
| full_pmf_max_mass_error | 6.66134e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9380 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 464 |
| first_buzzer_player_replay_accuracy_events | 9270 |
| first_buzzer_team_replay_accuracy_events | 9270 |
| tossup_scorer_player_replay_accuracy_events | 9380 |
| tossup_scorer_team_replay_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 458 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.641921 |
| tossup_game_margin_mae | 49.2004 |
| tossup_game_zero_margin_mae | 58.0704 |
| tossup_game_margin_mae_games | 469 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 458 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.726677 | 0.474419 | 0.0120256 | 0.153183 | 0.789105 | 0.773355 | 0.0157497 | 0.139147 | 0.581331 | 0.810531 | 0.917042 | 0.154702 |
| tossup_correctness | tier | fall | 2876 | 0.730617 | 0.450847 | 0.010879 | 0.14384 | 0.804242 | 0.793115 | 0.0111266 | 0.136855 | 0.591337 | 0.821094 | 0.924303 | 0.149181 |
| tossup_correctness | tier | nationals | 1579 | 0.721088 | 0.523273 | 0.0358224 | 0.173189 | 0.747942 | 0.729576 | 0.0183661 | 0.148542 | 0.563862 | 0.801553 | 0.910688 | 0.158849 |
| tossup_correctness | tier | regionals | 1990 | 0.732119 | 0.480181 | 0.0281615 | 0.155886 | 0.786935 | 0.765829 | 0.0211055 | 0.138592 | 0.571452 | 0.798938 | 0.908653 | 0.160121 |
| tossup_correctness | tier | winter | 2825 | 0.719282 | 0.467052 | 0.0152224 | 0.149607 | 0.79823 | 0.783009 | 0.0152212 | 0.13534 | 0.590746 | 0.811177 | 0.916047 | 0.154188 |
| tossup_correctness | category | Current Events | 123 | 0.77036 | 0.462197 | 0.0696589 | 0.150132 | 0.772358 | 0.764228 | 0.00813008 | 0.134186 | 0.569432 | 0.754972 | 0.912585 | 0.171911 |
| tossup_correctness | category | Fine Arts | 1093 | 0.738459 | 0.468822 | 0.0218323 | 0.150413 | 0.796889 | 0.769442 | 0.0274474 | 0.141571 | 0.582336 | 0.821905 | 0.920057 | 0.150928 |
| tossup_correctness | category | Geography | 191 | 0.796867 | 0.489506 | 0.0786346 | 0.159167 | 0.759162 | 0.691099 | 0.0680628 | 0.199479 | 0.449972 | 0.768742 | 0.895932 | 0.168106 |
| tossup_correctness | category | History | 1469 | 0.721127 | 0.497571 | 0.0291676 | 0.163564 | 0.76855 | 0.758339 | 0.010211 | 0.140525 | 0.577449 | 0.809627 | 0.920057 | 0.154881 |
| tossup_correctness | category | Literature | 1436 | 0.71499 | 0.432509 | 0.0175438 | 0.13566 | 0.816852 | 0.81546 | 0.00139276 | 0.117553 | 0.651421 | 0.845722 | 0.927427 | 0.138722 |
| tossup_correctness | category | Mythology | 325 | 0.686346 | 0.412705 | 0.0667925 | 0.127499 | 0.84 | 0.843077 | -0.00307692 | 0.0999565 | 0.67058 | 0.821915 | 0.913416 | 0.147251 |
| tossup_correctness | category | Other Academic | 67 | 0.684636 | 0.485357 | 0.0726172 | 0.15679 | 0.80597 | 0.791045 | 0.0149254 | 0.132414 | 0.592322 | 0.770366 | 0.890147 | 0.171114 |
| tossup_correctness | category | Philosophy | 322 | 0.683966 | 0.487037 | 0.0446295 | 0.158978 | 0.767081 | 0.785714 | -0.0186335 | 0.12458 | 0.611601 | 0.812862 | 0.932203 | 0.150566 |
| tossup_correctness | category | Popular Culture | 100 | 0.541369 | 0.363707 | 0.0648263 | 0.104833 | 0.89 | 0.89 | 0 | 0.0655246 | 0.761617 | 0.854446 | 0.920394 | 0.126574 |
| tossup_correctness | category | Religion | 365 | 0.669142 | 0.556043 | 0.0380991 | 0.185885 | 0.736986 | 0.723288 | 0.0136986 | 0.142055 | 0.561253 | 0.789369 | 0.912619 | 0.16294 |
| tossup_correctness | category | Science | 1456 | 0.726464 | 0.480831 | 0.0142599 | 0.155581 | 0.785714 | 0.76717 | 0.018544 | 0.143179 | 0.563981 | 0.797405 | 0.908005 | 0.161139 |
| tossup_correctness | category | Social Science | 333 | 0.749931 | 0.494389 | 0.0502615 | 0.160504 | 0.780781 | 0.72973 | 0.0510511 | 0.161112 | 0.496181 | 0.782042 | 0.90987 | 0.168031 |
| tossup_correctness | category | Unknown | 1990 | 0.732119 | 0.480181 | 0.0281615 | 0.155886 | 0.786935 | 0.765829 | 0.0211055 | 0.138592 | 0.571452 | 0.798938 | 0.908653 | 0.160121 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.766833 | 0.483047 | 0.0615673 | 0.15792 | 0.765363 | 0.748603 | 0.0167598 | 0.147758 | 0.522648 | 0.772147 | 0.879318 | 0.175006 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.703348 | 0.501603 | 0.0138991 | 0.163588 | 0.777429 | 0.754441 | 0.0229885 | 0.139202 | 0.556491 | 0.785523 | 0.902464 | 0.165378 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.725624 | 0.483237 | 0.024482 | 0.157068 | 0.783477 | 0.766682 | 0.0167953 | 0.1368 | 0.591282 | 0.809276 | 0.915047 | 0.155687 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.716068 | 0.462353 | 0.0140075 | 0.147882 | 0.802216 | 0.787441 | 0.014775 | 0.128759 | 0.62009 | 0.821733 | 0.919295 | 0.149071 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.740184 | 0.470677 | 0.017988 | 0.15197 | 0.785303 | 0.771758 | 0.0135455 | 0.148297 | 0.552474 | 0.811278 | 0.920323 | 0.154956 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 2.66324 | 0.733742 | 0.433927 | 1.44795 | 2.1689 | 2.66561 | 3.13457 | 3.95349 | 4.61046 |
| player | theta_1 | 1196 | -1.20201 | 0.843963 | -3.75953 | -2.45545 | -1.75927 | -1.27857 | -0.724206 | 0.301639 | 2.0551 |
| player | theta_2 | 1196 | -0.988213 | 0.658746 | -3.2659 | -2.10406 | -1.40312 | -1.00616 | -0.566051 | 0.0667515 | 1.49178 |
| player | theta_3 | 1196 | -1.11251 | 0.771382 | -3.34414 | -2.33063 | -1.59852 | -1.17138 | -0.659182 | 0.281428 | 2.09657 |
| player | theta_norm | 1196 | 2.24171 | 0.611463 | 0.530928 | 1.31504 | 1.80912 | 2.20769 | 2.63185 | 3.30005 | 4.30589 |
| tossup | start_difficulty_d1 | 1240 | -1.76347 | 0.546553 | -3.47088 | -2.54166 | -2.13561 | -1.80965 | -1.46415 | -0.778275 | 1.45283 |
| tossup | start_difficulty_d2 | 1240 | -1.75124 | 0.501962 | -3.39966 | -2.50464 | -2.1139 | -1.77751 | -1.43288 | -0.837879 | -0.125359 |
| tossup | start_difficulty_d3 | 1240 | -1.75216 | 0.510714 | -3.59175 | -2.52542 | -2.11761 | -1.78683 | -1.41826 | -0.848367 | 0.681724 |
| tossup | end_difficulty_d1 | 1240 | -2.75168 | 0.636554 | -4.62168 | -3.65842 | -3.20562 | -2.81403 | -2.39398 | -1.60494 | 0.776106 |
| tossup | end_difficulty_d2 | 1240 | -2.73718 | 0.58868 | -4.73837 | -3.62578 | -3.15201 | -2.75664 | -2.3628 | -1.68279 | -0.836636 |
| tossup | end_difficulty_d3 | 1240 | -2.73713 | 0.595327 | -4.88228 | -3.64771 | -3.16668 | -2.76966 | -2.34739 | -1.69138 | 0.0140107 |
| tossup | total_drop_d1 | 1240 | 0.988209 | 0.111119 | 0.588575 | 0.798233 | 0.913713 | 0.992303 | 1.06282 | 1.16637 | 1.39093 |
| tossup | total_drop_d2 | 1240 | 0.985941 | 0.103798 | 0.678286 | 0.816783 | 0.916921 | 0.984595 | 1.05359 | 1.1611 | 1.34243 |
| tossup | total_drop_d3 | 1240 | 0.984969 | 0.104096 | 0.625654 | 0.819742 | 0.913997 | 0.985028 | 1.05483 | 1.16254 | 1.40876 |
| tossup | drop_share_1_d1 | 1240 | 0.304147 | 0.0154873 | 0.229968 | 0.279335 | 0.294739 | 0.304399 | 0.314689 | 0.328058 | 0.365931 |
| tossup | drop_share_2_d1 | 1240 | 0.347104 | 0.0114089 | 0.30988 | 0.327994 | 0.339523 | 0.347247 | 0.355083 | 0.365034 | 0.387833 |
| tossup | drop_share_3_d1 | 1240 | 0.348749 | 0.0165707 | 0.296689 | 0.322773 | 0.337513 | 0.348469 | 0.35956 | 0.376788 | 0.417175 |
| tossup | drop_share_1_d2 | 1240 | 0.303631 | 0.0143391 | 0.245132 | 0.279448 | 0.294407 | 0.303783 | 0.313192 | 0.326226 | 0.346083 |
| tossup | drop_share_2_d2 | 1240 | 0.346945 | 0.0113629 | 0.307706 | 0.328071 | 0.339194 | 0.346657 | 0.354629 | 0.365464 | 0.3858 |
| tossup | drop_share_3_d2 | 1240 | 0.349424 | 0.0154601 | 0.302749 | 0.324778 | 0.3387 | 0.349493 | 0.358942 | 0.375444 | 0.415749 |
| tossup | drop_share_1_d3 | 1240 | 0.303457 | 0.0151142 | 0.240302 | 0.277711 | 0.294099 | 0.303781 | 0.313517 | 0.326906 | 0.359271 |
| tossup | drop_share_2_d3 | 1240 | 0.347143 | 0.0112157 | 0.311455 | 0.328772 | 0.339862 | 0.346907 | 0.35432 | 0.365315 | 0.384351 |
| tossup | drop_share_3_d3 | 1240 | 0.3494 | 0.0158872 | 0.30771 | 0.325196 | 0.338519 | 0.348963 | 0.35898 | 0.377453 | 0.417312 |
| tossup | r_1 | 1240 | 0.320927 | 0.144756 | 0.0583125 | 0.131289 | 0.213359 | 0.293653 | 0.408542 | 0.595674 | 0.860363 |
| tossup | r_2 | 1240 | 0.335657 | 0.113625 | 0.0572056 | 0.162568 | 0.256318 | 0.331713 | 0.403281 | 0.538996 | 0.825699 |
| tossup | r_3 | 1240 | 0.343417 | 0.126078 | 0.0725238 | 0.159191 | 0.254926 | 0.332675 | 0.41582 | 0.574967 | 0.842181 |
| tossup | r_norm | 1240 | 0.61765 | 0.0427098 | 0.57741 | 0.579232 | 0.588153 | 0.604108 | 0.631724 | 0.700846 | 0.866019 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.49492 | 0.484072 | 2.20817 | 3.80179 | 4.22536 | 4.45504 | 4.71209 | 5.41733 | 6.39697 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.46702 | 0.429525 | 2.15513 | 3.79766 | 4.24172 | 4.45227 | 4.67155 | 5.20383 | 6.60967 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.48082 | 0.435633 | 2.32761 | 3.7931 | 4.24683 | 4.44836 | 4.72215 | 5.21515 | 6.21909 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.8463 | 2.2701 | -11.1941 | -2.96275 | 0.914606 | 2.93247 | 3.3274 | 3.6473 | 4.38478 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.31587 | 2.03145 | -9.09464 | -2.58994 | 2.41374 | 3.14207 | 3.40164 | 3.70236 | 4.26429 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.2138 | 2.00265 | -11.2546 | -2.08641 | 1.91251 | 3.07551 | 3.37178 | 3.72846 | 4.33975 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.64861 | 2.44092 | 0.869001 | 0.984647 | 1.05975 | 1.28224 | 3.79225 | 7.96668 | 15.9612 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.15115 | 2.18853 | 0.90962 | 0.963319 | 1.02408 | 1.18303 | 1.82445 | 7.25392 | 13.962 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.26702 | 2.12742 | 0.868324 | 0.968821 | 1.02876 | 1.21442 | 2.46365 | 6.93539 | 15.7549 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.238245 | 0.0789202 | 0.0372699 | 0.0850087 | 0.185407 | 0.272387 | 0.292947 | 0.315738 | 0.545206 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.344415 | 0.0734035 | 0.0552122 | 0.186821 | 0.33791 | 0.352022 | 0.366647 | 0.447571 | 0.690792 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.41734 | 0.12602 | 0.130279 | 0.306365 | 0.348461 | 0.368856 | 0.431909 | 0.721829 | 0.901469 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.253754 | 0.0693216 | 0.0327283 | 0.0943972 | 0.236546 | 0.279918 | 0.296233 | 0.315105 | 0.626894 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.348883 | 0.0585878 | 0.0639572 | 0.245698 | 0.340933 | 0.351191 | 0.363646 | 0.410734 | 0.683641 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.397362 | 0.102 | 0.0970806 | 0.319929 | 0.348934 | 0.365432 | 0.39951 | 0.648576 | 0.890693 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.248331 | 0.0696275 | 0.0406095 | 0.0964115 | 0.213682 | 0.27475 | 0.296085 | 0.315021 | 0.544267 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.351099 | 0.0597037 | 0.0869056 | 0.241547 | 0.339857 | 0.351279 | 0.365299 | 0.441706 | 0.712011 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.40057 | 0.103127 | 0.079999 | 0.318058 | 0.349584 | 0.366825 | 0.407987 | 0.648288 | 0.871505 |
| tossup_hazard | hazard_r_1 | 1240 | 0.374806 | 0.278536 | 0.0332253 | 0.0632373 | 0.133025 | 0.271917 | 0.607924 | 0.880525 | 0.949068 |
| tossup_hazard | hazard_r_2 | 1240 | 0.29148 | 0.212719 | 0.0205929 | 0.0516116 | 0.117269 | 0.227407 | 0.432928 | 0.715987 | 0.863126 |
| tossup_hazard | hazard_r_3 | 1240 | 0.333714 | 0.249845 | 0.0224098 | 0.0476968 | 0.122004 | 0.244791 | 0.54842 | 0.785462 | 0.920625 |
