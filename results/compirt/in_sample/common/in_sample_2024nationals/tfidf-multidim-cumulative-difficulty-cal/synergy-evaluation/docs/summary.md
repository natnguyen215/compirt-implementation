# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/tfidf-multidim-cumulative-difficulty-cal/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/tfidf-multidim-cumulative-difficulty-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 58948.3 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 10878.2 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.510719 |
| mean_synergy_contribution | 1.51118 |
| median_synergy_contribution | 1.5289 |
| negative_synergy_fraction | 0 |
| positive_synergy_fraction | 0.999145 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.939995 |
| log_loss | 0.320562 |
| ece | 0.0359125 |
| part_accuracy | 0.863664 |
| part_accuracy_macro_team | 0.866499 |
| part_accuracy_macro_game | 0.864071 |
| part_accuracy_macro_bonus | 0.86737 |
| exact_acc | 0.634744 |
| ppb_mae | 0.531767 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.640286 |
| log_loss | 0.562068 |
| ece | 0.0208303 |
| accuracy | 0.728338 |
| buzz_position_mae | 0.111009 |
| buzz_position_median_absolute_error | 0.0914866 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 1.57964 | 0.761117 | -0.42659 | 0.344726 | 1.11728 | 1.47848 | 2.02253 | 2.9039 | 3.83926 |
| player | theta_1 | 189 | -0.702459 | 0.710418 | -2.71231 | -1.94179 | -1.2182 | -0.621879 | -0.131535 | 0.272782 | 0.702276 |
| player | theta_2 | 189 | -0.659619 | 0.747989 | -2.93582 | -1.87617 | -1.24624 | -0.587878 | -0.169434 | 0.549735 | 0.967318 |
| player | theta_3 | 189 | -0.682958 | 0.726745 | -3.06721 | -2.00907 | -1.10569 | -0.568096 | -0.196607 | 0.399044 | 1.08848 |
| player | theta_4 | 189 | -0.74719 | 0.763539 | -3.28072 | -2.16873 | -1.22887 | -0.638841 | -0.177759 | 0.377544 | 0.539552 |
| player | theta_5 | 189 | -0.726586 | 0.68084 | -2.92053 | -1.90066 | -1.13693 | -0.654323 | -0.264149 | 0.367864 | 0.891671 |
| player | theta_norm | 189 | 2.17091 | 0.628767 | 0.661662 | 1.11962 | 1.70625 | 2.19361 | 2.6349 | 3.21528 | 3.56979 |
| tossup | beta_1 | 360 | 0.705751 | 0.436746 | -0.895979 | 0.204732 | 0.426702 | 0.592441 | 0.836035 | 1.64857 | 2.42034 |
| tossup | beta_2 | 360 | 0.733688 | 0.462486 | -0.181854 | 0.221884 | 0.433321 | 0.59026 | 0.923823 | 1.69491 | 2.29811 |
| tossup | beta_3 | 360 | 0.608065 | 0.336402 | -0.163441 | 0.204748 | 0.398042 | 0.540045 | 0.732354 | 1.25243 | 2.52973 |
| tossup | beta_4 | 360 | 0.692359 | 0.441261 | -0.16728 | 0.226667 | 0.41948 | 0.568102 | 0.794366 | 1.63681 | 2.67012 |
| tossup | beta_5 | 360 | 0.711294 | 0.449167 | -0.196156 | 0.212444 | 0.435066 | 0.588835 | 0.818513 | 1.7038 | 2.17422 |
| tossup | gamma_1 | 360 | 10.63 | 30.2303 | 0.452829 | 4.02638 | 5.10046 | 5.85142 | 7.20122 | 20.1801 | 406.529 |
| tossup | gamma_2 | 360 | 13.093 | 34.582 | 1.66449 | 4.21634 | 5.14164 | 5.76914 | 7.06398 | 29.6401 | 407.125 |
| tossup | gamma_3 | 360 | 7.36275 | 10.0009 | 1.11186 | 4.09442 | 5.08125 | 5.70016 | 6.59561 | 13.2384 | 146.878 |
| tossup | gamma_4 | 360 | 9.98305 | 30.6141 | 1.25776 | 4.15532 | 5.03764 | 5.79149 | 6.81629 | 20.3922 | 521.856 |
| tossup | gamma_5 | 360 | 9.66802 | 19.1074 | 1.92592 | 4.19727 | 5.12319 | 5.77625 | 7.48038 | 25.3016 | 244.652 |
| tossup | mu_1 | 360 | 0.542695 | 0.117236 | 0.338305 | 0.426848 | 0.466169 | 0.497026 | 0.586392 | 0.81075 | 0.942589 |
| tossup | mu_2 | 360 | 0.551039 | 0.12748 | 0.397375 | 0.440134 | 0.46872 | 0.497516 | 0.585681 | 0.837198 | 0.97288 |
| tossup | mu_3 | 360 | 0.521727 | 0.105386 | 0.35423 | 0.423287 | 0.458011 | 0.486303 | 0.549233 | 0.769381 | 0.940321 |
| tossup | mu_4 | 360 | 0.538154 | 0.11738 | 0.382159 | 0.425175 | 0.465805 | 0.493745 | 0.568476 | 0.814049 | 0.953997 |
| tossup | mu_5 | 360 | 0.531379 | 0.102598 | 0.37282 | 0.431733 | 0.467219 | 0.494264 | 0.549334 | 0.766346 | 0.89246 |
| tossup | r_1 | 360 | 1.25451 | 0.702371 | 0.212263 | 0.352273 | 0.721288 | 1.12551 | 1.66082 | 2.60868 | 4.04798 |
| tossup | r_2 | 360 | 1.28298 | 0.871928 | 0.218703 | 0.370329 | 0.657384 | 0.986697 | 1.64648 | 3.10142 | 4.10348 |
| tossup | r_3 | 360 | 1.17422 | 0.689913 | 0.159267 | 0.344492 | 0.668634 | 1.03358 | 1.52857 | 2.47057 | 4.62211 |
| tossup | r_4 | 360 | 1.29589 | 0.843521 | 0.163418 | 0.367084 | 0.699666 | 1.08977 | 1.57421 | 3.10352 | 5.55215 |
| tossup | r_5 | 360 | 1.26721 | 0.709467 | 0.243213 | 0.340861 | 0.749706 | 1.10764 | 1.65844 | 2.63237 | 3.80748 |
| tossup | r_norm | 360 | 3.23202 | 0.612469 | 1.94976 | 2.35096 | 2.78993 | 3.1953 | 3.59675 | 4.23481 | 5.87186 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 1071 | 0.0293635 | 1.24389 | -2.2954 | -2.06933 | -1.03408 | 0.158333 | 1.16666 | 1.7873 | 1.96801 |
| bonus_part | alpha_1 | 1071 | 0.802472 | 0.231987 | 0.326187 | 0.467695 | 0.612142 | 0.793377 | 0.971559 | 1.16675 | 2.15715 |
| bonus_part | alpha_2 | 1071 | 0.835818 | 0.352613 | 0.316981 | 0.415955 | 0.534273 | 0.788914 | 1.07033 | 1.35704 | 2.92903 |
| bonus_part | alpha_3 | 1071 | 0.813425 | 0.289455 | 0.288229 | 0.468659 | 0.599694 | 0.765832 | 0.954305 | 1.33061 | 2.70046 |
| bonus_part | alpha_4 | 1071 | 0.822739 | 0.309151 | 0.267015 | 0.434895 | 0.576256 | 0.793232 | 1.00789 | 1.34622 | 3.59482 |
| bonus_part | alpha_5 | 1071 | 0.842086 | 0.344564 | 0.276963 | 0.424108 | 0.549117 | 0.771291 | 1.10627 | 1.41939 | 3.17884 |
| bonus_part | alpha_norm | 1071 | 1.89915 | 0.509407 | 1.00436 | 1.11105 | 1.46352 | 1.92376 | 2.31833 | 2.68987 | 3.84211 |
| synergy_player | psi_1 | 189 | -0.0148327 | 0.284797 | -0.791746 | -0.543644 | -0.0387104 | 0.00364229 | 0.0342788 | 0.52728 | 0.623726 |
| synergy_player | psi_2 | 189 | -0.0419788 | 0.289382 | -0.602694 | -0.557031 | -0.0705515 | -0.00748433 | 0.0306062 | 0.537398 | 0.605014 |
| synergy_player | psi_3 | 189 | -0.0201789 | 0.339211 | -0.690577 | -0.583448 | -0.0906313 | -0.00352328 | 0.0672933 | 0.504382 | 0.807383 |
| synergy_player | psi_norm | 189 | 0.517942 | 0.112367 | 0.062892 | 0.338356 | 0.473266 | 0.520183 | 0.5661 | 0.721721 | 0.861077 |
| synergy | synergy_score | 274 | 0.272026 | 0.101989 | 0.0700645 | 0.113788 | 0.221422 | 0.264708 | 0.313468 | 0.417688 | 0.73912 |
| synergy | synergy_contribution | 7017 | 1.51118 | 0.438192 | 0 | 0.695187 | 1.25514 | 1.5289 | 1.80996 | 2.21502 | 2.46706 |
