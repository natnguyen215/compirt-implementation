# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/tfidf-multidim-hazard-spike-all2024/evaluation`
Result root: `results/compirt/in_sample/tfidf-multidim-hazard-spike-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 360272 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 68474.4 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.013409 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.919742 |
| log_loss | 0.368009 |
| ece | 0.0373874 |
| part_accuracy | 0.837526 |
| exact_score_accuracy | 0.576101 |
| rounded_score_accuracy | 0.575314 |
| per_bonus_points_mae | 5.12906 |
| ppb_mae | 2.27471 |
| accuracy | 0.837526 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.699274 |
| log_loss | 0.575872 |
| ece | 0.126837 |
| accuracy | 0.715177 |
| buzz_position_mae | 0.129116 |
| buzz_position_median_absolute_error | 0.10849 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.919742 | 0.924446 | 0.00470428 | synergy |
| log_loss | 0.368009 | 0.357296 | -0.0107127 | synergy |
| ece | 0.0373874 | 0.0356475 | -0.00173996 | synergy |
| accuracy | 0.837526 | 0.842711 | 0.00518504 | synergy |
| part_accuracy | 0.837526 | 0.842711 | 0.00518504 | synergy |
| exact_score_accuracy | 0.576101 | 0.588914 | 0.0128127 | synergy |
| rounded_score_accuracy | 0.575314 | 0.592533 | 0.0172185 | synergy |
| per_bonus_points_mae | 5.12906 | 4.87721 | -0.251851 | synergy |
| ppb_mae | 2.27471 | 1.9496 | -0.325109 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.51991 | 1.36198 | 0.697611 | 1.59448 | 3.93031 | 4.86583 | 5.46246 | 6.18718 | 7.1942 |
| player | theta_1 | 1455 | -0.00957101 | 0.7293 | -2.3363 | -1.39767 | -0.433495 | 0.10427 | 0.528965 | 0.988212 | 1.61335 |
| player | theta_2 | 1455 | 0.00731483 | 0.742707 | -3.02312 | -1.41406 | -0.373908 | 0.135978 | 0.521328 | 1.00966 | 1.81892 |
| player | theta_3 | 1455 | 0.035099 | 0.729994 | -2.35441 | -1.32439 | -0.436131 | 0.16894 | 0.54611 | 1.06667 | 2.1354 |
| player | theta_4 | 1455 | 0.0836613 | 0.70724 | -2.28516 | -1.20421 | -0.366046 | 0.186512 | 0.592549 | 1.13199 | 2.0712 |
| player | theta_5 | 1455 | -0.0104911 | 0.707027 | -2.27916 | -1.35856 | -0.412902 | 0.119435 | 0.480498 | 0.941569 | 1.49599 |
| player | theta_norm | 1455 | 1.51077 | 0.58392 | 0.214953 | 0.713277 | 1.07374 | 1.42705 | 1.87526 | 2.6132 | 3.3996 |
| tossup | beta_1 | 1260 | 0.814819 | 0.566908 | -0.701659 | 0.215359 | 0.411664 | 0.598562 | 1.1458 | 1.98698 | 2.78196 |
| tossup | beta_2 | 1260 | 0.828037 | 0.523223 | -1.10061 | 0.215639 | 0.446079 | 0.677162 | 1.16424 | 1.86388 | 2.93627 |
| tossup | beta_3 | 1260 | 0.734794 | 0.478152 | -1.31777 | 0.229765 | 0.421593 | 0.580064 | 0.957816 | 1.72974 | 2.5696 |
| tossup | beta_4 | 1260 | 0.716011 | 0.489056 | -0.231781 | 0.233955 | 0.400699 | 0.546138 | 0.876076 | 1.85141 | 2.83601 |
| tossup | beta_5 | 1260 | 0.794513 | 0.505954 | -0.118223 | 0.249565 | 0.44002 | 0.638401 | 1.03619 | 1.89305 | 3.05179 |
| tossup | gamma_1 | 1260 | 14.8482 | 87.9019 | 1.03196 | 3.44505 | 4.58666 | 5.25014 | 6.58721 | 25.9482 | 2070.09 |
| tossup | gamma_2 | 1260 | 17.3895 | 110.091 | 0.729763 | 2.67538 | 4.23153 | 4.96818 | 6.03491 | 23.4223 | 1742.45 |
| tossup | gamma_3 | 1260 | 9.63671 | 37.8863 | 0.799124 | 2.97778 | 4.40194 | 4.97551 | 5.94992 | 17.925 | 930.984 |
| tossup | gamma_4 | 1260 | 9.46572 | 32.8461 | 1.39044 | 3.12011 | 4.47269 | 5.06921 | 5.83547 | 17.7034 | 721.894 |
| tossup | gamma_5 | 1260 | 13.179 | 58.2133 | 0.934046 | 3.24046 | 4.44468 | 5.08687 | 6.09294 | 28.1436 | 1268.11 |
| tossup | mu_1 | 1260 | 0.507231 | 0.111464 | 0.171956 | 0.38539 | 0.445915 | 0.47522 | 0.534029 | 0.745875 | 0.970684 |
| tossup | mu_2 | 1260 | 0.525685 | 0.117746 | 0.205704 | 0.383514 | 0.454022 | 0.489216 | 0.585735 | 0.749708 | 0.958134 |
| tossup | mu_3 | 1260 | 0.508448 | 0.110305 | 0.118756 | 0.392331 | 0.449939 | 0.479751 | 0.535024 | 0.730291 | 0.992941 |
| tossup | mu_4 | 1260 | 0.504545 | 0.106746 | 0.155814 | 0.389325 | 0.449624 | 0.476556 | 0.521299 | 0.729511 | 0.982608 |
| tossup | mu_5 | 1260 | 0.505776 | 0.109587 | 0.113674 | 0.365371 | 0.448544 | 0.480888 | 0.54114 | 0.740115 | 0.986652 |
| tossup | alpha_1 | 1260 | 1.18485 | 0.927937 | 0.0439193 | 0.242477 | 0.469043 | 0.835251 | 1.74535 | 3.01961 | 5.17185 |
| tossup | alpha_2 | 1260 | 1.32243 | 0.969673 | 0.0789037 | 0.22921 | 0.576094 | 1.10088 | 1.84471 | 3.21644 | 6.15927 |
| tossup | alpha_3 | 1260 | 1.06814 | 0.891805 | 0.105808 | 0.220319 | 0.455502 | 0.739886 | 1.3768 | 3.05511 | 5.39113 |
| tossup | alpha_4 | 1260 | 1.03121 | 0.916552 | 0.111275 | 0.21528 | 0.40158 | 0.647368 | 1.32519 | 3.07886 | 5.49448 |
| tossup | alpha_5 | 1260 | 1.13315 | 0.853814 | 0.0834831 | 0.232179 | 0.485512 | 0.855396 | 1.55617 | 2.92062 | 5.03311 |
| tossup | alpha_norm | 1260 | 3.17333 | 0.856744 | 1.14237 | 1.93821 | 2.55109 | 3.07574 | 3.69216 | 4.77544 | 6.76267 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 1.30264 | 1.4988 | -2.11969 | -1.29674 | -0.0324654 | 1.60045 | 2.57756 | 3.33822 | 4.05888 |
| bonus_part | alpha_1 | 3768 | 0.669813 | 0.268233 | 0.237585 | 0.387205 | 0.469811 | 0.603388 | 0.818082 | 1.11032 | 3.02851 |
| bonus_part | alpha_2 | 3768 | 0.679063 | 0.324366 | 0.244582 | 0.342544 | 0.436898 | 0.606951 | 0.844402 | 1.2164 | 3.20817 |
| bonus_part | alpha_3 | 3768 | 0.638515 | 0.256526 | 0.218422 | 0.365484 | 0.43722 | 0.564084 | 0.796798 | 1.09692 | 2.44912 |
| bonus_part | alpha_4 | 3768 | 0.647323 | 0.268496 | 0.207799 | 0.361724 | 0.435726 | 0.56979 | 0.814671 | 1.11217 | 2.20396 |
| bonus_part | alpha_5 | 3768 | 0.648059 | 0.269479 | 0.253387 | 0.3583 | 0.440919 | 0.576248 | 0.807961 | 1.09449 | 2.52484 |
| bonus_part | alpha_norm | 3768 | 1.51917 | 0.486043 | 0.784854 | 0.879543 | 1.08912 | 1.44857 | 1.92222 | 2.31052 | 3.47554 |
