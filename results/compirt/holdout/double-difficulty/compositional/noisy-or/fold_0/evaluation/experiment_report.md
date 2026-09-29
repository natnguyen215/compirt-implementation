# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.5945 |
| tournament_team_bonus_ppg_spearman | 0.779162 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.1365 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.892051 |
| log_loss | 0.415293 |
| ece | 0.0170399 |
| brier | 0.132712 |
| part_accuracy | 0.808622 |
| part_accuracy_easy | 0.900999 |
| part_accuracy_medium | 0.684987 |
| part_accuracy_hard | 0.839879 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.290185 |
| part_accuracy_macro_team | 0.809913 |
| part_accuracy_macro_bonus | 0.807338 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.358019 |
| probability_p10 | 0.0521843 |
| probability_p50 | 0.504114 |
| probability_p90 | 0.986464 |
| mean_predictive_variance | 0.121418 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.509993 |
| ranked_probability_score | 0.116968 |
| bonus_total_score_log_loss | 1.02695 |
| ppb_mae | 2.31543 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 7.35731 | 0.97072 | 36.2823 |
| 2024-acf-fall-at-cornell | 17 | 18 | 24.4938 | 0.857669 | 33.2947 |
| 2024-acf-fall-at-georgia | 24 | 25 | 21.3156 | 0.912495 | 43.2955 |
| 2024-acf-fall-at-illinois | 19 | 22 | 21.3499 | 0.902462 | 34.39 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 17.0315 | 0.937424 | 25.8798 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 18.072 | 0.905745 | 27.1528 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 19.5674 | 0.870632 | 36.5728 |
| 2024-acf-fall-at-washington | 14 | 13 | 20.7941 | 0.845817 | 36.1503 |
| 2024-acf-nationals | 46 | 81 | 20.8099 | 0.795496 | 32.6617 |
| 2024-acf-regionals-berkeley | 5 | 6 | 33.5528 | 0.8 | 41.4144 |
| 2024-acf-regionals-cornell | 6 | 6 | 23.9079 | 0.579771 | 39.2315 |
| 2024-acf-regionals-imperial | 14 | 18 | 22.0931 | 0.805281 | 38.6231 |
| 2024-acf-regionals-jmu | 18 | 23 | 19.3355 | 0.887742 | 29.2461 |
| 2024-acf-regionals-minnesota | 3 | 4 | 34.5707 | 0.5 | 56.3699 |
| 2024-acf-regionals-mit | 5 | 3 | 37.1749 | -0.9 | 41.7425 |
| 2024-acf-regionals-nebraska | 12 | 14 | 17.9605 | 0.921192 | 26.9512 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 14.2187 | 0.964286 | 12.2854 |
| 2024-acf-regionals-rutgers | 11 | 12 | 22.199 | 0.943055 | 33.1161 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 30.0608 | 0.782691 | 31.5514 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 19.7444 | 0.95 | 28.9797 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 14.1655 | 0.940649 | 26.3175 |
| 2024-acf-winter-at-clemson | 16 | 17 | 17.9285 | 0.923529 | 32.1576 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 16.5413 | 0.938328 | 26.6236 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 19.8947 | 0.941056 | 45.9976 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 18.0755 | 0.949694 | 24.3871 |
| 2024-acf-winter-at-online | 16 | 19 | 15.6896 | 0.891017 | 25.5679 |
| 2024-acf-winter-at-oxford | 19 | 21 | 15.9243 | 0.921794 | 28.8334 |
| 2024-acf-winter-at-ubc | 5 | 6 | 21.5413 | 0.6 | 39.6799 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 40.8704 | 0.257143 | 65.5487 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25818 | 0.0170399 | 0.132712 | 0.892051 | 0.415293 |
| bonus_part_correctness | tier | fall | 8415 | 0.0218579 | 0.135437 | 0.885042 | 0.416583 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0362814 | 0.131786 | 0.887709 | 0.418633 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0248989 | 0.132384 | 0.893085 | 0.414347 |
| bonus_part_correctness | tier | winter | 8154 | 0.017931 | 0.130579 | 0.894084 | 0.412838 |
| bonus_part_correctness | category | Current Events | 258 | 0.0502387 | 0.0975676 | 0.932813 | 0.333354 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0274915 | 0.141654 | 0.877699 | 0.442301 |
| bonus_part_correctness | category | Geography | 453 | 0.0445081 | 0.131879 | 0.888934 | 0.41317 |
| bonus_part_correctness | category | History | 4176 | 0.0300907 | 0.134953 | 0.888828 | 0.418684 |
| bonus_part_correctness | category | Literature | 4197 | 0.0149258 | 0.122369 | 0.905846 | 0.385723 |
| bonus_part_correctness | category | Mythology | 951 | 0.0289099 | 0.14287 | 0.870638 | 0.439998 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0585249 | 0.121328 | 0.909539 | 0.385186 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0317323 | 0.142683 | 0.875497 | 0.442029 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.062576 | 0.15363 | 0.856892 | 0.442301 |
| bonus_part_correctness | category | Religion | 1041 | 0.0297888 | 0.130971 | 0.893994 | 0.41372 |
| bonus_part_correctness | category | Science | 4152 | 0.0211563 | 0.131636 | 0.892752 | 0.41478 |
| bonus_part_correctness | category | Social Science | 915 | 0.0447702 | 0.134042 | 0.889429 | 0.423758 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0248989 | 0.132384 | 0.893085 | 0.414347 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0179006 | 0.0761237 | 0.805319 | 0.265173 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0232227 | 0.117747 | 0.766495 | 0.382802 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0423727 | 0.204265 | 0.751766 | 0.597904 |
