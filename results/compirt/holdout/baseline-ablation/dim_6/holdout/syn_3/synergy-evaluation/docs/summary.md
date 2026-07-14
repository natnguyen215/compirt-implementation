# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_6/holdout/syn_3/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_6/holdout/syn_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 6 |
| synergy | steps | 2000 |
| synergy | final_loss | 85458.9 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.553385 |
| mean_synergy_contribution | -0.587365 |
| median_synergy_contribution | -0.545316 |
| negative_synergy_fraction | 0.762001 |
| positive_synergy_fraction | 0.213617 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.940361 |
| log_loss | 0.32217 |
| ece | 0.0386174 |
| part_accuracy | 0.861349 |
| exact_acc | 0.631075 |
| per_bonus_points_mae | 4.53213 |
| ppb_mae | 1.71414 |
| accuracy | 0.861349 |

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
| bonus_part | beta | 4716 | 0.334029 | 1.47005 | -2.88313 | -1.99533 | -0.939874 | 0.426683 | 1.54574 | 2.57972 | 4.11307 |
| bonus_part | alpha_1 | 4716 | -0.0149387 | 0.425342 | -2.35183 | -0.714076 | -0.202353 | -0.00622197 | 0.198208 | 0.656283 | 1.88711 |
| bonus_part | alpha_2 | 4716 | -0.0109993 | 0.592486 | -2.09857 | -1.0661 | -0.367272 | 0.030433 | 0.393027 | 0.895245 | 2.13473 |
| bonus_part | alpha_3 | 4716 | 0.0350763 | 0.413756 | -1.7517 | -0.653565 | -0.191296 | 0.0379244 | 0.267702 | 0.718463 | 2.02219 |
| bonus_part | alpha_4 | 4716 | 0.154008 | 0.657827 | -1.8965 | -0.860427 | -0.301191 | 0.121796 | 0.546689 | 1.31067 | 2.69875 |
| bonus_part | alpha_5 | 4716 | 0.0211688 | 0.570952 | -1.73016 | -0.846284 | -0.379399 | 0.0100398 | 0.382798 | 0.977303 | 2.6363 |
| bonus_part | alpha_6 | 4716 | -0.0285409 | 0.517208 | -2.6132 | -0.936814 | -0.321152 | -0.00850148 | 0.314237 | 0.730084 | 1.71896 |
| bonus_part | alpha_norm | 4716 | 1.2232 | 0.509305 | 0.12448 | 0.46241 | 0.850623 | 1.19564 | 1.51797 | 2.17917 | 3.33025 |
