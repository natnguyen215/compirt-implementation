# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.6467 |
| tournament_team_bonus_ppg_spearman | 0.899765 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 26.2397 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.898666 |
| log_loss | 0.402386 |
| ece | 0.0122758 |
| brier | 0.128092 |
| part_accuracy | 0.816282 |
| part_accuracy_easy | 0.907747 |
| part_accuracy_medium | 0.700059 |
| part_accuracy_hard | 0.841041 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.290597 |
| part_accuracy_macro_team | 0.818412 |
| part_accuracy_macro_bonus | 0.816681 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.351972 |
| probability_p10 | 0.0483475 |
| probability_p50 | 0.520336 |
| probability_p90 | 0.985448 |
| mean_predictive_variance | 0.125548 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.530455 |
| ranked_probability_score | 0.112788 |
| bonus_total_score_log_loss | 0.996716 |
| ppb_mae | 1.62051 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 10.6138 | 0.966667 | 20.5848 |
| 2024-acf-fall-at-cornell | 16 | 18 | 14.2809 | 0.952171 | 30.6747 |
| 2024-acf-fall-at-georgia | 22 | 26 | 18.0045 | 0.955048 | 26.7744 |
| 2024-acf-fall-at-illinois | 16 | 15 | 14.994 | 0.861562 | 22.9034 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 16.7832 | 0.896933 | 45.4082 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 9.58833 | 0.991057 | 19.9676 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 25.5445 | 0.782842 | 51.546 |
| 2024-acf-fall-at-washington | 12 | 13 | 19.0463 | 0.909091 | 34.3085 |
| 2024-acf-nationals | 46 | 79 | 9.18911 | 0.960388 | 19.2903 |
| 2024-acf-regionals-berkeley | 6 | 5 | 14.0501 | 0.695725 | 31.7438 |
| 2024-acf-regionals-cornell | 5 | 6 | 14.4294 | 0.9 | 23.9068 |
| 2024-acf-regionals-imperial | 15 | 17 | 12.8277 | 0.959786 | 26.6861 |
| 2024-acf-regionals-jmu | 19 | 25 | 10.567 | 0.948201 | 19.8474 |
| 2024-acf-regionals-minnesota | 3 | 4 | 18.6822 | 1 | 31.1945 |
| 2024-acf-regionals-mit | 4 | 2 | 30.1168 | 0.8 | 10.9181 |
| 2024-acf-regionals-nebraska | 11 | 13 | 17.1297 | 0.824604 | 27.6332 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 15.3063 | 0.9 | 34.3897 |
| 2024-acf-regionals-rutgers | 11 | 11 | 21.7893 | 0.815492 | 40.3525 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 9.83757 | 0.975758 | 24.0467 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 11.9199 | 0.965645 | 14.3318 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 7.52372 | 0.97619 | 17.0734 |
| 2024-acf-winter-at-clemson | 16 | 17 | 13.017 | 0.974246 | 17.9504 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 17.0906 | 0.985699 | 23.5353 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 13.2986 | 0.968359 | 32.881 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 14.9343 | 0.963238 | 22.6921 |
| 2024-acf-winter-at-online | 17 | 19 | 13.7032 | 0.94298 | 24.8637 |
| 2024-acf-winter-at-oxford | 17 | 19 | 18.7134 | 0.835784 | 25.4874 |
| 2024-acf-winter-at-ubc | 5 | 6 | 13.2867 | 0.5 | 35.6 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 27.4875 | 0.885714 | 28.1258 |

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
| bonus_part_correctness | aggregate | all | 25365 | 0.0122758 | 0.128092 | 0.898666 | 0.402386 |
| bonus_part_correctness | tier | fall | 8094 | 0.018341 | 0.135504 | 0.885497 | 0.420772 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0181184 | 0.128744 | 0.89457 | 0.40895 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0206308 | 0.125447 | 0.901293 | 0.396582 |
| bonus_part_correctness | tier | winter | 7899 | 0.0162141 | 0.121913 | 0.908135 | 0.383975 |
| bonus_part_correctness | category | Current Events | 243 | 0.0646357 | 0.138749 | 0.882724 | 0.442504 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0292309 | 0.138005 | 0.882992 | 0.431644 |
| bonus_part_correctness | category | Geography | 456 | 0.0462443 | 0.129464 | 0.894407 | 0.400564 |
| bonus_part_correctness | category | History | 4050 | 0.0180207 | 0.125875 | 0.901407 | 0.394877 |
| bonus_part_correctness | category | Literature | 4029 | 0.0204657 | 0.123909 | 0.904849 | 0.390506 |
| bonus_part_correctness | category | Mythology | 936 | 0.0351529 | 0.129803 | 0.89258 | 0.403496 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0730228 | 0.105282 | 0.928244 | 0.350273 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0247239 | 0.137059 | 0.886419 | 0.421144 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.067781 | 0.144597 | 0.875202 | 0.439632 |
| bonus_part_correctness | category | Religion | 1014 | 0.0234898 | 0.125603 | 0.902333 | 0.39886 |
| bonus_part_correctness | category | Science | 4059 | 0.0186386 | 0.132121 | 0.892846 | 0.414856 |
| bonus_part_correctness | category | Social Science | 906 | 0.0391147 | 0.111048 | 0.922834 | 0.347973 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0206308 | 0.125447 | 0.901293 | 0.396582 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.027926 | 0.0705159 | 0.821368 | 0.243758 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0371449 | 0.117387 | 0.773392 | 0.383472 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0259434 | 0.196372 | 0.7692 | 0.579929 |
