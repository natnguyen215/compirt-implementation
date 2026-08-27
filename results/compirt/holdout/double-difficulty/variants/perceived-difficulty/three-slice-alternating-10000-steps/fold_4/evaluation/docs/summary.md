# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating-10000-steps/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/three-slice-alternating-10000-steps/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 307536 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.626634 |
| log_loss | 0.647109 |
| ece | 0.217535 |
| brier | 0.226113 |
| accuracy | 0.645631 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.127724 |
| probability_std | 0.174426 |
| probability_p10 | 0.304311 |
| probability_p50 | 0.577683 |
| probability_p90 | 0.768484 |
| mean_predictive_variance | 0.21646 |
| integrated_brier_score | 0.0956139 |
| joint_tossup_event_log_loss | 6.77765 |
| buzz_position_mae | 0.139718 |
| buzz_position_median_absolute_error | 0.115208 |
| buzz_position_bias | 0.00169304 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.363107 |
| first_buzzer_mean_reciprocal_rank | 0.570248 |
| first_buzzer_log_loss | 1.67632 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.626634 |
| neg_average_precision | 0.316088 |
| neg_precision | 0.31407 |
| neg_recall | 0.475964 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.141207 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0496648 |
| no_buzz_calibration_error | 0.0379378 |
| no_buzz_brier | 0.0173085 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.626634 | 0.647109 | 0.217535 | 0.226113 | 0.645631 | 0.773355 | -0.127724 | 0.174426 | 0.304311 | 0.577683 | 0.768484 | 0.21646 |
| tossup_correctness | tier | fall | 2876 | 0.63065 | 0.666237 | 0.250943 | 0.233095 | 0.643602 | 0.793115 | -0.149513 | 0.182838 | 0.273185 | 0.565889 | 0.763135 | 0.214792 |
| tossup_correctness | tier | nationals | 1579 | 0.6407 | 0.623324 | 0.158768 | 0.21701 | 0.654212 | 0.729576 | -0.0753642 | 0.154701 | 0.366036 | 0.581432 | 0.770412 | 0.221054 |
| tossup_correctness | tier | regionals | 1990 | 0.635597 | 0.621572 | 0.188077 | 0.214926 | 0.664824 | 0.765829 | -0.101005 | 0.178756 | 0.317485 | 0.604146 | 0.788329 | 0.212001 |
| tossup_correctness | tier | winter | 2825 | 0.61522 | 0.65892 | 0.237121 | 0.231975 | 0.629381 | 0.783009 | -0.153628 | 0.170774 | 0.293071 | 0.567448 | 0.755355 | 0.218731 |
| tossup_correctness | category | Current Events | 123 | 0.684153 | 0.691608 | 0.27921 | 0.246326 | 0.577236 | 0.764228 | -0.186992 | 0.160139 | 0.267769 | 0.484182 | 0.705686 | 0.224166 |
| tossup_correctness | category | Fine Arts | 1093 | 0.624847 | 0.63526 | 0.194296 | 0.220544 | 0.660567 | 0.769442 | -0.108875 | 0.176951 | 0.323712 | 0.598862 | 0.787266 | 0.213041 |
| tossup_correctness | category | Geography | 191 | 0.585516 | 0.742344 | 0.217874 | 0.268268 | 0.528796 | 0.691099 | -0.162304 | 0.164761 | 0.237501 | 0.484434 | 0.680609 | 0.222137 |
| tossup_correctness | category | History | 1469 | 0.629502 | 0.669319 | 0.231986 | 0.236596 | 0.616746 | 0.758339 | -0.141593 | 0.159691 | 0.293602 | 0.54774 | 0.718246 | 0.223804 |
| tossup_correctness | category | Literature | 1436 | 0.616287 | 0.598729 | 0.214574 | 0.20389 | 0.706825 | 0.81546 | -0.108635 | 0.171978 | 0.346029 | 0.633775 | 0.793568 | 0.210246 |
| tossup_correctness | category | Mythology | 325 | 0.497925 | 0.690314 | 0.292732 | 0.245364 | 0.624615 | 0.843077 | -0.218462 | 0.170145 | 0.298744 | 0.575211 | 0.755486 | 0.218455 |
| tossup_correctness | category | Other Academic | 67 | 0.632075 | 0.682871 | 0.275668 | 0.243525 | 0.626866 | 0.791045 | -0.164179 | 0.162774 | 0.273943 | 0.541531 | 0.697097 | 0.223244 |
| tossup_correctness | category | Philosophy | 322 | 0.715243 | 0.553778 | 0.182632 | 0.185231 | 0.742236 | 0.785714 | -0.0434783 | 0.176157 | 0.345151 | 0.632334 | 0.801945 | 0.208049 |
| tossup_correctness | category | Popular Culture | 100 | 0.552605 | 0.792965 | 0.40128 | 0.286991 | 0.56 | 0.89 | -0.33 | 0.174307 | 0.219506 | 0.501697 | 0.710657 | 0.21949 |
| tossup_correctness | category | Religion | 365 | 0.647915 | 0.656028 | 0.188202 | 0.230605 | 0.624658 | 0.723288 | -0.0986301 | 0.171676 | 0.30042 | 0.554398 | 0.744413 | 0.219296 |
| tossup_correctness | category | Science | 1456 | 0.602095 | 0.694564 | 0.247536 | 0.247002 | 0.598901 | 0.76717 | -0.168269 | 0.166118 | 0.282009 | 0.534125 | 0.722875 | 0.222019 |
| tossup_correctness | category | Social Science | 333 | 0.627801 | 0.658023 | 0.193372 | 0.231907 | 0.621622 | 0.72973 | -0.108108 | 0.171859 | 0.279429 | 0.555691 | 0.756197 | 0.219108 |
| tossup_correctness | category | Unknown | 1990 | 0.635597 | 0.621572 | 0.188077 | 0.214926 | 0.664824 | 0.765829 | -0.101005 | 0.178756 | 0.317485 | 0.604146 | 0.788329 | 0.212001 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.619071 | 0.775972 | 0.313403 | 0.283982 | 0.480447 | 0.748603 | -0.268156 | 0.17129 | 0.186961 | 0.449875 | 0.664961 | 0.216884 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.617723 | 0.721861 | 0.269617 | 0.259462 | 0.554859 | 0.754441 | -0.199582 | 0.171404 | 0.25296 | 0.501017 | 0.69954 | 0.22039 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.646967 | 0.678729 | 0.245543 | 0.238808 | 0.628688 | 0.766682 | -0.137994 | 0.17416 | 0.272313 | 0.540291 | 0.735645 | 0.219221 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.630902 | 0.636616 | 0.226287 | 0.221341 | 0.663533 | 0.787441 | -0.123909 | 0.169353 | 0.317229 | 0.583744 | 0.76636 | 0.21758 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.618978 | 0.602066 | 0.16552 | 0.20714 | 0.679648 | 0.771758 | -0.0921097 | 0.163409 | 0.377745 | 0.624322 | 0.802197 | 0.21197 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | 0.638667 | 1.11665 | -1.97921 | -1.08903 | -0.160683 | 0.450043 | 1.42624 | 2.65825 | 4.00408 |
| player | theta_2 | 1196 | -0.0742756 | 0.867897 | -3.09586 | -1.49761 | -0.552248 | -0.183923 | 0.389415 | 1.49017 | 3.82557 |
| player | theta_3 | 1196 | 0.510383 | 1.29979 | -2.90895 | -1.38754 | -0.477298 | 0.283991 | 1.56565 | 2.70816 | 3.93264 |
| player | theta_norm | 1196 | 1.86212 | 0.945348 | 0.153372 | 0.498093 | 1.08208 | 1.76359 | 2.5481 | 3.50832 | 4.81807 |
| tossup | start_difficulty_d1 | 1240 | 1.81459 | 0.598926 | -1.0822 | 0.509641 | 1.68649 | 1.96653 | 2.16986 | 2.50652 | 3.31243 |
| tossup | start_difficulty_d2 | 1240 | 0.806806 | 0.78125 | -1.38045 | -0.516318 | 0.269531 | 0.834483 | 1.3469 | 2.07238 | 2.78416 |
| tossup | start_difficulty_d3 | 1240 | 1.17378 | 1.00868 | -1.48843 | -0.373627 | 0.414324 | 1.06956 | 1.93918 | 2.85164 | 4.07285 |
| tossup | end_difficulty_d1 | 1240 | 0.509797 | 0.50218 | -1.93216 | -0.548709 | 0.380317 | 0.574202 | 0.746808 | 1.20012 | 2.1788 |
| tossup | end_difficulty_d2 | 1240 | -0.255674 | 0.883795 | -4.50787 | -1.81873 | -0.819819 | -0.192267 | 0.362129 | 1.06685 | 2.07438 |
| tossup | end_difficulty_d3 | 1240 | 0.11108 | 0.882324 | -3.07061 | -1.43608 | -0.516097 | 0.198648 | 0.822067 | 1.37574 | 2.85783 |
| tossup | total_drop_d1 | 1240 | 1.30479 | 0.360298 | 0.465895 | 0.796299 | 1.00257 | 1.30388 | 1.53175 | 1.89722 | 3.53501 |
| tossup | total_drop_d2 | 1240 | 1.06248 | 0.538108 | 0.52509 | 0.717864 | 0.824825 | 0.911118 | 1.02967 | 2.26229 | 6.05738 |
| tossup | total_drop_d3 | 1240 | 1.0627 | 0.439875 | 0.615889 | 0.730266 | 0.819888 | 0.910895 | 1.05873 | 1.97478 | 3.89785 |
| tossup | drop_share_1_d1 | 1240 | 0.181244 | 0.0914965 | 0.0403931 | 0.0829242 | 0.113248 | 0.146356 | 0.258831 | 0.319017 | 0.68817 |
| tossup | drop_share_2_d1 | 1240 | 0.242838 | 0.101887 | 0.0454315 | 0.107167 | 0.162332 | 0.22486 | 0.331329 | 0.389838 | 0.671398 |
| tossup | drop_share_3_d1 | 1240 | 0.575918 | 0.165603 | 0.114987 | 0.338428 | 0.404552 | 0.613097 | 0.71309 | 0.799354 | 0.914175 |
| tossup | drop_share_1_d2 | 1240 | 0.262091 | 0.0543319 | 0.0340735 | 0.128446 | 0.255342 | 0.278858 | 0.293236 | 0.312732 | 0.47653 |
| tossup | drop_share_2_d2 | 1240 | 0.323113 | 0.051345 | 0.0580061 | 0.185043 | 0.324726 | 0.338386 | 0.347919 | 0.362131 | 0.457007 |
| tossup | drop_share_3_d2 | 1240 | 0.414796 | 0.100767 | 0.193938 | 0.343947 | 0.36215 | 0.380659 | 0.409639 | 0.687836 | 0.90792 |
| tossup | drop_share_1_d3 | 1240 | 0.256032 | 0.0700868 | 0.0476723 | 0.0960137 | 0.251469 | 0.278135 | 0.293953 | 0.312867 | 0.639186 |
| tossup | drop_share_2_d3 | 1240 | 0.321118 | 0.0703603 | 0.0471523 | 0.148524 | 0.323735 | 0.336748 | 0.347683 | 0.3698 | 0.695409 |
| tossup | drop_share_3_d3 | 1240 | 0.42285 | 0.118688 | 0.123362 | 0.340579 | 0.363125 | 0.381025 | 0.413637 | 0.742238 | 0.901944 |
| tossup | r_1 | 1240 | 0.576329 | 0.284544 | 0.0158165 | 0.0329974 | 0.458365 | 0.68003 | 0.790477 | 0.882383 | 0.946639 |
| tossup | r_2 | 1240 | 0.148682 | 0.119037 | 0.0142497 | 0.0298597 | 0.0621588 | 0.107605 | 0.202095 | 0.401573 | 0.650936 |
| tossup | r_3 | 1240 | 0.274988 | 0.288713 | 0.0157821 | 0.0334578 | 0.0713566 | 0.144437 | 0.330013 | 0.899541 | 0.965929 |
| tossup | r_norm | 1240 | 0.775112 | 0.0862213 | 0.58457 | 0.643244 | 0.704394 | 0.773077 | 0.843578 | 0.917237 | 0.966231 |
