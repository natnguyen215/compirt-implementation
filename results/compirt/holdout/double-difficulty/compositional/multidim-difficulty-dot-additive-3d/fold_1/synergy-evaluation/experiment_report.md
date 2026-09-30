# Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Bonus-Only Team PPG (recorded opportunities)

Team bonus totals are divided by games played, including zero-bonus games. MAE averages team PPG errors within tournaments, then weights tournaments equally; Spearman is also averaged across tournaments with defined correlations. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| tournament_team_bonus_ppg_mae | 15.9883 |
| tournament_team_bonus_ppg_spearman | 0.915778 |
| bonus_ppg_tournaments | 29 |
| bonus_ppg_spearman_tournaments | 29 |
| bonus_ppg_games | 462 |
| bonus_ppg_incomplete_games | 0 |

### Bonus-Only Game Margins (recorded opportunities)

For each complete game, subtract team B's bonus points from team A's. MAE compares predicted and observed signed margins, weighting games equally. Predictions use expected points on recorded bonus opportunities.

| metric | value |
| --- | --- |
| bonus_game_margin_mae | 25.1988 |
| bonus_game_margin_mae_games | 462 |

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.900227 |
| log_loss | 0.399993 |
| ece | 0.0112111 |
| brier | 0.126923 |
| part_accuracy | 0.820665 |
| part_accuracy_easy | 0.904988 |
| part_accuracy_medium | 0.715439 |
| part_accuracy_hard | 0.841568 |
| part_accuracy_unknown |  |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.301663 |
| part_accuracy_macro_team | 0.823514 |
| part_accuracy_macro_bonus | 0.819742 |
| part_count_easy | 8420 |
| part_count_medium | 8420 |
| part_count_hard | 8420 |
| part_count_unknown | 0 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.354493 |
| probability_p10 | 0.0459494 |
| probability_p50 | 0.504518 |
| probability_p90 | 0.985329 |
| mean_predictive_variance | 0.124021 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.541568 |
| ranked_probability_score | 0.108693 |
| bonus_total_score_log_loss | 0.963597 |
| ppb_mae | 1.72106 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

### Bonus-Only PPG by Tournament

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae |
| --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 8 | 9 | 18.5085 | 0.886243 | 32.5773 |
| 2024-acf-fall-at-cornell | 17 | 18 | 11.2113 | 0.968062 | 25.2255 |
| 2024-acf-fall-at-georgia | 21 | 23 | 12.7463 | 0.962963 | 24.6875 |
| 2024-acf-fall-at-illinois | 17 | 19 | 14.3383 | 0.896685 | 21.3231 |
| 2024-acf-fall-at-north-carolina | 18 | 22 | 12.2551 | 0.986061 | 23.6264 |
| 2024-acf-fall-at-ohio-state | 18 | 20 | 10.6889 | 0.981405 | 24.9228 |
| 2024-acf-fall-at-rutgers | 15 | 19 | 14.5833 | 0.957143 | 20.7124 |
| 2024-acf-fall-at-washington | 12 | 13 | 9.69529 | 0.91769 | 23.6811 |
| 2024-acf-nationals | 48 | 80 | 11.017 | 0.957074 | 22.3028 |
| 2024-acf-regionals-berkeley | 6 | 7 | 14.8403 | 0.942857 | 21.7161 |
| 2024-acf-regionals-cornell | 6 | 6 | 30.135 | 0.6 | 48.606 |
| 2024-acf-regionals-imperial | 15 | 18 | 14.7286 | 0.935714 | 27.4881 |
| 2024-acf-regionals-jmu | 19 | 23 | 10.2852 | 0.98552 | 19.3352 |
| 2024-acf-regionals-minnesota | 3 | 4 | 10.7552 | 0.5 | 16.4577 |
| 2024-acf-regionals-mit | 7 | 4 | 22.1122 | 1 | 26.974 |
| 2024-acf-regionals-nebraska | 11 | 13 | 19.2673 | 0.947611 | 43.5493 |
| 2024-acf-regionals-ohio-state | 7 | 5 | 20.2787 | 0.964286 | 20.7278 |
| 2024-acf-regionals-rutgers | 10 | 11 | 14.3092 | 0.987879 | 21.1172 |
| 2024-acf-regionals-vanderbilt | 10 | 9 | 21.3641 | 0.951515 | 33.0574 |
| 2024-acf-winter-at-brandeis | 16 | 16 | 15.6308 | 0.949228 | 21.5564 |
| 2024-acf-winter-at-central-florida | 9 | 10 | 15.3787 | 0.966667 | 14.6543 |
| 2024-acf-winter-at-clemson | 15 | 17 | 15.8103 | 0.97051 | 28.4434 |
| 2024-acf-winter-at-lehigh | 13 | 12 | 14.383 | 0.98487 | 16.1646 |
| 2024-acf-winter-at-northwestern | 17 | 18 | 13.0921 | 0.965686 | 21.5441 |
| 2024-acf-winter-at-ohio-state | 16 | 16 | 17.8048 | 0.915256 | 31.2464 |
| 2024-acf-winter-at-online | 15 | 20 | 14.1517 | 0.932143 | 26.149 |
| 2024-acf-winter-at-oxford | 17 | 19 | 16.6321 | 0.906749 | 34.3385 |
| 2024-acf-winter-at-ubc | 6 | 6 | 14.4088 | 1 | 16.9467 |
| 2024-acf-winter-at-uc-berkeley | 6 | 5 | 33.2487 | 0.637748 | 65.5128 |

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
| bonus_part_correctness | aggregate | all | 25260 | 0.0112111 | 0.126923 | 0.900227 | 0.399993 |
| bonus_part_correctness | tier | fall | 8160 | 0.0151761 | 0.127585 | 0.894869 | 0.401462 |
| bonus_part_correctness | tier | nationals | 4107 | 0.024514 | 0.122551 | 0.902513 | 0.389763 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0163457 | 0.129612 | 0.895553 | 0.40624 |
| bonus_part_correctness | tier | winter | 7713 | 0.0170202 | 0.126711 | 0.899779 | 0.399611 |
| bonus_part_correctness | category | Current Events | 249 | 0.0553365 | 0.120258 | 0.909091 | 0.390867 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0141544 | 0.139668 | 0.88148 | 0.432153 |
| bonus_part_correctness | category | Geography | 459 | 0.032937 | 0.135637 | 0.88163 | 0.416522 |
| bonus_part_correctness | category | History | 4017 | 0.0166668 | 0.123142 | 0.905394 | 0.388261 |
| bonus_part_correctness | category | Literature | 4047 | 0.0233502 | 0.119974 | 0.907792 | 0.389291 |
| bonus_part_correctness | category | Mythology | 924 | 0.0348684 | 0.145206 | 0.867098 | 0.443603 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0467583 | 0.116972 | 0.918271 | 0.371849 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0361872 | 0.128477 | 0.897107 | 0.408564 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.0602114 | 0.135429 | 0.880103 | 0.403754 |
| bonus_part_correctness | category | Religion | 984 | 0.0293441 | 0.124556 | 0.903747 | 0.397524 |
| bonus_part_correctness | category | Science | 3990 | 0.0132504 | 0.124467 | 0.904238 | 0.390855 |
| bonus_part_correctness | category | Social Science | 897 | 0.0182149 | 0.107969 | 0.924279 | 0.348512 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0163457 | 0.129612 | 0.895553 | 0.40624 |
| bonus_part_correctness | difficulty | easy | 8420 | 0.0280945 | 0.0756231 | 0.808705 | 0.262944 |
| bonus_part_correctness | difficulty | hard | 8420 | 0.0236409 | 0.114841 | 0.786227 | 0.373765 |
| bonus_part_correctness | difficulty | medium | 8420 | 0.02424 | 0.190306 | 0.782025 | 0.563271 |
