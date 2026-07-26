# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/tfidf-multidim-cumulative-difficulty-all2024-cal/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/tfidf-multidim-cumulative-difficulty-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 447982 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 85296.3 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.967472 |
| mean_synergy_contribution | 0.337471 |
| median_synergy_contribution | 0.286901 |
| negative_synergy_fraction | 0.311079 |
| positive_synergy_fraction | 0.664538 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.932839 |
| log_loss | 0.333042 |
| ece | 0.0211868 |
| part_accuracy | 0.852847 |
| part_accuracy_macro_team | 0.854075 |
| part_accuracy_macro_game | 0.853134 |
| part_accuracy_macro_bonus | 0.8591 |
| exact_acc | 0.609521 |
| ppb_mae | 0.536299 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.624494 |
| log_loss | 0.521253 |
| ece | 0.00808228 |
| accuracy | 0.770984 |
| buzz_position_mae | 0.13075 |
| buzz_position_median_absolute_error | 0.107977 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.928178 | 0.932839 | 0.00466122 | synergy |
| log_loss | 0.342408 | 0.333042 | -0.00936658 | synergy |
| ece | 0.0212791 | 0.0211868 | -9.22858e-05 | synergy |
| part_accuracy | 0.845795 | 0.852847 | 0.00705219 | synergy |
| part_accuracy_macro_team | 0.846868 | 0.854075 | 0.00720723 | synergy |
| part_accuracy_macro_game | 0.84611 | 0.853134 | 0.00702345 | synergy |
| part_accuracy_macro_bonus | 0.852925 | 0.8591 | 0.00617413 | synergy |
| exact_acc | 0.594237 | 0.609521 | 0.0152843 | synergy |
| ppb_mae | 1.34287 | 0.536299 | -0.806568 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 0.86433 | 0.681822 | -1.07463 | -0.179568 | 0.428243 | 0.833807 | 1.27926 | 1.99243 | 4.96215 |
| player | theta_1 | 1755 | -0.63548 | 0.540004 | -2.62992 | -1.51915 | -0.97966 | -0.645033 | -0.281166 | 0.274397 | 1.20865 |
| player | theta_2 | 1755 | -0.662063 | 0.595896 | -2.43644 | -1.63107 | -1.10799 | -0.648955 | -0.225262 | 0.282675 | 1.30124 |
| player | theta_3 | 1755 | -0.376346 | 0.590858 | -2.51809 | -1.27483 | -0.800834 | -0.406199 | 0.01108 | 0.689063 | 1.70409 |
| player | theta_4 | 1755 | -0.521202 | 0.626043 | -2.56265 | -1.44399 | -1.00833 | -0.549981 | -0.102964 | 0.574819 | 1.61858 |
| player | theta_5 | 1755 | -0.553644 | 0.588208 | -2.899 | -1.46334 | -0.948487 | -0.559097 | -0.164112 | 0.408998 | 1.52981 |
| player | theta_norm | 1755 | 1.74875 | 0.486538 | 0.27397 | 0.960078 | 1.40397 | 1.75763 | 2.08339 | 2.53337 | 3.4064 |
| tossup | beta_1 | 1350 | 0.802111 | 0.492268 | -0.388626 | 0.196127 | 0.490547 | 0.696131 | 1.02041 | 1.76861 | 3.08801 |
| tossup | beta_2 | 1350 | 0.890897 | 0.479592 | -0.397376 | 0.249517 | 0.554495 | 0.8081 | 1.1765 | 1.76633 | 3.9106 |
| tossup | beta_3 | 1350 | 0.874789 | 0.489809 | -0.397415 | 0.225216 | 0.530713 | 0.757147 | 1.19563 | 1.79365 | 2.90781 |
| tossup | beta_4 | 1350 | 0.837676 | 0.500734 | -0.293776 | 0.222997 | 0.505063 | 0.708685 | 1.08351 | 1.82427 | 3.39497 |
| tossup | beta_5 | 1350 | 0.827484 | 0.489888 | -0.539254 | 0.208867 | 0.516563 | 0.72412 | 1.04638 | 1.84314 | 3.37839 |
| tossup | gamma_1 | 1350 | 15.7039 | 83.2392 | 1.00354 | 3.32242 | 4.42798 | 5.17925 | 6.54745 | 28.8754 | 1990.96 |
| tossup | gamma_2 | 1350 | 23.6162 | 120.918 | 0.921734 | 2.9164 | 4.24946 | 5.1626 | 6.95183 | 47.8416 | 2020.1 |
| tossup | gamma_3 | 1350 | 19.6302 | 80.4706 | 0.9176 | 3.12144 | 4.31901 | 5.17268 | 6.88782 | 52.5564 | 1071.79 |
| tossup | gamma_4 | 1350 | 15.2845 | 77.6558 | 1.28635 | 3.20601 | 4.30888 | 5.17869 | 6.61557 | 34.8221 | 1720.08 |
| tossup | gamma_5 | 1350 | 20.8878 | 115.668 | 1.31979 | 2.95821 | 4.22955 | 5.06655 | 6.50348 | 35.5893 | 2059.12 |
| tossup | mu_1 | 1350 | 0.51326 | 0.105729 | 0.179688 | 0.385652 | 0.450235 | 0.488901 | 0.552666 | 0.72299 | 0.993722 |
| tossup | mu_2 | 1350 | 0.534549 | 0.124176 | 0.171359 | 0.36906 | 0.454123 | 0.513092 | 0.600107 | 0.761748 | 0.99377 |
| tossup | mu_3 | 1350 | 0.544059 | 0.134726 | 0.174265 | 0.383199 | 0.454942 | 0.505527 | 0.60875 | 0.819935 | 0.993318 |
| tossup | mu_4 | 1350 | 0.522436 | 0.120037 | 0.18532 | 0.384746 | 0.451924 | 0.494807 | 0.57004 | 0.784976 | 0.988446 |
| tossup | mu_5 | 1350 | 0.51716 | 0.109442 | 0.135281 | 0.378812 | 0.451684 | 0.494829 | 0.56594 | 0.727474 | 0.989155 |
| tossup | alpha_1 | 1350 | 1.08971 | 0.608692 | 0.0406141 | 0.292368 | 0.64379 | 0.96778 | 1.43308 | 2.30296 | 3.46291 |
| tossup | alpha_2 | 1350 | 1.39308 | 0.648176 | 0.0564472 | 0.375224 | 0.906454 | 1.36631 | 1.82508 | 2.46763 | 3.67961 |
| tossup | alpha_3 | 1350 | 1.35296 | 0.845025 | 0.066285 | 0.350757 | 0.704375 | 1.07549 | 1.95458 | 2.87772 | 4.91625 |
| tossup | alpha_4 | 1350 | 1.32364 | 0.87625 | 0.061112 | 0.383201 | 0.738451 | 1.07799 | 1.58889 | 3.27698 | 4.78687 |
| tossup | alpha_5 | 1350 | 1.22401 | 0.617338 | 0.0518492 | 0.302922 | 0.766976 | 1.15752 | 1.62639 | 2.32716 | 3.35127 |
| tossup | alpha_norm | 1350 | 3.23328 | 0.637734 | 1.41125 | 2.21769 | 2.80179 | 3.19849 | 3.64455 | 4.3671 | 5.32634 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.0167303 | 1.46277 | -3.07501 | -2.34526 | -1.23584 | 0.104253 | 1.1716 | 2.35205 | 3.09623 |
| bonus_part | alpha_1 | 4716 | 0.824699 | 0.37028 | 0.204191 | 0.41047 | 0.527159 | 0.735977 | 1.05125 | 1.47994 | 3.24043 |
| bonus_part | alpha_2 | 4716 | 0.817164 | 0.377656 | 0.190063 | 0.396773 | 0.555357 | 0.722152 | 0.979303 | 1.56047 | 3.85097 |
| bonus_part | alpha_3 | 4716 | 0.836161 | 0.448555 | 0.190684 | 0.43392 | 0.600341 | 0.728573 | 0.916038 | 1.6122 | 5.01854 |
| bonus_part | alpha_4 | 4716 | 0.833523 | 0.423348 | 0.193465 | 0.415353 | 0.565232 | 0.73627 | 0.960806 | 1.5981 | 4.13699 |
| bonus_part | alpha_5 | 4716 | 0.792638 | 0.324312 | 0.212569 | 0.431006 | 0.581509 | 0.725765 | 0.909849 | 1.38487 | 3.73527 |
| bonus_part | alpha_norm | 4716 | 1.94257 | 0.601475 | 0.858832 | 1.13901 | 1.49897 | 1.86433 | 2.27269 | 3.05873 | 5.28107 |
| synergy_player | psi_1 | 1755 | 0.0102564 | 0.248012 | -1.10242 | -0.384916 | -0.0621313 | -0.00159384 | 0.0617635 | 0.450278 | 1.16444 |
| synergy_player | psi_2 | 1755 | -0.00708138 | 0.254669 | -1.20515 | -0.45462 | -0.0671244 | -0.00305256 | 0.0593662 | 0.427777 | 1.25702 |
| synergy_player | psi_3 | 1755 | 0.00415881 | 0.256523 | -1.30097 | -0.451967 | -0.0596917 | 0.000191329 | 0.066635 | 0.412254 | 1.28941 |
| synergy_player | psi_norm | 1755 | 0.372362 | 0.231539 | 0.0127184 | 0.0755583 | 0.206112 | 0.340097 | 0.476322 | 0.846877 | 1.60302 |
| synergy | synergy_score | 3042 | 0.0740631 | 0.186131 | -0.994866 | -0.205406 | 0.000114896 | 0.0633578 | 0.151628 | 0.346577 | 1.6025 |
| synergy | synergy_contribution | 60454 | 0.337471 | 0.59676 | -1.02906 | -0.596527 | -0.0487983 | 0.286901 | 0.729148 | 1.39846 | 2.33893 |
