# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.2379 |
| tournament_team_bonus_ppg_spearman | 0.901535 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 27.2755 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.897357 |
| log_loss | 0.406637 |
| ece | 0.0194853 |
| brier | 0.128937 |
| part_accuracy | 0.816322 |
| part_accuracy_easy | 0.913306 |
| part_accuracy_medium | 0.6945 |
| part_accuracy_hard | 0.841159 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.290637 |
| part_accuracy_macro_team | 0.818772 |
| part_accuracy_macro_bonus | 0.816609 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.350269 |
| probability_p10 | 0.0535221 |
| probability_p50 | 0.554112 |
| probability_p90 | 0.966042 |
| mean_predictive_variance | 0.126297 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.528445 |
| ranked_probability_score | 0.113576 |
| bonus_total_score_log_loss | 1.00636 |
| ppb_mae | 1.74116 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 10.9251 | 0.983333 | 15.1565 |
| 2024-acf-fall-at-cornell | 16 | 18 | 13.2774 | 0.959529 | 31.8682 |
| 2024-acf-fall-at-georgia | 22 | 26 | 19.8672 | 0.955048 | 30.2664 |
| 2024-acf-fall-at-illinois | 16 | 15 | 18.2922 | 0.835052 | 25.9582 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 15.5315 | 0.896933 | 41.9083 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 9.79459 | 0.994635 | 23.1565 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 24.4398 | 0.782842 | 49.5694 |
| 2024-acf-fall-at-washington | 12 | 13 | 15.8018 | 0.888112 | 34.8885 |
| 2024-acf-nationals | 46 | 79 | 8.88427 | 0.969705 | 19.8351 |
| 2024-acf-regionals-berkeley | 6 | 5 | 9.25919 | 0.985611 | 19.6471 |
| 2024-acf-regionals-cornell | 5 | 6 | 17.206 | 0.9 | 21.3598 |
| 2024-acf-regionals-imperial | 15 | 17 | 18.4834 | 0.959786 | 28.0518 |
| 2024-acf-regionals-jmu | 19 | 25 | 12.3476 | 0.954346 | 22.4426 |
| 2024-acf-regionals-minnesota | 3 | 4 | 9.96447 | 1 | 18.3364 |
| 2024-acf-regionals-mit | 4 | 2 | 21.8882 | 0.8 | 10.2605 |
| 2024-acf-regionals-nebraska | 11 | 13 | 20.8565 | 0.833715 | 29.1455 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 18.9144 | 0.8 | 34.7244 |
| 2024-acf-regionals-rutgers | 11 | 11 | 22.8896 | 0.760822 | 40.2485 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 12.0186 | 0.975758 | 27.8632 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 17.5139 | 0.965645 | 20.2328 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 13.9113 | 1 | 29.4224 |
| 2024-acf-winter-at-clemson | 16 | 17 | 14.9631 | 0.987491 | 17.834 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 16.9064 | 0.9901 | 24.0337 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 10.6131 | 0.965416 | 27.0633 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 13.2941 | 0.984763 | 21.3316 |
| 2024-acf-winter-at-online | 17 | 19 | 17.3939 | 0.92336 | 27.7261 |
| 2024-acf-winter-at-oxford | 17 | 19 | 21.0396 | 0.821078 | 32.7117 |
| 2024-acf-winter-at-ubc | 5 | 6 | 16.5781 | 0.5 | 38.6104 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 28.0432 | 0.771429 | 37.2125 |

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
| bonus_part_correctness | aggregate | all | 25365 | 0.0194853 | 0.128937 | 0.897357 | 0.406637 |
| bonus_part_correctness | tier | fall | 8094 | 0.0243643 | 0.135306 | 0.885461 | 0.424069 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0194564 | 0.129128 | 0.893834 | 0.409593 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0254271 | 0.127777 | 0.898754 | 0.403874 |
| bonus_part_correctness | tier | winter | 7899 | 0.0235218 | 0.123082 | 0.906401 | 0.389067 |
| bonus_part_correctness | category | Current Events | 243 | 0.0717943 | 0.134084 | 0.89065 | 0.425757 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0324974 | 0.138739 | 0.881939 | 0.435013 |
| bonus_part_correctness | category | Geography | 456 | 0.0549744 | 0.129843 | 0.892483 | 0.40413 |
| bonus_part_correctness | category | History | 4050 | 0.0212635 | 0.126768 | 0.89976 | 0.399906 |
| bonus_part_correctness | category | Literature | 4029 | 0.0180585 | 0.125615 | 0.901452 | 0.398893 |
| bonus_part_correctness | category | Mythology | 936 | 0.0347871 | 0.129664 | 0.893099 | 0.405486 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0475297 | 0.102451 | 0.931407 | 0.339419 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0181373 | 0.134807 | 0.889264 | 0.41627 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0632262 | 0.141077 | 0.886717 | 0.43007 |
| bonus_part_correctness | category | Religion | 1014 | 0.0237141 | 0.123029 | 0.904726 | 0.394153 |
| bonus_part_correctness | category | Science | 4059 | 0.0247608 | 0.132421 | 0.892257 | 0.417058 |
| bonus_part_correctness | category | Social Science | 906 | 0.0317523 | 0.114256 | 0.919485 | 0.361256 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0254271 | 0.127777 | 0.898754 | 0.403874 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.0222511 | 0.0686029 | 0.815126 | 0.241622 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0393836 | 0.117882 | 0.767405 | 0.387262 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0417225 | 0.200326 | 0.762731 | 0.591027 |
