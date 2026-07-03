# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim-ablation/dim_2/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/multidim-ablation/dim_2`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 471255 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 2 |
| synergy | steps | 2000 |
| synergy | final_loss | 84680.9 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.0701812 |
| mean_synergy_contribution | 0.0145389 |
| median_synergy_contribution | 0 |
| negative_synergy_fraction | 0.487594 |
| positive_synergy_fraction | 0.48943 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.924843 |
| log_loss | 0.353452 |
| ece | 0.0297067 |
| part_accuracy | 0.843716 |
| exact_score_accuracy | 0.587736 |
| rounded_score_accuracy | 0.591921 |
| per_bonus_points_mae | 4.89626 |
| ppb_mae | 1.69955 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.649391 |
| log_loss | 0.624876 |
| ece | 0.151855 |
| buzz_position_mae | 0.140936 |
| buzz_position_median_absolute_error | 0.119122 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1791 | 5.08786 | 1.09947 | 1.4326 | 2.48092 | 4.67794 | 5.27745 | 5.76151 | 6.505 | 7.80092 |
| player | theta_1 | 1791 | 0.22718 | 0.662017 | -2.01289 | -1.31237 | -0.0435539 | 0.341107 | 0.669168 | 1.07786 | 1.72346 |
| player | theta_2 | 1791 | 0.236505 | 0.621842 | -2.1423 | -1.21162 | -0.0373934 | 0.31139 | 0.627111 | 1.10733 | 2.07408 |
| player | theta_norm | 1791 | 0.848947 | 0.459833 | 0.023435 | 0.24344 | 0.523685 | 0.772018 | 1.08274 | 1.7593 | 2.64665 |
| tossup | beta_1 | 1350 | 1.33036 | 0.64099 | -0.0466752 | 0.266881 | 0.856855 | 1.38744 | 1.80536 | 2.33141 | 3.21071 |
| tossup | beta_2 | 1350 | 1.2106 | 0.649447 | -0.858484 | 0.235986 | 0.63894 | 1.23468 | 1.68023 | 2.25062 | 3.08054 |
| tossup | gamma_1 | 1350 | 34.9591 | 144.038 | 0.737571 | 2.29826 | 4.24743 | 5.55613 | 11.0349 | 105.492 | 1956.07 |
| tossup | gamma_2 | 1350 | 24.304 | 105.268 | 0.445039 | 2.27125 | 4.0347 | 5.2129 | 8.24871 | 67.5806 | 2129 |
| tossup | mu_1 | 1350 | 0.557828 | 0.157006 | 0.110939 | 0.318311 | 0.446765 | 0.542802 | 0.666103 | 0.833636 | 0.993314 |
| tossup | mu_2 | 1350 | 0.547337 | 0.152382 | 0.124425 | 0.313927 | 0.446719 | 0.523042 | 0.647421 | 0.808731 | 0.993569 |
| tossup | alpha_1 | 1350 | 2.10933 | 1.09326 | 0.121336 | 0.327739 | 1.2784 | 2.20691 | 2.8917 | 3.8124 | 5.99561 |
| tossup | alpha_2 | 1350 | 1.97113 | 1.18645 | 0.0898335 | 0.310554 | 0.948806 | 1.92428 | 2.83905 | 3.96259 | 7.13895 |
| tossup | alpha_norm | 1350 | 3.1287 | 1.0713 | 0.822892 | 1.61671 | 2.41055 | 3.03431 | 3.68907 | 4.99006 | 9.32266 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.242962 | 1.44951 | -3.09307 | -2.11162 | -0.995906 | 0.339475 | 1.42686 | 2.44813 | 3.97918 |
| bonus_part | alpha_1 | 4716 | 0.106167 | 0.639824 | -2.06834 | -0.872472 | -0.323364 | 0.0472087 | 0.487725 | 1.2405 | 2.17836 |
| bonus_part | alpha_2 | 4716 | 0.115573 | 0.66961 | -1.95979 | -0.946058 | -0.339196 | 0.0691056 | 0.561039 | 1.26944 | 2.37457 |
| bonus_part | alpha_norm | 4716 | 0.790563 | 0.507212 | 0.00153071 | 0.13598 | 0.367294 | 0.687213 | 1.16813 | 1.68928 | 2.65367 |
