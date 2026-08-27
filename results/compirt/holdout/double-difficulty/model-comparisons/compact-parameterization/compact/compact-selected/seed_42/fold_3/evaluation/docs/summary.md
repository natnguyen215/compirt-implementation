# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/compact-vs-332/compact/compact-selected/seed_42/fold_3/evaluation`
Result root: `results/compirt/holdout/compact-vs-332/compact/compact-selected/seed_42/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 279708 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.707212 |
| log_loss | 0.507528 |
| ece | 0.0501569 |
| brier | 0.163239 |
| accuracy | 0.772357 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00231278 |
| probability_std | 0.206924 |
| probability_p10 | 0.453378 |
| probability_p50 | 0.833444 |
| probability_p90 | 0.959289 |
| mean_predictive_variance | 0.13692 |
| integrated_brier_score | 0.0943354 |
| joint_tossup_event_log_loss | 6.38117 |
| buzz_position_mae | 0.141222 |
| buzz_position_median_absolute_error | 0.121031 |
| buzz_position_bias | -0.0336811 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.398678 |
| first_buzzer_mean_reciprocal_rank | 0.603896 |
| first_buzzer_log_loss | 1.56512 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.707212 |
| neg_average_precision | 0.434991 |
| neg_precision | 0.509519 |
| neg_recall | 0.269157 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.169633 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.00875126 |
| no_buzz_calibration_error | -0.00643313 |
| no_buzz_brier | 0.0129895 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.707212 | 0.507528 | 0.0501569 | 0.163239 | 0.772357 | 0.770044 | 0.00231278 | 0.206924 | 0.453378 | 0.833444 | 0.959289 | 0.13692 |
| tossup_correctness | tier | fall | 2817 | 0.708256 | 0.489924 | 0.0397907 | 0.155617 | 0.783813 | 0.781683 | 0.00212993 | 0.19268 | 0.496607 | 0.840555 | 0.961361 | 0.134939 |
| tossup_correctness | tier | nationals | 1542 | 0.708887 | 0.552119 | 0.0718623 | 0.18279 | 0.738003 | 0.73476 | 0.00324254 | 0.217706 | 0.422828 | 0.818971 | 0.954688 | 0.14164 |
| tossup_correctness | tier | regionals | 1934 | 0.699611 | 0.525362 | 0.0609093 | 0.169107 | 0.763702 | 0.75698 | 0.00672182 | 0.216394 | 0.426781 | 0.828664 | 0.958374 | 0.137065 |
| tossup_correctness | tier | winter | 2787 | 0.707897 | 0.488273 | 0.0553929 | 0.156054 | 0.785791 | 0.786868 | -0.00107643 | 0.206948 | 0.451351 | 0.836814 | 0.960645 | 0.136209 |
| tossup_correctness | category | Current Events | 125 | 0.7457 | 0.533016 | 0.0624305 | 0.180591 | 0.72 | 0.704 | 0.016 | 0.163327 | 0.535422 | 0.806766 | 0.937819 | 0.156044 |
| tossup_correctness | category | Fine Arts | 1072 | 0.722677 | 0.485197 | 0.0365656 | 0.155466 | 0.778918 | 0.770522 | 0.00839552 | 0.198365 | 0.476793 | 0.84009 | 0.952176 | 0.137907 |
| tossup_correctness | category | Geography | 185 | 0.748531 | 0.526022 | 0.0910864 | 0.175701 | 0.708108 | 0.702703 | 0.00540541 | 0.236855 | 0.32442 | 0.798728 | 0.944683 | 0.152236 |
| tossup_correctness | category | History | 1443 | 0.726139 | 0.49917 | 0.0531523 | 0.163522 | 0.774082 | 0.765073 | 0.00900901 | 0.211899 | 0.418443 | 0.810021 | 0.954581 | 0.143882 |
| tossup_correctness | category | Literature | 1411 | 0.691116 | 0.48103 | 0.0656396 | 0.152059 | 0.790928 | 0.81219 | -0.0212615 | 0.201533 | 0.506819 | 0.876287 | 0.973326 | 0.119912 |
| tossup_correctness | category | Mythology | 320 | 0.674541 | 0.497954 | 0.051943 | 0.15543 | 0.775 | 0.79375 | -0.01875 | 0.147176 | 0.60701 | 0.843662 | 0.961881 | 0.131535 |
| tossup_correctness | category | Other Academic | 64 | 0.613281 | 0.617259 | 0.120165 | 0.203758 | 0.71875 | 0.75 | -0.03125 | 0.137467 | 0.652511 | 0.863178 | 0.953686 | 0.129246 |
| tossup_correctness | category | Philosophy | 312 | 0.718258 | 0.446451 | 0.0510874 | 0.141085 | 0.807692 | 0.801282 | 0.00641026 | 0.164428 | 0.570762 | 0.838589 | 0.954401 | 0.13819 |
| tossup_correctness | category | Popular Culture | 104 | 0.585938 | 0.436361 | 0.0424175 | 0.127796 | 0.846154 | 0.846154 | 0 | 0.0599504 | 0.801799 | 0.895398 | 0.942291 | 0.100754 |
| tossup_correctness | category | Religion | 358 | 0.707535 | 0.537795 | 0.056339 | 0.180497 | 0.73743 | 0.726257 | 0.0111732 | 0.185278 | 0.458397 | 0.758617 | 0.921206 | 0.16611 |
| tossup_correctness | category | Science | 1431 | 0.685888 | 0.533988 | 0.0759518 | 0.171343 | 0.767296 | 0.765199 | 0.00209644 | 0.217156 | 0.432962 | 0.832421 | 0.961708 | 0.136466 |
| tossup_correctness | category | Social Science | 321 | 0.73135 | 0.526481 | 0.0657442 | 0.165125 | 0.781931 | 0.744548 | 0.0373832 | 0.229163 | 0.364619 | 0.799617 | 0.954894 | 0.146778 |
| tossup_correctness | category | Unknown | 1934 | 0.699611 | 0.525362 | 0.0609093 | 0.169107 | 0.763702 | 0.75698 | 0.00672182 | 0.216394 | 0.426781 | 0.828664 | 0.958374 | 0.137065 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.761837 | 0.542075 | 0.0721671 | 0.181331 | 0.734375 | 0.697917 | 0.0364583 | 0.200682 | 0.415812 | 0.794367 | 0.939694 | 0.154345 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.755934 | 0.501864 | 0.0501721 | 0.162825 | 0.770529 | 0.733408 | 0.0371204 | 0.202236 | 0.467045 | 0.845868 | 0.960881 | 0.132952 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.700572 | 0.528082 | 0.0661542 | 0.16838 | 0.766516 | 0.759276 | 0.00723982 | 0.197731 | 0.492198 | 0.857572 | 0.964575 | 0.128008 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.693542 | 0.489707 | 0.0491903 | 0.156182 | 0.788079 | 0.789125 | -0.00104566 | 0.186576 | 0.52126 | 0.847583 | 0.962262 | 0.131349 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.713463 | 0.508933 | 0.0697476 | 0.165218 | 0.764384 | 0.775342 | -0.0109589 | 0.226608 | 0.367179 | 0.78915 | 0.94934 | 0.149199 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 2.03089 | 0.588794 | 0.1728 | 1.06399 | 1.6132 | 2.04169 | 2.42548 | 2.98684 | 3.71826 |
| player | theta_1 | 1133 | -1.37877 | 0.669129 | -3.22059 | -2.4979 | -1.85467 | -1.37837 | -0.914816 | -0.245092 | 0.437006 |
| player | theta_2 | 1133 | -1.31678 | 0.637384 | -3.33765 | -2.30428 | -1.80015 | -1.3581 | -0.839166 | -0.277106 | 0.382414 |
| player | theta_3 | 1133 | -1.28726 | 0.650589 | -3.25482 | -2.33005 | -1.75443 | -1.30628 | -0.82802 | -0.199248 | 0.500797 |
| player | theta_norm | 1133 | 2.48719 | 0.61832 | 0.819351 | 1.49384 | 2.02625 | 2.49793 | 2.9264 | 3.48382 | 4.72949 |
| tossup | start_difficulty | 1240 | -3.22667 | 0.798853 | -5.37453 | -4.54993 | -3.76153 | -3.22805 | -2.67597 | -1.86738 | -0.628116 |
| tossup | end_difficulty | 1240 | -4.25689 | 0.976208 | -7.37368 | -5.89018 | -4.89749 | -4.23097 | -3.5599 | -2.72126 | -1.37187 |
| tossup | total_drop | 1240 | 1.03022 | 0.307878 | 0.591001 | 0.724473 | 0.85114 | 0.969595 | 1.10932 | 1.54274 | 3.44357 |
| tossup | drop_share_1 | 1240 | 0.294272 | 0.0293672 | 0.119853 | 0.243261 | 0.280405 | 0.297566 | 0.312518 | 0.335254 | 0.379989 |
| tossup | drop_share_2 | 1240 | 0.347945 | 0.0171149 | 0.199871 | 0.32303 | 0.337742 | 0.347103 | 0.356581 | 0.376173 | 0.448605 |
| tossup | drop_share_3 | 1240 | 0.357783 | 0.0329071 | 0.270907 | 0.313695 | 0.337739 | 0.354697 | 0.372962 | 0.41033 | 0.680276 |
| tossup | r_1 | 1240 | 0.973169 | 0.763809 | 0.0417125 | 0.130355 | 0.370217 | 0.769532 | 1.3465 | 2.54327 | 3.79554 |
| tossup | r_2 | 1240 | 0.793588 | 0.630034 | 0.040266 | 0.122662 | 0.299421 | 0.598686 | 1.1323 | 2.05018 | 3.07332 |
| tossup | r_3 | 1240 | 0.796184 | 0.687429 | 0.0404058 | 0.113782 | 0.297711 | 0.586474 | 1.05111 | 2.3211 | 3.64997 |
| tossup | r_norm | 1240 | 1.80655 | 0.631801 | 0.369821 | 0.85548 | 1.33213 | 1.76371 | 2.21378 | 2.93471 | 3.84883 |
| tossup_hazard | hazard_start_difficulty | 1240 | 3.78447 | 0.619416 | 1.6654 | 2.78233 | 3.35124 | 3.76932 | 4.23565 | 4.79145 | 5.77544 |
| tossup_hazard | hazard_end_difficulty | 1240 | -1.09928 | 1.51042 | -7.01258 | -3.52787 | -2.07387 | -1.13423 | -0.123905 | 1.59931 | 3.62844 |
| tossup_hazard | hazard_total_drop | 1240 | 4.88375 | 1.49398 | 0.884612 | 2.25545 | 4.00191 | 4.88731 | 5.81214 | 7.3357 | 11.7336 |
| tossup_hazard | hazard_drop_share_1 | 1240 | 0.160476 | 0.0875424 | 0.0358429 | 0.0668532 | 0.0984865 | 0.137201 | 0.197872 | 0.324512 | 0.612073 |
| tossup_hazard | hazard_drop_share_2 | 1240 | 0.315549 | 0.134471 | 0.0538707 | 0.119574 | 0.206286 | 0.305788 | 0.404192 | 0.566361 | 0.738562 |
| tossup_hazard | hazard_drop_share_3 | 1240 | 0.523975 | 0.1863 | 0.0753013 | 0.210397 | 0.378241 | 0.531741 | 0.67952 | 0.802541 | 0.901908 |
