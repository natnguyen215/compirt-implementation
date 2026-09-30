# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.4231 |
| tournament_team_bonus_ppg_spearman | 0.8646 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 471 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 25.6547 |
| bonus_game_margin_mae_games | 471 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.89888 |
| log_loss | 0.403633 |
| ece | 0.0217808 |
| brier | 0.128361 |
| part_accuracy | 0.817685 |
| part_accuracy_easy | 0.903672 |
| part_accuracy_medium | 0.704392 |
| part_accuracy_hard | 0.844992 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.299249 |
| part_accuracy_macro_team | 0.818243 |
| part_accuracy_macro_bonus | 0.815233 |
| part_count_easy | 8606 |
| part_count_medium | 8606 |
| part_count_hard | 8606 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.351045 |
| probability_p10 | 0.0545129 |
| probability_p50 | 0.554145 |
| probability_p90 | 0.966064 |
| mean_predictive_variance | 0.125669 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.529166 |
| ranked_probability_score | 0.111461 |
| bonus_total_score_log_loss | 0.985762 |
| ppb_mae | 1.82963 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 12.0755 | 0.953983 | 42.3145 |
| 2024-acf-fall-at-cornell | 17 | 18 | 17.4665 | 0.946013 | 24.4043 |
| 2024-acf-fall-at-georgia | 24 | 25 | 14.3038 | 0.948629 | 30.2284 |
| 2024-acf-fall-at-illinois | 19 | 22 | 19.6357 | 0.939369 | 26.3211 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 14.7981 | 0.942332 | 25.8809 |
| 2024-acf-fall-at-ohio-state | 16 | 20 | 14.2437 | 0.976437 | 19.7654 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 18.3326 | 0.869405 | 31.8343 |
| 2024-acf-fall-at-washington | 14 | 13 | 17.672 | 0.914099 | 20.0205 |
| 2024-acf-nationals | 46 | 81 | 12.6671 | 0.92667 | 24.0251 |
| 2024-acf-regionals-berkeley | 5 | 6 | 15.4898 | 0.9 | 27.2445 |
| 2024-acf-regionals-cornell | 6 | 6 | 22.0056 | 0.637748 | 33.0757 |
| 2024-acf-regionals-imperial | 14 | 18 | 17.1386 | 0.840485 | 36.4955 |
| 2024-acf-regionals-jmu | 18 | 23 | 14.4986 | 0.906366 | 24.2633 |
| 2024-acf-regionals-minnesota | 3 | 4 | 9.85239 | 1 | 19.9078 |
| 2024-acf-regionals-mit | 5 | 3 | 19.5897 | 0.3 | 19.1593 |
| 2024-acf-regionals-nebraska | 12 | 14 | 17.2168 | 0.949213 | 20.3103 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 17.0948 | 0.964286 | 7.11043 |
| 2024-acf-regionals-rutgers | 11 | 12 | 15.1422 | 0.911164 | 30.2697 |
| 2024-acf-regionals-vanderbilt | 6 | 5 | 26.0392 | 0.637748 | 36.6434 |
| 2024-acf-winter-at-brandeis | 16 | 17 | 16.7929 | 0.947059 | 25.427 |
| 2024-acf-winter-at-central-florida | 11 | 9 | 11.8497 | 0.977179 | 23.2681 |
| 2024-acf-winter-at-clemson | 16 | 17 | 14.6539 | 0.947059 | 21.4234 |
| 2024-acf-winter-at-lehigh | 14 | 12 | 14.4612 | 0.977976 | 20.4643 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 9.64107 | 0.969023 | 23.7645 |
| 2024-acf-winter-at-ohio-state | 17 | 18 | 14.0722 | 0.950921 | 19.5413 |
| 2024-acf-winter-at-online | 16 | 19 | 16.664 | 0.941091 | 23.1201 |
| 2024-acf-winter-at-oxford | 19 | 21 | 14.5181 | 0.942005 | 26.8488 |
| 2024-acf-winter-at-ubc | 5 | 6 | 11.9844 | 0.7 | 24.827 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 36.3708 | 0.257143 | 52.9964 |

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
| bonus_part_correctness | aggregate | all | 25818 | 0.0217808 | 0.128361 | 0.89888 | 0.403633 |
| bonus_part_correctness | tier | fall | 8415 | 0.0242451 | 0.131588 | 0.891599 | 0.408588 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0369128 | 0.125168 | 0.898989 | 0.399539 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0154455 | 0.127592 | 0.899482 | 0.401082 |
| bonus_part_correctness | tier | winter | 8154 | 0.0242734 | 0.127144 | 0.899729 | 0.402203 |
| bonus_part_correctness | category | Current Events | 258 | 0.0407321 | 0.104811 | 0.926082 | 0.350729 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.0240928 | 0.136241 | 0.886503 | 0.427399 |
| bonus_part_correctness | category | Geography | 453 | 0.0387016 | 0.130036 | 0.892021 | 0.409441 |
| bonus_part_correctness | category | History | 4176 | 0.0258048 | 0.129388 | 0.897228 | 0.404997 |
| bonus_part_correctness | category | Literature | 4197 | 0.0307581 | 0.119015 | 0.912128 | 0.377922 |
| bonus_part_correctness | category | Mythology | 951 | 0.0319568 | 0.134003 | 0.886544 | 0.414597 |
| bonus_part_correctness | category | Other Academic | 258 | 0.0333592 | 0.106718 | 0.929459 | 0.347518 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0340489 | 0.135004 | 0.886857 | 0.423165 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.0834383 | 0.156172 | 0.860222 | 0.456997 |
| bonus_part_correctness | category | Religion | 1041 | 0.0386901 | 0.129926 | 0.897687 | 0.409462 |
| bonus_part_correctness | category | Science | 4152 | 0.0225281 | 0.129381 | 0.896582 | 0.407987 |
| bonus_part_correctness | category | Social Science | 915 | 0.0347094 | 0.127706 | 0.898419 | 0.401326 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0154455 | 0.127592 | 0.899482 | 0.401082 |
| bonus_part_correctness | difficulty | easy | 8606 | 0.0138768 | 0.074069 | 0.815361 | 0.256819 |
| bonus_part_correctness | difficulty | hard | 8606 | 0.0357164 | 0.115212 | 0.783942 | 0.3755 |
| bonus_part_correctness | difficulty | medium | 8606 | 0.0457305 | 0.1958 | 0.773647 | 0.57858 |
