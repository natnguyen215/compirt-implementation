# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 23.152 |
| tournament_team_bonus_ppg_spearman | 0.903858 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 37.3157 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.887951 |
| log_loss | 0.423293 |
| ece | 0.0189187 |
| brier | 0.134775 |
| part_accuracy | 0.807508 |
| part_accuracy_easy | 0.908258 |
| part_accuracy_medium | 0.677801 |
| part_accuracy_hard | 0.836465 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.281953 |
| part_accuracy_macro_team | 0.811414 |
| part_accuracy_macro_bonus | 0.80324 |
| part_count_easy | 8622 |
| part_count_medium | 8622 |
| part_count_hard | 8622 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.331499 |
| probability_p10 | 0.0689433 |
| probability_p50 | 0.501217 |
| probability_p90 | 0.937852 |
| mean_predictive_variance | 0.140049 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.509163 |
| ranked_probability_score | 0.119622 |
| bonus_total_score_log_loss | 1.04356 |
| ppb_mae | 2.42557 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 8 | 22.882 | 0.966667 | 18.2749 |
| 2024-acf-fall-at-cornell | 15 | 17 | 14.535 | 0.981234 | 19.8975 |
| 2024-acf-fall-at-georgia | 24 | 26 | 21.538 | 0.897063 | 36.3999 |
| 2024-acf-fall-at-illinois | 18 | 22 | 23.1086 | 0.983456 | 31.0863 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 20.2776 | 0.919983 | 25.3512 |
| 2024-acf-fall-at-ohio-state | 17 | 18 | 24.0767 | 0.963741 | 41.8437 |
| 2024-acf-fall-at-rutgers | 17 | 19 | 21.4038 | 0.949694 | 46.835 |
| 2024-acf-fall-at-washington | 14 | 13 | 28.1158 | 0.928493 | 46.947 |
| 2024-acf-nationals | 47 | 81 | 22.8071 | 0.820626 | 39.9424 |
| 2024-acf-regionals-berkeley | 5 | 6 | 49.0534 | 0.8 | 75.4008 |
| 2024-acf-regionals-cornell | 6 | 6 | 31.9809 | 0.771429 | 48.1567 |
| 2024-acf-regionals-imperial | 15 | 18 | 33.1215 | 0.891868 | 55.5363 |
| 2024-acf-regionals-jmu | 20 | 25 | 20.9738 | 0.945072 | 39.3975 |
| 2024-acf-regionals-minnesota | 4 | 4 | 7.95599 | 1 | 21.4399 |
| 2024-acf-regionals-mit | 2 | 1 | 30.8542 | 1 | 61.7085 |
| 2024-acf-regionals-nebraska | 9 | 14 | 18.0573 | 0.9 | 40.1465 |
| 2024-acf-regionals-ohio-state | 7 | 6 | 21.1199 | 0.964286 | 41.5401 |
| 2024-acf-regionals-rutgers | 11 | 11 | 18.1729 | 0.972727 | 31.0486 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 24.1198 | 0.689037 | 41.6111 |
| 2024-acf-winter-at-brandeis | 19 | 18 | 25.2039 | 0.951295 | 37.9915 |
| 2024-acf-winter-at-central-florida | 10 | 10 | 11.9053 | 0.996965 | 25.3613 |
| 2024-acf-winter-at-clemson | 18 | 17 | 22.9894 | 0.904959 | 45.1705 |
| 2024-acf-winter-at-lehigh | 12 | 13 | 21.7977 | 0.952716 | 31.5766 |
| 2024-acf-winter-at-northwestern | 20 | 20 | 15.4766 | 0.964635 | 32.4051 |
| 2024-acf-winter-at-ohio-state | 18 | 15 | 23.17 | 0.901293 | 31.566 |
| 2024-acf-winter-at-online | 14 | 19 | 15.2991 | 0.894275 | 25.5605 |
| 2024-acf-winter-at-oxford | 18 | 19 | 17.4064 | 0.900362 | 35.9077 |
| 2024-acf-winter-at-ubc | 6 | 6 | 32.8391 | 0.6 | 46.5528 |
| 2024-acf-winter-at-uc-berkeley | 4 | 5 | 31.1654 | 0.8 | 42.5802 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25866 | 0.0189187 | 0.134775 | 0.887951 | 0.423293 |
| bonus_part_correctness | tier | fall | 8259 | 0.02934 | 0.134097 | 0.886772 | 0.418615 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0288954 | 0.142686 | 0.870625 | 0.449286 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0235673 | 0.138072 | 0.882673 | 0.431436 |
| bonus_part_correctness | tier | winter | 7983 | 0.0266634 | 0.129094 | 0.896873 | 0.408998 |
| bonus_part_correctness | category | Current Events | 258 | 0.0387999 | 0.146153 | 0.866406 | 0.461699 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0290373 | 0.138972 | 0.880384 | 0.436204 |
| bonus_part_correctness | category | Geography | 450 | 0.0508405 | 0.139993 | 0.876421 | 0.432059 |
| bonus_part_correctness | category | History | 4116 | 0.0227329 | 0.129613 | 0.895819 | 0.408604 |
| bonus_part_correctness | category | Literature | 4092 | 0.0281584 | 0.132695 | 0.890831 | 0.416956 |
| bonus_part_correctness | category | Mythology | 951 | 0.0631473 | 0.136465 | 0.882555 | 0.425075 |
| bonus_part_correctness | category | Other Academic | 276 | 0.059781 | 0.117536 | 0.911354 | 0.380583 |
| bonus_part_correctness | category | Philosophy | 957 | 0.040657 | 0.141522 | 0.876705 | 0.443856 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0403632 | 0.131653 | 0.892268 | 0.407984 |
| bonus_part_correctness | category | Religion | 1029 | 0.0286701 | 0.129186 | 0.897377 | 0.408682 |
| bonus_part_correctness | category | Science | 4089 | 0.0240034 | 0.136928 | 0.883087 | 0.431471 |
| bonus_part_correctness | category | Social Science | 891 | 0.0232424 | 0.121832 | 0.90688 | 0.385093 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0235673 | 0.138072 | 0.882673 | 0.431436 |
| bonus_part_correctness | difficulty | easy | 8622 | 0.0678218 | 0.0741614 | 0.789743 | 0.265977 |
| bonus_part_correctness | difficulty | hard | 8622 | 0.0366325 | 0.122222 | 0.739742 | 0.397353 |
| bonus_part_correctness | difficulty | medium | 8622 | 0.0387797 | 0.207942 | 0.741903 | 0.606549 |
