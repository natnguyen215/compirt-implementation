# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/topic-tfidf-ablation/dim_7/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/topic-tfidf-ablation/dim_7`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 7 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 510048 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 7 |
| synergy | steps | 2000 |
| synergy | final_loss | 110386 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.469256 |
| mean_synergy_contribution | -0.040717 |
| median_synergy_contribution | -0.00169304 |
| negative_synergy_fraction | 0.552685 |
| positive_synergy_fraction | 0.422933 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.920729 |
| log_loss | 0.377097 |
| ece | 0.0651602 |
| part_accuracy | 0.843777 |
| part_accuracy_macro_team | 0.845136 |
| part_accuracy_macro_game | 0.844277 |
| part_accuracy_macro_bonus | 0.836445 |
| exact_acc | 0.587405 |
| ppb_mae | 0.463094 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.654603 |
| log_loss | 0.562973 |
| ece | 0.106359 |
| accuracy | 0.72152 |
| buzz_position_mae | 0.145536 |
| buzz_position_median_absolute_error | 0.127336 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.71239 | 0.45464 | 3.81562 | 4.98144 | 5.40831 | 5.71018 | 6.01065 | 6.4867 | 7.1736 |
| player | theta_1 | 1755 | -1.01918 | 1.22371 | -4.22007 | -2.69435 | -1.967 | -1.20182 | -0.172256 | 1.27663 | 2.60247 |
| player | theta_2 | 1755 | -1.18904 | 1.46223 | -4.37918 | -3.20773 | -2.32274 | -1.3704 | -0.251086 | 1.45679 | 3.93604 |
| player | theta_3 | 1755 | -0.95143 | 1.20962 | -3.51104 | -2.44706 | -1.88164 | -1.22621 | -0.2542 | 1.42317 | 3.78919 |
| player | theta_4 | 1755 | -0.540067 | 0.861809 | -2.72662 | -1.57338 | -1.03884 | -0.762607 | -0.256024 | 1.22251 | 3.61679 |
| player | theta_5 | 1755 | -0.592792 | 0.886199 | -3.32829 | -2.41961 | -0.886996 | -0.256248 | -0.18274 | 0.330808 | 3.38358 |
| player | theta_6 | 1755 | -0.362759 | 0.497783 | -2.69743 | -1.34807 | -0.534608 | -0.232182 | -0.175273 | 0.215021 | 2.52385 |
| player | theta_7 | 1755 | -0.305491 | 0.50976 | -2.59084 | -1.22984 | -0.469633 | -0.273767 | -0.124309 | 0.471178 | 2.39005 |
| player | theta_norm | 1755 | 3.26612 | 0.830068 | 0.98649 | 1.89509 | 2.72204 | 3.26516 | 3.86624 | 4.52844 | 6.57255 |
| tossup | beta_1 | 1350 | 1.03285 | 1.31173 | -2.33766 | 0.00326891 | 0.136471 | 0.306976 | 2.09745 | 3.60892 | 5.71895 |
| tossup | beta_2 | 1350 | 0.807097 | 1.17872 | -3.06545 | -0.02815 | 0.148118 | 0.263143 | 0.804449 | 3.56158 | 5.01324 |
| tossup | beta_3 | 1350 | 0.767417 | 1.18894 | -3.03111 | -0.0439253 | 0.116556 | 0.226945 | 0.566407 | 3.45541 | 5.03933 |
| tossup | beta_4 | 1350 | 0.43268 | 0.852651 | -3.90072 | -0.0313596 | 0.110054 | 0.197822 | 0.31956 | 2.91005 | 4.98777 |
| tossup | beta_5 | 1350 | 0.582147 | 0.975806 | -1.23956 | -0.0485138 | 0.105024 | 0.221335 | 0.434987 | 3.24602 | 4.18987 |
| tossup | beta_6 | 1350 | 0.338453 | 0.623652 | -0.972989 | -0.0667997 | 0.0832882 | 0.191114 | 0.32463 | 1.34271 | 3.80794 |
| tossup | beta_7 | 1350 | 0.267353 | 0.436206 | -1.69858 | -0.0695583 | 0.0771294 | 0.18052 | 0.316737 | 0.842674 | 3.80009 |
| tossup | gamma_1 | 1350 | 34.3815 | 135.569 | 1.09559 | 4.42844 | 4.8703 | 5.23457 | 7.76988 | 131.991 | 2145.85 |
| tossup | gamma_2 | 1350 | 30.2692 | 131.339 | 0.523941 | 4.34781 | 4.84896 | 5.1417 | 5.7763 | 112.601 | 1839.57 |
| tossup | gamma_3 | 1350 | 20.5225 | 93.6334 | 1.39802 | 4.40236 | 4.81902 | 5.12065 | 5.5883 | 56.9299 | 1685.21 |
| tossup | gamma_4 | 1350 | 13.3164 | 69.657 | 1.36851 | 4.49991 | 4.8239 | 5.05739 | 5.34658 | 13.6763 | 1519.02 |
| tossup | gamma_5 | 1350 | 12.0785 | 71.0634 | 2.33679 | 4.47019 | 4.83319 | 5.10172 | 5.45311 | 19.9956 | 1727.83 |
| tossup | gamma_6 | 1350 | 9.65751 | 61.2249 | 2.12259 | 4.47109 | 4.82509 | 5.05531 | 5.3371 | 7.05734 | 1493.98 |
| tossup | gamma_7 | 1350 | 5.77728 | 10.4365 | 1.24322 | 4.41575 | 4.80074 | 5.05195 | 5.32636 | 5.98832 | 359.745 |
| tossup | mu_1 | 1350 | 0.556675 | 0.130884 | 0.135244 | 0.452728 | 0.489403 | 0.505954 | 0.554974 | 0.85616 | 0.987673 |
| tossup | mu_2 | 1350 | 0.551492 | 0.129456 | 0.221631 | 0.463243 | 0.489556 | 0.505264 | 0.528662 | 0.887547 | 0.991433 |
| tossup | mu_3 | 1350 | 0.545008 | 0.118818 | 0.143405 | 0.469494 | 0.489992 | 0.504004 | 0.524217 | 0.843131 | 0.991763 |
| tossup | mu_4 | 1350 | 0.523199 | 0.0891194 | 0.283007 | 0.470693 | 0.488881 | 0.501502 | 0.515447 | 0.778685 | 0.993878 |
| tossup | mu_5 | 1350 | 0.529823 | 0.0905286 | 0.35027 | 0.471411 | 0.488985 | 0.502814 | 0.5187 | 0.768126 | 0.965338 |
| tossup | mu_6 | 1350 | 0.511135 | 0.0603562 | 0.261849 | 0.470279 | 0.487804 | 0.500597 | 0.513199 | 0.571542 | 0.958646 |
| tossup | mu_7 | 1350 | 0.505066 | 0.04504 | 0.370209 | 0.468537 | 0.486101 | 0.499338 | 0.512331 | 0.541331 | 0.907919 |
| tossup | topic_weight_1 | 1350 | 0.223138 | 0.267717 | 0.00458119 | 0.0125228 | 0.0256082 | 0.0623045 | 0.479987 | 0.732689 | 0.912508 |
| tossup | topic_weight_2 | 1350 | 0.175673 | 0.240913 | 0.00572356 | 0.0157255 | 0.0265446 | 0.050629 | 0.202717 | 0.726227 | 0.950851 |
| tossup | topic_weight_3 | 1350 | 0.179389 | 0.267029 | 0.00631372 | 0.0144595 | 0.0258524 | 0.0434162 | 0.124371 | 0.793578 | 0.928296 |
| tossup | topic_weight_4 | 1350 | 0.0957867 | 0.173718 | 0.00845308 | 0.0162993 | 0.0254583 | 0.0373131 | 0.0605997 | 0.599247 | 0.869356 |
| tossup | topic_weight_5 | 1350 | 0.142121 | 0.217439 | 0.00675398 | 0.0148809 | 0.0317687 | 0.0527981 | 0.114836 | 0.751919 | 0.88844 |
| tossup | topic_weight_6 | 1350 | 0.097012 | 0.133972 | 0.00846784 | 0.019074 | 0.0361778 | 0.0555881 | 0.092865 | 0.327383 | 0.792961 |
| tossup | topic_weight_7 | 1350 | 0.08688 | 0.10668 | 0.00821029 | 0.01734 | 0.0327289 | 0.0526246 | 0.0913096 | 0.292153 | 0.730148 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 4716 | 0.00142742 | 0.957293 | -3.90896 | -1.89432 | -0.22697 | 0.0200705 | 0.240421 | 1.78482 | 4.20463 |
| bonus_part | beta_2 | 4716 | 0.0109948 | 0.792119 | -4.30416 | -0.962969 | -0.195788 | 0.0169482 | 0.221079 | 1.07922 | 3.91807 |
| bonus_part | beta_3 | 4716 | 0.0643277 | 0.868798 | -3.89585 | -1.22813 | -0.200602 | 0.0171729 | 0.221764 | 1.74517 | 4.41988 |
| bonus_part | beta_4 | 4716 | 0.0256235 | 0.621588 | -3.82972 | -0.4738 | -0.190265 | 0.0195953 | 0.202865 | 0.549559 | 4.18906 |
| bonus_part | beta_5 | 4716 | 0.0208594 | 0.713254 | -3.95609 | -0.605883 | -0.197861 | 0.0137131 | 0.21535 | 0.858718 | 3.97994 |
| bonus_part | beta_6 | 4716 | 0.00644156 | 0.470237 | -3.81283 | -0.442505 | -0.188338 | 0.0131574 | 0.200388 | 0.442256 | 3.41559 |
| bonus_part | beta_7 | 4716 | -0.00203627 | 0.620442 | -3.72353 | -0.614013 | -0.201663 | 0.0129172 | 0.210851 | 0.576058 | 4.03029 |
