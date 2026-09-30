# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-3/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/training/incorrect-loss-weight/weight-3/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 299017 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.708728 |
| log_loss | 0.592947 |
| ece | 0.18373 |
| brier | 0.202743 |
| accuracy | 0.688442 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0736831 |
| probability_std | 0.217762 |
| probability_p10 | 0.267166 |
| probability_p50 | 0.601984 |
| probability_p90 | 0.854204 |
| mean_predictive_variance | 0.196271 |
| integrated_brier_score | 0.101009 |
| joint_tossup_event_log_loss | 6.70839 |
| buzz_position_mae | 0.151454 |
| buzz_position_median_absolute_error | 0.133826 |
| buzz_position_bias | -0.0474003 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.34884 |
| first_buzzer_mean_reciprocal_rank | 0.561042 |
| first_buzzer_log_loss | 1.69079 |
| first_buzzer_events | 9093 |
| neg_auroc | 0.708728 |
| neg_average_precision | 0.443121 |
| neg_precision | 0.395833 |
| neg_recall | 0.588534 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.190919 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0148608 |
| no_buzz_calibration_error | -0.00104826 |
| no_buzz_brier | 0.0153788 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.708728 | 0.592947 | 0.18373 | 0.202743 | 0.688442 | 0.762125 | -0.0736831 | 0.217762 | 0.267166 | 0.601984 | 0.854204 | 0.196271 |
| tossup_correctness | tier | fall | 2842 | 0.725768 | 0.558674 | 0.179505 | 0.188196 | 0.71886 | 0.785362 | -0.0665025 | 0.218364 | 0.285393 | 0.633316 | 0.880397 | 0.190926 |
| tossup_correctness | tier | nationals | 1564 | 0.712248 | 0.615209 | 0.173346 | 0.212343 | 0.670077 | 0.718031 | -0.047954 | 0.216718 | 0.241978 | 0.559641 | 0.825579 | 0.200826 |
| tossup_correctness | tier | regionals | 1937 | 0.685716 | 0.613146 | 0.186209 | 0.210928 | 0.668043 | 0.758389 | -0.0903459 | 0.211984 | 0.270256 | 0.595327 | 0.842562 | 0.199791 |
| tossup_correctness | tier | winter | 2750 | 0.700485 | 0.601478 | 0.192256 | 0.206552 | 0.681818 | 0.765818 | -0.084 | 0.218472 | 0.259945 | 0.600952 | 0.847196 | 0.196725 |
| tossup_correctness | category | Current Events | 126 | 0.696765 | 0.64356 | 0.238991 | 0.226898 | 0.634921 | 0.769841 | -0.134921 | 0.208406 | 0.238582 | 0.536124 | 0.80737 | 0.205615 |
| tossup_correctness | category | Fine Arts | 1071 | 0.739269 | 0.576145 | 0.190048 | 0.195962 | 0.698413 | 0.766573 | -0.0681606 | 0.227144 | 0.243409 | 0.600836 | 0.861958 | 0.192549 |
| tossup_correctness | category | Geography | 185 | 0.786268 | 0.643974 | 0.241263 | 0.220538 | 0.664865 | 0.697297 | -0.0324324 | 0.240589 | 0.127887 | 0.477778 | 0.790781 | 0.191233 |
| tossup_correctness | category | History | 1440 | 0.707276 | 0.592839 | 0.174043 | 0.202919 | 0.677778 | 0.754167 | -0.0763889 | 0.221169 | 0.268678 | 0.607718 | 0.869991 | 0.193743 |
| tossup_correctness | category | Literature | 1422 | 0.67804 | 0.557048 | 0.185477 | 0.187227 | 0.724332 | 0.814346 | -0.0900141 | 0.203389 | 0.336668 | 0.660273 | 0.878107 | 0.192026 |
| tossup_correctness | category | Mythology | 318 | 0.676756 | 0.568559 | 0.184366 | 0.191982 | 0.710692 | 0.789308 | -0.0786164 | 0.20675 | 0.326692 | 0.64998 | 0.87053 | 0.193575 |
| tossup_correctness | category | Other Academic | 66 | 0.818589 | 0.548064 | 0.195218 | 0.17952 | 0.787879 | 0.712121 | 0.0757576 | 0.204857 | 0.23729 | 0.59726 | 0.821982 | 0.204934 |
| tossup_correctness | category | Philosophy | 311 | 0.721519 | 0.57783 | 0.16082 | 0.197352 | 0.694534 | 0.745981 | -0.0514469 | 0.212659 | 0.279568 | 0.597977 | 0.861333 | 0.197524 |
| tossup_correctness | category | Popular Culture | 102 | 0.547222 | 0.507633 | 0.224086 | 0.162966 | 0.833333 | 0.882353 | -0.0490196 | 0.151099 | 0.471284 | 0.702518 | 0.829158 | 0.197316 |
| tossup_correctness | category | Religion | 358 | 0.721188 | 0.634965 | 0.192605 | 0.219603 | 0.667598 | 0.712291 | -0.0446927 | 0.217012 | 0.230227 | 0.542721 | 0.804658 | 0.202516 |
| tossup_correctness | category | Science | 1433 | 0.694931 | 0.612966 | 0.175753 | 0.212569 | 0.669923 | 0.738311 | -0.068388 | 0.219402 | 0.251646 | 0.574494 | 0.845202 | 0.197949 |
| tossup_correctness | category | Social Science | 324 | 0.782773 | 0.57642 | 0.191687 | 0.194895 | 0.712963 | 0.731481 | -0.0185185 | 0.216195 | 0.23105 | 0.563031 | 0.812594 | 0.201676 |
| tossup_correctness | category | Unknown | 1937 | 0.685716 | 0.613146 | 0.186209 | 0.210928 | 0.668043 | 0.758389 | -0.0903459 | 0.211984 | 0.270256 | 0.595327 | 0.842562 | 0.199791 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.62605 | 0.685388 | 0.191957 | 0.238988 | 0.652695 | 0.712575 | -0.0598802 | 0.212583 | 0.26991 | 0.575717 | 0.818933 | 0.202443 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.722511 | 0.613471 | 0.182481 | 0.212204 | 0.671053 | 0.729167 | -0.058114 | 0.228131 | 0.221662 | 0.564894 | 0.83737 | 0.195777 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.709779 | 0.582202 | 0.164696 | 0.197846 | 0.699291 | 0.755083 | -0.055792 | 0.213192 | 0.277693 | 0.612206 | 0.859571 | 0.196379 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.691892 | 0.578956 | 0.184728 | 0.197003 | 0.694444 | 0.780942 | -0.0864979 | 0.205977 | 0.303313 | 0.622639 | 0.856035 | 0.197694 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.720315 | 0.60223 | 0.197328 | 0.206672 | 0.682488 | 0.762029 | -0.0795417 | 0.226123 | 0.23675 | 0.58047 | 0.854368 | 0.194682 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 2.67678 | 0.796134 | 0.373971 | 1.4281 | 2.09706 | 2.68127 | 3.22038 | 4.02967 | 4.74772 |
| player | theta_1 | 1167 | -1.25669 | 0.954456 | -4.00558 | -2.76904 | -1.87233 | -1.32363 | -0.702534 | 0.409462 | 1.9691 |
| player | theta_2 | 1167 | -1.05827 | 0.793003 | -3.82362 | -2.35814 | -1.53539 | -1.08757 | -0.577399 | 0.249697 | 1.91619 |
| player | theta_3 | 1167 | -1.08311 | 0.836467 | -3.4751 | -2.41731 | -1.62293 | -1.11729 | -0.575734 | 0.41294 | 2.07569 |
| player | theta_norm | 1167 | 2.35301 | 0.757471 | 0.364039 | 1.1808 | 1.82069 | 2.31011 | 2.86983 | 3.70233 | 4.82171 |
| tossup | start_difficulty_d1 | 1220 | -0.751727 | 0.68134 | -3.14855 | -1.77956 | -1.1758 | -0.777117 | -0.358858 | 0.30271 | 2.38861 |
| tossup | start_difficulty_d2 | 1220 | -0.733832 | 0.624084 | -3.10028 | -1.71968 | -1.10462 | -0.750796 | -0.383143 | 0.327525 | 1.57704 |
| tossup | start_difficulty_d3 | 1220 | -0.729869 | 0.61263 | -3.3474 | -1.73119 | -1.12433 | -0.727517 | -0.367433 | 0.305406 | 1.33518 |
| tossup | end_difficulty_d1 | 1220 | -1.75667 | 0.796124 | -4.85599 | -3.01125 | -2.22762 | -1.75606 | -1.30517 | -0.497383 | 1.7327 |
| tossup | end_difficulty_d2 | 1220 | -1.72807 | 0.731605 | -4.82742 | -2.93308 | -2.147 | -1.73016 | -1.29995 | -0.506558 | 0.833955 |
| tossup | end_difficulty_d3 | 1220 | -1.71738 | 0.718921 | -4.84906 | -2.8933 | -2.15764 | -1.70165 | -1.2919 | -0.513692 | 0.638702 |
| tossup | total_drop_d1 | 1220 | 1.00495 | 0.204146 | 0.580596 | 0.74948 | 0.898279 | 0.987331 | 1.07543 | 1.28977 | 3.05826 |
| tossup | total_drop_d2 | 1220 | 0.994237 | 0.166968 | 0.596292 | 0.779548 | 0.900678 | 0.983164 | 1.05702 | 1.23885 | 3.05718 |
| tossup | total_drop_d3 | 1220 | 0.987506 | 0.142859 | 0.593314 | 0.777438 | 0.895144 | 0.976021 | 1.05959 | 1.23765 | 1.8316 |
| tossup | drop_share_1_d1 | 1220 | 0.300981 | 0.0240732 | 0.10789 | 0.262262 | 0.290661 | 0.302324 | 0.315687 | 0.332915 | 0.383187 |
| tossup | drop_share_2_d1 | 1220 | 0.347169 | 0.0140715 | 0.23457 | 0.325526 | 0.338955 | 0.34715 | 0.355581 | 0.368946 | 0.426148 |
| tossup | drop_share_3_d1 | 1220 | 0.35185 | 0.0263474 | 0.274648 | 0.316884 | 0.337057 | 0.350315 | 0.363336 | 0.393396 | 0.657539 |
| tossup | drop_share_1_d2 | 1220 | 0.301271 | 0.0201948 | 0.126445 | 0.268848 | 0.290938 | 0.302434 | 0.312954 | 0.33163 | 0.374564 |
| tossup | drop_share_2_d2 | 1220 | 0.346908 | 0.0134903 | 0.298242 | 0.325374 | 0.338546 | 0.346718 | 0.355135 | 0.367939 | 0.447571 |
| tossup | drop_share_3_d2 | 1220 | 0.351821 | 0.0215304 | 0.268582 | 0.321427 | 0.33868 | 0.351074 | 0.362249 | 0.384867 | 0.575313 |
| tossup | drop_share_1_d3 | 1220 | 0.301461 | 0.0196396 | 0.197331 | 0.269797 | 0.290465 | 0.302481 | 0.313077 | 0.331704 | 0.387643 |
| tossup | drop_share_2_d3 | 1220 | 0.346962 | 0.0125002 | 0.295396 | 0.32738 | 0.338979 | 0.346896 | 0.3549 | 0.368176 | 0.395398 |
| tossup | drop_share_3_d3 | 1220 | 0.351577 | 0.0213694 | 0.27874 | 0.320822 | 0.338748 | 0.350188 | 0.362147 | 0.387799 | 0.504213 |
| tossup | r_1 | 1220 | 0.351691 | 0.228217 | 0.037693 | 0.0747442 | 0.152134 | 0.293538 | 0.521608 | 0.764504 | 0.895683 |
| tossup | r_2 | 1220 | 0.325397 | 0.203353 | 0.040373 | 0.0827128 | 0.156978 | 0.278716 | 0.444558 | 0.741273 | 0.903274 |
| tossup | r_3 | 1220 | 0.322912 | 0.202913 | 0.0484807 | 0.0863603 | 0.158383 | 0.264595 | 0.449871 | 0.733523 | 0.906323 |
| tossup | r_norm | 1220 | 0.680045 | 0.0767101 | 0.57737 | 0.585524 | 0.617308 | 0.661141 | 0.732571 | 0.827515 | 0.908743 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 4.49549 | 0.4931 | 1.79468 | 3.78467 | 4.20559 | 4.45055 | 4.74504 | 5.40462 | 6.39558 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 4.43995 | 0.440905 | 1.93539 | 3.72799 | 4.20887 | 4.41368 | 4.65873 | 5.16794 | 6.6114 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 4.43911 | 0.424557 | 2.1594 | 3.77055 | 4.21507 | 4.42985 | 4.66375 | 5.16688 | 5.97522 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | 1.67699 | 2.35485 | -11.1845 | -3.32052 | 0.536651 | 2.80665 | 3.29027 | 3.65097 | 4.41029 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | 2.16503 | 2.11046 | -8.93051 | -2.48997 | 2.03579 | 3.08939 | 3.35548 | 3.70407 | 4.11213 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | 2.21739 | 2.21662 | -9.37467 | -2.89824 | 2.38347 | 3.15082 | 3.39855 | 3.72786 | 4.4282 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 2.8185 | 2.52723 | 0.908129 | 0.981994 | 1.06304 | 1.38401 | 4.15758 | 8.10993 | 16.0892 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 2.27492 | 2.26423 | 0.896254 | 0.962835 | 1.02215 | 1.18953 | 2.15918 | 7.41863 | 13.5703 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 2.22172 | 2.32333 | 0.867161 | 0.966972 | 1.02412 | 1.15201 | 1.8571 | 7.71986 | 13.9162 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.232588 | 0.0808554 | 0.0427959 | 0.0801065 | 0.169876 | 0.266223 | 0.293883 | 0.314695 | 0.542705 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.342017 | 0.0766438 | 0.056659 | 0.17186 | 0.335797 | 0.351592 | 0.366344 | 0.44089 | 0.664926 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.425395 | 0.131807 | 0.117988 | 0.309573 | 0.348597 | 0.371613 | 0.452135 | 0.734104 | 0.900545 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.250557 | 0.071514 | 0.0307816 | 0.0904609 | 0.228914 | 0.278667 | 0.29571 | 0.313877 | 0.528765 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.347596 | 0.0650032 | 0.0682333 | 0.220792 | 0.339904 | 0.351233 | 0.364316 | 0.425363 | 0.702631 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.401847 | 0.110585 | 0.0934392 | 0.313647 | 0.349904 | 0.364718 | 0.398594 | 0.67011 | 0.884045 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.254245 | 0.0683418 | 0.0383255 | 0.0916201 | 0.240302 | 0.279247 | 0.296503 | 0.314408 | 0.570027 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.350724 | 0.0570965 | 0.0838696 | 0.257183 | 0.340728 | 0.351365 | 0.36388 | 0.419647 | 0.694922 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.39503 | 0.0995735 | 0.0729873 | 0.321102 | 0.349252 | 0.366123 | 0.396952 | 0.639968 | 0.869671 |
| tossup_hazard | hazard_r_1 | 1220 | 0.395459 | 0.275424 | 0.0288074 | 0.0578246 | 0.140577 | 0.327522 | 0.634605 | 0.872054 | 0.942488 |
| tossup_hazard | hazard_r_2 | 1220 | 0.305742 | 0.220312 | 0.0240737 | 0.052242 | 0.116405 | 0.240842 | 0.473748 | 0.723849 | 0.86073 |
| tossup_hazard | hazard_r_3 | 1220 | 0.298799 | 0.219666 | 0.0271178 | 0.0537171 | 0.124308 | 0.221752 | 0.446823 | 0.740235 | 0.916098 |
