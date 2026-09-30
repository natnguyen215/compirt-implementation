# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.4162 |
| tournament_team_bonus_ppg_spearman | 0.909152 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.2171 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.898688 |
| log_loss | 0.401917 |
| ece | 0.01043 |
| brier | 0.128102 |
| part_accuracy | 0.816361 |
| part_accuracy_easy | 0.908102 |
| part_accuracy_medium | 0.700414 |
| part_accuracy_hard | 0.840568 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.290676 |
| part_accuracy_macro_team | 0.819029 |
| part_accuracy_macro_bonus | 0.816511 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.349978 |
| probability_p10 | 0.0511977 |
| probability_p50 | 0.514898 |
| probability_p90 | 0.98504 |
| mean_predictive_variance | 0.126977 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.531047 |
| ranked_probability_score | 0.112739 |
| bonus_total_score_log_loss | 0.994294 |
| ppb_mae | 1.61596 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 10.3974 | 0.966667 | 19.9316 |
| 2024-acf-fall-at-cornell | 16 | 18 | 12.9816 | 0.961001 | 30.6979 |
| 2024-acf-fall-at-georgia | 22 | 26 | 17.2908 | 0.952786 | 25.7072 |
| 2024-acf-fall-at-illinois | 16 | 15 | 15.5836 | 0.899854 | 22.3506 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 16.1942 | 0.894479 | 45.1247 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 9.03995 | 0.994635 | 20.1415 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 25.7282 | 0.775693 | 51.1973 |
| 2024-acf-fall-at-washington | 12 | 13 | 18.5689 | 0.909091 | 35.7069 |
| 2024-acf-nationals | 46 | 79 | 8.97599 | 0.961498 | 19.2152 |
| 2024-acf-regionals-berkeley | 6 | 5 | 14.2424 | 0.695725 | 31.8211 |
| 2024-acf-regionals-cornell | 5 | 6 | 12.1748 | 1 | 20.9422 |
| 2024-acf-regionals-imperial | 15 | 17 | 13.5616 | 0.963361 | 26.9105 |
| 2024-acf-regionals-jmu | 19 | 25 | 10.6038 | 0.949956 | 21.1762 |
| 2024-acf-regionals-minnesota | 3 | 4 | 16.6003 | 1 | 27.7952 |
| 2024-acf-regionals-mit | 4 | 2 | 30.0119 | 0.8 | 7.15759 |
| 2024-acf-regionals-nebraska | 11 | 13 | 16.2856 | 0.842827 | 26.4812 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 14.0272 | 1 | 33.2384 |
| 2024-acf-regionals-rutgers | 11 | 11 | 20.5515 | 0.815492 | 38.8999 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 9.7216 | 0.975758 | 21.8177 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 12.7969 | 0.974234 | 14.6883 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 9.26777 | 0.97619 | 19.8914 |
| 2024-acf-winter-at-clemson | 16 | 17 | 13.5597 | 0.966888 | 18.0859 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 14.9956 | 0.985699 | 21.5132 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 13.4228 | 0.962473 | 34.2218 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 15.4969 | 0.966826 | 22.4274 |
| 2024-acf-winter-at-online | 17 | 19 | 16.3815 | 0.955242 | 27.4828 |
| 2024-acf-winter-at-oxford | 17 | 19 | 19.0191 | 0.833333 | 26.2515 |
| 2024-acf-winter-at-ubc | 5 | 6 | 14.0909 | 0.5 | 34.26 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 25.4967 | 0.885714 | 29.343 |

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
| bonus_part_correctness | aggregate | all | 25365 | 0.01043 | 0.128102 | 0.898688 | 0.401917 |
| bonus_part_correctness | tier | fall | 8094 | 0.0169899 | 0.135416 | 0.88549 | 0.41932 |
| bonus_part_correctness | tier | nationals | 4125 | 0.017066 | 0.12901 | 0.894225 | 0.409251 |
| bonus_part_correctness | tier | regionals | 5247 | 0.018493 | 0.125177 | 0.901761 | 0.395594 |
| bonus_part_correctness | tier | winter | 7899 | 0.0163394 | 0.122075 | 0.90789 | 0.384454 |
| bonus_part_correctness | category | Current Events | 243 | 0.0748815 | 0.137527 | 0.884621 | 0.43582 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0288184 | 0.137661 | 0.883449 | 0.430059 |
| bonus_part_correctness | category | Geography | 456 | 0.0462567 | 0.130614 | 0.892626 | 0.402816 |
| bonus_part_correctness | category | History | 4050 | 0.0143324 | 0.126418 | 0.900588 | 0.395724 |
| bonus_part_correctness | category | Literature | 4029 | 0.0213601 | 0.123805 | 0.905177 | 0.389845 |
| bonus_part_correctness | category | Mythology | 936 | 0.0323984 | 0.130249 | 0.89182 | 0.404354 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0454833 | 0.105391 | 0.928244 | 0.348584 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0330771 | 0.136696 | 0.887345 | 0.420249 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0695067 | 0.144213 | 0.876111 | 0.4366 |
| bonus_part_correctness | category | Religion | 1014 | 0.0342459 | 0.125718 | 0.902197 | 0.399293 |
| bonus_part_correctness | category | Science | 4059 | 0.0171557 | 0.132146 | 0.892715 | 0.414255 |
| bonus_part_correctness | category | Social Science | 906 | 0.0337564 | 0.111551 | 0.922281 | 0.349182 |
| bonus_part_correctness | category | Unknown | 5247 | 0.018493 | 0.125177 | 0.901761 | 0.395594 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.0295994 | 0.0708177 | 0.821021 | 0.244459 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0363431 | 0.117311 | 0.773598 | 0.38267 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0224859 | 0.196177 | 0.769296 | 0.578621 |
