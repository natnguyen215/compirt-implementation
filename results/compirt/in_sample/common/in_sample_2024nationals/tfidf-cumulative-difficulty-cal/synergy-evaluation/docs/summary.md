# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/tfidf-cumulative-difficulty-cal/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/tfidf-cumulative-difficulty-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 60105.3 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 10988.5 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.411979 |
| mean_synergy_contribution | 1.14226 |
| median_synergy_contribution | 1.25459 |
| negative_synergy_fraction | 0.0875018 |
| positive_synergy_fraction | 0.911643 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.930865 |
| log_loss | 0.341496 |
| ece | 0.0393355 |
| part_accuracy | 0.853784 |
| part_accuracy_macro_team | 0.857953 |
| part_accuracy_macro_game | 0.854601 |
| part_accuracy_macro_bonus | 0.851466 |
| exact_acc | 0.612797 |
| ppb_mae | 0.520556 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.636055 |
| log_loss | 0.563151 |
| ece | 0.00910649 |
| accuracy | 0.728212 |
| buzz_position_mae | 0.121719 |
| buzz_position_median_absolute_error | 0.107526 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 3.15701 | 0.489668 | 1.66746 | 2.35016 | 2.82383 | 3.16301 | 3.54309 | 3.93323 | 4.25808 |
| player | theta_1 | 189 | -1.00748 | 0.754812 | -2.73522 | -2.20785 | -1.6108 | -0.970635 | -0.447864 | 0.119341 | 0.903784 |
| player | theta_2 | 189 | -1.21874 | 0.726962 | -2.91742 | -2.4378 | -1.72219 | -1.21535 | -0.681546 | -0.037517 | 0.442967 |
| player | theta_3 | 189 | -0.928263 | 0.670177 | -2.71918 | -2.1227 | -1.35096 | -0.87903 | -0.483384 | 0.0957534 | 0.76452 |
| player | theta_4 | 189 | 1.09859 | 0.667957 | -0.892795 | -0.0222534 | 0.593867 | 1.05137 | 1.61717 | 2.0793 | 2.83423 |
| player | theta_5 | 189 | -0.951385 | 0.630223 | -2.65384 | -1.87884 | -1.39707 | -0.989672 | -0.523553 | 0.0900976 | 0.576392 |
| player | theta_norm | 189 | 2.72596 | 0.650767 | 0.869961 | 1.7451 | 2.2658 | 2.76838 | 3.21733 | 3.73482 | 4.31616 |
| tossup | beta | 360 | 3.03452 | 0.53311 | 1.61569 | 2.2228 | 2.65473 | 2.99779 | 3.40154 | 3.93421 | 4.72257 |
| tossup | gamma | 360 | 59.6558 | 148.028 | 3.26403 | 8.01198 | 12.0153 | 18.3776 | 42.7965 | 199.96 | 1722.65 |
| tossup | mu | 360 | 0.754171 | 0.118504 | 0.400741 | 0.548829 | 0.669297 | 0.764109 | 0.834935 | 0.945414 | 0.991333 |
| tossup | alpha_1 | 360 | 0.704268 | 0.769858 | -0.994133 | -0.496513 | 0.126197 | 0.631729 | 1.348 | 1.93751 | 2.38127 |
| tossup | alpha_2 | 360 | 0.704972 | 0.728874 | -1.25524 | -0.337902 | 0.145433 | 0.620005 | 1.27969 | 1.95934 | 2.83102 |
| tossup | alpha_3 | 360 | 0.593714 | 0.622517 | -0.837531 | -0.296848 | 0.125778 | 0.548022 | 0.981771 | 1.6758 | 2.59439 |
| tossup | alpha_4 | 360 | -0.621053 | 0.695836 | -2.73082 | -2.00409 | -0.988841 | -0.479106 | -0.137795 | 0.278945 | 0.772291 |
| tossup | alpha_5 | 360 | 0.586264 | 0.689104 | -1.02784 | -0.334113 | 0.1001 | 0.4572 | 1.02129 | 1.83952 | 2.74671 |
| tossup | alpha_norm | 360 | 2.07988 | 0.46175 | 0.655016 | 1.30491 | 1.77266 | 2.06641 | 2.41215 | 2.81587 | 3.71924 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 1071 | 0.00678286 | 0.892182 | -1.58653 | -1.20369 | -0.843377 | -0.0383497 | 0.858596 | 1.37336 | 1.5464 |
| bonus_part | alpha_1 | 1071 | 0.801772 | 0.231396 | 0.360322 | 0.490619 | 0.603519 | 0.784535 | 0.95932 | 1.2044 | 1.87838 |
| bonus_part | alpha_2 | 1071 | 0.844285 | 0.344581 | 0.299378 | 0.420244 | 0.52608 | 0.790136 | 1.13773 | 1.4279 | 1.9648 |
| bonus_part | alpha_3 | 1071 | 0.814094 | 0.262744 | 0.318944 | 0.469913 | 0.577109 | 0.779688 | 1.01544 | 1.246 | 1.88038 |
| bonus_part | alpha_4 | 1071 | 1.11373 | 0.828764 | 0.37077 | 0.405767 | 0.477367 | 0.721624 | 1.56224 | 3.04643 | 3.47017 |
| bonus_part | alpha_5 | 1071 | 0.819199 | 0.294955 | 0.369034 | 0.456574 | 0.559101 | 0.75411 | 1.04578 | 1.32503 | 1.97429 |
| bonus_part | alpha_norm | 1071 | 2.17567 | 0.459095 | 1.23766 | 1.56462 | 1.82419 | 2.13169 | 2.42499 | 3.21556 | 3.61663 |
| synergy_player | psi_1 | 189 | 0.0281163 | 0.236762 | -0.564384 | -0.454761 | -0.0394253 | 0.00165501 | 0.0438896 | 0.56471 | 0.580608 |
| synergy_player | psi_2 | 189 | -0.0171669 | 0.248656 | -0.593359 | -0.498597 | -0.0505202 | -0.00129865 | 0.0451345 | 0.439991 | 0.518721 |
| synergy_player | psi_3 | 189 | 0.00760853 | 0.304538 | -1.21679 | -0.529923 | -0.0592163 | -0.00509233 | 0.0643178 | 0.512975 | 0.551016 |
| synergy_player | psi_norm | 189 | 0.41761 | 0.190927 | 0.0196371 | 0.0499299 | 0.319562 | 0.464452 | 0.525956 | 0.686839 | 1.21786 |
| synergy | synergy_score | 274 | 0.190478 | 0.156482 | -0.606565 | -0.000902922 | 0.0978354 | 0.211567 | 0.268929 | 0.445655 | 0.565683 |
| synergy | synergy_contribution | 7017 | 1.14226 | 0.835748 | -1.03423 | -0.129945 | 0.555886 | 1.25459 | 1.58914 | 2.1153 | 3.37736 |
