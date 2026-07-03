# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/baseline-all2024-ard/synergy-evaluation`
Result root: `results/compirt/in_sample/baseline-all2024-ard`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 63519.5 |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.136528 |
| mean_synergy_contribution | 0.027982 |
| median_synergy_contribution | 0 |
| negative_synergy_fraction | 0.487581 |
| positive_synergy_fraction | 0.482501 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.919847 |
| log_loss | 0.371453 |
| ece | 0.0437228 |
| part_accuracy | 0.836596 |
| exact_score_accuracy | 0.582305 |
| per_bonus_points_mae | 4.98756 |
| ppb_mae | 1.82668 |

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
| bonus_part | beta | 3768 | 0.212213 | 1.66874 | -3.0676 | -2.46419 | -1.26084 | 0.392435 | 1.63581 | 2.63875 | 3.8256 |
| bonus_part | alpha_1 | 3768 | 0.000129894 | 0.0508137 | -0.396754 | -0.0827486 | -0.0268331 | 0.00120941 | 0.0304072 | 0.0758835 | 0.29753 |
| bonus_part | alpha_2 | 3768 | 0.0062571 | 0.0642149 | -0.267266 | -0.0926631 | -0.0374593 | 0.00524538 | 0.0503443 | 0.108798 | 0.21547 |
| bonus_part | alpha_3 | 3768 | -0.00690727 | 0.0628131 | -0.28101 | -0.113143 | -0.0426975 | -0.00326256 | 0.0327518 | 0.0867709 | 0.340929 |
| bonus_part | alpha_4 | 3768 | 0.000277171 | 0.0496768 | -0.253726 | -0.0787052 | -0.027363 | 0.00154371 | 0.0292996 | 0.0746281 | 0.360065 |
| bonus_part | alpha_5 | 3768 | 0.0034337 | 0.0543882 | -0.222197 | -0.0813873 | -0.0282738 | 0.00165058 | 0.0320994 | 0.0954554 | 0.24916 |
| bonus_part | alpha_norm | 3768 | 0.113804 | 0.0567532 | 0.00818413 | 0.0474429 | 0.0751623 | 0.101282 | 0.136016 | 0.231985 | 0.460592 |
| synergy_player | psi_1 | 1486 | 0.00647146 | 0.309049 | -1.69106 | -0.503336 | -0.0514152 | 0.00235059 | 0.0678721 | 0.488099 | 1.36214 |
| synergy_player | psi_2 | 1486 | 0.00826586 | 0.284766 | -1.28749 | -0.418009 | -0.0537939 | -0.000203992 | 0.0504333 | 0.475143 | 2.00789 |
| synergy_player | psi_3 | 1486 | -0.00801548 | 0.263686 | -1.2962 | -0.423073 | -0.0476622 | 0.00145904 | 0.0498803 | 0.36056 | 1.42042 |
| synergy_player | psi_norm | 1486 | 0.389199 | 0.307783 | 0.0109241 | 0.0554859 | 0.161635 | 0.320093 | 0.503406 | 1.05804 | 2.10037 |
| synergy | synergy_score | 3015 | -0.0190332 | 0.235934 | -1.9688 | -0.458005 | -0.0420534 | 0.0104903 | 0.0844322 | 0.239614 | 1.16426 |
| synergy | synergy_contribution | 44487 | 0.027982 | 0.740954 | -2.47438 | -1.1539 | -0.454444 | 0 | 0.53244 | 1.27961 | 1.98994 |
