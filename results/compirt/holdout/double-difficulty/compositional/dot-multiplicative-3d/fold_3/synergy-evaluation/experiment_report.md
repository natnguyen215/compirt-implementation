# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.1531 |
| tournament_team_bonus_ppg_spearman | 0.882869 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.3025 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.889314 |
| log_loss | 0.420185 |
| ece | 0.0183308 |
| brier | 0.134402 |
| part_accuracy | 0.806229 |
| part_accuracy_easy | 0.911532 |
| part_accuracy_medium | 0.671082 |
| part_accuracy_hard | 0.836073 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.280544 |
| part_accuracy_macro_team | 0.809179 |
| part_accuracy_macro_bonus | 0.806494 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.345934 |
| probability_p10 | 0.0564873 |
| probability_p50 | 0.543714 |
| probability_p90 | 0.967141 |
| mean_predictive_variance | 0.12936 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.506919 |
| ranked_probability_score | 0.119435 |
| bonus_total_score_log_loss | 1.04424 |
| ppb_mae | 2.34257 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 13.6857 | 0.966667 | 22.0231 |
| 2024-acf-fall-at-cornell | 16 | 18 | 17.5827 | 0.878587 | 35.5307 |
| 2024-acf-fall-at-georgia | 22 | 26 | 21.4442 | 0.946566 | 32.9111 |
| 2024-acf-fall-at-illinois | 16 | 15 | 13.8298 | 0.896908 | 22.1611 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 20.8961 | 0.896933 | 45.899 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 19.7507 | 0.989268 | 32.4463 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 24.6155 | 0.813226 | 45.2819 |
| 2024-acf-fall-at-washington | 12 | 13 | 23.8081 | 0.65035 | 41.37 |
| 2024-acf-nationals | 46 | 79 | 18.4496 | 0.827359 | 31.001 |
| 2024-acf-regionals-berkeley | 6 | 5 | 22.1803 | 0.927634 | 30.9789 |
| 2024-acf-regionals-cornell | 5 | 6 | 21.6852 | 0.9 | 18.9881 |
| 2024-acf-regionals-imperial | 15 | 17 | 22.9635 | 0.890081 | 36.0523 |
| 2024-acf-regionals-jmu | 19 | 25 | 21.6995 | 0.926251 | 27.9162 |
| 2024-acf-regionals-minnesota | 3 | 4 | 31.3128 | 1 | 53.4382 |
| 2024-acf-regionals-mit | 4 | 2 | 22.8439 | 0.8 | 20.2153 |
| 2024-acf-regionals-nebraska | 11 | 13 | 25.4104 | 0.824604 | 40.4565 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 14.2272 | 0.8 | 27.6381 |
| 2024-acf-regionals-rutgers | 11 | 11 | 28.1945 | 0.769934 | 33.0216 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 10.5314 | 0.987879 | 20.9418 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 22.3917 | 0.966872 | 25.8384 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 22.3801 | 1 | 33.8192 |
| 2024-acf-winter-at-clemson | 16 | 17 | 19.8479 | 0.908021 | 28.5649 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 20.1595 | 0.981299 | 39.4986 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 19.2734 | 0.943341 | 38.1792 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 24.2811 | 0.923776 | 36.0816 |
| 2024-acf-winter-at-online | 17 | 19 | 20.3072 | 0.887799 | 32.7092 |
| 2024-acf-winter-at-oxford | 17 | 19 | 19.5054 | 0.828431 | 27.4372 |
| 2024-acf-winter-at-ubc | 5 | 6 | 19.3788 | 0.7 | 45.3298 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 30.8042 | 0.771429 | 43.3737 |

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
| bonus_part_correctness | aggregate | all | 25365 | 0.0183308 | 0.134402 | 0.889314 | 0.420185 |
| bonus_part_correctness | tier | fall | 8094 | 0.0211788 | 0.137061 | 0.882033 | 0.426225 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0130741 | 0.137213 | 0.881561 | 0.430011 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0336834 | 0.136082 | 0.88854 | 0.4243 |
| bonus_part_correctness | tier | winter | 7899 | 0.015888 | 0.129091 | 0.896999 | 0.406131 |
| bonus_part_correctness | category | Current Events | 243 | 0.0754557 | 0.134128 | 0.883875 | 0.43785 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0339818 | 0.14637 | 0.870255 | 0.451777 |
| bonus_part_correctness | category | Geography | 456 | 0.0344226 | 0.129145 | 0.891766 | 0.40239 |
| bonus_part_correctness | category | History | 4050 | 0.0137299 | 0.130868 | 0.893475 | 0.409924 |
| bonus_part_correctness | category | Literature | 4029 | 0.016975 | 0.132484 | 0.891702 | 0.416303 |
| bonus_part_correctness | category | Mythology | 936 | 0.0447899 | 0.130385 | 0.893694 | 0.401441 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0386983 | 0.10426 | 0.927375 | 0.340427 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0551091 | 0.149063 | 0.865819 | 0.452465 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0747831 | 0.135395 | 0.891162 | 0.414235 |
| bonus_part_correctness | category | Religion | 1014 | 0.0251019 | 0.128637 | 0.897959 | 0.406708 |
| bonus_part_correctness | category | Science | 4059 | 0.0216003 | 0.133498 | 0.888904 | 0.42249 |
| bonus_part_correctness | category | Social Science | 906 | 0.0391641 | 0.120391 | 0.909917 | 0.37595 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0336834 | 0.136082 | 0.88854 | 0.4243 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.0244954 | 0.0715253 | 0.791881 | 0.252058 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.039236 | 0.121862 | 0.750954 | 0.397029 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0488396 | 0.209817 | 0.738249 | 0.611467 |
