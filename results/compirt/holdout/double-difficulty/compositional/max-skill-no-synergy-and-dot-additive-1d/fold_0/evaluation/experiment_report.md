# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.5712 |
| tournament_team_bonus_ppg_spearman | 0.823915 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 34.1219 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.888926 |
| log_loss | 0.420794 |
| ece | 0.0111228 |
| brier | 0.134329 |
| part_accuracy | 0.809668 |
| part_accuracy_easy | 0.899024 |
| part_accuracy_medium | 0.690913 |
| part_accuracy_hard | 0.839066 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.291231 |
| part_accuracy_macro_team | 0.810769 |
| part_accuracy_macro_bonus | 0.804274 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.331373 |
| probability_p10 | 0.0722383 |
| probability_p50 | 0.513031 |
| probability_p90 | 0.939415 |
| mean_predictive_variance | 0.140005 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.513828 |
| ranked_probability_score | 0.117315 |
| bonus_total_score_log_loss | 1.02409 |
| ppb_mae | 2.35471 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 15.2555 | 0.962352 | 21.6207 |
| 2024-acf-fall-at-cornell | 17 | 18 | 19.5591 | 0.899387 | 36.2823 |
| 2024-acf-fall-at-georgia | 24 | 25 | 23.4722 | 0.906836 | 50.1591 |
| 2024-acf-fall-at-illinois | 19 | 22 | 22.2263 | 0.8761 | 35.3823 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 19.9367 | 0.954602 | 44.0005 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 16.9594 | 0.954346 | 26.7932 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 25.6202 | 0.837523 | 40.1728 |
| 2024-acf-fall-at-washington | 14 | 13 | 21.4348 | 0.817183 | 36.9313 |
| 2024-acf-nationals | 46 | 81 | 23.0468 | 0.76625 | 35.8808 |
| 2024-acf-regionals-berkeley | 5 | 6 | 34.0543 | 0.8 | 40.3467 |
| 2024-acf-regionals-cornell | 6 | 6 | 26.5994 | 0.579771 | 46.3001 |
| 2024-acf-regionals-imperial | 14 | 18 | 23.5563 | 0.770077 | 37.102 |
| 2024-acf-regionals-jmu | 18 | 23 | 18.8367 | 0.883604 | 30.3981 |
| 2024-acf-regionals-minnesota | 3 | 4 | 36.7336 | 1 | 43.3103 |
| 2024-acf-regionals-mit | 5 | 3 | 38.0379 | 0.3 | 34.1476 |
| 2024-acf-regionals-nebraska | 12 | 14 | 15.4566 | 0.942208 | 26.6354 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 21.267 | 0.964286 | 23.2997 |
| 2024-acf-regionals-rutgers | 11 | 12 | 15.4085 | 0.938499 | 29.0723 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 26.1044 | 0.927634 | 33.1019 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 21.0431 | 0.95 | 33.1227 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 16.9079 | 0.981745 | 31.3366 |
| 2024-acf-winter-at-clemson | 16 | 17 | 15.4344 | 0.95 | 28.7894 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 15.6266 | 0.892073 | 25.3436 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 13.3494 | 0.960709 | 28.2815 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 21.4618 | 0.926381 | 31.1804 |
| 2024-acf-winter-at-online | 16 | 19 | 20.2588 | 0.830634 | 31.3133 |
| 2024-acf-winter-at-oxford | 19 | 21 | 15.4134 | 0.949914 | 19.4677 |
| 2024-acf-winter-at-ubc | 5 | 6 | 39.8662 | 0 | 53.1088 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 31.6376 | 0.371429 | 42.5264 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25818 | 0.0111228 | 0.134329 | 0.888926 | 0.420794 |
| bonus_part_correctness | tier | fall | 8415 | 0.0160132 | 0.137073 | 0.881374 | 0.424777 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0277221 | 0.136931 | 0.880232 | 0.430685 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0246706 | 0.133756 | 0.889745 | 0.421002 |
| bonus_part_correctness | tier | winter | 8154 | 0.015712 | 0.130522 | 0.89371 | 0.411485 |
| bonus_part_correctness | category | Current Events | 258 | 0.0573207 | 0.108293 | 0.926022 | 0.354805 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0169858 | 0.142813 | 0.875785 | 0.442808 |
| bonus_part_correctness | category | Geography | 453 | 0.0456565 | 0.134288 | 0.881398 | 0.422932 |
| bonus_part_correctness | category | History | 4176 | 0.0225499 | 0.135364 | 0.886646 | 0.421542 |
| bonus_part_correctness | category | Literature | 4197 | 0.027962 | 0.123198 | 0.905354 | 0.391222 |
| bonus_part_correctness | category | Mythology | 951 | 0.034285 | 0.146278 | 0.86353 | 0.44974 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0460031 | 0.135875 | 0.885173 | 0.431174 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0251307 | 0.146235 | 0.868936 | 0.452376 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.0574661 | 0.151224 | 0.858187 | 0.449596 |
| bonus_part_correctness | category | Religion | 1041 | 0.0341594 | 0.132161 | 0.891303 | 0.420364 |
| bonus_part_correctness | category | Science | 4152 | 0.0150523 | 0.133558 | 0.889359 | 0.41851 |
| bonus_part_correctness | category | Social Science | 915 | 0.0262131 | 0.137608 | 0.881735 | 0.430302 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0246706 | 0.133756 | 0.889745 | 0.421002 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0521795 | 0.0801817 | 0.789357 | 0.280595 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0376307 | 0.11945 | 0.765727 | 0.385833 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0339599 | 0.203356 | 0.752396 | 0.595955 |
