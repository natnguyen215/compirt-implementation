# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/lda-all2024/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/lda-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 476713 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| pyramidal | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 86726.5 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |
| synergy | topic_vectors | topic/fixed/outputs/lda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.359565 |
| mean_synergy_contribution | -0.809161 |
| median_synergy_contribution | -0.792739 |
| negative_synergy_fraction | 0.841251 |
| positive_synergy_fraction | 0.134367 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.917409 |
| log_loss | 0.379104 |
| ece | 0.0555877 |
| part_accuracy | 0.837981 |
| exact_score_accuracy | 0.575396 |
| rounded_score_accuracy | 0.58155 |
| per_bonus_points_mae | 4.95794 |
| ppb_mae | 1.7856 |
| accuracy | 0.837981 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.650061 |
| log_loss | 0.620788 |
| ece | 0.181646 |
| accuracy | 0.672903 |
| buzz_position_mae | 0.1581 |
| buzz_position_median_absolute_error | 0.140271 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.24388 | 0.433487 | 3.21044 | 4.57547 | 4.96041 | 5.24625 | 5.52115 | 5.97125 | 6.74891 |
| player | theta_1 | 1755 | 0.212227 | 1.1586 | -2.17341 | -1.41022 | -0.733384 | 0.134047 | 0.978315 | 2.32784 | 4.05203 |
| player | theta_2 | 1755 | 0.260838 | 0.936544 | -1.86777 | -1.13117 | -0.471956 | 0.242156 | 0.955267 | 1.8465 | 3.20168 |
| player | theta_3 | 1755 | 0.254707 | 1.24621 | -2.40397 | -1.59036 | -0.716746 | 0.185025 | 1.17951 | 2.38586 | 3.78691 |
| player | theta_4 | 1755 | 0.1324 | 0.903448 | -1.63818 | -0.904389 | -0.493509 | -0.0845984 | 0.542979 | 2.00502 | 4.60086 |
| player | theta_5 | 1755 | 0.146342 | 1.25318 | -2.47843 | -1.61005 | -0.791534 | 0.0259618 | 0.889743 | 2.45317 | 4.62922 |
| player | theta_norm | 1755 | 2.353 | 0.914585 | 0.502584 | 1.12703 | 1.70922 | 2.21449 | 2.85703 | 4.10828 | 6.32198 |
| tossup | beta_1 | 1350 | 0.909622 | 1.45678 | -1.73082 | -0.0678895 | 0.00864749 | 0.10812 | 1.09396 | 3.94065 | 5.05557 |
| tossup | beta_2 | 1350 | 1.22577 | 1.51954 | -4.63047 | -0.0482011 | 0.0847417 | 0.470541 | 2.2483 | 4.24383 | 5.01275 |
| tossup | beta_3 | 1350 | 1.20987 | 1.56452 | -5.14264 | -0.0603159 | 0.0669193 | 0.392947 | 2.44526 | 4.21447 | 5.26074 |
| tossup | beta_4 | 1350 | 0.342705 | 0.970874 | -0.781292 | -0.0754976 | -0.0196583 | 0.0224574 | 0.096071 | 3.33298 | 4.71696 |
| tossup | beta_5 | 1350 | 1.25182 | 1.62516 | -3.39852 | -0.0561958 | 0.0617716 | 0.375839 | 2.48043 | 4.46577 | 5.55303 |
| tossup | gamma_1 | 1350 | 16.0083 | 69.479 | 1.7022 | 4.5505 | 4.90211 | 5.20525 | 6.50004 | 33.4076 | 1321.21 |
| tossup | gamma_2 | 1350 | 25.613 | 97.8923 | 2.26813 | 4.61501 | 5.03414 | 5.51595 | 10.6003 | 80.8264 | 1848.67 |
| tossup | gamma_3 | 1350 | 26.6929 | 105.96 | 1.04761 | 4.58934 | 5.04799 | 5.45876 | 10.2658 | 80.3431 | 1831.18 |
| tossup | gamma_4 | 1350 | 14.0783 | 95.5592 | 3.89331 | 4.52422 | 4.81803 | 5.04769 | 5.3208 | 16.4279 | 2240.56 |
| tossup | gamma_5 | 1350 | 23.1691 | 106.2 | 0.293318 | 4.55993 | 4.99332 | 5.41857 | 10.0423 | 63.3989 | 1868.13 |
| tossup | mu_1 | 1350 | 0.52296 | 0.0823803 | 0.149905 | 0.456787 | 0.490658 | 0.502816 | 0.519189 | 0.708356 | 0.97849 |
| tossup | mu_2 | 1350 | 0.534032 | 0.0990893 | 0.221784 | 0.438308 | 0.488144 | 0.505121 | 0.545922 | 0.757582 | 0.94182 |
| tossup | mu_3 | 1350 | 0.52257 | 0.0923914 | 0.136193 | 0.412375 | 0.487053 | 0.503378 | 0.530368 | 0.71118 | 0.968756 |
| tossup | mu_4 | 1350 | 0.512877 | 0.0624825 | 0.109147 | 0.475584 | 0.491141 | 0.501706 | 0.512217 | 0.631097 | 0.955445 |
| tossup | mu_5 | 1350 | 0.539636 | 0.104 | 0.211297 | 0.435481 | 0.488919 | 0.505005 | 0.550129 | 0.774353 | 0.971671 |
| tossup | topic_weight_1 | 1350 | 0.218069 | 0.342105 | 0.00285499 | 0.00342265 | 0.00389982 | 0.0325199 | 0.212112 | 0.945478 | 0.984634 |
| tossup | topic_weight_2 | 1350 | 0.226277 | 0.240582 | 0.00512236 | 0.00639485 | 0.0377977 | 0.126754 | 0.352091 | 0.742052 | 0.956967 |
| tossup | topic_weight_3 | 1350 | 0.245531 | 0.288679 | 0.00479686 | 0.00593483 | 0.0242585 | 0.105729 | 0.406981 | 0.849477 | 0.983099 |
| tossup | topic_weight_4 | 1350 | 0.0702435 | 0.189705 | 0.00110557 | 0.00128605 | 0.00143514 | 0.00159348 | 0.0203562 | 0.635436 | 0.974287 |
| tossup | topic_weight_5 | 1350 | 0.23988 | 0.281031 | 0.0042974 | 0.00519295 | 0.0234817 | 0.103026 | 0.38706 | 0.830482 | 0.981875 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| synergy_player | psi_1 | 1755 | -0.00193276 | 0.371738 | -1.68435 | -0.686307 | -0.0626587 | -0.00215969 | 0.0628943 | 0.668878 | 1.5998 |
| synergy_player | psi_2 | 1755 | -0.00478443 | 0.411485 | -1.55869 | -0.777715 | -0.0826654 | -0.00208626 | 0.0674072 | 0.742422 | 1.68185 |
| synergy_player | psi_3 | 1755 | -0.00166683 | 0.38654 | -1.72922 | -0.695732 | -0.0665836 | 0.00258354 | 0.0643332 | 0.669151 | 1.77862 |
| synergy_player | psi_norm | 1755 | 0.535828 | 0.411918 | 0.00617407 | 0.0524297 | 0.188349 | 0.43227 | 0.827441 | 1.34686 | 1.98993 |
| synergy | synergy_score | 3042 | -0.138549 | 0.416672 | -2.5494 | -0.97666 | -0.294315 | -0.00241955 | 0.0696815 | 0.33167 | 1.49451 |
| synergy | synergy_contribution | 60454 | -0.809161 | 0.71834 | -2.5494 | -1.9591 | -1.39419 | -0.792739 | -0.133229 | 0.229549 | 1.14015 |
