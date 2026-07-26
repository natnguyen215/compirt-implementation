# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold/fold_1/holdout/evaluation`
Result root: `results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold/fold_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 299008 |
| pyramidal | calibrate_correctness | False |
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.130757 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.886937 |
| log_loss | 0.424365 |
| ece | 0.0171191 |
| brier | 0.13514 |
| part_accuracy | 0.807601 |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.288599 |
| part_accuracy_macro_team | 0.811346 |
| part_accuracy_macro_bonus | 0.80443 |
| probability_std | 0.326577 |
| probability_p10 | 0.0855848 |
| probability_p50 | 0.472889 |
| probability_p90 | 0.930805 |
| mean_predictive_variance | 0.143341 |
| exact_acc | 0.516033 |
| ranked_probability_score | 0.115895 |
| bonus_total_score_log_loss | 1.01453 |
| ppb_mae | 2.37596 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.62571 |
| log_loss | 0.824752 |
| ece | 0.219196 |
| brier | 0.262063 |
| accuracy | 0.623667 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.138458 |
| probability_std | 0.295596 |
| probability_p10 | 0.104138 |
| probability_p50 | 0.621281 |
| probability_p90 | 0.915539 |
| mean_predictive_variance | 0.158709 |
| integrated_brier_score | 0.0952366 |
| joint_tossup_event_log_loss | 6.80028 |
| buzz_position_mae | 0.145832 |
| buzz_position_median_absolute_error | 0.124799 |
| buzz_position_bias | -0.0444516 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.388981 |
| first_buzzer_mean_reciprocal_rank | 0.5956 |
| first_buzzer_log_loss | 1.63493 |
| first_buzzer_events | 9093 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.755459 |
| match_winner_brier | 0.160192 |
| match_games | 458 |
| match_simulations_per_game | 500 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.62571 | 0.824752 | 0.219196 | 0.262063 | 0.623667 | 0.762125 | -0.138458 | 0.295596 | 0.104138 | 0.621281 | 0.915539 | 0.158709 |
| tossup_correctness | tier | fall | 2842 | 0.634413 | 0.800585 | 0.223092 | 0.253613 | 0.63582 | 0.785362 | -0.149543 | 0.289079 | 0.126686 | 0.636549 | 0.906792 | 0.161689 |
| tossup_correctness | tier | nationals | 1564 | 0.607602 | 0.792163 | 0.195418 | 0.260967 | 0.616368 | 0.718031 | -0.101662 | 0.293157 | 0.117104 | 0.653062 | 0.927914 | 0.156011 |
| tossup_correctness | tier | regionals | 1937 | 0.629286 | 0.799011 | 0.208392 | 0.255233 | 0.632938 | 0.758389 | -0.125452 | 0.298031 | 0.103721 | 0.650762 | 0.924678 | 0.154952 |
| tossup_correctness | tier | winter | 2750 | 0.631682 | 0.886394 | 0.246845 | 0.276229 | 0.608727 | 0.765818 | -0.157091 | 0.298906 | 0.079891 | 0.567718 | 0.907836 | 0.159809 |
| tossup_correctness | category | Current Events | 126 | 0.561678 | 1.06723 | 0.316818 | 0.323889 | 0.52381 | 0.769841 | -0.246032 | 0.284712 | 0.0622602 | 0.509861 | 0.854257 | 0.168092 |
| tossup_correctness | category | Fine Arts | 1071 | 0.629734 | 0.857282 | 0.243028 | 0.273006 | 0.611578 | 0.766573 | -0.154995 | 0.301092 | 0.0775402 | 0.588967 | 0.912488 | 0.157768 |
| tossup_correctness | category | Geography | 185 | 0.625692 | 0.888883 | 0.244004 | 0.29594 | 0.578378 | 0.697297 | -0.118919 | 0.280781 | 0.0711804 | 0.451853 | 0.832922 | 0.169446 |
| tossup_correctness | category | History | 1440 | 0.622616 | 0.79732 | 0.213543 | 0.257529 | 0.634722 | 0.754167 | -0.119444 | 0.292266 | 0.113792 | 0.639413 | 0.917939 | 0.159434 |
| tossup_correctness | category | Literature | 1422 | 0.610084 | 0.828703 | 0.228826 | 0.253449 | 0.640647 | 0.814346 | -0.173699 | 0.299435 | 0.125499 | 0.682095 | 0.936303 | 0.150697 |
| tossup_correctness | category | Mythology | 318 | 0.602902 | 0.825482 | 0.272848 | 0.274509 | 0.591195 | 0.789308 | -0.198113 | 0.276975 | 0.121434 | 0.588625 | 0.887496 | 0.172007 |
| tossup_correctness | category | Other Academic | 66 | 0.702128 | 0.762023 | 0.221402 | 0.23981 | 0.590909 | 0.712121 | -0.121212 | 0.281858 | 0.034268 | 0.525373 | 0.870219 | 0.170358 |
| tossup_correctness | category | Philosophy | 311 | 0.665757 | 0.827232 | 0.205007 | 0.258306 | 0.62701 | 0.745981 | -0.118971 | 0.305706 | 0.0804444 | 0.609505 | 0.922709 | 0.154059 |
| tossup_correctness | category | Popular Culture | 102 | 0.466667 | 1.1214 | 0.406935 | 0.34659 | 0.5 | 0.882353 | -0.382353 | 0.271237 | 0.0630874 | 0.498734 | 0.791698 | 0.175826 |
| tossup_correctness | category | Religion | 358 | 0.649876 | 0.793317 | 0.179454 | 0.256361 | 0.628492 | 0.712291 | -0.0837989 | 0.2904 | 0.11545 | 0.602583 | 0.900381 | 0.163464 |
| tossup_correctness | category | Science | 1433 | 0.622725 | 0.822897 | 0.210599 | 0.260481 | 0.627355 | 0.738311 | -0.110956 | 0.290376 | 0.119588 | 0.615037 | 0.908362 | 0.161898 |
| tossup_correctness | category | Social Science | 324 | 0.627528 | 0.804017 | 0.23158 | 0.263902 | 0.601852 | 0.731481 | -0.12963 | 0.279227 | 0.108666 | 0.561602 | 0.889405 | 0.170727 |
| tossup_correctness | category | Unknown | 1937 | 0.629286 | 0.799011 | 0.208392 | 0.255233 | 0.632938 | 0.758389 | -0.125452 | 0.298031 | 0.103721 | 0.650762 | 0.924678 | 0.154952 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.643557 | 1.34686 | 0.453617 | 0.427139 | 0.377246 | 0.712575 | -0.335329 | 0.241342 | 0.0127156 | 0.184037 | 0.678391 | 0.135572 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.640571 | 1.19325 | 0.387229 | 0.366082 | 0.479167 | 0.729167 | -0.25 | 0.26842 | 0.0291289 | 0.294344 | 0.758512 | 0.154426 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.645061 | 0.881647 | 0.273322 | 0.285366 | 0.586288 | 0.755083 | -0.168794 | 0.285794 | 0.0776763 | 0.505289 | 0.863396 | 0.16815 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.628457 | 0.749354 | 0.200848 | 0.239838 | 0.654008 | 0.780942 | -0.126934 | 0.278478 | 0.162026 | 0.665069 | 0.919213 | 0.162823 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.622782 | 0.717007 | 0.143843 | 0.226544 | 0.677905 | 0.762029 | -0.0841244 | 0.269529 | 0.219721 | 0.748253 | 0.941529 | 0.150885 |
| bonus_part_correctness | aggregate | all | 25260 | 0.886937 | 0.424365 | 0.0171191 | 0.13514 | 0.807601 | 0.519002 | 0.288599 | 0.326577 | 0.0855848 | 0.472889 | 0.930805 | 0.143341 |
| bonus_part_correctness | tier | fall | 8160 | 0.884438 | 0.422801 | 0.0411483 | 0.135507 | 0.800123 | 0.608701 | 0.191422 | 0.317688 | 0.117305 | 0.601538 | 0.935316 | 0.144511 |
| bonus_part_correctness | tier | nationals | 4107 | 0.873269 | 0.439212 | 0.0217494 | 0.138976 | 0.805698 | 0.411493 | 0.394205 | 0.310302 | 0.0749291 | 0.341594 | 0.88598 | 0.148246 |
| bonus_part_correctness | tier | regionals | 5280 | 0.883969 | 0.427312 | 0.0162643 | 0.136242 | 0.809091 | 0.48125 | 0.327841 | 0.326119 | 0.0821755 | 0.423586 | 0.929192 | 0.143147 |
| bonus_part_correctness | tier | winter | 7713 | 0.890536 | 0.416097 | 0.0219283 | 0.131956 | 0.815506 | 0.507196 | 0.308311 | 0.332116 | 0.0766955 | 0.446795 | 0.935856 | 0.139625 |
| bonus_part_correctness | category | Current Events | 249 | 0.897792 | 0.41237 | 0.0730819 | 0.130024 | 0.823293 | 0.514056 | 0.309237 | 0.336597 | 0.0726649 | 0.417922 | 0.918077 | 0.13619 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.876934 | 0.44197 | 0.023952 | 0.141509 | 0.800613 | 0.507157 | 0.293456 | 0.319384 | 0.0862092 | 0.443852 | 0.921436 | 0.147799 |
| bonus_part_correctness | category | Geography | 459 | 0.88505 | 0.425456 | 0.0758463 | 0.135976 | 0.795207 | 0.618736 | 0.176471 | 0.314884 | 0.108898 | 0.630845 | 0.93118 | 0.146658 |
| bonus_part_correctness | category | History | 4017 | 0.888118 | 0.421894 | 0.0375936 | 0.135128 | 0.798606 | 0.552153 | 0.246453 | 0.326944 | 0.089338 | 0.551467 | 0.93244 | 0.142097 |
| bonus_part_correctness | category | Literature | 4047 | 0.892529 | 0.411888 | 0.0256455 | 0.129182 | 0.822585 | 0.50556 | 0.317025 | 0.327524 | 0.0879907 | 0.451795 | 0.9338 | 0.142727 |
| bonus_part_correctness | category | Mythology | 924 | 0.869283 | 0.443912 | 0.037289 | 0.144112 | 0.778139 | 0.619048 | 0.159091 | 0.300824 | 0.138969 | 0.629041 | 0.932393 | 0.151794 |
| bonus_part_correctness | category | Other Academic | 237 | 0.903937 | 0.396434 | 0.055229 | 0.122918 | 0.827004 | 0.481013 | 0.345992 | 0.345037 | 0.0743221 | 0.518359 | 0.949966 | 0.130722 |
| bonus_part_correctness | category | Philosophy | 948 | 0.87124 | 0.447366 | 0.0498863 | 0.143148 | 0.803797 | 0.494726 | 0.309072 | 0.315863 | 0.0857449 | 0.417236 | 0.917541 | 0.149267 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.893413 | 0.426747 | 0.114644 | 0.139712 | 0.768707 | 0.673469 | 0.0952381 | 0.308699 | 0.118279 | 0.540216 | 0.938883 | 0.15068 |
| bonus_part_correctness | category | Religion | 984 | 0.889832 | 0.422782 | 0.0325488 | 0.134466 | 0.802846 | 0.513211 | 0.289634 | 0.334294 | 0.066622 | 0.448659 | 0.930299 | 0.138172 |
| bonus_part_correctness | category | Science | 3990 | 0.888164 | 0.422558 | 0.023845 | 0.13448 | 0.81203 | 0.52807 | 0.28396 | 0.327412 | 0.0896972 | 0.486712 | 0.93223 | 0.142704 |
| bonus_part_correctness | category | Social Science | 897 | 0.903526 | 0.391494 | 0.0379863 | 0.123456 | 0.823857 | 0.490524 | 0.333333 | 0.340335 | 0.0627672 | 0.386804 | 0.932936 | 0.133001 |
| bonus_part_correctness | category | Unknown | 5280 | 0.883969 | 0.427312 | 0.0162643 | 0.136242 | 0.809091 | 0.48125 | 0.327841 | 0.326119 | 0.0821755 | 0.423586 | 0.929192 | 0.143147 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.886937 | 0.895033 | 0.00809623 | synergy |
| log_loss | 0.424365 | 0.412246 | -0.0121185 | synergy |
| ece | 0.0171191 | 0.0296166 | 0.0124975 | no-synergy |
| brier | 0.13514 | 0.131349 | -0.00379076 | synergy |
| accuracy_lift_over_all_correct | 0.288599 | 0.294933 | 0.00633413 | synergy |
| part_accuracy | 0.807601 | 0.813935 | 0.00633413 | synergy |
| part_accuracy_macro_team | 0.811346 | 0.815481 | 0.0041355 | synergy |
| part_accuracy_macro_bonus | 0.80443 | 0.81202 | 0.00759039 | synergy |
| exact_acc | 0.516033 | 0.527316 | 0.0112827 | synergy |
| ranked_probability_score | 0.115895 | 0.111424 | -0.00447144 | synergy |
| bonus_total_score_log_loss | 1.01453 | 0.983064 | -0.0314695 | synergy |
| ppb_mae | 2.37596 | 1.96012 | -0.415845 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 4.57538 | 1.19537 | 0.942228 | 1.96691 | 4.01629 | 4.81242 | 5.41953 | 6.12458 | 7.08922 |
| player | theta_1 | 1167 | 0.0397435 | 0.734588 | -2.25561 | -1.40422 | -0.370357 | 0.179845 | 0.548504 | 1.03827 | 1.87267 |
| player | theta_2 | 1167 | 0.0767129 | 0.740675 | -2.56475 | -1.44272 | -0.290102 | 0.18154 | 0.575667 | 1.12572 | 1.95869 |
| player | theta_3 | 1167 | 0.0198033 | 0.715639 | -2.5477 | -1.27587 | -0.436423 | 0.0934691 | 0.548394 | 1.07551 | 1.6257 |
| player | theta_4 | 1167 | 0.061582 | 0.736657 | -2.25958 | -1.37025 | -0.33977 | 0.190506 | 0.578008 | 1.08712 | 2.08349 |
| player | theta_5 | 1167 | -0.00557151 | 0.76193 | -2.79139 | -1.47633 | -0.416426 | 0.155657 | 0.538952 | 0.977233 | 1.80937 |
| player | theta_norm | 1167 | 1.53964 | 0.602272 | 0.40605 | 0.730279 | 1.09989 | 1.43997 | 1.88608 | 2.74177 | 3.82381 |
| tossup | beta_1 | 1220 | 0.761323 | 0.520982 | -1.34914 | 0.220025 | 0.395878 | 0.588175 | 0.999242 | 1.85955 | 2.63687 |
| tossup | beta_2 | 1220 | 0.861103 | 0.593281 | -1.04501 | 0.209669 | 0.430159 | 0.660904 | 1.22118 | 2.03631 | 2.90673 |
| tossup | beta_3 | 1220 | 0.733083 | 0.543628 | -2.24679 | 0.185206 | 0.389686 | 0.55339 | 0.88403 | 1.92179 | 3.25063 |
| tossup | beta_4 | 1220 | 0.749787 | 0.523178 | -0.979079 | 0.204085 | 0.412284 | 0.576361 | 0.934957 | 1.89862 | 2.77376 |
| tossup | beta_5 | 1220 | 0.804069 | 0.550193 | -1.14851 | 0.203444 | 0.405229 | 0.624596 | 1.09049 | 1.91565 | 3.1265 |
| tossup | gamma_1 | 1220 | 11.8518 | 58.8273 | 0.535377 | 3.36457 | 4.50691 | 5.15356 | 6.15846 | 26.9598 | 1751.74 |
| tossup | gamma_2 | 1220 | 13.7176 | 85.1313 | 0.567172 | 3.05098 | 4.40572 | 5.09401 | 6.17647 | 21.3719 | 1943.98 |
| tossup | gamma_3 | 1220 | 12.624 | 54.5476 | 0.386695 | 3.36121 | 4.51163 | 5.09326 | 5.8706 | 26.3371 | 1177.17 |
| tossup | gamma_4 | 1220 | 12.0581 | 76.8517 | 0.753421 | 3.20668 | 4.49619 | 5.09868 | 5.94231 | 19.0988 | 1519.04 |
| tossup | gamma_5 | 1220 | 15.2692 | 68.0401 | 0.48676 | 3.0918 | 4.4398 | 5.12688 | 6.51291 | 28.5543 | 1323.79 |
| tossup | mu_1 | 1220 | 0.501968 | 0.104907 | 0.122048 | 0.384064 | 0.445747 | 0.476033 | 0.528555 | 0.722412 | 0.969192 |
| tossup | mu_2 | 1220 | 0.527198 | 0.127213 | 0.183218 | 0.380758 | 0.446717 | 0.487059 | 0.588171 | 0.800284 | 0.987564 |
| tossup | mu_3 | 1220 | 0.501698 | 0.105188 | 0.184576 | 0.395724 | 0.446795 | 0.47494 | 0.519156 | 0.727977 | 0.967001 |
| tossup | mu_4 | 1220 | 0.502667 | 0.107859 | 0.145716 | 0.382488 | 0.447391 | 0.479279 | 0.523791 | 0.738551 | 0.960575 |
| tossup | mu_5 | 1220 | 0.514104 | 0.112777 | 0.156969 | 0.374742 | 0.44745 | 0.486173 | 0.561319 | 0.741685 | 0.984113 |
| tossup | r_1 | 1220 | 1.03084 | 0.770324 | 0.088998 | 0.219083 | 0.43589 | 0.763344 | 1.47366 | 2.59989 | 4.06906 |
| tossup | r_2 | 1220 | 1.41349 | 1.09856 | 0.105359 | 0.24468 | 0.529978 | 1.06873 | 2.14066 | 3.54445 | 6.13056 |
| tossup | r_3 | 1220 | 0.985543 | 0.818814 | 0.106585 | 0.207978 | 0.415851 | 0.706791 | 1.25262 | 2.76878 | 5.46532 |
| tossup | r_4 | 1220 | 1.03254 | 0.853558 | 0.0618371 | 0.224516 | 0.422159 | 0.746138 | 1.34568 | 2.85907 | 5.41896 |
| tossup | r_5 | 1220 | 1.14129 | 0.794687 | 0.0726977 | 0.214198 | 0.481601 | 0.915825 | 1.67751 | 2.65218 | 5.06854 |
| tossup | r_norm | 1220 | 3.0974 | 0.796768 | 1.3864 | 1.95998 | 2.52021 | 3.00359 | 3.55978 | 4.54497 | 6.24081 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
