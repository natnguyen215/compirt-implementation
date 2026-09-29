# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.6788 |
| tournament_team_bonus_ppg_spearman | 0.864555 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 25.9151 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.896493 |
| log_loss | 0.407851 |
| ece | 0.0169707 |
| brier | 0.129197 |
| part_accuracy | 0.818537 |
| part_accuracy_easy | 0.901116 |
| part_accuracy_medium | 0.706484 |
| part_accuracy_hard | 0.848013 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.300101 |
| part_accuracy_macro_team | 0.819154 |
| part_accuracy_macro_bonus | 0.815964 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.335867 |
| probability_p10 | 0.0765947 |
| probability_p50 | 0.527504 |
| probability_p90 | 0.949506 |
| mean_predictive_variance | 0.136721 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.533233 |
| ranked_probability_score | 0.111129 |
| bonus_total_score_log_loss | 0.983696 |
| ppb_mae | 1.77648 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 15.8099 | 0.953983 | 46.2615 |
| 2024-acf-fall-at-cornell | 17 | 18 | 15.4289 | 0.936197 | 24.9772 |
| 2024-acf-fall-at-georgia | 24 | 25 | 14.6707 | 0.937746 | 29.5923 |
| 2024-acf-fall-at-illinois | 19 | 22 | 18.0868 | 0.946399 | 29.214 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 15.157 | 0.949694 | 27.1026 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 11.6247 | 0.966128 | 20.2726 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 17.9532 | 0.87431 | 32.046 |
| 2024-acf-fall-at-washington | 14 | 13 | 18.6412 | 0.887667 | 25.5803 |
| 2024-acf-nationals | 46 | 81 | 11.084 | 0.922289 | 22.7426 |
| 2024-acf-regionals-berkeley | 5 | 6 | 16.3486 | 0.7 | 35.23 |
| 2024-acf-regionals-cornell | 6 | 6 | 25.9485 | 0.637748 | 33.8218 |
| 2024-acf-regionals-imperial | 14 | 18 | 16.4659 | 0.842685 | 28.7816 |
| 2024-acf-regionals-jmu | 18 | 23 | 12.3707 | 0.931198 | 23.5106 |
| 2024-acf-regionals-minnesota | 3 | 4 | 7.77603 | 1 | 14.8691 |
| 2024-acf-regionals-mit | 5 | 3 | 27.1616 | 0.5 | 40.4578 |
| 2024-acf-regionals-nebraska | 12 | 14 | 14.4905 | 0.924695 | 21.4897 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 12.9926 | 0.964286 | 6.03865 |
| 2024-acf-regionals-rutgers | 11 | 12 | 16.6325 | 0.924832 | 33.2137 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 26.9322 | 0.782691 | 38.598 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 18.14 | 0.952941 | 28.9863 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 15.3674 | 0.977179 | 26.7102 |
| 2024-acf-winter-at-clemson | 16 | 17 | 15.0502 | 0.938235 | 23.6515 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 17.7401 | 0.955949 | 22.256 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 9.22612 | 0.975826 | 24.5582 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 13.4708 | 0.98405 | 20.0322 |
| 2024-acf-winter-at-online | 16 | 19 | 14.5763 | 0.899854 | 17.3083 |
| 2024-acf-winter-at-oxford | 19 | 21 | 15.0386 | 0.934096 | 26.2183 |
| 2024-acf-winter-at-ubc | 5 | 6 | 17.789 | 0.5 | 27.6384 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 31.7105 | 0.371429 | 45.3005 |

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
| bonus_part_correctness | aggregate | all | 25818 | 0.0169707 | 0.129197 | 0.896493 | 0.407851 |
| bonus_part_correctness | tier | fall | 8415 | 0.022329 | 0.131658 | 0.890732 | 0.409642 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0492689 | 0.127753 | 0.893969 | 0.411192 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0225528 | 0.129252 | 0.896352 | 0.409267 |
| bonus_part_correctness | tier | winter | 8154 | 0.0202212 | 0.127362 | 0.898226 | 0.403409 |
| bonus_part_correctness | category | Current Events | 258 | 0.0618776 | 0.108197 | 0.924399 | 0.361267 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0178154 | 0.136008 | 0.88628 | 0.426639 |
| bonus_part_correctness | category | Geography | 453 | 0.0517513 | 0.12818 | 0.892732 | 0.404021 |
| bonus_part_correctness | category | History | 4176 | 0.0151206 | 0.130311 | 0.894369 | 0.408826 |
| bonus_part_correctness | category | Literature | 4197 | 0.0322058 | 0.119889 | 0.91033 | 0.383152 |
| bonus_part_correctness | category | Mythology | 951 | 0.028873 | 0.136716 | 0.88094 | 0.423573 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0625524 | 0.114341 | 0.918921 | 0.372072 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0395448 | 0.137309 | 0.882468 | 0.430458 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.0971503 | 0.154261 | 0.860592 | 0.453255 |
| bonus_part_correctness | category | Religion | 1041 | 0.0346101 | 0.128651 | 0.896354 | 0.409751 |
| bonus_part_correctness | category | Science | 4152 | 0.022295 | 0.129135 | 0.895498 | 0.408796 |
| bonus_part_correctness | category | Social Science | 915 | 0.0326878 | 0.130417 | 0.892557 | 0.409052 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0225528 | 0.129252 | 0.896352 | 0.409267 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0420029 | 0.0763686 | 0.813222 | 0.26726 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0426815 | 0.115811 | 0.778194 | 0.378812 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0279341 | 0.195411 | 0.771718 | 0.57748 |
