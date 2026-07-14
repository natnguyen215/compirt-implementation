# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/in_sample_2024nationals/baseline/synergy-evaluation`
Result root: `results/compirt/in_sample/in_sample_2024nationals/baseline`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 62696.5 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 11258.8 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.501185 |
| mean_synergy_contribution | -2.13455 |
| median_synergy_contribution | -2.17841 |
| negative_synergy_fraction | 0.999145 |
| positive_synergy_fraction | 0 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.939384 |
| log_loss | 0.340882 |
| ece | 0.0701651 |
| part_accuracy | 0.857014 |
| exact_score_accuracy | 0.622488 |
| per_bonus_points_mae | 4.52304 |
| ppb_mae | 1.90708 |
| accuracy | 0.857014 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.69748 |
| log_loss | 0.603793 |
| ece | 0.1436 |
| accuracy | 0.68262 |
| buzz_position_mae | 0.135971 |
| buzz_position_median_absolute_error | 0.124329 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 5.35645 | 0.475592 | 3.61701 | 4.60847 | 5.04222 | 5.35455 | 5.68096 | 6.09097 | 6.61872 |
| player | theta_1 | 189 | 0.057369 | 0.796168 | -1.6123 | -1.21115 | -0.613974 | 0.0467015 | 0.749235 | 1.17347 | 1.79404 |
| player | theta_2 | 189 | 0.0653808 | 0.73544 | -1.41121 | -1.14663 | -0.498737 | 0.104132 | 0.542198 | 1.30136 | 1.80048 |
| player | theta_3 | 189 | -0.0229333 | 0.541558 | -1.83327 | -0.941999 | -0.322423 | -0.0427148 | 0.353271 | 0.838995 | 1.39631 |
| player | theta_4 | 189 | 0.0635407 | 0.609032 | -1.49182 | -0.959312 | -0.306783 | -0.0047381 | 0.419428 | 1.10732 | 2.15001 |
| player | theta_5 | 189 | -0.0119344 | 0.58589 | -1.4488 | -0.939449 | -0.383743 | -0.00466747 | 0.351886 | 0.929618 | 1.66708 |
| player | theta_norm | 189 | 1.41878 | 0.413423 | 0.272131 | 0.707934 | 1.14429 | 1.39196 | 1.75344 | 2.06488 | 2.50408 |
| tossup | beta | 360 | 3.26184 | 0.437533 | 1.5977 | 2.51968 | 3.02643 | 3.28279 | 3.55749 | 3.96474 | 4.56626 |
| tossup | gamma | 360 | 45.9829 | 101.042 | 4.66029 | 7.74893 | 11.8197 | 17.0853 | 34.0421 | 197.675 | 961.66 |
| tossup | mu | 360 | 0.680081 | 0.105816 | 0.216299 | 0.514914 | 0.614759 | 0.674392 | 0.746978 | 0.861573 | 0.934658 |
| tossup | alpha_1 | 360 | 0.54643 | 0.722065 | -1.25782 | -0.628053 | 0.0314364 | 0.507123 | 1.09319 | 1.68772 | 2.71431 |
| tossup | alpha_2 | 360 | -0.364509 | 0.748972 | -2.50921 | -1.79204 | -0.856504 | -0.260128 | 0.214055 | 0.702581 | 1.07787 |
| tossup | alpha_3 | 360 | -0.24691 | 0.672211 | -2.25168 | -1.53258 | -0.689936 | -0.1638 | 0.216828 | 0.745599 | 1.23217 |
| tossup | alpha_4 | 360 | -0.277941 | 0.690048 | -2.68191 | -1.49917 | -0.696223 | -0.215676 | 0.182421 | 0.820715 | 1.56695 |
| tossup | alpha_5 | 360 | 0.273675 | 0.675108 | -1.44319 | -0.673003 | -0.149852 | 0.173365 | 0.600696 | 1.69766 | 3.63636 |
| tossup | alpha_norm | 360 | 1.7047 | 0.445421 | 0.633494 | 0.991884 | 1.41527 | 1.69482 | 1.98494 | 2.42151 | 3.84058 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 1071 | 0.177084 | 1.36016 | -2.49241 | -2.1024 | -0.942764 | 0.358746 | 1.40515 | 2.04633 | 2.23489 |
| bonus_part | alpha_1 | 1071 | 0.858763 | 0.409461 | 0.284183 | 0.450523 | 0.549581 | 0.713161 | 1.06845 | 1.64515 | 2.86497 |
| bonus_part | alpha_2 | 1071 | 0.801334 | 0.31816 | 0.335889 | 0.475539 | 0.572743 | 0.696721 | 0.94283 | 1.40143 | 3.06599 |
| bonus_part | alpha_3 | 1071 | 0.780621 | 0.193145 | 0.426122 | 0.561235 | 0.649908 | 0.739312 | 0.861093 | 1.16777 | 2.25916 |
| bonus_part | alpha_4 | 1071 | 0.791248 | 0.275578 | 0.359238 | 0.497686 | 0.575291 | 0.716319 | 0.939782 | 1.3314 | 2.40231 |
| bonus_part | alpha_5 | 1071 | 0.806904 | 0.282039 | 0.342817 | 0.500236 | 0.617185 | 0.734304 | 0.920638 | 1.32863 | 2.59591 |
| bonus_part | alpha_norm | 1071 | 1.87186 | 0.473017 | 1.19453 | 1.28763 | 1.45376 | 1.78546 | 2.24806 | 2.70003 | 3.44374 |
| synergy_player | psi_1 | 189 | 0.000523436 | 0.617271 | -1.74644 | -1.19732 | -0.0707519 | -0.00577136 | 0.225907 | 1.15298 | 1.64582 |
| synergy_player | psi_2 | 189 | -0.00131209 | 0.680748 | -1.65269 | -1.212 | -0.444155 | 0.00917576 | 0.313235 | 1.25055 | 1.69682 |
| synergy_player | psi_3 | 189 | -0.00522395 | 0.553768 | -1.34398 | -0.971734 | -0.263087 | -0.0112957 | 0.132486 | 1.0248 | 1.66741 |
| synergy_player | psi_norm | 189 | 0.983708 | 0.422257 | 0.0536928 | 0.384633 | 0.619837 | 0.951516 | 1.32801 | 1.67412 | 2.12379 |
| synergy | synergy_score | 274 | -0.384953 | 0.839775 | -3.25411 | -1.67193 | -1.01979 | -0.474526 | 0.306241 | 0.898364 | 1.46174 |
| synergy | synergy_contribution | 7017 | -2.13455 | 0.730263 | -3.85264 | -3.67865 | -2.54984 | -2.17841 | -1.64862 | -0.896888 | 0 |
