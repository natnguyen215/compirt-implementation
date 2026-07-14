# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/in_sample_2024nationals/plda-cal/synergy-evaluation`
Result root: `results/compirt/in_sample/in_sample_2024nationals/plda-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 62821 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| pyramidal | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 10455.5 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |
| synergy | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.96404 |
| mean_synergy_contribution | 0.354965 |
| median_synergy_contribution | 0.393494 |
| negative_synergy_fraction | 0.0145361 |
| positive_synergy_fraction | 0.984609 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.924768 |
| log_loss | 0.349892 |
| ece | 0.0276531 |
| part_accuracy | 0.849176 |
| exact_score_accuracy | 0.598974 |
| per_bonus_points_mae | 4.67515 |
| ppb_mae | 1.6494 |
| accuracy | 0.849176 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.617915 |
| log_loss | 0.570207 |
| ece | 0.0209683 |
| accuracy | 0.728086 |
| buzz_position_mae | 0.164806 |
| buzz_position_median_absolute_error | 0.16027 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 4.14266 | 0.577253 | 2.61817 | 3.25384 | 3.75824 | 4.1442 | 4.46415 | 5.11166 | 6.15658 |
| player | theta_1 | 189 | -1.04718 | 0.721389 | -2.42402 | -2.08905 | -1.58319 | -1.13776 | -0.588914 | 0.332036 | 0.763046 |
| player | theta_2 | 189 | -1.09266 | 0.819651 | -3.02619 | -2.26839 | -1.6877 | -1.20217 | -0.64568 | 0.432793 | 1.24735 |
| player | theta_3 | 189 | -0.83825 | 1.01959 | -2.74056 | -2.28896 | -1.65052 | -0.869575 | -0.231234 | 1.01159 | 2.51416 |
| player | theta_4 | 189 | -1.14053 | 0.951259 | -2.90962 | -2.40925 | -1.88792 | -1.32647 | -0.566568 | 0.638692 | 1.34491 |
| player | theta_5 | 189 | -0.962589 | 0.826503 | -2.87155 | -2.28422 | -1.51012 | -1.00076 | -0.501936 | 0.525878 | 1.33129 |
| player | theta_norm | 189 | 2.94173 | 0.606884 | 1.29947 | 1.95986 | 2.54764 | 2.95748 | 3.33871 | 3.93053 | 4.51399 |
| tossup | beta_1 | 360 | 1.14714 | 1.28189 | -0.116708 | -0.00335376 | 0.140908 | 0.622324 | 1.7962 | 3.88758 | 4.73657 |
| tossup | beta_2 | 360 | 1.29524 | 1.42928 | -0.083886 | -0.0142828 | 0.108602 | 0.609169 | 2.54573 | 3.93627 | 4.80546 |
| tossup | beta_3 | 360 | 1.1341 | 1.53681 | -0.0992233 | -0.0429294 | 0.043798 | 0.201467 | 2.92085 | 3.87452 | 4.14845 |
| tossup | beta_4 | 360 | 1.27881 | 1.51008 | -0.120915 | -0.0149472 | 0.0735991 | 0.488883 | 2.5435 | 4.10961 | 4.79489 |
| tossup | beta_5 | 360 | 0.940505 | 1.27019 | -0.0803452 | -0.0253083 | 0.0626213 | 0.339473 | 1.17171 | 3.84528 | 4.61935 |
| tossup | gamma_1 | 360 | 14.9853 | 36.6338 | 4.34511 | 4.7671 | 5.18906 | 5.91931 | 10.6219 | 48.0651 | 496.181 |
| tossup | gamma_2 | 360 | 17.0894 | 36.6375 | 4.35152 | 4.62217 | 5.1142 | 5.90075 | 13.7238 | 63.1773 | 405.377 |
| tossup | gamma_3 | 360 | 14.6997 | 36.0474 | 4.20451 | 4.59925 | 4.98772 | 5.3155 | 10.2703 | 43.4798 | 422.262 |
| tossup | gamma_4 | 360 | 15.1946 | 32.0471 | 4.119 | 4.68311 | 5.06125 | 5.65782 | 14.4535 | 51.86 | 476.196 |
| tossup | gamma_5 | 360 | 11.6923 | 24.6776 | 4.23155 | 4.63233 | 4.99577 | 5.46151 | 7.58763 | 38.4311 | 316.446 |
| tossup | mu_1 | 360 | 0.563271 | 0.102 | 0.459039 | 0.480033 | 0.498514 | 0.517154 | 0.592339 | 0.79622 | 0.916765 |
| tossup | mu_2 | 360 | 0.56973 | 0.104844 | 0.395191 | 0.480908 | 0.49672 | 0.515257 | 0.630711 | 0.788328 | 0.898317 |
| tossup | mu_3 | 360 | 0.565482 | 0.114012 | 0.4637 | 0.482048 | 0.494658 | 0.510007 | 0.598985 | 0.82271 | 0.95059 |
| tossup | mu_4 | 360 | 0.573944 | 0.109898 | 0.448948 | 0.485113 | 0.500112 | 0.517649 | 0.629732 | 0.813286 | 0.92809 |
| tossup | mu_5 | 360 | 0.548874 | 0.0879704 | 0.446033 | 0.479014 | 0.497378 | 0.511402 | 0.55824 | 0.747069 | 0.881129 |
| tossup | topic_weight_1 | 360 | 0.201924 | 0.199241 | 0.00392111 | 0.00586507 | 0.0406952 | 0.152056 | 0.291651 | 0.628855 | 0.926751 |
| tossup | topic_weight_2 | 360 | 0.206319 | 0.198213 | 0.00398982 | 0.00581619 | 0.0327229 | 0.141286 | 0.322207 | 0.599221 | 0.84832 |
| tossup | topic_weight_3 | 360 | 0.22347 | 0.312012 | 0.0027962 | 0.00332675 | 0.00522799 | 0.0446618 | 0.397554 | 0.879803 | 0.981607 |
| tossup | topic_weight_4 | 360 | 0.211833 | 0.233617 | 0.0036341 | 0.00481661 | 0.0143924 | 0.113861 | 0.351439 | 0.696429 | 0.953908 |
| tossup | topic_weight_5 | 360 | 0.156453 | 0.186828 | 0.00295113 | 0.00396609 | 0.0090372 | 0.0813912 | 0.223781 | 0.597685 | 0.854723 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 1071 | -0.00597522 | 0.55338 | -2.2528 | -1.05609 | -0.132462 | 0.0122992 | 0.165075 | 0.872291 | 1.94287 |
| bonus_part | beta_2 | 1071 | 0.00984588 | 0.699494 | -2.33858 | -1.34707 | -0.227672 | 0.014836 | 0.293825 | 1.24453 | 1.98377 |
| bonus_part | beta_3 | 1071 | 0.0491744 | 0.678382 | -2.35424 | -1.1315 | -0.092454 | 0.00648544 | 0.141332 | 1.44524 | 2.25308 |
| bonus_part | beta_4 | 1071 | -0.0137072 | 0.580429 | -2.44437 | -1.15032 | -0.0925452 | 0.00441134 | 0.116592 | 0.985599 | 2.01904 |
| bonus_part | beta_5 | 1071 | 0.0134599 | 0.642188 | -2.3312 | -1.25978 | -0.131641 | 0.0229613 | 0.199841 | 1.15612 | 2.00562 |
| synergy_player | psi_1 | 189 | -0.0152902 | 0.160071 | -0.398046 | -0.293582 | -0.0840974 | -0.00522157 | 0.0386194 | 0.302035 | 0.424473 |
| synergy_player | psi_2 | 189 | 0.00244453 | 0.122122 | -0.327327 | -0.25318 | -0.0368459 | 0.000757198 | 0.0369475 | 0.249579 | 0.350662 |
| synergy_player | psi_3 | 189 | 0.0180308 | 0.158332 | -0.31943 | -0.271243 | -0.0315417 | 0.00992824 | 0.0552774 | 0.30214 | 0.337798 |
| synergy_player | psi_norm | 189 | 0.24385 | 0.0799637 | 0.0213929 | 0.104751 | 0.201989 | 0.258354 | 0.294319 | 0.375923 | 0.429864 |
| synergy | synergy_score | 274 | 0.0603059 | 0.0362864 | -0.0651048 | 0.00268641 | 0.0367262 | 0.0637224 | 0.0802585 | 0.114532 | 0.181546 |
| synergy | synergy_contribution | 7017 | 0.354965 | 0.164415 | -0.0836051 | 0.0121421 | 0.236308 | 0.393494 | 0.47001 | 0.573301 | 0.657287 |
