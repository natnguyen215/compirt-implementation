# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/baseline-all2024-ard/evaluation`
Result root: `results/compirt/in_sample/baseline-all2024-ard`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 63388.2 |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.131418 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.907591 |
| log_loss | 0.398074 |
| ece | 0.0460006 |
| part_accuracy | 0.823402 |
| exact_score_accuracy | 0.549172 |
| per_bonus_points_mae | 5.53964 |
| ppb_mae | 2.82131 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.704075 |
| log_loss | 0.581126 |
| ece | 0.146344 |
| buzz_position_mae | 0.13897 |
| buzz_position_median_absolute_error | 0.121654 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1486 | 4.76023 | 1.0444 | 1.38397 | 2.64118 | 4.20395 | 5.01228 | 5.50442 | 6.0692 | 7.18595 |
| player | theta_1 | 1486 | 0.0609591 | 0.709922 | -2.32292 | -1.19272 | -0.401217 | 0.123312 | 0.530367 | 1.18513 | 1.99028 |
| player | theta_2 | 1486 | -0.0922024 | 1.09183 | -2.9583 | -2.33903 | -0.726063 | 0.148495 | 0.729697 | 1.3 | 2.176 |
| player | theta_3 | 1486 | 0.274468 | 0.851205 | -2.24831 | -1.08218 | -0.31917 | 0.176284 | 0.82121 | 1.82988 | 2.66596 |
| player | theta_4 | 1486 | -0.0720392 | 0.748792 | -2.15208 | -1.23433 | -0.597696 | -0.12618 | 0.420814 | 1.26833 | 2.43448 |
| player | theta_5 | 1486 | -0.11765 | 0.769849 | -2.38973 | -1.37935 | -0.678154 | -0.0427884 | 0.440462 | 1.10065 | 2.109 |
| player | theta_norm | 1486 | 1.80009 | 0.661924 | 0.233813 | 0.902261 | 1.33447 | 1.70168 | 2.14999 | 3.17367 | 3.67236 |
| tossup | beta | 1260 | 3.38914 | 0.691709 | 0.286505 | 2.36582 | 3.03817 | 3.41617 | 3.83497 | 4.40869 | 5.73258 |
| tossup | gamma | 1260 | 50.0248 | 171.742 | 3.68805 | 5.772 | 8.91508 | 12.7428 | 24.3807 | 185.668 | 2078.49 |
| tossup | mu | 1260 | 0.607038 | 0.132255 | 0.199963 | 0.389139 | 0.513516 | 0.611314 | 0.697239 | 0.821242 | 0.984271 |
| tossup | alpha_1 | 1260 | 0.0549814 | 0.669691 | -2.52144 | -1.10176 | -0.394417 | 0.102633 | 0.495297 | 1.06818 | 2.338 |
| tossup | alpha_2 | 1260 | 0.921445 | 0.649827 | -0.862903 | -0.21464 | 0.502115 | 0.924022 | 1.34848 | 1.99117 | 2.86858 |
| tossup | alpha_3 | 1260 | -0.677729 | 0.7086 | -2.89797 | -1.95444 | -1.17056 | -0.609122 | -0.165115 | 0.425405 | 1.20013 |
| tossup | alpha_4 | 1260 | 0.00406712 | 0.739064 | -2.54317 | -1.22696 | -0.493871 | 0.000514085 | 0.523852 | 1.19447 | 2.25058 |
| tossup | alpha_5 | 1260 | 0.220814 | 0.713121 | -1.96218 | -0.901176 | -0.220206 | 0.171901 | 0.638007 | 1.46726 | 2.77514 |
| tossup | alpha_norm | 1260 | 1.88588 | 0.479075 | 0.610813 | 1.08107 | 1.56465 | 1.87401 | 2.20863 | 2.68641 | 3.53121 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.320039 | 1.5833 | -2.80169 | -2.30526 | -1.02118 | 0.523697 | 1.66717 | 2.60196 | 3.46163 |
| bonus_part | alpha_1 | 3768 | -0.00728104 | 0.0645294 | -0.51612 | -0.113487 | -0.0381066 | -0.00269925 | 0.0279592 | 0.083184 | 0.344857 |
| bonus_part | alpha_2 | 3768 | 0.0364275 | 0.0699808 | -0.198539 | -0.0745453 | -0.0112135 | 0.034884 | 0.0794223 | 0.1597 | 0.350583 |
| bonus_part | alpha_3 | 3768 | -0.0755352 | 0.154298 | -0.792478 | -0.374018 | -0.147717 | -0.0514423 | 0.0286668 | 0.11771 | 0.399615 |
| bonus_part | alpha_4 | 3768 | -0.0062913 | 0.0711929 | -0.444116 | -0.127774 | -0.0387699 | -0.00129636 | 0.0339821 | 0.0924525 | 0.351434 |
| bonus_part | alpha_5 | 3768 | 0.0363293 | 0.117143 | -0.325558 | -0.11217 | -0.0348659 | 0.0162938 | 0.0797435 | 0.27239 | 0.630313 |
| bonus_part | alpha_norm | 3768 | 0.20231 | 0.138445 | 0.0186489 | 0.0631618 | 0.106835 | 0.155996 | 0.25626 | 0.498852 | 0.944035 |
