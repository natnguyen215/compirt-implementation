# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/plda-all2024-cal/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/plda-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 358329 |
| pyramidal | calibrate_correctness | True |
| pyramidal | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 62808.9 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |
| synergy | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.562694 |
| mean_synergy_contribution | 0.0639754 |
| median_synergy_contribution | 0.00689773 |
| negative_synergy_fraction | 0.425518 |
| positive_synergy_fraction | 0.54308 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.918246 |
| log_loss | 0.364504 |
| ece | 0.0177973 |
| part_accuracy | 0.838125 |
| part_accuracy_macro_team | 0.840304 |
| part_accuracy_macro_game | 0.838457 |
| part_accuracy_macro_bonus | 0.840561 |
| exact_acc | 0.576663 |
| ppb_mae | 0.533572 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.631458 |
| log_loss | 0.522886 |
| ece | 0.0115755 |
| accuracy | 0.767876 |
| buzz_position_mae | 0.155549 |
| buzz_position_median_absolute_error | 0.140671 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.909508 | 0.918246 | 0.00873797 | synergy |
| log_loss | 0.381065 | 0.364504 | -0.0165617 | synergy |
| ece | 0.0137997 | 0.0177973 | 0.00399761 | no-synergy |
| part_accuracy | 0.826466 | 0.838125 | 0.0116588 | synergy |
| part_accuracy_macro_team | 0.827285 | 0.840304 | 0.0130185 | synergy |
| part_accuracy_macro_game | 0.826371 | 0.838457 | 0.0120862 | synergy |
| part_accuracy_macro_bonus | 0.832129 | 0.840561 | 0.0084323 | synergy |
| exact_acc | 0.550992 | 0.576663 | 0.0256704 | synergy |
| ppb_mae | 1.69657 | 0.533572 | -1.163 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 3.64313 | 0.664401 | 1.21265 | 2.56889 | 3.2074 | 3.61273 | 4.04697 | 4.84496 | 5.7265 |
| player | theta_1 | 1455 | -0.884367 | 0.611372 | -2.50223 | -1.8542 | -1.26978 | -0.922999 | -0.529164 | 0.176923 | 1.3553 |
| player | theta_2 | 1455 | -0.907857 | 0.672524 | -3.13625 | -1.95462 | -1.33242 | -0.95289 | -0.515854 | 0.250505 | 1.66789 |
| player | theta_3 | 1455 | -0.788661 | 0.857674 | -3.03431 | -2.01482 | -1.36382 | -0.901752 | -0.27591 | 0.832745 | 2.70005 |
| player | theta_4 | 1455 | -0.975817 | 0.818254 | -2.93485 | -2.1652 | -1.49466 | -1.07517 | -0.58161 | 0.547716 | 2.77275 |
| player | theta_5 | 1455 | -0.74168 | 0.677613 | -3.11937 | -1.81141 | -1.14801 | -0.778671 | -0.374901 | 0.462177 | 1.76697 |
| player | theta_norm | 1455 | 2.45764 | 0.615958 | 0.501629 | 1.52142 | 2.06367 | 2.38492 | 2.81197 | 3.61361 | 4.99104 |
| tossup | beta_1 | 1260 | 1.38382 | 1.56559 | -0.175263 | -0.00395605 | 0.147389 | 0.653461 | 2.32612 | 4.54976 | 6.38618 |
| tossup | beta_2 | 1260 | 1.43148 | 1.59249 | -1.20229 | 0.00467507 | 0.139791 | 0.689894 | 2.58475 | 4.57096 | 5.50253 |
| tossup | beta_3 | 1260 | 1.2824 | 1.74338 | -0.498354 | -0.0278164 | 0.0428622 | 0.21932 | 2.88849 | 4.61566 | 5.33516 |
| tossup | beta_4 | 1260 | 1.508 | 1.79179 | -0.784574 | -0.0159131 | 0.0789499 | 0.534533 | 3.09435 | 4.88344 | 5.94394 |
| tossup | beta_5 | 1260 | 1.06845 | 1.46 | -0.584473 | -0.0211115 | 0.0571028 | 0.342233 | 1.46201 | 4.43993 | 6.29399 |
| tossup | gamma_1 | 1260 | 16.8275 | 73.2666 | 4.2167 | 4.68403 | 5.10922 | 5.70022 | 9.96272 | 41.6376 | 1676.01 |
| tossup | gamma_2 | 1260 | 16.7849 | 47.3181 | 3.35851 | 4.69512 | 5.11875 | 5.69783 | 10.9913 | 50.8547 | 731.77 |
| tossup | gamma_3 | 1260 | 13.3783 | 33.0483 | 4.13078 | 4.6093 | 4.99086 | 5.32562 | 8.45347 | 42.01 | 471.078 |
| tossup | gamma_4 | 1260 | 19.6246 | 83.4521 | 3.74498 | 4.63653 | 5.02955 | 5.54234 | 10.5621 | 62.2239 | 1936.3 |
| tossup | gamma_5 | 1260 | 17.0541 | 78.2734 | 3.86458 | 4.63265 | 4.99188 | 5.36601 | 7.54525 | 37.1315 | 1549.13 |
| tossup | mu_1 | 1260 | 0.55931 | 0.108509 | 0.211432 | 0.468479 | 0.497522 | 0.514005 | 0.586493 | 0.807033 | 0.973161 |
| tossup | mu_2 | 1260 | 0.559569 | 0.109796 | 0.231064 | 0.468773 | 0.495832 | 0.512652 | 0.589482 | 0.805833 | 0.97175 |
| tossup | mu_3 | 1260 | 0.553339 | 0.109808 | 0.285699 | 0.477036 | 0.49593 | 0.508758 | 0.54997 | 0.819988 | 0.97428 |
| tossup | mu_4 | 1260 | 0.566653 | 0.117595 | 0.236613 | 0.474972 | 0.496263 | 0.513243 | 0.611769 | 0.829464 | 0.980253 |
| tossup | mu_5 | 1260 | 0.54094 | 0.0933766 | 0.208212 | 0.472538 | 0.493067 | 0.508093 | 0.539153 | 0.761558 | 0.952302 |
| tossup | topic_weight_1 | 1260 | 0.200576 | 0.214052 | 0.00370697 | 0.005197 | 0.0308285 | 0.12792 | 0.292306 | 0.66322 | 0.926751 |
| tossup | topic_weight_2 | 1260 | 0.205835 | 0.214444 | 0.00398982 | 0.00558828 | 0.0316991 | 0.125187 | 0.314035 | 0.652465 | 0.955158 |
| tossup | topic_weight_3 | 1260 | 0.223934 | 0.31904 | 0.00268899 | 0.00332675 | 0.0053612 | 0.0413884 | 0.347751 | 0.908727 | 0.983898 |
| tossup | topic_weight_4 | 1260 | 0.218438 | 0.252486 | 0.00348319 | 0.00432043 | 0.0136133 | 0.100842 | 0.375711 | 0.726929 | 0.953908 |
| tossup | topic_weight_5 | 1260 | 0.151217 | 0.188521 | 0.00295113 | 0.00357754 | 0.00775737 | 0.0711816 | 0.223126 | 0.573349 | 0.943172 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 3768 | -0.0232266 | 0.692708 | -2.85003 | -1.36577 | -0.157092 | 0.00573614 | 0.178756 | 1.14067 | 2.57772 |
| bonus_part | beta_2 | 3768 | -0.00825514 | 0.742611 | -2.96531 | -1.46998 | -0.191037 | 0.00826966 | 0.222601 | 1.29743 | 2.87263 |
| bonus_part | beta_3 | 3768 | 0.0605288 | 0.769808 | -2.70979 | -1.35656 | -0.0900108 | 0.00528398 | 0.135165 | 1.60938 | 3.19514 |
| bonus_part | beta_4 | 3768 | -0.0112822 | 0.724164 | -2.83427 | -1.43564 | -0.109964 | 0.00420161 | 0.139512 | 1.32141 | 2.98291 |
| bonus_part | beta_5 | 3768 | -0.0133438 | 0.667653 | -2.82999 | -1.34206 | -0.117274 | 0.00714948 | 0.134953 | 1.12503 | 2.80964 |
| synergy_player | psi_1 | 1455 | -0.011658 | 0.203413 | -0.989978 | -0.371865 | -0.0496947 | -0.00267448 | 0.037177 | 0.337262 | 1.1259 |
| synergy_player | psi_2 | 1455 | -0.00441096 | 0.205784 | -1.24252 | -0.346199 | -0.0452548 | -0.0028167 | 0.0369011 | 0.341105 | 0.952296 |
| synergy_player | psi_3 | 1455 | -0.000384427 | 0.198928 | -0.906896 | -0.357933 | -0.0468897 | -0.00126121 | 0.0449042 | 0.331313 | 1.35419 |
| synergy_player | psi_norm | 1455 | 0.278779 | 0.21373 | 0.00860115 | 0.0438059 | 0.104115 | 0.233216 | 0.390892 | 0.711378 | 1.35439 |
| synergy | synergy_score | 2521 | 0.00100043 | 0.134908 | -0.965089 | -0.244951 | -0.022174 | 0.00616881 | 0.0539839 | 0.176315 | 0.93794 |
| synergy | synergy_contribution | 44487 | 0.0639754 | 0.323685 | -1.12974 | -0.462817 | -0.130789 | 0.00689773 | 0.280551 | 0.60194 | 1.11806 |
