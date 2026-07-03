# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/lda-all2024-cal/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/lda-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 459458 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| pyramidal | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 81671.3 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |
| synergy | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.711218 |
| mean_synergy_contribution | 0.102096 |
| median_synergy_contribution | 0.0481461 |
| negative_synergy_fraction | 0.363003 |
| positive_synergy_fraction | 0.612615 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.922076 |
| log_loss | 0.354969 |
| ece | 0.0145648 |
| part_accuracy | 0.842034 |
| exact_score_accuracy | 0.584246 |
| rounded_score_accuracy | 0.596834 |
| per_bonus_points_mae | 4.82956 |
| ppb_mae | 1.67569 |
| accuracy | 0.842034 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.597036 |
| log_loss | 0.527886 |
| ece | 0.00371094 |
| accuracy | 0.770337 |
| buzz_position_mae | 0.15253 |
| buzz_position_median_absolute_error | 0.135587 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 3.31638 | 0.645522 | 1.28402 | 2.23691 | 2.87896 | 3.31972 | 3.71559 | 4.43372 | 5.17599 |
| player | theta_1 | 1755 | -1.09037 | 0.88146 | -3.63913 | -2.26622 | -1.71161 | -1.24885 | -0.577449 | 0.613114 | 2.63313 |
| player | theta_2 | 1755 | -1.10408 | 0.485674 | -3.01891 | -1.81811 | -1.37163 | -1.144 | -0.884029 | -0.224194 | 1.12295 |
| player | theta_3 | 1755 | -1.30113 | 0.902252 | -3.93089 | -2.5736 | -1.9013 | -1.46259 | -0.756426 | 0.394856 | 1.81921 |
| player | theta_4 | 1755 | -0.477844 | 0.651531 | -2.53185 | -1.41875 | -0.800629 | -0.557392 | -0.260016 | 0.805412 | 3.2606 |
| player | theta_5 | 1755 | -1.35183 | 0.849268 | -3.69859 | -2.40898 | -1.87705 | -1.51913 | -0.995816 | 0.320305 | 2.65402 |
| player | theta_norm | 1755 | 2.97102 | 0.548438 | 0.619818 | 2.06218 | 2.6933 | 2.95398 | 3.24141 | 3.92409 | 5.45713 |
| tossup | beta_1 | 1350 | 1.10829 | 1.69177 | -0.129866 | -0.0438091 | 0.0334603 | 0.151312 | 1.33712 | 4.57763 | 5.92696 |
| tossup | beta_2 | 1350 | 1.4814 | 1.70212 | -1.49407 | -0.00709777 | 0.14263 | 0.626895 | 2.80779 | 4.80264 | 6.00188 |
| tossup | beta_3 | 1350 | 1.45289 | 1.70523 | -3.1238 | -0.0133231 | 0.116417 | 0.545889 | 2.84715 | 4.68482 | 5.76125 |
| tossup | beta_4 | 1350 | 0.474808 | 1.30118 | -0.195721 | -0.0710097 | -0.0152626 | 0.0321269 | 0.118083 | 4.58633 | 6.05168 |
| tossup | beta_5 | 1350 | 1.49678 | 1.81132 | -1.89257 | -0.0132785 | 0.105953 | 0.483013 | 3.05562 | 5.03313 | 6.20636 |
| tossup | gamma_1 | 1350 | 13.5991 | 61.9463 | 3.9897 | 4.5854 | 4.93126 | 5.24565 | 6.55302 | 25.0686 | 1178.14 |
| tossup | gamma_2 | 1350 | 26.1586 | 110.205 | 3.94072 | 4.68211 | 5.08426 | 5.66073 | 10.4119 | 82.0008 | 1763.39 |
| tossup | gamma_3 | 1350 | 23.8782 | 98.3284 | 2.98864 | 4.65791 | 5.02945 | 5.49748 | 10.1155 | 67.8516 | 1832.99 |
| tossup | gamma_4 | 1350 | 11.3391 | 64.3469 | 3.3649 | 4.51291 | 4.8111 | 5.0418 | 5.32604 | 13.4635 | 1715.91 |
| tossup | gamma_5 | 1350 | 22.5497 | 97.3776 | 3.49592 | 4.65071 | 5.02445 | 5.469 | 9.95513 | 65.6638 | 1705.78 |
| tossup | mu_1 | 1350 | 0.539656 | 0.0963544 | 0.238914 | 0.473601 | 0.493957 | 0.505396 | 0.525785 | 0.772696 | 0.985919 |
| tossup | mu_2 | 1350 | 0.560417 | 0.114097 | 0.194144 | 0.471757 | 0.494433 | 0.510531 | 0.59161 | 0.830769 | 0.993304 |
| tossup | mu_3 | 1350 | 0.544191 | 0.102136 | 0.156536 | 0.450365 | 0.494456 | 0.509503 | 0.568275 | 0.758671 | 0.973013 |
| tossup | mu_4 | 1350 | 0.523195 | 0.0812847 | 0.305455 | 0.479027 | 0.49233 | 0.502259 | 0.513126 | 0.767554 | 0.970181 |
| tossup | mu_5 | 1350 | 0.562259 | 0.117725 | 0.221413 | 0.46873 | 0.49436 | 0.509165 | 0.593037 | 0.817083 | 0.985308 |
| tossup | topic_weight_1 | 1350 | 0.218069 | 0.342105 | 0.00285499 | 0.00342265 | 0.00389982 | 0.0325199 | 0.212112 | 0.945478 | 0.984634 |
| tossup | topic_weight_2 | 1350 | 0.226277 | 0.240582 | 0.00512236 | 0.00639485 | 0.0377977 | 0.126754 | 0.352091 | 0.742052 | 0.956967 |
| tossup | topic_weight_3 | 1350 | 0.245531 | 0.288679 | 0.00479686 | 0.00593483 | 0.0242585 | 0.105729 | 0.406981 | 0.849477 | 0.983099 |
| tossup | topic_weight_4 | 1350 | 0.0702435 | 0.189705 | 0.00110557 | 0.00128605 | 0.00143514 | 0.00159348 | 0.0203562 | 0.635436 | 0.974287 |
| tossup | topic_weight_5 | 1350 | 0.23988 | 0.281031 | 0.0042974 | 0.00519295 | 0.0234817 | 0.103026 | 0.38706 | 0.830482 | 0.981875 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| synergy_player | psi_1 | 1755 | -0.00105243 | 0.2141 | -1.04521 | -0.350243 | -0.0450935 | -0.00186044 | 0.0412021 | 0.395142 | 0.917047 |
| synergy_player | psi_2 | 1755 | -0.00705306 | 0.188115 | -1.00484 | -0.319823 | -0.0477802 | -0.00285487 | 0.0379319 | 0.275086 | 1.06675 |
| synergy_player | psi_3 | 1755 | 0.00589137 | 0.203536 | -1.00647 | -0.332548 | -0.0369079 | 0.000769847 | 0.0399003 | 0.368641 | 1.12288 |
| synergy_player | psi_norm | 1755 | 0.278963 | 0.211834 | 0.0115404 | 0.0432983 | 0.106103 | 0.233212 | 0.382831 | 0.712082 | 1.12523 |
| synergy | synergy_score | 3042 | 0.00765557 | 0.13365 | -1.07 | -0.211076 | -0.0126721 | 0.00833702 | 0.0574016 | 0.185809 | 1.01493 |
| synergy | synergy_contribution | 60454 | 0.102096 | 0.340292 | -1.07719 | -0.442888 | -0.0940983 | 0.0481461 | 0.329888 | 0.70125 | 1.56327 |
