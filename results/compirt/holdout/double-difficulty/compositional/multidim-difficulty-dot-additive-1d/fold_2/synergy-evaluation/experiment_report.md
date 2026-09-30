# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.1117 |
| tournament_team_bonus_ppg_spearman | 0.888131 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.4093 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.896758 |
| log_loss | 0.405585 |
| ece | 0.0126333 |
| brier | 0.129346 |
| part_accuracy | 0.813733 |
| part_accuracy_easy | 0.892521 |
| part_accuracy_medium | 0.702687 |
| part_accuracy_hard | 0.845993 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.294366 |
| part_accuracy_macro_team | 0.819284 |
| part_accuracy_macro_bonus | 0.811334 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.352995 |
| probability_p10 | 0.0435375 |
| probability_p50 | 0.491166 |
| probability_p90 | 0.98363 |
| mean_predictive_variance | 0.125267 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.526695 |
| ranked_probability_score | 0.111056 |
| bonus_total_score_log_loss | 0.984151 |
| ppb_mae | 1.59059 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 21.9862 | 0.880952 | 33.3304 |
| 2024-acf-fall-at-cornell | 17 | 18 | 13.172 | 0.981596 | 23.4318 |
| 2024-acf-fall-at-georgia | 22 | 24 | 12.9104 | 0.939481 | 25.9334 |
| 2024-acf-fall-at-illinois | 19 | 21 | 10.7887 | 0.975439 | 22.3289 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.9375 | 0.95872 | 26.5933 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 14.8391 | 0.971606 | 26.605 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 14.7062 | 0.970546 | 23.9066 |
| 2024-acf-fall-at-washington | 13 | 12 | 22.1487 | 0.917582 | 26.9851 |
| 2024-acf-nationals | 47 | 79 | 10.1082 | 0.961136 | 24.1906 |
| 2024-acf-regionals-berkeley | 5 | 6 | 4.4821 | 0.872082 | 7.55244 |
| 2024-acf-regionals-cornell | 4 | 7 | 22.1255 | 0.4 | 36.3812 |
| 2024-acf-regionals-imperial | 15 | 18 | 8.73521 | 0.986596 | 16.6998 |
| 2024-acf-regionals-jmu | 18 | 24 | 10.238 | 0.951447 | 21.9416 |
| 2024-acf-regionals-minnesota | 4 | 4 | 27.4883 | 0.4 | 50.2588 |
| 2024-acf-regionals-mit | 6 | 4 | 16.4276 | 0.942857 | 18.5176 |
| 2024-acf-regionals-nebraska | 12 | 13 | 11.8991 | 0.952716 | 29.5787 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 11.3315 | 0.828571 | 14.801 |
| 2024-acf-regionals-rutgers | 11 | 11 | 16.4092 | 0.954545 | 25.8546 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 15.0847 | 0.951515 | 28.856 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 18.8774 | 0.940955 | 29.6622 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 14.2032 | 0.983333 | 17.5649 |
| 2024-acf-winter-at-clemson | 18 | 17 | 12.7857 | 0.932852 | 29.6127 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 7.85248 | 0.980179 | 22.5687 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 12.3269 | 0.966529 | 21.8541 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 19.7191 | 0.929309 | 30.2745 |
| 2024-acf-winter-at-online | 18 | 19 | 21.0556 | 0.919505 | 43.3586 |
| 2024-acf-winter-at-oxford | 17 | 18 | 19.573 | 0.748621 | 40.1458 |
| 2024-acf-winter-at-ubc | 5 | 6 | 5.95406 | 0.9 | 22.4038 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 26.0724 | 0.657143 | 39.0689 |

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
| bonus_part_correctness | aggregate | all | 25791 | 0.0126333 | 0.129346 | 0.896758 | 0.405585 |
| bonus_part_correctness | tier | fall | 7995 | 0.0145759 | 0.124739 | 0.901669 | 0.388365 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0248011 | 0.128208 | 0.894964 | 0.404408 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0222344 | 0.129523 | 0.896193 | 0.404345 |
| bonus_part_correctness | tier | winter | 8121 | 0.0216166 | 0.134334 | 0.888721 | 0.423983 |
| bonus_part_correctness | category | Current Events | 216 | 0.0487179 | 0.109163 | 0.923117 | 0.350825 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0245998 | 0.140074 | 0.88143 | 0.432859 |
| bonus_part_correctness | category | Geography | 501 | 0.0362631 | 0.130799 | 0.89337 | 0.4096 |
| bonus_part_correctness | category | History | 4068 | 0.0200305 | 0.127062 | 0.900292 | 0.397829 |
| bonus_part_correctness | category | Literature | 4065 | 0.0195208 | 0.124286 | 0.901974 | 0.39361 |
| bonus_part_correctness | category | Mythology | 945 | 0.0383627 | 0.147919 | 0.862753 | 0.449744 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0827995 | 0.146511 | 0.877461 | 0.45158 |
| bonus_part_correctness | category | Philosophy | 963 | 0.034441 | 0.132956 | 0.889435 | 0.422584 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0719554 | 0.15275 | 0.858488 | 0.456019 |
| bonus_part_correctness | category | Religion | 1008 | 0.0368985 | 0.125062 | 0.902433 | 0.397669 |
| bonus_part_correctness | category | Science | 4059 | 0.0241205 | 0.127281 | 0.899182 | 0.404307 |
| bonus_part_correctness | category | Social Science | 909 | 0.0337694 | 0.10935 | 0.923105 | 0.346654 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0222344 | 0.129523 | 0.896193 | 0.404345 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0321863 | 0.0789343 | 0.816194 | 0.267234 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0334437 | 0.11554 | 0.77359 | 0.379388 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0173718 | 0.193564 | 0.774055 | 0.570133 |
