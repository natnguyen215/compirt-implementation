# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim-ablation/dim_5/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/multidim-ablation/dim_5`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 472661 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 85916.2 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.371686 |
| mean_synergy_contribution | -0.382091 |
| median_synergy_contribution | -0.323311 |
| negative_synergy_fraction | 0.66128 |
| positive_synergy_fraction | 0.315744 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.93522 |
| log_loss | 0.334592 |
| ece | 0.0391442 |
| part_accuracy | 0.854716 |
| exact_score_accuracy | 0.615509 |
| per_bonus_points_mae | 4.66959 |
| ppb_mae | 1.73147 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.673183 |
| log_loss | 0.602057 |
| ece | 0.139912 |
| accuracy | 0.703335 |
| buzz_position_mae | 0.135109 |
| buzz_position_median_absolute_error | 0.113291 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1791 | 4.88488 | 1.07642 | 1.42208 | 2.27814 | 4.45387 | 5.09261 | 5.60178 | 6.20648 | 7.18004 |
| player | theta_1 | 1791 | 0.0733064 | 0.572891 | -1.96472 | -0.919171 | -0.294595 | 0.122576 | 0.480538 | 0.962644 | 1.74354 |
| player | theta_2 | 1791 | 0.052617 | 0.643838 | -1.79736 | -1.13754 | -0.345171 | 0.124808 | 0.54354 | 0.99335 | 1.53598 |
| player | theta_3 | 1791 | -0.0804882 | 0.60877 | -2.66681 | -1.10548 | -0.496758 | -0.0222962 | 0.3412 | 0.835554 | 1.90345 |
| player | theta_4 | 1791 | 0.220209 | 0.614656 | -1.87738 | -1.09911 | -0.117222 | 0.306648 | 0.645299 | 1.09422 | 2.11122 |
| player | theta_5 | 1791 | 0.160798 | 0.616973 | -2.46461 | -1.07876 | -0.185899 | 0.243927 | 0.584299 | 1.02819 | 2.00918 |
| player | theta_norm | 1791 | 1.32101 | 0.463436 | 0.324238 | 0.671568 | 0.97796 | 1.25725 | 1.59989 | 2.22682 | 3.21932 |
| tossup | beta_1 | 1350 | 0.673199 | 0.480902 | -3.60647 | 0.136026 | 0.407238 | 0.582971 | 0.864536 | 1.56011 | 2.60096 |
| tossup | beta_2 | 1350 | 0.853941 | 0.602107 | -1.9589 | 0.158122 | 0.395223 | 0.630188 | 1.31604 | 1.98478 | 2.85157 |
| tossup | beta_3 | 1350 | 0.744198 | 0.540111 | -0.267962 | 0.120873 | 0.384079 | 0.576381 | 1.02157 | 1.86721 | 3.0489 |
| tossup | beta_4 | 1350 | 0.819112 | 0.489541 | -1.60806 | 0.200825 | 0.478489 | 0.702828 | 1.11325 | 1.74703 | 2.61406 |
| tossup | beta_5 | 1350 | 0.755464 | 0.520181 | -1.07947 | 0.189886 | 0.414828 | 0.570627 | 1.03021 | 1.84853 | 2.78478 |
| tossup | gamma_1 | 1350 | 11.6769 | 55.588 | 0.054091 | 2.70055 | 4.11715 | 4.84153 | 5.74377 | 23.6607 | 1290.63 |
| tossup | gamma_2 | 1350 | 27.1593 | 140.444 | 0.227244 | 3.29227 | 4.48648 | 5.1639 | 7.15898 | 67.1785 | 2204.4 |
| tossup | gamma_3 | 1350 | 15.5079 | 73.0798 | 0.789251 | 2.81887 | 4.28415 | 4.94922 | 5.90593 | 27.7669 | 1454.42 |
| tossup | gamma_4 | 1350 | 16.1359 | 81.9418 | 0.110004 | 2.47801 | 3.94327 | 4.88846 | 6.12772 | 31.4404 | 1675.9 |
| tossup | gamma_5 | 1350 | 15.9045 | 78.5046 | 0.524837 | 2.88412 | 4.3378 | 4.99689 | 5.94789 | 27.3335 | 1408.36 |
| tossup | mu_1 | 1350 | 0.498671 | 0.106607 | 0.126653 | 0.372607 | 0.441091 | 0.47806 | 0.530026 | 0.712407 | 0.98458 |
| tossup | mu_2 | 1350 | 0.500803 | 0.116066 | 0.129074 | 0.357244 | 0.437842 | 0.475456 | 0.539103 | 0.742882 | 0.991845 |
| tossup | mu_3 | 1350 | 0.503345 | 0.116883 | 0.14981 | 0.375847 | 0.43434 | 0.473235 | 0.538603 | 0.738908 | 0.993531 |
| tossup | mu_4 | 1350 | 0.521547 | 0.126801 | 0.114743 | 0.360164 | 0.444892 | 0.491841 | 0.579423 | 0.761846 | 0.992523 |
| tossup | mu_5 | 1350 | 0.497764 | 0.108502 | 0.122194 | 0.367879 | 0.441143 | 0.476311 | 0.524477 | 0.726105 | 0.989295 |
| tossup | alpha_1 | 1350 | 1.00502 | 0.753703 | 0.0907372 | 0.242339 | 0.457622 | 0.759441 | 1.34841 | 2.59909 | 4.72221 |
| tossup | alpha_2 | 1350 | 1.24402 | 0.953611 | 0.0621194 | 0.249438 | 0.512961 | 0.872442 | 1.84578 | 3.18185 | 4.72099 |
| tossup | alpha_3 | 1350 | 1.08545 | 0.803201 | 0.069182 | 0.228685 | 0.501108 | 0.841036 | 1.45852 | 2.82879 | 4.32078 |
| tossup | alpha_4 | 1350 | 1.36857 | 0.981066 | 0.0672923 | 0.276757 | 0.566322 | 1.11683 | 1.97383 | 3.20998 | 6.94375 |
| tossup | alpha_5 | 1350 | 1.08793 | 0.845263 | 0.0949147 | 0.24246 | 0.45264 | 0.768245 | 1.51857 | 2.87505 | 4.55778 |
| tossup | alpha_norm | 1350 | 3.14582 | 0.832729 | 1.20262 | 1.90092 | 2.58064 | 3.08888 | 3.61023 | 4.56887 | 8.30708 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.310461 | 1.49155 | -2.97629 | -2.13522 | -0.970362 | 0.433175 | 1.52459 | 2.58155 | 4.11493 |
| bonus_part | alpha_1 | 4716 | 0.0488623 | 0.522779 | -1.93037 | -0.80888 | -0.285928 | 0.057761 | 0.376681 | 0.873176 | 2.56454 |
| bonus_part | alpha_2 | 4716 | 0.0628317 | 0.508267 | -1.89607 | -0.694985 | -0.249042 | 0.0380046 | 0.343873 | 0.892794 | 2.71678 |
| bonus_part | alpha_3 | 4716 | 0.104843 | 0.481812 | -1.59101 | -0.662578 | -0.193036 | 0.0889395 | 0.398505 | 0.909169 | 1.95706 |
| bonus_part | alpha_4 | 4716 | 0.0648472 | 0.616251 | -1.86995 | -0.835441 | -0.376679 | 0.025468 | 0.479698 | 1.07038 | 2.72373 |
| bonus_part | alpha_5 | 4716 | 0.0568864 | 0.518999 | -1.88815 | -0.745099 | -0.306255 | 0.0395121 | 0.405458 | 0.917431 | 2.28369 |
| bonus_part | alpha_norm | 4716 | 1.0839 | 0.512423 | 0.105203 | 0.347565 | 0.685369 | 1.0406 | 1.42075 | 1.97127 | 3.11836 |
