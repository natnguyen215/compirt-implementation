# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/in_sample_2024nationals/lda-cal/synergy-evaluation`
Result root: `results/compirt/in_sample/in_sample_2024nationals/lda-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 61875.8 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| pyramidal | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 10321.7 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |
| synergy | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.1079 |
| mean_synergy_contribution | 0.346234 |
| median_synergy_contribution | 0.372762 |
| negative_synergy_fraction | 0.0145361 |
| positive_synergy_fraction | 0.984609 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.92609 |
| log_loss | 0.346688 |
| ece | 0.0260322 |
| part_accuracy | 0.849936 |
| exact_score_accuracy | 0.601397 |
| per_bonus_points_mae | 4.65025 |
| ppb_mae | 1.64084 |
| accuracy | 0.849936 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.610943 |
| log_loss | 0.571378 |
| ece | 0.0140442 |
| accuracy | 0.727834 |
| buzz_position_mae | 0.157426 |
| buzz_position_median_absolute_error | 0.151374 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 4.0161 | 0.570755 | 2.45893 | 3.17669 | 3.62346 | 4.03053 | 4.34053 | 4.99332 | 5.99066 |
| player | theta_1 | 189 | -0.84296 | 0.973718 | -2.9084 | -2.1393 | -1.6407 | -0.904301 | -0.27318 | 0.865386 | 2.31912 |
| player | theta_2 | 189 | -1.19996 | 0.679104 | -2.5686 | -2.2061 | -1.77615 | -1.22873 | -0.774037 | 0.0100097 | 0.606059 |
| player | theta_3 | 189 | -1.13404 | 1.00868 | -3.38844 | -2.54024 | -1.85045 | -1.36107 | -0.488402 | 0.774387 | 1.1459 |
| player | theta_4 | 189 | -0.499705 | 0.888801 | -1.84584 | -1.49753 | -1.08358 | -0.735486 | -0.130342 | 1.28154 | 2.78633 |
| player | theta_5 | 189 | -1.16481 | 0.994502 | -2.84025 | -2.44987 | -1.94359 | -1.33412 | -0.61224 | 0.717764 | 1.4788 |
| player | theta_norm | 189 | 2.97278 | 0.625432 | 1.08805 | 1.98537 | 2.583 | 2.93465 | 3.37337 | 3.95038 | 4.77002 |
| tossup | beta_1 | 360 | 1.0239 | 1.50361 | -0.106649 | -0.0368309 | 0.0319588 | 0.156251 | 1.5261 | 3.90932 | 4.28235 |
| tossup | beta_2 | 360 | 1.3625 | 1.43394 | -0.0635188 | 0.00866624 | 0.223391 | 0.670872 | 2.49477 | 4.04655 | 4.65452 |
| tossup | beta_3 | 360 | 1.30501 | 1.50529 | -0.0801761 | -0.0115676 | 0.129917 | 0.535439 | 2.61753 | 4.09382 | 4.67414 |
| tossup | beta_4 | 360 | 0.393503 | 1.10009 | -0.1431 | -0.0670881 | -0.0142979 | 0.0333709 | 0.138144 | 3.98315 | 5.0112 |
| tossup | beta_5 | 360 | 1.25321 | 1.53869 | -0.0781261 | 0.00756707 | 0.128093 | 0.435277 | 2.11131 | 4.24715 | 4.71582 |
| tossup | gamma_1 | 360 | 13.5344 | 38.1039 | 4.20059 | 4.6173 | 4.97258 | 5.25445 | 8.35013 | 37.0777 | 472.533 |
| tossup | gamma_2 | 360 | 17.2068 | 40.0805 | 4.38098 | 4.74909 | 5.13682 | 5.86848 | 12.6379 | 57.5791 | 399.294 |
| tossup | gamma_3 | 360 | 16.1193 | 37.8174 | 4.36784 | 4.71213 | 5.08135 | 5.65483 | 12.1099 | 53.1428 | 382.355 |
| tossup | gamma_4 | 360 | 14.1085 | 106.303 | 4.1799 | 4.55073 | 4.84564 | 5.03366 | 5.30773 | 14.2709 | 1972.53 |
| tossup | gamma_5 | 360 | 14.699 | 33.8435 | 4.18082 | 4.7341 | 5.11669 | 5.48679 | 12.0108 | 52.5999 | 525.416 |
| tossup | mu_1 | 360 | 0.558523 | 0.111122 | 0.460559 | 0.479731 | 0.495377 | 0.508318 | 0.549407 | 0.819562 | 0.953619 |
| tossup | mu_2 | 360 | 0.570557 | 0.10439 | 0.401265 | 0.479805 | 0.501583 | 0.518347 | 0.632918 | 0.794038 | 0.906191 |
| tossup | mu_3 | 360 | 0.566802 | 0.102494 | 0.405584 | 0.483032 | 0.500009 | 0.515374 | 0.607076 | 0.788832 | 0.899026 |
| tossup | mu_4 | 360 | 0.522718 | 0.0783504 | 0.465825 | 0.478087 | 0.492764 | 0.502925 | 0.513874 | 0.725339 | 0.94657 |
| tossup | mu_5 | 360 | 0.568398 | 0.112629 | 0.460609 | 0.479985 | 0.496392 | 0.513771 | 0.607247 | 0.824192 | 0.929804 |
| tossup | topic_weight_1 | 360 | 0.223952 | 0.333494 | 0.00281902 | 0.00313496 | 0.00370607 | 0.0345403 | 0.26672 | 0.923587 | 0.983542 |
| tossup | topic_weight_2 | 360 | 0.240054 | 0.21258 | 0.00533466 | 0.00609217 | 0.0703108 | 0.164108 | 0.385038 | 0.658598 | 0.843227 |
| tossup | topic_weight_3 | 360 | 0.239308 | 0.25606 | 0.00486135 | 0.00553053 | 0.0397695 | 0.131536 | 0.403593 | 0.756245 | 0.92202 |
| tossup | topic_weight_4 | 360 | 0.0751751 | 0.202531 | 0.00109164 | 0.00121315 | 0.00134598 | 0.0014843 | 0.0297544 | 0.689082 | 0.948814 |
| tossup | topic_weight_5 | 360 | 0.221512 | 0.246693 | 0.00418633 | 0.00495095 | 0.0344891 | 0.113857 | 0.341132 | 0.743912 | 0.933887 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 1071 | 0.0446345 | 0.650211 | -2.28177 | -1.07536 | -0.0739315 | 0.00952849 | 0.101501 | 1.436 | 2.25657 |
| bonus_part | beta_2 | 1071 | -0.024064 | 0.693213 | -2.47724 | -1.43423 | -0.234295 | 0.0201374 | 0.254031 | 1.17293 | 1.78163 |
| bonus_part | beta_3 | 1071 | -0.00550527 | 0.727712 | -2.45477 | -1.46704 | -0.212376 | 0.0105061 | 0.250035 | 1.37561 | 2.00684 |
| bonus_part | beta_4 | 1071 | 0.0324059 | 0.344809 | -2.12975 | -0.204426 | -0.0387706 | 0.0021225 | 0.0489197 | 0.383452 | 2.23582 |
| bonus_part | beta_5 | 1071 | -0.0156508 | 0.614942 | -2.44401 | -1.33096 | -0.112496 | 0.0106591 | 0.133726 | 1.07819 | 1.98878 |
| synergy_player | psi_1 | 189 | -0.00693 | 0.152024 | -0.301756 | -0.277489 | -0.0622371 | 0.0007094 | 0.0421072 | 0.252227 | 0.510952 |
| synergy_player | psi_2 | 189 | -0.0320451 | 0.154153 | -0.449336 | -0.327438 | -0.0521433 | -0.00502643 | 0.030332 | 0.23291 | 0.347545 |
| synergy_player | psi_3 | 189 | -0.0264199 | 0.131199 | -0.450943 | -0.270306 | -0.0598499 | -0.00454778 | 0.0311106 | 0.210964 | 0.315597 |
| synergy_player | psi_norm | 189 | 0.237063 | 0.0968097 | 0.017087 | 0.0597366 | 0.186102 | 0.255542 | 0.291816 | 0.40491 | 0.514892 |
| synergy | synergy_score | 274 | 0.0584584 | 0.0438649 | -0.137722 | 0.00141198 | 0.0324733 | 0.0594158 | 0.0796372 | 0.121018 | 0.199082 |
| synergy | synergy_contribution | 7017 | 0.346234 | 0.192534 | -0.196689 | 0.0068089 | 0.217523 | 0.372762 | 0.479904 | 0.635526 | 0.678605 |
