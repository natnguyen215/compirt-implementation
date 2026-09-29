# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.672 |
| tournament_team_bonus_ppg_spearman | 0.807835 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.026 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.890968 |
| log_loss | 0.417161 |
| ece | 0.0157673 |
| brier | 0.133461 |
| part_accuracy | 0.809474 |
| part_accuracy_easy | 0.903323 |
| part_accuracy_medium | 0.685103 |
| part_accuracy_hard | 0.839995 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.291037 |
| part_accuracy_macro_team | 0.810099 |
| part_accuracy_macro_bonus | 0.806393 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.350555 |
| probability_p10 | 0.0497687 |
| probability_p50 | 0.522473 |
| probability_p90 | 0.967472 |
| mean_predictive_variance | 0.126635 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.511852 |
| ranked_probability_score | 0.11729 |
| bonus_total_score_log_loss | 1.02719 |
| ppb_mae | 2.32639 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 7.52577 | 0.995825 | 35.5236 |
| 2024-acf-fall-at-cornell | 17 | 18 | 24.5933 | 0.868712 | 33.4411 |
| 2024-acf-fall-at-georgia | 24 | 25 | 21.8302 | 0.914237 | 43.0273 |
| 2024-acf-fall-at-illinois | 19 | 22 | 20.9287 | 0.915643 | 34.7375 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 16.8648 | 0.941105 | 25.8756 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 17.6554 | 0.913109 | 28.4219 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 19.3577 | 0.852238 | 36.8771 |
| 2024-acf-fall-at-washington | 14 | 13 | 20.7977 | 0.845817 | 35.8668 |
| 2024-acf-nationals | 46 | 81 | 20.0345 | 0.816104 | 31.5235 |
| 2024-acf-regionals-berkeley | 5 | 6 | 35.0119 | 0.8 | 43.1744 |
| 2024-acf-regionals-cornell | 6 | 6 | 25.1209 | 0.579771 | 40.9226 |
| 2024-acf-regionals-imperial | 14 | 18 | 22.2552 | 0.866887 | 39.9817 |
| 2024-acf-regionals-jmu | 18 | 23 | 19.3014 | 0.887742 | 28.9209 |
| 2024-acf-regionals-minnesota | 3 | 4 | 31.3544 | 1 | 51.626 |
| 2024-acf-regionals-mit | 5 | 3 | 35.8124 | -0.8 | 37.9745 |
| 2024-acf-regionals-nebraska | 12 | 14 | 18.4844 | 0.921192 | 27.6851 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 14.3034 | 0.964286 | 13.2617 |
| 2024-acf-regionals-rutgers | 11 | 12 | 23.8709 | 0.943055 | 35.2957 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 31.2351 | 0.782691 | 29.4368 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 20.6777 | 0.95 | 31.0664 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 14.153 | 0.940649 | 24.3961 |
| 2024-acf-winter-at-clemson | 16 | 17 | 17.9823 | 0.926471 | 30.809 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 16.5295 | 0.938328 | 26.057 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 20.4352 | 0.941056 | 45.5048 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 18.376 | 0.949694 | 23.6688 |
| 2024-acf-winter-at-online | 16 | 19 | 16.144 | 0.891017 | 26.3883 |
| 2024-acf-winter-at-oxford | 19 | 21 | 15.8594 | 0.92443 | 29.0171 |
| 2024-acf-winter-at-ubc | 5 | 6 | 21.8027 | 0.7 | 39.6877 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 40.189 | 0.257143 | 64.4188 |

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
| bonus_part_correctness | aggregate | all | 25818 | 0.0157673 | 0.133461 | 0.890968 | 0.417161 |
| bonus_part_correctness | tier | fall | 8415 | 0.0211142 | 0.135874 | 0.884016 | 0.418274 |
| bonus_part_correctness | tier | nationals | 4179 | 0.033992 | 0.131547 | 0.890036 | 0.415349 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0208593 | 0.133907 | 0.889826 | 0.420766 |
| bonus_part_correctness | tier | winter | 8154 | 0.0208886 | 0.131676 | 0.892676 | 0.414699 |
| bonus_part_correctness | category | Current Events | 258 | 0.056368 | 0.0992395 | 0.932933 | 0.336722 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0252993 | 0.14258 | 0.876462 | 0.443404 |
| bonus_part_correctness | category | Geography | 453 | 0.0434465 | 0.132613 | 0.887045 | 0.420712 |
| bonus_part_correctness | category | History | 4176 | 0.0226831 | 0.135119 | 0.889056 | 0.416936 |
| bonus_part_correctness | category | Literature | 4197 | 0.0183224 | 0.122599 | 0.906997 | 0.385141 |
| bonus_part_correctness | category | Mythology | 951 | 0.0377387 | 0.143038 | 0.87094 | 0.438086 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0435 | 0.118935 | 0.914352 | 0.378786 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0347434 | 0.142116 | 0.876409 | 0.44212 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.0746119 | 0.151562 | 0.860962 | 0.44374 |
| bonus_part_correctness | category | Religion | 1041 | 0.0404805 | 0.131032 | 0.893633 | 0.417873 |
| bonus_part_correctness | category | Science | 4152 | 0.0227276 | 0.133296 | 0.8898 | 0.418802 |
| bonus_part_correctness | category | Social Science | 915 | 0.0323587 | 0.135172 | 0.887861 | 0.4234 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0208593 | 0.133907 | 0.889826 | 0.420766 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.018828 | 0.0775145 | 0.789159 | 0.269729 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0253393 | 0.11778 | 0.772524 | 0.38176 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0490523 | 0.20509 | 0.749917 | 0.599994 |
