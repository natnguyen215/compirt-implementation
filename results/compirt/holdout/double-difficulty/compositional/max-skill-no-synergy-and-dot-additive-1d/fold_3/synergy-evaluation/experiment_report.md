# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.0864 |
| tournament_team_bonus_ppg_spearman | 0.906309 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 27.477 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.895243 |
| log_loss | 0.410825 |
| ece | 0.019238 |
| brier | 0.129983 |
| part_accuracy | 0.81644 |
| part_accuracy_easy | 0.911768 |
| part_accuracy_medium | 0.699823 |
| part_accuracy_hard | 0.837729 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.290755 |
| part_accuracy_macro_team | 0.818501 |
| part_accuracy_macro_bonus | 0.81629 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.333548 |
| probability_p10 | 0.0774685 |
| probability_p50 | 0.533373 |
| probability_p90 | 0.95092 |
| mean_predictive_variance | 0.138086 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.53152 |
| ranked_probability_score | 0.113457 |
| bonus_total_score_log_loss | 1.00422 |
| ppb_mae | 1.66639 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 11.4772 | 0.966667 | 23.1872 |
| 2024-acf-fall-at-cornell | 16 | 18 | 12.3089 | 0.969831 | 32.6923 |
| 2024-acf-fall-at-georgia | 22 | 26 | 19.3383 | 0.956179 | 27.5873 |
| 2024-acf-fall-at-illinois | 16 | 15 | 14.7826 | 0.896908 | 22.2419 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 18.4102 | 0.907976 | 48.7794 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 8.31068 | 0.991057 | 21.6119 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 25.3842 | 0.788204 | 54.4361 |
| 2024-acf-fall-at-washington | 12 | 13 | 22.9806 | 0.832168 | 37.0146 |
| 2024-acf-nationals | 46 | 79 | 8.8425 | 0.966866 | 19.5714 |
| 2024-acf-regionals-berkeley | 6 | 5 | 13.7057 | 0.695725 | 32.1636 |
| 2024-acf-regionals-cornell | 5 | 6 | 15.071 | 0.9 | 26.3302 |
| 2024-acf-regionals-imperial | 15 | 17 | 15.437 | 0.959786 | 28.1088 |
| 2024-acf-regionals-jmu | 19 | 25 | 8.17973 | 0.974539 | 19.7513 |
| 2024-acf-regionals-minnesota | 3 | 4 | 11.8686 | 1 | 19.4549 |
| 2024-acf-regionals-mit | 4 | 2 | 32.5358 | 0.8 | 9.50234 |
| 2024-acf-regionals-nebraska | 11 | 13 | 21.74 | 0.833715 | 29.2577 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 12.4716 | 1 | 29.1549 |
| 2024-acf-regionals-rutgers | 11 | 11 | 16.2562 | 0.906608 | 35.4266 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 11.7371 | 0.975758 | 27.0163 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 14.1999 | 0.950921 | 15.2547 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 10.5823 | 0.97619 | 19.1395 |
| 2024-acf-winter-at-clemson | 16 | 17 | 13.8144 | 0.984548 | 18.1207 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 18.4253 | 0.950496 | 26.6129 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 13.0683 | 0.980133 | 32.8751 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 15.1493 | 0.981176 | 27.6803 |
| 2024-acf-winter-at-online | 17 | 19 | 19.1108 | 0.92336 | 31.1433 |
| 2024-acf-winter-at-oxford | 17 | 19 | 19.0764 | 0.828431 | 24.8174 |
| 2024-acf-winter-at-ubc | 5 | 6 | 14.9977 | 0.5 | 34.9073 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 27.2442 | 0.885714 | 39.6652 |

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
| bonus_part_correctness | aggregate | all | 25365 | 0.019238 | 0.129983 | 0.895243 | 0.410825 |
| bonus_part_correctness | tier | fall | 8094 | 0.025001 | 0.137019 | 0.882133 | 0.429369 |
| bonus_part_correctness | tier | nationals | 4125 | 0.036886 | 0.131433 | 0.892152 | 0.417767 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0289331 | 0.127567 | 0.898509 | 0.406021 |
| bonus_part_correctness | tier | winter | 7899 | 0.0245464 | 0.123621 | 0.905531 | 0.391389 |
| bonus_part_correctness | category | Current Events | 243 | 0.0585985 | 0.137023 | 0.881098 | 0.431488 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0317922 | 0.140255 | 0.878411 | 0.439658 |
| bonus_part_correctness | category | Geography | 456 | 0.0429731 | 0.133399 | 0.885338 | 0.417374 |
| bonus_part_correctness | category | History | 4050 | 0.0167053 | 0.128121 | 0.897741 | 0.402553 |
| bonus_part_correctness | category | Literature | 4029 | 0.0271542 | 0.126073 | 0.900898 | 0.403013 |
| bonus_part_correctness | category | Mythology | 936 | 0.0501449 | 0.130362 | 0.892319 | 0.409821 |
| bonus_part_correctness | category | Other Academic | 255 | 0.058676 | 0.105933 | 0.927251 | 0.34835 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0221308 | 0.138155 | 0.88435 | 0.427089 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0722424 | 0.144721 | 0.879343 | 0.437199 |
| bonus_part_correctness | category | Religion | 1014 | 0.0378403 | 0.124003 | 0.904049 | 0.3953 |
| bonus_part_correctness | category | Science | 4059 | 0.0222388 | 0.13389 | 0.88905 | 0.422109 |
| bonus_part_correctness | category | Social Science | 906 | 0.0485127 | 0.115166 | 0.91727 | 0.368187 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0289331 | 0.127567 | 0.898509 | 0.406021 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.050763 | 0.0715379 | 0.809841 | 0.254403 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0478789 | 0.120143 | 0.76299 | 0.39201 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0310273 | 0.198269 | 0.765422 | 0.586061 |
