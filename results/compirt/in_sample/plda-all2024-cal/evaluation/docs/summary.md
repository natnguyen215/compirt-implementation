# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/plda-all2024-cal/evaluation`
Result root: `results/compirt/in_sample/plda-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 358329 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| pyramidal | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 60428.8 |
| compositional | calibrate_correctness | True |
| compositional | synergy_dimensions | 0 |
| compositional | topic_vectors | topic/fixed/outputs/plda/document_latent_vectors.csv |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.535013 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.909508 |
| log_loss | 0.381065 |
| ece | 0.0137997 |
| part_accuracy | 0.826466 |
| exact_score_accuracy | 0.550992 |
| per_bonus_points_mae | 5.21734 |
| ppb_mae | 2.37358 |
| accuracy | 0.826466 |

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

No sibling comparison/bonus_model_comparison.csv was found.

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

No bonus parameter distribution summary CSV was found.
