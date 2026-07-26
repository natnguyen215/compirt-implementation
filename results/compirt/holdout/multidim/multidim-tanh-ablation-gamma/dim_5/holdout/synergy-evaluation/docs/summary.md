# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_5/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_5`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 470030 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 81988.7 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.06584 |
| mean_synergy_contribution | -0.0989626 |
| median_synergy_contribution | -0.0047439 |
| negative_synergy_fraction | 0.536706 |
| positive_synergy_fraction | 0.438912 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.930733 |
| log_loss | 0.344638 |
| ece | 0.0379766 |
| part_accuracy | 0.851512 |
| part_accuracy_macro_team | 0.852599 |
| part_accuracy_macro_game | 0.851804 |
| part_accuracy_macro_bonus | 0.85716 |
| exact_acc | 0.606296 |
| ppb_mae | 0.51757 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.67705 |
| log_loss | 0.593399 |
| ece | 0.133383 |
| accuracy | 0.71063 |
| buzz_position_mae | 0.133471 |
| buzz_position_median_absolute_error | 0.111066 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.98703 | 0.93464 | 1.30919 | 3.05326 | 4.51813 | 5.12244 | 5.63153 | 6.23399 | 7.23685 |
| player | theta_1 | 1755 | -0.48475 | 0.657009 | -2.47759 | -1.65251 | -0.89871 | -0.442569 | -0.0289805 | 0.54646 | 1.64216 |
| player | theta_2 | 1755 | -0.38419 | 0.649647 | -2.1938 | -1.56952 | -0.823663 | -0.331962 | 0.108631 | 0.561971 | 1.62774 |
| player | theta_3 | 1755 | -0.55028 | 0.646648 | -2.91592 | -1.717 | -0.996008 | -0.491601 | -0.09344 | 0.437654 | 1.36385 |
| player | theta_4 | 1755 | -0.478551 | 0.64802 | -3.24101 | -1.65938 | -0.85407 | -0.40562 | -0.0324241 | 0.484018 | 1.25273 |
| player | theta_5 | 1755 | -0.598966 | 0.644446 | -2.62472 | -1.70628 | -1.03442 | -0.569836 | -0.163685 | 0.472335 | 1.39043 |
| player | theta_norm | 1755 | 1.68647 | 0.731554 | 0.214787 | 0.703338 | 1.14046 | 1.5511 | 2.1109 | 3.10002 | 4.03824 |
| tossup | beta_1 | 1350 | 0.39366 | 0.604525 | -2.83762 | -0.0956073 | 0.0352791 | 0.122334 | 0.663766 | 1.64794 | 3.14535 |
| tossup | beta_2 | 1350 | 0.39657 | 0.591578 | -2.63062 | -0.10187 | 0.0354475 | 0.130061 | 0.717254 | 1.62351 | 2.36051 |
| tossup | beta_3 | 1350 | 0.355702 | 0.576226 | -1.89654 | -0.0821096 | 0.0311475 | 0.112862 | 0.313853 | 1.60763 | 3.19098 |
| tossup | beta_4 | 1350 | 0.350611 | 0.56218 | -2.31103 | -0.101532 | 0.0299976 | 0.120253 | 0.359117 | 1.63222 | 2.52166 |
| tossup | beta_5 | 1350 | 0.476727 | 0.635543 | -3.62834 | -0.0536888 | 0.0541409 | 0.15613 | 0.983853 | 1.66752 | 2.5521 |
| tossup | gamma_1 | 1350 | 6.8461 | 34.5712 | 0.794774 | 1.41692 | 2.25722 | 2.8861 | 3.50075 | 9.16731 | 599.896 |
| tossup | gamma_2 | 1350 | 6.7615 | 36.6437 | 0.59721 | 1.29783 | 2.15347 | 2.75409 | 3.40574 | 10.7533 | 813.818 |
| tossup | gamma_3 | 1350 | 8.59134 | 52.3761 | 0.640865 | 1.28551 | 2.22767 | 2.77132 | 3.43779 | 9.59399 | 982.125 |
| tossup | gamma_4 | 1350 | 5.46932 | 29.8007 | 0.662274 | 1.11413 | 2.03934 | 2.73711 | 3.4509 | 8.71737 | 932.099 |
| tossup | gamma_5 | 1350 | 5.7087 | 32.2656 | 0.630394 | 1.23083 | 2.01311 | 2.72485 | 3.43686 | 8.68234 | 757.938 |
| tossup | mu_1 | 1350 | 0.540931 | 0.107814 | 0.0496005 | 0.356509 | 0.506906 | 0.537944 | 0.574068 | 0.724444 | 0.992504 |
| tossup | mu_2 | 1350 | 0.535866 | 0.11379 | 0.09447 | 0.323076 | 0.505912 | 0.537892 | 0.579558 | 0.715337 | 0.981093 |
| tossup | mu_3 | 1350 | 0.539834 | 0.102882 | 0.0818042 | 0.344498 | 0.507833 | 0.540257 | 0.576784 | 0.689359 | 0.994074 |
| tossup | mu_4 | 1350 | 0.543601 | 0.108694 | 0.0877762 | 0.362489 | 0.508023 | 0.538975 | 0.579414 | 0.730936 | 0.993473 |
| tossup | mu_5 | 1350 | 0.542663 | 0.120029 | 0.0866212 | 0.311944 | 0.498901 | 0.537129 | 0.585082 | 0.762491 | 0.968357 |
| tossup | r_1 | 1350 | 1.00579 | 0.860199 | 0.0453705 | 0.212091 | 0.41471 | 0.699077 | 1.22175 | 2.95098 | 4.4888 |
| tossup | r_2 | 1350 | 1.02327 | 0.722204 | 0.0514913 | 0.226127 | 0.465859 | 0.779627 | 1.45849 | 2.46111 | 3.98706 |
| tossup | r_3 | 1350 | 0.903881 | 0.596531 | 0.0631529 | 0.205031 | 0.461115 | 0.764678 | 1.20372 | 2.10228 | 3.72836 |
| tossup | r_4 | 1350 | 0.988933 | 0.681983 | 0.0532962 | 0.202319 | 0.458547 | 0.792631 | 1.39119 | 2.34516 | 3.69459 |
| tossup | r_5 | 1350 | 1.19635 | 0.876177 | 0.0610074 | 0.216046 | 0.479987 | 0.92631 | 1.81038 | 2.92424 | 4.03603 |
| tossup | r_norm | 1350 | 2.76654 | 0.692532 | 0.773357 | 1.69618 | 2.29577 | 2.72951 | 3.21202 | 3.98582 | 5.5956 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.0216933 | 1.63833 | -3.51009 | -2.59401 | -1.41273 | 0.109909 | 1.35991 | 2.592 | 3.44894 |
| bonus_part | alpha_1 | 4716 | 0.830432 | 0.386133 | 0.226965 | 0.458467 | 0.618479 | 0.748965 | 0.916911 | 1.45281 | 4.75796 |
| bonus_part | alpha_2 | 4716 | 0.804067 | 0.314661 | 0.239692 | 0.471658 | 0.63537 | 0.747491 | 0.881486 | 1.3391 | 4.47695 |
| bonus_part | alpha_3 | 4716 | 0.813498 | 0.34658 | 0.2123 | 0.454379 | 0.601249 | 0.751581 | 0.932879 | 1.35242 | 4.18922 |
| bonus_part | alpha_4 | 4716 | 0.797275 | 0.284914 | 0.218733 | 0.473239 | 0.627451 | 0.747437 | 0.88499 | 1.312 | 3.46203 |
| bonus_part | alpha_5 | 4716 | 0.846083 | 0.425035 | 0.193005 | 0.406107 | 0.58367 | 0.747186 | 0.972163 | 1.64077 | 3.83888 |
| bonus_part | alpha_norm | 4716 | 1.91712 | 0.551435 | 0.808837 | 1.2303 | 1.60511 | 1.79778 | 2.12187 | 3.02104 | 5.02773 |
