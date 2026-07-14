# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/in_sample_2024nationals/plda/synergy-evaluation`
Result root: `results/compirt/in_sample/in_sample_2024nationals/plda`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 64422.1 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| pyramidal | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 11464.9 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |
| synergy | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.340013 |
| mean_synergy_contribution | -1.38436 |
| median_synergy_contribution | -1.32781 |
| negative_synergy_fraction | 0.999145 |
| positive_synergy_fraction | 0 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.918728 |
| log_loss | 0.408651 |
| ece | 0.108074 |
| part_accuracy | 0.844805 |
| exact_score_accuracy | 0.591991 |
| per_bonus_points_mae | 4.8559 |
| ppb_mae | 1.70766 |
| accuracy | 0.844805 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.656791 |
| log_loss | 0.62707 |
| ece | 0.157313 |
| accuracy | 0.661965 |
| buzz_position_mae | 0.170267 |
| buzz_position_median_absolute_error | 0.165268 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 5.59555 | 0.358326 | 4.02174 | 5.06014 | 5.35268 | 5.62476 | 5.8107 | 6.1378 | 6.32741 |
| player | theta_1 | 189 | 0.188718 | 0.996277 | -1.82242 | -1.25331 | -0.603155 | 0.112598 | 0.912698 | 1.94469 | 2.52265 |
| player | theta_2 | 189 | 0.196799 | 1.11473 | -1.90016 | -1.39199 | -0.599439 | 0.0394632 | 0.968174 | 2.0979 | 3.20046 |
| player | theta_3 | 189 | 0.227878 | 1.09403 | -1.90637 | -1.38299 | -0.728576 | 0.272704 | 0.942459 | 2.17812 | 3.46466 |
| player | theta_4 | 189 | 0.0742984 | 1.19243 | -2.06281 | -1.68615 | -0.888489 | -0.100414 | 0.931674 | 2.24107 | 2.7131 |
| player | theta_5 | 189 | 0.0603718 | 1.03416 | -1.89977 | -1.48049 | -0.728511 | 0.0186422 | 0.769256 | 1.87273 | 2.71359 |
| player | theta_norm | 189 | 2.35697 | 0.68904 | 0.766921 | 1.15827 | 1.96432 | 2.30369 | 2.77444 | 3.60277 | 5.12662 |
| tossup | beta_1 | 360 | 1.00368 | 1.18422 | -0.145583 | -0.0103431 | 0.115301 | 0.472859 | 1.49684 | 3.55345 | 4.47738 |
| tossup | beta_2 | 360 | 1.15426 | 1.3294 | -0.152261 | -0.0175125 | 0.102688 | 0.464094 | 2.24384 | 3.74944 | 4.56896 |
| tossup | beta_3 | 360 | 0.988699 | 1.38199 | -0.144656 | -0.0482755 | 0.0215449 | 0.157993 | 2.46568 | 3.52984 | 4.01612 |
| tossup | beta_4 | 360 | 1.14526 | 1.40078 | -0.137823 | -0.0311571 | 0.0578117 | 0.38001 | 2.22171 | 3.84439 | 4.58722 |
| tossup | beta_5 | 360 | 0.811026 | 1.13647 | -0.108072 | -0.0271913 | 0.0469284 | 0.273244 | 1.03453 | 3.45255 | 4.35533 |
| tossup | gamma_1 | 360 | 16.4346 | 44.52 | 4.30056 | 4.62726 | 5.11129 | 5.87852 | 10.5813 | 45.1391 | 494.171 |
| tossup | gamma_2 | 360 | 18.6552 | 42.3118 | 4.19819 | 4.71398 | 5.15742 | 5.75245 | 13.487 | 65.2272 | 462.271 |
| tossup | gamma_3 | 360 | 13.3075 | 25.4654 | 4.30988 | 4.64955 | 4.99411 | 5.29945 | 10.0446 | 45.4995 | 344.448 |
| tossup | gamma_4 | 360 | 16.4469 | 29.9371 | 4.26544 | 4.67359 | 5.04308 | 5.62679 | 13.1246 | 65.9624 | 234.617 |
| tossup | gamma_5 | 360 | 11.8179 | 23.2014 | 4.24117 | 4.60149 | 5.01451 | 5.39068 | 7.30665 | 38.7844 | 306.584 |
| tossup | mu_1 | 360 | 0.542562 | 0.0892693 | 0.414856 | 0.472461 | 0.491984 | 0.507085 | 0.547689 | 0.733467 | 0.907569 |
| tossup | mu_2 | 360 | 0.55356 | 0.0930852 | 0.397085 | 0.476529 | 0.496995 | 0.511544 | 0.585872 | 0.762472 | 0.894894 |
| tossup | mu_3 | 360 | 0.547122 | 0.0943382 | 0.439072 | 0.476551 | 0.493682 | 0.505424 | 0.554589 | 0.758881 | 0.930181 |
| tossup | mu_4 | 360 | 0.554945 | 0.0975357 | 0.431324 | 0.476561 | 0.495316 | 0.510303 | 0.582306 | 0.778309 | 0.90296 |
| tossup | mu_5 | 360 | 0.529901 | 0.0756285 | 0.329494 | 0.474986 | 0.492629 | 0.503543 | 0.525862 | 0.701099 | 0.866812 |
| tossup | topic_weight_1 | 360 | 0.201924 | 0.199241 | 0.00392111 | 0.00586507 | 0.0406952 | 0.152056 | 0.291651 | 0.628855 | 0.926751 |
| tossup | topic_weight_2 | 360 | 0.206319 | 0.198213 | 0.00398982 | 0.00581619 | 0.0327229 | 0.141286 | 0.322207 | 0.599221 | 0.84832 |
| tossup | topic_weight_3 | 360 | 0.22347 | 0.312012 | 0.0027962 | 0.00332675 | 0.00522799 | 0.0446618 | 0.397554 | 0.879803 | 0.981607 |
| tossup | topic_weight_4 | 360 | 0.211833 | 0.233617 | 0.0036341 | 0.00481661 | 0.0143924 | 0.113861 | 0.351439 | 0.696429 | 0.953908 |
| tossup | topic_weight_5 | 360 | 0.156453 | 0.186828 | 0.00295113 | 0.00396609 | 0.0090372 | 0.0813912 | 0.223781 | 0.597685 | 0.854723 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 1071 | 0.0310065 | 0.667532 | -2.55717 | -1.20219 | -0.141204 | 0.0145099 | 0.239914 | 1.15947 | 2.51222 |
| bonus_part | beta_2 | 1071 | 0.0663541 | 0.836031 | -2.71791 | -1.42964 | -0.232677 | 0.0288601 | 0.429039 | 1.58863 | 2.64609 |
| bonus_part | beta_3 | 1071 | 0.0410722 | 0.817881 | -2.7268 | -1.5502 | -0.0888331 | 0.0129814 | 0.171941 | 1.70453 | 2.53561 |
| bonus_part | beta_4 | 1071 | 0.0271058 | 0.685516 | -2.56724 | -1.20352 | -0.0989904 | 0.0152162 | 0.16592 | 1.26238 | 2.34421 |
| bonus_part | beta_5 | 1071 | 0.0352241 | 0.763502 | -2.61645 | -1.41608 | -0.138736 | 0.0228972 | 0.26462 | 1.3926 | 2.51032 |
| synergy_player | psi_1 | 189 | -0.0034019 | 0.458831 | -1.4552 | -0.853142 | -0.0657903 | -0.00270959 | 0.0463282 | 0.760253 | 1.46643 |
| synergy_player | psi_2 | 189 | 0.000566933 | 0.569211 | -1.45082 | -0.955747 | -0.258414 | 0.00679865 | 0.315859 | 1.04322 | 1.47497 |
| synergy_player | psi_3 | 189 | 0.00345002 | 0.458565 | -1.34356 | -0.753786 | -0.0874155 | 0.00429147 | 0.08764 | 0.819262 | 1.44387 |
| synergy_player | psi_norm | 189 | 0.792299 | 0.337278 | 0.0758073 | 0.445082 | 0.553167 | 0.631181 | 1.03419 | 1.44745 | 1.52423 |
| synergy | synergy_score | 274 | -0.244858 | 0.566824 | -1.38399 | -0.995139 | -0.758328 | -0.453431 | 0.307569 | 0.423777 | 0.957323 |
| synergy | synergy_contribution | 7017 | -1.38436 | 0.231028 | -1.90662 | -1.71966 | -1.55986 | -1.32781 | -1.21621 | -1.0539 | 0 |
