# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.1711 |
| tournament_team_bonus_ppg_spearman | 0.907486 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.0929 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.89088 |
| log_loss | 0.416586 |
| ece | 0.0163746 |
| brier | 0.133323 |
| part_accuracy | 0.808397 |
| part_accuracy_easy | 0.913013 |
| part_accuracy_medium | 0.673626 |
| part_accuracy_hard | 0.838553 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.282842 |
| part_accuracy_macro_team | 0.812606 |
| part_accuracy_macro_bonus | 0.805561 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.34164 |
| probability_p10 | 0.0592839 |
| probability_p50 | 0.528178 |
| probability_p90 | 0.95811 |
| mean_predictive_variance | 0.13275 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.509047 |
| ranked_probability_score | 0.118376 |
| bonus_total_score_log_loss | 1.03378 |
| ppb_mae | 2.3466 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 18.0856 | 0.966667 | 21.521 |
| 2024-acf-fall-at-cornell | 15 | 17 | 16.9411 | 0.879357 | 21.3734 |
| 2024-acf-fall-at-georgia | 24 | 26 | 16.6696 | 0.935365 | 32.1411 |
| 2024-acf-fall-at-illinois | 18 | 22 | 19.2124 | 0.991729 | 31.4592 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 22.2722 | 0.919983 | 26.8954 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 21.8563 | 0.901049 | 37.9407 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 24.1475 | 0.904295 | 42.6176 |
| 2024-acf-fall-at-washington | 14 | 13 | 20.8204 | 0.924093 | 30.7351 |
| 2024-acf-nationals | 47 | 81 | 17.019 | 0.900489 | 30.0893 |
| 2024-acf-regionals-berkeley | 5 | 6 | 36.3082 | 1 | 71.3826 |
| 2024-acf-regionals-cornell | 6 | 6 | 25.3726 | 0.771429 | 43.84 |
| 2024-acf-regionals-imperial | 15 | 18 | 25.0958 | 0.934764 | 28.7231 |
| 2024-acf-regionals-jmu | 20 | 25 | 21.4306 | 0.939052 | 27.7875 |
| 2024-acf-regionals-minnesota | 4 | 4 | 13.6142 | 0.8 | 19.9096 |
| 2024-acf-regionals-mit | 2 | 1 | 21.6201 | 1 | 43.2402 |
| 2024-acf-regionals-nebraska | 9 | 14 | 24.394 | 0.8 | 47.7767 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 19.0441 | 0.892857 | 35.782 |
| 2024-acf-regionals-rutgers | 11 | 11 | 20.2757 | 0.936364 | 36.3868 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 23.1729 | 0.762209 | 34.375 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 28.1339 | 0.967091 | 40.1458 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 7.85616 | 0.996965 | 19.6513 |
| 2024-acf-winter-at-clemson | 18 | 17 | 19.3497 | 0.934918 | 36.9838 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 27.1677 | 0.935203 | 37.2254 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 18.4209 | 0.950339 | 28.7173 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 22.4879 | 0.938502 | 26.4261 |
| 2024-acf-winter-at-online | 14 | 19 | 16.7906 | 0.929518 | 28.426 |
| 2024-acf-winter-at-oxford | 18 | 19 | 18.411 | 0.847703 | 39.7797 |
| 2024-acf-winter-at-ubc | 6 | 6 | 28.4237 | 0.657143 | 43.5433 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 48.5672 | 1 | 64.5904 |

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
| bonus_part_correctness | aggregate | all | 25866 | 0.0163746 | 0.133323 | 0.89088 | 0.416586 |
| bonus_part_correctness | tier | fall | 8259 | 0.0174612 | 0.131751 | 0.890215 | 0.409116 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0265687 | 0.136159 | 0.884129 | 0.426595 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0177646 | 0.135748 | 0.887016 | 0.423441 |
| bonus_part_correctness | tier | winter | 7983 | 0.0189894 | 0.131811 | 0.892582 | 0.414404 |
| bonus_part_correctness | category | Current Events | 258 | 0.0523104 | 0.139355 | 0.884211 | 0.432618 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0244665 | 0.137547 | 0.884232 | 0.427896 |
| bonus_part_correctness | category | Geography | 450 | 0.0500796 | 0.131901 | 0.891587 | 0.409989 |
| bonus_part_correctness | category | History | 4116 | 0.0180736 | 0.128525 | 0.897989 | 0.40084 |
| bonus_part_correctness | category | Literature | 4092 | 0.021205 | 0.131418 | 0.892564 | 0.412208 |
| bonus_part_correctness | category | Mythology | 951 | 0.0468925 | 0.133068 | 0.885084 | 0.415077 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0359675 | 0.121131 | 0.908664 | 0.385049 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0366298 | 0.142922 | 0.87596 | 0.44685 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.06057 | 0.133122 | 0.886769 | 0.403921 |
| bonus_part_correctness | category | Religion | 1029 | 0.0298644 | 0.130717 | 0.896973 | 0.405799 |
| bonus_part_correctness | category | Science | 4089 | 0.0175867 | 0.135055 | 0.886732 | 0.424775 |
| bonus_part_correctness | category | Social Science | 891 | 0.0525048 | 0.123009 | 0.90362 | 0.38607 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0177646 | 0.135748 | 0.887016 | 0.423441 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0388717 | 0.0711375 | 0.802282 | 0.25039 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0391551 | 0.120996 | 0.748596 | 0.393702 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0445 | 0.207836 | 0.741108 | 0.605666 |
