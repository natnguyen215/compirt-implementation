# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_3/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 463592 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 3 |
| synergy | steps | 2000 |
| synergy | final_loss | 81054.6 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.696282 |
| mean_synergy_contribution | 0.0347335 |
| median_synergy_contribution | 0 |
| negative_synergy_fraction | 0.492523 |
| positive_synergy_fraction | 0.483095 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.927156 |
| log_loss | 0.352541 |
| ece | 0.0372575 |
| part_accuracy | 0.846798 |
| part_accuracy_macro_team | 0.848133 |
| part_accuracy_macro_game | 0.847102 |
| part_accuracy_macro_bonus | 0.851638 |
| exact_acc | 0.594915 |
| ppb_mae | 0.487651 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.66375 |
| log_loss | 0.605639 |
| ece | 0.137172 |
| accuracy | 0.701422 |
| buzz_position_mae | 0.136676 |
| buzz_position_median_absolute_error | 0.114423 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.0706 | 0.895102 | 1.3898 | 3.25411 | 4.63463 | 5.21604 | 5.67572 | 6.29413 | 7.5215 |
| player | theta_1 | 1755 | -0.545617 | 0.650333 | -2.66705 | -1.76426 | -0.947652 | -0.492456 | -0.101155 | 0.436867 | 1.45201 |
| player | theta_2 | 1755 | -0.581759 | 0.680167 | -2.78029 | -1.94531 | -0.985128 | -0.493204 | -0.0802887 | 0.380621 | 0.953215 |
| player | theta_3 | 1755 | -0.648835 | 0.664419 | -2.58759 | -1.89892 | -1.06063 | -0.583361 | -0.212855 | 0.372407 | 1.10299 |
| player | theta_norm | 1755 | 1.36259 | 0.725961 | 0.0964527 | 0.458556 | 0.833882 | 1.21158 | 1.73947 | 2.82316 | 3.77757 |
| tossup | beta_1 | 1350 | 0.475434 | 0.649088 | -3.0318 | -0.0657348 | 0.0397589 | 0.142491 | 0.99233 | 1.69595 | 3.12251 |
| tossup | beta_2 | 1350 | 0.612574 | 0.681878 | -2.71598 | -0.0524052 | 0.0613412 | 0.241793 | 1.21615 | 1.81021 | 3.00173 |
| tossup | beta_3 | 1350 | 0.661682 | 0.710137 | -1.59201 | -0.0485511 | 0.0623369 | 0.286682 | 1.29682 | 1.9071 | 3.02018 |
| tossup | gamma_1 | 1350 | 8.03278 | 37.4431 | 0.539827 | 1.29305 | 2.17317 | 2.84534 | 3.5114 | 18.476 | 707.93 |
| tossup | gamma_2 | 1350 | 10.8313 | 56.9347 | 0.687553 | 1.42275 | 2.19916 | 2.88316 | 3.77277 | 28.2893 | 1088.09 |
| tossup | gamma_3 | 1350 | 7.51335 | 32.7062 | 0.71674 | 1.22564 | 1.95781 | 2.71369 | 3.42578 | 15.0971 | 440.399 |
| tossup | mu_1 | 1350 | 0.548207 | 0.122694 | 0.0803732 | 0.339251 | 0.505507 | 0.539408 | 0.584167 | 0.773849 | 0.994752 |
| tossup | mu_2 | 1350 | 0.535201 | 0.137417 | 0.0882662 | 0.276399 | 0.492219 | 0.538871 | 0.583679 | 0.774153 | 0.993785 |
| tossup | mu_3 | 1350 | 0.542909 | 0.146028 | 0.0817352 | 0.259638 | 0.494806 | 0.537685 | 0.600228 | 0.805116 | 0.992588 |
| tossup | r_1 | 1350 | 1.14012 | 0.907848 | 0.0460786 | 0.250146 | 0.497476 | 0.850309 | 1.45851 | 3.1532 | 4.7596 |
| tossup | r_2 | 1350 | 1.28999 | 0.925125 | 0.0448358 | 0.245512 | 0.575143 | 0.99456 | 1.84878 | 3.14237 | 4.88481 |
| tossup | r_3 | 1350 | 1.45061 | 1.06429 | 0.0617026 | 0.265854 | 0.604441 | 1.12321 | 2.09525 | 3.63388 | 5.19965 |
| tossup | r_norm | 1350 | 2.6967 | 0.779186 | 0.561011 | 1.46806 | 2.19571 | 2.62679 | 3.1755 | 4.06698 | 5.35379 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.0405622 | 1.63992 | -3.55128 | -2.58787 | -1.39906 | 0.129877 | 1.38089 | 2.60973 | 3.44287 |
| bonus_part | alpha_1 | 4716 | 0.823536 | 0.387058 | 0.205305 | 0.440435 | 0.608327 | 0.736623 | 0.914973 | 1.48791 | 4.21313 |
| bonus_part | alpha_2 | 4716 | 0.817706 | 0.374417 | 0.211791 | 0.450149 | 0.620215 | 0.747886 | 0.905296 | 1.3598 | 4.44929 |
| bonus_part | alpha_3 | 4716 | 0.860493 | 0.509513 | 0.198427 | 0.411958 | 0.584461 | 0.743151 | 0.951651 | 1.7 | 5.03366 |
| bonus_part | alpha_norm | 4716 | 1.51649 | 0.58062 | 0.547897 | 0.881328 | 1.16333 | 1.38227 | 1.69615 | 2.69581 | 5.21056 |
