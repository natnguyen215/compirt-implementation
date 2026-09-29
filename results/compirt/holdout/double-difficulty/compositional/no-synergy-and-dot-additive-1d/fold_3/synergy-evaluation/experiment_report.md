# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.308 |
| tournament_team_bonus_ppg_spearman | 0.902642 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 27.1424 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.897015 |
| log_loss | 0.407623 |
| ece | 0.022342 |
| brier | 0.129288 |
| part_accuracy | 0.81577 |
| part_accuracy_easy | 0.912951 |
| part_accuracy_medium | 0.693791 |
| part_accuracy_hard | 0.840568 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.290085 |
| part_accuracy_macro_team | 0.817838 |
| part_accuracy_macro_bonus | 0.815512 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.34816 |
| probability_p10 | 0.0579343 |
| probability_p50 | 0.559948 |
| probability_p90 | 0.966205 |
| mean_predictive_variance | 0.127515 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.527499 |
| ranked_probability_score | 0.113722 |
| bonus_total_score_log_loss | 1.00737 |
| ppb_mae | 1.71448 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 11.995 | 0.966667 | 19.3453 |
| 2024-acf-fall-at-cornell | 16 | 18 | 13.012 | 0.975718 | 28.1205 |
| 2024-acf-fall-at-georgia | 22 | 26 | 16.1148 | 0.974838 | 24.056 |
| 2024-acf-fall-at-illinois | 16 | 15 | 16.9516 | 0.89249 | 25.133 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 17.4354 | 0.896933 | 45.7431 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 8.28703 | 0.994635 | 20.8403 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 23.5078 | 0.788204 | 51.061 |
| 2024-acf-fall-at-washington | 12 | 13 | 17.4948 | 0.902098 | 33.2636 |
| 2024-acf-nationals | 46 | 79 | 9.4575 | 0.966866 | 20.3961 |
| 2024-acf-regionals-berkeley | 6 | 5 | 18.6308 | 0.695725 | 38.8064 |
| 2024-acf-regionals-cornell | 5 | 6 | 16.9471 | 1 | 28.1218 |
| 2024-acf-regionals-imperial | 15 | 17 | 17.5279 | 0.952637 | 26.8211 |
| 2024-acf-regionals-jmu | 19 | 25 | 10.3883 | 0.948201 | 20.494 |
| 2024-acf-regionals-minnesota | 3 | 4 | 11.4288 | 1 | 20.9832 |
| 2024-acf-regionals-mit | 4 | 2 | 22.04 | 0.8 | 4.52745 |
| 2024-acf-regionals-nebraska | 11 | 13 | 21.8185 | 0.833715 | 27.6906 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 17.8717 | 0.9 | 35.7166 |
| 2024-acf-regionals-rutgers | 11 | 11 | 21.5998 | 0.760822 | 40.8088 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 9.8849 | 0.975758 | 23.4147 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 14.4933 | 0.965645 | 17.317 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 10.4486 | 0.97619 | 20.2365 |
| 2024-acf-winter-at-clemson | 16 | 17 | 15.634 | 0.974246 | 19.4212 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 14.6023 | 0.9901 | 23.9062 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 13.3546 | 0.965416 | 30.3596 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 16.8566 | 0.970413 | 27.8374 |
| 2024-acf-winter-at-online | 17 | 19 | 21.3923 | 0.902514 | 32.5085 |
| 2024-acf-winter-at-oxford | 17 | 19 | 18.5476 | 0.821078 | 27.2701 |
| 2024-acf-winter-at-ubc | 5 | 6 | 14.7978 | 0.5 | 35.5499 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 30.4107 | 0.885714 | 39.6817 |

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
| bonus_part_correctness | aggregate | all | 25365 | 0.022342 | 0.129288 | 0.897015 | 0.407623 |
| bonus_part_correctness | tier | fall | 8094 | 0.0248924 | 0.135557 | 0.885375 | 0.424892 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0252384 | 0.130668 | 0.892127 | 0.413481 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0290387 | 0.127447 | 0.899666 | 0.402837 |
| bonus_part_correctness | tier | winter | 7899 | 0.0260155 | 0.123366 | 0.906336 | 0.390047 |
| bonus_part_correctness | category | Current Events | 243 | 0.048219 | 0.137447 | 0.886382 | 0.433181 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0333209 | 0.139093 | 0.881463 | 0.436759 |
| bonus_part_correctness | category | Geography | 456 | 0.0431615 | 0.12846 | 0.891398 | 0.401963 |
| bonus_part_correctness | category | History | 4050 | 0.024536 | 0.12707 | 0.899612 | 0.399854 |
| bonus_part_correctness | category | Literature | 4029 | 0.0170544 | 0.124799 | 0.902564 | 0.396893 |
| bonus_part_correctness | category | Mythology | 936 | 0.0447369 | 0.129363 | 0.894343 | 0.404293 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0291981 | 0.105241 | 0.927065 | 0.344576 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0292727 | 0.137199 | 0.88577 | 0.422609 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0666365 | 0.148176 | 0.875707 | 0.449489 |
| bonus_part_correctness | category | Religion | 1014 | 0.0319142 | 0.125962 | 0.900757 | 0.403575 |
| bonus_part_correctness | category | Science | 4059 | 0.0246701 | 0.132944 | 0.891714 | 0.418636 |
| bonus_part_correctness | category | Social Science | 906 | 0.0338202 | 0.116072 | 0.916498 | 0.366847 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0290387 | 0.127447 | 0.899666 | 0.402837 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.0239232 | 0.0691873 | 0.811793 | 0.243444 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0409969 | 0.118462 | 0.768812 | 0.388547 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0456774 | 0.200214 | 0.763651 | 0.590877 |
