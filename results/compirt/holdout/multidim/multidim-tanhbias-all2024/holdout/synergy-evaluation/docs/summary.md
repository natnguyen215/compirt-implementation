# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanhbias-all2024/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanhbias-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 497672 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 100584 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.00628083 |
| mean_synergy_contribution | 0.548643 |
| median_synergy_contribution | 0.530772 |
| negative_synergy_fraction | 0.249479 |
| positive_synergy_fraction | 0.726139 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.938054 |
| log_loss | 0.314144 |
| ece | 0.00380027 |
| part_accuracy | 0.857335 |
| part_accuracy_macro_team | 0.857711 |
| part_accuracy_macro_game | 0.857649 |
| part_accuracy_macro_bonus | 0.871275 |
| exact_acc | 0.620571 |
| ppb_mae | 0.412961 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.671555 |
| log_loss | 0.564876 |
| ece | 0.107922 |
| accuracy | 0.730404 |
| buzz_position_mae | 0.135007 |
| buzz_position_median_absolute_error | 0.111379 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.927318 | 0.938054 | 0.0107367 | synergy |
| log_loss | 0.339205 | 0.314144 | -0.0250606 | synergy |
| ece | 0.00837581 | 0.00380027 | -0.00457554 | synergy |
| part_accuracy | 0.842552 | 0.857335 | 0.0147826 | synergy |
| part_accuracy_macro_team | 0.842337 | 0.857711 | 0.0153736 | synergy |
| part_accuracy_macro_game | 0.842776 | 0.857649 | 0.014873 | synergy |
| part_accuracy_macro_bonus | 0.858138 | 0.871275 | 0.0131379 | synergy |
| exact_acc | 0.587868 | 0.620571 | 0.0327026 | synergy |
| ppb_mae | 1.77381 | 0.412961 | -1.36085 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.49622 | 0.779438 | 2.29356 | 4.19984 | 4.96794 | 5.5384 | 6.00575 | 6.74688 | 8.44499 |
| player | theta_1 | 1755 | -3.2916 | 0.665342 | -5.2303 | -4.36354 | -3.75757 | -3.30021 | -2.84062 | -2.16655 | -1.2725 |
| player | theta_2 | 1755 | -2.92001 | 0.735641 | -5.40816 | -4.05034 | -3.47181 | -2.95009 | -2.38788 | -1.70628 | -0.636302 |
| player | theta_3 | 1755 | -2.98916 | 0.685566 | -5.89108 | -4.16118 | -3.44323 | -2.99162 | -2.54621 | -1.84432 | -0.09444 |
| player | theta_4 | 1755 | -2.58017 | 0.636231 | -4.49333 | -3.51123 | -3.07696 | -2.6202 | -2.17919 | -1.43478 | -0.618596 |
| player | theta_5 | 1755 | -1.87414 | 1.77712 | -6.30312 | -5.11397 | -3.37556 | -0.959908 | -0.65811 | -0.333662 | 0.949488 |
| player | theta_norm | 1755 | 6.53766 | 0.8598 | 4.50344 | 5.27005 | 5.89214 | 6.44067 | 7.13783 | 8.02229 | 9.70475 |
| tossup | gamma_1 | 1350 | 2.33279 | 14.6761 | 0.0193177 | 0.0958695 | 0.224616 | 0.490341 | 1.21443 | 4.96896 | 317.645 |
| tossup | gamma_2 | 1350 | 3.54432 | 21.9803 | 0.0198351 | 0.128088 | 0.277809 | 0.555249 | 1.95354 | 5.47601 | 454.584 |
| tossup | gamma_3 | 1350 | 2.93892 | 30.6405 | 0.0269112 | 0.133733 | 0.314046 | 0.634879 | 1.91042 | 5.77261 | 1101.83 |
| tossup | gamma_4 | 1350 | 3.45391 | 21.2487 | 0.0160616 | 0.13802 | 0.320271 | 0.610249 | 1.84909 | 5.07369 | 440.676 |
| tossup | gamma_5 | 1350 | 13.5979 | 58.8801 | 0.0946691 | 0.311841 | 0.943019 | 2.88399 | 4.52268 | 49.2338 | 916.576 |
| tossup | mu_1 | 1350 | 0.573747 | 0.112552 | 0.139918 | 0.381486 | 0.499101 | 0.582243 | 0.650543 | 0.752156 | 0.918357 |
| tossup | mu_2 | 1350 | 0.597124 | 0.1073 | 0.212761 | 0.407939 | 0.533232 | 0.602878 | 0.664487 | 0.758582 | 0.976418 |
| tossup | mu_3 | 1350 | 0.586241 | 0.111478 | 0.198091 | 0.408696 | 0.509548 | 0.593339 | 0.663861 | 0.763887 | 0.916721 |
| tossup | mu_4 | 1350 | 0.590556 | 0.104579 | 0.170674 | 0.415676 | 0.517519 | 0.597183 | 0.662824 | 0.751729 | 0.95513 |
| tossup | mu_5 | 1350 | 0.62687 | 0.133413 | 0.247311 | 0.392315 | 0.538714 | 0.631088 | 0.718126 | 0.839781 | 0.981805 |
| tossup | r_1 | 1350 | 1.18553 | 0.876599 | 0.0275778 | 0.118405 | 0.422071 | 1.0399 | 1.78079 | 2.78098 | 6.92888 |
| tossup | r_2 | 1350 | 0.678228 | 0.585344 | 0.0216211 | 0.0593041 | 0.238986 | 0.501171 | 0.97688 | 1.84979 | 4.34582 |
| tossup | r_3 | 1350 | 0.721982 | 0.742387 | 0.0242804 | 0.0702691 | 0.216265 | 0.441854 | 0.947984 | 2.34012 | 5.59795 |
| tossup | r_4 | 1350 | 0.753568 | 0.862459 | 0.0241192 | 0.0597154 | 0.184402 | 0.382366 | 0.937564 | 2.68675 | 7.08324 |
| tossup | r_5 | 1350 | 0.347395 | 0.553918 | 0.0162177 | 0.031399 | 0.0627534 | 0.16334 | 0.348942 | 1.50338 | 8.04911 |
| tossup | r_norm | 1350 | 2.26929 | 0.798071 | 0.249386 | 0.971201 | 1.78112 | 2.2401 | 2.76466 | 3.53943 | 8.08653 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | -0.00367762 | 0.558532 | -1.63032 | -0.900789 | -0.412257 | -0.0289384 | 0.443988 | 0.870964 | 1.69015 |
| bonus_part | alpha_1 | 4716 | 0.0771586 | 0.563469 | -1.46871 | -0.764973 | -0.380205 | 0.0699803 | 0.522514 | 0.957139 | 1.92203 |
| bonus_part | alpha_2 | 4716 | 0.0497059 | 0.630215 | -1.81964 | -0.799375 | -0.498243 | -0.0111252 | 0.549241 | 1.11613 | 2.19176 |
| bonus_part | alpha_3 | 4716 | 0.0516054 | 0.606648 | -1.53372 | -0.761143 | -0.469537 | 0.00131517 | 0.515513 | 1.06469 | 2.28861 |
| bonus_part | alpha_4 | 4716 | 0.0997414 | 0.674629 | -1.645 | -0.789936 | -0.471447 | 0.0151384 | 0.614352 | 1.31277 | 2.37263 |
| bonus_part | alpha_5 | 4716 | 0.009433 | 0.589686 | -1.87898 | -0.869401 | -0.41352 | -0.0287123 | 0.421784 | 0.998955 | 1.94768 |
| bonus_part | alpha_norm | 4716 | 1.31969 | 0.405864 | 0.142275 | 0.665282 | 1.03659 | 1.32582 | 1.58613 | 2.01248 | 3.03873 |
