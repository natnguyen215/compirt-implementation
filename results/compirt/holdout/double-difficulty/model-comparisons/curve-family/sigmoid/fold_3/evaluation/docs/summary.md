# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 298349 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.662451 |
| log_loss | 0.545967 |
| ece | 0.106769 |
| brier | 0.182832 |
| accuracy | 0.728304 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0417401 |
| probability_std | 0.177724 |
| probability_p10 | 0.415175 |
| probability_p50 | 0.681217 |
| probability_p90 | 0.894823 |
| mean_predictive_variance | 0.190962 |
| integrated_brier_score | 0.103799 |
| joint_tossup_event_log_loss | 6.66126 |
| buzz_position_mae | 0.158056 |
| buzz_position_median_absolute_error | 0.1398 |
| buzz_position_bias | -0.0667759 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.328304 |
| first_buzzer_mean_reciprocal_rank | 0.545185 |
| first_buzzer_log_loss | 1.72297 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.662451 |
| neg_average_precision | 0.371564 |
| neg_precision | 0.391776 |
| neg_recall | 0.328544 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.153706 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.00619646 |
| no_buzz_calibration_error | -0.00898792 |
| no_buzz_brier | 0.0140235 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.662451 | 0.545967 | 0.106769 | 0.182832 | 0.728304 | 0.770044 | -0.0417401 | 0.177724 | 0.415175 | 0.681217 | 0.894823 | 0.190962 |
| tossup_correctness | tier | fall | 2817 | 0.674439 | 0.521535 | 0.0937297 | 0.171975 | 0.752574 | 0.781683 | -0.029109 | 0.185164 | 0.434692 | 0.727023 | 0.919176 | 0.177094 |
| tossup_correctness | tier | nationals | 1542 | 0.663049 | 0.567365 | 0.0991912 | 0.191277 | 0.716602 | 0.73476 | -0.0181582 | 0.132983 | 0.45937 | 0.656016 | 0.794486 | 0.213553 |
| tossup_correctness | tier | regionals | 1934 | 0.650525 | 0.571654 | 0.121419 | 0.19396 | 0.70424 | 0.75698 | -0.0527404 | 0.171851 | 0.388298 | 0.658875 | 0.85358 | 0.202012 |
| tossup_correctness | tier | winter | 2787 | 0.655721 | 0.540998 | 0.116031 | 0.181412 | 0.726947 | 0.786868 | -0.0599211 | 0.189494 | 0.405506 | 0.684963 | 0.909967 | 0.184812 |
| tossup_correctness | category | Current Events | 125 | 0.69441 | 0.563519 | 0.0758941 | 0.193104 | 0.672 | 0.704 | -0.032 | 0.167196 | 0.41978 | 0.65348 | 0.879961 | 0.198629 |
| tossup_correctness | category | Fine Arts | 1072 | 0.679324 | 0.536911 | 0.107762 | 0.178845 | 0.742537 | 0.770522 | -0.0279851 | 0.18373 | 0.403924 | 0.688408 | 0.899227 | 0.187936 |
| tossup_correctness | category | Geography | 185 | 0.702378 | 0.577374 | 0.112849 | 0.199313 | 0.681081 | 0.702703 | -0.0216216 | 0.204161 | 0.306617 | 0.591391 | 0.86497 | 0.200064 |
| tossup_correctness | category | History | 1443 | 0.679791 | 0.541628 | 0.105538 | 0.181416 | 0.726265 | 0.765073 | -0.038808 | 0.177717 | 0.42335 | 0.66937 | 0.897097 | 0.192239 |
| tossup_correctness | category | Literature | 1411 | 0.611285 | 0.520435 | 0.112615 | 0.169763 | 0.766123 | 0.81219 | -0.0460666 | 0.16887 | 0.470506 | 0.734364 | 0.920134 | 0.176222 |
| tossup_correctness | category | Mythology | 320 | 0.678955 | 0.493377 | 0.0877188 | 0.161465 | 0.771875 | 0.79375 | -0.021875 | 0.167622 | 0.482626 | 0.742867 | 0.919954 | 0.174138 |
| tossup_correctness | category | Other Academic | 64 | 0.615885 | 0.555489 | 0.130823 | 0.185937 | 0.78125 | 0.75 | 0.03125 | 0.137288 | 0.471742 | 0.670907 | 0.839728 | 0.204312 |
| tossup_correctness | category | Philosophy | 312 | 0.632839 | 0.527267 | 0.144014 | 0.175721 | 0.75 | 0.801282 | -0.0512821 | 0.161967 | 0.442397 | 0.669339 | 0.877822 | 0.195205 |
| tossup_correctness | category | Popular Culture | 104 | 0.59304 | 0.441283 | 0.0770505 | 0.136312 | 0.836538 | 0.846154 | -0.00961538 | 0.137945 | 0.601127 | 0.825296 | 0.938712 | 0.14441 |
| tossup_correctness | category | Religion | 358 | 0.661028 | 0.589982 | 0.11276 | 0.202413 | 0.701117 | 0.726257 | -0.0251397 | 0.163552 | 0.404315 | 0.615026 | 0.822857 | 0.210048 |
| tossup_correctness | category | Science | 1431 | 0.65131 | 0.552247 | 0.100168 | 0.186203 | 0.707198 | 0.765199 | -0.0580014 | 0.178712 | 0.416464 | 0.684156 | 0.901835 | 0.189955 |
| tossup_correctness | category | Social Science | 321 | 0.696908 | 0.553785 | 0.106724 | 0.185224 | 0.732087 | 0.744548 | -0.0124611 | 0.187113 | 0.393481 | 0.655199 | 0.882797 | 0.193584 |
| tossup_correctness | category | Unknown | 1934 | 0.650525 | 0.571654 | 0.121419 | 0.19396 | 0.70424 | 0.75698 | -0.0527404 | 0.171851 | 0.388298 | 0.658875 | 0.85358 | 0.202012 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.736619 | 0.539285 | 0.0434045 | 0.181632 | 0.71875 | 0.697917 | 0.0208333 | 0.170873 | 0.469504 | 0.77575 | 0.903426 | 0.170254 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.743334 | 0.500877 | 0.0226849 | 0.165031 | 0.760405 | 0.733408 | 0.0269966 | 0.174064 | 0.489401 | 0.779463 | 0.934558 | 0.161665 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.680867 | 0.524497 | 0.0635924 | 0.171313 | 0.764253 | 0.759276 | 0.00497738 | 0.176489 | 0.469632 | 0.750806 | 0.923697 | 0.171401 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.666192 | 0.526025 | 0.116397 | 0.174503 | 0.750784 | 0.789125 | -0.0383409 | 0.168728 | 0.443521 | 0.685853 | 0.888653 | 0.191674 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.644577 | 0.595977 | 0.182891 | 0.205233 | 0.669863 | 0.775342 | -0.105479 | 0.161568 | 0.369309 | 0.601742 | 0.798597 | 0.215349 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 4.02271 | 0.553666 | 2.00119 | 3.08137 | 3.6683 | 4.0344 | 4.4159 | 4.88359 | 5.59306 |
| player | theta_1 | 1133 | -0.225913 | 1.00466 | -2.59383 | -1.79432 | -1.02338 | -0.282268 | 0.519672 | 1.46764 | 3.19438 |
| player | theta_2 | 1133 | -0.506968 | 0.719172 | -2.57926 | -1.56013 | -1.04363 | -0.569923 | -0.0294909 | 0.746729 | 1.76606 |
| player | theta_3 | 1133 | -0.56568 | 0.841008 | -2.80321 | -1.83898 | -1.15492 | -0.627355 | -0.0573136 | 0.919159 | 2.17475 |
| player | theta_norm | 1133 | 1.57362 | 0.619661 | 0.151484 | 0.638286 | 1.10967 | 1.53197 | 1.99954 | 2.67285 | 4.33337 |
| tossup | beta_1 | 1240 | -0.609194 | 0.75678 | -3.424 | -2.40381 | -0.764158 | -0.361785 | -0.149574 | 0.162023 | 1.99789 |
| tossup | beta_2 | 1240 | -0.43094 | 0.700701 | -3.88056 | -2.25411 | -0.392165 | -0.225203 | -0.129793 | 0.112877 | 1.97174 |
| tossup | beta_3 | 1240 | -0.433638 | 0.689249 | -3.66313 | -2.3411 | -0.389692 | -0.234474 | -0.124887 | 0.126839 | 1.23815 |
| tossup | gamma_1 | 1240 | 5.46113 | 3.50825 | 0.63131 | 2.98188 | 4.33433 | 4.78612 | 5.18623 | 11.7565 | 31.2809 |
| tossup | gamma_2 | 1240 | 5.49838 | 3.26765 | 0.409641 | 3.9074 | 4.6346 | 4.90228 | 5.18708 | 9.63831 | 39.3323 |
| tossup | gamma_3 | 1240 | 5.56775 | 3.86002 | 0.431171 | 3.94163 | 4.64725 | 4.91157 | 5.17663 | 8.66536 | 63.8918 |
| tossup | mu_1 | 1240 | 0.562481 | 0.120444 | 0.438086 | 0.474706 | 0.495717 | 0.51214 | 0.553644 | 0.871114 | 0.949404 |
| tossup | mu_2 | 1240 | 0.541201 | 0.10806 | 0.442354 | 0.476773 | 0.494024 | 0.506023 | 0.521 | 0.866293 | 0.949222 |
| tossup | mu_3 | 1240 | 0.54022 | 0.10639 | 0.455416 | 0.476867 | 0.493317 | 0.505905 | 0.520746 | 0.856024 | 0.979732 |
| tossup | r_1 | 1240 | 0.418754 | 0.240944 | 0.0380981 | 0.0782466 | 0.207485 | 0.397318 | 0.631313 | 0.81158 | 0.878561 |
| tossup | r_2 | 1240 | 0.289293 | 0.220221 | 0.0463754 | 0.074815 | 0.124625 | 0.206823 | 0.391347 | 0.794121 | 0.909165 |
| tossup | r_3 | 1240 | 0.291953 | 0.209125 | 0.0455501 | 0.0708091 | 0.127962 | 0.22959 | 0.395454 | 0.784553 | 0.891502 |
| tossup | r_norm | 1240 | 0.697444 | 0.0895713 | 0.577394 | 0.58471 | 0.619797 | 0.674517 | 0.770994 | 0.856328 | 0.911431 |
| tossup_hazard | hazard_beta_1 | 1240 | 1.94283 | 1.49683 | -0.0417056 | 0.426511 | 0.675397 | 1.173 | 3.53459 | 4.50636 | 5.10589 |
| tossup_hazard | hazard_beta_2 | 1240 | 1.90106 | 1.2773 | 0.0606091 | 0.420514 | 0.711851 | 1.4687 | 3.18822 | 3.95452 | 4.92006 |
| tossup_hazard | hazard_beta_3 | 1240 | 1.92013 | 1.36821 | -0.0949625 | 0.377215 | 0.685215 | 1.41691 | 3.30406 | 4.19912 | 4.72091 |
| tossup_hazard | hazard_gamma_1 | 1240 | 13.6364 | 39.6102 | 2.37944 | 5.54249 | 6.23842 | 7.24795 | 10.3991 | 35.294 | 1022.37 |
| tossup_hazard | hazard_gamma_2 | 1240 | 14.1519 | 21.2885 | 2.90872 | 5.57569 | 6.41417 | 7.94455 | 13.2015 | 39.0607 | 304.587 |
| tossup_hazard | hazard_gamma_3 | 1240 | 14.733 | 43.211 | 4.16931 | 5.5478 | 6.36202 | 7.67272 | 11.1548 | 36.5411 | 1244.77 |
| tossup_hazard | hazard_mu_1 | 1240 | 0.599856 | 0.105113 | 0.31624 | 0.490167 | 0.53247 | 0.564101 | 0.648445 | 0.823966 | 0.957014 |
| tossup_hazard | hazard_mu_2 | 1240 | 0.597229 | 0.105174 | 0.212474 | 0.470315 | 0.528307 | 0.564327 | 0.659012 | 0.810431 | 0.939207 |
| tossup_hazard | hazard_mu_3 | 1240 | 0.598451 | 0.102403 | 0.248566 | 0.480953 | 0.527518 | 0.569291 | 0.653476 | 0.803078 | 0.946118 |
| tossup_hazard | hazard_r_1 | 1240 | 0.315105 | 0.33889 | 0.0199686 | 0.0319678 | 0.0500539 | 0.102796 | 0.673602 | 0.911021 | 0.95815 |
| tossup_hazard | hazard_r_2 | 1240 | 0.350149 | 0.3363 | 0.0134673 | 0.0276847 | 0.0589297 | 0.152863 | 0.739094 | 0.889105 | 0.951165 |
| tossup_hazard | hazard_r_3 | 1240 | 0.334746 | 0.328449 | 0.0137818 | 0.0272762 | 0.0601274 | 0.152912 | 0.696563 | 0.895301 | 0.949495 |
