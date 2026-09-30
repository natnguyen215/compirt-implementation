# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.452 |
| tournament_team_bonus_ppg_spearman | 0.910813 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.1815 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.899841 |
| log_loss | 0.401623 |
| ece | 0.020328 |
| brier | 0.127469 |
| part_accuracy | 0.818963 |
| part_accuracy_easy | 0.905107 |
| part_accuracy_medium | 0.710095 |
| part_accuracy_hard | 0.841686 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.29996 |
| part_accuracy_macro_team | 0.821369 |
| part_accuracy_macro_bonus | 0.816972 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.350789 |
| probability_p10 | 0.0545149 |
| probability_p50 | 0.551596 |
| probability_p90 | 0.964993 |
| mean_predictive_variance | 0.126021 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.535392 |
| ranked_probability_score | 0.109267 |
| bonus_total_score_log_loss | 0.968754 |
| ppb_mae | 1.79413 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 16.5978 | 0.922172 | 31.2567 |
| 2024-acf-fall-at-cornell | 17 | 18 | 9.71849 | 0.955777 | 23.8465 |
| 2024-acf-fall-at-georgia | 21 | 23 | 15.099 | 0.951267 | 26.3498 |
| 2024-acf-fall-at-illinois | 17 | 19 | 16.7272 | 0.892995 | 21.3363 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.7648 | 0.972638 | 27.8256 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 9.01455 | 0.966943 | 26.6405 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 12.8351 | 0.953571 | 20.4228 |
| 2024-acf-fall-at-washington | 12 | 13 | 10.4764 | 0.910684 | 25.6428 |
| 2024-acf-nationals | 48 | 80 | 12.6447 | 0.959844 | 22.8454 |
| 2024-acf-regionals-berkeley | 6 | 7 | 16.3053 | 0.942857 | 23.8504 |
| 2024-acf-regionals-cornell | 6 | 6 | 32.3135 | 0.6 | 43.7713 |
| 2024-acf-regionals-imperial | 15 | 18 | 15.9155 | 0.889286 | 28.4704 |
| 2024-acf-regionals-jmu | 19 | 23 | 12.2868 | 0.978499 | 21.6748 |
| 2024-acf-regionals-minnesota | 3 | 4 | 8.50162 | 0.5 | 13.7558 |
| 2024-acf-regionals-mit | 7 | 4 | 17.2583 | 1 | 25.3283 |
| 2024-acf-regionals-nebraska | 11 | 13 | 24.3371 | 0.924832 | 44.4835 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 17.7552 | 0.964286 | 14.1876 |
| 2024-acf-regionals-rutgers | 10 | 11 | 15.584 | 0.975758 | 27.9669 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 26.4071 | 0.951515 | 43.6128 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 17.2628 | 0.922738 | 23.3411 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 16.7263 | 0.966667 | 14.6254 |
| 2024-acf-winter-at-clemson | 15 | 17 | 14.6989 | 0.959786 | 30.0709 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 14.224 | 0.98487 | 20.0311 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 12.0232 | 0.970588 | 19.6892 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 17.7585 | 0.907887 | 31.1552 |
| 2024-acf-winter-at-online | 15 | 20 | 16.5885 | 0.917857 | 29.9394 |
| 2024-acf-winter-at-oxford | 17 | 19 | 14.2791 | 0.932516 | 30.1165 |
| 2024-acf-winter-at-ubc | 6 | 6 | 15.8668 | 1 | 16.9125 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 33.1363 | 0.637748 | 67.3854 |

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
| bonus_part_correctness | aggregate | all | 25260 | 0.020328 | 0.127469 | 0.899841 | 0.401623 |
| bonus_part_correctness | tier | fall | 8160 | 0.014565 | 0.127847 | 0.894405 | 0.401886 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0362293 | 0.123249 | 0.903053 | 0.392788 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0260187 | 0.132149 | 0.892761 | 0.413715 |
| bonus_part_correctness | tier | winter | 7713 | 0.0264655 | 0.126112 | 0.901408 | 0.397772 |
| bonus_part_correctness | category | Current Events | 249 | 0.0488822 | 0.124065 | 0.90031 | 0.400585 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0216946 | 0.1388 | 0.882819 | 0.432061 |
| bonus_part_correctness | category | Geography | 459 | 0.0335123 | 0.135731 | 0.878833 | 0.421285 |
| bonus_part_correctness | category | History | 4017 | 0.0254432 | 0.123926 | 0.905295 | 0.389696 |
| bonus_part_correctness | category | Literature | 4047 | 0.0199071 | 0.119982 | 0.909091 | 0.383987 |
| bonus_part_correctness | category | Mythology | 924 | 0.0444233 | 0.144261 | 0.869115 | 0.443733 |
| bonus_part_correctness | category | Other Academic | 237 | 0.06415 | 0.120151 | 0.915989 | 0.385721 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0408878 | 0.128307 | 0.896698 | 0.40754 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0465461 | 0.132049 | 0.881734 | 0.405925 |
| bonus_part_correctness | category | Religion | 984 | 0.0241451 | 0.123069 | 0.904992 | 0.394663 |
| bonus_part_correctness | category | Science | 3990 | 0.0203874 | 0.124911 | 0.903608 | 0.394496 |
| bonus_part_correctness | category | Social Science | 897 | 0.0354871 | 0.107666 | 0.92506 | 0.3466 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0260187 | 0.132149 | 0.892761 | 0.413715 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0179433 | 0.0741242 | 0.80569 | 0.257958 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0314822 | 0.116482 | 0.781305 | 0.378585 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.0418536 | 0.1918 | 0.782155 | 0.568326 |
