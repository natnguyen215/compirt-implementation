# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/plda-all2024-cal/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/plda-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 467347 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| pyramidal | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 83934.9 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |
| synergy | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.650441 |
| mean_synergy_contribution | 0.126091 |
| median_synergy_contribution | 0.0730799 |
| negative_synergy_fraction | 0.366957 |
| positive_synergy_fraction | 0.608661 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.918793 |
| log_loss | 0.362169 |
| ece | 0.0157777 |
| part_accuracy | 0.837849 |
| exact_score_accuracy | 0.574106 |
| rounded_score_accuracy | 0.58461 |
| per_bonus_points_mae | 4.93264 |
| ppb_mae | 1.69586 |
| accuracy | 0.837849 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.589869 |
| log_loss | 0.529554 |
| ece | 0.00411149 |
| accuracy | 0.770337 |
| buzz_position_mae | 0.156792 |
| buzz_position_median_absolute_error | 0.140265 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 3.43898 | 0.652937 | 1.46355 | 2.38469 | 2.99898 | 3.42618 | 3.83761 | 4.56314 | 5.3179 |
| player | theta_1 | 1755 | -1.06148 | 0.498542 | -2.86891 | -1.73084 | -1.32703 | -1.13663 | -0.853561 | -0.144366 | 1.47105 |
| player | theta_2 | 1755 | -1.07675 | 0.582648 | -3.1436 | -1.99759 | -1.38191 | -1.11509 | -0.815312 | -0.0128561 | 1.64454 |
| player | theta_3 | 1755 | -1.10581 | 0.885438 | -3.70818 | -2.28674 | -1.69363 | -1.27255 | -0.61803 | 0.562193 | 2.7302 |
| player | theta_4 | 1755 | -1.29613 | 0.792731 | -3.42554 | -2.32823 | -1.78233 | -1.45234 | -0.929696 | 0.236607 | 2.84052 |
| player | theta_5 | 1755 | -0.905994 | 0.61973 | -3.47699 | -1.81925 | -1.21052 | -0.968947 | -0.655577 | 0.261158 | 1.66514 |
| player | theta_norm | 1755 | 2.84712 | 0.535655 | 0.693646 | 2.02971 | 2.5803 | 2.80066 | 3.08864 | 3.83056 | 5.42424 |
| tossup | beta_1 | 1350 | 1.35811 | 1.55474 | -0.91976 | -0.00727669 | 0.111562 | 0.623633 | 2.38149 | 4.58643 | 5.78036 |
| tossup | beta_2 | 1350 | 1.53774 | 1.6907 | -0.825968 | -0.00762353 | 0.121597 | 0.689123 | 2.98019 | 4.73354 | 5.97885 |
| tossup | beta_3 | 1350 | 1.26798 | 1.70822 | -0.241558 | -0.0291925 | 0.0503233 | 0.258086 | 2.30513 | 4.62857 | 5.83743 |
| tossup | beta_4 | 1350 | 1.60335 | 1.80095 | -1.92681 | -0.0118542 | 0.0881504 | 0.648303 | 3.24107 | 4.94469 | 6.34997 |
| tossup | beta_5 | 1350 | 1.00615 | 1.43555 | -0.549529 | -0.0245 | 0.0540174 | 0.259314 | 1.38029 | 4.39782 | 5.59991 |
| tossup | gamma_1 | 1350 | 25.3498 | 106.647 | 3.75847 | 4.65176 | 5.06979 | 5.6075 | 10.2289 | 61.9652 | 1906.23 |
| tossup | gamma_2 | 1350 | 28.5316 | 105.59 | 4.3364 | 4.6809 | 5.09905 | 5.6945 | 12.097 | 98.3653 | 1633 |
| tossup | gamma_3 | 1350 | 19.8788 | 101.71 | 3.52849 | 4.61464 | 4.95545 | 5.32926 | 8.52527 | 38.9327 | 1859.27 |
| tossup | gamma_4 | 1350 | 26.0314 | 98.526 | 4.10896 | 4.64437 | 5.03471 | 5.68161 | 12.1867 | 78.5347 | 1767.82 |
| tossup | gamma_5 | 1350 | 17.5516 | 78.4781 | 4.21415 | 4.63964 | 4.95181 | 5.28672 | 7.43938 | 39.6975 | 1782.53 |
| tossup | mu_1 | 1350 | 0.557653 | 0.110323 | 0.227416 | 0.467796 | 0.495452 | 0.511615 | 0.590576 | 0.809208 | 0.98547 |
| tossup | mu_2 | 1350 | 0.557637 | 0.1123 | 0.15176 | 0.458929 | 0.49467 | 0.512146 | 0.600415 | 0.797976 | 0.993138 |
| tossup | mu_3 | 1350 | 0.545117 | 0.0988637 | 0.245853 | 0.471715 | 0.494026 | 0.507082 | 0.55649 | 0.776148 | 0.985513 |
| tossup | mu_4 | 1350 | 0.570222 | 0.122901 | 0.233309 | 0.467798 | 0.495403 | 0.512711 | 0.627408 | 0.833792 | 0.982989 |
| tossup | mu_5 | 1350 | 0.533139 | 0.0855411 | 0.217745 | 0.471291 | 0.49258 | 0.506072 | 0.531603 | 0.732769 | 0.93555 |
| tossup | topic_weight_1 | 1350 | 0.193366 | 0.214386 | 0.00403773 | 0.00600104 | 0.0238805 | 0.118032 | 0.287111 | 0.673767 | 0.968847 |
| tossup | topic_weight_2 | 1350 | 0.213074 | 0.225166 | 0.00428213 | 0.00675765 | 0.0260513 | 0.126268 | 0.33058 | 0.686117 | 0.947785 |
| tossup | topic_weight_3 | 1350 | 0.217725 | 0.311051 | 0.00283386 | 0.00374078 | 0.00673389 | 0.0488541 | 0.285499 | 0.90438 | 0.981274 |
| tossup | topic_weight_4 | 1350 | 0.23566 | 0.26665 | 0.00368735 | 0.00544153 | 0.0167964 | 0.117151 | 0.392932 | 0.790912 | 0.977032 |
| tossup | topic_weight_5 | 1350 | 0.140175 | 0.187266 | 0.00311917 | 0.00436076 | 0.00834852 | 0.0536184 | 0.195212 | 0.564457 | 0.966084 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| synergy_player | psi_1 | 1755 | 0.00198577 | 0.197987 | -0.946453 | -0.327511 | -0.0394646 | 0.00038812 | 0.0438508 | 0.359683 | 1.08042 |
| synergy_player | psi_2 | 1755 | 0.00524334 | 0.213975 | -1.13332 | -0.382615 | -0.0428345 | 0.00271714 | 0.0484443 | 0.386712 | 1.0637 |
| synergy_player | psi_3 | 1755 | 0.000841058 | 0.186321 | -0.956878 | -0.32729 | -0.0368751 | 0.000195518 | 0.0431715 | 0.289159 | 0.845693 |
| synergy_player | psi_norm | 1755 | 0.27864 | 0.205055 | 0.00619244 | 0.0437141 | 0.11151 | 0.235069 | 0.388612 | 0.690634 | 1.13405 |
| synergy | synergy_score | 3042 | 0.0104545 | 0.130316 | -0.997754 | -0.213226 | -0.012982 | 0.00943104 | 0.0602315 | 0.180384 | 0.899509 |
| synergy | synergy_contribution | 60454 | 0.126091 | 0.337751 | -1.03505 | -0.432475 | -0.069867 | 0.0730799 | 0.354328 | 0.689514 | 1.54707 |
