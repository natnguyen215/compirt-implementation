# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/learned-topic-all2024-cal/synergy-evaluation`
Result root: `results/compirt/in_sample/learned-topic-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 688739 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 221414 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.515555 |
| mean_synergy_contribution | 0.0813953 |
| median_synergy_contribution | 0.0166168 |
| negative_synergy_fraction | 0.399038 |
| positive_synergy_fraction | 0.56956 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.921769 |
| log_loss | 0.355762 |
| ece | 0.0133989 |
| part_accuracy | 0.840965 |
| exact_score_accuracy | 0.582799 |
| rounded_score_accuracy | 0.595635 |
| per_bonus_points_mae | 4.80533 |
| ppb_mae | 1.71382 |
| accuracy | 0.840965 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.630615 |
| log_loss | 0.522923 |
| ece | 0.0103939 |
| accuracy | 0.768001 |
| buzz_position_mae | 0.144669 |
| buzz_position_median_absolute_error | 0.128838 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.915078 | 0.921769 | 0.00669171 | synergy |
| log_loss | 0.368554 | 0.355762 | -0.0127922 | synergy |
| ece | 0.00766231 | 0.0133989 | 0.00573655 | no-synergy |
| accuracy | 0.831719 | 0.840965 | 0.00924615 | synergy |
| part_accuracy | 0.831719 | 0.840965 | 0.00924615 | synergy |
| exact_score_accuracy | 0.562074 | 0.582799 | 0.0207252 | synergy |
| rounded_score_accuracy | 0.57464 | 0.595635 | 0.0209949 | synergy |
| per_bonus_points_mae | 5.04876 | 4.80533 | -0.243424 | synergy |
| ppb_mae | 2.2458 | 1.71382 | -0.531981 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 3.50865 | 0.66628 | 1.02844 | 2.42367 | 3.07483 | 3.48508 | 3.91066 | 4.67401 | 5.45065 |
| player | theta_1 | 1455 | -0.967557 | 0.799399 | -3.47991 | -2.14211 | -1.50868 | -1.05216 | -0.495156 | 0.543449 | 1.65894 |
| player | theta_2 | 1455 | -0.668844 | 0.679438 | -2.445 | -1.68157 | -1.112 | -0.72615 | -0.294751 | 0.533359 | 1.87417 |
| player | theta_3 | 1455 | -0.583356 | 0.541546 | -2.35571 | -1.40122 | -0.936031 | -0.624942 | -0.277004 | 0.380803 | 1.43563 |
| player | theta_4 | 1455 | -0.777095 | 0.835966 | -3.56743 | -1.99917 | -1.35397 | -0.881251 | -0.276136 | 0.788743 | 2.4998 |
| player | theta_5 | 1455 | -0.945075 | 0.781427 | -2.6759 | -2.03166 | -1.46465 | -1.06982 | -0.561192 | 0.63687 | 2.24988 |
| player | theta_norm | 1455 | 2.36737 | 0.564076 | 0.720201 | 1.48962 | 2.0115 | 2.33277 | 2.68556 | 3.39015 | 4.93537 |
| tossup | beta_1 | 1260 | 1.34658 | 1.74269 | -0.352041 | 0.0431659 | 0.123826 | 0.267798 | 3.1437 | 4.61893 | 5.49974 |
| tossup | beta_2 | 1260 | 0.921677 | 1.56153 | -0.330535 | 0.0450391 | 0.115168 | 0.182617 | 0.429827 | 4.67296 | 5.73548 |
| tossup | beta_3 | 1260 | 0.794582 | 1.44057 | -0.305058 | 0.0464134 | 0.118403 | 0.190291 | 0.378875 | 4.62129 | 5.65075 |
| tossup | beta_4 | 1260 | 1.05822 | 1.66536 | -0.188613 | 0.0434905 | 0.10133 | 0.179065 | 0.641805 | 4.63811 | 5.41519 |
| tossup | beta_5 | 1260 | 1.319 | 1.83393 | -0.64773 | 0.0472623 | 0.124475 | 0.220474 | 3.02799 | 4.87299 | 5.56796 |
| tossup | gamma_1 | 1260 | 13.8064 | 51.4811 | 3.47426 | 4.66313 | 4.97321 | 5.2735 | 8.50883 | 36.0682 | 1237.94 |
| tossup | gamma_2 | 1260 | 15.973 | 89.3086 | 4.28001 | 4.60594 | 4.92351 | 5.15878 | 5.66241 | 22.3123 | 1735.43 |
| tossup | gamma_3 | 1260 | 11.4641 | 57.7021 | 3.94593 | 4.62249 | 4.90774 | 5.13976 | 5.46365 | 16.8272 | 1605.42 |
| tossup | gamma_4 | 1260 | 10.7316 | 33.7064 | 4.14899 | 4.6405 | 4.93424 | 5.16696 | 5.71505 | 24.8849 | 618.384 |
| tossup | gamma_5 | 1260 | 16.1 | 86.0275 | 4.17477 | 4.6138 | 4.94334 | 5.21365 | 6.89216 | 25.0355 | 1834.48 |
| tossup | mu_1 | 1260 | 0.547499 | 0.103718 | 0.284036 | 0.472924 | 0.494395 | 0.506096 | 0.539786 | 0.793255 | 0.964494 |
| tossup | mu_2 | 1260 | 0.538851 | 0.0988982 | 0.254205 | 0.478333 | 0.493167 | 0.504102 | 0.518781 | 0.78202 | 0.98289 |
| tossup | mu_3 | 1260 | 0.530127 | 0.0872723 | 0.205915 | 0.479294 | 0.493348 | 0.502348 | 0.515654 | 0.771064 | 0.95998 |
| tossup | mu_4 | 1260 | 0.540356 | 0.101053 | 0.299401 | 0.478016 | 0.493259 | 0.503043 | 0.519731 | 0.798153 | 0.977513 |
| tossup | mu_5 | 1260 | 0.554355 | 0.108932 | 0.309946 | 0.480215 | 0.495136 | 0.507219 | 0.543555 | 0.819414 | 0.982819 |
| tossup | topic_weight_1 | 1260 | 0.245346 | 0.336223 | 0.0060447 | 0.0099394 | 0.0148993 | 0.0338077 | 0.525821 | 0.893416 | 0.941948 |
| tossup | topic_weight_2 | 1260 | 0.153205 | 0.285115 | 0.00725103 | 0.0111861 | 0.0150772 | 0.0215823 | 0.0619941 | 0.900186 | 0.953444 |
| tossup | topic_weight_3 | 1260 | 0.130925 | 0.251374 | 0.00777875 | 0.0114635 | 0.0163292 | 0.0241275 | 0.0597311 | 0.8402 | 0.942194 |
| tossup | topic_weight_4 | 1260 | 0.217335 | 0.353089 | 0.007417 | 0.0113146 | 0.0168046 | 0.0264182 | 0.138739 | 0.947373 | 0.970747 |
| tossup | topic_weight_5 | 1260 | 0.253189 | 0.354139 | 0.00687808 | 0.0119774 | 0.0210446 | 0.038964 | 0.509054 | 0.93285 | 0.962065 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| synergy_player | psi_1 | 1455 | 0.00438508 | 0.203682 | -0.907492 | -0.340645 | -0.045 | 0.000760532 | 0.0433648 | 0.382326 | 1.26055 |
| synergy_player | psi_2 | 1455 | -0.00919534 | 0.188489 | -1.04599 | -0.320378 | -0.041518 | -0.00502779 | 0.0350565 | 0.277689 | 0.833328 |
| synergy_player | psi_3 | 1455 | -0.00301726 | 0.190027 | -0.961456 | -0.313911 | -0.0465747 | -0.00256374 | 0.0416422 | 0.314394 | 1.18712 |
| synergy_player | psi_norm | 1455 | 0.266948 | 0.204762 | 0.0082896 | 0.0401608 | 0.102964 | 0.226479 | 0.37041 | 0.69035 | 1.26066 |
| synergy | synergy_score | 2521 | 0.00587862 | 0.125796 | -0.864341 | -0.219161 | -0.0184799 | 0.00714714 | 0.0567119 | 0.171586 | 0.984437 |
| synergy | synergy_contribution | 44487 | 0.0813953 | 0.310985 | -0.973883 | -0.435459 | -0.100963 | 0.0166168 | 0.310827 | 0.600081 | 1.03392 |
