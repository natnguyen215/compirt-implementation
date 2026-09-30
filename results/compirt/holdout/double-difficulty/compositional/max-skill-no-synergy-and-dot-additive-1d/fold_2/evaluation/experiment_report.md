# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 23.0971 |
| tournament_team_bonus_ppg_spearman | 0.833025 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 35.8592 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.886653 |
| log_loss | 0.425338 |
| ece | 0.0167845 |
| brier | 0.135893 |
| part_accuracy | 0.806832 |
| part_accuracy_easy | 0.89601 |
| part_accuracy_medium | 0.682796 |
| part_accuracy_hard | 0.841689 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.287465 |
| part_accuracy_macro_team | 0.811302 |
| part_accuracy_macro_bonus | 0.803297 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.33134 |
| probability_p10 | 0.0669523 |
| probability_p50 | 0.490573 |
| probability_p90 | 0.935479 |
| mean_predictive_variance | 0.140206 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.507619 |
| ranked_probability_score | 0.118031 |
| bonus_total_score_log_loss | 1.03064 |
| ppb_mae | 2.40396 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 27.3227 | 0.785714 | 40.052 |
| 2024-acf-fall-at-cornell | 17 | 18 | 23.7642 | 0.865031 | 34.6551 |
| 2024-acf-fall-at-georgia | 22 | 24 | 22.5656 | 0.886313 | 42.4306 |
| 2024-acf-fall-at-illinois | 19 | 21 | 20.0958 | 0.95614 | 28.9073 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.4548 | 0.960784 | 23.286 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 21.9818 | 0.972638 | 27.7558 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 19.9238 | 0.913109 | 20.6504 |
| 2024-acf-fall-at-washington | 13 | 12 | 32.8444 | 0.802198 | 39.8358 |
| 2024-acf-nationals | 47 | 79 | 23.8223 | 0.804118 | 39.5761 |
| 2024-acf-regionals-berkeley | 5 | 6 | 30.3928 | 0.718185 | 50.348 |
| 2024-acf-regionals-cornell | 4 | 7 | 22.6232 | 0.4 | 33.9278 |
| 2024-acf-regionals-imperial | 15 | 18 | 23.8263 | 0.902592 | 37.2521 |
| 2024-acf-regionals-jmu | 18 | 24 | 21.8006 | 0.920455 | 37.9843 |
| 2024-acf-regionals-minnesota | 4 | 4 | 21.2371 | 0.8 | 47.637 |
| 2024-acf-regionals-mit | 6 | 4 | 24.6041 | 0.942857 | 47.5052 |
| 2024-acf-regionals-nebraska | 12 | 13 | 10.4017 | 0.949213 | 19.4623 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 24.1013 | 0.828571 | 47.3637 |
| 2024-acf-regionals-rutgers | 11 | 11 | 27.6357 | 0.954545 | 37.1345 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 17.5963 | 0.890909 | 40.2728 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 25.6937 | 0.904852 | 39.8718 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 25.5918 | 0.916667 | 39.1267 |
| 2024-acf-winter-at-clemson | 18 | 17 | 19.2982 | 0.907025 | 34.9435 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 19.36 | 0.929518 | 33.1742 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 14.7823 | 0.959007 | 24.0437 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 28.6471 | 0.882181 | 41.1997 |
| 2024-acf-winter-at-online | 18 | 19 | 26.1545 | 0.936017 | 41.7291 |
| 2024-acf-winter-at-oxford | 17 | 18 | 21.4882 | 0.869088 | 41.8411 |
| 2024-acf-winter-at-ubc | 5 | 6 | 28.017 | 0 | 34.0915 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 29.7873 | 0.6 | 43.4434 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25791 | 0.0167845 | 0.135893 | 0.886653 | 0.425338 |
| bonus_part_correctness | tier | fall | 7995 | 0.0213949 | 0.129828 | 0.894701 | 0.405937 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0147412 | 0.145228 | 0.864747 | 0.454424 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0274686 | 0.137525 | 0.883845 | 0.430342 |
| bonus_part_correctness | tier | winter | 8121 | 0.0175512 | 0.136034 | 0.886157 | 0.426334 |
| bonus_part_correctness | category | Current Events | 216 | 0.0591572 | 0.125161 | 0.907189 | 0.393332 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0232377 | 0.145215 | 0.87162 | 0.451841 |
| bonus_part_correctness | category | Geography | 501 | 0.0445194 | 0.136208 | 0.883519 | 0.429636 |
| bonus_part_correctness | category | History | 4068 | 0.0184364 | 0.13391 | 0.890237 | 0.418579 |
| bonus_part_correctness | category | Literature | 4065 | 0.0184723 | 0.131432 | 0.892852 | 0.412969 |
| bonus_part_correctness | category | Mythology | 945 | 0.0275507 | 0.152297 | 0.853075 | 0.465046 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0853692 | 0.140235 | 0.878879 | 0.437511 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0266503 | 0.13751 | 0.882713 | 0.431983 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0888464 | 0.15724 | 0.853755 | 0.470308 |
| bonus_part_correctness | category | Religion | 1008 | 0.0243664 | 0.133634 | 0.891181 | 0.416881 |
| bonus_part_correctness | category | Science | 4059 | 0.0230318 | 0.132657 | 0.890965 | 0.418892 |
| bonus_part_correctness | category | Social Science | 909 | 0.0372272 | 0.116982 | 0.913591 | 0.371485 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0274686 | 0.137525 | 0.883845 | 0.430342 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.058647 | 0.0821759 | 0.784113 | 0.286539 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0329523 | 0.12102 | 0.744288 | 0.39378 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0319769 | 0.204482 | 0.748978 | 0.595694 |
