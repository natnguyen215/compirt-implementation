# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/tfidf-cumulative-difficulty-all2024-cal/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/tfidf-cumulative-difficulty-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 448833 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 86522.2 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.685632 |
| mean_synergy_contribution | 0.204134 |
| median_synergy_contribution | 0.099693 |
| negative_synergy_fraction | 0.385252 |
| positive_synergy_fraction | 0.590366 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.927395 |
| log_loss | 0.345773 |
| ece | 0.0244892 |
| part_accuracy | 0.847168 |
| exact_score_accuracy | 0.597181 |
| rounded_score_accuracy | 0.596652 |
| per_bonus_points_mae | 4.81641 |
| ppb_mae | 1.68331 |
| accuracy | 0.847168 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.600306 |
| log_loss | 0.529003 |
| ece | 0.0148788 |
| accuracy | 0.770414 |
| buzz_position_mae | 0.135113 |
| buzz_position_median_absolute_error | 0.114952 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.912494 | 0.927395 | 0.0149013 | synergy |
| log_loss | 0.376319 | 0.345773 | -0.0305459 | synergy |
| ece | 0.0210548 | 0.0244892 | 0.00343436 | no-synergy |
| accuracy | 0.82847 | 0.847168 | 0.0186974 | synergy |
| part_accuracy | 0.82847 | 0.847168 | 0.0186974 | synergy |
| exact_score_accuracy | 0.554422 | 0.597181 | 0.0427598 | synergy |
| per_bonus_points_mae | 5.32994 | 4.81641 | -0.513523 | synergy |
| ppb_mae | 2.63971 | 1.68331 | -0.956404 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 1.40842 | 0.719111 | -0.464005 | 0.362476 | 0.920134 | 1.34316 | 1.82108 | 2.72562 | 4.72883 |
| player | theta_1 | 1755 | -0.689015 | 0.603466 | -2.35558 | -1.63947 | -1.08881 | -0.711568 | -0.315024 | 0.362038 | 1.3494 |
| player | theta_2 | 1755 | -0.296732 | 0.882213 | -2.46009 | -1.56377 | -0.955444 | -0.40132 | 0.261866 | 1.35874 | 3.5877 |
| player | theta_3 | 1755 | -1.24605 | 0.464227 | -2.85355 | -1.98692 | -1.56602 | -1.25993 | -0.93787 | -0.48162 | 0.552319 |
| player | theta_4 | 1755 | 1.02865 | 0.662258 | -1.19012 | -0.180648 | 0.58704 | 1.12352 | 1.52533 | 1.99413 | 2.69913 |
| player | theta_5 | 1755 | -0.309097 | 0.649944 | -2.78215 | -1.3633 | -0.752511 | -0.324547 | 0.124538 | 0.798606 | 1.64288 |
| player | theta_norm | 1755 | 2.29887 | 0.449569 | 0.91929 | 1.5822 | 1.97948 | 2.30263 | 2.61795 | 3.04765 | 3.9207 |
| tossup | beta | 1350 | 3.25709 | 0.855369 | 0.668735 | 1.91157 | 2.77601 | 3.23085 | 3.69243 | 4.60899 | 7.22395 |
| tossup | gamma | 1350 | 100.766 | 274.851 | 1.87787 | 5.22829 | 8.6831 | 14.1297 | 39.5558 | 667.092 | 2427.09 |
| tossup | mu | 1350 | 0.702037 | 0.158565 | 0.136107 | 0.437074 | 0.592491 | 0.706181 | 0.819365 | 0.957061 | 0.993959 |
| tossup | alpha_1 | 1350 | 0.871873 | 0.691504 | -1.0501 | -0.227847 | 0.374699 | 0.850463 | 1.35468 | 2.07174 | 2.77619 |
| tossup | alpha_2 | 1350 | 0.179478 | 0.596562 | -1.91091 | -0.859526 | -0.171915 | 0.249006 | 0.559614 | 1.07797 | 2.19736 |
| tossup | alpha_3 | 1350 | 1.77001 | 0.718137 | -1.58847 | 0.520919 | 1.37406 | 1.84688 | 2.26878 | 2.77722 | 3.63971 |
| tossup | alpha_4 | 1350 | -1.39682 | 0.683236 | -3.42935 | -2.57191 | -1.85216 | -1.35925 | -0.954715 | -0.28231 | 0.792674 |
| tossup | alpha_5 | 1350 | 0.269822 | 0.707623 | -1.82072 | -1.06703 | -0.146958 | 0.382696 | 0.742771 | 1.31739 | 2.06199 |
| tossup | alpha_norm | 1350 | 2.82825 | 0.515779 | 0.903145 | 1.93678 | 2.50703 | 2.85299 | 3.18252 | 3.62752 | 4.25197 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | -0.0033662 | 1.14693 | -2.43267 | -1.76698 | -0.990607 | 0.00611856 | 0.956647 | 1.80114 | 2.56118 |
| bonus_part | alpha_1 | 4716 | 0.85299 | 0.373947 | 0.23286 | 0.455893 | 0.580325 | 0.757185 | 1.04871 | 1.50392 | 3.68702 |
| bonus_part | alpha_2 | 4716 | 0.873748 | 0.465297 | 0.225884 | 0.374603 | 0.558243 | 0.741631 | 1.04733 | 1.84977 | 3.53872 |
| bonus_part | alpha_3 | 4716 | 0.979205 | 0.608184 | 0.2054 | 0.36108 | 0.479407 | 0.76064 | 1.35266 | 2.15541 | 3.84552 |
| bonus_part | alpha_4 | 4716 | 0.932917 | 0.663468 | 0.171673 | 0.350704 | 0.501569 | 0.693586 | 1.06037 | 2.38622 | 3.97881 |
| bonus_part | alpha_5 | 4716 | 0.789601 | 0.293886 | 0.186138 | 0.455426 | 0.625913 | 0.740259 | 0.86615 | 1.33449 | 3.88064 |
| bonus_part | alpha_norm | 4716 | 2.22332 | 0.503071 | 1.08855 | 1.56183 | 1.83665 | 2.14622 | 2.52 | 3.16944 | 4.43037 |
| synergy_player | psi_1 | 1755 | 0.0123644 | 0.349942 | -1.90429 | -0.548993 | -0.0602208 | 0.00274741 | 0.0728027 | 0.590282 | 1.87934 |
| synergy_player | psi_2 | 1755 | -0.00427321 | 0.311444 | -1.40687 | -0.523675 | -0.0720082 | -0.00301618 | 0.0671674 | 0.529097 | 1.71107 |
| synergy_player | psi_3 | 1755 | -0.0115876 | 0.366202 | -1.81001 | -0.620689 | -0.0748127 | -0.0027651 | 0.0627246 | 0.582709 | 1.81717 |
| synergy_player | psi_norm | 1755 | 0.480516 | 0.350483 | 0.00800487 | 0.0670766 | 0.23117 | 0.410496 | 0.624552 | 1.2213 | 2.0672 |
| synergy | synergy_score | 3042 | 0.0118321 | 0.379975 | -3.37721 | -0.730671 | -0.0340886 | 0.0583364 | 0.186772 | 0.457456 | 1.50074 |
| synergy | synergy_contribution | 60454 | 0.204134 | 1.05576 | -4.0395 | -1.55824 | -0.416696 | 0.099693 | 0.932842 | 1.86107 | 3.76145 |
