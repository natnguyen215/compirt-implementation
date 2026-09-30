# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.9333 |
| tournament_team_bonus_ppg_spearman | 0.84649 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 469 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.8526 |
| bonus_game_margin_mae_games | 469 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.888484 |
| log_loss | 0.421638 |
| ece | 0.0165685 |
| brier | 0.134681 |
| part_accuracy | 0.809352 |
| part_accuracy_easy | 0.900314 |
| part_accuracy_medium | 0.685937 |
| part_accuracy_hard | 0.841805 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.289985 |
| part_accuracy_macro_team | 0.813186 |
| part_accuracy_macro_bonus | 0.806497 |
| part_count_easy | 8597 |
| part_count_medium | 8597 |
| part_count_hard | 8597 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.344406 |
| probability_p10 | 0.05348 |
| probability_p50 | 0.521629 |
| probability_p90 | 0.958457 |
| mean_predictive_variance | 0.131057 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.513784 |
| ranked_probability_score | 0.116907 |
| bonus_total_score_log_loss | 1.0255 |
| ppb_mae | 2.28683 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 12.7009 | 0.97619 | 25.1248 |
| 2024-acf-fall-at-cornell | 17 | 18 | 23.1313 | 0.851534 | 34.1428 |
| 2024-acf-fall-at-georgia | 22 | 24 | 20.1379 | 0.91516 | 33.7442 |
| 2024-acf-fall-at-illinois | 19 | 21 | 17.5663 | 0.968421 | 29.7591 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 14.0873 | 0.956656 | 19.3888 |
| 2024-acf-fall-at-ohio-state | 18 | 19 | 24.2019 | 0.945793 | 30.1282 |
| 2024-acf-fall-at-rutgers | 16 | 16 | 14.1431 | 0.949927 | 20.0482 |
| 2024-acf-fall-at-washington | 13 | 12 | 31.6249 | 0.846154 | 37.6631 |
| 2024-acf-nationals | 47 | 79 | 18.4895 | 0.878954 | 34.926 |
| 2024-acf-regionals-berkeley | 5 | 6 | 33.0401 | 0.872082 | 47.5188 |
| 2024-acf-regionals-cornell | 4 | 7 | 24.8391 | 0.4 | 36.1236 |
| 2024-acf-regionals-imperial | 15 | 18 | 18.6758 | 0.927614 | 34.5768 |
| 2024-acf-regionals-jmu | 18 | 24 | 18.9671 | 0.886364 | 30.8438 |
| 2024-acf-regionals-minnesota | 4 | 4 | 27.2526 | 0.8 | 70.9942 |
| 2024-acf-regionals-mit | 6 | 4 | 22.9271 | 0.942857 | 37.9272 |
| 2024-acf-regionals-nebraska | 12 | 13 | 10.3207 | 0.963224 | 20.178 |
| 2024-acf-regionals-ohio-state | 6 | 6 | 14.0059 | 0.542857 | 20.0185 |
| 2024-acf-regionals-rutgers | 11 | 11 | 30.3893 | 0.963636 | 43.2476 |
| 2024-acf-regionals-vanderbilt | 10 | 11 | 24.4464 | 0.90303 | 51.1201 |
| 2024-acf-winter-at-brandeis | 20 | 18 | 24.8693 | 0.917638 | 39.1086 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 18.7518 | 0.983333 | 28.0574 |
| 2024-acf-winter-at-clemson | 18 | 17 | 20.2461 | 0.893596 | 35.9132 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 22.0128 | 0.973571 | 36.9466 |
| 2024-acf-winter-at-northwestern | 20 | 21 | 14.1392 | 0.962016 | 25.8439 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 27.1603 | 0.879235 | 31.1568 |
| 2024-acf-winter-at-online | 18 | 19 | 25.2151 | 0.911249 | 43.3502 |
| 2024-acf-winter-at-oxford | 17 | 18 | 20.0715 | 0.837127 | 41.9913 |
| 2024-acf-winter-at-ubc | 5 | 6 | 18.9896 | 0.1 | 29.0697 |
| 2024-acf-winter-at-uc-berkeley | 6 | 6 | 43.6633 | 0.6 | 67.7118 |

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
| bonus_part_correctness | aggregate | all | 25791 | 0.0165685 | 0.134681 | 0.888484 | 0.421638 |
| bonus_part_correctness | tier | fall | 7995 | 0.0208434 | 0.128364 | 0.896409 | 0.39913 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0223083 | 0.13588 | 0.88214 | 0.427908 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0213013 | 0.136061 | 0.886215 | 0.425061 |
| bonus_part_correctness | tier | winter | 8121 | 0.0209179 | 0.139346 | 0.881009 | 0.438283 |
| bonus_part_correctness | category | Current Events | 216 | 0.0628029 | 0.117769 | 0.908653 | 0.383334 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0282564 | 0.145058 | 0.874024 | 0.447009 |
| bonus_part_correctness | category | Geography | 501 | 0.051275 | 0.136423 | 0.885783 | 0.43171 |
| bonus_part_correctness | category | History | 4068 | 0.0170322 | 0.130418 | 0.894363 | 0.411171 |
| bonus_part_correctness | category | Literature | 4065 | 0.0269624 | 0.130397 | 0.893823 | 0.411131 |
| bonus_part_correctness | category | Mythology | 945 | 0.0316646 | 0.150936 | 0.857016 | 0.459345 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0502336 | 0.14448 | 0.875292 | 0.455992 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0349312 | 0.13873 | 0.879725 | 0.43582 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0906165 | 0.142697 | 0.873097 | 0.431312 |
| bonus_part_correctness | category | Religion | 1008 | 0.0336365 | 0.134784 | 0.890035 | 0.417412 |
| bonus_part_correctness | category | Science | 4059 | 0.0259331 | 0.132085 | 0.891342 | 0.417439 |
| bonus_part_correctness | category | Social Science | 909 | 0.0366942 | 0.11898 | 0.91227 | 0.372977 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0213013 | 0.136061 | 0.886215 | 0.425061 |
| bonus_part_correctness | difficulty | easy | 8597 | 0.0284163 | 0.0783596 | 0.789489 | 0.271369 |
| bonus_part_correctness | difficulty | hard | 8597 | 0.0377958 | 0.12092 | 0.747572 | 0.395543 |
| bonus_part_correctness | difficulty | medium | 8597 | 0.0393314 | 0.204763 | 0.749051 | 0.598002 |
