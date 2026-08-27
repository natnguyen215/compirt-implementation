# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/compact-vs-332/compact/compact-selected/seed_42/fold_4/evaluation`
Result root: `results/compirt/holdout/compact-vs-332/compact/compact-selected/seed_42/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 278091 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.713817 |
| log_loss | 0.500655 |
| ece | 0.0472527 |
| brier | 0.161706 |
| accuracy | 0.770874 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00248112 |
| probability_std | 0.20847 |
| probability_p10 | 0.441111 |
| probability_p50 | 0.823797 |
| probability_p90 | 0.956027 |
| mean_predictive_variance | 0.14054 |
| integrated_brier_score | 0.0945328 |
| joint_tossup_event_log_loss | 6.42009 |
| buzz_position_mae | 0.140865 |
| buzz_position_median_absolute_error | 0.120982 |
| buzz_position_bias | -0.0269796 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.389752 |
| first_buzzer_mean_reciprocal_rank | 0.597981 |
| first_buzzer_log_loss | 1.58467 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.713817 |
| neg_average_precision | 0.428337 |
| neg_precision | 0.490551 |
| neg_recall | 0.28415 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.173034 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.00908625 |
| no_buzz_calibration_error | -0.00264083 |
| no_buzz_brier | 0.010524 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.713817 | 0.500655 | 0.0472527 | 0.161706 | 0.770874 | 0.773355 | -0.00248112 | 0.20847 | 0.441111 | 0.823797 | 0.956027 | 0.14054 |
| tossup_correctness | tier | fall | 2876 | 0.7154 | 0.46938 | 0.0414492 | 0.150282 | 0.788943 | 0.793115 | -0.00417246 | 0.193205 | 0.484951 | 0.829796 | 0.956736 | 0.13892 |
| tossup_correctness | tier | nationals | 1579 | 0.707002 | 0.553188 | 0.0624364 | 0.181715 | 0.737175 | 0.729576 | 0.00759975 | 0.219033 | 0.407037 | 0.810247 | 0.956338 | 0.142638 |
| tossup_correctness | tier | regionals | 1990 | 0.73658 | 0.50153 | 0.0503187 | 0.162201 | 0.775879 | 0.765829 | 0.0100503 | 0.223926 | 0.385769 | 0.811944 | 0.954141 | 0.142441 |
| tossup_correctness | tier | winter | 2825 | 0.697236 | 0.502515 | 0.0582174 | 0.161804 | 0.767788 | 0.783009 | -0.0152212 | 0.204746 | 0.443457 | 0.829423 | 0.956161 | 0.139677 |
| tossup_correctness | category | Current Events | 123 | 0.730741 | 0.517186 | 0.103579 | 0.174418 | 0.747967 | 0.764228 | -0.0162602 | 0.208083 | 0.413615 | 0.758724 | 0.946088 | 0.158922 |
| tossup_correctness | category | Fine Arts | 1093 | 0.715347 | 0.492294 | 0.045472 | 0.156799 | 0.775846 | 0.769442 | 0.00640439 | 0.195215 | 0.477474 | 0.835656 | 0.954482 | 0.137633 |
| tossup_correctness | category | Geography | 191 | 0.761299 | 0.516087 | 0.0685119 | 0.16796 | 0.743455 | 0.691099 | 0.052356 | 0.221584 | 0.425307 | 0.766676 | 0.928624 | 0.16043 |
| tossup_correctness | category | History | 1469 | 0.712979 | 0.51816 | 0.0531777 | 0.171264 | 0.748128 | 0.758339 | -0.010211 | 0.206251 | 0.435558 | 0.822721 | 0.955387 | 0.141149 |
| tossup_correctness | category | Literature | 1436 | 0.693183 | 0.470777 | 0.075174 | 0.146879 | 0.800139 | 0.81546 | -0.0153203 | 0.20908 | 0.467761 | 0.861592 | 0.9694 | 0.125477 |
| tossup_correctness | category | Mythology | 325 | 0.693717 | 0.410691 | 0.045073 | 0.126695 | 0.833846 | 0.843077 | -0.00923077 | 0.134236 | 0.634964 | 0.852914 | 0.944316 | 0.136144 |
| tossup_correctness | category | Other Academic | 67 | 0.579515 | 0.568086 | 0.121994 | 0.181834 | 0.746269 | 0.791045 | -0.0447761 | 0.186186 | 0.429401 | 0.768936 | 0.945661 | 0.153352 |
| tossup_correctness | category | Philosophy | 322 | 0.710947 | 0.482594 | 0.0417305 | 0.157877 | 0.785714 | 0.785714 | 0 | 0.17861 | 0.523963 | 0.818205 | 0.96115 | 0.142301 |
| tossup_correctness | category | Popular Culture | 100 | 0.622063 | 0.361192 | 0.0705026 | 0.105861 | 0.88 | 0.89 | -0.01 | 0.0914487 | 0.771054 | 0.887962 | 0.938842 | 0.108163 |
| tossup_correctness | category | Religion | 365 | 0.643002 | 0.588009 | 0.0759707 | 0.198029 | 0.69863 | 0.723288 | -0.0246575 | 0.190035 | 0.454559 | 0.775947 | 0.932505 | 0.162066 |
| tossup_correctness | category | Science | 1456 | 0.694153 | 0.521601 | 0.0669326 | 0.169504 | 0.759615 | 0.76717 | -0.00755495 | 0.217572 | 0.416708 | 0.815967 | 0.950812 | 0.143039 |
| tossup_correctness | category | Social Science | 333 | 0.746868 | 0.505768 | 0.0495442 | 0.165038 | 0.747748 | 0.72973 | 0.018018 | 0.206634 | 0.387083 | 0.778558 | 0.940573 | 0.158001 |
| tossup_correctness | category | Unknown | 1990 | 0.73658 | 0.50153 | 0.0503187 | 0.162201 | 0.775879 | 0.765829 | 0.0100503 | 0.223926 | 0.385769 | 0.811944 | 0.954141 | 0.142441 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.721061 | 0.528305 | 0.0726557 | 0.173724 | 0.75419 | 0.748603 | 0.00558659 | 0.218538 | 0.360947 | 0.820057 | 0.939786 | 0.142943 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.71319 | 0.51927 | 0.0613226 | 0.167667 | 0.76489 | 0.754441 | 0.0104493 | 0.200574 | 0.463634 | 0.829162 | 0.956834 | 0.139067 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.713995 | 0.505719 | 0.0530068 | 0.163306 | 0.769859 | 0.766682 | 0.00317749 | 0.199151 | 0.474057 | 0.840825 | 0.961156 | 0.134089 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.711233 | 0.479694 | 0.0398655 | 0.152744 | 0.784755 | 0.787441 | -0.00268637 | 0.19436 | 0.488802 | 0.836332 | 0.956634 | 0.137077 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.718428 | 0.510305 | 0.0662499 | 0.166891 | 0.760582 | 0.771758 | -0.0111751 | 0.225955 | 0.369133 | 0.787577 | 0.951661 | 0.149176 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 2.04585 | 0.580863 | 0.0918567 | 1.08662 | 1.66826 | 2.04944 | 2.45659 | 2.98501 | 3.84946 |
| player | theta_1 | 1196 | -1.38952 | 0.656349 | -3.30976 | -2.4213 | -1.864 | -1.40469 | -0.947442 | -0.251962 | 0.380567 |
| player | theta_2 | 1196 | -1.33896 | 0.635461 | -3.09731 | -2.33001 | -1.82249 | -1.3438 | -0.865748 | -0.302533 | 0.585961 |
| player | theta_3 | 1196 | -1.28222 | 0.631949 | -2.89149 | -2.30435 | -1.75478 | -1.27263 | -0.844136 | -0.210154 | 0.637925 |
| player | theta_norm | 1196 | 2.49464 | 0.614575 | 0.838727 | 1.52319 | 2.0537 | 2.47983 | 2.91381 | 3.53196 | 4.39426 |
| tossup | start_difficulty | 1240 | -3.21796 | 0.794239 | -5.25243 | -4.52363 | -3.76226 | -3.22839 | -2.69829 | -1.91298 | -0.473438 |
| tossup | end_difficulty | 1240 | -4.24416 | 0.956111 | -7.39952 | -5.84911 | -4.89522 | -4.2292 | -3.5996 | -2.70341 | -1.14541 |
| tossup | total_drop | 1240 | 1.0262 | 0.294465 | 0.611964 | 0.72029 | 0.852488 | 0.965414 | 1.11326 | 1.49944 | 4.03014 |
| tossup | drop_share_1 | 1240 | 0.29403 | 0.0291675 | 0.128737 | 0.242925 | 0.279854 | 0.296844 | 0.312445 | 0.335062 | 0.380803 |
| tossup | drop_share_2 | 1240 | 0.347867 | 0.0169175 | 0.237011 | 0.323758 | 0.338174 | 0.346923 | 0.357042 | 0.373855 | 0.496131 |
| tossup | drop_share_3 | 1240 | 0.358104 | 0.03265 | 0.257169 | 0.314047 | 0.337959 | 0.354427 | 0.373181 | 0.41374 | 0.622774 |
| tossup | r_1 | 1240 | 0.971244 | 0.808105 | 0.063083 | 0.14874 | 0.362271 | 0.72294 | 1.34897 | 2.65721 | 4.95932 |
| tossup | r_2 | 1240 | 0.829574 | 0.655215 | 0.0501018 | 0.132901 | 0.318226 | 0.622446 | 1.17425 | 2.16064 | 3.36497 |
| tossup | r_3 | 1240 | 0.769589 | 0.694557 | 0.0461694 | 0.120709 | 0.287478 | 0.53445 | 0.960136 | 2.40757 | 3.88754 |
| tossup | r_norm | 1240 | 1.83416 | 0.650726 | 0.405831 | 0.874727 | 1.36286 | 1.78452 | 2.24375 | 2.97877 | 5.02069 |
| tossup_hazard | hazard_start_difficulty | 1240 | 3.78007 | 0.621544 | 1.77304 | 2.77252 | 3.36317 | 3.7589 | 4.22569 | 4.76574 | 5.63005 |
| tossup_hazard | hazard_end_difficulty | 1240 | -1.11901 | 1.52593 | -6.95811 | -3.52213 | -2.10669 | -1.18117 | -0.151631 | 1.4849 | 3.4789 |
| tossup_hazard | hazard_total_drop | 1240 | 4.89908 | 1.51505 | 0.728694 | 2.14775 | 3.97559 | 4.91644 | 5.85719 | 7.33784 | 11.9354 |
| tossup_hazard | hazard_drop_share_1 | 1240 | 0.16041 | 0.0882882 | 0.0341494 | 0.0670676 | 0.0998235 | 0.13604 | 0.194964 | 0.336573 | 0.666874 |
| tossup_hazard | hazard_drop_share_2 | 1240 | 0.315777 | 0.136068 | 0.049867 | 0.120771 | 0.205619 | 0.310514 | 0.40435 | 0.55974 | 0.73456 |
| tossup_hazard | hazard_drop_share_3 | 1240 | 0.523814 | 0.188137 | 0.0721296 | 0.205873 | 0.373949 | 0.531614 | 0.682472 | 0.800769 | 0.906658 |
