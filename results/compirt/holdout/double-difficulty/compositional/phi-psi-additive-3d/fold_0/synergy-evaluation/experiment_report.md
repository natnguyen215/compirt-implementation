# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.7957 |
| tournament_team_bonus_ppg_spearman | 0.85538 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.3458 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.898042 |
| log_loss | 0.404756 |
| ece | 0.0181585 |
| brier | 0.128623 |
| part_accuracy | 0.817375 |
| part_accuracy_easy | 0.903788 |
| part_accuracy_medium | 0.701952 |
| part_accuracy_hard | 0.846386 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.298939 |
| part_accuracy_macro_team | 0.817985 |
| part_accuracy_macro_bonus | 0.815607 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.352888 |
| probability_p10 | 0.051405 |
| probability_p50 | 0.542251 |
| probability_p90 | 0.965477 |
| mean_predictive_variance | 0.124754 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.529747 |
| ranked_probability_score | 0.111846 |
| bonus_total_score_log_loss | 0.989323 |
| ppb_mae | 1.85926 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 12.7559 | 0.97072 | 39.1886 |
| 2024-acf-fall-at-cornell | 17 | 18 | 18.3618 | 0.925154 | 22.1311 |
| 2024-acf-fall-at-georgia | 24 | 25 | 14.9937 | 0.946453 | 29.4173 |
| 2024-acf-fall-at-illinois | 19 | 22 | 17.7098 | 0.936733 | 28.3797 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 16.1187 | 0.949694 | 26.2165 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 12.0726 | 0.979383 | 19.9372 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 19.2978 | 0.851012 | 37.0204 |
| 2024-acf-fall-at-washington | 14 | 13 | 15.8382 | 0.92291 | 15.9736 |
| 2024-acf-nationals | 46 | 81 | 12.7004 | 0.910628 | 25.0266 |
| 2024-acf-regionals-berkeley | 5 | 6 | 13.1158 | 0.9 | 24.8895 |
| 2024-acf-regionals-cornell | 6 | 6 | 23.9843 | 0.637748 | 34.4555 |
| 2024-acf-regionals-imperial | 14 | 18 | 19.4141 | 0.825083 | 42.5836 |
| 2024-acf-regionals-jmu | 18 | 23 | 15.936 | 0.887742 | 25.0693 |
| 2024-acf-regionals-minnesota | 3 | 4 | 14.311 | 1 | 29.811 |
| 2024-acf-regionals-mit | 5 | 3 | 24.0505 | 0 | 28.7993 |
| 2024-acf-regionals-nebraska | 12 | 14 | 15.9628 | 0.942208 | 23.6052 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 18.8417 | 0.964286 | 9.37534 |
| 2024-acf-regionals-rutgers | 11 | 12 | 15.1371 | 0.91572 | 29.9035 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 29.2404 | 0.782691 | 33.0391 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 16.7755 | 0.944118 | 24.3467 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 12.4355 | 0.940649 | 26.3823 |
| 2024-acf-winter-at-clemson | 16 | 17 | 14.8343 | 0.926471 | 25.6138 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 13.2294 | 0.975773 | 19.4243 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 9.57818 | 0.970535 | 24.1309 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 13.6509 | 0.95951 | 24.3581 |
| 2024-acf-winter-at-online | 16 | 19 | 16.4548 | 0.938145 | 20.5986 |
| 2024-acf-winter-at-oxford | 19 | 21 | 13.7307 | 0.94552 | 23.5481 |
| 2024-acf-winter-at-ubc | 5 | 6 | 11.0271 | 0.7 | 21.3651 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 35.5173 | 0.257143 | 49.8302 |

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
| bonus_part_correctness | aggregate | all | 25818 | 0.0181585 | 0.128623 | 0.898042 | 0.404756 |
| bonus_part_correctness | tier | fall | 8415 | 0.0224166 | 0.132098 | 0.890411 | 0.409625 |
| bonus_part_correctness | tier | nationals | 4179 | 0.032866 | 0.125778 | 0.897585 | 0.40099 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0170764 | 0.12881 | 0.897521 | 0.404603 |
| bonus_part_correctness | tier | winter | 8154 | 0.0197277 | 0.126379 | 0.900008 | 0.401755 |
| bonus_part_correctness | category | Current Events | 258 | 0.0471638 | 0.104842 | 0.92476 | 0.351112 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0189967 | 0.135985 | 0.885913 | 0.428006 |
| bonus_part_correctness | category | Geography | 453 | 0.0397143 | 0.130796 | 0.889686 | 0.414059 |
| bonus_part_correctness | category | History | 4176 | 0.024651 | 0.129239 | 0.897138 | 0.404402 |
| bonus_part_correctness | category | Literature | 4197 | 0.0244904 | 0.119422 | 0.911119 | 0.378895 |
| bonus_part_correctness | category | Mythology | 951 | 0.0332781 | 0.136525 | 0.882143 | 0.421498 |
| bonus_part_correctness | category | Other Academic | 258 | 0.040473 | 0.106301 | 0.930373 | 0.346991 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0260564 | 0.135185 | 0.885544 | 0.425165 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.101326 | 0.154699 | 0.862673 | 0.45179 |
| bonus_part_correctness | category | Religion | 1041 | 0.0305207 | 0.129867 | 0.89762 | 0.409536 |
| bonus_part_correctness | category | Science | 4152 | 0.0192143 | 0.129256 | 0.89594 | 0.408167 |
| bonus_part_correctness | category | Social Science | 915 | 0.0318967 | 0.126083 | 0.900624 | 0.399002 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0170764 | 0.12881 | 0.897521 | 0.404603 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0128297 | 0.0748038 | 0.810792 | 0.259249 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0298571 | 0.114295 | 0.782211 | 0.373941 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0404478 | 0.196771 | 0.770299 | 0.581078 |
