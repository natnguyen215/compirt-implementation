# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.8679 |
| tournament_team_bonus_ppg_spearman | 0.905393 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 27.2722 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.897586 |
| log_loss | 0.405929 |
| ece | 0.0180226 |
| brier | 0.12873 |
| part_accuracy | 0.817583 |
| part_accuracy_easy | 0.912714 |
| part_accuracy_medium | 0.696747 |
| part_accuracy_hard | 0.843288 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.291898 |
| part_accuracy_macro_team | 0.819445 |
| part_accuracy_macro_bonus | 0.816931 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.347658 |
| probability_p10 | 0.0565702 |
| probability_p50 | 0.55006 |
| probability_p90 | 0.96345 |
| mean_predictive_variance | 0.128196 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.530455 |
| ranked_probability_score | 0.113319 |
| bonus_total_score_log_loss | 1.00296 |
| ppb_mae | 1.73436 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 10.464 | 0.983333 | 16.7156 |
| 2024-acf-fall-at-cornell | 16 | 18 | 10.8335 | 0.962473 | 28.9214 |
| 2024-acf-fall-at-georgia | 22 | 26 | 19.1133 | 0.962398 | 31.365 |
| 2024-acf-fall-at-illinois | 16 | 15 | 16.634 | 0.863035 | 25.2954 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 16.6409 | 0.893252 | 42.0421 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 9.74003 | 0.987479 | 25.3238 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 24.2971 | 0.764969 | 49.0853 |
| 2024-acf-fall-at-washington | 12 | 13 | 13.6069 | 0.916084 | 33.9159 |
| 2024-acf-nationals | 46 | 79 | 9.36797 | 0.964213 | 19.598 |
| 2024-acf-regionals-berkeley | 6 | 5 | 10.2834 | 0.985611 | 20.071 |
| 2024-acf-regionals-cornell | 5 | 6 | 16.916 | 0.9 | 23.4544 |
| 2024-acf-regionals-imperial | 15 | 17 | 17.4324 | 0.956211 | 28.2115 |
| 2024-acf-regionals-jmu | 19 | 25 | 12.0118 | 0.955224 | 21.6189 |
| 2024-acf-regionals-minnesota | 3 | 4 | 8.00659 | 1 | 15.4572 |
| 2024-acf-regionals-mit | 4 | 2 | 22.0496 | 0.8 | 9.64434 |
| 2024-acf-regionals-nebraska | 11 | 13 | 22.5534 | 0.824604 | 29.941 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 16.0787 | 0.8 | 33.3206 |
| 2024-acf-regionals-rutgers | 11 | 11 | 22.007 | 0.760822 | 39.9396 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 13.1492 | 0.975758 | 30.0716 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 17.3394 | 0.954602 | 19.3272 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 14.8882 | 1 | 27.9489 |
| 2024-acf-winter-at-clemson | 16 | 17 | 14.9632 | 0.974246 | 19.534 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 16.129 | 0.985699 | 24.0008 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 11.1234 | 0.965416 | 28.1778 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 14.1305 | 0.988351 | 20.464 |
| 2024-acf-winter-at-online | 17 | 19 | 13.9659 | 0.925813 | 27.5708 |
| 2024-acf-winter-at-oxford | 17 | 19 | 21.509 | 0.821078 | 33.1051 |
| 2024-acf-winter-at-ubc | 5 | 6 | 16.6407 | 0.5 | 38.3632 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 28.2936 | 0.885714 | 37.3931 |

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
| bonus_part_correctness | aggregate | all | 25365 | 0.0180226 | 0.12873 | 0.897586 | 0.405929 |
| bonus_part_correctness | tier | fall | 8094 | 0.0226528 | 0.134457 | 0.886485 | 0.421246 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0198842 | 0.129231 | 0.893666 | 0.409881 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0221402 | 0.128106 | 0.898122 | 0.404947 |
| bonus_part_correctness | tier | winter | 7899 | 0.0216147 | 0.123013 | 0.906425 | 0.388824 |
| bonus_part_correctness | category | Current Events | 243 | 0.054303 | 0.134077 | 0.893293 | 0.422597 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.030115 | 0.138016 | 0.882924 | 0.432378 |
| bonus_part_correctness | category | Geography | 456 | 0.0453729 | 0.129162 | 0.893957 | 0.402001 |
| bonus_part_correctness | category | History | 4050 | 0.0211813 | 0.126426 | 0.900114 | 0.399139 |
| bonus_part_correctness | category | Literature | 4029 | 0.0192741 | 0.125497 | 0.901525 | 0.398932 |
| bonus_part_correctness | category | Mythology | 936 | 0.033375 | 0.129859 | 0.89276 | 0.405756 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0402368 | 0.101612 | 0.932213 | 0.335467 |
| bonus_part_correctness | category | Philosophy | 948 | 0.014676 | 0.134817 | 0.889175 | 0.416361 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0550234 | 0.13805 | 0.889091 | 0.422106 |
| bonus_part_correctness | category | Religion | 1014 | 0.0223865 | 0.12382 | 0.903267 | 0.395951 |
| bonus_part_correctness | category | Science | 4059 | 0.022769 | 0.131632 | 0.893321 | 0.414143 |
| bonus_part_correctness | category | Social Science | 906 | 0.0300773 | 0.114916 | 0.918695 | 0.363237 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0221402 | 0.128106 | 0.898122 | 0.404947 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.0250598 | 0.0689483 | 0.814477 | 0.243033 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0381691 | 0.117876 | 0.767629 | 0.386692 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0360576 | 0.199365 | 0.764078 | 0.588063 |
