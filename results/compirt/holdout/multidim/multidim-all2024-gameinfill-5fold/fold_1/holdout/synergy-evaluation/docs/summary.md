# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold/fold_1/holdout/synergy-evaluation`
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
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.511782 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.895033 |
| log_loss | 0.412246 |
| ece | 0.0296166 |
| brier | 0.131349 |
| part_accuracy | 0.813935 |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.294933 |
| part_accuracy_macro_team | 0.815481 |
| part_accuracy_macro_bonus | 0.81202 |
| probability_std | 0.339824 |
| probability_p10 | 0.0634169 |
| probability_p50 | 0.457856 |
| probability_p90 | 0.947216 |
| mean_predictive_variance | 0.134407 |
| exact_acc | 0.527316 |
| ranked_probability_score | 0.111424 |
| bonus_total_score_log_loss | 0.983064 |
| ppb_mae | 1.96012 |
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
| match_winner_accuracy | 0.768559 |
| match_winner_brier | 0.157402 |
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
| bonus_part_correctness | aggregate | all | 25260 | 0.895033 | 0.412246 | 0.0296166 | 0.131349 | 0.813935 | 0.519002 | 0.294933 | 0.339824 | 0.0634169 | 0.457856 | 0.947216 | 0.134407 |
| bonus_part_correctness | tier | fall | 8160 | 0.891301 | 0.409255 | 0.0355042 | 0.130852 | 0.811029 | 0.608701 | 0.202328 | 0.328929 | 0.102921 | 0.619893 | 0.955657 | 0.136448 |
| bonus_part_correctness | tier | nationals | 4107 | 0.889608 | 0.419599 | 0.0453178 | 0.133418 | 0.811298 | 0.411493 | 0.399805 | 0.314889 | 0.0442792 | 0.254716 | 0.86924 | 0.133834 |
| bonus_part_correctness | tier | regionals | 5280 | 0.892078 | 0.417029 | 0.0289808 | 0.132726 | 0.81572 | 0.48125 | 0.33447 | 0.335573 | 0.0562907 | 0.393085 | 0.943008 | 0.135113 |
| bonus_part_correctness | tier | winter | 7713 | 0.895278 | 0.408222 | 0.0228992 | 0.129832 | 0.817192 | 0.507196 | 0.309996 | 0.34326 | 0.0623764 | 0.453461 | 0.950837 | 0.132071 |
| bonus_part_correctness | category | Current Events | 249 | 0.901537 | 0.40074 | 0.0539571 | 0.125518 | 0.835341 | 0.514056 | 0.321285 | 0.34843 | 0.0639567 | 0.439956 | 0.950266 | 0.128178 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.875382 | 0.446089 | 0.0336933 | 0.144399 | 0.793456 | 0.507157 | 0.286299 | 0.333403 | 0.065371 | 0.425364 | 0.937854 | 0.138152 |
| bonus_part_correctness | category | Geography | 459 | 0.890241 | 0.41503 | 0.0542859 | 0.133529 | 0.810458 | 0.618736 | 0.191721 | 0.331137 | 0.0858002 | 0.635505 | 0.953297 | 0.136194 |
| bonus_part_correctness | category | History | 4017 | 0.898144 | 0.404488 | 0.0287313 | 0.128738 | 0.817028 | 0.552153 | 0.264874 | 0.341108 | 0.0693859 | 0.541804 | 0.948575 | 0.133073 |
| bonus_part_correctness | category | Literature | 4047 | 0.901118 | 0.400072 | 0.0229942 | 0.125737 | 0.826044 | 0.50556 | 0.320484 | 0.340631 | 0.0648922 | 0.439828 | 0.948343 | 0.133758 |
| bonus_part_correctness | category | Mythology | 924 | 0.871543 | 0.438301 | 0.0382462 | 0.143005 | 0.786797 | 0.619048 | 0.167749 | 0.320364 | 0.109512 | 0.644481 | 0.960034 | 0.140327 |
| bonus_part_correctness | category | Other Academic | 237 | 0.916631 | 0.369701 | 0.0484506 | 0.113593 | 0.835443 | 0.481013 | 0.35443 | 0.356311 | 0.0457705 | 0.448129 | 0.965583 | 0.12281 |
| bonus_part_correctness | category | Philosophy | 948 | 0.897801 | 0.408525 | 0.0479987 | 0.130145 | 0.816456 | 0.494726 | 0.32173 | 0.330604 | 0.0595382 | 0.403042 | 0.937192 | 0.139166 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.880208 | 0.423979 | 0.0961906 | 0.14036 | 0.789116 | 0.673469 | 0.115646 | 0.315424 | 0.104431 | 0.617183 | 0.956504 | 0.143289 |
| bonus_part_correctness | category | Religion | 984 | 0.900258 | 0.405181 | 0.0430881 | 0.128871 | 0.807927 | 0.513211 | 0.294715 | 0.347519 | 0.054586 | 0.445926 | 0.947614 | 0.128976 |
| bonus_part_correctness | category | Science | 3990 | 0.896748 | 0.408813 | 0.0303579 | 0.1303 | 0.812782 | 0.52807 | 0.284712 | 0.340419 | 0.0663913 | 0.472719 | 0.948425 | 0.134115 |
| bonus_part_correctness | category | Social Science | 897 | 0.916068 | 0.372356 | 0.0447991 | 0.116474 | 0.837235 | 0.490524 | 0.346711 | 0.351321 | 0.0483217 | 0.367887 | 0.948534 | 0.124011 |
| bonus_part_correctness | category | Unknown | 5280 | 0.892078 | 0.417029 | 0.0289808 | 0.132726 | 0.81572 | 0.48125 | 0.33447 | 0.335573 | 0.0562907 | 0.393085 | 0.943008 | 0.135113 |

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
