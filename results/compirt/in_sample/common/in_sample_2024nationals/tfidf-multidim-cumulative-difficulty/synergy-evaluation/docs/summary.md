# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/tfidf-multidim-cumulative-difficulty/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/tfidf-multidim-cumulative-difficulty`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 60628.9 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 10650.5 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.316076 |
| mean_synergy_contribution | -0.140579 |
| median_synergy_contribution | -0.00418906 |
| negative_synergy_fraction | 0.596266 |
| positive_synergy_fraction | 0.402879 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.934495 |
| log_loss | 0.353324 |
| ece | 0.0696102 |
| part_accuracy | 0.854496 |
| part_accuracy_macro_team | 0.856025 |
| part_accuracy_macro_game | 0.855213 |
| part_accuracy_macro_bonus | 0.853151 |
| exact_acc | 0.617073 |
| ppb_mae | 0.749956 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.706388 |
| log_loss | 0.583761 |
| ece | 0.10309 |
| accuracy | 0.700882 |
| buzz_position_mae | 0.114465 |
| buzz_position_median_absolute_error | 0.0956818 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 5.09626 | 0.866636 | 1.27095 | 3.45243 | 4.7357 | 5.23184 | 5.61174 | 6.23448 | 7.01262 |
| player | theta_1 | 189 | -0.374656 | 0.635949 | -2.25104 | -1.59375 | -0.748297 | -0.270015 | 0.0575213 | 0.550985 | 1.15947 |
| player | theta_2 | 189 | -0.296819 | 0.642649 | -2.66349 | -1.60562 | -0.682779 | -0.214045 | 0.153488 | 0.656243 | 0.968708 |
| player | theta_3 | 189 | -0.40143 | 0.727127 | -2.34947 | -1.83898 | -0.867773 | -0.219561 | 0.120551 | 0.547681 | 1.00398 |
| player | theta_4 | 189 | -0.281183 | 0.670333 | -2.57398 | -1.57665 | -0.643724 | -0.188262 | 0.23255 | 0.651718 | 0.995812 |
| player | theta_5 | 189 | -0.313023 | 0.628383 | -2.29225 | -1.37592 | -0.656392 | -0.24883 | 0.147491 | 0.652457 | 1.20794 |
| player | theta_norm | 189 | 1.49114 | 0.724365 | 0.215492 | 0.648594 | 0.938844 | 1.31501 | 1.96292 | 2.79257 | 3.97981 |
| tossup | beta_1 | 360 | 0.446159 | 0.352789 | -0.0855229 | 0.0753656 | 0.231685 | 0.355244 | 0.513066 | 1.24285 | 1.8913 |
| tossup | beta_2 | 360 | 0.438307 | 0.34433 | -0.655437 | 0.102692 | 0.233971 | 0.347376 | 0.522943 | 1.27501 | 1.85777 |
| tossup | beta_3 | 360 | 0.511236 | 0.42667 | -0.246076 | 0.0473182 | 0.230747 | 0.359888 | 0.658356 | 1.46335 | 2.05563 |
| tossup | beta_4 | 360 | 0.626179 | 0.472179 | -0.253825 | 0.124505 | 0.266599 | 0.4562 | 0.925206 | 1.55201 | 2.44234 |
| tossup | beta_5 | 360 | 0.450055 | 0.367783 | -0.425328 | 0.0724818 | 0.245999 | 0.343058 | 0.513523 | 1.31916 | 1.82085 |
| tossup | gamma_1 | 360 | 9.62698 | 29.3497 | 0.838929 | 4.00203 | 5.00966 | 5.56328 | 6.19547 | 15.4272 | 425.466 |
| tossup | gamma_2 | 360 | 7.11352 | 8.2327 | 1.88969 | 4.0099 | 5.03723 | 5.54573 | 6.18789 | 12.4677 | 89.9663 |
| tossup | gamma_3 | 360 | 8.97226 | 32.4738 | 1.35476 | 3.85751 | 4.91698 | 5.44614 | 6.42873 | 13.317 | 531.013 |
| tossup | gamma_4 | 360 | 13.3514 | 35.8223 | 1.50209 | 3.97349 | 5.05454 | 5.61431 | 7.43352 | 44.5221 | 523.776 |
| tossup | gamma_5 | 360 | 11.8592 | 76.5156 | 1.97089 | 3.78865 | 4.92849 | 5.44818 | 6.2363 | 12.4065 | 1433.87 |
| tossup | mu_1 | 360 | 0.488553 | 0.0993171 | 0.378995 | 0.409186 | 0.437887 | 0.459906 | 0.484583 | 0.700936 | 0.965873 |
| tossup | mu_2 | 360 | 0.485971 | 0.0986671 | 0.323262 | 0.406953 | 0.438794 | 0.460138 | 0.482069 | 0.714944 | 0.926349 |
| tossup | mu_3 | 360 | 0.510369 | 0.11496 | 0.353969 | 0.411882 | 0.439536 | 0.465197 | 0.5449 | 0.793675 | 0.893345 |
| tossup | mu_4 | 360 | 0.533601 | 0.129148 | 0.28658 | 0.412629 | 0.44631 | 0.473951 | 0.606355 | 0.820137 | 0.942627 |
| tossup | mu_5 | 360 | 0.495777 | 0.105532 | 0.369705 | 0.408865 | 0.443886 | 0.460439 | 0.487958 | 0.78994 | 0.965473 |
| tossup | r_1 | 360 | 1.0565 | 0.903761 | 0.141337 | 0.27324 | 0.48493 | 0.815909 | 1.20089 | 3.10869 | 6.3061 |
| tossup | r_2 | 360 | 1.06433 | 0.889621 | 0.150861 | 0.256523 | 0.451324 | 0.768843 | 1.28881 | 3.1619 | 5.31671 |
| tossup | r_3 | 360 | 1.28224 | 1.01677 | 0.143567 | 0.250502 | 0.541268 | 0.91773 | 1.69006 | 3.52164 | 4.63635 |
| tossup | r_4 | 360 | 1.43035 | 1.06665 | 0.141997 | 0.271184 | 0.571834 | 1.03607 | 2.11074 | 3.359 | 5.4365 |
| tossup | r_5 | 360 | 1.09153 | 0.893448 | 0.141528 | 0.275362 | 0.470879 | 0.775998 | 1.38031 | 3.1969 | 4.50007 |
| tossup | r_norm | 360 | 3.33402 | 0.762698 | 1.61192 | 2.25772 | 2.73925 | 3.26199 | 3.83858 | 4.64896 | 6.52048 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 1071 | 0.211992 | 1.51779 | -2.61992 | -2.31168 | -1.05277 | 0.402525 | 1.61938 | 2.30352 | 2.483 |
| bonus_part | alpha_1 | 1071 | 0.7932 | 0.176845 | 0.404815 | 0.592737 | 0.696665 | 0.769937 | 0.84401 | 1.08117 | 2.40389 |
| bonus_part | alpha_2 | 1071 | 0.794546 | 0.185446 | 0.385798 | 0.555604 | 0.669125 | 0.776664 | 0.874306 | 1.10569 | 1.88876 |
| bonus_part | alpha_3 | 1071 | 0.80308 | 0.20793 | 0.380452 | 0.54002 | 0.674265 | 0.766263 | 0.879115 | 1.19254 | 2.5617 |
| bonus_part | alpha_4 | 1071 | 0.792512 | 0.177 | 0.368399 | 0.558794 | 0.683313 | 0.76866 | 0.872999 | 1.13011 | 1.84257 |
| bonus_part | alpha_5 | 1071 | 0.804324 | 0.196156 | 0.421886 | 0.554248 | 0.683889 | 0.773957 | 0.876186 | 1.17114 | 2.10867 |
| bonus_part | alpha_norm | 1071 | 1.81671 | 0.242014 | 1.30123 | 1.47891 | 1.65679 | 1.78749 | 1.94396 | 2.26002 | 3.08658 |
| synergy_player | psi_1 | 189 | -0.0019882 | 0.178638 | -1.09072 | -0.232408 | -0.0351347 | -0.00149273 | 0.0296104 | 0.257814 | 0.807918 |
| synergy_player | psi_2 | 189 | 0.0033956 | 0.152948 | -0.802293 | -0.106488 | -0.0470805 | -0.00817517 | 0.0339865 | 0.275231 | 0.619221 |
| synergy_player | psi_3 | 189 | -0.00191357 | 0.184697 | -0.762777 | -0.360948 | -0.0408929 | 0.00465753 | 0.045066 | 0.201041 | 0.970815 |
| synergy_player | psi_norm | 189 | 0.204275 | 0.217915 | 0.0180758 | 0.0330573 | 0.0638105 | 0.0943351 | 0.278008 | 0.750451 | 1.0921 |
| synergy | synergy_score | 274 | -0.0239802 | 0.124486 | -0.595245 | -0.338714 | -0.0048951 | 0.00115222 | 0.00525855 | 0.124216 | 0.260202 |
| synergy | synergy_contribution | 7017 | -0.140579 | 0.264677 | -0.853352 | -0.592733 | -0.290693 | -0.00418906 | 0.00762603 | 0.0356566 | 0.447896 |
