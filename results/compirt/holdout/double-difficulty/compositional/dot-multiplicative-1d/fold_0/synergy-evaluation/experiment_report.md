# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.6414 |
| tournament_team_bonus_ppg_spearman | 0.805012 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.0104 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.891173 |
| log_loss | 0.416435 |
| ece | 0.0132361 |
| brier | 0.1333 |
| part_accuracy | 0.809048 |
| part_accuracy_easy | 0.902742 |
| part_accuracy_medium | 0.684871 |
| part_accuracy_hard | 0.839531 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.290611 |
| part_accuracy_macro_team | 0.809191 |
| part_accuracy_macro_bonus | 0.805916 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.34814 |
| probability_p10 | 0.0529087 |
| probability_p50 | 0.524401 |
| probability_p90 | 0.963523 |
| mean_predictive_variance | 0.128323 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.511271 |
| ranked_probability_score | 0.117104 |
| bonus_total_score_log_loss | 1.02414 |
| ppb_mae | 2.32724 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 8.27098 | 0.995825 | 36.7647 |
| 2024-acf-fall-at-cornell | 17 | 18 | 24.5108 | 0.87362 | 33.2076 |
| 2024-acf-fall-at-georgia | 24 | 25 | 21.7582 | 0.91206 | 42.7213 |
| 2024-acf-fall-at-illinois | 19 | 22 | 21.137 | 0.895432 | 34.8754 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 16.5437 | 0.941105 | 26.3151 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 18.0847 | 0.913109 | 28.4298 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 19.0902 | 0.849786 | 36.5808 |
| 2024-acf-fall-at-washington | 14 | 13 | 20.5874 | 0.845817 | 35.4608 |
| 2024-acf-nationals | 46 | 81 | 20.0271 | 0.817523 | 31.379 |
| 2024-acf-regionals-berkeley | 5 | 6 | 34.7623 | 0.8 | 43.099 |
| 2024-acf-regionals-cornell | 6 | 6 | 24.9135 | 0.579771 | 41.4243 |
| 2024-acf-regionals-imperial | 14 | 18 | 22.5726 | 0.866887 | 39.7657 |
| 2024-acf-regionals-jmu | 18 | 23 | 19.2315 | 0.887742 | 29.0077 |
| 2024-acf-regionals-minnesota | 3 | 4 | 31.0883 | 1 | 51.8571 |
| 2024-acf-regionals-mit | 5 | 3 | 35.6333 | -0.9 | 38.3088 |
| 2024-acf-regionals-nebraska | 12 | 14 | 18.3582 | 0.928198 | 27.1579 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 14.5199 | 0.964286 | 12.9438 |
| 2024-acf-regionals-rutgers | 11 | 12 | 23.6374 | 0.943055 | 34.987 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 31.326 | 0.782691 | 29.074 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 20.8736 | 0.95 | 31.4142 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 14.6593 | 0.940649 | 25.0286 |
| 2024-acf-winter-at-clemson | 16 | 17 | 17.9248 | 0.935294 | 30.6528 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 16.3871 | 0.949342 | 27.3689 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 20.3866 | 0.941056 | 45.2 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 18.5143 | 0.95951 | 24.2072 |
| 2024-acf-winter-at-online | 16 | 19 | 16.2832 | 0.891017 | 26.4829 |
| 2024-acf-winter-at-oxford | 19 | 21 | 15.6857 | 0.92443 | 28.6807 |
| 2024-acf-winter-at-ubc | 5 | 6 | 20.92 | 0.7 | 38.5816 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 39.9127 | 0.257143 | 64.2373 |

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
| bonus_part_correctness | aggregate | all | 25818 | 0.0132361 | 0.1333 | 0.891173 | 0.416435 |
| bonus_part_correctness | tier | fall | 8415 | 0.0186789 | 0.135718 | 0.884234 | 0.418 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0329027 | 0.131591 | 0.890101 | 0.415092 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0210644 | 0.133923 | 0.88975 | 0.420354 |
| bonus_part_correctness | tier | winter | 8154 | 0.0180315 | 0.131294 | 0.893191 | 0.413071 |
| bonus_part_correctness | category | Current Events | 258 | 0.0549245 | 0.0995502 | 0.933353 | 0.337541 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0223737 | 0.141949 | 0.877468 | 0.441033 |
| bonus_part_correctness | category | Geography | 453 | 0.0453833 | 0.131997 | 0.887918 | 0.4177 |
| bonus_part_correctness | category | History | 4176 | 0.0212266 | 0.134932 | 0.889277 | 0.416645 |
| bonus_part_correctness | category | Literature | 4197 | 0.0169557 | 0.122547 | 0.907122 | 0.385173 |
| bonus_part_correctness | category | Mythology | 951 | 0.0368841 | 0.143395 | 0.86996 | 0.439868 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0395208 | 0.118573 | 0.914047 | 0.379482 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0353481 | 0.141986 | 0.876111 | 0.442331 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.076238 | 0.152485 | 0.858927 | 0.446454 |
| bonus_part_correctness | category | Religion | 1041 | 0.0415864 | 0.131096 | 0.893954 | 0.415064 |
| bonus_part_correctness | category | Science | 4152 | 0.0228013 | 0.133035 | 0.890139 | 0.417511 |
| bonus_part_correctness | category | Social Science | 915 | 0.0325252 | 0.134649 | 0.888038 | 0.421484 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0210644 | 0.133923 | 0.88975 | 0.420354 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0207462 | 0.0775318 | 0.788828 | 0.269597 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0261413 | 0.117688 | 0.772061 | 0.381305 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0452417 | 0.204681 | 0.750477 | 0.598403 |
