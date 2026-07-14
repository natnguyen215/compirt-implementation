# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_6/holdout/syn_1/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_6/holdout/syn_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 6 |
| synergy | steps | 2000 |
| synergy | final_loss | 83020.7 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.655696 |
| mean_synergy_contribution | -0.724454 |
| median_synergy_contribution | -0.675255 |
| negative_synergy_fraction | 0.844411 |
| positive_synergy_fraction | 0.131207 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.940237 |
| log_loss | 0.322907 |
| ece | 0.0396771 |
| part_accuracy | 0.860941 |
| exact_acc | 0.629801 |
| per_bonus_points_mae | 4.53672 |
| ppb_mae | 1.702 |
| accuracy | 0.860941 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.691294 |
| log_loss | 0.58649 |
| ece | 0.14959 |
| accuracy | 0.703659 |
| buzz_position_mae | 0.14111 |
| buzz_position_median_absolute_error | 0.122507 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.9815 | 0.795546 | 1.54546 | 3.40224 | 4.60923 | 5.10119 | 5.51704 | 6.0438 | 6.94687 |
| player | theta_1 | 1755 | 0.0865676 | 0.515783 | -1.93285 | -0.822311 | -0.213187 | 0.10033 | 0.41564 | 0.917022 | 1.98769 |
| player | theta_2 | 1755 | -0.233001 | 0.794109 | -2.0731 | -1.35379 | -0.767224 | -0.331759 | 0.172499 | 1.19267 | 2.82653 |
| player | theta_3 | 1755 | -0.0579003 | 0.522234 | -1.74159 | -0.958271 | -0.410601 | -0.0470353 | 0.287305 | 0.786366 | 1.95416 |
| player | theta_4 | 1755 | -0.150364 | 0.796029 | -3.18359 | -1.40802 | -0.635525 | -0.164728 | 0.349216 | 1.16126 | 2.49111 |
| player | theta_5 | 1755 | 0.0819832 | 0.750392 | -2.09145 | -1.31529 | -0.399103 | 0.161567 | 0.631798 | 1.22762 | 1.93967 |
| player | theta_6 | 1755 | -0.029169 | 0.651001 | -2.3556 | -1.12614 | -0.470948 | 0.0148698 | 0.441496 | 0.965721 | 1.9911 |
| player | theta_norm | 1755 | 1.6228 | 0.500295 | 0.438693 | 0.877063 | 1.2675 | 1.58669 | 1.91543 | 2.44842 | 3.49556 |
| tossup | beta | 1350 | 3.35263 | 0.783921 | 0.492665 | 1.94368 | 2.92703 | 3.40477 | 3.85978 | 4.50641 | 5.44633 |
| tossup | gamma | 1350 | 57.6578 | 182.3 | 2.62334 | 5.90258 | 9.11278 | 13.3628 | 27.2344 | 206.503 | 2449.2 |
| tossup | mu | 1350 | 0.588854 | 0.132459 | 0.11132 | 0.362138 | 0.504162 | 0.586082 | 0.676557 | 0.80738 | 0.985474 |
| tossup | alpha_1 | 1350 | -0.028611 | 0.580521 | -1.94061 | -1.16246 | -0.330915 | 0.0620652 | 0.374436 | 0.786478 | 1.58095 |
| tossup | alpha_2 | 1350 | -0.133968 | 0.844972 | -2.89451 | -1.73095 | -0.550993 | -0.0267956 | 0.443344 | 1.10525 | 2.20547 |
| tossup | alpha_3 | 1350 | -0.103431 | 0.629182 | -2.44987 | -1.14636 | -0.556022 | -0.0762691 | 0.330078 | 0.88011 | 1.58034 |
| tossup | alpha_4 | 1350 | 0.836709 | 0.705497 | -0.982563 | -0.313428 | 0.346609 | 0.817721 | 1.31492 | 2.03943 | 2.76758 |
| tossup | alpha_5 | 1350 | 0.398131 | 0.730023 | -1.77934 | -0.820106 | -0.0667157 | 0.411137 | 0.868774 | 1.6436 | 2.83544 |
| tossup | alpha_6 | 1350 | -0.277286 | 0.701844 | -2.62676 | -1.74811 | -0.560432 | -0.11031 | 0.198283 | 0.628031 | 1.37124 |
| tossup | alpha_norm | 1350 | 1.92024 | 0.495668 | 0.35019 | 1.10854 | 1.58176 | 1.91821 | 2.23668 | 2.74381 | 3.46471 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.29065 | 1.45685 | -2.90961 | -2.02366 | -0.96673 | 0.389105 | 1.4857 | 2.52229 | 4.038 |
| bonus_part | alpha_1 | 4716 | -0.0147399 | 0.423939 | -2.34565 | -0.709326 | -0.204443 | -0.00497768 | 0.199789 | 0.653954 | 1.83696 |
| bonus_part | alpha_2 | 4716 | -0.0166034 | 0.590871 | -2.13117 | -1.0624 | -0.37504 | 0.0269032 | 0.388544 | 0.888424 | 2.09849 |
| bonus_part | alpha_3 | 4716 | 0.0340677 | 0.41195 | -1.73019 | -0.654989 | -0.19227 | 0.0344663 | 0.266127 | 0.715225 | 2.02683 |
| bonus_part | alpha_4 | 4716 | 0.152334 | 0.656311 | -1.88029 | -0.855739 | -0.302523 | 0.116302 | 0.543477 | 1.30847 | 2.71655 |
| bonus_part | alpha_5 | 4716 | 0.0249064 | 0.568352 | -1.70669 | -0.835787 | -0.370294 | 0.01016 | 0.385401 | 0.98428 | 2.63192 |
| bonus_part | alpha_6 | 4716 | -0.0281013 | 0.515917 | -2.59081 | -0.928892 | -0.322359 | -0.00881995 | 0.316119 | 0.733107 | 1.71628 |
| bonus_part | alpha_norm | 4716 | 1.21992 | 0.506205 | 0.122083 | 0.464063 | 0.843173 | 1.19442 | 1.51855 | 2.16061 | 3.34845 |
