# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.2935 |
| tournament_team_bonus_ppg_spearman | 0.9296 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 25.7081 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.899701 |
| log_loss | 0.400737 |
| ece | 0.0114302 |
| brier | 0.127347 |
| part_accuracy | 0.817753 |
| part_accuracy_easy | 0.90849 |
| part_accuracy_medium | 0.696126 |
| part_accuracy_hard | 0.848643 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.292198 |
| part_accuracy_macro_team | 0.820719 |
| part_accuracy_macro_bonus | 0.813777 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.351417 |
| probability_p10 | 0.0490861 |
| probability_p50 | 0.500639 |
| probability_p90 | 0.985572 |
| mean_predictive_variance | 0.126214 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.533635 |
| ranked_probability_score | 0.112 |
| bonus_total_score_log_loss | 0.992677 |
| ppb_mae | 1.63456 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 14.0763 | 0.966667 | 31.8316 |
| 2024-acf-fall-at-cornell | 15 | 17 | 10.8522 | 0.975872 | 18.9701 |
| 2024-acf-fall-at-georgia | 24 | 26 | 11.4234 | 0.975409 | 26.4966 |
| 2024-acf-fall-at-illinois | 18 | 22 | 17.8472 | 0.96691 | 28.1496 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.718 | 0.957406 | 20.0809 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 11.1663 | 0.957595 | 23.4578 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 17.0847 | 0.930062 | 38.5138 |
| 2024-acf-fall-at-washington | 14 | 13 | 15.125 | 0.950496 | 30.4512 |
| 2024-acf-nationals | 47 | 81 | 9.05227 | 0.958535 | 19.0477 |
| 2024-acf-regionals-berkeley | 5 | 6 | 14.2209 | 1 | 42.3478 |
| 2024-acf-regionals-cornell | 6 | 6 | 19.5002 | 0.828571 | 37.655 |
| 2024-acf-regionals-imperial | 15 | 18 | 13.0323 | 0.945487 | 21.127 |
| 2024-acf-regionals-jmu | 20 | 25 | 10.9307 | 0.953349 | 18.1011 |
| 2024-acf-regionals-minnesota | 4 | 4 | 12.3391 | 0.8 | 17.5092 |
| 2024-acf-regionals-mit | 2 | 1 | 14.4694 | 1 | 28.9388 |
| 2024-acf-regionals-nebraska | 9 | 14 | 16.6009 | 0.883333 | 41.6971 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 18.0155 | 0.892857 | 29.6822 |
| 2024-acf-regionals-rutgers | 11 | 11 | 14.6177 | 0.963636 | 30.4545 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 13.1883 | 0.859772 | 17.2975 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 19.422 | 0.969724 | 29.8 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 5.39844 | 0.996965 | 13.7708 |
| 2024-acf-winter-at-clemson | 18 | 17 | 13.3517 | 0.981405 | 21.5059 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 19.1307 | 0.91769 | 30.6972 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 11.3615 | 0.980437 | 23.6343 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 17.4591 | 0.950906 | 23.3802 |
| 2024-acf-winter-at-online | 14 | 19 | 16.4098 | 0.938328 | 21.8813 |
| 2024-acf-winter-at-oxford | 18 | 19 | 16.2224 | 0.856995 | 37.7601 |
| 2024-acf-winter-at-ubc | 6 | 6 | 23.4972 | 0.6 | 44.0949 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 32.9969 | 1 | 59.1379 |

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
| bonus_part_correctness | aggregate | all | 25866 | 0.0114302 | 0.127347 | 0.899701 | 0.400737 |
| bonus_part_correctness | tier | fall | 8259 | 0.00866261 | 0.127207 | 0.897036 | 0.397202 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0211975 | 0.128895 | 0.89389 | 0.411584 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0170482 | 0.127319 | 0.899905 | 0.398674 |
| bonus_part_correctness | tier | winter | 7983 | 0.0153652 | 0.126702 | 0.900164 | 0.400142 |
| bonus_part_correctness | category | Current Events | 258 | 0.0496754 | 0.139219 | 0.880782 | 0.448205 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0236241 | 0.130088 | 0.895273 | 0.40897 |
| bonus_part_correctness | category | Geography | 450 | 0.0372394 | 0.12447 | 0.901758 | 0.390477 |
| bonus_part_correctness | category | History | 4116 | 0.0172221 | 0.12433 | 0.90362 | 0.392093 |
| bonus_part_correctness | category | Literature | 4092 | 0.0196142 | 0.123924 | 0.903827 | 0.392121 |
| bonus_part_correctness | category | Mythology | 951 | 0.0449676 | 0.129098 | 0.892154 | 0.405216 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0334996 | 0.117819 | 0.912883 | 0.370728 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0210212 | 0.133062 | 0.890665 | 0.424139 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0379508 | 0.139942 | 0.876757 | 0.419412 |
| bonus_part_correctness | category | Religion | 1029 | 0.0168756 | 0.127134 | 0.899807 | 0.400578 |
| bonus_part_correctness | category | Science | 4089 | 0.0197989 | 0.131825 | 0.89263 | 0.415492 |
| bonus_part_correctness | category | Social Science | 891 | 0.024908 | 0.11635 | 0.915368 | 0.362145 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0170482 | 0.127319 | 0.899905 | 0.398674 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0358172 | 0.0705782 | 0.822634 | 0.244 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0359765 | 0.114771 | 0.769957 | 0.3793 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0203378 | 0.19669 | 0.767532 | 0.578911 |
