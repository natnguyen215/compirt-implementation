# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/tfidf-replace-position-all2024/evaluation`
Result root: `results/compirt/in_sample/tfidf-replace-position-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 363805 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 69516 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.106058 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.918031 |
| log_loss | 0.367085 |
| ece | 0.026544 |
| part_accuracy | 0.836094 |
| exact_score_accuracy | 0.576056 |
| rounded_score_accuracy | 0.572235 |
| per_bonus_points_mae | 5.14453 |
| ppb_mae | 2.49301 |
| accuracy | 0.836094 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.703265 |
| log_loss | 0.577832 |
| ece | 0.149347 |
| accuracy | 0.706787 |
| buzz_position_mae | 0.139117 |
| buzz_position_median_absolute_error | 0.121778 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.918031 | 0.930324 | 0.0122923 | synergy |
| log_loss | 0.367085 | 0.343419 | -0.023666 | synergy |
| ece | 0.026544 | 0.034373 | 0.00782896 | no-synergy |
| accuracy | 0.836094 | 0.849956 | 0.0138617 | synergy |
| part_accuracy | 0.836094 | 0.849956 | 0.0138617 | synergy |
| exact_score_accuracy | 0.576056 | 0.606155 | 0.0300987 | synergy |
| rounded_score_accuracy | 0.572235 | 0.604042 | 0.031807 | synergy |
| per_bonus_points_mae | 5.14453 | 4.74466 | -0.399866 | synergy |
| ppb_mae | 2.49301 | 1.82214 | -0.67087 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.76617 | 1.01995 | 1.71924 | 2.61948 | 4.28598 | 5.0216 | 5.4753 | 6.02687 | 6.99108 |
| player | theta_1 | 1455 | 0.0512894 | 0.731955 | -2.2221 | -1.17965 | -0.466562 | 0.0572953 | 0.584448 | 1.19784 | 2.11805 |
| player | theta_2 | 1455 | -0.0904652 | 0.665938 | -2.38694 | -1.2421 | -0.476259 | -0.0568124 | 0.358656 | 0.97982 | 2.05611 |
| player | theta_3 | 1455 | 0.046635 | 0.911592 | -3.31189 | -1.60481 | -0.500851 | 0.168741 | 0.706595 | 1.35289 | 2.31287 |
| player | theta_4 | 1455 | -0.138883 | 0.913331 | -2.69812 | -1.76351 | -0.755025 | -0.0409268 | 0.523477 | 1.23538 | 2.2095 |
| player | theta_5 | 1455 | -0.260446 | 0.719349 | -2.5183 | -1.44385 | -0.762071 | -0.258715 | 0.231548 | 0.90868 | 1.82089 |
| player | theta_norm | 1455 | 1.70851 | 0.583984 | 0.363168 | 0.85169 | 1.292 | 1.65276 | 2.05245 | 2.79449 | 3.61932 |
| tossup | beta | 1260 | 3.28475 | 0.673095 | 0.385695 | 2.26459 | 2.93172 | 3.3118 | 3.70212 | 4.28404 | 5.50333 |
| tossup | gamma | 1260 | 44.8022 | 174.065 | 3.61061 | 5.63021 | 9.11637 | 12.9896 | 24.6765 | 134.18 | 3470.16 |
| tossup | mu | 1260 | 0.643083 | 0.141217 | 0.198944 | 0.404594 | 0.541278 | 0.64873 | 0.743751 | 0.869857 | 0.975128 |
| tossup | alpha_1 | 1260 | -0.183888 | 0.686621 | -2.58445 | -1.43887 | -0.614675 | -0.11822 | 0.26781 | 0.9015 | 2.04515 |
| tossup | alpha_2 | 1260 | 0.348083 | 0.624161 | -1.31541 | -0.562742 | -0.0828884 | 0.286748 | 0.716794 | 1.45954 | 3.25806 |
| tossup | alpha_3 | 1260 | 0.497637 | 0.786367 | -1.60426 | -0.662486 | -0.0769337 | 0.384449 | 1.0686 | 1.88392 | 2.86914 |
| tossup | alpha_4 | 1260 | 0.700786 | 0.667806 | -1.13289 | -0.396949 | 0.237003 | 0.706159 | 1.16004 | 1.80498 | 2.83206 |
| tossup | alpha_5 | 1260 | 0.355312 | 0.676524 | -1.75194 | -0.672306 | -0.128335 | 0.319885 | 0.807828 | 1.51841 | 2.48868 |
| tossup | alpha_norm | 1260 | 1.78643 | 0.45822 | 0.480424 | 1.03862 | 1.4853 | 1.76506 | 2.08026 | 2.55401 | 3.41122 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 1.1418 | 1.56349 | -2.43821 | -1.57559 | -0.138047 | 1.39624 | 2.47904 | 3.30209 | 4.03627 |
| bonus_part | alpha_1 | 3768 | 0.590641 | 0.241563 | 0.146755 | 0.27741 | 0.425571 | 0.53909 | 0.733965 | 1.01446 | 2.2113 |
| bonus_part | alpha_2 | 3768 | 0.621442 | 0.238746 | 0.188068 | 0.329167 | 0.43887 | 0.573133 | 0.776285 | 1.03684 | 2.12706 |
| bonus_part | alpha_3 | 3768 | 0.6021 | 0.332568 | 0.157739 | 0.277212 | 0.35472 | 0.4843 | 0.783544 | 1.27687 | 2.67711 |
| bonus_part | alpha_4 | 3768 | 0.654192 | 0.326309 | 0.184062 | 0.30514 | 0.400093 | 0.574398 | 0.838417 | 1.2141 | 2.94374 |
| bonus_part | alpha_5 | 3768 | 0.62954 | 0.291296 | 0.191483 | 0.325331 | 0.416286 | 0.555874 | 0.772955 | 1.17731 | 2.87219 |
| bonus_part | alpha_norm | 3768 | 1.45358 | 0.475593 | 0.664196 | 0.85192 | 1.03614 | 1.36311 | 1.83618 | 2.2282 | 3.35515 |
