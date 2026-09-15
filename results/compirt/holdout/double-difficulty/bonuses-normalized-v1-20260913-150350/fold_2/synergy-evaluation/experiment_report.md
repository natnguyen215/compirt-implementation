# Frozen Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.896414 |
| log_loss | 0.407479 |
| ece | 0.0166293 |
| brier | 0.129425 |
| part_accuracy | 0.814431 |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.295064 |
| part_accuracy_macro_team | 0.816324 |
| part_accuracy_macro_bonus | 0.813061 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.352185 |
| probability_p10 | 0.0496652 |
| probability_p50 | 0.531951 |
| probability_p90 | 0.964646 |
| mean_predictive_variance | 0.125527 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.527277 |
| ranked_probability_score | 0.111169 |
| bonus_total_score_log_loss | 0.987443 |
| ppb_mae | 1.67884 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25791 | 0.0166293 | 0.129425 | 0.896414 | 0.407479 |
| bonus_part_correctness | tier | fall | 7995 | 0.0222194 | 0.125934 | 0.90039 | 0.392493 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0159406 | 0.128125 | 0.894513 | 0.405168 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0186198 | 0.129485 | 0.896184 | 0.407131 |
| bonus_part_correctness | tier | winter | 8121 | 0.023337 | 0.133475 | 0.889427 | 0.423636 |
| bonus_part_correctness | category | Current Events | 216 | 0.051059 | 0.112097 | 0.920362 | 0.357315 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0311537 | 0.139286 | 0.883047 | 0.431993 |
| bonus_part_correctness | category | Geography | 501 | 0.0603999 | 0.129502 | 0.896936 | 0.407947 |
| bonus_part_correctness | category | History | 4068 | 0.0233671 | 0.12699 | 0.900153 | 0.399832 |
| bonus_part_correctness | category | Literature | 4065 | 0.0256998 | 0.124437 | 0.902324 | 0.394393 |
| bonus_part_correctness | category | Mythology | 945 | 0.0342731 | 0.148939 | 0.862467 | 0.453348 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0862611 | 0.141249 | 0.884635 | 0.438818 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0290374 | 0.133469 | 0.886944 | 0.423742 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.083882 | 0.151831 | 0.862037 | 0.464835 |
| bonus_part_correctness | category | Religion | 1008 | 0.0307491 | 0.127954 | 0.899024 | 0.403457 |
| bonus_part_correctness | category | Science | 4059 | 0.0177748 | 0.127493 | 0.897487 | 0.406864 |
| bonus_part_correctness | category | Social Science | 909 | 0.0354675 | 0.109845 | 0.923222 | 0.350487 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0186198 | 0.129485 | 0.896184 | 0.407131 |

## Distributions

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png). Aggregate ability is part-weighted; synergy is response-weighted.

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png) describe the training fit. These distributions are across entities, not posterior uncertainty intervals.

[Synergy parameters](graphs/parameters/synergy_parameter_distributions.png).
