# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 20.9894 |
| tournament_team_bonus_ppg_spearman | 0.88812 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.1543 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.890148 |
| log_loss | 0.418402 |
| ece | 0.0160285 |
| brier | 0.13368 |
| part_accuracy | 0.80753 |
| part_accuracy_easy | 0.912241 |
| part_accuracy_medium | 0.674512 |
| part_accuracy_hard | 0.835837 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.281845 |
| part_accuracy_macro_team | 0.810394 |
| part_accuracy_macro_bonus | 0.807468 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.34117 |
| probability_p10 | 0.0608107 |
| probability_p50 | 0.53577 |
| probability_p90 | 0.958807 |
| mean_predictive_variance | 0.132903 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.509403 |
| ranked_probability_score | 0.118734 |
| bonus_total_score_log_loss | 1.03633 |
| ppb_mae | 2.31908 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 12.5889 | 0.966667 | 20.4722 |
| 2024-acf-fall-at-cornell | 16 | 18 | 16.8494 | 0.878587 | 35.3746 |
| 2024-acf-fall-at-georgia | 22 | 26 | 20.8957 | 0.946 | 32.4196 |
| 2024-acf-fall-at-illinois | 16 | 15 | 13.4585 | 0.896908 | 22.7077 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 20.7022 | 0.896933 | 45.1016 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 19.7385 | 0.989268 | 32.4376 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 24.9479 | 0.813226 | 44.8196 |
| 2024-acf-fall-at-washington | 12 | 13 | 23.196 | 0.678322 | 40.3034 |
| 2024-acf-nationals | 46 | 79 | 18.19 | 0.829395 | 30.7652 |
| 2024-acf-regionals-berkeley | 6 | 5 | 22.6258 | 0.927634 | 31.8239 |
| 2024-acf-regionals-cornell | 5 | 6 | 21.3227 | 0.9 | 19.4904 |
| 2024-acf-regionals-imperial | 15 | 17 | 21.9029 | 0.890081 | 35.3016 |
| 2024-acf-regionals-jmu | 19 | 25 | 20.9813 | 0.924496 | 27.5351 |
| 2024-acf-regionals-minnesota | 3 | 4 | 32.9195 | 1 | 55.7638 |
| 2024-acf-regionals-mit | 4 | 2 | 22.0554 | 0.8 | 20.0169 |
| 2024-acf-regionals-nebraska | 11 | 13 | 24.9379 | 0.824604 | 39.4842 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 14.4833 | 0.8 | 27.2446 |
| 2024-acf-regionals-rutgers | 11 | 11 | 28.8943 | 0.769934 | 32.0619 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 10.5465 | 1 | 21.8303 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 22.7763 | 0.966872 | 26.1959 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 21.8029 | 1 | 34.7387 |
| 2024-acf-winter-at-clemson | 16 | 17 | 19.1519 | 0.908021 | 27.5541 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 20.0534 | 0.976898 | 40.748 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 19.0706 | 0.931568 | 38.7154 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 24.6567 | 0.938126 | 36.5425 |
| 2024-acf-winter-at-online | 17 | 19 | 20.4445 | 0.887799 | 31.5333 |
| 2024-acf-winter-at-oxford | 17 | 19 | 21.0454 | 0.828431 | 29.9557 |
| 2024-acf-winter-at-ubc | 5 | 6 | 19.1373 | 0.7 | 44.5546 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 29.3175 | 0.885714 | 39.6242 |

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
| bonus_part_correctness | aggregate | all | 25365 | 0.0160285 | 0.13368 | 0.890148 | 0.418402 |
| bonus_part_correctness | tier | fall | 8094 | 0.0218773 | 0.136389 | 0.883048 | 0.424083 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0178649 | 0.136218 | 0.882644 | 0.42791 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0296312 | 0.134855 | 0.889523 | 0.420894 |
| bonus_part_correctness | tier | winter | 7899 | 0.0173277 | 0.128798 | 0.897307 | 0.40596 |
| bonus_part_correctness | category | Current Events | 243 | 0.0733169 | 0.130768 | 0.889566 | 0.419642 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0263541 | 0.145035 | 0.871962 | 0.449778 |
| bonus_part_correctness | category | Geography | 456 | 0.0409311 | 0.132317 | 0.888122 | 0.410338 |
| bonus_part_correctness | category | History | 4050 | 0.0166221 | 0.130232 | 0.894531 | 0.4092 |
| bonus_part_correctness | category | Literature | 4029 | 0.0214711 | 0.132628 | 0.891233 | 0.415777 |
| bonus_part_correctness | category | Mythology | 936 | 0.0377275 | 0.130411 | 0.892614 | 0.404014 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0485252 | 0.102746 | 0.930042 | 0.335706 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0367791 | 0.148081 | 0.866986 | 0.451228 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0666528 | 0.130226 | 0.898333 | 0.400697 |
| bonus_part_correctness | category | Religion | 1014 | 0.0237369 | 0.127164 | 0.899329 | 0.402981 |
| bonus_part_correctness | category | Science | 4059 | 0.0190111 | 0.133009 | 0.889607 | 0.420676 |
| bonus_part_correctness | category | Social Science | 906 | 0.0367076 | 0.120026 | 0.910846 | 0.375217 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0296312 | 0.134855 | 0.889523 | 0.420894 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.0309141 | 0.0713445 | 0.797253 | 0.251461 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0369678 | 0.121587 | 0.748305 | 0.396921 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0414744 | 0.208109 | 0.740784 | 0.606823 |
