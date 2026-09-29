# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.1708 |
| tournament_team_bonus_ppg_spearman | 0.908122 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 32.9203 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.891042 |
| log_loss | 0.416471 |
| ece | 0.0185444 |
| brier | 0.133279 |
| part_accuracy | 0.808629 |
| part_accuracy_easy | 0.913477 |
| part_accuracy_medium | 0.673394 |
| part_accuracy_hard | 0.839016 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.283074 |
| part_accuracy_macro_team | 0.812949 |
| part_accuracy_macro_bonus | 0.80562 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.342999 |
| probability_p10 | 0.0579547 |
| probability_p50 | 0.530136 |
| probability_p90 | 0.958674 |
| mean_predictive_variance | 0.131808 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.509279 |
| ranked_probability_score | 0.11842 |
| bonus_total_score_log_loss | 1.03463 |
| ppb_mae | 2.34643 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 18.2701 | 0.966667 | 21.388 |
| 2024-acf-fall-at-cornell | 15 | 17 | 17.1106 | 0.879357 | 20.9369 |
| 2024-acf-fall-at-georgia | 24 | 26 | 16.6094 | 0.935365 | 31.5921 |
| 2024-acf-fall-at-illinois | 18 | 22 | 19.1159 | 0.991729 | 31.6263 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 22.5103 | 0.919983 | 26.8967 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 22.0449 | 0.901049 | 37.4438 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 23.7286 | 0.904295 | 41.9554 |
| 2024-acf-fall-at-washington | 14 | 13 | 20.7744 | 0.924093 | 30.9704 |
| 2024-acf-nationals | 47 | 81 | 17.1014 | 0.902573 | 30.2183 |
| 2024-acf-regionals-berkeley | 5 | 6 | 36.2985 | 1 | 71.0437 |
| 2024-acf-regionals-cornell | 6 | 6 | 25.2653 | 0.771429 | 43.764 |
| 2024-acf-regionals-imperial | 15 | 18 | 25.1908 | 0.934764 | 28.6679 |
| 2024-acf-regionals-jmu | 20 | 25 | 21.419 | 0.939052 | 27.8406 |
| 2024-acf-regionals-minnesota | 4 | 4 | 14.3002 | 0.8 | 20.3663 |
| 2024-acf-regionals-mit | 2 | 1 | 21.4591 | 1 | 42.9181 |
| 2024-acf-regionals-nebraska | 9 | 14 | 24.3616 | 0.8 | 47.7038 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 18.8334 | 0.892857 | 35.5719 |
| 2024-acf-regionals-rutgers | 11 | 11 | 20.3172 | 0.936364 | 36.8622 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 23.1219 | 0.762209 | 34.0209 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 27.923 | 0.970601 | 39.7475 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 7.96264 | 0.996965 | 19.4964 |
| 2024-acf-winter-at-clemson | 18 | 17 | 18.9175 | 0.945248 | 36.6412 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 27.0605 | 0.935203 | 37.2743 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 18.1318 | 0.952596 | 27.8964 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 22.638 | 0.934368 | 25.9079 |
| 2024-acf-winter-at-online | 14 | 19 | 15.9649 | 0.933923 | 27.2859 |
| 2024-acf-winter-at-oxford | 18 | 19 | 18.577 | 0.847703 | 39.863 |
| 2024-acf-winter-at-ubc | 6 | 6 | 29.2475 | 0.657143 | 44.9581 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 48.6966 | 1 | 63.9995 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

[Fitted synergy parameters](graphs/parameters/synergy_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25866 | 0.0185444 | 0.133279 | 0.891042 | 0.416471 |
| bonus_part_correctness | tier | fall | 8259 | 0.0205753 | 0.131656 | 0.890555 | 0.408968 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0295315 | 0.136308 | 0.88419 | 0.426936 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0192946 | 0.135696 | 0.887129 | 0.42311 |
| bonus_part_correctness | tier | winter | 7983 | 0.021296 | 0.131725 | 0.892854 | 0.414232 |
| bonus_part_correctness | category | Current Events | 258 | 0.0708428 | 0.1401 | 0.883609 | 0.435959 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0298577 | 0.137331 | 0.88466 | 0.427655 |
| bonus_part_correctness | category | Geography | 450 | 0.0460047 | 0.13161 | 0.89248 | 0.408939 |
| bonus_part_correctness | category | History | 4116 | 0.02086 | 0.12874 | 0.897599 | 0.401459 |
| bonus_part_correctness | category | Literature | 4092 | 0.0230723 | 0.131351 | 0.892807 | 0.412175 |
| bonus_part_correctness | category | Mythology | 951 | 0.0436849 | 0.132677 | 0.885932 | 0.414526 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0384463 | 0.120847 | 0.907662 | 0.387314 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0397836 | 0.143517 | 0.874865 | 0.447917 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0631871 | 0.13313 | 0.887662 | 0.403517 |
| bonus_part_correctness | category | Religion | 1029 | 0.034612 | 0.130456 | 0.89734 | 0.406175 |
| bonus_part_correctness | category | Science | 4089 | 0.0183372 | 0.134844 | 0.887442 | 0.423605 |
| bonus_part_correctness | category | Social Science | 891 | 0.0488119 | 0.123144 | 0.903338 | 0.386235 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0192946 | 0.135696 | 0.887129 | 0.42311 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0365744 | 0.0708368 | 0.801603 | 0.24985 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0385186 | 0.120921 | 0.748639 | 0.3934 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0463599 | 0.208079 | 0.74103 | 0.606162 |
