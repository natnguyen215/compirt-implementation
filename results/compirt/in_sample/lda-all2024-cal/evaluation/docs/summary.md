# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/lda-all2024-cal/evaluation`
Result root: `results/compirt/in_sample/lda-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 354403 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| pyramidal | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 59645.2 |
| compositional | calibrate_correctness | True |
| compositional | synergy_dimensions | 0 |
| compositional | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.57996 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.910794 |
| log_loss | 0.378086 |
| ece | 0.00953195 |
| part_accuracy | 0.828167 |
| exact_score_accuracy | 0.555039 |
| rounded_score_accuracy | 0.563446 |
| per_bonus_points_mae | 5.16652 |
| ppb_mae | 2.33561 |
| accuracy | 0.828167 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.632096 |
| log_loss | 0.522508 |
| ece | 0.0125672 |
| accuracy | 0.767771 |
| buzz_position_mae | 0.152394 |
| buzz_position_median_absolute_error | 0.137647 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 3.52728 | 0.66089 | 1.21486 | 2.47292 | 3.10774 | 3.504 | 3.93164 | 4.67525 | 5.54692 |
| player | theta_1 | 1455 | -0.76127 | 0.830406 | -3.30164 | -1.92588 | -1.33827 | -0.852471 | -0.284953 | 0.787367 | 2.59357 |
| player | theta_2 | 1455 | -0.968001 | 0.557104 | -2.58833 | -1.86662 | -1.34139 | -0.983535 | -0.612254 | -0.0239254 | 1.0578 |
| player | theta_3 | 1455 | -1.0097 | 0.84196 | -3.64373 | -2.28339 | -1.55951 | -1.11044 | -0.525751 | 0.541115 | 1.79237 |
| player | theta_4 | 1455 | -0.356883 | 0.686774 | -2.08999 | -1.32237 | -0.77807 | -0.439721 | -0.0771235 | 1.0664 | 2.81654 |
| player | theta_5 | 1455 | -1.00587 | 0.850451 | -3.08981 | -2.18927 | -1.5522 | -1.12718 | -0.595479 | 0.685196 | 2.7825 |
| player | theta_norm | 1455 | 2.48776 | 0.623123 | 0.807368 | 1.52655 | 2.08463 | 2.43773 | 2.88139 | 3.62229 | 4.93551 |
| tossup | beta_1 | 1260 | 1.1466 | 1.70924 | -1.97164 | -0.039614 | 0.0364074 | 0.161466 | 1.82741 | 4.63789 | 5.41979 |
| tossup | beta_2 | 1260 | 1.52755 | 1.66852 | -0.622107 | -0.00109586 | 0.214318 | 0.698046 | 2.88608 | 4.6975 | 5.65924 |
| tossup | beta_3 | 1260 | 1.5098 | 1.66551 | -0.834277 | -0.00279414 | 0.156696 | 0.692741 | 2.98526 | 4.64627 | 5.5851 |
| tossup | beta_4 | 1260 | 0.450822 | 1.2571 | -0.154456 | -0.0657904 | -0.0114671 | 0.0331119 | 0.133239 | 4.565 | 5.89902 |
| tossup | beta_5 | 1260 | 1.50574 | 1.81603 | -0.484523 | -0.0134922 | 0.110941 | 0.530761 | 3.04125 | 5.00312 | 5.77292 |
| tossup | gamma_1 | 1260 | 13.2792 | 58.0826 | 3.80029 | 4.55767 | 4.93671 | 5.25375 | 7.01951 | 31.3761 | 1636.85 |
| tossup | gamma_2 | 1260 | 21.859 | 100.723 | 3.93605 | 4.68436 | 5.09759 | 5.66464 | 10.7017 | 52.9753 | 1949.55 |
| tossup | gamma_3 | 1260 | 15.1799 | 39.0057 | 3.55561 | 4.6871 | 5.09944 | 5.64889 | 10.4696 | 45.1081 | 574.484 |
| tossup | gamma_4 | 1260 | 9.85166 | 71.5872 | 4.01989 | 4.57284 | 4.83253 | 5.05808 | 5.31988 | 10.4048 | 1843.74 |
| tossup | gamma_5 | 1260 | 17.9186 | 67.6252 | 3.66358 | 4.64373 | 5.02735 | 5.46913 | 9.63049 | 55.5546 | 1468.08 |
| tossup | mu_1 | 1260 | 0.546208 | 0.10536 | 0.298438 | 0.473915 | 0.493434 | 0.506084 | 0.529871 | 0.807396 | 0.976152 |
| tossup | mu_2 | 1260 | 0.563109 | 0.114288 | 0.213188 | 0.472299 | 0.495676 | 0.512433 | 0.603689 | 0.820407 | 0.976713 |
| tossup | mu_3 | 1260 | 0.552302 | 0.104666 | 0.206798 | 0.462817 | 0.493517 | 0.511628 | 0.585455 | 0.786948 | 0.953983 |
| tossup | mu_4 | 1260 | 0.51957 | 0.0731509 | 0.262948 | 0.477263 | 0.492455 | 0.502692 | 0.512858 | 0.699637 | 0.966283 |
| tossup | mu_5 | 1260 | 0.566179 | 0.118877 | 0.203581 | 0.476357 | 0.496466 | 0.511072 | 0.602642 | 0.838829 | 0.983876 |
| tossup | topic_weight_1 | 1260 | 0.221736 | 0.338273 | 0.00281902 | 0.00332106 | 0.00402274 | 0.0350853 | 0.258354 | 0.936399 | 0.983542 |
| tossup | topic_weight_2 | 1260 | 0.228052 | 0.223592 | 0.00533466 | 0.00650254 | 0.0525904 | 0.140319 | 0.358766 | 0.693386 | 0.938077 |
| tossup | topic_weight_3 | 1260 | 0.249632 | 0.274127 | 0.00486135 | 0.00589093 | 0.036681 | 0.129695 | 0.389331 | 0.83102 | 0.981573 |
| tossup | topic_weight_4 | 1260 | 0.0682778 | 0.184495 | 0.00109164 | 0.00126724 | 0.00141176 | 0.00162333 | 0.0239446 | 0.629021 | 0.948814 |
| tossup | topic_weight_5 | 1260 | 0.232302 | 0.267257 | 0.00418633 | 0.00536058 | 0.0248013 | 0.10832 | 0.37173 | 0.792905 | 0.977667 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
