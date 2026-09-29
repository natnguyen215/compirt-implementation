# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.8219 |
| tournament_team_bonus_ppg_spearman | 0.9154 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 25.0368 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.900067 |
| log_loss | 0.399905 |
| ece | 0.0118676 |
| brier | 0.127046 |
| part_accuracy | 0.820467 |
| part_accuracy_easy | 0.904513 |
| part_accuracy_medium | 0.714964 |
| part_accuracy_hard | 0.841924 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.301465 |
| part_accuracy_macro_team | 0.823644 |
| part_accuracy_macro_bonus | 0.819138 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.352156 |
| probability_p10 | 0.0495293 |
| probability_p50 | 0.502428 |
| probability_p90 | 0.985046 |
| mean_predictive_variance | 0.125645 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.541449 |
| ranked_probability_score | 0.108765 |
| bonus_total_score_log_loss | 0.962957 |
| ppb_mae | 1.70448 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 18.2044 | 0.922172 | 29.1184 |
| 2024-acf-fall-at-cornell | 17 | 18 | 11.9994 | 0.95332 | 25.6787 |
| 2024-acf-fall-at-georgia | 21 | 23 | 12.2011 | 0.97336 | 24.4442 |
| 2024-acf-fall-at-illinois | 17 | 19 | 15.931 | 0.892995 | 21.3613 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 13.2949 | 0.978833 | 25.9666 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 10.7927 | 0.981405 | 24.1283 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 14.8258 | 0.953571 | 20.3681 |
| 2024-acf-fall-at-washington | 12 | 13 | 8.89355 | 0.91769 | 24.0247 |
| 2024-acf-nationals | 48 | 80 | 9.92204 | 0.966469 | 21.6878 |
| 2024-acf-regionals-berkeley | 6 | 7 | 13.8013 | 0.942857 | 20.5122 |
| 2024-acf-regionals-cornell | 6 | 6 | 30.879 | 0.6 | 49.9697 |
| 2024-acf-regionals-imperial | 15 | 18 | 13.6589 | 0.903571 | 25.3723 |
| 2024-acf-regionals-jmu | 19 | 23 | 10.5288 | 0.983765 | 19.8155 |
| 2024-acf-regionals-minnesota | 3 | 4 | 11.995 | 0.5 | 17.0997 |
| 2024-acf-regionals-mit | 7 | 4 | 19.5925 | 1 | 28.1033 |
| 2024-acf-regionals-nebraska | 11 | 13 | 18.0812 | 0.956722 | 38.6885 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 20.4871 | 0.964286 | 21.5459 |
| 2024-acf-regionals-rutgers | 10 | 11 | 12.5964 | 0.987879 | 19.3525 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 21.4206 | 0.951515 | 32.07 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 16.6514 | 0.940398 | 22.6726 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 14.7368 | 0.966667 | 13.0429 |
| 2024-acf-winter-at-clemson | 15 | 17 | 14.4655 | 0.959786 | 28.2593 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 14.9989 | 0.98487 | 23.141 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 11.875 | 0.965686 | 19.8783 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 18.2616 | 0.919678 | 32.5554 |
| 2024-acf-winter-at-online | 15 | 20 | 15.3768 | 0.932143 | 27.088 |
| 2024-acf-winter-at-oxford | 17 | 19 | 15.9284 | 0.909203 | 34.288 |
| 2024-acf-winter-at-ubc | 6 | 6 | 13.6595 | 1 | 13.3129 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 33.775 | 0.637748 | 66.9043 |

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
| bonus_part_correctness | aggregate | all | 25260 | 0.0118676 | 0.127046 | 0.900067 | 0.399905 |
| bonus_part_correctness | tier | fall | 8160 | 0.0118726 | 0.127883 | 0.894352 | 0.401777 |
| bonus_part_correctness | tier | nationals | 4107 | 0.026203 | 0.122172 | 0.903289 | 0.38869 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0182748 | 0.129402 | 0.895915 | 0.405343 |
| bonus_part_correctness | tier | winter | 7713 | 0.0132578 | 0.127142 | 0.899044 | 0.400173 |
| bonus_part_correctness | category | Current Events | 249 | 0.0405066 | 0.119448 | 0.909543 | 0.389435 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0114725 | 0.139182 | 0.882144 | 0.430459 |
| bonus_part_correctness | category | Geography | 459 | 0.0412386 | 0.136342 | 0.88159 | 0.416957 |
| bonus_part_correctness | category | History | 4017 | 0.0122544 | 0.123496 | 0.904898 | 0.38866 |
| bonus_part_correctness | category | Literature | 4047 | 0.0259041 | 0.120491 | 0.907082 | 0.390624 |
| bonus_part_correctness | category | Mythology | 924 | 0.0313622 | 0.14509 | 0.867019 | 0.442561 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0509479 | 0.117586 | 0.918343 | 0.373616 |
| bonus_part_correctness | category | Philosophy | 948 | 0.037365 | 0.129203 | 0.89603 | 0.409931 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0561601 | 0.134411 | 0.882207 | 0.400468 |
| bonus_part_correctness | category | Religion | 984 | 0.0251274 | 0.124782 | 0.903838 | 0.397193 |
| bonus_part_correctness | category | Science | 3990 | 0.00927203 | 0.124875 | 0.903827 | 0.391567 |
| bonus_part_correctness | category | Social Science | 897 | 0.0316045 | 0.107655 | 0.92493 | 0.346658 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0182748 | 0.129402 | 0.895915 | 0.405343 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0287853 | 0.0757054 | 0.808712 | 0.263102 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0242475 | 0.114998 | 0.786048 | 0.373603 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.0210043 | 0.190434 | 0.78147 | 0.56301 |
