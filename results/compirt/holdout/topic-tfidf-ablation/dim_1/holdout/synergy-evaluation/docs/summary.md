# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/topic-tfidf-ablation/dim_1/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/topic-tfidf-ablation/dim_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 513069 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 1 |
| synergy | steps | 2000 |
| synergy | final_loss | 101872 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.269698 |
| mean_synergy_contribution | 0.0713172 |
| median_synergy_contribution | 0.000371004 |
| negative_synergy_fraction | 0.469812 |
| positive_synergy_fraction | 0.505806 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.9155 |
| log_loss | 0.375409 |
| ece | 0.0355007 |
| part_accuracy | 0.834298 |
| exact_acc | 0.566546 |
| per_bonus_points_mae | 5.07541 |
| ppb_mae | 1.72026 |
| accuracy | 0.834298 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.617574 |
| log_loss | 0.629712 |
| ece | 0.160556 |
| accuracy | 0.678116 |
| buzz_position_mae | 0.152026 |
| buzz_position_median_absolute_error | 0.133908 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.37071 | 0.827961 | 1.92049 | 3.72737 | 4.95369 | 5.47177 | 5.92166 | 6.51774 | 7.55356 |
| player | theta_1 | 1755 | -1.34811 | 1.46854 | -6.28277 | -4.12311 | -2.07556 | -1.20455 | -0.31333 | 0.714075 | 1.88006 |
| player | theta_norm | 1755 | 1.53058 | 1.27712 | 0.000551784 | 0.103928 | 0.563578 | 1.23854 | 2.07556 | 4.12311 | 6.28277 |
| tossup | beta_1 | 1350 | 2.36196 | 0.795751 | -1.48052 | 0.999969 | 1.88151 | 2.4474 | 2.93175 | 3.49305 | 4.17887 |
| tossup | gamma_1 | 1350 | 84.0966 | 216.111 | 0.248135 | 2.40615 | 5.67651 | 11.1815 | 41.6588 | 494.871 | 2092.09 |
| tossup | mu_1 | 1350 | 0.72944 | 0.182925 | 0.112703 | 0.386683 | 0.612388 | 0.765245 | 0.871238 | 0.966541 | 0.994101 |
| tossup | topic_weight_1 | 1350 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 4716 | 0.0558097 | 1.70438 | -3.93194 | -2.75951 | -1.41655 | 0.182613 | 1.47537 | 2.65215 | 3.58544 |
