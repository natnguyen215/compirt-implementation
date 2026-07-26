# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_3/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 467679 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 3 |
| synergy | steps | 2000 |
| synergy | final_loss | 82686.4 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.164889 |
| mean_synergy_contribution | -0.530077 |
| median_synergy_contribution | -0.484345 |
| negative_synergy_fraction | 0.776789 |
| positive_synergy_fraction | 0.198829 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.924181 |
| log_loss | 0.357523 |
| ece | 0.0352784 |
| part_accuracy | 0.843788 |
| part_accuracy_macro_team | 0.846019 |
| part_accuracy_macro_game | 0.844187 |
| part_accuracy_macro_bonus | 0.850961 |
| exact_acc | 0.589159 |
| ppb_mae | 0.603974 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.660105 |
| log_loss | 0.612804 |
| ece | 0.145901 |
| accuracy | 0.693849 |
| buzz_position_mae | 0.138324 |
| buzz_position_median_absolute_error | 0.116297 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.99635 | 0.982081 | 1.05552 | 2.88637 | 4.55027 | 5.17183 | 5.6426 | 6.27743 | 7.85378 |
| player | theta_1 | 1755 | 0.137029 | 0.549058 | -1.76331 | -0.9383 | -0.15892 | 0.196765 | 0.501946 | 0.937183 | 1.52508 |
| player | theta_2 | 1755 | 0.0365843 | 0.568697 | -2.15365 | -1.0709 | -0.299703 | 0.0834974 | 0.411127 | 0.877396 | 1.68037 |
| player | theta_3 | 1755 | -0.057229 | 0.5999 | -2.13054 | -1.25149 | -0.38786 | 0.0106014 | 0.379151 | 0.784449 | 1.40375 |
| player | theta_norm | 1755 | 0.899791 | 0.445061 | 0.0533951 | 0.32028 | 0.57538 | 0.824814 | 1.13721 | 1.73983 | 2.59934 |
| tossup | beta_1 | 1350 | 0.973484 | 0.594098 | -1.79623 | 0.152624 | 0.500801 | 0.9246 | 1.41176 | 1.98204 | 2.65222 |
| tossup | beta_2 | 1350 | 0.831655 | 0.640395 | -3.45658 | 0.107221 | 0.359056 | 0.659643 | 1.25621 | 2.01903 | 3.32767 |
| tossup | beta_3 | 1350 | 0.94162 | 0.667722 | -2.99675 | 0.117619 | 0.415727 | 0.803278 | 1.44927 | 2.06664 | 2.81263 |
| tossup | gamma_1 | 1350 | 20.8383 | 91.5747 | 0.277138 | 2.1473 | 3.86493 | 4.90299 | 7.12827 | 60.1439 | 1677.31 |
| tossup | gamma_2 | 1350 | 25.4082 | 113.332 | 0.105391 | 2.33704 | 4.05997 | 4.89668 | 6.24897 | 65.8668 | 1427.06 |
| tossup | gamma_3 | 1350 | 31.1576 | 141.694 | 0.0785257 | 2.2769 | 4.19636 | 5.09937 | 8.14764 | 97.0241 | 2125.74 |
| tossup | mu_1 | 1350 | 0.543762 | 0.149244 | 0.108846 | 0.337357 | 0.441465 | 0.511055 | 0.644461 | 0.826351 | 0.993756 |
| tossup | mu_2 | 1350 | 0.51873 | 0.135094 | 0.135803 | 0.350053 | 0.438947 | 0.48462 | 0.573998 | 0.798259 | 0.993458 |
| tossup | mu_3 | 1350 | 0.51835 | 0.138473 | 0.122627 | 0.326212 | 0.432636 | 0.486175 | 0.593336 | 0.792387 | 0.9854 |
| tossup | r_1 | 1350 | 1.71325 | 1.14589 | 0.0702893 | 0.363975 | 0.790129 | 1.48987 | 2.33392 | 3.88191 | 7.99726 |
| tossup | r_2 | 1350 | 1.37462 | 1.04088 | 0.0877359 | 0.218593 | 0.602836 | 1.09758 | 1.81139 | 3.5413 | 5.83619 |
| tossup | r_3 | 1350 | 1.42257 | 0.885133 | 0.057214 | 0.330952 | 0.72372 | 1.23139 | 1.94512 | 3.18004 | 4.67431 |
| tossup | r_norm | 1350 | 3.01754 | 0.959801 | 0.799047 | 1.56788 | 2.3566 | 2.94891 | 3.58918 | 4.63315 | 8.62122 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.339062 | 1.50217 | -3.24353 | -2.13629 | -0.949468 | 0.485917 | 1.58184 | 2.52456 | 3.9073 |
| bonus_part | alpha_1 | 4716 | 0.856854 | 0.481326 | 0.212103 | 0.393202 | 0.525461 | 0.726681 | 1.02971 | 1.70193 | 4.72837 |
| bonus_part | alpha_2 | 4716 | 0.831033 | 0.405649 | 0.233407 | 0.423803 | 0.556363 | 0.748903 | 0.98614 | 1.54011 | 4.13151 |
| bonus_part | alpha_3 | 4716 | 0.790052 | 0.358659 | 0.222152 | 0.422686 | 0.553405 | 0.722468 | 0.9242 | 1.30498 | 4.42595 |
| bonus_part | alpha_norm | 4716 | 1.49464 | 0.582984 | 0.636761 | 0.775321 | 1.06215 | 1.39873 | 1.8238 | 2.50314 | 4.83542 |
