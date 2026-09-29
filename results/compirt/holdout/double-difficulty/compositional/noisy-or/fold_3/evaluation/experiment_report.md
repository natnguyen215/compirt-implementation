# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.1427 |
| tournament_team_bonus_ppg_spearman | 0.89197 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.7186 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.889827 |
| log_loss | 0.418368 |
| ece | 0.0167815 |
| brier | 0.133981 |
| part_accuracy | 0.807688 |
| part_accuracy_easy | 0.908811 |
| part_accuracy_medium | 0.674749 |
| part_accuracy_hard | 0.839503 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.282003 |
| part_accuracy_macro_team | 0.81103 |
| part_accuracy_macro_bonus | 0.807935 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.355041 |
| probability_p10 | 0.0569743 |
| probability_p50 | 0.515673 |
| probability_p90 | 0.987141 |
| mean_predictive_variance | 0.123279 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.511532 |
| ranked_probability_score | 0.119409 |
| bonus_total_score_log_loss | 1.04581 |
| ppb_mae | 2.33968 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 12.9463 | 0.966667 | 21.5376 |
| 2024-acf-fall-at-cornell | 16 | 18 | 17.3933 | 0.852097 | 36.0087 |
| 2024-acf-fall-at-georgia | 22 | 26 | 21.0926 | 0.947697 | 33.3174 |
| 2024-acf-fall-at-illinois | 16 | 15 | 14.6475 | 0.896908 | 24.4295 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 21.7854 | 0.880982 | 45.2241 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 19.0974 | 0.989268 | 31.9732 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 25.9668 | 0.813226 | 44.8054 |
| 2024-acf-fall-at-washington | 12 | 13 | 24.6441 | 0.678322 | 41.8202 |
| 2024-acf-nationals | 46 | 79 | 19.6395 | 0.789782 | 32.1447 |
| 2024-acf-regionals-berkeley | 6 | 5 | 21.347 | 0.927634 | 33.4577 |
| 2024-acf-regionals-cornell | 5 | 6 | 19.496 | 0.9 | 18.8801 |
| 2024-acf-regionals-imperial | 15 | 17 | 20.9034 | 0.886506 | 33.7329 |
| 2024-acf-regionals-jmu | 19 | 25 | 21.143 | 0.91396 | 28.8136 |
| 2024-acf-regionals-minnesota | 3 | 4 | 33.2886 | 1 | 56.1971 |
| 2024-acf-regionals-mit | 4 | 2 | 23.0247 | 0.8 | 21.6708 |
| 2024-acf-regionals-nebraska | 11 | 13 | 24.4011 | 0.824604 | 40.9304 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 13.0421 | 1 | 27.1465 |
| 2024-acf-regionals-rutgers | 11 | 11 | 30.5011 | 0.769934 | 32.8194 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 9.88879 | 1 | 20.3983 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 22.4776 | 0.966872 | 25.9552 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 23.1481 | 1 | 36.8633 |
| 2024-acf-winter-at-clemson | 16 | 17 | 19.4163 | 0.908021 | 28.149 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 20.3326 | 0.981299 | 38.852 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 17.7989 | 0.927153 | 39.1226 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 25.3609 | 0.938126 | 37.4791 |
| 2024-acf-winter-at-online | 17 | 19 | 20.4321 | 0.898835 | 32.337 |
| 2024-acf-winter-at-oxford | 17 | 19 | 20.6706 | 0.823529 | 29.0497 |
| 2024-acf-winter-at-ubc | 5 | 6 | 19.4821 | 0.7 | 46.5734 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 29.77 | 0.885714 | 40.9635 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25365 | 0.0167815 | 0.133981 | 0.889827 | 0.418368 |
| bonus_part_correctness | tier | fall | 8094 | 0.0184777 | 0.136917 | 0.882977 | 0.421963 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0204912 | 0.137658 | 0.879696 | 0.435302 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0297644 | 0.13469 | 0.889414 | 0.420654 |
| bonus_part_correctness | tier | winter | 7899 | 0.0139743 | 0.12858 | 0.897475 | 0.404322 |
| bonus_part_correctness | category | Current Events | 243 | 0.0577588 | 0.129733 | 0.89397 | 0.415313 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0242847 | 0.145958 | 0.869969 | 0.452612 |
| bonus_part_correctness | category | Geography | 456 | 0.0371238 | 0.131228 | 0.890149 | 0.404875 |
| bonus_part_correctness | category | History | 4050 | 0.0184368 | 0.130629 | 0.894338 | 0.40808 |
| bonus_part_correctness | category | Literature | 4029 | 0.0210652 | 0.132986 | 0.891399 | 0.414054 |
| bonus_part_correctness | category | Mythology | 936 | 0.0352451 | 0.12865 | 0.894203 | 0.396049 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0551412 | 0.10475 | 0.9226 | 0.356431 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0471255 | 0.149895 | 0.864524 | 0.456691 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0673045 | 0.133295 | 0.89202 | 0.408872 |
| bonus_part_correctness | category | Religion | 1014 | 0.0272721 | 0.128531 | 0.896869 | 0.411039 |
| bonus_part_correctness | category | Science | 4059 | 0.0178683 | 0.133437 | 0.889725 | 0.420766 |
| bonus_part_correctness | category | Social Science | 906 | 0.0303662 | 0.118805 | 0.911853 | 0.367734 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0297644 | 0.13469 | 0.889414 | 0.420654 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.0232835 | 0.0716716 | 0.798993 | 0.251275 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0290584 | 0.120589 | 0.748814 | 0.393229 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0467652 | 0.209681 | 0.738458 | 0.6106 |
