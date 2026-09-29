# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.2023 |
| tournament_team_bonus_ppg_spearman | 0.909854 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 32.9378 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.890824 |
| log_loss | 0.416415 |
| ece | 0.0163911 |
| brier | 0.133425 |
| part_accuracy | 0.807392 |
| part_accuracy_easy | 0.908606 |
| part_accuracy_medium | 0.674322 |
| part_accuracy_hard | 0.839248 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.281837 |
| part_accuracy_macro_team | 0.811553 |
| part_accuracy_macro_bonus | 0.80355 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.356699 |
| probability_p10 | 0.0546789 |
| probability_p50 | 0.503663 |
| probability_p90 | 0.987763 |
| mean_predictive_variance | 0.122311 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.51067 |
| ranked_probability_score | 0.118916 |
| bonus_total_score_log_loss | 1.0414 |
| ppb_mae | 2.35512 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 17.4645 | 0.966667 | 18.476 |
| 2024-acf-fall-at-cornell | 15 | 17 | 16.5783 | 0.888293 | 20.4994 |
| 2024-acf-fall-at-georgia | 24 | 26 | 17.4815 | 0.937977 | 32.481 |
| 2024-acf-fall-at-illinois | 18 | 22 | 17.7949 | 0.991729 | 29.8544 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 23.8094 | 0.919983 | 27.8142 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 22.1326 | 0.901049 | 36.7953 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 23.5782 | 0.904295 | 42.052 |
| 2024-acf-fall-at-washington | 14 | 13 | 21.5363 | 0.937294 | 31.0117 |
| 2024-acf-nationals | 47 | 81 | 17.7336 | 0.886427 | 30.5501 |
| 2024-acf-regionals-berkeley | 5 | 6 | 37.4821 | 1 | 71.2433 |
| 2024-acf-regionals-cornell | 6 | 6 | 23.9612 | 0.771429 | 43.2327 |
| 2024-acf-regionals-imperial | 15 | 18 | 25.2488 | 0.934764 | 29.9654 |
| 2024-acf-regionals-jmu | 20 | 25 | 21.2588 | 0.942062 | 29.0671 |
| 2024-acf-regionals-minnesota | 4 | 4 | 13.7645 | 0.8 | 18.5636 |
| 2024-acf-regionals-mit | 2 | 1 | 23.2241 | 1 | 46.4482 |
| 2024-acf-regionals-nebraska | 9 | 14 | 24.1646 | 0.8 | 47.1121 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 17.8846 | 0.892857 | 35.8968 |
| 2024-acf-regionals-rutgers | 11 | 11 | 19.3065 | 0.936364 | 34.9073 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 21.9885 | 0.780502 | 31.4456 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 28.0115 | 0.970601 | 39.8637 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 8.85315 | 0.996965 | 20.4076 |
| 2024-acf-winter-at-clemson | 18 | 17 | 19.7282 | 0.919422 | 36.5755 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 27.5915 | 0.973732 | 37.6634 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 17.6422 | 0.956358 | 26.7904 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 22.249 | 0.942637 | 25.0448 |
| 2024-acf-winter-at-online | 14 | 19 | 17.0579 | 0.929518 | 28.173 |
| 2024-acf-winter-at-oxford | 18 | 19 | 19.524 | 0.847703 | 40.6685 |
| 2024-acf-winter-at-ubc | 6 | 6 | 30.4744 | 0.657143 | 46.4779 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 46.3414 | 1 | 64.1835 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25866 | 0.0163911 | 0.133425 | 0.890824 | 0.416415 |
| bonus_part_correctness | tier | fall | 8259 | 0.017659 | 0.132137 | 0.889671 | 0.409387 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0236099 | 0.136955 | 0.881758 | 0.433269 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0216235 | 0.13527 | 0.888407 | 0.420384 |
| bonus_part_correctness | tier | winter | 7983 | 0.0181359 | 0.131654 | 0.89327 | 0.412176 |
| bonus_part_correctness | category | Current Events | 258 | 0.0574817 | 0.141135 | 0.879759 | 0.455282 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0210155 | 0.137088 | 0.884323 | 0.425541 |
| bonus_part_correctness | category | Geography | 450 | 0.05394 | 0.136495 | 0.884948 | 0.429856 |
| bonus_part_correctness | category | History | 4116 | 0.0191921 | 0.129284 | 0.896297 | 0.405088 |
| bonus_part_correctness | category | Literature | 4092 | 0.0240317 | 0.131589 | 0.892694 | 0.411772 |
| bonus_part_correctness | category | Mythology | 951 | 0.0458285 | 0.13326 | 0.886945 | 0.408599 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0393503 | 0.121356 | 0.908612 | 0.38503 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0450971 | 0.143087 | 0.87582 | 0.448451 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0683991 | 0.133213 | 0.886816 | 0.404081 |
| bonus_part_correctness | category | Religion | 1029 | 0.0289014 | 0.129777 | 0.898186 | 0.401122 |
| bonus_part_correctness | category | Science | 4089 | 0.0250989 | 0.135328 | 0.886605 | 0.425571 |
| bonus_part_correctness | category | Social Science | 891 | 0.0337835 | 0.122667 | 0.904493 | 0.380444 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0216235 | 0.13527 | 0.888407 | 0.420384 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0284312 | 0.0713799 | 0.800997 | 0.249246 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0311069 | 0.120078 | 0.746612 | 0.391249 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0497042 | 0.208818 | 0.740944 | 0.60875 |
