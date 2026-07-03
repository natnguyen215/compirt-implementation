# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/all-2024/evaluation`
Result root: `results/compirt/in_sample/all-2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 363404 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 65831.2 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.183888 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.93318 |
| log_loss | 0.341453 |
| ece | 0.0415155 |
| part_accuracy | 0.852301 |
| exact_score_accuracy | 0.611662 |
| rounded_score_accuracy | 0.60548 |
| per_bonus_points_mae | 4.82035 |
| ppb_mae | 2.17874 |
| accuracy | 0.852301 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.70368 |
| log_loss | 0.580392 |
| ece | 0.151482 |
| accuracy | 0.705931 |
| buzz_position_mae | 0.138836 |
| buzz_position_median_absolute_error | 0.121284 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.93318 | 0.939144 | 0.0059641 | synergy |
| log_loss | 0.341453 | 0.328479 | -0.0129744 | synergy |
| ece | 0.0415155 | 0.0447856 | 0.0032701 | no-synergy |
| accuracy | 0.852301 | 0.858693 | 0.00639138 | synergy |
| part_accuracy | 0.852301 | 0.858693 | 0.00639138 | synergy |
| exact_score_accuracy | 0.611662 | 0.626453 | 0.0147908 | synergy |
| rounded_score_accuracy | 0.60548 | 0.623823 | 0.0183424 | synergy |
| per_bonus_points_mae | 4.82035 | 4.5566 | -0.263754 | synergy |
| ppb_mae | 2.17874 | 1.76204 | -0.416696 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.72992 | 1.02899 | 1.57541 | 2.57268 | 4.23106 | 4.97025 | 5.44094 | 6.04183 | 7.15025 |
| player | theta_1 | 1455 | -0.0545043 | 0.719242 | -2.32128 | -1.26173 | -0.529482 | -0.0718292 | 0.405541 | 1.21023 | 1.98207 |
| player | theta_2 | 1455 | 0.0795811 | 0.803382 | -1.95569 | -1.20738 | -0.489937 | 0.0684209 | 0.678854 | 1.40364 | 2.32643 |
| player | theta_3 | 1455 | 0.148088 | 0.926453 | -2.43299 | -1.21126 | -0.509572 | 0.0306273 | 0.722188 | 1.85252 | 2.89459 |
| player | theta_4 | 1455 | -0.196893 | 0.79028 | -2.54469 | -1.50322 | -0.750458 | -0.216674 | 0.325337 | 1.18168 | 2.56392 |
| player | theta_5 | 1455 | -0.0406318 | 0.771597 | -2.42499 | -1.41855 | -0.558134 | 0.0273555 | 0.523706 | 1.10243 | 2.1991 |
| player | theta_norm | 1455 | 1.72393 | 0.581953 | 0.236211 | 0.85335 | 1.31673 | 1.68364 | 2.0749 | 2.7955 | 3.54924 |
| tossup | beta | 1260 | 3.36433 | 0.690971 | 0.359666 | 2.28217 | 3.01439 | 3.41161 | 3.81599 | 4.3591 | 5.6672 |
| tossup | gamma | 1260 | 51.7059 | 178.778 | 3.69829 | 5.78002 | 8.89318 | 12.7736 | 25.0612 | 184.919 | 2051.49 |
| tossup | mu | 1260 | 0.603548 | 0.13268 | 0.202009 | 0.380392 | 0.511996 | 0.606552 | 0.692687 | 0.822221 | 0.98497 |
| tossup | alpha_1 | 1260 | -0.0556313 | 0.681278 | -2.46043 | -1.25244 | -0.476471 | -0.0360728 | 0.413679 | 1.00069 | 1.84852 |
| tossup | alpha_2 | 1260 | 0.354686 | 0.694435 | -1.28203 | -0.654819 | -0.203213 | 0.312714 | 0.876656 | 1.55915 | 2.77204 |
| tossup | alpha_3 | 1260 | -0.718115 | 0.65347 | -2.92486 | -1.85909 | -1.12998 | -0.680847 | -0.263262 | 0.28993 | 1.00924 |
| tossup | alpha_4 | 1260 | 0.232635 | 0.820231 | -2.31936 | -1.13423 | -0.33354 | 0.281823 | 0.82049 | 1.50093 | 2.39967 |
| tossup | alpha_5 | 1260 | 0.532974 | 0.590031 | -1.12965 | -0.315651 | 0.102646 | 0.489631 | 0.911367 | 1.54232 | 2.71118 |
| tossup | alpha_norm | 1260 | 1.7793 | 0.457662 | 0.398203 | 1.05313 | 1.45173 | 1.77902 | 2.07571 | 2.59161 | 3.26752 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.846445 | 1.49612 | -2.257 | -1.73413 | -0.398158 | 1.11083 | 2.10794 | 2.89308 | 3.76075 |
| bonus_part | alpha_1 | 3768 | 0.0311628 | 0.459373 | -2.12255 | -0.756871 | -0.199739 | 0.0463085 | 0.274329 | 0.766523 | 2.07811 |
| bonus_part | alpha_2 | 3768 | 0.00624085 | 0.497824 | -2.07805 | -0.721839 | -0.293475 | -0.0602534 | 0.271604 | 0.900566 | 2.10467 |
| bonus_part | alpha_3 | 3768 | -0.21698 | 0.573222 | -2.25789 | -1.19948 | -0.593929 | -0.187305 | 0.169005 | 0.685942 | 1.69408 |
| bonus_part | alpha_4 | 3768 | 0.104333 | 0.561544 | -2.07559 | -0.842208 | -0.202448 | 0.108716 | 0.42975 | 1.02218 | 2.30413 |
| bonus_part | alpha_5 | 3768 | 0.121617 | 0.467947 | -1.73887 | -0.60411 | -0.195849 | 0.0974804 | 0.433573 | 0.925293 | 1.98041 |
| bonus_part | alpha_norm | 3768 | 1.0712 | 0.497739 | 0.102651 | 0.368398 | 0.695273 | 1.00067 | 1.37576 | 2.00209 | 2.97808 |
