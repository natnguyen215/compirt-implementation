# Frozen Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.89906 |
| log_loss | 0.403038 |
| ece | 0.0206284 |
| brier | 0.128121 |
| part_accuracy | 0.819118 |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.300682 |
| part_accuracy_macro_team | 0.821057 |
| part_accuracy_macro_bonus | 0.817208 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.351266 |
| probability_p10 | 0.0523124 |
| probability_p50 | 0.550438 |
| probability_p90 | 0.965487 |
| mean_predictive_variance | 0.125661 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.532535 |
| ranked_probability_score | 0.111197 |
| bonus_total_score_log_loss | 0.983876 |
| ppb_mae | 1.81008 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25818 | 0.0206284 | 0.128121 | 0.89906 | 0.403038 |
| bonus_part_correctness | tier | fall | 8415 | 0.0207383 | 0.131734 | 0.891323 | 0.408953 |
| bonus_part_correctness | tier | nationals | 4179 | 0.0356751 | 0.124964 | 0.89945 | 0.398546 |
| bonus_part_correctness | tier | regionals | 5070 | 0.0163903 | 0.126943 | 0.900296 | 0.399362 |
| bonus_part_correctness | tier | winter | 8154 | 0.0244909 | 0.126744 | 0.900046 | 0.401522 |
| bonus_part_correctness | category | Current Events | 258 | 0.032997 | 0.104915 | 0.925841 | 0.351344 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.026903 | 0.13647 | 0.886313 | 0.42728 |
| bonus_part_correctness | category | Geography | 453 | 0.0363025 | 0.129328 | 0.893078 | 0.407916 |
| bonus_part_correctness | category | History | 4176 | 0.0238074 | 0.12937 | 0.896971 | 0.405105 |
| bonus_part_correctness | category | Literature | 4197 | 0.0317802 | 0.119355 | 0.911666 | 0.378862 |
| bonus_part_correctness | category | Mythology | 951 | 0.0336116 | 0.134732 | 0.885704 | 0.416148 |
| bonus_part_correctness | category | Other Academic | 258 | 0.040579 | 0.106555 | 0.929398 | 0.347663 |
| bonus_part_correctness | category | Philosophy | 969 | 0.0295438 | 0.135551 | 0.885996 | 0.424408 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.0793029 | 0.156375 | 0.858557 | 0.457741 |
| bonus_part_correctness | category | Religion | 1041 | 0.0372239 | 0.128194 | 0.899204 | 0.405979 |
| bonus_part_correctness | category | Science | 4152 | 0.0212006 | 0.128422 | 0.897459 | 0.405716 |
| bonus_part_correctness | category | Social Science | 915 | 0.0424881 | 0.127587 | 0.898591 | 0.401302 |
| bonus_part_correctness | category | Unknown | 5070 | 0.0163903 | 0.126943 | 0.900296 | 0.399362 |

## Distributions

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png). Aggregate ability is part-weighted; synergy is response-weighted.

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png) describe the training fit. These distributions are across entities, not posterior uncertainty intervals.

[Synergy parameters](graphs/parameters/synergy_parameter_distributions.png).
