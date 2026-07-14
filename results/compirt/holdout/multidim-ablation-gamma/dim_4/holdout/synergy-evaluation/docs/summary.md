# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim-ablation-gamma/dim_4/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/multidim-ablation-gamma/dim_4`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 466081 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 4 |
| synergy | steps | 2000 |
| synergy | final_loss | 84715.4 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.225335 |
| mean_synergy_contribution | -0.969165 |
| median_synergy_contribution | -0.935017 |
| negative_synergy_fraction | 0.87354 |
| positive_synergy_fraction | 0.102078 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.924462 |
| log_loss | 0.355777 |
| ece | 0.0325979 |
| part_accuracy | 0.844085 |
| exact_acc | 0.590532 |
| per_bonus_points_mae | 4.89303 |
| ppb_mae | 1.825 |
| accuracy | 0.844085 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.671373 |
| log_loss | 0.599422 |
| ece | 0.137397 |
| accuracy | 0.702579 |
| buzz_position_mae | 0.136233 |
| buzz_position_median_absolute_error | 0.114666 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.93623 | 0.986744 | 1.17887 | 2.79721 | 4.50592 | 5.12006 | 5.60161 | 6.19178 | 7.24262 |
| player | theta_1 | 1755 | 0.1805 | 0.583761 | -2.23368 | -0.924556 | -0.172658 | 0.229431 | 0.569293 | 1.06138 | 1.91746 |
| player | theta_2 | 1755 | 0.182413 | 0.538583 | -1.98533 | -0.885278 | -0.127533 | 0.24137 | 0.524218 | 0.996339 | 1.6671 |
| player | theta_3 | 1755 | 0.0468144 | 0.572716 | -2.2141 | -1.06121 | -0.288158 | 0.116336 | 0.417529 | 0.886858 | 1.73007 |
| player | theta_4 | 1755 | 0.174015 | 0.605364 | -1.82686 | -1.02794 | -0.173761 | 0.229074 | 0.616691 | 1.02716 | 1.6116 |
| player | theta_norm | 1755 | 1.11381 | 0.427109 | 0.204802 | 0.499364 | 0.799442 | 1.07005 | 1.36095 | 1.92024 | 2.62494 |
| tossup | beta_1 | 1350 | 0.800674 | 0.611502 | -3.10816 | 0.142134 | 0.39452 | 0.582731 | 1.1295 | 2.04066 | 2.6629 |
| tossup | beta_2 | 1350 | 0.801258 | 0.531744 | -2.44742 | 0.167889 | 0.43544 | 0.660233 | 1.10469 | 1.80821 | 2.62013 |
| tossup | beta_3 | 1350 | 0.852759 | 0.59349 | -1.28843 | 0.135368 | 0.406753 | 0.668659 | 1.27458 | 1.99005 | 2.93157 |
| tossup | beta_4 | 1350 | 0.900087 | 0.637029 | -1.47623 | 0.143107 | 0.404667 | 0.684244 | 1.39243 | 2.0793 | 2.9938 |
| tossup | gamma_1 | 1350 | 14.4328 | 66.4166 | 0.110944 | 2.90769 | 4.25432 | 4.99282 | 6.04315 | 34.3688 | 1167.76 |
| tossup | gamma_2 | 1350 | 20.0823 | 104.68 | 0.272052 | 2.52921 | 4.03906 | 4.88919 | 6.11587 | 37.9115 | 2233.01 |
| tossup | gamma_3 | 1350 | 16.4286 | 78.5105 | 0.322179 | 2.93998 | 4.27599 | 5.00733 | 6.53371 | 34.8331 | 1504.76 |
| tossup | gamma_4 | 1350 | 24.003 | 113.563 | 0.173552 | 2.86796 | 4.39101 | 5.09535 | 7.10588 | 72.1962 | 1901.54 |
| tossup | mu_1 | 1350 | 0.497297 | 0.112522 | 0.141677 | 0.350672 | 0.437511 | 0.475027 | 0.529647 | 0.726333 | 0.989696 |
| tossup | mu_2 | 1350 | 0.513287 | 0.12855 | 0.1128 | 0.356436 | 0.439612 | 0.481987 | 0.566499 | 0.77126 | 0.991806 |
| tossup | mu_3 | 1350 | 0.508109 | 0.130376 | 0.148111 | 0.346284 | 0.432552 | 0.475788 | 0.556977 | 0.76505 | 0.991534 |
| tossup | mu_4 | 1350 | 0.505215 | 0.119635 | 0.108926 | 0.348369 | 0.436533 | 0.480591 | 0.556491 | 0.74915 | 0.992118 |
| tossup | r_1 | 1350 | 1.24431 | 1.04141 | 0.0857817 | 0.235682 | 0.492744 | 0.879032 | 1.63972 | 3.57377 | 5.75182 |
| tossup | r_2 | 1350 | 1.26725 | 0.992695 | 0.0647997 | 0.277305 | 0.521598 | 0.937255 | 1.72957 | 3.42305 | 5.90265 |
| tossup | r_3 | 1350 | 1.31683 | 0.966852 | 0.0761522 | 0.263955 | 0.549821 | 0.986868 | 1.92819 | 3.28757 | 4.87422 |
| tossup | r_4 | 1350 | 1.32715 | 0.968265 | 0.0618481 | 0.241978 | 0.552866 | 1.04168 | 1.92385 | 3.22263 | 5.2177 |
| tossup | r_norm | 1350 | 3.12919 | 0.893188 | 0.921725 | 1.80206 | 2.53517 | 3.06209 | 3.66368 | 4.66454 | 8.30109 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.424235 | 1.42248 | -2.77913 | -1.83744 | -0.802863 | 0.542294 | 1.59533 | 2.53295 | 3.97672 |
| bonus_part | alpha_1 | 4716 | 0.823142 | 0.414156 | 0.197168 | 0.404211 | 0.527606 | 0.719845 | 1.01425 | 1.53858 | 3.95617 |
| bonus_part | alpha_2 | 4716 | 0.790464 | 0.385434 | 0.241509 | 0.391297 | 0.508292 | 0.692702 | 0.981202 | 1.42046 | 3.65013 |
| bonus_part | alpha_3 | 4716 | 0.79007 | 0.355758 | 0.192902 | 0.400453 | 0.53585 | 0.713533 | 0.951392 | 1.38747 | 3.39813 |
| bonus_part | alpha_4 | 4716 | 0.797363 | 0.40912 | 0.170084 | 0.398265 | 0.51474 | 0.686241 | 0.978678 | 1.48468 | 4.52086 |
| bonus_part | alpha_norm | 4716 | 1.67445 | 0.610413 | 0.748149 | 0.879094 | 1.17934 | 1.58831 | 2.09064 | 2.74314 | 4.58062 |
