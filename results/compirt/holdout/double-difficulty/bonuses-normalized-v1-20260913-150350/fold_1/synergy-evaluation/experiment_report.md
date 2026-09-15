# Frozen Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.899831 |
| log_loss | 0.401246 |
| ece | 0.0172029 |
| brier | 0.127255 |
| part_accuracy | 0.818606 |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.299604 |
| part_accuracy_macro_team | 0.821936 |
| part_accuracy_macro_bonus | 0.81682 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.350947 |
| probability_p10 | 0.0525036 |
| probability_p50 | 0.543052 |
| probability_p90 | 0.964078 |
| mean_predictive_variance | 0.126142 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.534679 |
| ranked_probability_score | 0.10907 |
| bonus_total_score_log_loss | 0.968068 |
| ppb_mae | 1.76101 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25260 | 0.0172029 | 0.127255 | 0.899831 | 0.401246 |
| bonus_part_correctness | tier | fall | 8160 | 0.015114 | 0.127851 | 0.894265 | 0.401984 |
| bonus_part_correctness | tier | nationals | 4107 | 0.0346544 | 0.122966 | 0.902587 | 0.392414 |
| bonus_part_correctness | tier | regionals | 5280 | 0.0226261 | 0.13138 | 0.893531 | 0.411894 |
| bonus_part_correctness | tier | winter | 7713 | 0.02383 | 0.126084 | 0.901206 | 0.39788 |
| bonus_part_correctness | category | Current Events | 249 | 0.0451625 | 0.123349 | 0.903732 | 0.396085 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.0222558 | 0.139049 | 0.88247 | 0.432226 |
| bonus_part_correctness | category | Geography | 459 | 0.0182585 | 0.135083 | 0.881388 | 0.418266 |
| bonus_part_correctness | category | History | 4017 | 0.0222262 | 0.123697 | 0.905099 | 0.389486 |
| bonus_part_correctness | category | Literature | 4047 | 0.0182228 | 0.120212 | 0.908217 | 0.385154 |
| bonus_part_correctness | category | Mythology | 924 | 0.0343074 | 0.143515 | 0.869974 | 0.441613 |
| bonus_part_correctness | category | Other Academic | 237 | 0.0613119 | 0.120847 | 0.913707 | 0.388672 |
| bonus_part_correctness | category | Philosophy | 948 | 0.0383651 | 0.12853 | 0.896235 | 0.408115 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.046092 | 0.130003 | 0.88568 | 0.401495 |
| bonus_part_correctness | category | Religion | 984 | 0.0193114 | 0.123738 | 0.904252 | 0.39498 |
| bonus_part_correctness | category | Science | 3990 | 0.0195673 | 0.124617 | 0.903547 | 0.394477 |
| bonus_part_correctness | category | Social Science | 897 | 0.0371585 | 0.107474 | 0.924861 | 0.346612 |
| bonus_part_correctness | category | Unknown | 5280 | 0.0226261 | 0.13138 | 0.893531 | 0.411894 |

## Distributions

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png). Aggregate ability is part-weighted; synergy is response-weighted.

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png) describe the training fit. These distributions are across entities, not posterior uncertainty intervals.

[Synergy parameters](graphs/parameters/synergy_parameter_distributions.png).
