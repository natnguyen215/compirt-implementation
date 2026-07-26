# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/learned-topic/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/learned-topic`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 161960 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 56660 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.346319 |
| mean_synergy_contribution | -1.46347 |
| median_synergy_contribution | -1.38998 |
| negative_synergy_fraction | 0.999145 |
| positive_synergy_fraction | 0 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.92288 |
| log_loss | 0.388372 |
| ece | 0.0885815 |
| part_accuracy | 0.846421 |
| part_accuracy_macro_team | 0.841694 |
| part_accuracy_macro_game | 0.846564 |
| part_accuracy_macro_bonus | 0.83632 |
| exact_acc | 0.597121 |
| ppb_mae | 0.644481 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.663814 |
| log_loss | 0.628697 |
| ece | 0.152239 |
| accuracy | 0.664736 |
| buzz_position_mae | 0.151691 |
| buzz_position_median_absolute_error | 0.142988 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 5.48597 | 0.370404 | 3.90719 | 4.9078 | 5.2278 | 5.50263 | 5.71527 | 6.09433 | 6.22926 |
| player | theta_1 | 189 | 0.151212 | 1.05593 | -1.8243 | -1.40518 | -0.711731 | 0.183676 | 0.894248 | 1.99885 | 3.16608 |
| player | theta_2 | 189 | 0.128403 | 1.10844 | -1.75053 | -1.42679 | -0.810076 | 0.0254411 | 0.923286 | 2.12305 | 2.95665 |
| player | theta_3 | 189 | 0.221279 | 0.949639 | -1.72984 | -1.28138 | -0.442464 | 0.279496 | 0.816475 | 1.84348 | 3.03682 |
| player | theta_4 | 189 | 0.157277 | 1.16012 | -2.04085 | -1.6106 | -0.77577 | 0.0442617 | 1.18642 | 2.00087 | 2.93522 |
| player | theta_5 | 189 | 0.0901808 | 1.15339 | -2.01672 | -1.6043 | -0.831815 | 0.0227353 | 1.0644 | 2.01287 | 2.83769 |
| player | theta_norm | 189 | 2.35167 | 0.695493 | 0.7176 | 1.3399 | 1.90091 | 2.26638 | 2.70805 | 3.55356 | 5.40455 |
| tossup | beta_1 | 360 | 0.817223 | 1.31887 | -0.0935935 | -0.0164769 | 0.0554033 | 0.113075 | 0.451144 | 3.49137 | 3.95644 |
| tossup | beta_2 | 360 | 0.682748 | 1.21038 | -0.0930646 | 0.00213973 | 0.0695119 | 0.128584 | 0.258354 | 3.53438 | 4.34603 |
| tossup | beta_3 | 360 | 0.749072 | 1.24242 | -0.105674 | -0.00268887 | 0.0646701 | 0.128128 | 0.55728 | 3.62433 | 4.32102 |
| tossup | beta_4 | 360 | 0.855168 | 1.30432 | -0.0810947 | 0.00421604 | 0.0626847 | 0.123837 | 1.01151 | 3.58559 | 4.21165 |
| tossup | beta_5 | 360 | 1.02073 | 1.43786 | -0.0929108 | 0.0161799 | 0.0681109 | 0.140234 | 2.24174 | 3.72655 | 4.21136 |
| tossup | gamma_1 | 360 | 11.3424 | 23.7525 | 4.15467 | 4.63202 | 4.89834 | 5.14245 | 5.94745 | 37.5516 | 330.238 |
| tossup | gamma_2 | 360 | 17.131 | 62.1757 | 4.37132 | 4.64888 | 4.91699 | 5.13433 | 5.55396 | 53.2299 | 856.156 |
| tossup | gamma_3 | 360 | 11.4786 | 24.0218 | 4.40649 | 4.62643 | 4.8925 | 5.14932 | 5.8342 | 36.2192 | 340.472 |
| tossup | gamma_4 | 360 | 13.238 | 33.1008 | 4.40115 | 4.63788 | 4.95445 | 5.20388 | 8.4691 | 36.5335 | 353.96 |
| tossup | gamma_5 | 360 | 15.4357 | 37.518 | 4.24828 | 4.5996 | 4.92024 | 5.22886 | 10.1916 | 55.8504 | 409.344 |
| tossup | mu_1 | 360 | 0.538366 | 0.0880211 | 0.449722 | 0.479689 | 0.493878 | 0.504269 | 0.519222 | 0.742707 | 0.928994 |
| tossup | mu_2 | 360 | 0.535084 | 0.0875732 | 0.457504 | 0.479175 | 0.492995 | 0.503184 | 0.51879 | 0.742961 | 0.914423 |
| tossup | mu_3 | 360 | 0.530764 | 0.0785792 | 0.418275 | 0.476773 | 0.491348 | 0.503517 | 0.516037 | 0.710602 | 0.89896 |
| tossup | mu_4 | 360 | 0.539786 | 0.0896649 | 0.330079 | 0.479591 | 0.494616 | 0.506344 | 0.520205 | 0.758549 | 0.864568 |
| tossup | mu_5 | 360 | 0.550703 | 0.0949571 | 0.407661 | 0.475866 | 0.49259 | 0.50731 | 0.578948 | 0.767904 | 0.866441 |
| tossup | topic_weight_1 | 360 | 0.211104 | 0.348483 | 0.00868119 | 0.010833 | 0.0141133 | 0.0184783 | 0.128792 | 0.918685 | 0.938391 |
| tossup | topic_weight_2 | 360 | 0.158623 | 0.292094 | 0.00964332 | 0.0126583 | 0.0161435 | 0.0229562 | 0.0573376 | 0.91865 | 0.953065 |
| tossup | topic_weight_3 | 360 | 0.175491 | 0.292658 | 0.0096283 | 0.0134411 | 0.0181449 | 0.0270846 | 0.11832 | 0.887603 | 0.93309 |
| tossup | topic_weight_4 | 360 | 0.216238 | 0.325109 | 0.00756077 | 0.0141369 | 0.0211998 | 0.0310764 | 0.268202 | 0.919185 | 0.952118 |
| tossup | topic_weight_5 | 360 | 0.238544 | 0.331052 | 0.0114887 | 0.0156197 | 0.0228426 | 0.0360889 | 0.406704 | 0.916853 | 0.961422 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 1071 | 0.0267599 | 0.788705 | -2.94278 | -1.49861 | -0.117015 | 0.0195355 | 0.139355 | 1.72238 | 2.50668 |
| bonus_part | beta_2 | 1071 | 0.0429887 | 0.636512 | -2.68781 | -0.717511 | -0.10307 | 0.0209066 | 0.130789 | 1.25204 | 2.67067 |
| bonus_part | beta_3 | 1071 | 0.0285357 | 0.677784 | -2.78238 | -0.999093 | -0.124991 | 0.0261658 | 0.170255 | 1.34389 | 2.44231 |
| bonus_part | beta_4 | 1071 | 0.0573104 | 0.848535 | -2.73701 | -1.63102 | -0.138557 | 0.030826 | 0.171998 | 1.84414 | 2.67482 |
| bonus_part | beta_5 | 1071 | 0.0429529 | 0.743467 | -2.63782 | -1.36678 | -0.104482 | 0.0172693 | 0.151952 | 1.59092 | 2.5164 |
| synergy_player | psi_1 | 189 | -0.00548031 | 0.575406 | -1.52794 | -1.06933 | -0.258364 | -0.0112893 | 0.256043 | 1.04003 | 1.52676 |
| synergy_player | psi_2 | 189 | 0.00185572 | 0.445234 | -1.36411 | -0.790046 | -0.0553548 | 0.00595514 | 0.0917431 | 0.615903 | 1.50356 |
| synergy_player | psi_3 | 189 | -0.00333187 | 0.500289 | -1.33471 | -0.851586 | -0.0743873 | 0.00189582 | 0.0648136 | 0.965193 | 1.49878 |
| synergy_player | psi_norm | 189 | 0.805788 | 0.356246 | 0.0153581 | 0.333031 | 0.55704 | 0.647924 | 1.09369 | 1.40644 | 1.52934 |
| synergy | synergy_score | 274 | -0.257045 | 0.595396 | -1.73204 | -1.1257 | -0.736635 | -0.388448 | 0.298659 | 0.58284 | 0.903106 |
| synergy | synergy_contribution | 7017 | -1.46347 | 0.237191 | -2.04834 | -1.81375 | -1.66765 | -1.38998 | -1.26159 | -1.10504 | 0 |
