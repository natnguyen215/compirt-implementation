# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/terminal-cell-intercepts/off/degree_3/curves_3/dirichlet_2/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/terminal-cell-intercepts/off/degree_3/curves_3/dirichlet_2/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 307566 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.71243 |
| log_loss | 0.498979 |
| ece | 0.0683664 |
| brier | 0.162119 |
| accuracy | 0.779075 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00903084 |
| probability_std | 0.166224 |
| probability_p10 | 0.469766 |
| probability_p50 | 0.730716 |
| probability_p90 | 0.899906 |
| mean_predictive_variance | 0.18048 |
| integrated_brier_score | 0.108581 |
| joint_tossup_event_log_loss | 6.73213 |
| buzz_position_mae | 0.179699 |
| buzz_position_median_absolute_error | 0.159901 |
| buzz_position_bias | -0.10347 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.345044 |
| first_buzzer_mean_reciprocal_rank | 0.558902 |
| first_buzzer_log_loss | 1.69503 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.71243 |
| neg_average_precision | 0.449944 |
| neg_precision | 0.535902 |
| neg_recall | 0.293103 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0919765 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0754861 |
| no_buzz_calibration_error | 0.0603017 |
| no_buzz_brier | 0.0222073 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.71243 | 0.498979 | 0.0683664 | 0.162119 | 0.779075 | 0.770044 | 0.00903084 | 0.166224 | 0.469766 | 0.730716 | 0.899906 | 0.18048 |
| tossup_correctness | tier | fall | 2817 | 0.70549 | 0.485931 | 0.0575775 | 0.155713 | 0.794817 | 0.781683 | 0.0131345 | 0.160958 | 0.501804 | 0.761498 | 0.915222 | 0.170551 |
| tossup_correctness | tier | nationals | 1542 | 0.718207 | 0.536033 | 0.0820832 | 0.178456 | 0.738651 | 0.73476 | 0.00389105 | 0.169526 | 0.428769 | 0.677289 | 0.861927 | 0.197294 |
| tossup_correctness | tier | regionals | 1934 | 0.704483 | 0.516558 | 0.0714914 | 0.170103 | 0.76577 | 0.75698 | 0.00879007 | 0.164978 | 0.453795 | 0.712083 | 0.881368 | 0.188376 |
| tossup_correctness | tier | winter | 2787 | 0.712911 | 0.479466 | 0.0720986 | 0.154016 | 0.794761 | 0.786868 | 0.00789379 | 0.162789 | 0.492438 | 0.745426 | 0.90404 | 0.175732 |
| tossup_correctness | category | Current Events | 125 | 0.76812 | 0.515616 | 0.07365 | 0.171947 | 0.736 | 0.704 | 0.032 | 0.160703 | 0.458111 | 0.686973 | 0.866104 | 0.192035 |
| tossup_correctness | category | Fine Arts | 1072 | 0.734946 | 0.484166 | 0.0609461 | 0.155348 | 0.791978 | 0.770522 | 0.0214552 | 0.168594 | 0.474417 | 0.741507 | 0.905286 | 0.175946 |
| tossup_correctness | category | Geography | 185 | 0.805594 | 0.496297 | 0.100456 | 0.16213 | 0.789189 | 0.702703 | 0.0864865 | 0.206722 | 0.34076 | 0.683629 | 0.855624 | 0.190272 |
| tossup_correctness | category | History | 1443 | 0.738687 | 0.493817 | 0.0735887 | 0.160738 | 0.774082 | 0.765073 | 0.00900901 | 0.168235 | 0.461035 | 0.713506 | 0.892071 | 0.183966 |
| tossup_correctness | category | Literature | 1411 | 0.651085 | 0.478265 | 0.0714299 | 0.152513 | 0.805103 | 0.81219 | -0.00708717 | 0.146845 | 0.545846 | 0.773824 | 0.917825 | 0.165579 |
| tossup_correctness | category | Mythology | 320 | 0.644834 | 0.506788 | 0.0882602 | 0.161884 | 0.78125 | 0.79375 | -0.0125 | 0.150115 | 0.527043 | 0.764561 | 0.909064 | 0.170911 |
| tossup_correctness | category | Other Academic | 64 | 0.657552 | 0.541399 | 0.0941389 | 0.179076 | 0.703125 | 0.75 | -0.046875 | 0.136469 | 0.533325 | 0.723765 | 0.874858 | 0.186507 |
| tossup_correctness | category | Philosophy | 312 | 0.661935 | 0.489422 | 0.0855802 | 0.157007 | 0.801282 | 0.801282 | 0 | 0.148753 | 0.512627 | 0.747008 | 0.902872 | 0.177589 |
| tossup_correctness | category | Popular Culture | 104 | 0.615767 | 0.432595 | 0.0458609 | 0.132953 | 0.836538 | 0.846154 | -0.00961538 | 0.101157 | 0.680807 | 0.822177 | 0.927551 | 0.144851 |
| tossup_correctness | category | Religion | 358 | 0.72916 | 0.533864 | 0.0810914 | 0.178063 | 0.715084 | 0.726257 | -0.0111732 | 0.154057 | 0.451266 | 0.674543 | 0.83957 | 0.20057 |
| tossup_correctness | category | Science | 1431 | 0.706477 | 0.503616 | 0.0687666 | 0.164426 | 0.781971 | 0.765199 | 0.0167715 | 0.170677 | 0.461052 | 0.725937 | 0.903983 | 0.180842 |
| tossup_correctness | category | Social Science | 321 | 0.757883 | 0.506829 | 0.0843783 | 0.164447 | 0.766355 | 0.744548 | 0.0218069 | 0.185773 | 0.399759 | 0.698977 | 0.898734 | 0.186394 |
| tossup_correctness | category | Unknown | 1934 | 0.704483 | 0.516558 | 0.0714914 | 0.170103 | 0.76577 | 0.75698 | 0.00879007 | 0.164978 | 0.453795 | 0.712083 | 0.881368 | 0.188376 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.734817 | 0.554661 | 0.0889322 | 0.187062 | 0.729167 | 0.697917 | 0.03125 | 0.172345 | 0.374471 | 0.626686 | 0.829855 | 0.206787 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.749443 | 0.505893 | 0.0551222 | 0.166291 | 0.76153 | 0.733408 | 0.0281215 | 0.177654 | 0.428467 | 0.711606 | 0.890268 | 0.185857 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.701751 | 0.516011 | 0.063179 | 0.168476 | 0.765611 | 0.759276 | 0.00633484 | 0.170177 | 0.462197 | 0.730968 | 0.900247 | 0.179142 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.697937 | 0.485202 | 0.0731961 | 0.156099 | 0.794702 | 0.789125 | 0.00557686 | 0.158609 | 0.496919 | 0.746713 | 0.908861 | 0.176307 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.715384 | 0.493857 | 0.0745689 | 0.160314 | 0.782534 | 0.775342 | 0.00719178 | 0.16366 | 0.471704 | 0.727471 | 0.894267 | 0.182225 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 4.37227 | 0.575323 | 2.69489 | 3.38974 | 3.97939 | 4.38273 | 4.7779 | 5.31458 | 5.87203 |
| player | theta_1 | 1133 | -1.21326 | 0.976389 | -3.35748 | -2.62363 | -1.91362 | -1.36107 | -0.641203 | 0.603922 | 2.09954 |
| player | theta_2 | 1133 | -1.04015 | 0.779137 | -3.57035 | -2.31342 | -1.54563 | -1.05679 | -0.543065 | 0.23557 | 1.78854 |
| player | theta_3 | 1133 | -1.11834 | 0.763629 | -3.26918 | -2.31821 | -1.65284 | -1.17797 | -0.59571 | 0.222104 | 1.36753 |
| player | theta_norm | 1133 | 2.3455 | 0.667281 | 0.450835 | 1.21254 | 1.88809 | 2.37551 | 2.80393 | 3.3932 | 4.60702 |
| tossup | start_difficulty_d1 | 1240 | -0.749661 | 0.663093 | -3.33172 | -2.00712 | -1.05533 | -0.670669 | -0.358592 | 0.226704 | 1.60443 |
| tossup | start_difficulty_d2 | 1240 | -0.623914 | 0.539033 | -3.23324 | -1.60177 | -0.819873 | -0.566593 | -0.351823 | 0.128918 | 1.30231 |
| tossup | start_difficulty_d3 | 1240 | -0.629585 | 0.527592 | -3.0638 | -1.60146 | -0.83857 | -0.554596 | -0.356949 | 0.101853 | 1.04938 |
| tossup | end_difficulty_d1 | 1240 | -1.91658 | 0.870573 | -5.74668 | -3.70872 | -2.29013 | -1.78219 | -1.41929 | -0.668929 | 0.756995 |
| tossup | end_difficulty_d2 | 1240 | -1.74852 | 0.693825 | -5.91338 | -2.89407 | -1.99455 | -1.66586 | -1.39451 | -0.813555 | 0.538913 |
| tossup | end_difficulty_d3 | 1240 | -1.75645 | 0.667584 | -4.90056 | -2.98131 | -2.01098 | -1.65507 | -1.40814 | -0.86021 | 0.280633 |
| tossup | total_drop_d1 | 1240 | 1.16692 | 0.269669 | 0.709503 | 0.886304 | 1.02507 | 1.11134 | 1.22921 | 1.63134 | 3.47603 |
| tossup | total_drop_d2 | 1240 | 1.12461 | 0.190694 | 0.731936 | 0.914157 | 1.02552 | 1.09821 | 1.1826 | 1.42626 | 3.50307 |
| tossup | total_drop_d3 | 1240 | 1.12687 | 0.182254 | 0.756446 | 0.926253 | 1.034 | 1.10251 | 1.1797 | 1.38489 | 2.84593 |
| tossup | drop_share_1_d1 | 1240 | 0.317396 | 0.0213847 | 0.209435 | 0.288811 | 0.304303 | 0.315192 | 0.326882 | 0.355387 | 0.442368 |
| tossup | drop_share_2_d1 | 1240 | 0.349485 | 0.0124711 | 0.308152 | 0.329508 | 0.341334 | 0.348753 | 0.357043 | 0.371044 | 0.410347 |
| tossup | drop_share_3_d1 | 1240 | 0.333119 | 0.0216797 | 0.229272 | 0.290763 | 0.323075 | 0.335441 | 0.347163 | 0.362648 | 0.413493 |
| tossup | drop_share_1_d2 | 1240 | 0.314574 | 0.0187483 | 0.244383 | 0.289797 | 0.3037 | 0.313016 | 0.323217 | 0.345181 | 0.473002 |
| tossup | drop_share_2_d2 | 1240 | 0.348465 | 0.0117138 | 0.310168 | 0.329482 | 0.340248 | 0.348635 | 0.356425 | 0.367072 | 0.387527 |
| tossup | drop_share_3_d2 | 1240 | 0.336961 | 0.0179133 | 0.215886 | 0.308333 | 0.328481 | 0.33835 | 0.347454 | 0.362069 | 0.397736 |
| tossup | drop_share_1_d3 | 1240 | 0.314812 | 0.0173134 | 0.246661 | 0.291106 | 0.303602 | 0.313931 | 0.323857 | 0.342046 | 0.417608 |
| tossup | drop_share_2_d3 | 1240 | 0.34845 | 0.0117879 | 0.309327 | 0.329098 | 0.340604 | 0.348166 | 0.3562 | 0.367918 | 0.396407 |
| tossup | drop_share_3_d3 | 1240 | 0.336738 | 0.0173585 | 0.255748 | 0.309291 | 0.327821 | 0.337624 | 0.347696 | 0.36254 | 0.395309 |
| tossup | r_1 | 1240 | 0.371983 | 0.200668 | 0.0440961 | 0.0937102 | 0.204412 | 0.340176 | 0.515046 | 0.744572 | 0.86816 |
| tossup | r_2 | 1240 | 0.315208 | 0.17458 | 0.0630441 | 0.104401 | 0.183197 | 0.279046 | 0.40617 | 0.67673 | 0.88576 |
| tossup | r_3 | 1240 | 0.312809 | 0.187357 | 0.0494915 | 0.0913675 | 0.167554 | 0.26255 | 0.420958 | 0.714051 | 0.881364 |
| tossup | r_norm | 1240 | 0.660195 | 0.0740776 | 0.577427 | 0.582678 | 0.60221 | 0.633608 | 0.703461 | 0.812701 | 0.88944 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 1.73141 | 0.956125 | 0.232581 | 0.56105 | 0.909922 | 1.51828 | 2.48046 | 3.4388 | 4.24944 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 1.49113 | 0.816824 | 0.313225 | 0.52663 | 0.854831 | 1.29365 | 1.97375 | 3.08424 | 4.90056 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 1.51972 | 0.818312 | 0.244207 | 0.484893 | 0.838381 | 1.37735 | 2.04099 | 3.05359 | 4.74699 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | -0.606668 | 1.48619 | -9.50426 | -3.61972 | -1.1219 | -0.175976 | 0.303406 | 0.890935 | 1.94765 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | -0.413879 | 1.24433 | -11.1567 | -3.06215 | -0.441542 | -0.1116 | 0.236334 | 0.64323 | 1.34344 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | -0.604546 | 1.36974 | -8.86919 | -3.36739 | -0.632178 | -0.222258 | 0.129047 | 0.710666 | 1.70929 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.33808 | 2.14745 | 0.759133 | 0.947986 | 1.0043 | 1.08629 | 3.88271 | 6.79175 | 11.7496 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.905 | 1.792 | 0.901938 | 0.946072 | 0.991415 | 1.06033 | 1.70699 | 6.12874 | 14.0212 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.12426 | 1.93257 | 0.876073 | 0.952899 | 0.997091 | 1.09387 | 2.48601 | 6.11001 | 11.9999 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.222201 | 0.08424 | 0.0341948 | 0.0641541 | 0.143214 | 0.262296 | 0.286511 | 0.302593 | 0.396995 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.327858 | 0.0850996 | 0.0505558 | 0.13126 | 0.330304 | 0.347031 | 0.359721 | 0.431492 | 0.661917 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.449941 | 0.147701 | 0.179723 | 0.339946 | 0.359585 | 0.382092 | 0.466123 | 0.797011 | 0.915249 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.236979 | 0.0753497 | 0.0263533 | 0.0749375 | 0.204274 | 0.271562 | 0.290917 | 0.305836 | 0.370738 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.33303 | 0.0669317 | 0.0412865 | 0.163189 | 0.334818 | 0.347472 | 0.3586 | 0.391032 | 0.648767 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.429992 | 0.126234 | 0.246838 | 0.341215 | 0.357074 | 0.374996 | 0.434874 | 0.754822 | 0.928775 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.230582 | 0.0785707 | 0.0364598 | 0.0703208 | 0.176779 | 0.267192 | 0.290039 | 0.307882 | 0.500758 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.338491 | 0.0700963 | 0.0682449 | 0.179216 | 0.335237 | 0.348181 | 0.360656 | 0.425227 | 0.72057 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.430927 | 0.126072 | 0.110862 | 0.340316 | 0.35846 | 0.376784 | 0.447097 | 0.736162 | 0.895295 |
| tossup_hazard | hazard_r_1 | 1240 | 0.364035 | 0.312715 | 0.0240643 | 0.0426216 | 0.0876214 | 0.228194 | 0.67153 | 0.904021 | 0.948235 |
| tossup_hazard | hazard_r_2 | 1240 | 0.29657 | 0.269693 | 0.0127905 | 0.0328769 | 0.0700139 | 0.171802 | 0.502984 | 0.827432 | 0.933034 |
| tossup_hazard | hazard_r_3 | 1240 | 0.339395 | 0.288643 | 0.0111002 | 0.026136 | 0.0751584 | 0.239851 | 0.599172 | 0.843886 | 0.947487 |
