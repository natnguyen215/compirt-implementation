# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/learned-topic-tfidf-all2024-cal/synergy-evaluation`
Result root: `results/compirt/in_sample/learned-topic-tfidf-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 689428 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 221977 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.520619 |
| mean_synergy_contribution | 0.060315 |
| median_synergy_contribution | 0.00868576 |
| negative_synergy_fraction | 0.402342 |
| positive_synergy_fraction | 0.566255 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.921569 |
| log_loss | 0.356425 |
| ece | 0.0138302 |
| part_accuracy | 0.841152 |
| exact_acc | 0.582934 |
| per_bonus_points_mae | 4.81564 |
| ppb_mae | 1.72377 |
| accuracy | 0.841152 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.622335 |
| log_loss | 0.525161 |
| ece | 0.0041303 |
| accuracy | 0.767521 |
| buzz_position_mae | 0.143703 |
| buzz_position_median_absolute_error | 0.127082 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 3.79418 | 0.663878 | 1.3309 | 2.71378 | 3.36661 | 3.78232 | 4.19383 | 4.98901 | 5.73083 |
| player | theta_1 | 1455 | -1.24446 | 0.820396 | -3.04685 | -2.40925 | -1.82218 | -1.35476 | -0.829847 | 0.338552 | 2.37173 |
| player | theta_2 | 1455 | -0.763295 | 0.578188 | -2.68955 | -1.70727 | -1.11509 | -0.784554 | -0.426388 | 0.214141 | 1.23403 |
| player | theta_3 | 1455 | -0.903131 | 0.833684 | -3.27525 | -2.07462 | -1.4881 | -0.994308 | -0.428977 | 0.621447 | 2.41478 |
| player | theta_4 | 1455 | -0.749329 | 0.748126 | -3.15792 | -1.83286 | -1.23969 | -0.833824 | -0.330389 | 0.591304 | 1.86883 |
| player | theta_5 | 1455 | -0.555684 | 0.629326 | -2.44788 | -1.46095 | -0.946913 | -0.64431 | -0.247264 | 0.655066 | 2.37938 |
| player | theta_norm | 1455 | 2.48047 | 0.566585 | 0.657947 | 1.54617 | 2.11665 | 2.46102 | 2.84592 | 3.43599 | 4.52487 |
| tossup | beta_1 | 1260 | 1.60879 | 1.86472 | -0.133701 | 0.0490944 | 0.144043 | 0.339376 | 3.70349 | 4.82083 | 5.47648 |
| tossup | beta_2 | 1260 | 0.934431 | 1.47582 | -0.868796 | 0.0362557 | 0.113274 | 0.212747 | 0.654705 | 4.38439 | 5.10717 |
| tossup | beta_3 | 1260 | 1.08191 | 1.61918 | -2.20819 | 0.042014 | 0.111309 | 0.190072 | 1.04755 | 4.46272 | 5.50604 |
| tossup | beta_4 | 1260 | 0.908539 | 1.46138 | -0.261909 | 0.0358115 | 0.110185 | 0.194466 | 0.667332 | 4.47133 | 5.77737 |
| tossup | beta_5 | 1260 | 0.668184 | 1.31552 | -0.299386 | 0.0343719 | 0.10144 | 0.173236 | 0.292367 | 4.35016 | 5.53896 |
| tossup | gamma_1 | 1260 | 19.1365 | 83.6485 | 4.0423 | 4.62375 | 4.97242 | 5.33979 | 9.02463 | 45.2535 | 1769.74 |
| tossup | gamma_2 | 1260 | 12.8521 | 58.964 | 3.38524 | 4.58379 | 4.92756 | 5.16355 | 5.67095 | 24.4092 | 1418.8 |
| tossup | gamma_3 | 1260 | 13.9728 | 48.7594 | 4.06754 | 4.60482 | 4.92345 | 5.17939 | 5.84943 | 33.1024 | 812.945 |
| tossup | gamma_4 | 1260 | 10.6101 | 38.3985 | 3.48343 | 4.609 | 4.92053 | 5.17288 | 5.58607 | 19.0969 | 641.308 |
| tossup | gamma_5 | 1260 | 13.5579 | 89.6788 | 4.08093 | 4.60219 | 4.88269 | 5.10563 | 5.38121 | 14.2221 | 1779.24 |
| tossup | mu_1 | 1260 | 0.590487 | 0.143189 | 0.229595 | 0.480781 | 0.496333 | 0.51068 | 0.681032 | 0.88985 | 0.989381 |
| tossup | mu_2 | 1260 | 0.536135 | 0.0949336 | 0.2069 | 0.474258 | 0.493574 | 0.504359 | 0.520066 | 0.777829 | 0.982048 |
| tossup | mu_3 | 1260 | 0.55372 | 0.118436 | 0.284515 | 0.478603 | 0.494227 | 0.505105 | 0.524446 | 0.849267 | 0.986647 |
| tossup | mu_4 | 1260 | 0.533421 | 0.0888893 | 0.293945 | 0.476832 | 0.493572 | 0.504415 | 0.520773 | 0.760719 | 0.978049 |
| tossup | mu_5 | 1260 | 0.527537 | 0.0854831 | 0.219765 | 0.480324 | 0.493618 | 0.50337 | 0.513948 | 0.753778 | 0.984268 |
| tossup | topic_weight_1 | 1260 | 0.299163 | 0.362619 | 0.00673179 | 0.0114601 | 0.0180418 | 0.0441328 | 0.72057 | 0.913074 | 0.950207 |
| tossup | topic_weight_2 | 1260 | 0.164111 | 0.271779 | 0.0062023 | 0.0108593 | 0.0163891 | 0.0288472 | 0.109034 | 0.82942 | 0.931719 |
| tossup | topic_weight_3 | 1260 | 0.227096 | 0.353867 | 0.00822422 | 0.0108857 | 0.0159453 | 0.0256345 | 0.214188 | 0.940352 | 0.967892 |
| tossup | topic_weight_4 | 1260 | 0.185019 | 0.300394 | 0.00710157 | 0.012484 | 0.020544 | 0.0354284 | 0.130069 | 0.908196 | 0.955759 |
| tossup | topic_weight_5 | 1260 | 0.124611 | 0.250653 | 0.00909254 | 0.0128817 | 0.0194072 | 0.027279 | 0.0546986 | 0.908671 | 0.962701 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 3768 | -0.0349424 | 0.847467 | -3.08999 | -1.83575 | -0.216094 | -0.00441108 | 0.195776 | 1.51024 | 3.14353 |
| bonus_part | beta_2 | 3768 | -0.0232088 | 0.683424 | -2.83875 | -1.35215 | -0.185121 | 0.00623865 | 0.178667 | 1.14065 | 2.72802 |
| bonus_part | beta_3 | 3768 | 0.0270795 | 0.749338 | -2.90933 | -1.40785 | -0.153961 | 0.00177218 | 0.154439 | 1.537 | 3.11912 |
| bonus_part | beta_4 | 3768 | 0.00892836 | 0.657137 | -2.83154 | -1.15972 | -0.15129 | 0.0085143 | 0.152545 | 1.12563 | 3.08094 |
| bonus_part | beta_5 | 3768 | 0.0289353 | 0.512601 | -2.67132 | -0.558576 | -0.12741 | 0.0168969 | 0.149431 | 0.750479 | 2.81537 |
