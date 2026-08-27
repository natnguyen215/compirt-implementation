# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-logit/unconstrained/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-logit/unconstrained/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 335020 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.548516 |
| log_loss | 0.594461 |
| ece | 0.100641 |
| brier | 0.185733 |
| accuracy | 0.773679 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.000323625 |
| probability_std | 0.0921651 |
| probability_p10 | 0.743276 |
| probability_p50 | 0.892975 |
| probability_p90 | 0.95256 |
| mean_predictive_variance | 0.107189 |
| integrated_brier_score | 0.174394 |
| joint_tossup_event_log_loss | 7.78902 |
| buzz_position_mae | 0.340424 |
| buzz_position_median_absolute_error | 0.343535 |
| buzz_position_bias | -0.328039 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.354153 |
| first_buzzer_mean_reciprocal_rank | 0.565077 |
| first_buzzer_log_loss | 1.67743 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.548516 |
| neg_average_precision | 0.271099 |
| neg_precision | 0.533333 |
| neg_recall | 0.0114231 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0284576 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.238101 |
| no_buzz_calibration_error | 0.226374 |
| no_buzz_brier | 0.0736556 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.548516 | 0.594461 | 0.100641 | 0.185733 | 0.773679 | 0.773355 | 0.000323625 | 0.0921651 | 0.743276 | 0.892975 | 0.95256 | 0.107189 |
| tossup_correctness | tier | fall | 2876 | 0.534589 | 0.554363 | 0.0935168 | 0.172119 | 0.793115 | 0.793115 | 0 | 0.0755234 | 0.774194 | 0.889882 | 0.94665 | 0.106678 |
| tossup_correctness | tier | nationals | 1579 | 0.571443 | 0.654171 | 0.117152 | 0.210109 | 0.730209 | 0.729576 | 0.000633312 | 0.115495 | 0.65875 | 0.872366 | 0.954615 | 0.120617 |
| tossup_correctness | tier | regionals | 1990 | 0.53182 | 0.613936 | 0.107632 | 0.192074 | 0.766332 | 0.765829 | 0.000502513 | 0.107775 | 0.688038 | 0.883808 | 0.955542 | 0.116389 |
| tossup_correctness | tier | winter | 2825 | 0.55217 | 0.58819 | 0.109028 | 0.1815 | 0.783363 | 0.783009 | 0.000353982 | 0.07309 | 0.79562 | 0.908076 | 0.954895 | 0.0937227 |
| tossup_correctness | category | Current Events | 123 | 0.578136 | 0.583559 | 0.105167 | 0.188138 | 0.756098 | 0.764228 | -0.00813008 | 0.107904 | 0.716756 | 0.881947 | 0.944996 | 0.120968 |
| tossup_correctness | category | Fine Arts | 1093 | 0.54845 | 0.614956 | 0.129833 | 0.190734 | 0.771272 | 0.769442 | 0.00182983 | 0.0768105 | 0.786145 | 0.905803 | 0.957219 | 0.095703 |
| tossup_correctness | category | Geography | 191 | 0.646379 | 0.67724 | 0.16773 | 0.226043 | 0.685864 | 0.691099 | -0.0052356 | 0.0951999 | 0.726643 | 0.87884 | 0.943606 | 0.116675 |
| tossup_correctness | category | History | 1469 | 0.552641 | 0.611081 | 0.106086 | 0.193875 | 0.7597 | 0.758339 | 0.00136147 | 0.0920262 | 0.712408 | 0.87952 | 0.946301 | 0.115512 |
| tossup_correctness | category | Literature | 1436 | 0.532478 | 0.526028 | 0.0801582 | 0.157623 | 0.814763 | 0.81546 | -0.000696379 | 0.0790024 | 0.786602 | 0.908358 | 0.958278 | 0.0942852 |
| tossup_correctness | category | Mythology | 325 | 0.566767 | 0.454061 | 0.059613 | 0.136337 | 0.84 | 0.843077 | -0.00307692 | 0.0777546 | 0.80491 | 0.909589 | 0.950316 | 0.0956717 |
| tossup_correctness | category | Other Academic | 67 | 0.533693 | 0.551695 | 0.133047 | 0.170934 | 0.80597 | 0.791045 | 0.0149254 | 0.0847146 | 0.794613 | 0.886156 | 0.944346 | 0.107123 |
| tossup_correctness | category | Philosophy | 322 | 0.4998 | 0.609823 | 0.127087 | 0.185284 | 0.78882 | 0.785714 | 0.00310559 | 0.0819867 | 0.783535 | 0.91844 | 0.95584 | 0.0925273 |
| tossup_correctness | category | Popular Culture | 100 | 0.533197 | 0.367027 | 0.034444 | 0.103306 | 0.89 | 0.89 | 0 | 0.0762124 | 0.792576 | 0.89266 | 0.941961 | 0.106058 |
| tossup_correctness | category | Religion | 365 | 0.555768 | 0.700317 | 0.157166 | 0.22225 | 0.726027 | 0.723288 | 0.00273973 | 0.0895865 | 0.77111 | 0.903451 | 0.951619 | 0.0985366 |
| tossup_correctness | category | Science | 1456 | 0.555515 | 0.591019 | 0.0965438 | 0.187692 | 0.766484 | 0.76717 | -0.000686813 | 0.0884501 | 0.753177 | 0.882146 | 0.945183 | 0.11295 |
| tossup_correctness | category | Social Science | 333 | 0.537952 | 0.687238 | 0.149686 | 0.220489 | 0.72973 | 0.72973 | 0 | 0.0925216 | 0.751547 | 0.890765 | 0.945407 | 0.108373 |
| tossup_correctness | category | Unknown | 1990 | 0.53182 | 0.613936 | 0.107632 | 0.192074 | 0.766332 | 0.765829 | 0.000502513 | 0.107775 | 0.688038 | 0.883808 | 0.955542 | 0.116389 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.544942 | 0.59311 | 0.0920792 | 0.188868 | 0.765363 | 0.748603 | 0.0167598 | 0.09365 | 0.730711 | 0.855178 | 0.924438 | 0.131254 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.473725 | 0.637432 | 0.109938 | 0.201983 | 0.750261 | 0.754441 | -0.00417973 | 0.0962041 | 0.713285 | 0.865541 | 0.934068 | 0.123686 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.541874 | 0.596133 | 0.0990933 | 0.189901 | 0.765774 | 0.766682 | -0.000907853 | 0.0885812 | 0.744442 | 0.879715 | 0.943252 | 0.114893 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.569699 | 0.557802 | 0.086616 | 0.173484 | 0.78912 | 0.787441 | 0.00167898 | 0.0902429 | 0.745363 | 0.89511 | 0.951754 | 0.105263 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.553207 | 0.616339 | 0.116088 | 0.189518 | 0.772096 | 0.771758 | 0.000338639 | 0.092308 | 0.750893 | 0.90983 | 0.960667 | 0.09658 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1196 | -1.42723 | 0.653044 | -2.99908 | -2.33348 | -1.81312 | -1.48453 | -1.12178 | -0.3759 | 2.06091 |
| player | beta | 1196 | -3.19128 | 1.03996 | -6.76874 | -5.27167 | -3.74809 | -2.94475 | -2.41673 | -1.91503 | -1.5821 |
| player | theta_1 | 1196 | 0.905042 | 0.891009 | -2.45726 | -0.695001 | 0.360497 | 1.00305 | 1.55901 | 2.18459 | 3.30981 |
| player | theta_2 | 1196 | 0.888237 | 0.928479 | -2.3462 | -0.746191 | 0.286295 | 1.00017 | 1.55841 | 2.24869 | 3.51471 |
| player | theta_3 | 1196 | 0.894056 | 0.869025 | -2.33337 | -0.725227 | 0.389058 | 1.01893 | 1.51285 | 2.13594 | 3.20393 |
| player | theta_norm | 1196 | 2.09665 | 0.648811 | 0.217462 | 0.953696 | 1.65703 | 2.14171 | 2.56699 | 3.07233 | 4.26252 |
| tossup | start_difficulty_d1 | 1240 | -1.00903 | 0.458685 | -2.22435 | -1.80423 | -1.3866 | -0.954714 | -0.609715 | -0.363888 | -0.0812157 |
| tossup | start_difficulty_d2 | 1240 | -0.977173 | 0.445319 | -2.12029 | -1.7086 | -1.33718 | -0.953682 | -0.59243 | -0.333298 | -0.153305 |
| tossup | start_difficulty_d3 | 1240 | -0.967031 | 0.46539 | -2.13646 | -1.78998 | -1.31871 | -0.912268 | -0.575083 | -0.328921 | -0.108457 |
| tossup | end_difficulty_d1 | 1240 | -1.65966 | 0.356384 | -2.68257 | -2.28113 | -1.91315 | -1.63014 | -1.37676 | -1.13823 | -0.895316 |
| tossup | end_difficulty_d2 | 1240 | -1.64427 | 0.366519 | -2.73069 | -2.27623 | -1.91186 | -1.61881 | -1.34041 | -1.12268 | -0.968169 |
| tossup | end_difficulty_d3 | 1240 | -1.64308 | 0.407107 | -3.1701 | -2.44245 | -1.88989 | -1.56871 | -1.31977 | -1.11739 | -0.904271 |
| tossup | total_drop_d1 | 1240 | 0.650629 | 0.201198 | 0.221983 | 0.301082 | 0.484868 | 0.687696 | 0.815472 | 0.930018 | 1.1296 |
| tossup | total_drop_d2 | 1240 | 0.6671 | 0.177284 | 0.243257 | 0.334413 | 0.545304 | 0.703798 | 0.803129 | 0.909487 | 1.09504 |
| tossup | total_drop_d3 | 1240 | 0.676048 | 0.163649 | 0.261971 | 0.369304 | 0.564548 | 0.706143 | 0.796294 | 0.906438 | 1.1234 |
| tossup | drop_share_1_d1 | 1240 | 0.327113 | 0.0294561 | 0.194257 | 0.284933 | 0.310299 | 0.323773 | 0.3412 | 0.379059 | 0.463912 |
| tossup | drop_share_2_d1 | 1240 | 0.321244 | 0.0185727 | 0.256711 | 0.28699 | 0.308541 | 0.324712 | 0.335462 | 0.346696 | 0.366966 |
| tossup | drop_share_3_d1 | 1240 | 0.351643 | 0.0309285 | 0.243795 | 0.306848 | 0.333647 | 0.347817 | 0.366914 | 0.407771 | 0.531421 |
| tossup | drop_share_1_d2 | 1240 | 0.322102 | 0.0250069 | 0.2125 | 0.279904 | 0.309378 | 0.322677 | 0.336048 | 0.361489 | 0.44351 |
| tossup | drop_share_2_d2 | 1240 | 0.322595 | 0.0186234 | 0.250542 | 0.286217 | 0.313406 | 0.325673 | 0.33537 | 0.346273 | 0.367068 |
| tossup | drop_share_3_d2 | 1240 | 0.355303 | 0.0323418 | 0.255125 | 0.31676 | 0.334759 | 0.34912 | 0.368423 | 0.419302 | 0.521185 |
| tossup | drop_share_1_d3 | 1240 | 0.323605 | 0.0268255 | 0.197033 | 0.280551 | 0.309824 | 0.322362 | 0.337348 | 0.365593 | 0.427476 |
| tossup | drop_share_2_d3 | 1240 | 0.323669 | 0.0169561 | 0.258383 | 0.29064 | 0.314831 | 0.326751 | 0.335711 | 0.345317 | 0.36603 |
| tossup | drop_share_3_d3 | 1240 | 0.352725 | 0.0327695 | 0.245736 | 0.309911 | 0.333474 | 0.347655 | 0.364526 | 0.415488 | 0.509583 |
| tossup | r_1 | 1240 | 0.345604 | 0.253248 | 0.0319646 | 0.0739795 | 0.131746 | 0.248272 | 0.545148 | 0.829114 | 0.90729 |
| tossup | r_2 | 1240 | 0.336944 | 0.251851 | 0.0346866 | 0.0679654 | 0.12263 | 0.242041 | 0.552034 | 0.815509 | 0.923116 |
| tossup | r_3 | 1240 | 0.317452 | 0.232117 | 0.0330869 | 0.0644103 | 0.124398 | 0.234198 | 0.48764 | 0.776352 | 0.892245 |
| tossup | r_norm | 1240 | 0.712379 | 0.0869936 | 0.577415 | 0.59216 | 0.636472 | 0.700657 | 0.782229 | 0.860222 | 0.924761 |
