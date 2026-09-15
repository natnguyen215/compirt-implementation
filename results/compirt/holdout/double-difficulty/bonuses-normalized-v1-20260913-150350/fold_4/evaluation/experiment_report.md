# Frozen Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.890772 |
| log_loss | 0.41746 |
| ece | 0.0194317 |
| brier | 0.133505 |
| part_accuracy | 0.807315 |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.28176 |
| part_accuracy_macro_team | 0.810707 |
| part_accuracy_macro_bonus | 0.803836 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.342949 |
| probability_p10 | 0.058817 |
| probability_p50 | 0.53765 |
| probability_p90 | 0.95696 |
| mean_predictive_variance | 0.131694 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.507423 |
| ranked_probability_score | 0.118782 |
| bonus_total_score_log_loss | 1.03777 |
| ppb_mae | 2.36623 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25866 | 0.0194317 | 0.133505 | 0.890772 | 0.41746 |
| bonus_part_correctness | tier | fall | 8259 | 0.02299 | 0.131843 | 0.890377 | 0.40979 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0341321 | 0.136874 | 0.883434 | 0.429654 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0192448 | 0.136457 | 0.885673 | 0.425965 |
| bonus_part_correctness | tier | winter | 7983 | 0.0222895 | 0.131448 | 0.893532 | 0.413215 |
| bonus_part_correctness | category | Current Events | 258 | 0.0584746 | 0.141069 | 0.879158 | 0.441516 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0274955 | 0.13741 | 0.884672 | 0.427765 |
| bonus_part_correctness | category | Geography | 450 | 0.0387929 | 0.134726 | 0.887973 | 0.418798 |
| bonus_part_correctness | category | History | 4116 | 0.0186395 | 0.129171 | 0.897088 | 0.403124 |
| bonus_part_correctness | category | Literature | 4092 | 0.0240094 | 0.131099 | 0.893481 | 0.41134 |
| bonus_part_correctness | category | Mythology | 951 | 0.0413948 | 0.131702 | 0.887362 | 0.412224 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0377107 | 0.121122 | 0.909824 | 0.385963 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0381827 | 0.14307 | 0.876437 | 0.448946 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0739397 | 0.133607 | 0.885875 | 0.404444 |
| bonus_part_correctness | category | Religion | 1029 | 0.0488255 | 0.129145 | 0.90009 | 0.401985 |
| bonus_part_correctness | category | Science | 4089 | 0.0269107 | 0.13509 | 0.88694 | 0.42506 |
| bonus_part_correctness | category | Social Science | 891 | 0.0512024 | 0.123751 | 0.903075 | 0.386256 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0192448 | 0.136457 | 0.885673 | 0.425965 |

## Distributions

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png). Aggregate ability is part-weighted; synergy is response-weighted.

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png) describe the training fit. These distributions are across entities, not posterior uncertainty intervals.
