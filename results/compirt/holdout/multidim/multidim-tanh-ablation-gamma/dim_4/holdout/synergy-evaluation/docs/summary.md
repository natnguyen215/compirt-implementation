# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_4/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_4`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 465611 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 4 |
| synergy | steps | 2000 |
| synergy | final_loss | 81545.5 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.878577 |
| mean_synergy_contribution | -0.0331318 |
| median_synergy_contribution | -0.000102115 |
| negative_synergy_fraction | 0.502911 |
| positive_synergy_fraction | 0.472707 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.929188 |
| log_loss | 0.348178 |
| ece | 0.0378185 |
| part_accuracy | 0.849412 |
| part_accuracy_macro_team | 0.85085 |
| part_accuracy_macro_game | 0.849743 |
| part_accuracy_macro_bonus | 0.854922 |
| exact_acc | 0.601085 |
| ppb_mae | 0.507605 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.669224 |
| log_loss | 0.600025 |
| ece | 0.135809 |
| accuracy | 0.706898 |
| buzz_position_mae | 0.134709 |
| buzz_position_median_absolute_error | 0.112627 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.02673 | 0.913085 | 1.39965 | 3.15924 | 4.57159 | 5.16585 | 5.65886 | 6.23965 | 7.30109 |
| player | theta_1 | 1755 | -0.479496 | 0.657198 | -3.01481 | -1.66309 | -0.907999 | -0.437289 | -0.0403816 | 0.541908 | 1.64134 |
| player | theta_2 | 1755 | -0.502744 | 0.645157 | -3.45995 | -1.76823 | -0.884887 | -0.430969 | -0.0670262 | 0.449063 | 1.52981 |
| player | theta_3 | 1755 | -0.544602 | 0.670817 | -2.60852 | -1.8459 | -0.966413 | -0.481396 | -0.050638 | 0.43707 | 1.01259 |
| player | theta_4 | 1755 | -0.638595 | 0.626132 | -2.62296 | -1.74392 | -1.06431 | -0.598331 | -0.216481 | 0.348045 | 1.33827 |
| player | theta_norm | 1755 | 1.53487 | 0.721631 | 0.150854 | 0.604117 | 0.998861 | 1.39061 | 1.96707 | 2.92375 | 3.8513 |
| tossup | beta_1 | 1350 | 0.412867 | 0.606034 | -1.47249 | -0.0676361 | 0.0336399 | 0.126358 | 0.66691 | 1.61523 | 3.49876 |
| tossup | beta_2 | 1350 | 0.507361 | 0.645655 | -1.53885 | -0.065559 | 0.044079 | 0.157137 | 1.03908 | 1.80804 | 2.46779 |
| tossup | beta_3 | 1350 | 0.542182 | 0.67343 | -3.07887 | -0.0714892 | 0.0508526 | 0.182579 | 1.15004 | 1.74866 | 3.04277 |
| tossup | beta_4 | 1350 | 0.37766 | 0.601576 | -2.56933 | -0.0772594 | 0.0292947 | 0.117524 | 0.43571 | 1.61325 | 2.85462 |
| tossup | gamma_1 | 1350 | 6.93253 | 37.9571 | 0.642814 | 1.37877 | 2.20996 | 2.86215 | 3.48267 | 11.993 | 1017.35 |
| tossup | gamma_2 | 1350 | 7.12859 | 33.6682 | 0.617559 | 1.14279 | 1.98328 | 2.66731 | 3.40924 | 11.5076 | 602.841 |
| tossup | gamma_3 | 1350 | 7.92443 | 39.1725 | 0.693889 | 1.35228 | 2.19145 | 2.83522 | 3.58405 | 16.4297 | 858.84 |
| tossup | gamma_4 | 1350 | 7.15595 | 42.5525 | 0.695769 | 1.20573 | 2.12023 | 2.77771 | 3.44148 | 8.30283 | 814.037 |
| tossup | mu_1 | 1350 | 0.54875 | 0.113676 | 0.0722534 | 0.367053 | 0.505963 | 0.540376 | 0.579526 | 0.76462 | 0.992811 |
| tossup | mu_2 | 1350 | 0.537674 | 0.125269 | 0.0562735 | 0.29042 | 0.497446 | 0.535113 | 0.582154 | 0.767633 | 0.99279 |
| tossup | mu_3 | 1350 | 0.533894 | 0.129524 | 0.0765646 | 0.276073 | 0.498943 | 0.536921 | 0.582029 | 0.752015 | 0.975077 |
| tossup | mu_4 | 1350 | 0.549024 | 0.111773 | 0.08175 | 0.372491 | 0.506558 | 0.53731 | 0.58301 | 0.757966 | 0.993955 |
| tossup | r_1 | 1350 | 1.06103 | 0.901385 | 0.046805 | 0.225258 | 0.442525 | 0.743799 | 1.26615 | 3.10694 | 4.56927 |
| tossup | r_2 | 1350 | 1.18752 | 0.811171 | 0.0697058 | 0.242174 | 0.546071 | 0.978054 | 1.67732 | 2.7467 | 4.50564 |
| tossup | r_3 | 1350 | 1.24898 | 0.923556 | 0.0442726 | 0.237492 | 0.543844 | 0.911049 | 1.81188 | 3.14029 | 4.77683 |
| tossup | r_4 | 1350 | 1.02848 | 0.756457 | 0.0543616 | 0.189847 | 0.465034 | 0.813534 | 1.38213 | 2.70548 | 4.26723 |
| tossup | r_norm | 1350 | 2.74431 | 0.718605 | 0.673007 | 1.60223 | 2.23798 | 2.723 | 3.19558 | 3.97772 | 5.28337 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.0264216 | 1.63871 | -3.54743 | -2.58645 | -1.41054 | 0.113956 | 1.36845 | 2.60503 | 3.45406 |
| bonus_part | alpha_1 | 4716 | 0.823734 | 0.383218 | 0.186644 | 0.455675 | 0.61352 | 0.742433 | 0.902044 | 1.47923 | 4.26951 |
| bonus_part | alpha_2 | 4716 | 0.830999 | 0.407384 | 0.215611 | 0.461076 | 0.61592 | 0.748246 | 0.91091 | 1.47593 | 5.00477 |
| bonus_part | alpha_3 | 4716 | 0.823441 | 0.38436 | 0.223216 | 0.44631 | 0.616363 | 0.751651 | 0.914628 | 1.38794 | 4.68674 |
| bonus_part | alpha_4 | 4716 | 0.822832 | 0.385995 | 0.207495 | 0.410535 | 0.578475 | 0.739139 | 0.94681 | 1.52199 | 4.24444 |
| bonus_part | alpha_norm | 4716 | 1.73332 | 0.573829 | 0.656124 | 1.05413 | 1.395 | 1.60832 | 1.94538 | 2.86803 | 5.45829 |
