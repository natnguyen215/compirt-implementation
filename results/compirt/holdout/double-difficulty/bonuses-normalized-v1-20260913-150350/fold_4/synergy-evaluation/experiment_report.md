# Frozen Bonus Evaluation

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.898912 |
| log_loss | 0.403292 |
| ece | 0.0187589 |
| brier | 0.127967 |
| part_accuracy | 0.817289 |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.291734 |
| part_accuracy_macro_team | 0.822807 |
| part_accuracy_macro_bonus | 0.814768 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.349698 |
| probability_p10 | 0.0535397 |
| probability_p50 | 0.548285 |
| probability_p90 | 0.965973 |
| mean_predictive_variance | 0.126791 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.531199 |
| ranked_probability_score | 0.112765 |
| bonus_total_score_log_loss | 0.998791 |
| ppb_mae | 1.66831 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25866 | 0.0187589 | 0.127967 | 0.898912 | 0.403292 |
| bonus_part_correctness | tier | fall | 8259 | 0.022272 | 0.128391 | 0.89617 | 0.401061 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0267761 | 0.12832 | 0.894982 | 0.408 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0127338 | 0.12798 | 0.898066 | 0.404715 |
| bonus_part_correctness | tier | winter | 7983 | 0.0241645 | 0.127335 | 0.899962 | 0.402169 |
| bonus_part_correctness | category | Current Events | 258 | 0.0407245 | 0.143278 | 0.880782 | 0.443796 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0336704 | 0.132744 | 0.892571 | 0.415179 |
| bonus_part_correctness | category | Geography | 450 | 0.0527151 | 0.129508 | 0.896723 | 0.406915 |
| bonus_part_correctness | category | History | 4116 | 0.023147 | 0.124252 | 0.904302 | 0.390626 |
| bonus_part_correctness | category | Literature | 4092 | 0.0232805 | 0.124153 | 0.903394 | 0.393505 |
| bonus_part_correctness | category | Mythology | 951 | 0.0358148 | 0.126211 | 0.894306 | 0.400006 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0371852 | 0.116663 | 0.912988 | 0.373314 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0376339 | 0.133537 | 0.891466 | 0.426181 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0724609 | 0.144322 | 0.875488 | 0.4299 |
| bonus_part_correctness | category | Religion | 1029 | 0.0480761 | 0.127207 | 0.901677 | 0.39939 |
| bonus_part_correctness | category | Science | 4089 | 0.0249129 | 0.131793 | 0.892953 | 0.415558 |
| bonus_part_correctness | category | Social Science | 891 | 0.0265515 | 0.118478 | 0.911851 | 0.371911 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0127338 | 0.12798 | 0.898066 | 0.404715 |

## Distributions

[Evaluated probabilities, aggregate ability, and synergy contributions](graphs/bonus/bonus_prediction_distributions.png). Aggregate ability is part-weighted; synergy is response-weighted.

[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png) describe the training fit. These distributions are across entities, not posterior uncertainty intervals.

[Synergy parameters](graphs/parameters/synergy_parameter_distributions.png).
