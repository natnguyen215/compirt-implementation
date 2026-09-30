# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.6289 |
| tournament_team_bonus_ppg_spearman | 0.799129 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 32.8745 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.891429 |
| log_loss | 0.416012 |
| ece | 0.0136348 |
| brier | 0.132993 |
| part_accuracy | 0.809358 |
| part_accuracy_easy | 0.902858 |
| part_accuracy_medium | 0.684522 |
| part_accuracy_hard | 0.840693 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.290921 |
| part_accuracy_macro_team | 0.80979 |
| part_accuracy_macro_bonus | 0.806618 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.345093 |
| probability_p10 | 0.0552151 |
| probability_p50 | 0.528652 |
| probability_p90 | 0.958717 |
| mean_predictive_variance | 0.130428 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.511271 |
| ranked_probability_score | 0.11686 |
| bonus_total_score_log_loss | 1.02113 |
| ppb_mae | 2.33475 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 9.25835 | 0.97072 | 37.9608 |
| 2024-acf-fall-at-cornell | 17 | 18 | 24.6619 | 0.855215 | 33.7885 |
| 2024-acf-fall-at-georgia | 24 | 25 | 21.7311 | 0.915978 | 41.5397 |
| 2024-acf-fall-at-illinois | 19 | 22 | 21.2277 | 0.905977 | 34.8433 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 16.6731 | 0.941105 | 26.3482 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 18.0087 | 0.913109 | 28.9056 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 18.6617 | 0.870632 | 36.1923 |
| 2024-acf-fall-at-washington | 14 | 13 | 20.4362 | 0.845817 | 35.4569 |
| 2024-acf-nationals | 46 | 81 | 19.991 | 0.813389 | 31.1363 |
| 2024-acf-regionals-berkeley | 5 | 6 | 34.5692 | 0.8 | 42.7387 |
| 2024-acf-regionals-cornell | 6 | 6 | 25.0819 | 0.579771 | 41.3541 |
| 2024-acf-regionals-imperial | 14 | 18 | 22.318 | 0.833884 | 39.3512 |
| 2024-acf-regionals-jmu | 18 | 23 | 19.6012 | 0.875326 | 28.7218 |
| 2024-acf-regionals-minnesota | 3 | 4 | 30.2397 | 1 | 47.6677 |
| 2024-acf-regionals-mit | 5 | 3 | 35.188 | -1 | 41.4174 |
| 2024-acf-regionals-nebraska | 12 | 14 | 18.7576 | 0.928198 | 27.5767 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 15.0603 | 0.964286 | 13.2357 |
| 2024-acf-regionals-rutgers | 11 | 12 | 23.253 | 0.943055 | 34.3174 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 29.7538 | 0.782691 | 27.7148 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 21.1503 | 0.952941 | 31.3467 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 14.8868 | 0.949782 | 25.6959 |
| 2024-acf-winter-at-clemson | 16 | 17 | 17.9894 | 0.935294 | 30.5289 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 16.9126 | 0.949342 | 27.1619 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 20.1026 | 0.941056 | 45.0127 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 18.3361 | 0.946013 | 24.3309 |
| 2024-acf-winter-at-online | 16 | 19 | 16.3565 | 0.891017 | 26.4905 |
| 2024-acf-winter-at-oxford | 19 | 21 | 15.6694 | 0.913007 | 28.3619 |
| 2024-acf-winter-at-ubc | 5 | 6 | 21.1587 | 0.7 | 38.8305 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 40.2031 | 0.257143 | 64.2208 |

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
| bonus_part_correctness | aggregate | all | 25818 | 0.0136348 | 0.132993 | 0.891429 | 0.416012 |
| bonus_part_correctness | tier | fall | 8415 | 0.0189133 | 0.135458 | 0.884644 | 0.417738 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0347232 | 0.1317 | 0.889859 | 0.416143 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0166116 | 0.132984 | 0.891108 | 0.417241 |
| bonus_part_correctness | tier | winter | 8154 | 0.0160809 | 0.131118 | 0.893025 | 0.413399 |
| bonus_part_correctness | category | Current Events | 258 | 0.0595273 | 0.100177 | 0.932752 | 0.33762 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0234776 | 0.141849 | 0.877364 | 0.441073 |
| bonus_part_correctness | category | Geography | 453 | 0.0417204 | 0.131293 | 0.889584 | 0.413539 |
| bonus_part_correctness | category | History | 4176 | 0.020788 | 0.134477 | 0.889539 | 0.416349 |
| bonus_part_correctness | category | Literature | 4197 | 0.0217966 | 0.122768 | 0.906586 | 0.387693 |
| bonus_part_correctness | category | Mythology | 951 | 0.0272074 | 0.143519 | 0.869649 | 0.439965 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0440961 | 0.121109 | 0.908687 | 0.38956 |
| bonus_part_correctness | category | Philosophy | 969 | 0.036986 | 0.143316 | 0.873576 | 0.446133 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.0738281 | 0.155181 | 0.855689 | 0.453467 |
| bonus_part_correctness | category | Religion | 1041 | 0.0344222 | 0.130825 | 0.89522 | 0.413899 |
| bonus_part_correctness | category | Science | 4152 | 0.0137519 | 0.132228 | 0.891098 | 0.415522 |
| bonus_part_correctness | category | Social Science | 915 | 0.0307508 | 0.133575 | 0.889826 | 0.419554 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0166116 | 0.132984 | 0.891108 | 0.417241 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0217306 | 0.0770667 | 0.789639 | 0.268977 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0299363 | 0.117797 | 0.770769 | 0.381654 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0392513 | 0.204116 | 0.751245 | 0.597404 |
