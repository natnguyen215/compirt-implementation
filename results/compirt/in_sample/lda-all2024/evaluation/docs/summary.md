# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/lda-all2024/evaluation`
Result root: `results/compirt/in_sample/lda-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 367033 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| pyramidal | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 68193.3 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |
| compositional | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.0255934 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.90667 |
| log_loss | 0.408108 |
| ece | 0.0729473 |
| part_accuracy | 0.81767 |
| exact_score_accuracy | 0.535415 |
| rounded_score_accuracy | 0.533257 |
| per_bonus_points_mae | 5.44135 |
| ppb_mae | 2.79818 |
| accuracy | 0.81767 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.665682 |
| log_loss | 0.608305 |
| ece | 0.176829 |
| accuracy | 0.680615 |
| buzz_position_mae | 0.15774 |
| buzz_position_median_absolute_error | 0.141937 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 5.11362 | 0.59978 | 2.74822 | 3.84686 | 4.86504 | 5.18074 | 5.50686 | 5.96088 | 6.70368 |
| player | theta_1 | 1455 | 0.155216 | 1.10647 | -1.78201 | -1.29866 | -0.786052 | 0.017418 | 0.905396 | 2.15403 | 4.02359 |
| player | theta_2 | 1455 | 0.0893024 | 0.965046 | -2.21571 | -1.30528 | -0.700171 | 0.0238175 | 0.767598 | 1.74709 | 2.96964 |
| player | theta_3 | 1455 | 0.100491 | 1.16227 | -2.14706 | -1.4608 | -0.862048 | -0.047515 | 0.925288 | 2.22454 | 3.7508 |
| player | theta_4 | 1455 | 0.0276561 | 0.90528 | -1.42039 | -0.943689 | -0.605935 | -0.245667 | 0.44789 | 1.91286 | 4.07813 |
| player | theta_5 | 1455 | 0.0342218 | 1.21975 | -2.14646 | -1.48373 | -0.930144 | -0.195912 | 0.771119 | 2.50316 | 4.44248 |
| player | theta_norm | 1455 | 2.26265 | 0.857199 | 0.468243 | 1.09994 | 1.68691 | 2.10578 | 2.71915 | 3.92878 | 6.13995 |
| tossup | beta_1 | 1260 | 0.930111 | 1.45421 | -3.88518 | -0.0520467 | 0.0183837 | 0.119449 | 1.3591 | 3.96518 | 4.65585 |
| tossup | beta_2 | 1260 | 1.24096 | 1.46594 | -3.186 | -0.027142 | 0.137098 | 0.505385 | 2.39501 | 4.08694 | 5.39042 |
| tossup | beta_3 | 1260 | 1.23128 | 1.46532 | -2.83397 | -0.0307021 | 0.090212 | 0.493404 | 2.41173 | 4.03237 | 5.1018 |
| tossup | beta_4 | 1260 | 0.333964 | 0.959155 | -0.729822 | -0.0742416 | -0.0172472 | 0.0246772 | 0.0997681 | 3.35616 | 4.66851 |
| tossup | beta_5 | 1260 | 1.22845 | 1.57755 | -1.94324 | -0.0324487 | 0.0690298 | 0.356715 | 2.4263 | 4.33582 | 5.13012 |
| tossup | gamma_1 | 1260 | 14.3548 | 53.6466 | 4.15166 | 4.58606 | 4.92957 | 5.22401 | 7.48021 | 35.4593 | 1434.83 |
| tossup | gamma_2 | 1260 | 31.956 | 150.222 | 3.33166 | 4.64701 | 5.04019 | 5.61722 | 11.7404 | 97.7588 | 2311.9 |
| tossup | gamma_3 | 1260 | 23.4074 | 102.587 | 3.04785 | 4.60169 | 5.04474 | 5.57464 | 11.8222 | 68.9981 | 1938.39 |
| tossup | gamma_4 | 1260 | 9.35826 | 39.7509 | 3.95347 | 4.53992 | 4.85166 | 5.08618 | 5.37084 | 12.7259 | 817.689 |
| tossup | gamma_5 | 1260 | 22.436 | 90.3102 | 3.08503 | 4.60377 | 5.03404 | 5.45659 | 10.1105 | 78.5399 | 1839.17 |
| tossup | mu_1 | 1260 | 0.526047 | 0.0931068 | 0.204488 | 0.441262 | 0.490323 | 0.502975 | 0.519882 | 0.746666 | 0.94939 |
| tossup | mu_2 | 1260 | 0.531461 | 0.097252 | 0.207469 | 0.428563 | 0.486839 | 0.503967 | 0.534721 | 0.742214 | 0.923458 |
| tossup | mu_3 | 1260 | 0.529686 | 0.0947527 | 0.159512 | 0.419321 | 0.48953 | 0.505402 | 0.538199 | 0.73643 | 0.933174 |
| tossup | mu_4 | 1260 | 0.509037 | 0.0543481 | 0.245441 | 0.472295 | 0.49068 | 0.500598 | 0.511045 | 0.588121 | 0.918101 |
| tossup | mu_5 | 1260 | 0.538609 | 0.10286 | 0.20109 | 0.44479 | 0.49042 | 0.504797 | 0.542917 | 0.771435 | 0.958113 |
| tossup | topic_weight_1 | 1260 | 0.221736 | 0.338273 | 0.00281902 | 0.00332106 | 0.00402274 | 0.0350853 | 0.258354 | 0.936399 | 0.983542 |
| tossup | topic_weight_2 | 1260 | 0.228052 | 0.223592 | 0.00533466 | 0.00650254 | 0.0525904 | 0.140319 | 0.358766 | 0.693386 | 0.938077 |
| tossup | topic_weight_3 | 1260 | 0.249632 | 0.274127 | 0.00486135 | 0.00589093 | 0.036681 | 0.129695 | 0.389331 | 0.83102 | 0.981573 |
| tossup | topic_weight_4 | 1260 | 0.0682778 | 0.184495 | 0.00109164 | 0.00126724 | 0.00141176 | 0.00162333 | 0.0239446 | 0.629021 | 0.948814 |
| tossup | topic_weight_5 | 1260 | 0.232302 | 0.267257 | 0.00418633 | 0.00536058 | 0.0248013 | 0.10832 | 0.37173 | 0.792905 | 0.977667 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
