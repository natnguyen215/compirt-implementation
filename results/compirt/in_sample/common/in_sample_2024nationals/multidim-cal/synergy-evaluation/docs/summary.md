# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/multidim-cal/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/multidim-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 59027.1 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 10785.2 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.964115 |
| mean_synergy_contribution | 0.902429 |
| median_synergy_contribution | 1.00279 |
| negative_synergy_fraction | 0 |
| positive_synergy_fraction | 0.999145 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.941458 |
| log_loss | 0.315804 |
| ece | 0.0323877 |
| part_accuracy | 0.863997 |
| part_accuracy_macro_team | 0.867227 |
| part_accuracy_macro_game | 0.864666 |
| part_accuracy_macro_bonus | 0.868134 |
| exact_acc | 0.636169 |
| ppb_mae | 0.705632 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.642609 |
| log_loss | 0.561715 |
| ece | 0.0216391 |
| accuracy | 0.728463 |
| buzz_position_mae | 0.112872 |
| buzz_position_median_absolute_error | 0.094873 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 1.44479 | 0.659271 | -0.579085 | 0.376005 | 1.06173 | 1.45149 | 1.84834 | 2.59956 | 3.26125 |
| player | theta_1 | 189 | -0.6071 | 0.77721 | -2.58397 | -2.00647 | -1.17278 | -0.548296 | 0.01618 | 0.501612 | 0.965158 |
| player | theta_2 | 189 | -0.560774 | 0.767972 | -2.67094 | -2.00184 | -1.02654 | -0.519535 | 0.0255192 | 0.619152 | 1.08222 |
| player | theta_3 | 189 | -0.43407 | 0.58947 | -2.1598 | -1.42698 | -0.827059 | -0.372987 | -0.0107993 | 0.398643 | 0.856389 |
| player | theta_4 | 189 | -0.483349 | 0.695773 | -2.34908 | -1.59067 | -0.955135 | -0.458114 | -0.0313987 | 0.598558 | 1.29405 |
| player | theta_5 | 189 | -0.502433 | 0.71636 | -2.76108 | -1.72831 | -0.936298 | -0.417652 | -0.0562205 | 0.521795 | 1.46413 |
| player | theta_norm | 189 | 1.88149 | 0.586934 | 0.69739 | 1.00226 | 1.44259 | 1.8111 | 2.34542 | 2.87676 | 3.23263 |
| tossup | beta_1 | 360 | 0.987674 | 0.553121 | 0.0779482 | 0.294721 | 0.537609 | 0.833393 | 1.38273 | 2.01233 | 2.52594 |
| tossup | beta_2 | 360 | 0.851644 | 0.492941 | -0.0888983 | 0.32451 | 0.520472 | 0.68552 | 1.08039 | 1.98393 | 2.33206 |
| tossup | beta_3 | 360 | 0.720537 | 0.4117 | -0.087805 | 0.283193 | 0.473206 | 0.618483 | 0.817573 | 1.69917 | 2.66203 |
| tossup | beta_4 | 360 | 0.769276 | 0.457843 | 0.0138249 | 0.252986 | 0.484024 | 0.635056 | 0.896663 | 1.82207 | 2.52208 |
| tossup | beta_5 | 360 | 0.771796 | 0.416413 | 0.00109114 | 0.323107 | 0.50518 | 0.651151 | 0.899416 | 1.67518 | 2.33585 |
| tossup | gamma_1 | 360 | 13.8889 | 35.0641 | 1.56167 | 4.62872 | 5.38537 | 6.43885 | 9.33384 | 39.5115 | 495.637 |
| tossup | gamma_2 | 360 | 8.98156 | 14.8423 | 2.33655 | 4.50869 | 5.30965 | 6.10109 | 7.82215 | 16.3448 | 212.948 |
| tossup | gamma_3 | 360 | 8.6255 | 18.4214 | 2.77432 | 4.60269 | 5.32297 | 5.93093 | 7.02126 | 17.3471 | 317.928 |
| tossup | gamma_4 | 360 | 8.80174 | 16.7874 | 3.64297 | 4.68357 | 5.32402 | 5.97896 | 6.89418 | 14.5247 | 260.077 |
| tossup | gamma_5 | 360 | 10.2503 | 34.3849 | 3.02168 | 4.58383 | 5.29281 | 5.9923 | 7.2697 | 19.9695 | 614.672 |
| tossup | mu_1 | 360 | 0.572069 | 0.125206 | 0.371861 | 0.440462 | 0.478577 | 0.525639 | 0.649591 | 0.823774 | 0.936914 |
| tossup | mu_2 | 360 | 0.549286 | 0.115596 | 0.374118 | 0.438112 | 0.471469 | 0.49832 | 0.600888 | 0.793632 | 0.9494 |
| tossup | mu_3 | 360 | 0.516971 | 0.0909902 | 0.374617 | 0.443037 | 0.467626 | 0.487499 | 0.528817 | 0.713807 | 0.925094 |
| tossup | mu_4 | 360 | 0.528497 | 0.10374 | 0.387201 | 0.432399 | 0.465465 | 0.491233 | 0.542821 | 0.753818 | 0.967105 |
| tossup | mu_5 | 360 | 0.530512 | 0.10422 | 0.363794 | 0.438987 | 0.468055 | 0.494752 | 0.557593 | 0.773991 | 0.967238 |
| tossup | r_1 | 360 | 1.38368 | 0.802872 | 0.181791 | 0.35492 | 0.756147 | 1.19222 | 1.85736 | 2.92793 | 4.10667 |
| tossup | r_2 | 360 | 1.24771 | 0.841732 | 0.213314 | 0.329203 | 0.61448 | 1.02417 | 1.56182 | 3.07609 | 4.92548 |
| tossup | r_3 | 360 | 1.03198 | 0.560965 | 0.197444 | 0.342808 | 0.596095 | 0.893609 | 1.37847 | 2.10881 | 3.43441 |
| tossup | r_4 | 360 | 1.14164 | 0.776522 | 0.199201 | 0.341829 | 0.598218 | 0.88709 | 1.40661 | 2.81941 | 4.24094 |
| tossup | r_5 | 360 | 1.15061 | 0.793308 | 0.19145 | 0.363124 | 0.617774 | 0.924332 | 1.45223 | 2.7213 | 5.07681 |
| tossup | r_norm | 360 | 3.12184 | 0.557305 | 2.01042 | 2.35789 | 2.71911 | 3.03073 | 3.50698 | 4.04484 | 5.29381 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 1071 | 0.0349703 | 1.28195 | -2.33925 | -2.10469 | -1.05813 | 0.154567 | 1.19115 | 1.88424 | 2.06876 |
| bonus_part | alpha_1 | 1071 | 0.826942 | 0.305345 | 0.28283 | 0.445344 | 0.581648 | 0.803515 | 0.983822 | 1.40078 | 2.34887 |
| bonus_part | alpha_2 | 1071 | 0.823791 | 0.316877 | 0.32863 | 0.456242 | 0.598842 | 0.771043 | 0.962433 | 1.38906 | 3.43337 |
| bonus_part | alpha_3 | 1071 | 0.812945 | 0.269568 | 0.335676 | 0.475601 | 0.607881 | 0.775309 | 0.964948 | 1.27041 | 2.48504 |
| bonus_part | alpha_4 | 1071 | 0.815045 | 0.303311 | 0.325671 | 0.441907 | 0.558648 | 0.776711 | 1.00977 | 1.30693 | 2.45901 |
| bonus_part | alpha_5 | 1071 | 0.814032 | 0.290289 | 0.338822 | 0.48866 | 0.618755 | 0.770127 | 0.921441 | 1.31842 | 3.0347 |
| bonus_part | alpha_norm | 1071 | 1.89597 | 0.444882 | 1.09549 | 1.21035 | 1.5449 | 1.91003 | 2.17921 | 2.6341 | 3.63486 |
| synergy_player | psi_1 | 189 | 0.0120582 | 0.237814 | -0.516378 | -0.430586 | -0.0324846 | 0.00620816 | 0.068206 | 0.4353 | 0.487739 |
| synergy_player | psi_2 | 189 | 0.0421615 | 0.253854 | -0.471263 | -0.420647 | -0.0324867 | 0.012878 | 0.0651502 | 0.489834 | 0.67804 |
| synergy_player | psi_3 | 189 | -0.0374017 | 0.222499 | -0.604299 | -0.451199 | -0.0616393 | -0.00663438 | 0.0347264 | 0.387928 | 0.617992 |
| synergy_player | psi_norm | 189 | 0.400433 | 0.112442 | 0.0423936 | 0.180997 | 0.351175 | 0.418738 | 0.459821 | 0.551889 | 0.743341 |
| synergy | synergy_score | 274 | 0.166193 | 0.0785952 | 0.000706681 | 0.0428564 | 0.120962 | 0.172842 | 0.205502 | 0.280055 | 0.547467 |
| synergy | synergy_contribution | 7017 | 0.902429 | 0.384118 | 0 | 0.156892 | 0.658463 | 1.00279 | 1.15707 | 1.54143 | 1.70402 |
