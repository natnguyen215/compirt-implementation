# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/in_sample_2024nationals/baseline-cal/synergy-evaluation`
Result root: `results/compirt/in_sample/in_sample_2024nationals/baseline-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 60923.1 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 11158.1 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.677752 |
| mean_synergy_contribution | 1.33584 |
| median_synergy_contribution | 1.35952 |
| negative_synergy_fraction | 0.0406156 |
| positive_synergy_fraction | 0.958529 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.934904 |
| log_loss | 0.334292 |
| ece | 0.0452835 |
| part_accuracy | 0.857536 |
| exact_score_accuracy | 0.623913 |
| per_bonus_points_mae | 4.56497 |
| ppb_mae | 1.66133 |
| accuracy | 0.857536 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.646145 |
| log_loss | 0.559931 |
| ece | 0.0147429 |
| accuracy | 0.727708 |
| buzz_position_mae | 0.129554 |
| buzz_position_median_absolute_error | 0.118104 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 2.75839 | 0.480815 | 1.47984 | 1.9471 | 2.41983 | 2.77672 | 3.12919 | 3.46835 | 3.82373 |
| player | theta_1 | 189 | 0.742831 | 0.744788 | -0.690565 | -0.365068 | 0.219675 | 0.599156 | 1.32968 | 1.94274 | 2.52071 |
| player | theta_2 | 189 | -0.799103 | 0.637131 | -2.42912 | -1.93042 | -1.23364 | -0.772276 | -0.312472 | 0.16507 | 0.936882 |
| player | theta_3 | 189 | -0.733195 | 0.644159 | -2.17732 | -1.73982 | -1.29254 | -0.72422 | -0.251834 | 0.268818 | 0.982211 |
| player | theta_4 | 189 | -0.701602 | 0.611193 | -2.14303 | -1.74274 | -1.07068 | -0.697163 | -0.253708 | 0.287336 | 0.816818 |
| player | theta_5 | 189 | -0.603588 | 0.645334 | -2.37261 | -1.56538 | -1.08357 | -0.610804 | -0.201036 | 0.432641 | 1.10651 |
| player | theta_norm | 189 | 2.09582 | 0.589929 | 0.716473 | 1.20045 | 1.68097 | 2.10611 | 2.49856 | 3.03916 | 3.75259 |
| tossup | beta | 360 | 3.65796 | 0.420661 | 2.53194 | 3.01746 | 3.37169 | 3.66445 | 3.93229 | 4.34435 | 5.06871 |
| tossup | gamma | 360 | 43.9986 | 99.8907 | 5.89712 | 8.41011 | 11.5918 | 16.2763 | 31.6693 | 153.328 | 870.723 |
| tossup | mu | 360 | 0.719429 | 0.106754 | 0.411405 | 0.54373 | 0.648747 | 0.719143 | 0.790194 | 0.90238 | 0.984839 |
| tossup | alpha_1 | 360 | -0.710187 | 0.767196 | -2.45735 | -1.77104 | -1.28559 | -0.858004 | -0.0771281 | 0.595188 | 1.07985 |
| tossup | alpha_2 | 360 | 0.694372 | 0.660741 | -0.839586 | -0.338796 | 0.212023 | 0.692832 | 1.13109 | 1.78268 | 2.41841 |
| tossup | alpha_3 | 360 | 0.635213 | 0.733893 | -1.3379 | -0.521652 | 0.0760941 | 0.636213 | 1.14967 | 1.88457 | 2.81166 |
| tossup | alpha_4 | 360 | 0.640177 | 0.63598 | -1.27457 | -0.352658 | 0.234096 | 0.635283 | 1.06474 | 1.69544 | 2.37148 |
| tossup | alpha_5 | 360 | 0.5883 | 0.659534 | -0.772525 | -0.310782 | 0.150094 | 0.512598 | 0.886426 | 1.87195 | 3.35359 |
| tossup | alpha_norm | 360 | 2.08143 | 0.459037 | 0.851625 | 1.29958 | 1.76285 | 2.07856 | 2.41 | 2.76985 | 3.47239 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 1071 | 0.0214351 | 1.0702 | -2.01039 | -1.50449 | -1.00755 | 0.0458942 | 1.01344 | 1.63695 | 1.79062 |
| bonus_part | alpha_1 | 1071 | 1.03408 | 0.725068 | 0.371544 | 0.413786 | 0.487705 | 0.709117 | 1.34503 | 2.74927 | 3.23767 |
| bonus_part | alpha_2 | 1071 | 0.83298 | 0.301946 | 0.345419 | 0.447349 | 0.577142 | 0.794919 | 1.05545 | 1.32016 | 2.49654 |
| bonus_part | alpha_3 | 1071 | 0.821488 | 0.271704 | 0.344034 | 0.466673 | 0.59099 | 0.79289 | 1.01249 | 1.24828 | 2.29972 |
| bonus_part | alpha_4 | 1071 | 0.816003 | 0.283475 | 0.347175 | 0.470133 | 0.576114 | 0.753193 | 1.01418 | 1.25779 | 2.26985 |
| bonus_part | alpha_5 | 1071 | 0.8039 | 0.267076 | 0.368449 | 0.477213 | 0.600522 | 0.773348 | 0.955883 | 1.24576 | 2.65949 |
| bonus_part | alpha_norm | 1071 | 2.09987 | 0.427169 | 1.10536 | 1.47775 | 1.81292 | 2.07357 | 2.28777 | 3.02245 | 3.66905 |
| synergy_player | psi_1 | 189 | 0.102995 | 0.27832 | -0.60441 | -0.401617 | -0.0214867 | 0.0207118 | 0.364362 | 0.595593 | 0.666404 |
| synergy_player | psi_2 | 189 | -0.0509527 | 0.276962 | -0.875486 | -0.551428 | -0.0388488 | -0.00381781 | 0.0275952 | 0.464463 | 1.28676 |
| synergy_player | psi_3 | 189 | -0.00385287 | 0.30447 | -0.838597 | -0.574799 | -0.0517487 | 0.00131231 | 0.0721002 | 0.520813 | 0.665961 |
| synergy_player | psi_norm | 189 | 0.466274 | 0.203946 | 0.021878 | 0.0587619 | 0.384187 | 0.489125 | 0.599391 | 0.672939 | 1.29548 |
| synergy | synergy_score | 274 | 0.230931 | 0.180365 | -1.14677 | 2.02534e-05 | 0.132967 | 0.229808 | 0.3456 | 0.435727 | 0.797717 |
| synergy | synergy_contribution | 7017 | 1.33584 | 0.831204 | -1.37011 | 0.00204817 | 0.797442 | 1.35952 | 2.01684 | 2.5442 | 2.70433 |
