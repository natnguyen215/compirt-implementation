# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/plda-all2024/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/plda-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 485057 |
| pyramidal | calibrate_correctness | False |
| pyramidal | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 89153.7 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |
| synergy | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.306986 |
| mean_synergy_contribution | -0.777649 |
| median_synergy_contribution | -0.755686 |
| negative_synergy_fraction | 0.835214 |
| positive_synergy_fraction | 0.140404 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.912869 |
| log_loss | 0.390657 |
| ece | 0.0609813 |
| part_accuracy | 0.833841 |
| part_accuracy_macro_team | 0.835974 |
| part_accuracy_macro_game | 0.834301 |
| part_accuracy_macro_bonus | 0.828449 |
| exact_acc | 0.566348 |
| ppb_mae | 0.603698 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.6445 |
| log_loss | 0.629071 |
| ece | 0.191069 |
| accuracy | 0.664127 |
| buzz_position_mae | 0.162279 |
| buzz_position_median_absolute_error | 0.144586 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.904623 | 0.912869 | 0.00824554 | synergy |
| log_loss | 0.409574 | 0.390657 | -0.0189167 | synergy |
| ece | 0.0707294 | 0.0609813 | -0.00974809 | synergy |
| part_accuracy | 0.816125 | 0.833841 | 0.0177159 | synergy |
| part_accuracy_macro_team | 0.818909 | 0.835974 | 0.0170653 | synergy |
| part_accuracy_macro_game | 0.816401 | 0.834301 | 0.0179007 | synergy |
| part_accuracy_macro_bonus | 0.793945 | 0.828449 | 0.0345035 | synergy |
| exact_acc | 0.527624 | 0.566348 | 0.0387237 | synergy |
| ppb_mae | 1.9993 | 0.603698 | -1.39561 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.29696 | 0.431098 | 3.16434 | 4.62888 | 5.02646 | 5.29229 | 5.58307 | 6.00139 | 6.88571 |
| player | theta_1 | 1755 | 0.237583 | 0.89312 | -1.88508 | -1.05257 | -0.435927 | 0.150748 | 0.807547 | 1.8164 | 3.39121 |
| player | theta_2 | 1755 | 0.334071 | 0.950811 | -2.00322 | -1.09206 | -0.354546 | 0.287608 | 0.948924 | 2.01083 | 3.78399 |
| player | theta_3 | 1755 | 0.235182 | 1.13753 | -2.19675 | -1.30823 | -0.669831 | 0.119034 | 0.967849 | 2.34667 | 4.2229 |
| player | theta_4 | 1755 | 0.209389 | 1.16849 | -2.24948 | -1.50288 | -0.63569 | 0.111862 | 0.932075 | 2.33368 | 4.69974 |
| player | theta_5 | 1755 | 0.296224 | 0.939571 | -1.9156 | -0.968576 | -0.453874 | 0.172738 | 0.926504 | 2.01504 | 3.77359 |
| player | theta_norm | 1755 | 2.17795 | 0.923494 | 0.253604 | 0.968926 | 1.51956 | 1.98997 | 2.67033 | 3.98569 | 5.97504 |
| tossup | beta_1 | 1350 | 1.12316 | 1.39333 | -3.39329 | -0.0606151 | 0.0627971 | 0.478262 | 1.97385 | 4.05764 | 5.27254 |
| tossup | beta_2 | 1350 | 1.26399 | 1.51674 | -3.59432 | -0.060313 | 0.0856505 | 0.507596 | 2.43443 | 4.16048 | 5.3349 |
| tossup | beta_3 | 1350 | 1.05914 | 1.5132 | -1.64851 | -0.059373 | 0.0266148 | 0.173117 | 1.8862 | 4.07743 | 5.16244 |
| tossup | beta_4 | 1350 | 1.34338 | 1.63844 | -4.01233 | -0.0678963 | 0.0515607 | 0.460454 | 2.72619 | 4.41517 | 6.10858 |
| tossup | beta_5 | 1350 | 0.812937 | 1.25154 | -2.71095 | -0.0687605 | 0.0288212 | 0.179449 | 1.08585 | 3.74418 | 4.98203 |
| tossup | gamma_1 | 1350 | 26.174 | 111.829 | 2.20084 | 4.62124 | 5.01339 | 5.54437 | 10.5645 | 68.0252 | 1773.96 |
| tossup | gamma_2 | 1350 | 29.1039 | 110.126 | 1.21589 | 4.62734 | 5.03686 | 5.64388 | 12.6468 | 97.0465 | 2217.59 |
| tossup | gamma_3 | 1350 | 22.0838 | 105.464 | 1.75128 | 4.57694 | 4.90919 | 5.28257 | 8.63541 | 49.6891 | 1840.15 |
| tossup | gamma_4 | 1350 | 24.4865 | 91.2782 | 2.84987 | 4.58713 | 5.01654 | 5.58936 | 12.4049 | 77.4453 | 1625.2 |
| tossup | gamma_5 | 1350 | 18.2363 | 71.4215 | 2.32095 | 4.54121 | 4.92694 | 5.27181 | 7.3275 | 47.0354 | 1129.96 |
| tossup | mu_1 | 1350 | 0.528761 | 0.0995608 | 0.109725 | 0.415603 | 0.488265 | 0.503928 | 0.53722 | 0.749051 | 0.953418 |
| tossup | mu_2 | 1350 | 0.531375 | 0.0986717 | 0.135834 | 0.420116 | 0.488865 | 0.504861 | 0.549168 | 0.739067 | 0.966387 |
| tossup | mu_3 | 1350 | 0.526033 | 0.086587 | 0.199231 | 0.43596 | 0.490691 | 0.504817 | 0.527984 | 0.725976 | 0.980752 |
| tossup | mu_4 | 1350 | 0.542679 | 0.111093 | 0.133047 | 0.422022 | 0.490356 | 0.507139 | 0.568205 | 0.788088 | 0.971212 |
| tossup | mu_5 | 1350 | 0.516338 | 0.079738 | 0.131241 | 0.426186 | 0.489063 | 0.502888 | 0.52054 | 0.680305 | 0.923434 |
| tossup | topic_weight_1 | 1350 | 0.193366 | 0.214386 | 0.00403773 | 0.00600104 | 0.0238805 | 0.118032 | 0.287111 | 0.673767 | 0.968847 |
| tossup | topic_weight_2 | 1350 | 0.213074 | 0.225166 | 0.00428213 | 0.00675765 | 0.0260513 | 0.126268 | 0.33058 | 0.686117 | 0.947785 |
| tossup | topic_weight_3 | 1350 | 0.217725 | 0.311051 | 0.00283386 | 0.00374078 | 0.00673389 | 0.0488541 | 0.285499 | 0.90438 | 0.981274 |
| tossup | topic_weight_4 | 1350 | 0.23566 | 0.26665 | 0.00368735 | 0.00544153 | 0.0167964 | 0.117151 | 0.392932 | 0.790912 | 0.977032 |
| tossup | topic_weight_5 | 1350 | 0.140175 | 0.187266 | 0.00311917 | 0.00436076 | 0.00834852 | 0.0536184 | 0.195212 | 0.564457 | 0.966084 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 4716 | 0.0960527 | 0.872318 | -3.3007 | -1.39637 | -0.110718 | 0.0198027 | 0.283929 | 1.72465 | 4.96606 |
| bonus_part | beta_2 | 4716 | 0.0954392 | 0.949452 | -3.34627 | -1.63395 | -0.172161 | 0.026272 | 0.363171 | 1.87399 | 4.65045 |
| bonus_part | beta_3 | 4716 | 0.143388 | 0.95739 | -3.54305 | -1.36602 | -0.0749989 | 0.015033 | 0.19158 | 2.22202 | 4.78874 |
| bonus_part | beta_4 | 4716 | 0.115247 | 0.922679 | -3.52408 | -1.46857 | -0.0865833 | 0.0205228 | 0.216645 | 1.93647 | 5.17157 |
| bonus_part | beta_5 | 4716 | 0.0620868 | 0.818046 | -3.29164 | -1.36574 | -0.0952576 | 0.0140456 | 0.192438 | 1.59471 | 4.67317 |
| synergy_player | psi_1 | 1755 | -0.0035085 | 0.377115 | -1.80893 | -0.660316 | -0.0690712 | -0.000663885 | 0.0635367 | 0.644981 | 1.68018 |
| synergy_player | psi_2 | 1755 | -0.00845477 | 0.418967 | -1.71515 | -0.775316 | -0.0834921 | -0.00219134 | 0.0682226 | 0.801385 | 1.63659 |
| synergy_player | psi_3 | 1755 | -0.00268621 | 0.356902 | -1.45431 | -0.645187 | -0.0682807 | -0.00186365 | 0.0599687 | 0.588457 | 1.58772 |
| synergy_player | psi_norm | 1755 | 0.531421 | 0.403298 | 0.0112261 | 0.0542848 | 0.198477 | 0.433941 | 0.799687 | 1.31616 | 1.95959 |
| synergy | synergy_score | 3042 | -0.13352 | 0.408402 | -2.61182 | -0.916893 | -0.299355 | -0.00273272 | 0.0753421 | 0.355356 | 1.81356 |
| synergy | synergy_contribution | 60454 | -0.777649 | 0.69617 | -2.61182 | -1.88192 | -1.34383 | -0.755686 | -0.145217 | 0.20367 | 1.26028 |
