# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/topic-tfidf-ablation/dim_3/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/topic-tfidf-ablation/dim_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 506620 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 3 |
| synergy | steps | 2000 |
| synergy | final_loss | 104787 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.621422 |
| mean_synergy_contribution | -0.120647 |
| median_synergy_contribution | -0.00856406 |
| negative_synergy_fraction | 0.557201 |
| positive_synergy_fraction | 0.418417 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.921409 |
| log_loss | 0.368059 |
| ece | 0.0483303 |
| part_accuracy | 0.842514 |
| exact_acc | 0.584279 |
| per_bonus_points_mae | 4.85682 |
| ppb_mae | 1.66948 |
| accuracy | 0.842514 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.64411 |
| log_loss | 0.58662 |
| ece | 0.128875 |
| accuracy | 0.706959 |
| buzz_position_mae | 0.146832 |
| buzz_position_median_absolute_error | 0.127735 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.54829 | 0.48903 | 3.09846 | 4.76867 | 5.23216 | 5.55841 | 5.86127 | 6.35379 | 7.31898 |
| player | theta_1 | 1755 | -1.13283 | 1.13229 | -4.09464 | -2.83231 | -1.98417 | -1.22264 | -0.308274 | 0.853565 | 2.09774 |
| player | theta_2 | 1755 | -1.08481 | 1.19092 | -3.53751 | -2.77141 | -2.03444 | -1.22084 | -0.309519 | 1.03404 | 3.06499 |
| player | theta_3 | 1755 | -1.22524 | 1.2896 | -4.0173 | -3.05919 | -2.18851 | -1.38857 | -0.420756 | 1.10294 | 3.23154 |
| player | theta_norm | 1755 | 2.69571 | 1.02762 | 0.268647 | 1.04769 | 1.90825 | 2.67996 | 3.46298 | 4.39529 | 5.63048 |
| tossup | beta_1 | 1350 | 1.26923 | 1.28836 | -2.18086 | -0.013191 | 0.191909 | 0.632849 | 2.46365 | 3.53347 | 5.43102 |
| tossup | beta_2 | 1350 | 0.859848 | 1.19914 | -3.81529 | -0.0755712 | 0.14663 | 0.323876 | 1.21619 | 3.33387 | 5.37858 |
| tossup | beta_3 | 1350 | 1.25465 | 1.41836 | -3.85236 | -0.105632 | 0.186834 | 0.548158 | 2.57147 | 3.85634 | 4.68749 |
| tossup | gamma_1 | 1350 | 42.4121 | 153.733 | 0.361578 | 4.04833 | 4.85426 | 5.31189 | 11.2399 | 208.115 | 2225.09 |
| tossup | gamma_2 | 1350 | 26.0183 | 114.957 | 0.392614 | 4.1923 | 4.81357 | 5.14871 | 5.84017 | 86.5444 | 1554.25 |
| tossup | gamma_3 | 1350 | 39.6662 | 146.116 | 0.140577 | 4.2132 | 4.83763 | 5.26948 | 10.8891 | 189.154 | 2036.44 |
| tossup | mu_1 | 1350 | 0.587218 | 0.152836 | 0.131889 | 0.444208 | 0.491561 | 0.51362 | 0.689435 | 0.892405 | 0.993541 |
| tossup | mu_2 | 1350 | 0.554396 | 0.132689 | 0.138563 | 0.459114 | 0.488737 | 0.506096 | 0.544364 | 0.867136 | 0.992343 |
| tossup | mu_3 | 1350 | 0.604355 | 0.171187 | 0.215849 | 0.453254 | 0.489836 | 0.51353 | 0.744356 | 0.944508 | 0.993728 |
| tossup | topic_weight_1 | 1350 | 0.368133 | 0.339503 | 0.00585086 | 0.0185861 | 0.0499302 | 0.220207 | 0.716875 | 0.919011 | 0.982087 |
| tossup | topic_weight_2 | 1350 | 0.263319 | 0.319723 | 0.00660645 | 0.0203874 | 0.0405847 | 0.0954119 | 0.353187 | 0.929644 | 0.981247 |
| tossup | topic_weight_3 | 1350 | 0.368548 | 0.350609 | 0.00800852 | 0.0235986 | 0.0559394 | 0.194795 | 0.75344 | 0.939485 | 0.985848 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 4716 | 0.00276748 | 1.25059 | -3.95067 | -2.31777 | -0.346962 | 0.0251355 | 0.401876 | 2.36938 | 3.72739 |
| bonus_part | beta_2 | 4716 | 0.0609842 | 0.937178 | -3.95057 | -1.66013 | -0.237253 | 0.0252562 | 0.265298 | 1.99502 | 3.9915 |
| bonus_part | beta_3 | 4716 | 0.0434663 | 0.978215 | -3.90404 | -1.7788 | -0.241144 | 0.0247171 | 0.287178 | 1.94272 | 3.96251 |
