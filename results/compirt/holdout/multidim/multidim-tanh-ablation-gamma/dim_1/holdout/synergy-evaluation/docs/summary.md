# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_1/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 471975 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 1 |
| synergy | steps | 2000 |
| synergy | final_loss | 80819.2 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.296916 |
| mean_synergy_contribution | 0.138577 |
| median_synergy_contribution | 0.0133586 |
| negative_synergy_fraction | 0.407781 |
| positive_synergy_fraction | 0.567837 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.920661 |
| log_loss | 0.36593 |
| ece | 0.0374145 |
| part_accuracy | 0.839575 |
| part_accuracy_macro_team | 0.840944 |
| part_accuracy_macro_game | 0.839986 |
| part_accuracy_macro_bonus | 0.845967 |
| exact_acc | 0.578704 |
| ppb_mae | 0.475436 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.635168 |
| log_loss | 0.638369 |
| ece | 0.160403 |
| accuracy | 0.676744 |
| buzz_position_mae | 0.144528 |
| buzz_position_median_absolute_error | 0.120967 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.31353 | 0.871029 | 1.45776 | 3.68509 | 4.85771 | 5.36198 | 5.86561 | 6.63505 | 7.92004 |
| player | theta_1 | 1755 | -0.780321 | 0.827494 | -3.94529 | -2.46233 | -1.09649 | -0.651375 | -0.254821 | 0.28774 | 1.00673 |
| player | theta_norm | 1755 | 0.853077 | 0.752223 | 0.00033036 | 0.0631508 | 0.329558 | 0.667626 | 1.09649 | 2.46233 | 3.94529 |
| tossup | beta_1 | 1350 | 1.4391 | 0.456127 | -0.821388 | 0.735299 | 1.14379 | 1.4154 | 1.70374 | 2.18176 | 3.3601 |
| tossup | gamma_1 | 1350 | 12.4507 | 59.7677 | 0.633392 | 1.20411 | 1.96398 | 2.77509 | 4.93402 | 29.596 | 1092.86 |
| tossup | mu_1 | 1350 | 0.560038 | 0.179271 | 0.0784089 | 0.240248 | 0.435458 | 0.580293 | 0.687191 | 0.83685 | 0.984158 |
| tossup | r_1 | 1350 | 2.2604 | 1.06456 | 0.235332 | 1.00251 | 1.50854 | 1.9705 | 2.75762 | 4.53021 | 6.20209 |
| tossup | r_norm | 1350 | 2.2604 | 1.06456 | 0.235332 | 1.00251 | 1.50854 | 1.9705 | 2.75762 | 4.53021 | 6.20209 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.0570389 | 1.63791 | -3.50521 | -2.59572 | -1.37343 | 0.172226 | 1.41534 | 2.56647 | 3.70681 |
| bonus_part | alpha_1 | 4716 | 0.878649 | 0.499705 | 0.259397 | 0.43222 | 0.576042 | 0.7461 | 1.01354 | 1.7516 | 4.76782 |
| bonus_part | alpha_norm | 4716 | 0.878649 | 0.499705 | 0.259397 | 0.43222 | 0.576042 | 0.7461 | 1.01354 | 1.7516 | 4.76782 |
