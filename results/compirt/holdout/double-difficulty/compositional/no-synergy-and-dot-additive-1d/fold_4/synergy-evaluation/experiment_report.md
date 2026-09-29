# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.2105 |
| tournament_team_bonus_ppg_spearman | 0.928616 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.4264 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.899123 |
| log_loss | 0.403042 |
| ece | 0.0221565 |
| brier | 0.12795 |
| part_accuracy | 0.816941 |
| part_accuracy_easy | 0.914173 |
| part_accuracy_medium | 0.692763 |
| part_accuracy_hard | 0.843888 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.291386 |
| part_accuracy_macro_team | 0.821912 |
| part_accuracy_macro_bonus | 0.815149 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.349432 |
| probability_p10 | 0.05494 |
| probability_p50 | 0.55496 |
| probability_p90 | 0.966815 |
| mean_predictive_variance | 0.126786 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.531083 |
| ranked_probability_score | 0.112789 |
| bonus_total_score_log_loss | 0.998163 |
| ppb_mae | 1.65808 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 17.3877 | 0.966667 | 28.9816 |
| 2024-acf-fall-at-cornell | 15 | 17 | 13.2586 | 0.977659 | 16.3539 |
| 2024-acf-fall-at-georgia | 24 | 26 | 10.0279 | 0.982808 | 27.6902 |
| 2024-acf-fall-at-illinois | 18 | 22 | 16.3768 | 0.96691 | 32.7993 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 15.1132 | 0.937655 | 22.5191 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 13.1223 | 0.9662 | 23.8105 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 17.5064 | 0.933743 | 35.6779 |
| 2024-acf-fall-at-washington | 14 | 13 | 13.4645 | 0.943895 | 31.848 |
| 2024-acf-nationals | 47 | 81 | 9.77189 | 0.957956 | 18.6137 |
| 2024-acf-regionals-berkeley | 5 | 6 | 12.606 | 1 | 41.0263 |
| 2024-acf-regionals-cornell | 6 | 6 | 21.6291 | 0.828571 | 37.6361 |
| 2024-acf-regionals-imperial | 15 | 18 | 14.9377 | 0.941913 | 22.7786 |
| 2024-acf-regionals-jmu | 20 | 25 | 12.1475 | 0.949586 | 18.8644 |
| 2024-acf-regionals-minnesota | 4 | 4 | 13.6902 | 0.8 | 16.8183 |
| 2024-acf-regionals-mit | 2 | 1 | 10.323 | 1 | 20.6461 |
| 2024-acf-regionals-nebraska | 9 | 14 | 17.2468 | 0.816667 | 40.0806 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 14.586 | 0.964286 | 30.6737 |
| 2024-acf-regionals-rutgers | 11 | 11 | 15.1129 | 0.963636 | 30.6869 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 14.9889 | 0.859772 | 19.3485 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 16.7975 | 0.969724 | 29.1373 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 6.061 | 0.996965 | 15.4918 |
| 2024-acf-winter-at-clemson | 18 | 17 | 10.7209 | 0.981405 | 21.1601 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 14.0292 | 0.942208 | 25.624 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 12.78 | 0.96915 | 25.6543 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 18.7469 | 0.930234 | 29.8481 |
| 2024-acf-winter-at-online | 14 | 19 | 18.6132 | 0.927315 | 29.2675 |
| 2024-acf-winter-at-oxford | 18 | 19 | 16.9654 | 0.85493 | 37.4473 |
| 2024-acf-winter-at-ubc | 6 | 6 | 20.6813 | 0.6 | 42.0379 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 32.4109 | 1 | 69.6776 |

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
| bonus_part_correctness | aggregate | all | 25866 | 0.0221565 | 0.12795 | 0.899123 | 0.403042 |
| bonus_part_correctness | tier | fall | 8259 | 0.0218712 | 0.128155 | 0.896719 | 0.400189 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0294005 | 0.128701 | 0.894882 | 0.408797 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0169888 | 0.128212 | 0.897693 | 0.405247 |
| bonus_part_correctness | tier | winter | 7983 | 0.0270191 | 0.127165 | 0.900277 | 0.401482 |
| bonus_part_correctness | category | Current Events | 258 | 0.0451713 | 0.143538 | 0.879519 | 0.444973 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0369218 | 0.132181 | 0.893672 | 0.413778 |
| bonus_part_correctness | category | Geography | 450 | 0.0582143 | 0.131116 | 0.895566 | 0.411298 |
| bonus_part_correctness | category | History | 4116 | 0.0222343 | 0.124169 | 0.904736 | 0.390051 |
| bonus_part_correctness | category | Literature | 4092 | 0.0212948 | 0.124461 | 0.903385 | 0.393483 |
| bonus_part_correctness | category | Mythology | 951 | 0.0479289 | 0.126387 | 0.894311 | 0.400215 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0346046 | 0.116077 | 0.913832 | 0.372056 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0425639 | 0.133248 | 0.892097 | 0.424758 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0500881 | 0.141333 | 0.880047 | 0.422706 |
| bonus_part_correctness | category | Religion | 1029 | 0.0454733 | 0.127001 | 0.902281 | 0.399378 |
| bonus_part_correctness | category | Science | 4089 | 0.0265201 | 0.131923 | 0.892978 | 0.415789 |
| bonus_part_correctness | category | Social Science | 891 | 0.0258771 | 0.11748 | 0.912694 | 0.369388 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0169888 | 0.128212 | 0.897693 | 0.405247 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0284122 | 0.0677748 | 0.821556 | 0.238344 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0457786 | 0.117042 | 0.766332 | 0.38487 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0432434 | 0.199032 | 0.765443 | 0.585912 |
