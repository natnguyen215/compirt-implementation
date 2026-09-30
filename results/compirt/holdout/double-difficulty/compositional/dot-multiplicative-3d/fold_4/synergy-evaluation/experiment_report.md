# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.0554 |
| tournament_team_bonus_ppg_spearman | 0.909055 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.2269 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.890803 |
| log_loss | 0.416936 |
| ece | 0.0158199 |
| brier | 0.133472 |
| part_accuracy | 0.807624 |
| part_accuracy_easy | 0.912897 |
| part_accuracy_medium | 0.673394 |
| part_accuracy_hard | 0.836581 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.282069 |
| part_accuracy_macro_team | 0.811168 |
| part_accuracy_macro_bonus | 0.803964 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.348233 |
| probability_p10 | 0.0525586 |
| probability_p50 | 0.532083 |
| probability_p90 | 0.967728 |
| mean_predictive_variance | 0.128075 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.508351 |
| ranked_probability_score | 0.118741 |
| bonus_total_score_log_loss | 1.03724 |
| ppb_mae | 2.34757 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 17.0083 | 0.966667 | 19.9096 |
| 2024-acf-fall-at-cornell | 15 | 17 | 17.8249 | 0.872208 | 21.6467 |
| 2024-acf-fall-at-georgia | 24 | 26 | 16.7539 | 0.935365 | 32.3955 |
| 2024-acf-fall-at-illinois | 18 | 22 | 17.2048 | 0.993797 | 30.054 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 23.3449 | 0.919983 | 27.2835 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 22.1426 | 0.897361 | 38.1846 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 24.2221 | 0.896933 | 43.0655 |
| 2024-acf-fall-at-washington | 14 | 13 | 20.2663 | 0.937294 | 30.141 |
| 2024-acf-nationals | 47 | 81 | 17.2916 | 0.895512 | 30.9993 |
| 2024-acf-regionals-berkeley | 5 | 6 | 35.3276 | 1 | 70.8579 |
| 2024-acf-regionals-cornell | 6 | 6 | 25.4813 | 0.771429 | 44.3863 |
| 2024-acf-regionals-imperial | 15 | 18 | 25.0355 | 0.934764 | 28.6665 |
| 2024-acf-regionals-jmu | 20 | 25 | 21.555 | 0.939052 | 27.644 |
| 2024-acf-regionals-minnesota | 4 | 4 | 13.6185 | 0.8 | 19.1797 |
| 2024-acf-regionals-mit | 2 | 1 | 20.2487 | 1 | 40.4974 |
| 2024-acf-regionals-nebraska | 9 | 14 | 24.0559 | 0.8 | 47.8838 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 18.2673 | 0.892857 | 34.766 |
| 2024-acf-regionals-rutgers | 11 | 11 | 19.9317 | 0.954545 | 36.0906 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 23.1873 | 0.762209 | 34.1105 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 27.9343 | 0.967091 | 40.1276 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 8.14017 | 0.996965 | 20.3032 |
| 2024-acf-winter-at-clemson | 18 | 17 | 19.4349 | 0.932852 | 37.0699 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 26.578 | 0.959721 | 36.2375 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 18.7475 | 0.954854 | 28.2422 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 22.1986 | 0.946771 | 26.3037 |
| 2024-acf-winter-at-online | 14 | 19 | 17.4072 | 0.929518 | 28.9814 |
| 2024-acf-winter-at-oxford | 18 | 19 | 19.1054 | 0.847703 | 40.8498 |
| 2024-acf-winter-at-ubc | 6 | 6 | 30.1114 | 0.657143 | 45.9687 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 47.1807 | 1 | 64.5257 |

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
| bonus_part_correctness | aggregate | all | 25866 | 0.0158199 | 0.133472 | 0.890803 | 0.416936 |
| bonus_part_correctness | tier | fall | 8259 | 0.0152564 | 0.131904 | 0.889985 | 0.408854 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0273184 | 0.13692 | 0.883174 | 0.428476 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0206481 | 0.135677 | 0.887732 | 0.421952 |
| bonus_part_correctness | tier | winter | 7983 | 0.0214696 | 0.131787 | 0.892602 | 0.415845 |
| bonus_part_correctness | category | Current Events | 258 | 0.0459337 | 0.14041 | 0.88385 | 0.432876 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0249638 | 0.138242 | 0.883367 | 0.428425 |
| bonus_part_correctness | category | Geography | 450 | 0.0511017 | 0.135213 | 0.888785 | 0.417045 |
| bonus_part_correctness | category | History | 4116 | 0.0181451 | 0.12863 | 0.897273 | 0.403262 |
| bonus_part_correctness | category | Literature | 4092 | 0.0210143 | 0.131136 | 0.893293 | 0.411622 |
| bonus_part_correctness | category | Mythology | 951 | 0.0461826 | 0.132912 | 0.884522 | 0.416591 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0379794 | 0.120783 | 0.910879 | 0.378491 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0502422 | 0.142435 | 0.877523 | 0.444169 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0618475 | 0.131063 | 0.889213 | 0.398615 |
| bonus_part_correctness | category | Religion | 1029 | 0.0360061 | 0.130877 | 0.897121 | 0.406934 |
| bonus_part_correctness | category | Science | 4089 | 0.0187276 | 0.135631 | 0.886341 | 0.426955 |
| bonus_part_correctness | category | Social Science | 891 | 0.0425523 | 0.122909 | 0.903398 | 0.385198 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0206481 | 0.135677 | 0.887732 | 0.421952 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0320496 | 0.0710199 | 0.797131 | 0.2495 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0402083 | 0.121236 | 0.749985 | 0.39458 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0481846 | 0.20816 | 0.741924 | 0.606728 |
