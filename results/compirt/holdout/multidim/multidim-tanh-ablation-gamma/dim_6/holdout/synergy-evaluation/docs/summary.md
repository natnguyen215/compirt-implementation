# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_6/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_6`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 469271 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 6 |
| synergy | steps | 2000 |
| synergy | final_loss | 82716 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.26276 |
| mean_synergy_contribution | -0.0986057 |
| median_synergy_contribution | -0.000568713 |
| negative_synergy_fraction | 0.504996 |
| positive_synergy_fraction | 0.470622 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.932703 |
| log_loss | 0.340012 |
| ece | 0.0372513 |
| part_accuracy | 0.853558 |
| part_accuracy_macro_team | 0.854641 |
| part_accuracy_macro_game | 0.853792 |
| part_accuracy_macro_bonus | 0.859457 |
| exact_acc | 0.61139 |
| ppb_mae | 0.557203 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.680105 |
| log_loss | 0.590506 |
| ece | 0.131703 |
| accuracy | 0.713175 |
| buzz_position_mae | 0.131148 |
| buzz_position_median_absolute_error | 0.108602 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.95034 | 0.934034 | 1.3241 | 3.0722 | 4.46949 | 5.08861 | 5.58479 | 6.22918 | 7.19177 |
| player | theta_1 | 1755 | -0.482286 | 0.636794 | -2.97759 | -1.53104 | -0.920311 | -0.43823 | -0.0407767 | 0.526248 | 1.50315 |
| player | theta_2 | 1755 | -0.540888 | 0.634953 | -2.8924 | -1.65603 | -0.935435 | -0.504524 | -0.128031 | 0.503505 | 1.38007 |
| player | theta_3 | 1755 | -0.520339 | 0.681531 | -2.78041 | -1.75182 | -0.96216 | -0.465931 | -0.00551487 | 0.504534 | 1.04119 |
| player | theta_4 | 1755 | -0.406911 | 0.633138 | -3.39403 | -1.49253 | -0.817256 | -0.350759 | 0.0188821 | 0.5837 | 1.38587 |
| player | theta_5 | 1755 | -0.483905 | 0.656055 | -2.71004 | -1.5922 | -0.921199 | -0.453846 | -0.031988 | 0.569894 | 1.46854 |
| player | theta_6 | 1755 | -0.478885 | 0.598716 | -2.92971 | -1.50422 | -0.871146 | -0.424956 | -0.0838138 | 0.475259 | 1.16385 |
| player | theta_norm | 1755 | 1.82893 | 0.736054 | 0.156463 | 0.808688 | 1.27037 | 1.71053 | 2.27765 | 3.22723 | 4.04053 |
| tossup | beta_1 | 1350 | 0.246313 | 0.489667 | -1.87569 | -0.0982449 | 0.00718751 | 0.0848167 | 0.196319 | 1.46526 | 2.74269 |
| tossup | beta_2 | 1350 | 0.426213 | 0.619101 | -2.26379 | -0.091874 | 0.0337288 | 0.123761 | 0.812504 | 1.68558 | 2.97345 |
| tossup | beta_3 | 1350 | 0.498208 | 0.666788 | -2.72424 | -0.0783274 | 0.0390427 | 0.144914 | 1.06022 | 1.77693 | 3.36596 |
| tossup | beta_4 | 1350 | 0.225762 | 0.481445 | -1.54989 | -0.119827 | 0.00183048 | 0.0815048 | 0.17934 | 1.47685 | 3.54427 |
| tossup | beta_5 | 1350 | 0.304618 | 0.520347 | -0.901257 | -0.0960668 | 0.0199356 | 0.0957374 | 0.243667 | 1.47439 | 2.57553 |
| tossup | beta_6 | 1350 | 0.292266 | 0.535017 | -3.59571 | -0.0913618 | 0.0205935 | 0.0909844 | 0.226173 | 1.55406 | 2.60154 |
| tossup | gamma_1 | 1350 | 6.10275 | 31.5478 | 0.683987 | 1.37307 | 2.24613 | 2.84062 | 3.41742 | 5.41583 | 621.932 |
| tossup | gamma_2 | 1350 | 4.41783 | 16.5908 | 0.68287 | 1.28007 | 2.08097 | 2.6543 | 3.32892 | 6.06376 | 361.41 |
| tossup | gamma_3 | 1350 | 7.74847 | 46.6908 | 0.80073 | 1.39971 | 2.1976 | 2.77894 | 3.52224 | 12.7846 | 953.712 |
| tossup | gamma_4 | 1350 | 6.44647 | 39.4245 | 0.635468 | 1.35002 | 2.22679 | 2.78379 | 3.37951 | 5.13248 | 929.426 |
| tossup | gamma_5 | 1350 | 5.20138 | 29.7973 | 0.687493 | 1.4055 | 2.20125 | 2.77842 | 3.34977 | 5.27671 | 807.504 |
| tossup | gamma_6 | 1350 | 6.88084 | 40.5327 | 0.583993 | 1.22799 | 2.11904 | 2.67157 | 3.28854 | 5.65042 | 845.124 |
| tossup | mu_1 | 1350 | 0.538391 | 0.0925013 | 0.0894707 | 0.407928 | 0.506395 | 0.535589 | 0.568091 | 0.666525 | 0.991798 |
| tossup | mu_2 | 1350 | 0.536016 | 0.112428 | 0.0910036 | 0.316092 | 0.49999 | 0.535893 | 0.57573 | 0.730155 | 0.983472 |
| tossup | mu_3 | 1350 | 0.528182 | 0.120054 | 0.0827831 | 0.277161 | 0.494191 | 0.535788 | 0.576185 | 0.708694 | 0.992936 |
| tossup | mu_4 | 1350 | 0.541725 | 0.0891206 | 0.0876926 | 0.440702 | 0.508645 | 0.536946 | 0.569336 | 0.663458 | 0.994009 |
| tossup | mu_5 | 1350 | 0.545308 | 0.0920602 | 0.0860372 | 0.436022 | 0.511113 | 0.540941 | 0.576152 | 0.697905 | 0.962301 |
| tossup | mu_6 | 1350 | 0.544846 | 0.100719 | 0.0861536 | 0.404192 | 0.507808 | 0.541236 | 0.573977 | 0.708091 | 0.991005 |
| tossup | r_1 | 1350 | 0.768927 | 0.543381 | 0.0499539 | 0.182793 | 0.377852 | 0.628412 | 0.971783 | 1.96357 | 3.37379 |
| tossup | r_2 | 1350 | 1.12848 | 0.895057 | 0.0710847 | 0.219682 | 0.467802 | 0.8119 | 1.59091 | 2.95107 | 4.45695 |
| tossup | r_3 | 1350 | 1.16639 | 0.869283 | 0.0477756 | 0.208735 | 0.500614 | 0.880668 | 1.70499 | 2.91088 | 4.4247 |
| tossup | r_4 | 1350 | 0.763443 | 0.532399 | 0.059935 | 0.192661 | 0.387756 | 0.638004 | 0.977798 | 1.80771 | 3.85081 |
| tossup | r_5 | 1350 | 0.925577 | 0.747182 | 0.044791 | 0.20699 | 0.41113 | 0.6865 | 1.13952 | 2.6491 | 4.12002 |
| tossup | r_6 | 1350 | 0.951653 | 0.756314 | 0.0793224 | 0.228615 | 0.444622 | 0.716606 | 1.1967 | 2.50487 | 4.65254 |
| tossup | r_norm | 1350 | 2.88991 | 0.694627 | 1.03401 | 1.81188 | 2.41613 | 2.8592 | 3.33592 | 4.10355 | 5.23618 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.00545126 | 1.63462 | -3.47823 | -2.59767 | -1.43902 | 0.0899254 | 1.326 | 2.58863 | 3.44155 |
| bonus_part | alpha_1 | 4716 | 0.782035 | 0.276967 | 0.245977 | 0.458159 | 0.607273 | 0.738305 | 0.878607 | 1.27511 | 3.79653 |
| bonus_part | alpha_2 | 4716 | 0.83889 | 0.447773 | 0.213337 | 0.440793 | 0.598752 | 0.742032 | 0.920651 | 1.53537 | 5.1784 |
| bonus_part | alpha_3 | 4716 | 0.82923 | 0.390056 | 0.211023 | 0.440707 | 0.596249 | 0.749827 | 0.956015 | 1.4284 | 4.9104 |
| bonus_part | alpha_4 | 4716 | 0.801638 | 0.299836 | 0.212289 | 0.477967 | 0.61775 | 0.746271 | 0.90054 | 1.30722 | 4.92805 |
| bonus_part | alpha_5 | 4716 | 0.822015 | 0.368064 | 0.195301 | 0.45073 | 0.621052 | 0.749921 | 0.90817 | 1.42408 | 5.24445 |
| bonus_part | alpha_6 | 4716 | 0.809463 | 0.338417 | 0.254802 | 0.452943 | 0.610424 | 0.747217 | 0.90265 | 1.39372 | 4.87966 |
| bonus_part | alpha_norm | 4716 | 2.0967 | 0.591197 | 0.914411 | 1.33423 | 1.76169 | 1.97478 | 2.34166 | 3.20463 | 5.50381 |
