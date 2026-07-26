# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-ablation-gamma/dim_3/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-ablation-gamma/dim_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 464696 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 3 |
| synergy | steps | 2000 |
| synergy | final_loss | 83602.7 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.0817119 |
| mean_synergy_contribution | -0.738745 |
| median_synergy_contribution | -0.72969 |
| negative_synergy_fraction | 0.834122 |
| positive_synergy_fraction | 0.141496 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.923262 |
| log_loss | 0.357357 |
| ece | 0.0312544 |
| part_accuracy | 0.842459 |
| part_accuracy_macro_team | 0.844723 |
| part_accuracy_macro_game | 0.842913 |
| part_accuracy_macro_bonus | 0.850518 |
| exact_acc | 0.586214 |
| ppb_mae | 0.635941 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.663127 |
| log_loss | 0.607594 |
| ece | 0.142893 |
| accuracy | 0.697211 |
| buzz_position_mae | 0.138012 |
| buzz_position_median_absolute_error | 0.116133 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.9885 | 0.983428 | 1.16924 | 2.83424 | 4.55754 | 5.1707 | 5.6297 | 6.25254 | 7.22949 |
| player | theta_1 | 1755 | 0.200865 | 0.546664 | -1.59953 | -0.866237 | -0.0898435 | 0.252373 | 0.549761 | 1.03577 | 1.67484 |
| player | theta_2 | 1755 | 0.188329 | 0.59119 | -1.86983 | -1.05275 | -0.111375 | 0.253313 | 0.61007 | 1.01604 | 1.52063 |
| player | theta_3 | 1755 | 0.197491 | 0.569762 | -2.10674 | -0.894448 | -0.128351 | 0.244692 | 0.577394 | 1.02628 | 1.88371 |
| player | theta_norm | 1755 | 0.959815 | 0.407542 | 0.103915 | 0.37779 | 0.664474 | 0.911457 | 1.20167 | 1.70278 | 2.63191 |
| tossup | beta_1 | 1350 | 1.04283 | 0.668629 | -1.66046 | 0.166096 | 0.482457 | 0.944183 | 1.57754 | 2.20461 | 2.78881 |
| tossup | beta_2 | 1350 | 0.968716 | 0.679257 | -2.27643 | 0.16231 | 0.403658 | 0.753556 | 1.55204 | 2.14989 | 3.11177 |
| tossup | beta_3 | 1350 | 0.889405 | 0.65088 | -1.6563 | 0.178087 | 0.402398 | 0.635232 | 1.34416 | 2.14899 | 3.03835 |
| tossup | gamma_1 | 1350 | 17.5103 | 78.0917 | 0.0873183 | 2.76062 | 4.17943 | 5.08175 | 7.31073 | 41.0573 | 1521.58 |
| tossup | gamma_2 | 1350 | 28.5754 | 136.741 | 0.147583 | 2.97928 | 4.38687 | 5.14649 | 7.48036 | 85.9233 | 2394.41 |
| tossup | gamma_3 | 1350 | 21.26 | 94.2052 | 0.316803 | 2.83489 | 4.27144 | 4.99898 | 6.36065 | 55.5522 | 1276.27 |
| tossup | mu_1 | 1350 | 0.532614 | 0.14664 | 0.110704 | 0.341017 | 0.437551 | 0.492218 | 0.62135 | 0.820757 | 0.991992 |
| tossup | mu_2 | 1350 | 0.505292 | 0.127406 | 0.12693 | 0.337054 | 0.432905 | 0.474071 | 0.558141 | 0.764718 | 0.991388 |
| tossup | mu_3 | 1350 | 0.502404 | 0.122712 | 0.129779 | 0.353687 | 0.436067 | 0.475298 | 0.540897 | 0.752617 | 0.989687 |
| tossup | r_1 | 1350 | 1.74791 | 1.28892 | 0.0696837 | 0.29679 | 0.686635 | 1.41479 | 2.50162 | 4.20263 | 8.42387 |
| tossup | r_2 | 1350 | 1.43865 | 1.05332 | 0.0776021 | 0.261753 | 0.590635 | 1.13494 | 2.09472 | 3.51839 | 5.08894 |
| tossup | r_3 | 1350 | 1.3095 | 1.05365 | 0.0937191 | 0.254849 | 0.530018 | 0.96767 | 1.72411 | 3.62255 | 6.05068 |
| tossup | r_norm | 1350 | 3.1292 | 0.962608 | 0.776623 | 1.69299 | 2.48233 | 3.0425 | 3.68666 | 4.73943 | 9.1245 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.398858 | 1.40139 | -2.84482 | -1.83141 | -0.814037 | 0.506371 | 1.56195 | 2.47213 | 3.88936 |
| bonus_part | alpha_1 | 4716 | 0.822617 | 0.46388 | 0.211386 | 0.362482 | 0.491975 | 0.698642 | 1.00979 | 1.59883 | 4.25007 |
| bonus_part | alpha_2 | 4716 | 0.8007 | 0.418266 | 0.187801 | 0.384213 | 0.497741 | 0.679986 | 0.992353 | 1.54418 | 4.13418 |
| bonus_part | alpha_3 | 4716 | 0.828732 | 0.428731 | 0.224381 | 0.38726 | 0.510437 | 0.718149 | 1.0486 | 1.58922 | 3.84186 |
| bonus_part | alpha_norm | 4716 | 1.48044 | 0.62194 | 0.596693 | 0.711168 | 0.971196 | 1.36358 | 1.90325 | 2.5741 | 4.37967 |
