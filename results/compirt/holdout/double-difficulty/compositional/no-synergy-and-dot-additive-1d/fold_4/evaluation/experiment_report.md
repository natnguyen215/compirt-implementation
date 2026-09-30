# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.0861 |
| tournament_team_bonus_ppg_spearman | 0.907897 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 32.7916 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.89067 |
| log_loss | 0.417548 |
| ece | 0.0197888 |
| brier | 0.133613 |
| part_accuracy | 0.807508 |
| part_accuracy_easy | 0.912433 |
| part_accuracy_medium | 0.67293 |
| part_accuracy_hard | 0.837161 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.281953 |
| part_accuracy_macro_team | 0.810588 |
| part_accuracy_macro_bonus | 0.804955 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.34309 |
| probability_p10 | 0.0587328 |
| probability_p50 | 0.540675 |
| probability_p90 | 0.957477 |
| mean_predictive_variance | 0.131578 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.508583 |
| ranked_probability_score | 0.118825 |
| bonus_total_score_log_loss | 1.03772 |
| ppb_mae | 2.37228 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 17.5998 | 0.966667 | 20.2279 |
| 2024-acf-fall-at-cornell | 15 | 17 | 17.2819 | 0.872208 | 20.704 |
| 2024-acf-fall-at-georgia | 24 | 26 | 16.8373 | 0.935365 | 31.6346 |
| 2024-acf-fall-at-illinois | 18 | 22 | 18.2603 | 0.991729 | 30.7215 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 23.0944 | 0.919983 | 26.6726 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 21.993 | 0.901049 | 37.491 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 23.1987 | 0.901841 | 41.3474 |
| 2024-acf-fall-at-washington | 14 | 13 | 20.6151 | 0.924093 | 30.2794 |
| 2024-acf-nationals | 47 | 81 | 17.6799 | 0.896091 | 30.3302 |
| 2024-acf-regionals-berkeley | 5 | 6 | 35.009 | 1 | 71.2433 |
| 2024-acf-regionals-cornell | 6 | 6 | 26.0986 | 0.771429 | 44.4771 |
| 2024-acf-regionals-imperial | 15 | 18 | 25.3947 | 0.934764 | 28.1062 |
| 2024-acf-regionals-jmu | 20 | 25 | 22.8037 | 0.939052 | 29.0004 |
| 2024-acf-regionals-minnesota | 4 | 4 | 12.0469 | 0.8 | 18.1761 |
| 2024-acf-regionals-mit | 2 | 1 | 20.0602 | 1 | 40.1204 |
| 2024-acf-regionals-nebraska | 9 | 14 | 24.965 | 0.8 | 48.4599 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 18.3167 | 0.892857 | 36.642 |
| 2024-acf-regionals-rutgers | 11 | 11 | 19.7084 | 0.936364 | 35.8565 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 23.3721 | 0.774405 | 31.5959 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 28.3753 | 0.967969 | 39.696 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 8.59856 | 0.996965 | 20.524 |
| 2024-acf-winter-at-clemson | 18 | 17 | 18.8079 | 0.934918 | 35.8286 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 26.5405 | 0.935203 | 37.3804 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 18.0984 | 0.960873 | 27.1337 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 22.624 | 0.934368 | 25.4593 |
| 2024-acf-winter-at-online | 14 | 19 | 15.9988 | 0.933923 | 27.4797 |
| 2024-acf-winter-at-oxford | 18 | 19 | 19.2948 | 0.849768 | 40.0028 |
| 2024-acf-winter-at-ubc | 6 | 6 | 29.9209 | 0.657143 | 45.9697 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 47.9026 | 1 | 65.0809 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25866 | 0.0197888 | 0.133613 | 0.89067 | 0.417548 |
| bonus_part_correctness | tier | fall | 8259 | 0.0218187 | 0.132154 | 0.889945 | 0.410302 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0336419 | 0.136826 | 0.883647 | 0.429354 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0188355 | 0.136156 | 0.886118 | 0.425114 |
| bonus_part_correctness | tier | winter | 7983 | 0.0216021 | 0.131707 | 0.893187 | 0.41371 |
| bonus_part_correctness | category | Current Events | 258 | 0.0651191 | 0.141361 | 0.881023 | 0.441206 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0307661 | 0.138369 | 0.88338 | 0.430037 |
| bonus_part_correctness | category | Geography | 450 | 0.0547279 | 0.136816 | 0.886349 | 0.422969 |
| bonus_part_correctness | category | History | 4116 | 0.0221846 | 0.129244 | 0.897022 | 0.403232 |
| bonus_part_correctness | category | Literature | 4092 | 0.0243852 | 0.131147 | 0.893167 | 0.411533 |
| bonus_part_correctness | category | Mythology | 951 | 0.0423899 | 0.133557 | 0.884634 | 0.417564 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0370638 | 0.120552 | 0.910932 | 0.383219 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0325475 | 0.141948 | 0.878088 | 0.446059 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0581344 | 0.132621 | 0.88832 | 0.401602 |
| bonus_part_correctness | category | Religion | 1029 | 0.0487473 | 0.129898 | 0.899051 | 0.40363 |
| bonus_part_correctness | category | Science | 4089 | 0.0278157 | 0.135065 | 0.887243 | 0.424367 |
| bonus_part_correctness | category | Social Science | 891 | 0.0392761 | 0.122781 | 0.904564 | 0.383473 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0188355 | 0.136156 | 0.886118 | 0.425114 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0333964 | 0.0700148 | 0.804643 | 0.247816 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0413109 | 0.121783 | 0.744266 | 0.396059 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0497835 | 0.209041 | 0.739476 | 0.608769 |
