# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 16.2354 |
| tournament_team_bonus_ppg_spearman | 0.887574 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 27.276 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.896031 |
| log_loss | 0.40842 |
| ece | 0.018172 |
| brier | 0.129767 |
| part_accuracy | 0.813927 |
| part_accuracy_easy | 0.90171 |
| part_accuracy_medium | 0.699663 |
| part_accuracy_hard | 0.840409 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.29456 |
| part_accuracy_macro_team | 0.816501 |
| part_accuracy_macro_bonus | 0.812243 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.351999 |
| probability_p10 | 0.0511217 |
| probability_p50 | 0.54007 |
| probability_p90 | 0.965628 |
| mean_predictive_variance | 0.125477 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.524485 |
| ranked_probability_score | 0.111585 |
| bonus_total_score_log_loss | 0.990023 |
| ppb_mae | 1.72324 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 17.5193 | 0.880952 | 25.5042 |
| 2024-acf-fall-at-cornell | 17 | 18 | 15.5638 | 0.975461 | 27.255 |
| 2024-acf-fall-at-georgia | 22 | 24 | 14.349 | 0.9474 | 28.3315 |
| 2024-acf-fall-at-illinois | 19 | 21 | 12.705 | 0.97193 | 24.5864 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 13.1385 | 0.956656 | 26.4976 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 17.5148 | 0.974703 | 27.5822 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 16.8882 | 0.961709 | 25.8613 |
| 2024-acf-fall-at-washington | 13 | 12 | 24.8605 | 0.895604 | 28.215 |
| 2024-acf-nationals | 47 | 79 | 11.3615 | 0.954312 | 25.4202 |
| 2024-acf-regionals-berkeley | 5 | 6 | 6.78866 | 0.974679 | 14.3361 |
| 2024-acf-regionals-cornell | 4 | 7 | 21.2714 | 0.4 | 33.102 |
| 2024-acf-regionals-imperial | 15 | 18 | 11.7043 | 0.965148 | 19.0905 |
| 2024-acf-regionals-jmu | 18 | 24 | 9.99908 | 0.953513 | 20.3635 |
| 2024-acf-regionals-minnesota | 4 | 4 | 29.8432 | 0.4 | 52.8507 |
| 2024-acf-regionals-mit | 6 | 4 | 19.1995 | 0.942857 | 21.6426 |
| 2024-acf-regionals-nebraska | 12 | 13 | 10.6751 | 0.956219 | 24.69 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 14.4684 | 0.714286 | 17.8385 |
| 2024-acf-regionals-rutgers | 11 | 11 | 16.9979 | 0.954545 | 29.624 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 16.8954 | 0.939394 | 37.7456 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 19.4654 | 0.941707 | 28.0166 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 14.0919 | 0.983333 | 19.6328 |
| 2024-acf-winter-at-clemson | 18 | 17 | 12.8013 | 0.950414 | 28.5082 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 9.08393 | 0.991192 | 21.6181 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 15.2494 | 0.945468 | 25.7217 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 20.9678 | 0.939618 | 31.6292 |
| 2024-acf-winter-at-online | 18 | 19 | 21.1827 | 0.898865 | 42.4072 |
| 2024-acf-winter-at-oxford | 17 | 18 | 17.3497 | 0.812542 | 37.5682 |
| 2024-acf-winter-at-ubc | 5 | 6 | 6.29687 | 0.9 | 21.1041 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 32.5952 | 0.657143 | 41.44 |

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
| bonus_part_correctness | aggregate | all | 25791 | 0.018172 | 0.129767 | 0.896031 | 0.40842 |
| bonus_part_correctness | tier | fall | 7995 | 0.0273489 | 0.126853 | 0.89929 | 0.395014 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0186931 | 0.128459 | 0.893956 | 0.406518 |
| bonus_part_correctness | tier | regionals | 5580 | 0.019831 | 0.128998 | 0.897142 | 0.405444 |
| bonus_part_correctness | tier | winter | 8121 | 0.0205259 | 0.133823 | 0.888869 | 0.424623 |
| bonus_part_correctness | category | Current Events | 216 | 0.0511236 | 0.114061 | 0.919242 | 0.362231 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0278858 | 0.139245 | 0.883335 | 0.431596 |
| bonus_part_correctness | category | Geography | 501 | 0.0505136 | 0.129436 | 0.899248 | 0.406215 |
| bonus_part_correctness | category | History | 4068 | 0.024552 | 0.128186 | 0.898343 | 0.403719 |
| bonus_part_correctness | category | Literature | 4065 | 0.0281739 | 0.125299 | 0.901175 | 0.396672 |
| bonus_part_correctness | category | Mythology | 945 | 0.0459314 | 0.150018 | 0.860468 | 0.456703 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0760592 | 0.14155 | 0.884551 | 0.44049 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0230495 | 0.133486 | 0.887026 | 0.424635 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0947223 | 0.153977 | 0.858796 | 0.470642 |
| bonus_part_correctness | category | Religion | 1008 | 0.0239629 | 0.127311 | 0.9 | 0.401735 |
| bonus_part_correctness | category | Science | 4059 | 0.0207972 | 0.127878 | 0.896797 | 0.408084 |
| bonus_part_correctness | category | Social Science | 909 | 0.034729 | 0.110132 | 0.923242 | 0.35083 |
| bonus_part_correctness | category | Unknown | 5580 | 0.019831 | 0.128998 | 0.897142 | 0.405444 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0205092 | 0.0758275 | 0.808267 | 0.261472 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0377967 | 0.117589 | 0.767437 | 0.385172 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0358989 | 0.195883 | 0.771912 | 0.578616 |
