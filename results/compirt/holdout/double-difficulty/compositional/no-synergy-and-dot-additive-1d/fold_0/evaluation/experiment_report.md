# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.6444 |
| tournament_team_bonus_ppg_spearman | 0.785885 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 32.8154 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.891617 |
| log_loss | 0.416273 |
| ece | 0.0199448 |
| brier | 0.133061 |
| part_accuracy | 0.809706 |
| part_accuracy_easy | 0.903091 |
| part_accuracy_medium | 0.684174 |
| part_accuracy_hard | 0.841855 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.29127 |
| part_accuracy_macro_team | 0.810373 |
| part_accuracy_macro_bonus | 0.806954 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.344753 |
| probability_p10 | 0.0552828 |
| probability_p50 | 0.531983 |
| probability_p90 | 0.956119 |
| mean_predictive_variance | 0.13061 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.512782 |
| ranked_probability_score | 0.11694 |
| bonus_total_score_log_loss | 1.02218 |
| ppb_mae | 2.34778 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 9.37429 | 0.97072 | 38.2524 |
| 2024-acf-fall-at-cornell | 17 | 18 | 24.3516 | 0.855215 | 33.5767 |
| 2024-acf-fall-at-georgia | 24 | 25 | 21.3962 | 0.920767 | 41.383 |
| 2024-acf-fall-at-illinois | 19 | 22 | 21.4277 | 0.920037 | 34.5696 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 16.8601 | 0.941105 | 26.4582 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 17.9357 | 0.905745 | 28.393 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 19.5756 | 0.870632 | 35.6939 |
| 2024-acf-fall-at-washington | 14 | 13 | 20.275 | 0.845817 | 35.4355 |
| 2024-acf-nationals | 46 | 81 | 20.7093 | 0.802468 | 31.8098 |
| 2024-acf-regionals-berkeley | 5 | 6 | 32.7237 | 0.8 | 39.8729 |
| 2024-acf-regionals-cornell | 6 | 6 | 24.5636 | 0.637748 | 40.334 |
| 2024-acf-regionals-imperial | 14 | 18 | 22.1439 | 0.809681 | 39.4082 |
| 2024-acf-regionals-jmu | 18 | 23 | 20.1231 | 0.887742 | 28.7081 |
| 2024-acf-regionals-minnesota | 3 | 4 | 31.5548 | 0.5 | 52.9812 |
| 2024-acf-regionals-mit | 5 | 3 | 34.7617 | -0.9 | 40.0786 |
| 2024-acf-regionals-nebraska | 12 | 14 | 18.6992 | 0.921192 | 25.9222 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 16.0287 | 0.964286 | 12.1079 |
| 2024-acf-regionals-rutgers | 11 | 12 | 21.8512 | 0.943055 | 32.5027 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 30.1517 | 0.782691 | 28.8483 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 20.7249 | 0.95 | 30.8811 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 14.9456 | 0.940649 | 25.8121 |
| 2024-acf-winter-at-clemson | 16 | 17 | 18.3211 | 0.923529 | 31.1511 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 17.1851 | 0.949342 | 26.6568 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 19.5182 | 0.941056 | 44.4935 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 18.8193 | 0.946013 | 24.7726 |
| 2024-acf-winter-at-online | 16 | 19 | 16.2722 | 0.891017 | 26.8259 |
| 2024-acf-winter-at-oxford | 19 | 21 | 15.669 | 0.913007 | 27.8429 |
| 2024-acf-winter-at-ubc | 5 | 6 | 21.2709 | 0.7 | 38.4211 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 40.4551 | 0.257143 | 65.7052 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25818 | 0.0199448 | 0.133061 | 0.891617 | 0.416273 |
| bonus_part_correctness | tier | fall | 8415 | 0.0234598 | 0.134837 | 0.885944 | 0.416183 |
| bonus_part_correctness | tier | nationals | 4179 | 0.046777 | 0.132583 | 0.889444 | 0.418736 |
| bonus_part_correctness | tier | regionals | 5070 | 0.022188 | 0.133189 | 0.890994 | 0.417457 |
| bonus_part_correctness | tier | winter | 8154 | 0.0195535 | 0.131395 | 0.892659 | 0.414368 |
| bonus_part_correctness | category | Current Events | 258 | 0.0563754 | 0.100054 | 0.93119 | 0.340405 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0226493 | 0.141719 | 0.87771 | 0.440411 |
| bonus_part_correctness | category | Geography | 453 | 0.0495466 | 0.131134 | 0.890356 | 0.411219 |
| bonus_part_correctness | category | History | 4176 | 0.0271023 | 0.134932 | 0.889211 | 0.418218 |
| bonus_part_correctness | category | Literature | 4197 | 0.0266156 | 0.123234 | 0.905683 | 0.39 |
| bonus_part_correctness | category | Mythology | 951 | 0.0306091 | 0.142333 | 0.871195 | 0.435945 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0351681 | 0.117934 | 0.911367 | 0.379552 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0251637 | 0.14287 | 0.876068 | 0.442109 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.11002 | 0.153249 | 0.86161 | 0.446225 |
| bonus_part_correctness | category | Religion | 1041 | 0.0469883 | 0.130703 | 0.895534 | 0.414687 |
| bonus_part_correctness | category | Science | 4152 | 0.0213045 | 0.132301 | 0.891431 | 0.415491 |
| bonus_part_correctness | category | Social Science | 915 | 0.0339046 | 0.133749 | 0.88853 | 0.422111 |
| bonus_part_correctness | category | Unknown | 5070 | 0.022188 | 0.133189 | 0.890994 | 0.417457 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0215299 | 0.076038 | 0.801876 | 0.265002 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.034354 | 0.118454 | 0.764839 | 0.385188 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0424041 | 0.204692 | 0.750198 | 0.59863 |
