# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/tfidf-multidim-replace-position-all2024/evaluation`
Result root: `results/compirt/in_sample/tfidf-multidim-replace-position-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 360157 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 67890.2 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.0125606 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.920995 |
| log_loss | 0.366105 |
| ece | 0.0388104 |
| part_accuracy | 0.838567 |
| exact_score_accuracy | 0.579068 |
| rounded_score_accuracy | 0.578821 |
| per_bonus_points_mae | 5.10018 |
| ppb_mae | 2.24734 |
| accuracy | 0.838567 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.704774 |
| log_loss | 0.56892 |
| ece | 0.124527 |
| accuracy | 0.720583 |
| buzz_position_mae | 0.129552 |
| buzz_position_median_absolute_error | 0.109297 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.920995 | 0.925582 | 0.00458725 | synergy |
| log_loss | 0.366105 | 0.35573 | -0.010375 | synergy |
| ece | 0.0388104 | 0.0375613 | -0.00124909 | synergy |
| accuracy | 0.838567 | 0.843602 | 0.00503518 | synergy |
| part_accuracy | 0.838567 | 0.843602 | 0.00503518 | synergy |
| exact_score_accuracy | 0.579068 | 0.591431 | 0.0123632 | synergy |
| rounded_score_accuracy | 0.578821 | 0.593544 | 0.0147234 | synergy |
| per_bonus_points_mae | 5.10018 | 4.85701 | -0.243174 | synergy |
| ppb_mae | 2.24734 | 1.94933 | -0.298014 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.53542 | 1.35925 | 0.698999 | 1.60278 | 3.9335 | 4.91371 | 5.48112 | 6.19371 | 7.21349 |
| player | theta_1 | 1455 | 0.000556082 | 0.731485 | -2.2664 | -1.38332 | -0.415256 | 0.0877224 | 0.529126 | 1.04282 | 1.5399 |
| player | theta_2 | 1455 | 0.00826044 | 0.708662 | -2.47728 | -1.27893 | -0.427695 | 0.12552 | 0.493253 | 1.03636 | 1.99511 |
| player | theta_3 | 1455 | 0.0561832 | 0.73119 | -2.37847 | -1.33692 | -0.404828 | 0.179418 | 0.577003 | 1.07897 | 1.90499 |
| player | theta_4 | 1455 | 0.0173132 | 0.729461 | -2.43698 | -1.31139 | -0.432005 | 0.139656 | 0.517627 | 1.05167 | 1.96161 |
| player | theta_5 | 1455 | -0.108763 | 0.727533 | -2.68713 | -1.48683 | -0.489245 | 0.00746671 | 0.391906 | 0.968048 | 1.75248 |
| player | theta_norm | 1455 | 1.51359 | 0.596804 | 0.362691 | 0.694864 | 1.06734 | 1.42405 | 1.89178 | 2.64066 | 3.81024 |
| tossup | beta_1 | 1260 | 0.793775 | 0.577617 | -1.42022 | 0.218841 | 0.37798 | 0.571739 | 1.14359 | 1.98322 | 2.68588 |
| tossup | beta_2 | 1260 | 0.697242 | 0.483999 | -2.24183 | 0.205397 | 0.382925 | 0.54106 | 0.846832 | 1.72035 | 2.6568 |
| tossup | beta_3 | 1260 | 0.73634 | 0.506872 | -1.4322 | 0.230095 | 0.396759 | 0.573531 | 0.933478 | 1.83731 | 3.05711 |
| tossup | beta_4 | 1260 | 0.716704 | 0.479372 | -0.320873 | 0.217359 | 0.393371 | 0.55818 | 0.904677 | 1.77687 | 2.49005 |
| tossup | beta_5 | 1260 | 0.835839 | 0.582963 | -0.965855 | 0.175905 | 0.398856 | 0.635049 | 1.2455 | 1.97674 | 2.77483 |
| tossup | gamma_1 | 1260 | 11.6107 | 55.2771 | 0.526305 | 3.66072 | 4.76374 | 5.31242 | 6.78494 | 23.871 | 1636.4 |
| tossup | gamma_2 | 1260 | 11.9011 | 68.2703 | 0.424808 | 2.97422 | 4.52603 | 5.09255 | 5.84284 | 18.5588 | 1530.67 |
| tossup | gamma_3 | 1260 | 10.5476 | 44.3779 | 0.536577 | 2.87737 | 4.4442 | 5.07432 | 5.93202 | 20.2334 | 1121.56 |
| tossup | gamma_4 | 1260 | 11.0212 | 64.8309 | 0.728847 | 3.0399 | 4.54312 | 5.13393 | 5.92026 | 17.4501 | 1936.12 |
| tossup | gamma_5 | 1260 | 13.8748 | 81.7708 | 0.703506 | 3.16561 | 4.54032 | 5.23948 | 6.43185 | 21.8149 | 2273.91 |
| tossup | mu_1 | 1260 | 0.514202 | 0.123056 | 0.138042 | 0.385979 | 0.447839 | 0.476838 | 0.543181 | 0.78839 | 0.968041 |
| tossup | mu_2 | 1260 | 0.508051 | 0.107896 | 0.153944 | 0.39232 | 0.451656 | 0.478929 | 0.525976 | 0.74119 | 0.979236 |
| tossup | mu_3 | 1260 | 0.51532 | 0.114157 | 0.172263 | 0.396357 | 0.452131 | 0.482796 | 0.54523 | 0.766137 | 0.980477 |
| tossup | mu_4 | 1260 | 0.506585 | 0.109678 | 0.16307 | 0.386692 | 0.450667 | 0.479994 | 0.528061 | 0.747324 | 0.976022 |
| tossup | mu_5 | 1260 | 0.534416 | 0.134996 | 0.202172 | 0.388185 | 0.444847 | 0.486179 | 0.602219 | 0.82137 | 0.987249 |
| tossup | alpha_1 | 1260 | 1.16815 | 0.917065 | 0.117772 | 0.244927 | 0.446523 | 0.807063 | 1.75845 | 2.97019 | 4.87407 |
| tossup | alpha_2 | 1260 | 0.973774 | 0.766722 | 0.074474 | 0.212829 | 0.421705 | 0.729541 | 1.31869 | 2.62651 | 4.80486 |
| tossup | alpha_3 | 1260 | 1.0372 | 0.812869 | 0.104765 | 0.211815 | 0.451258 | 0.780615 | 1.36983 | 2.75178 | 5.74316 |
| tossup | alpha_4 | 1260 | 1.02189 | 0.79995 | 0.0758975 | 0.208514 | 0.431531 | 0.793393 | 1.30995 | 2.66211 | 4.95114 |
| tossup | alpha_5 | 1260 | 1.37286 | 1.07404 | 0.093038 | 0.237831 | 0.563062 | 1.03393 | 1.91523 | 3.69099 | 5.98117 |
| tossup | alpha_norm | 1260 | 3.08953 | 0.808046 | 1.15248 | 1.91749 | 2.51567 | 2.98375 | 3.56555 | 4.49237 | 6.34541 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 1.26734 | 1.51284 | -2.22913 | -1.34827 | -0.0530279 | 1.56073 | 2.56479 | 3.31793 | 4.07328 |
| bonus_part | alpha_1 | 3768 | 0.672327 | 0.281598 | 0.222899 | 0.381113 | 0.467739 | 0.597151 | 0.820599 | 1.12739 | 2.98296 |
| bonus_part | alpha_2 | 3768 | 0.670505 | 0.289553 | 0.2249 | 0.36106 | 0.452643 | 0.606125 | 0.829943 | 1.11844 | 3.22136 |
| bonus_part | alpha_3 | 3768 | 0.640021 | 0.258743 | 0.228832 | 0.362399 | 0.436328 | 0.566291 | 0.800018 | 1.10803 | 2.37714 |
| bonus_part | alpha_4 | 3768 | 0.65076 | 0.261462 | 0.232542 | 0.366665 | 0.448904 | 0.584125 | 0.807651 | 1.09116 | 2.52649 |
| bonus_part | alpha_5 | 3768 | 0.707598 | 0.346066 | 0.246086 | 0.364885 | 0.471816 | 0.640691 | 0.842336 | 1.28401 | 3.8145 |
| bonus_part | alpha_norm | 3768 | 1.5527 | 0.492648 | 0.823786 | 0.90325 | 1.11777 | 1.49434 | 1.94385 | 2.32698 | 4.04166 |
