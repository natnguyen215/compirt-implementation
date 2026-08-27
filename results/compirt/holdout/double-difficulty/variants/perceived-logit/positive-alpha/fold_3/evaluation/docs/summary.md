# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-logit/positive-alpha/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-logit/positive-alpha/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 303455 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.611064 |
| log_loss | 0.782683 |
| ece | 0.346736 |
| brier | 0.292505 |
| accuracy | 0.377974 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.39207 |
| probability_std | 0.0940351 |
| probability_p10 | 0.300311 |
| probability_p50 | 0.424666 |
| probability_p90 | 0.543286 |
| mean_predictive_variance | 0.235293 |
| integrated_brier_score | 0.0927016 |
| joint_tossup_event_log_loss | 6.70808 |
| buzz_position_mae | 0.136521 |
| buzz_position_median_absolute_error | 0.11352 |
| buzz_position_bias | -0.0110053 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.400551 |
| first_buzzer_mean_reciprocal_rank | 0.604022 |
| first_buzzer_log_loss | 1.57989 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.611064 |
| neg_average_precision | 0.330054 |
| neg_precision | 0.250491 |
| neg_recall | 0.855843 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.125075 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0489808 |
| no_buzz_calibration_error | 0.0337964 |
| no_buzz_brier | 0.0185553 |
| full_pmf_max_mass_error | 1.11022e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.611064 | 0.782683 | 0.346736 | 0.292505 | 0.377974 | 0.770044 | -0.39207 | 0.0940351 | 0.300311 | 0.424666 | 0.543286 | 0.235293 |
| tossup_correctness | tier | fall | 2817 | 0.613665 | 0.776198 | 0.352948 | 0.289941 | 0.370607 | 0.781683 | -0.411076 | 0.0895072 | 0.312106 | 0.430283 | 0.54273 | 0.23691 |
| tossup_correctness | tier | nationals | 1542 | 0.576756 | 0.783452 | 0.312591 | 0.292123 | 0.402075 | 0.73476 | -0.332685 | 0.0991909 | 0.289936 | 0.422812 | 0.547458 | 0.234103 |
| tossup_correctness | tier | regionals | 1934 | 0.61192 | 0.77416 | 0.330877 | 0.288135 | 0.407446 | 0.75698 | -0.349535 | 0.0991547 | 0.300564 | 0.426376 | 0.555598 | 0.234817 |
| tossup_correctness | tier | winter | 2787 | 0.632009 | 0.794727 | 0.370511 | 0.29834 | 0.351633 | 0.786868 | -0.435235 | 0.0914198 | 0.293968 | 0.419517 | 0.535039 | 0.234646 |
| tossup_correctness | category | Current Events | 125 | 0.593366 | 0.757468 | 0.284528 | 0.281415 | 0.376 | 0.704 | -0.328 | 0.0858725 | 0.309521 | 0.428158 | 0.521066 | 0.236603 |
| tossup_correctness | category | Fine Arts | 1072 | 0.573614 | 0.799434 | 0.35401 | 0.300802 | 0.343284 | 0.770522 | -0.427239 | 0.0915407 | 0.298494 | 0.415084 | 0.538341 | 0.23465 |
| tossup_correctness | category | Geography | 185 | 0.595804 | 0.762561 | 0.287594 | 0.283369 | 0.410811 | 0.702703 | -0.291892 | 0.0907348 | 0.302479 | 0.41507 | 0.543617 | 0.235151 |
| tossup_correctness | category | History | 1443 | 0.632292 | 0.774286 | 0.342077 | 0.288791 | 0.370062 | 0.765073 | -0.39501 | 0.0888988 | 0.305128 | 0.425215 | 0.536599 | 0.236167 |
| tossup_correctness | category | Literature | 1411 | 0.598528 | 0.789271 | 0.378739 | 0.295144 | 0.377746 | 0.81219 | -0.434444 | 0.0963203 | 0.303283 | 0.439397 | 0.553913 | 0.236294 |
| tossup_correctness | category | Mythology | 320 | 0.554462 | 0.83947 | 0.392017 | 0.319288 | 0.303125 | 0.79375 | -0.490625 | 0.088335 | 0.301606 | 0.397453 | 0.513597 | 0.232541 |
| tossup_correctness | category | Other Academic | 64 | 0.583333 | 0.805874 | 0.354941 | 0.30414 | 0.34375 | 0.75 | -0.40625 | 0.0817719 | 0.297749 | 0.392959 | 0.497213 | 0.233552 |
| tossup_correctness | category | Philosophy | 312 | 0.625871 | 0.795495 | 0.382672 | 0.298535 | 0.362179 | 0.801282 | -0.439103 | 0.0962751 | 0.292465 | 0.42415 | 0.546167 | 0.234601 |
| tossup_correctness | category | Popular Culture | 104 | 0.544744 | 0.891278 | 0.454593 | 0.343066 | 0.25 | 0.846154 | -0.596154 | 0.0908654 | 0.28998 | 0.38451 | 0.516202 | 0.229984 |
| tossup_correctness | category | Religion | 358 | 0.649686 | 0.773108 | 0.319077 | 0.288294 | 0.368715 | 0.726257 | -0.357542 | 0.0943691 | 0.270331 | 0.411591 | 0.523715 | 0.232479 |
| tossup_correctness | category | Science | 1431 | 0.630914 | 0.768176 | 0.336566 | 0.285855 | 0.398323 | 0.765199 | -0.366876 | 0.0913522 | 0.304822 | 0.430815 | 0.546107 | 0.236562 |
| tossup_correctness | category | Social Science | 321 | 0.620778 | 0.774781 | 0.324892 | 0.288881 | 0.392523 | 0.744548 | -0.352025 | 0.095067 | 0.29801 | 0.419519 | 0.544336 | 0.234507 |
| tossup_correctness | category | Unknown | 1934 | 0.61192 | 0.77416 | 0.330877 | 0.288135 | 0.407446 | 0.75698 | -0.349535 | 0.0991547 | 0.300564 | 0.426376 | 0.555598 | 0.234817 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.699177 | 0.898676 | 0.386643 | 0.343219 | 0.317708 | 0.697917 | -0.380208 | 0.0889504 | 0.202364 | 0.305502 | 0.439461 | 0.20647 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.65285 | 0.869315 | 0.383763 | 0.332213 | 0.313836 | 0.733408 | -0.419573 | 0.0898586 | 0.240824 | 0.343146 | 0.468803 | 0.219319 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.630182 | 0.821598 | 0.367386 | 0.310954 | 0.31629 | 0.759276 | -0.442986 | 0.087639 | 0.281452 | 0.388713 | 0.507386 | 0.230632 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.606746 | 0.780728 | 0.359499 | 0.292006 | 0.376438 | 0.789125 | -0.412687 | 0.0849641 | 0.324023 | 0.425414 | 0.541188 | 0.237829 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.596207 | 0.721149 | 0.304669 | 0.263608 | 0.449658 | 0.775342 | -0.325685 | 0.0779268 | 0.3724 | 0.468393 | 0.573528 | 0.243087 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1133 | 5.14563 | 1.58823 | 1.86789 | 3.49697 | 4.19798 | 4.76816 | 5.59572 | 7.91948 | 13.328 |
| player | beta | 1133 | -2.86826 | 0.824387 | -6.48062 | -4.31138 | -3.37164 | -2.74063 | -2.29953 | -1.70631 | -0.920134 |
| player | theta_1 | 1133 | -1.62262 | 0.579439 | -3.9416 | -2.60767 | -1.98483 | -1.60238 | -1.2543 | -0.728359 | 0.537919 |
| player | theta_2 | 1133 | -1.59539 | 0.632293 | -3.72911 | -2.57422 | -2.01882 | -1.64301 | -1.21823 | -0.432894 | 0.763195 |
| player | theta_3 | 1133 | -1.48135 | 0.554329 | -3.5985 | -2.34544 | -1.85586 | -1.49864 | -1.11979 | -0.569542 | 0.309032 |
| player | theta_norm | 1133 | 2.85455 | 0.516003 | 0.986264 | 1.99002 | 2.51719 | 2.87666 | 3.20607 | 3.65261 | 4.31643 |
| tossup | start_difficulty_d1 | 1240 | 0.142446 | 0.319242 | -0.919013 | -0.393068 | -0.0697485 | 0.154674 | 0.362264 | 0.665044 | 1.09424 |
| tossup | start_difficulty_d2 | 1240 | 0.167005 | 0.304385 | -0.975329 | -0.34965 | -0.0416924 | 0.174169 | 0.374088 | 0.659597 | 1.0476 |
| tossup | start_difficulty_d3 | 1240 | 0.173184 | 0.305552 | -0.802961 | -0.337647 | -0.0391461 | 0.186551 | 0.384741 | 0.662612 | 1.05751 |
| tossup | end_difficulty_d1 | 1240 | -1.37472 | 0.554484 | -3.87622 | -2.15872 | -1.71544 | -1.43945 | -1.02744 | -0.398884 | -0.0446812 |
| tossup | end_difficulty_d2 | 1240 | -1.2404 | 0.500179 | -3.66551 | -1.99353 | -1.58193 | -1.28806 | -0.850536 | -0.407783 | -0.0116788 |
| tossup | end_difficulty_d3 | 1240 | -1.14799 | 0.512473 | -3.87405 | -1.98661 | -1.47621 | -1.16562 | -0.765328 | -0.331161 | 0.109066 |
| tossup | total_drop_d1 | 1240 | 1.51717 | 0.536083 | 0.629039 | 0.880917 | 1.05657 | 1.46067 | 1.83684 | 2.46348 | 4.97046 |
| tossup | total_drop_d2 | 1240 | 1.40741 | 0.471188 | 0.655885 | 0.872265 | 0.982368 | 1.31927 | 1.71921 | 2.27166 | 4.07689 |
| tossup | total_drop_d3 | 1240 | 1.32118 | 0.438335 | 0.662337 | 0.869207 | 0.958937 | 1.20233 | 1.57378 | 2.19283 | 3.5005 |
| tossup | drop_share_1_d1 | 1240 | 0.256713 | 0.0930281 | 0.0463869 | 0.13261 | 0.194224 | 0.253038 | 0.294206 | 0.446626 | 0.738136 |
| tossup | drop_share_2_d1 | 1240 | 0.272278 | 0.0637559 | 0.0907352 | 0.155358 | 0.224498 | 0.282505 | 0.323712 | 0.352512 | 0.49047 |
| tossup | drop_share_3_d1 | 1240 | 0.471009 | 0.123891 | 0.0754498 | 0.301329 | 0.381775 | 0.447144 | 0.557153 | 0.693134 | 0.849905 |
| tossup | drop_share_1_d2 | 1240 | 0.250725 | 0.0753219 | 0.083581 | 0.13557 | 0.200381 | 0.253775 | 0.291169 | 0.373394 | 0.711615 |
| tossup | drop_share_2_d2 | 1240 | 0.277719 | 0.0663939 | 0.0727388 | 0.157526 | 0.230978 | 0.294702 | 0.329094 | 0.353805 | 0.593657 |
| tossup | drop_share_3_d2 | 1240 | 0.471555 | 0.116347 | 0.105276 | 0.331737 | 0.381945 | 0.445251 | 0.549855 | 0.688922 | 0.832455 |
| tossup | drop_share_1_d3 | 1240 | 0.261575 | 0.0704995 | 0.0720878 | 0.155434 | 0.220562 | 0.264949 | 0.291868 | 0.364371 | 0.685639 |
| tossup | drop_share_2_d3 | 1240 | 0.290147 | 0.0563039 | 0.0671011 | 0.173755 | 0.261262 | 0.305782 | 0.33087 | 0.352496 | 0.495025 |
| tossup | drop_share_3_d3 | 1240 | 0.448278 | 0.100509 | 0.153783 | 0.33305 | 0.380375 | 0.425937 | 0.499101 | 0.644564 | 0.860811 |
| tossup | r_1 | 1240 | 0.37061 | 0.185466 | 0.034057 | 0.0834714 | 0.224378 | 0.364259 | 0.502802 | 0.692569 | 0.857363 |
| tossup | r_2 | 1240 | 0.338868 | 0.17594 | 0.0269083 | 0.0834393 | 0.191976 | 0.329442 | 0.460676 | 0.651728 | 0.844983 |
| tossup | r_3 | 1240 | 0.290522 | 0.1641 | 0.0245049 | 0.0757095 | 0.161347 | 0.261283 | 0.392292 | 0.613174 | 0.85855 |
| tossup | r_norm | 1240 | 0.65251 | 0.0550167 | 0.577482 | 0.583816 | 0.609665 | 0.641913 | 0.684219 | 0.761123 | 0.86441 |
