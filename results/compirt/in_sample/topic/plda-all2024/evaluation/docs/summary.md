# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/plda-all2024/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/plda-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 370838 |
| pyramidal | calibrate_correctness | False |
| pyramidal | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 69571.2 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |
| compositional | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.026995 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.903899 |
| log_loss | 0.416895 |
| ece | 0.0795391 |
| part_accuracy | 0.813586 |
| part_accuracy_macro_team | 0.818199 |
| part_accuracy_macro_game | 0.813384 |
| part_accuracy_macro_bonus | 0.794929 |
| exact_acc | 0.527323 |
| ppb_mae | 2.1892 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.663084 |
| log_loss | 0.611765 |
| ece | 0.181746 |
| accuracy | 0.676232 |
| buzz_position_mae | 0.160887 |
| buzz_position_median_absolute_error | 0.145466 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.903899 | 0.913454 | 0.00955532 | synergy |
| log_loss | 0.416895 | 0.393717 | -0.0231778 | synergy |
| ece | 0.0795391 | 0.0646788 | -0.0148602 | synergy |
| part_accuracy | 0.813586 | 0.833996 | 0.0204105 | synergy |
| part_accuracy_macro_team | 0.818199 | 0.835996 | 0.0177968 | synergy |
| part_accuracy_macro_game | 0.813384 | 0.834276 | 0.0208926 | synergy |
| part_accuracy_macro_bonus | 0.794929 | 0.830191 | 0.0352622 | synergy |
| exact_acc | 0.527323 | 0.568076 | 0.0407535 | synergy |
| ppb_mae | 2.1892 | 0.740042 | -1.44916 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 5.14912 | 0.596633 | 2.67829 | 3.91092 | 4.89201 | 5.21113 | 5.5297 | 5.99478 | 6.81659 |
| player | theta_1 | 1455 | 0.0775118 | 0.969823 | -1.77836 | -1.26544 | -0.658644 | -0.0433431 | 0.677336 | 1.84655 | 3.34732 |
| player | theta_2 | 1455 | 0.120636 | 1.03165 | -1.92529 | -1.2681 | -0.720057 | -0.0267321 | 0.836682 | 1.93954 | 3.61968 |
| player | theta_3 | 1455 | 0.158947 | 1.12213 | -2.01104 | -1.31989 | -0.756809 | -0.00898718 | 0.911735 | 2.17281 | 4.15858 |
| player | theta_4 | 1455 | 0.0434346 | 1.17204 | -2.23774 | -1.44458 | -0.857578 | -0.185644 | 0.781639 | 2.37699 | 4.52054 |
| player | theta_5 | 1455 | 0.103103 | 0.945027 | -1.89514 | -1.12424 | -0.638803 | -0.0880361 | 0.683453 | 1.89759 | 3.68356 |
| player | theta_norm | 1455 | 2.20752 | 0.844195 | 0.357129 | 1.05635 | 1.64203 | 2.05971 | 2.60673 | 3.88705 | 6.0638 |
| tossup | beta_1 | 1260 | 1.1158 | 1.3722 | -3.28751 | -0.0403991 | 0.0788924 | 0.479419 | 1.85057 | 4.00125 | 6.31228 |
| tossup | beta_2 | 1260 | 1.15491 | 1.42008 | -3.45051 | -0.043658 | 0.0880523 | 0.473721 | 2.10915 | 4.00055 | 5.1841 |
| tossup | beta_3 | 1260 | 1.05206 | 1.50265 | -1.88379 | -0.0523042 | 0.0285556 | 0.141546 | 2.3421 | 4.04004 | 4.69468 |
| tossup | beta_4 | 1260 | 1.24527 | 1.57345 | -2.16427 | -0.0439943 | 0.05189 | 0.357581 | 2.57605 | 4.23903 | 5.35759 |
| tossup | beta_5 | 1260 | 0.832639 | 1.24356 | -2.14299 | -0.0503226 | 0.0331266 | 0.235019 | 1.10694 | 3.74788 | 5.52391 |
| tossup | gamma_1 | 1260 | 23.0705 | 108.14 | 2.7116 | 4.59108 | 5.07358 | 5.63102 | 10.1851 | 61.736 | 1812.99 |
| tossup | gamma_2 | 1260 | 26.4026 | 106.656 | 2.68988 | 4.59128 | 5.06392 | 5.60397 | 12.2473 | 84.7552 | 2017.95 |
| tossup | gamma_3 | 1260 | 14.0537 | 31.5735 | 4.16833 | 4.6006 | 4.96144 | 5.28519 | 8.93942 | 51.5601 | 473.532 |
| tossup | gamma_4 | 1260 | 23.9748 | 104.66 | 3.38118 | 4.57399 | 5.00802 | 5.49197 | 11.242 | 68.0475 | 2207.55 |
| tossup | gamma_5 | 1260 | 18.2195 | 86.2413 | 2.30747 | 4.65278 | 4.99605 | 5.3452 | 7.7846 | 40.5302 | 1967.69 |
| tossup | mu_1 | 1260 | 0.529576 | 0.0937769 | 0.190804 | 0.429125 | 0.488205 | 0.505602 | 0.535668 | 0.735541 | 0.916942 |
| tossup | mu_2 | 1260 | 0.53079 | 0.0979803 | 0.167035 | 0.420678 | 0.48816 | 0.504684 | 0.538626 | 0.748248 | 0.915165 |
| tossup | mu_3 | 1260 | 0.530469 | 0.096058 | 0.202918 | 0.438575 | 0.490412 | 0.5036 | 0.523513 | 0.748749 | 0.948904 |
| tossup | mu_4 | 1260 | 0.53798 | 0.101968 | 0.197807 | 0.446358 | 0.489823 | 0.505769 | 0.544527 | 0.76645 | 0.954577 |
| tossup | mu_5 | 1260 | 0.517133 | 0.0798879 | 0.206013 | 0.431455 | 0.488178 | 0.501924 | 0.519111 | 0.687767 | 0.93042 |
| tossup | topic_weight_1 | 1260 | 0.200576 | 0.214052 | 0.00370697 | 0.005197 | 0.0308285 | 0.12792 | 0.292306 | 0.66322 | 0.926751 |
| tossup | topic_weight_2 | 1260 | 0.205835 | 0.214444 | 0.00398982 | 0.00558828 | 0.0316991 | 0.125187 | 0.314035 | 0.652465 | 0.955158 |
| tossup | topic_weight_3 | 1260 | 0.223934 | 0.31904 | 0.00268899 | 0.00332675 | 0.0053612 | 0.0413884 | 0.347751 | 0.908727 | 0.983898 |
| tossup | topic_weight_4 | 1260 | 0.218438 | 0.252486 | 0.00348319 | 0.00432043 | 0.0136133 | 0.100842 | 0.375711 | 0.726929 | 0.953908 |
| tossup | topic_weight_5 | 1260 | 0.151217 | 0.188521 | 0.00295113 | 0.00357754 | 0.00775737 | 0.0711816 | 0.223126 | 0.573349 | 0.943172 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 3768 | 0.364264 | 0.973012 | -2.61011 | -0.896501 | -0.0455036 | 0.0763349 | 0.608826 | 2.48253 | 4.42404 |
| bonus_part | beta_2 | 3768 | 0.431869 | 1.04933 | -2.61171 | -0.886019 | -0.0496071 | 0.0977169 | 0.759031 | 2.78067 | 4.87509 |
| bonus_part | beta_3 | 3768 | 0.411761 | 1.10622 | -2.54447 | -0.845611 | -0.0387156 | 0.0474029 | 0.465362 | 3.08963 | 4.59851 |
| bonus_part | beta_4 | 3768 | 0.376244 | 1.03904 | -2.64265 | -0.890141 | -0.0408969 | 0.0574258 | 0.500674 | 2.80672 | 4.64567 |
| bonus_part | beta_5 | 3768 | 0.334608 | 0.932767 | -2.60833 | -0.796764 | -0.0391294 | 0.0590298 | 0.496662 | 2.45138 | 4.35362 |
