# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 17.1442 |
| tournament_team_bonus_ppg_spearman | 0.909256 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.7458 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.898916 |
| log_loss | 0.402609 |
| ece | 0.0158132 |
| brier | 0.127714 |
| part_accuracy | 0.818488 |
| part_accuracy_easy | 0.903563 |
| part_accuracy_medium | 0.708551 |
| part_accuracy_hard | 0.843349 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.299485 |
| part_accuracy_macro_team | 0.821386 |
| part_accuracy_macro_bonus | 0.816022 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.350654 |
| probability_p10 | 0.0531449 |
| probability_p50 | 0.53576 |
| probability_p90 | 0.962572 |
| mean_predictive_variance | 0.126461 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.534323 |
| ranked_probability_score | 0.109609 |
| bonus_total_score_log_loss | 0.972613 |
| ppb_mae | 1.8542 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 17.6113 | 0.862291 | 26.9151 |
| 2024-acf-fall-at-cornell | 17 | 18 | 12.7375 | 0.947177 | 27.2929 |
| 2024-acf-fall-at-georgia | 21 | 23 | 14.2213 | 0.957765 | 23.5233 |
| 2024-acf-fall-at-illinois | 17 | 19 | 16.4962 | 0.889305 | 22.1381 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 15.6672 | 0.969541 | 28.1245 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 8.23941 | 0.975207 | 23.7689 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 14.585 | 0.946429 | 21.6866 |
| 2024-acf-fall-at-washington | 12 | 13 | 12.6463 | 0.903679 | 22.1121 |
| 2024-acf-nationals | 48 | 80 | 13.3974 | 0.942956 | 24.8269 |
| 2024-acf-regionals-berkeley | 6 | 7 | 14.7306 | 0.942857 | 24.2176 |
| 2024-acf-regionals-cornell | 6 | 6 | 30.7034 | 0.6 | 46.4657 |
| 2024-acf-regionals-imperial | 15 | 18 | 14.115 | 0.896429 | 28.2079 |
| 2024-acf-regionals-jmu | 19 | 23 | 14.3671 | 0.978499 | 26.3291 |
| 2024-acf-regionals-minnesota | 3 | 4 | 9.03067 | 0.5 | 14.2304 |
| 2024-acf-regionals-mit | 7 | 4 | 26.578 | 1 | 37.8746 |
| 2024-acf-regionals-nebraska | 11 | 13 | 23.2066 | 0.897497 | 41.0889 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 18.9036 | 1 | 18.8815 |
| 2024-acf-regionals-rutgers | 10 | 11 | 16.2244 | 0.975758 | 28.4153 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 27.1172 | 0.963636 | 43.5912 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 17.3861 | 0.944813 | 22.3873 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 15.4011 | 0.983333 | 11.8073 |
| 2024-acf-winter-at-clemson | 15 | 17 | 14.1525 | 0.963361 | 27.7761 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 12.0836 | 0.98487 | 21.7406 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 12.9309 | 0.965686 | 19.6445 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 16.3167 | 0.919678 | 29.3053 |
| 2024-acf-winter-at-online | 15 | 20 | 21.0252 | 0.910714 | 35.6938 |
| 2024-acf-winter-at-oxford | 17 | 19 | 14.6555 | 0.909203 | 28.9807 |
| 2024-acf-winter-at-ubc | 6 | 6 | 15.6648 | 1 | 18.8949 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 36.9881 | 0.637748 | 73.6817 |

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
| bonus_part_correctness | aggregate | all | 25260 | 0.0158132 | 0.127714 | 0.898916 | 0.402609 |
| bonus_part_correctness | tier | fall | 8160 | 0.0124622 | 0.127997 | 0.894216 | 0.401409 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0315455 | 0.124045 | 0.901267 | 0.394984 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0203368 | 0.132999 | 0.890948 | 0.41596 |
| bonus_part_correctness | tier | winter | 7713 | 0.0237788 | 0.12575 | 0.900817 | 0.398799 |
| bonus_part_correctness | category | Current Events | 249 | 0.0469863 | 0.126026 | 0.900568 | 0.406248 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0240411 | 0.136803 | 0.885071 | 0.427944 |
| bonus_part_correctness | category | Geography | 459 | 0.0357371 | 0.138492 | 0.875895 | 0.429632 |
| bonus_part_correctness | category | History | 4017 | 0.0231419 | 0.123367 | 0.905477 | 0.388359 |
| bonus_part_correctness | category | Literature | 4047 | 0.0192355 | 0.121132 | 0.906818 | 0.387231 |
| bonus_part_correctness | category | Mythology | 924 | 0.0394735 | 0.140615 | 0.874394 | 0.434289 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0645551 | 0.116921 | 0.918699 | 0.377499 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0274944 | 0.127271 | 0.898594 | 0.403126 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0552169 | 0.136335 | 0.874842 | 0.419222 |
| bonus_part_correctness | category | Religion | 984 | 0.0282666 | 0.124917 | 0.902879 | 0.397536 |
| bonus_part_correctness | category | Science | 3990 | 0.0195994 | 0.125753 | 0.901893 | 0.397472 |
| bonus_part_correctness | category | Social Science | 897 | 0.0318616 | 0.109992 | 0.920693 | 0.355934 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0203368 | 0.132999 | 0.890948 | 0.41596 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0200786 | 0.0748593 | 0.800329 | 0.260769 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0256213 | 0.116427 | 0.777605 | 0.378619 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.0367921 | 0.191857 | 0.780354 | 0.568438 |
