# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 21.0883 |
| tournament_team_bonus_ppg_spearman | 0.885626 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 461 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 33.2308 |
| bonus_game_margin_mae_games | 461 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.889525 |
| log_loss | 0.420214 |
| ece | 0.0218523 |
| brier | 0.134294 |
| part_accuracy | 0.806742 |
| part_accuracy_easy | 0.912241 |
| part_accuracy_medium | 0.672383 |
| part_accuracy_hard | 0.8356 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.281057 |
| part_accuracy_macro_team | 0.809226 |
| part_accuracy_macro_bonus | 0.8064 |
| part_count_easy | 8455 |
| part_count_medium | 8455 |
| part_count_hard | 8455 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.341181 |
| probability_p10 | 0.0597004 |
| probability_p50 | 0.545618 |
| probability_p90 | 0.956589 |
| mean_predictive_variance | 0.132694 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.50822 |
| ranked_probability_score | 0.119216 |
| bonus_total_score_log_loss | 1.042 |
| ppb_mae | 2.35782 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 9 | 9 | 13.4856 | 0.966667 | 21.6782 |
| 2024-acf-fall-at-cornell | 16 | 18 | 17.072 | 0.860927 | 34.9281 |
| 2024-acf-fall-at-georgia | 22 | 26 | 20.9327 | 0.940346 | 32.3099 |
| 2024-acf-fall-at-illinois | 16 | 15 | 14.5508 | 0.904272 | 24.8776 |
| 2024-acf-fall-at-north-carolina | 17 | 22 | 21.2893 | 0.894479 | 45.2438 |
| 2024-acf-fall-at-ohio-state | 15 | 20 | 19.3726 | 0.989268 | 32.4587 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 25.8109 | 0.832887 | 44.6583 |
| 2024-acf-fall-at-washington | 12 | 13 | 23.5411 | 0.65035 | 40.4283 |
| 2024-acf-nationals | 46 | 79 | 19.2186 | 0.821188 | 31.0687 |
| 2024-acf-regionals-berkeley | 6 | 5 | 22.9572 | 0.927634 | 33.1188 |
| 2024-acf-regionals-cornell | 5 | 6 | 21.324 | 0.9 | 18.7959 |
| 2024-acf-regionals-imperial | 15 | 17 | 21.953 | 0.879357 | 33.0686 |
| 2024-acf-regionals-jmu | 19 | 25 | 22.1312 | 0.921862 | 28.087 |
| 2024-acf-regionals-minnesota | 3 | 4 | 30.1276 | 1 | 51.697 |
| 2024-acf-regionals-mit | 4 | 2 | 21.7782 | 0.8 | 18.0389 |
| 2024-acf-regionals-nebraska | 11 | 13 | 25.5249 | 0.815492 | 39.7948 |
| 2024-acf-regionals-ohio-state | 5 | 6 | 14.8501 | 0.8 | 27.7731 |
| 2024-acf-regionals-rutgers | 11 | 11 | 28.0031 | 0.769934 | 33.3989 |
| 2024-acf-regionals-vanderbilt | 10 | 10 | 10.4741 | 0.975758 | 20.6999 |
| 2024-acf-winter-at-brandeis | 17 | 16 | 22.6081 | 0.960737 | 26.263 |
| 2024-acf-winter-at-central-florida | 8 | 10 | 22.3949 | 1 | 33.965 |
| 2024-acf-winter-at-clemson | 16 | 17 | 19.8928 | 0.908021 | 27.4253 |
| 2024-acf-winter-at-lehigh | 14 | 14 | 20.1409 | 0.981299 | 39.7954 |
| 2024-acf-winter-at-northwestern | 16 | 18 | 17.3967 | 0.931568 | 39.0989 |
| 2024-acf-winter-at-ohio-state | 15 | 17 | 25.0178 | 0.938126 | 37.2268 |
| 2024-acf-winter-at-online | 17 | 19 | 20.434 | 0.898835 | 32.4872 |
| 2024-acf-winter-at-oxford | 17 | 19 | 20.6011 | 0.828431 | 29.4686 |
| 2024-acf-winter-at-ubc | 5 | 6 | 18.555 | 0.7 | 43.8898 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 30.1229 | 0.885714 | 41.002 |

[Team PPG and absolute errors](csvs/bonus_team_ppg_leaderboard.csv); [game bonus margins](csvs/bonus_game_margin_predictions.csv).

### Bonus Distributions

Aggregate ability is part-weighted; synergy is response-weighted. Parameter plots describe fitted training parameters across entities, not posterior uncertainty intervals.

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png).

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png).

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25365 | 0.0218523 | 0.134294 | 0.889525 | 0.420214 |
| bonus_part_correctness | tier | fall | 8094 | 0.0244455 | 0.137028 | 0.882743 | 0.425453 |
| bonus_part_correctness | tier | nationals | 4125 | 0.0289122 | 0.137812 | 0.880494 | 0.433639 |
| bonus_part_correctness | tier | regionals | 5247 | 0.0328643 | 0.135943 | 0.888399 | 0.424287 |
| bonus_part_correctness | tier | winter | 7899 | 0.0190702 | 0.128559 | 0.897624 | 0.40513 |
| bonus_part_correctness | category | Current Events | 243 | 0.0460792 | 0.129857 | 0.895528 | 0.417232 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.0345926 | 0.145986 | 0.870435 | 0.453287 |
| bonus_part_correctness | category | Geography | 456 | 0.0417294 | 0.1327 | 0.886935 | 0.415387 |
| bonus_part_correctness | category | History | 4050 | 0.0202882 | 0.130719 | 0.894279 | 0.40995 |
| bonus_part_correctness | category | Literature | 4029 | 0.0250573 | 0.132987 | 0.890706 | 0.41681 |
| bonus_part_correctness | category | Mythology | 936 | 0.0454727 | 0.13043 | 0.893113 | 0.404103 |
| bonus_part_correctness | category | Other Academic | 255 | 0.0496656 | 0.105318 | 0.923964 | 0.356494 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0435383 | 0.149551 | 0.865049 | 0.453499 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.0747568 | 0.135205 | 0.892677 | 0.413892 |
| bonus_part_correctness | category | Religion | 1014 | 0.02457 | 0.128525 | 0.89685 | 0.408356 |
| bonus_part_correctness | category | Science | 4059 | 0.0207962 | 0.132673 | 0.890517 | 0.418401 |
| bonus_part_correctness | category | Social Science | 906 | 0.0372686 | 0.120232 | 0.909966 | 0.376809 |
| bonus_part_correctness | category | Unknown | 5247 | 0.0328643 | 0.135943 | 0.888399 | 0.424287 |
| bonus_part_correctness | difficulty | easy | 8455 | 0.027001 | 0.0708119 | 0.797778 | 0.250914 |
| bonus_part_correctness | difficulty | hard | 8455 | 0.0409361 | 0.122275 | 0.745254 | 0.398926 |
| bonus_part_correctness | difficulty | medium | 8455 | 0.0486897 | 0.209794 | 0.737754 | 0.610804 |
