# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/perceived-difficulty/positive-alpha/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 301284 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.601595 |
| log_loss | 0.630779 |
| ece | 0.202388 |
| brier | 0.22 |
| accuracy | 0.650551 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.119493 |
| probability_std | 0.145772 |
| probability_p10 | 0.356658 |
| probability_p50 | 0.586181 |
| probability_p90 | 0.743963 |
| mean_predictive_variance | 0.224173 |
| integrated_brier_score | 0.0932378 |
| joint_tossup_event_log_loss | 6.59304 |
| buzz_position_mae | 0.135432 |
| buzz_position_median_absolute_error | 0.110562 |
| buzz_position_bias | -0.00190791 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.395705 |
| first_buzzer_mean_reciprocal_rank | 0.600064 |
| first_buzzer_log_loss | 1.59138 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.601595 |
| neg_average_precision | 0.313931 |
| neg_precision | 0.304222 |
| neg_recall | 0.403736 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.134976 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0468609 |
| no_buzz_calibration_error | 0.0316765 |
| no_buzz_brier | 0.0182009 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.601595 | 0.630779 | 0.202388 | 0.22 | 0.650551 | 0.770044 | -0.119493 | 0.145772 | 0.356658 | 0.586181 | 0.743963 | 0.224173 |
| tossup_correctness | tier | fall | 2817 | 0.612393 | 0.628997 | 0.221536 | 0.219189 | 0.658857 | 0.781683 | -0.122826 | 0.145591 | 0.347527 | 0.58237 | 0.735042 | 0.225186 |
| tossup_correctness | tier | nationals | 1542 | 0.590459 | 0.623157 | 0.143572 | 0.216777 | 0.653696 | 0.73476 | -0.0810636 | 0.132656 | 0.419044 | 0.608425 | 0.749596 | 0.224087 |
| tossup_correctness | tier | regionals | 1934 | 0.619432 | 0.62204 | 0.178339 | 0.215681 | 0.664426 | 0.75698 | -0.0925543 | 0.152631 | 0.356047 | 0.5988 | 0.765699 | 0.220519 |
| tossup_correctness | tier | winter | 2787 | 0.596473 | 0.642861 | 0.232264 | 0.225601 | 0.630786 | 0.786868 | -0.156082 | 0.145897 | 0.345367 | 0.57286 | 0.732846 | 0.225733 |
| tossup_correctness | category | Current Events | 125 | 0.612408 | 0.650525 | 0.152233 | 0.228641 | 0.616 | 0.704 | -0.088 | 0.132224 | 0.366731 | 0.579686 | 0.700859 | 0.229837 |
| tossup_correctness | category | Fine Arts | 1072 | 0.579957 | 0.629334 | 0.189747 | 0.21923 | 0.654851 | 0.770522 | -0.115672 | 0.14592 | 0.372536 | 0.600102 | 0.756286 | 0.222183 |
| tossup_correctness | category | Geography | 185 | 0.529091 | 0.696593 | 0.178674 | 0.251272 | 0.562162 | 0.702703 | -0.140541 | 0.146102 | 0.32914 | 0.549755 | 0.705666 | 0.227609 |
| tossup_correctness | category | History | 1443 | 0.607092 | 0.63034 | 0.20169 | 0.219813 | 0.657658 | 0.765073 | -0.107415 | 0.142119 | 0.36175 | 0.580249 | 0.735622 | 0.225785 |
| tossup_correctness | category | Literature | 1411 | 0.575534 | 0.598989 | 0.212034 | 0.205418 | 0.678951 | 0.81219 | -0.133239 | 0.140713 | 0.401985 | 0.630158 | 0.763316 | 0.220169 |
| tossup_correctness | category | Mythology | 320 | 0.577547 | 0.641272 | 0.237231 | 0.225131 | 0.61875 | 0.79375 | -0.175 | 0.13977 | 0.363244 | 0.577177 | 0.723827 | 0.22727 |
| tossup_correctness | category | Other Academic | 64 | 0.591146 | 0.628838 | 0.193353 | 0.219222 | 0.671875 | 0.75 | -0.078125 | 0.120612 | 0.372537 | 0.588947 | 0.694817 | 0.23113 |
| tossup_correctness | category | Philosophy | 312 | 0.617484 | 0.595882 | 0.215119 | 0.204019 | 0.698718 | 0.801282 | -0.102564 | 0.139663 | 0.393002 | 0.597164 | 0.75704 | 0.22307 |
| tossup_correctness | category | Popular Culture | 104 | 0.566761 | 0.752466 | 0.360261 | 0.275313 | 0.509615 | 0.846154 | -0.336538 | 0.159165 | 0.266969 | 0.497112 | 0.68791 | 0.224467 |
| tossup_correctness | category | Religion | 358 | 0.625078 | 0.649209 | 0.192269 | 0.228993 | 0.597765 | 0.726257 | -0.128492 | 0.14765 | 0.331738 | 0.548896 | 0.715975 | 0.227044 |
| tossup_correctness | category | Science | 1431 | 0.603305 | 0.655659 | 0.229148 | 0.231584 | 0.626834 | 0.765199 | -0.138365 | 0.137794 | 0.335832 | 0.559546 | 0.702046 | 0.22964 |
| tossup_correctness | category | Social Science | 321 | 0.616134 | 0.637295 | 0.190036 | 0.223138 | 0.65109 | 0.744548 | -0.0934579 | 0.138184 | 0.362907 | 0.564622 | 0.718912 | 0.227933 |
| tossup_correctness | category | Unknown | 1934 | 0.619432 | 0.62204 | 0.178339 | 0.215681 | 0.664426 | 0.75698 | -0.0925543 | 0.152631 | 0.356047 | 0.5988 | 0.765699 | 0.220519 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.70561 | 0.635349 | 0.195136 | 0.22199 | 0.666667 | 0.697917 | -0.03125 | 0.151702 | 0.302205 | 0.521896 | 0.706716 | 0.226883 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.630096 | 0.66073 | 0.210378 | 0.233991 | 0.616423 | 0.733408 | -0.116985 | 0.150388 | 0.307612 | 0.548433 | 0.704478 | 0.226853 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.610376 | 0.640822 | 0.206124 | 0.224577 | 0.634389 | 0.759276 | -0.124887 | 0.145738 | 0.344755 | 0.57429 | 0.725104 | 0.225935 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.596191 | 0.624066 | 0.214861 | 0.216806 | 0.662252 | 0.789125 | -0.126873 | 0.141315 | 0.374686 | 0.590622 | 0.74321 | 0.224515 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.577715 | 0.620353 | 0.185835 | 0.215286 | 0.660616 | 0.775342 | -0.114726 | 0.143105 | 0.383177 | 0.605647 | 0.762781 | 0.221509 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | 0.353552 | 0.973249 | -1.84553 | -1.07664 | -0.452533 | 0.308152 | 1.07152 | 2.02651 | 2.92366 |
| player | theta_2 | 1133 | 0.446894 | 0.928703 | -1.70133 | -0.88232 | -0.266431 | 0.338819 | 1.10555 | 2.06347 | 3.19598 |
| player | theta_3 | 1133 | 0.142615 | 0.768124 | -1.7683 | -0.957517 | -0.445747 | 0.0653016 | 0.657474 | 1.50103 | 2.84069 |
| player | alpha_1 | 1133 | 8.59282 | 3.74059 | 1.01682 | 3.55968 | 6.08595 | 7.98961 | 10.4279 | 16.0147 | 24.0812 |
| player | alpha_2 | 1133 | 10.2842 | 5.22252 | 1.49242 | 4.22431 | 6.9007 | 9.25005 | 12.3718 | 19.3914 | 44.1763 |
| player | alpha_3 | 1133 | 5.84003 | 3.49826 | 0.678575 | 1.44063 | 3.25239 | 5.13753 | 7.72753 | 11.9424 | 24.1982 |
| player | beta_1 | 1133 | -1.6972 | 0.60244 | -4.07927 | -2.76205 | -2.07838 | -1.64692 | -1.2529 | -0.816753 | -0.0663345 |
| player | beta_2 | 1133 | -1.55566 | 0.581394 | -3.84169 | -2.535 | -1.92523 | -1.54739 | -1.12662 | -0.644094 | -0.253865 |
| player | beta_3 | 1133 | -1.45124 | 0.613347 | -3.69855 | -2.60071 | -1.81912 | -1.387 | -0.996666 | -0.57548 | 0.030852 |
| player | theta_norm | 1133 | 1.49658 | 0.709469 | 0.0650948 | 0.513907 | 0.943833 | 1.40463 | 1.98313 | 2.76934 | 3.75658 |
| tossup | start_difficulty_d1 | 1240 | 1.14949 | 0.301495 | -0.166866 | 0.646105 | 0.968033 | 1.16193 | 1.35187 | 1.60851 | 2.07056 |
| tossup | start_difficulty_d2 | 1240 | 1.24184 | 0.307125 | -0.429404 | 0.766457 | 1.06023 | 1.222 | 1.42678 | 1.77045 | 2.14488 |
| tossup | start_difficulty_d3 | 1240 | 1.01854 | 0.390783 | -0.61681 | 0.28516 | 0.808198 | 1.07031 | 1.27216 | 1.57636 | 2.07238 |
| tossup | end_difficulty_d1 | 1240 | 0.139744 | 0.38415 | -1.80046 | -0.595437 | -0.0159152 | 0.180322 | 0.383697 | 0.657206 | 1.18451 |
| tossup | end_difficulty_d2 | 1240 | 0.337359 | 0.381433 | -2.19015 | -0.300028 | 0.151075 | 0.34582 | 0.543169 | 0.981343 | 1.39889 |
| tossup | end_difficulty_d3 | 1240 | 0.00935969 | 0.533411 | -2.46848 | -1.05311 | -0.231424 | 0.104115 | 0.365856 | 0.7041 | 1.24019 |
| tossup | total_drop_d1 | 1240 | 1.00975 | 0.288862 | 0.390814 | 0.627905 | 0.819878 | 0.960814 | 1.15599 | 1.538 | 2.47051 |
| tossup | total_drop_d2 | 1240 | 0.904476 | 0.250833 | 0.363446 | 0.583675 | 0.738007 | 0.857462 | 1.01962 | 1.36017 | 3.11978 |
| tossup | total_drop_d3 | 1240 | 1.00918 | 0.316575 | 0.461608 | 0.645209 | 0.782237 | 0.939444 | 1.15459 | 1.64695 | 2.88208 |
| tossup | drop_share_1_d1 | 1240 | 0.219808 | 0.0799087 | 0.0456029 | 0.114334 | 0.162648 | 0.208592 | 0.265662 | 0.356005 | 0.650266 |
| tossup | drop_share_2_d1 | 1240 | 0.255133 | 0.0646759 | 0.0694518 | 0.14511 | 0.208926 | 0.262056 | 0.301786 | 0.348141 | 0.545271 |
| tossup | drop_share_3_d1 | 1240 | 0.525059 | 0.125191 | 0.156426 | 0.338977 | 0.428975 | 0.518617 | 0.618315 | 0.731369 | 0.884945 |
| tossup | drop_share_1_d2 | 1240 | 0.22143 | 0.0646698 | 0.0713792 | 0.128112 | 0.177781 | 0.217683 | 0.258771 | 0.325468 | 0.620867 |
| tossup | drop_share_2_d2 | 1240 | 0.262623 | 0.0629039 | 0.0663322 | 0.148035 | 0.220936 | 0.27122 | 0.311431 | 0.343627 | 0.483534 |
| tossup | drop_share_3_d2 | 1240 | 0.515948 | 0.110474 | 0.17922 | 0.367461 | 0.434442 | 0.504671 | 0.586754 | 0.709869 | 0.855723 |
| tossup | drop_share_1_d3 | 1240 | 0.235113 | 0.0585986 | 0.060006 | 0.135947 | 0.194487 | 0.239657 | 0.276548 | 0.317405 | 0.528342 |
| tossup | drop_share_2_d3 | 1240 | 0.28518 | 0.0526608 | 0.0749875 | 0.188044 | 0.255067 | 0.296029 | 0.322337 | 0.350539 | 0.476136 |
| tossup | drop_share_3_d3 | 1240 | 0.479707 | 0.101358 | 0.241462 | 0.353083 | 0.402722 | 0.45732 | 0.540574 | 0.662212 | 0.865007 |
| tossup | r_1 | 1240 | 0.382508 | 0.177518 | 0.0360085 | 0.102997 | 0.236543 | 0.391055 | 0.51676 | 0.662377 | 0.831509 |
| tossup | r_2 | 1240 | 0.365983 | 0.170036 | 0.0337445 | 0.0977028 | 0.240224 | 0.362932 | 0.489664 | 0.665421 | 0.860279 |
| tossup | r_3 | 1240 | 0.251509 | 0.137256 | 0.0330223 | 0.0724632 | 0.138743 | 0.228161 | 0.340145 | 0.522086 | 0.644873 |
| tossup | r_norm | 1240 | 0.648301 | 0.0491992 | 0.57735 | 0.583276 | 0.612695 | 0.641123 | 0.673071 | 0.74709 | 0.86599 |
