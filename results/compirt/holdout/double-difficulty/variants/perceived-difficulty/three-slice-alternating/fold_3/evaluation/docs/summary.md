# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 327997 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.595645 |
| log_loss | 0.725946 |
| ece | 0.281336 |
| brier | 0.261761 |
| accuracy | 0.551872 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.218172 |
| probability_std | 0.157809 |
| probability_p10 | 0.261556 |
| probability_p50 | 0.506865 |
| probability_p90 | 0.680934 |
| mean_predictive_variance | 0.224969 |
| integrated_brier_score | 0.0938729 |
| joint_tossup_event_log_loss | 6.82032 |
| buzz_position_mae | 0.138127 |
| buzz_position_median_absolute_error | 0.114049 |
| buzz_position_bias | -0.00854359 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.363877 |
| first_buzzer_mean_reciprocal_rank | 0.57439 |
| first_buzzer_log_loss | 1.65974 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.595645 |
| neg_average_precision | 0.302109 |
| neg_precision | 0.27555 |
| neg_recall | 0.582375 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.135005 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0477485 |
| no_buzz_calibration_error | 0.0325642 |
| no_buzz_brier | 0.0182999 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.595645 | 0.725946 | 0.281336 | 0.261761 | 0.551872 | 0.770044 | -0.218172 | 0.157809 | 0.261556 | 0.506865 | 0.680934 | 0.224969 |
| tossup_correctness | tier | fall | 2817 | 0.601537 | 0.749855 | 0.312989 | 0.272516 | 0.526802 | 0.781683 | -0.254881 | 0.157469 | 0.235018 | 0.488838 | 0.657835 | 0.224223 |
| tossup_correctness | tier | nationals | 1542 | 0.565291 | 0.685143 | 0.211451 | 0.245229 | 0.581712 | 0.73476 | -0.153048 | 0.131339 | 0.340147 | 0.539691 | 0.684726 | 0.232207 |
| tossup_correctness | tier | regionals | 1934 | 0.619546 | 0.703075 | 0.25376 | 0.250442 | 0.584798 | 0.75698 | -0.172182 | 0.164148 | 0.266304 | 0.523648 | 0.702564 | 0.223045 |
| tossup_correctness | tier | winter | 2787 | 0.606339 | 0.740228 | 0.307144 | 0.267892 | 0.537854 | 0.786868 | -0.249013 | 0.1629 | 0.250877 | 0.493089 | 0.684543 | 0.223052 |
| tossup_correctness | category | Current Events | 125 | 0.56941 | 0.748008 | 0.231506 | 0.27087 | 0.536 | 0.704 | -0.168 | 0.151355 | 0.229239 | 0.495434 | 0.653767 | 0.226335 |
| tossup_correctness | category | Fine Arts | 1072 | 0.577319 | 0.735387 | 0.284369 | 0.266359 | 0.543843 | 0.770522 | -0.226679 | 0.155564 | 0.253069 | 0.502873 | 0.672391 | 0.225608 |
| tossup_correctness | category | Geography | 185 | 0.540699 | 0.791995 | 0.260483 | 0.291719 | 0.486486 | 0.702703 | -0.216216 | 0.161152 | 0.221223 | 0.439576 | 0.652589 | 0.220692 |
| tossup_correctness | category | History | 1443 | 0.604987 | 0.740914 | 0.293998 | 0.268558 | 0.522523 | 0.765073 | -0.24255 | 0.153817 | 0.248883 | 0.484359 | 0.661489 | 0.225504 |
| tossup_correctness | category | Literature | 1411 | 0.563976 | 0.702434 | 0.294882 | 0.251716 | 0.564139 | 0.81219 | -0.248051 | 0.153623 | 0.300467 | 0.540821 | 0.702096 | 0.2261 |
| tossup_correctness | category | Mythology | 320 | 0.567526 | 0.745732 | 0.314624 | 0.272306 | 0.540625 | 0.79375 | -0.253125 | 0.151486 | 0.262101 | 0.497266 | 0.667876 | 0.226616 |
| tossup_correctness | category | Other Academic | 64 | 0.589844 | 0.69839 | 0.258009 | 0.251536 | 0.59375 | 0.75 | -0.15625 | 0.133719 | 0.314816 | 0.53305 | 0.638891 | 0.232086 |
| tossup_correctness | category | Philosophy | 312 | 0.63929 | 0.67295 | 0.28799 | 0.238886 | 0.596154 | 0.801282 | -0.205128 | 0.152241 | 0.305595 | 0.524497 | 0.705939 | 0.226646 |
| tossup_correctness | category | Popular Culture | 104 | 0.520597 | 0.984551 | 0.458003 | 0.366001 | 0.384615 | 0.846154 | -0.461538 | 0.169948 | 0.139462 | 0.396466 | 0.583424 | 0.208607 |
| tossup_correctness | category | Religion | 358 | 0.620016 | 0.731973 | 0.263789 | 0.265453 | 0.558659 | 0.726257 | -0.167598 | 0.16539 | 0.237863 | 0.482288 | 0.666582 | 0.221237 |
| tossup_correctness | category | Science | 1431 | 0.586225 | 0.736293 | 0.285198 | 0.266817 | 0.534591 | 0.765199 | -0.230608 | 0.150732 | 0.260899 | 0.501021 | 0.663744 | 0.22688 |
| tossup_correctness | category | Social Science | 321 | 0.608378 | 0.722281 | 0.262874 | 0.260717 | 0.58567 | 0.744548 | -0.158879 | 0.156321 | 0.250343 | 0.504186 | 0.67984 | 0.225228 |
| tossup_correctness | category | Unknown | 1934 | 0.619546 | 0.703075 | 0.25376 | 0.250442 | 0.584798 | 0.75698 | -0.172182 | 0.164148 | 0.266304 | 0.523648 | 0.702564 | 0.223045 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.712301 | 0.773043 | 0.308474 | 0.28317 | 0.463542 | 0.697917 | -0.234375 | 0.144752 | 0.20204 | 0.38945 | 0.58035 | 0.216824 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.613199 | 0.795855 | 0.314667 | 0.292807 | 0.466817 | 0.733408 | -0.266592 | 0.15319 | 0.196009 | 0.429291 | 0.613587 | 0.21993 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.614929 | 0.752579 | 0.29975 | 0.273315 | 0.525792 | 0.759276 | -0.233484 | 0.154476 | 0.234871 | 0.478194 | 0.653814 | 0.224499 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.588591 | 0.72241 | 0.293894 | 0.260127 | 0.555594 | 0.789125 | -0.233531 | 0.152035 | 0.278007 | 0.516871 | 0.677175 | 0.226863 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.569783 | 0.684884 | 0.243129 | 0.243763 | 0.599658 | 0.775342 | -0.175685 | 0.153067 | 0.307687 | 0.556443 | 0.713672 | 0.225533 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | 0.317621 | 0.948224 | -1.87439 | -1.19008 | -0.383899 | 0.275955 | 0.988128 | 1.96768 | 2.79693 |
| player | theta_2 | 1133 | 0.194029 | 0.855534 | -1.82452 | -1.12558 | -0.491696 | 0.179207 | 0.829408 | 1.60336 | 2.70702 |
| player | theta_3 | 1133 | 0.23332 | 0.885105 | -1.87013 | -1.14975 | -0.427064 | 0.176275 | 0.919715 | 1.67545 | 2.64738 |
| player | theta_norm | 1133 | 1.46325 | 0.681629 | 0.153227 | 0.494156 | 0.920666 | 1.37808 | 1.95423 | 2.69173 | 3.64391 |
| tossup | start_difficulty_d1 | 1240 | 1.63104 | 0.361434 | 0.082831 | 0.96395 | 1.42944 | 1.66073 | 1.8828 | 2.15326 | 2.74327 |
| tossup | start_difficulty_d2 | 1240 | 1.56563 | 0.372643 | -0.576539 | 0.898512 | 1.35078 | 1.60224 | 1.80755 | 2.11236 | 2.49563 |
| tossup | start_difficulty_d3 | 1240 | 1.53632 | 0.354303 | -0.0329866 | 0.851 | 1.35922 | 1.57567 | 1.77091 | 2.03207 | 2.61024 |
| tossup | end_difficulty_d1 | 1240 | 0.465617 | 0.391583 | -1.6627 | -0.213636 | 0.270131 | 0.474475 | 0.699784 | 1.05876 | 1.71223 |
| tossup | end_difficulty_d2 | 1240 | 0.265588 | 0.434302 | -2.67633 | -0.518595 | 0.0426258 | 0.336184 | 0.549621 | 0.834353 | 1.3518 |
| tossup | end_difficulty_d3 | 1240 | 0.433777 | 0.427821 | -2.1563 | -0.383646 | 0.243209 | 0.503426 | 0.713565 | 0.98726 | 1.38601 |
| tossup | total_drop_d1 | 1240 | 1.16543 | 0.371881 | 0.539234 | 0.729533 | 0.87168 | 1.07485 | 1.39815 | 1.8461 | 3.58155 |
| tossup | total_drop_d2 | 1240 | 1.30005 | 0.484104 | 0.544013 | 0.744279 | 0.921044 | 1.19529 | 1.58706 | 2.14869 | 4.73343 |
| tossup | total_drop_d3 | 1240 | 1.10254 | 0.347116 | 0.4918 | 0.720332 | 0.867678 | 1.00454 | 1.24039 | 1.74493 | 2.9046 |
| tossup | drop_share_1_d1 | 1240 | 0.200195 | 0.0603565 | 0.0519967 | 0.106023 | 0.152604 | 0.20257 | 0.243837 | 0.290476 | 0.471755 |
| tossup | drop_share_2_d1 | 1240 | 0.27217 | 0.0693195 | 0.0591282 | 0.141834 | 0.227534 | 0.290364 | 0.320256 | 0.357502 | 0.513278 |
| tossup | drop_share_3_d1 | 1240 | 0.527635 | 0.119212 | 0.216606 | 0.37308 | 0.435157 | 0.505893 | 0.60894 | 0.745917 | 0.874885 |
| tossup | drop_share_1_d2 | 1240 | 0.194757 | 0.0660359 | 0.0418553 | 0.0970346 | 0.137493 | 0.191687 | 0.248124 | 0.298359 | 0.479601 |
| tossup | drop_share_2_d2 | 1240 | 0.266241 | 0.073031 | 0.0752778 | 0.136935 | 0.210579 | 0.280266 | 0.323114 | 0.361816 | 0.537409 |
| tossup | drop_share_3_d2 | 1240 | 0.539002 | 0.1293 | 0.0960198 | 0.365778 | 0.427473 | 0.525652 | 0.640604 | 0.760503 | 0.874813 |
| tossup | drop_share_1_d3 | 1240 | 0.215851 | 0.0532877 | 0.0526683 | 0.122592 | 0.181084 | 0.217446 | 0.253776 | 0.29028 | 0.438979 |
| tossup | drop_share_2_d3 | 1240 | 0.28869 | 0.0564299 | 0.0737378 | 0.175275 | 0.259679 | 0.29937 | 0.325513 | 0.356608 | 0.507899 |
| tossup | drop_share_3_d3 | 1240 | 0.495458 | 0.0986751 | 0.240293 | 0.37168 | 0.422368 | 0.478435 | 0.548818 | 0.686703 | 0.873594 |
| tossup | r_1 | 1240 | 0.380461 | 0.213231 | 0.0362049 | 0.0836393 | 0.2036 | 0.358175 | 0.536489 | 0.757719 | 0.924796 |
| tossup | r_2 | 1240 | 0.331607 | 0.193457 | 0.0261986 | 0.0638253 | 0.171399 | 0.312278 | 0.462109 | 0.700354 | 0.867802 |
| tossup | r_3 | 1240 | 0.287931 | 0.16305 | 0.0377135 | 0.0698125 | 0.151808 | 0.27094 | 0.395251 | 0.59503 | 0.81815 |
| tossup | r_norm | 1240 | 0.664748 | 0.0715715 | 0.577416 | 0.582392 | 0.607814 | 0.648477 | 0.700674 | 0.810078 | 0.926464 |
