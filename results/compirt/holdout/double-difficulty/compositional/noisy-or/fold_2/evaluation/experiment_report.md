# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 22.0365 |
| tournament_team_bonus_ppg_spearman | 0.844423 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 34.3034 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.889536 |
| log_loss | 0.420231 |
| ece | 0.0171618 |
| brier | 0.134083 |
| part_accuracy | 0.808344 |
| part_accuracy_easy | 0.896941 |
| part_accuracy_medium | 0.686053 |
| part_accuracy_hard | 0.842038 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.288977 |
| part_accuracy_macro_team | 0.810902 |
| part_accuracy_macro_bonus | 0.806787 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.357692 |
| probability_p10 | 0.0495933 |
| probability_p50 | 0.494221 |
| probability_p90 | 0.987082 |
| mean_predictive_variance | 0.121845 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.512039 |
| ranked_probability_score | 0.116907 |
| bonus_total_score_log_loss | 1.03033 |
| ppb_mae | 2.30113 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 13.2069 | 0.97619 | 25.5272 |
| 2024-acf-fall-at-cornell | 17 | 18 | 24.0928 | 0.862577 | 36.0774 |
| 2024-acf-fall-at-georgia | 22 | 24 | 20.7798 | 0.908938 | 35.4567 |
| 2024-acf-fall-at-illinois | 19 | 21 | 17.9361 | 0.977193 | 29.9642 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.6558 | 0.954592 | 19.2831 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 24.4771 | 0.934435 | 30.6864 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 13.6498 | 0.933727 | 19.0296 |
| 2024-acf-fall-at-washington | 13 | 12 | 31.2822 | 0.846154 | 38.4459 |
| 2024-acf-nationals | 47 | 79 | 19.8321 | 0.866405 | 36.7011 |
| 2024-acf-regionals-berkeley | 5 | 6 | 34.0568 | 0.974679 | 47.7227 |
| 2024-acf-regionals-cornell | 4 | 7 | 23.8381 | 0.4 | 36.3593 |
| 2024-acf-regionals-imperial | 15 | 18 | 17.4409 | 0.927614 | 32.2167 |
| 2024-acf-regionals-jmu | 18 | 24 | 19.0325 | 0.896695 | 32.0132 |
| 2024-acf-regionals-minnesota | 4 | 4 | 26.2847 | 0.8 | 71.3238 |
| 2024-acf-regionals-mit | 6 | 4 | 22.9723 | 0.942857 | 38.0726 |
| 2024-acf-regionals-nebraska | 12 | 13 | 10.7284 | 0.956219 | 21.0992 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 14.9759 | 0.542857 | 22.3796 |
| 2024-acf-regionals-rutgers | 11 | 11 | 30.9982 | 0.963636 | 43.7056 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 23.128 | 0.90303 | 46.0947 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 24.3099 | 0.929673 | 38.6027 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 18.4352 | 0.983333 | 29.3718 |
| 2024-acf-winter-at-clemson | 18 | 17 | 21.216 | 0.870868 | 38.5827 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 22.9367 | 0.973571 | 37.3551 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 13.2317 | 0.955999 | 23.5831 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 26.4869 | 0.879235 | 30.6463 |
| 2024-acf-winter-at-online | 18 | 19 | 25.8621 | 0.896801 | 44.6305 |
| 2024-acf-winter-at-oxford | 17 | 18 | 20.1663 | 0.830981 | 42.6848 |
| 2024-acf-winter-at-ubc | 5 | 6 | 19.0918 | 0 | 28.3349 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 43.9534 | 0.6 | 65.6832 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25791 | 0.0171618 | 0.134083 | 0.889536 | 0.420231 |
| bonus_part_correctness | tier | fall | 7995 | 0.0123042 | 0.128184 | 0.896279 | 0.396711 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0232769 | 0.136003 | 0.880637 | 0.432117 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0223105 | 0.134865 | 0.888247 | 0.421411 |
| bonus_part_correctness | tier | winter | 8121 | 0.0295364 | 0.138384 | 0.883236 | 0.436582 |
| bonus_part_correctness | category | Current Events | 216 | 0.059448 | 0.119982 | 0.906586 | 0.386714 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.037125 | 0.145135 | 0.874249 | 0.448075 |
| bonus_part_correctness | category | Geography | 501 | 0.0589794 | 0.133739 | 0.889658 | 0.42772 |
| bonus_part_correctness | category | History | 4068 | 0.0150805 | 0.129888 | 0.895303 | 0.40992 |
| bonus_part_correctness | category | Literature | 4065 | 0.0207306 | 0.129035 | 0.895575 | 0.406669 |
| bonus_part_correctness | category | Mythology | 945 | 0.0455351 | 0.15073 | 0.85748 | 0.466189 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0775581 | 0.148601 | 0.87379 | 0.471605 |
| bonus_part_correctness | category | Philosophy | 963 | 0.033068 | 0.139668 | 0.87893 | 0.441262 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0709494 | 0.142293 | 0.874486 | 0.424963 |
| bonus_part_correctness | category | Religion | 1008 | 0.0465011 | 0.134273 | 0.891354 | 0.418427 |
| bonus_part_correctness | category | Science | 4059 | 0.0192221 | 0.13224 | 0.89143 | 0.417489 |
| bonus_part_correctness | category | Social Science | 909 | 0.0298013 | 0.11675 | 0.913664 | 0.362959 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0223105 | 0.134865 | 0.888247 | 0.421411 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0290455 | 0.0786463 | 0.795535 | 0.272168 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0294846 | 0.119881 | 0.747307 | 0.392487 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0419595 | 0.20372 | 0.752521 | 0.596039 |
