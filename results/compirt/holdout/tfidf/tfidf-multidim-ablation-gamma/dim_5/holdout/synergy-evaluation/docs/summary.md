# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_5/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_5`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 468044 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 85136.4 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.357205 |
| mean_synergy_contribution | -1.07802 |
| median_synergy_contribution | -1.04097 |
| negative_synergy_fraction | 0.910626 |
| positive_synergy_fraction | 0.0649916 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.926423 |
| log_loss | 0.35315 |
| ece | 0.0356766 |
| part_accuracy | 0.846131 |
| part_accuracy_macro_team | 0.848604 |
| part_accuracy_macro_game | 0.846621 |
| part_accuracy_macro_bonus | 0.854243 |
| exact_acc | 0.595478 |
| ppb_mae | 0.879324 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.675944 |
| log_loss | 0.596942 |
| ece | 0.137716 |
| accuracy | 0.704553 |
| buzz_position_mae | 0.134958 |
| buzz_position_median_absolute_error | 0.112798 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.89847 | 0.995337 | 1.09569 | 2.75848 | 4.45092 | 5.07741 | 5.57256 | 6.18618 | 7.09686 |
| player | theta_1 | 1755 | 0.166549 | 0.561197 | -1.81125 | -0.833674 | -0.182474 | 0.206765 | 0.552279 | 1.01183 | 2.04651 |
| player | theta_2 | 1755 | 0.182022 | 0.600647 | -2.22774 | -1.00052 | -0.169686 | 0.248751 | 0.625314 | 1.06191 | 1.53718 |
| player | theta_3 | 1755 | 0.0894155 | 0.608353 | -2.54018 | -1.01076 | -0.275719 | 0.131321 | 0.512031 | 1.01539 | 1.96352 |
| player | theta_4 | 1755 | 0.0658585 | 0.576327 | -2.00002 | -1.0206 | -0.259794 | 0.134708 | 0.4601 | 0.896594 | 1.69528 |
| player | theta_5 | 1755 | -0.113339 | 0.580707 | -2.46658 | -1.12398 | -0.479908 | -0.07608 | 0.291341 | 0.799173 | 1.47468 |
| player | theta_norm | 1755 | 1.26826 | 0.438048 | 0.223888 | 0.64214 | 0.958001 | 1.20458 | 1.52344 | 2.07881 | 2.92499 |
| tossup | beta_1 | 1350 | 0.610031 | 0.42468 | -1.47924 | 0.158736 | 0.366977 | 0.502531 | 0.736897 | 1.46919 | 2.90909 |
| tossup | beta_2 | 1350 | 0.852449 | 0.582509 | -2.92355 | 0.197308 | 0.416737 | 0.669836 | 1.2745 | 1.93396 | 2.98548 |
| tossup | beta_3 | 1350 | 0.73109 | 0.554386 | -2.00424 | 0.122306 | 0.382252 | 0.553904 | 0.96851 | 1.88929 | 3.07288 |
| tossup | beta_4 | 1350 | 0.699357 | 0.469582 | -1.82324 | 0.132576 | 0.407509 | 0.588038 | 0.902661 | 1.62723 | 2.71192 |
| tossup | beta_5 | 1350 | 0.790043 | 0.590866 | -2.33285 | 0.123521 | 0.381971 | 0.61027 | 1.15068 | 1.92225 | 3.91819 |
| tossup | gamma_1 | 1350 | 13.5696 | 81.0537 | 0.323393 | 3.05154 | 4.27552 | 4.85664 | 5.57911 | 20.9235 | 2034.04 |
| tossup | gamma_2 | 1350 | 22.1905 | 117.498 | 0.0538023 | 2.90238 | 4.38068 | 5.08896 | 7.07918 | 50.3899 | 2355.09 |
| tossup | gamma_3 | 1350 | 16.5562 | 86.7213 | 0.150738 | 3.02767 | 4.3024 | 4.96003 | 5.91158 | 33.0182 | 1708.23 |
| tossup | gamma_4 | 1350 | 14.1668 | 64.6793 | 0.128516 | 2.60385 | 4.04473 | 4.79141 | 5.88305 | 28.8317 | 1345.45 |
| tossup | gamma_5 | 1350 | 22.4302 | 105.202 | 0.675455 | 2.92195 | 4.30864 | 5.05104 | 6.67258 | 52.7922 | 1705.32 |
| tossup | mu_1 | 1350 | 0.484618 | 0.0945709 | 0.131465 | 0.372387 | 0.441429 | 0.468883 | 0.504079 | 0.659503 | 0.959764 |
| tossup | mu_2 | 1350 | 0.50713 | 0.119505 | 0.127115 | 0.353067 | 0.440473 | 0.481647 | 0.553741 | 0.745674 | 0.97581 |
| tossup | mu_3 | 1350 | 0.49647 | 0.109787 | 0.166435 | 0.367702 | 0.439527 | 0.473428 | 0.520722 | 0.728769 | 0.989282 |
| tossup | mu_4 | 1350 | 0.49769 | 0.110213 | 0.110919 | 0.364736 | 0.440422 | 0.476121 | 0.528777 | 0.726455 | 0.990518 |
| tossup | mu_5 | 1350 | 0.512146 | 0.132878 | 0.145136 | 0.36661 | 0.433737 | 0.47186 | 0.553461 | 0.803468 | 0.993115 |
| tossup | r_1 | 1350 | 0.856277 | 0.707029 | 0.0865621 | 0.207253 | 0.382156 | 0.622394 | 1.06761 | 2.30202 | 4.98257 |
| tossup | r_2 | 1350 | 1.33855 | 1.00268 | 0.0864317 | 0.256788 | 0.551856 | 0.986208 | 2.001 | 3.30951 | 4.90603 |
| tossup | r_3 | 1350 | 1.12444 | 0.957136 | 0.0510535 | 0.251341 | 0.478538 | 0.784183 | 1.36368 | 3.25264 | 5.37946 |
| tossup | r_4 | 1350 | 1.08761 | 0.802693 | 0.0602866 | 0.247638 | 0.51077 | 0.856157 | 1.44432 | 2.81874 | 6.58735 |
| tossup | r_5 | 1350 | 1.25186 | 0.961476 | 0.0682422 | 0.263052 | 0.551155 | 0.927788 | 1.6343 | 3.3787 | 4.92158 |
| tossup | r_norm | 1350 | 3.13236 | 0.845782 | 1.21662 | 1.83191 | 2.54757 | 3.07978 | 3.67165 | 4.59021 | 7.31516 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.424974 | 1.46684 | -2.79838 | -1.89221 | -0.854631 | 0.545832 | 1.64927 | 2.57889 | 4.04241 |
| bonus_part | alpha_1 | 4716 | 0.799075 | 0.365035 | 0.227859 | 0.415962 | 0.541964 | 0.717708 | 0.967446 | 1.40843 | 3.78945 |
| bonus_part | alpha_2 | 4716 | 0.800869 | 0.401169 | 0.204379 | 0.404055 | 0.52508 | 0.691098 | 0.976124 | 1.48749 | 4.33417 |
| bonus_part | alpha_3 | 4716 | 0.81881 | 0.380375 | 0.233852 | 0.431669 | 0.555844 | 0.741128 | 0.976946 | 1.45324 | 4.45934 |
| bonus_part | alpha_4 | 4716 | 0.77868 | 0.307403 | 0.263184 | 0.425894 | 0.548482 | 0.717028 | 0.932722 | 1.3265 | 3.06191 |
| bonus_part | alpha_5 | 4716 | 0.789508 | 0.337958 | 0.231419 | 0.436581 | 0.573611 | 0.736635 | 0.897169 | 1.3743 | 3.94455 |
| bonus_part | alpha_norm | 4716 | 1.86686 | 0.585127 | 0.930362 | 1.0814 | 1.40651 | 1.80101 | 2.26279 | 2.89387 | 4.61832 |
