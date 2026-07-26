# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/multidim/multidim-all2024-bounceback-cal/synergy-evaluation`
Result root: `results/compirt/in_sample/multidim/multidim-all2024-bounceback-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 391292 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 64375.6 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.756592 |
| mean_synergy_contribution | 0.0708129 |
| median_synergy_contribution | 0.010204 |
| negative_synergy_fraction | 0.427046 |
| positive_synergy_fraction | 0.541551 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.936291 |
| log_loss | 0.330929 |
| ece | 0.037406 |
| brier | 0.102833 |
| part_accuracy | 0.855726 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.335237 |
| part_accuracy_macro_team | 0.858083 |
| part_accuracy_macro_game | 0.856058 |
| part_accuracy_macro_bonus | 0.860165 |
| probability_std | 0.358731 |
| probability_p10 | 0.0449433 |
| probability_p50 | 0.46241 |
| probability_p90 | 0.966319 |
| mean_predictive_variance | 0.121269 |
| exact_acc | 0.620586 |
| ranked_probability_score | 0.0920475 |
| bonus_total_score_log_loss | 0.828797 |
| ppb_mae | 0.86116 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.663602 |
| log_loss | 0.512191 |
| ece | 0.0114169 |
| brier | 0.167145 |
| accuracy | 0.770526 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | 0.00325583 |
| probability_std | 0.0934659 |
| probability_p10 | 0.645357 |
| probability_p50 | 0.787441 |
| probability_p90 | 0.877345 |
| mean_predictive_variance | 0.16713 |
| integrated_brier_score | 0.0862266 |
| joint_tossup_event_log_loss | 6.01746 |
| buzz_position_mae | 0.130462 |
| buzz_position_median_absolute_error | 0.110282 |
| buzz_position_bias | -0.00629646 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |
| first_buzzer_top1_accuracy | 0.485996 |
| first_buzzer_mean_reciprocal_rank | 0.6741 |
| first_buzzer_log_loss | 1.33989 |
| first_buzzer_events | 47914 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.803238 |
| match_winner_brier | 0.13282 |
| match_games | 2409 |
| match_simulations_per_game | 500 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.663602 | 0.512191 | 0.0114169 | 0.167145 | 0.770526 | 0.767271 | 0.00325583 | 0.0934659 | 0.645357 | 0.787441 | 0.877345 | 0.16713 |
| tossup_correctness | tier | fall | 14760 | 0.684439 | 0.482364 | 0.0264963 | 0.154897 | 0.791125 | 0.787466 | 0.00365854 | 0.0897309 | 0.652239 | 0.787984 | 0.872607 | 0.167545 |
| tossup_correctness | tier | nationals | 7940 | 0.633137 | 0.572932 | 0.0521448 | 0.191848 | 0.728841 | 0.72733 | 0.00151134 | 0.0997314 | 0.640029 | 0.795304 | 0.891992 | 0.162184 |
| tossup_correctness | tier | regionals | 10202 | 0.655768 | 0.523878 | 0.0139978 | 0.171838 | 0.764556 | 0.758969 | 0.00558714 | 0.0970989 | 0.642002 | 0.789486 | 0.881784 | 0.166061 |
| tossup_correctness | tier | winter | 15012 | 0.675015 | 0.501447 | 0.0235072 | 0.162932 | 0.776379 | 0.774181 | 0.00219824 | 0.090843 | 0.644418 | 0.781752 | 0.870953 | 0.170066 |
| tossup_correctness | category | Current Events | 640 | 0.663504 | 0.5501 | 0.028778 | 0.183371 | 0.734375 | 0.734375 | 0 | 0.0918076 | 0.628812 | 0.76154 | 0.854979 | 0.179586 |
| tossup_correctness | category | Fine Arts | 5640 | 0.6633 | 0.512429 | 0.00996907 | 0.167219 | 0.770745 | 0.766489 | 0.00425532 | 0.0950567 | 0.640428 | 0.785777 | 0.878464 | 0.167835 |
| tossup_correctness | category | Geography | 972 | 0.668034 | 0.603658 | 0.0752848 | 0.208938 | 0.680041 | 0.675926 | 0.00411523 | 0.0854401 | 0.62706 | 0.74687 | 0.845731 | 0.185245 |
| tossup_correctness | category | History | 7599 | 0.691196 | 0.506183 | 0.0247385 | 0.16537 | 0.767075 | 0.764969 | 0.00210554 | 0.0900924 | 0.653725 | 0.788655 | 0.874724 | 0.166856 |
| tossup_correctness | category | Literature | 7469 | 0.636401 | 0.467578 | 0.0275937 | 0.147948 | 0.811086 | 0.812157 | -0.00107109 | 0.0966827 | 0.652456 | 0.805673 | 0.887338 | 0.159676 |
| tossup_correctness | category | Mythology | 1692 | 0.660287 | 0.471768 | 0.0600082 | 0.148787 | 0.807329 | 0.80792 | -0.000591017 | 0.0871946 | 0.642725 | 0.767487 | 0.86102 | 0.176243 |
| tossup_correctness | category | Other Academic | 357 | 0.622691 | 0.538485 | 0.040398 | 0.177016 | 0.756303 | 0.756303 | 0 | 0.0901343 | 0.62334 | 0.757416 | 0.851869 | 0.180822 |
| tossup_correctness | category | Philosophy | 1649 | 0.672104 | 0.492607 | 0.0274453 | 0.158697 | 0.790176 | 0.77926 | 0.0109157 | 0.094912 | 0.636317 | 0.786504 | 0.872033 | 0.169187 |
| tossup_correctness | category | Popular Culture | 538 | 0.598144 | 0.427662 | 0.108705 | 0.129102 | 0.864312 | 0.864312 | 0 | 0.0790537 | 0.644359 | 0.760919 | 0.851833 | 0.178416 |
| tossup_correctness | category | Religion | 1889 | 0.690078 | 0.547773 | 0.0353825 | 0.183043 | 0.730016 | 0.724722 | 0.00529381 | 0.0945876 | 0.626533 | 0.773786 | 0.863793 | 0.174774 |
| tossup_correctness | category | Science | 7556 | 0.667362 | 0.528029 | 0.028119 | 0.173881 | 0.757544 | 0.754235 | 0.00330863 | 0.0874986 | 0.659176 | 0.791962 | 0.877354 | 0.164686 |
| tossup_correctness | category | Social Science | 1711 | 0.646793 | 0.567717 | 0.0358571 | 0.189697 | 0.728814 | 0.722385 | 0.00642899 | 0.0914301 | 0.638763 | 0.767818 | 0.87001 | 0.174952 |
| tossup_correctness | category | Unknown | 10202 | 0.655768 | 0.523878 | 0.0139978 | 0.171838 | 0.764556 | 0.758969 | 0.00558714 | 0.0970989 | 0.642002 | 0.789486 | 0.881784 | 0.166061 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.687133 | 0.553595 | 0.0837066 | 0.184468 | 0.755037 | 0.727466 | 0.0275716 | 0.111904 | 0.508567 | 0.666956 | 0.801093 | 0.211719 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.686899 | 0.53857 | 0.0462848 | 0.178713 | 0.748819 | 0.736496 | 0.0123229 | 0.106522 | 0.554359 | 0.709303 | 0.826477 | 0.199776 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.689854 | 0.511788 | 0.0290967 | 0.167748 | 0.764629 | 0.761053 | 0.00357548 | 0.0947397 | 0.618629 | 0.755888 | 0.858255 | 0.18107 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.691278 | 0.483619 | 0.030005 | 0.155684 | 0.787562 | 0.786033 | 0.00152976 | 0.0803065 | 0.672769 | 0.788281 | 0.873336 | 0.165668 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.639725 | 0.529287 | 0.0503062 | 0.17309 | 0.766154 | 0.765769 | 0.000384615 | 0.0684709 | 0.725814 | 0.82471 | 0.895985 | 0.145408 |
| bonus_part_correctness | aggregate | all | 133461 | 0.936291 | 0.330929 | 0.037406 | 0.102833 | 0.855726 | 0.520489 | 0.335237 | 0.358731 | 0.0449433 | 0.46241 | 0.966319 | 0.121269 |
| bonus_part_correctness | tier | fall | 42336 | 0.928862 | 0.335858 | 0.0217364 | 0.106043 | 0.847836 | 0.598828 | 0.249008 | 0.353595 | 0.0703226 | 0.645761 | 0.981424 | 0.118389 |
| bonus_part_correctness | tier | nationals | 21051 | 0.942939 | 0.327857 | 0.0648176 | 0.0997902 | 0.863379 | 0.428911 | 0.434469 | 0.329415 | 0.0400991 | 0.275033 | 0.89532 | 0.129262 |
| bonus_part_correctness | tier | regionals | 27762 | 0.943849 | 0.322748 | 0.0552712 | 0.0990466 | 0.864239 | 0.483611 | 0.380628 | 0.350725 | 0.0353042 | 0.362723 | 0.940561 | 0.123764 |
| bonus_part_correctness | tier | winter | 42312 | 0.933857 | 0.332895 | 0.0283977 | 0.103619 | 0.854226 | 0.511864 | 0.342362 | 0.362451 | 0.0413155 | 0.445057 | 0.966654 | 0.118539 |
| bonus_part_correctness | category | Current Events | 1281 | 0.934937 | 0.331675 | 0.0309303 | 0.102449 | 0.855582 | 0.501952 | 0.35363 | 0.366761 | 0.0419327 | 0.454925 | 0.957778 | 0.115202 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.925201 | 0.353436 | 0.0316696 | 0.111064 | 0.845024 | 0.507697 | 0.337327 | 0.352881 | 0.047364 | 0.437438 | 0.964421 | 0.125172 |
| bonus_part_correctness | category | Geography | 2427 | 0.929447 | 0.337971 | 0.0365249 | 0.105312 | 0.851257 | 0.60033 | 0.250927 | 0.348244 | 0.0594125 | 0.665648 | 0.972492 | 0.123052 |
| bonus_part_correctness | category | History | 21273 | 0.935866 | 0.328847 | 0.0335722 | 0.102555 | 0.853993 | 0.555446 | 0.298547 | 0.358777 | 0.0501089 | 0.555558 | 0.9734 | 0.120315 |
| bonus_part_correctness | category | Literature | 21312 | 0.94151 | 0.317001 | 0.0347526 | 0.0975842 | 0.865803 | 0.515813 | 0.349991 | 0.364279 | 0.044883 | 0.445424 | 0.97201 | 0.117254 |
| bonus_part_correctness | category | Mythology | 4923 | 0.917339 | 0.359322 | 0.0315499 | 0.114453 | 0.832013 | 0.617713 | 0.2143 | 0.33495 | 0.09999 | 0.642588 | 0.977876 | 0.129554 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.946519 | 0.307868 | 0.0434866 | 0.0931179 | 0.868711 | 0.522799 | 0.345912 | 0.36727 | 0.0378986 | 0.49056 | 0.962914 | 0.115073 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.93105 | 0.344393 | 0.0406026 | 0.107274 | 0.850872 | 0.491481 | 0.359391 | 0.349361 | 0.0473858 | 0.403398 | 0.957378 | 0.126862 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.905957 | 0.373046 | 0.0219095 | 0.1214 | 0.823568 | 0.622396 | 0.201172 | 0.339565 | 0.0930107 | 0.676669 | 0.984978 | 0.123157 |
| bonus_part_correctness | category | Religion | 5280 | 0.935444 | 0.330769 | 0.033177 | 0.102987 | 0.85303 | 0.505871 | 0.347159 | 0.361588 | 0.0395845 | 0.44917 | 0.96392 | 0.119014 |
| bonus_part_correctness | category | Science | 21183 | 0.933845 | 0.333813 | 0.0319563 | 0.104107 | 0.851013 | 0.529812 | 0.321201 | 0.360342 | 0.049429 | 0.489937 | 0.970737 | 0.120103 |
| bonus_part_correctness | category | Social Science | 4698 | 0.943098 | 0.30928 | 0.0322861 | 0.0956488 | 0.866539 | 0.476799 | 0.38974 | 0.369953 | 0.0316609 | 0.350429 | 0.970044 | 0.111143 |
| bonus_part_correctness | category | Unknown | 27762 | 0.943849 | 0.322748 | 0.0552712 | 0.0990466 | 0.864239 | 0.483611 | 0.380628 | 0.350725 | 0.0353042 | 0.362723 | 0.940561 | 0.123764 |

## Posterior Predictive Checks

| stage | discrepancy | stratum | observed | replicated_mean | replicated_p05 | replicated_p95 | posterior_predictive_p_value | draws |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| compositional | bonus_score_mass | 0 | 0.074 | 0.0731 | 0.0618 | 0.0841 | 0.5 | 20 |
| compositional | bonus_score_mass | 10 | 0.442 | 0.4198 | 0.3819 | 0.4447 | 0.15 | 20 |
| compositional | bonus_score_mass | 20 | 0.378 | 0.3928 | 0.3559 | 0.4301 | 0.75 | 20 |
| compositional | bonus_score_mass | 30 | 0.106 | 0.1143 | 0.097 | 0.1304 | 0.8 | 20 |
| pyramidal | buzz_position_mass | Q1 | 0.0162602 | 0.0669732 | 0.0510337 | 0.0903712 | 1 | 20 |
| pyramidal | buzz_position_mass | Q2 | 0.0934959 | 0.0954916 | 0.075213 | 0.112045 | 0.6 | 20 |
| pyramidal | buzz_position_mass | Q3 | 0.25813 | 0.210521 | 0.187023 | 0.23371 | 0 | 20 |
| pyramidal | buzz_position_mass | Q4 | 0.329268 | 0.325247 | 0.30453 | 0.346334 | 0.4 | 20 |
| pyramidal | buzz_position_mass | Q5 | 0.302846 | 0.301767 | 0.28054 | 0.330081 | 0.4 | 20 |
| pyramidal | dead_tossup_rate | all | 0.016 | 0.0627 | 0.0495 | 0.0821 | 1 | 20 |
| pyramidal | neg_rate | all | 0.254065 | 0.236095 | 0.197042 | 0.270536 | 0.3 | 20 |
| pyramidal | player_neg_rate | alec-riso | 0 | 0.104167 | 0 | 0.441667 | 1 | 8 |
| pyramidal | player_neg_rate | andrew-kelley | 0 | 0 | 0 | 0 | 1 | 1 |
| pyramidal | player_neg_rate | arhith-dharanendra | 0.666667 | 0 | 0 | 0 | 0 | 1 |
| pyramidal | player_neg_rate | arunn-sankar | 0.25 | 0.233333 | 0 | 0.466667 | 0.6 | 5 |
| pyramidal | player_neg_rate | biniam-alaro | 0 | 0.333333 | 0.0333333 | 0.633333 | 1 | 2 |
| pyramidal | player_neg_rate | caleb-kendrick | 0 | 0.227273 | 0 | 0.5 | 1 | 11 |
| pyramidal | player_neg_rate | cormac-beirne | 0 | 0.134615 | 0 | 0.666667 | 1 | 13 |
| pyramidal | player_neg_rate | daniel-chen | 0.666667 | 0.444444 | 0.333333 | 0.633333 | 0.333333 | 3 |
| pyramidal | player_neg_rate | henry-bylinowski | 0.4 | 0.0909091 | 0 | 0.291667 | 0 | 11 |
| pyramidal | player_neg_rate | jack-rado | 0 | 0.241667 | 0 | 0.666667 | 1 | 10 |
| pyramidal | player_neg_rate | jason-zhang | 0 | 0.291667 | 0.254167 | 0.329167 | 1 | 2 |
| pyramidal | player_neg_rate | jonathan-shauf | 0.333333 | 0.238095 | 0 | 0.566667 | 0.571429 | 7 |
| pyramidal | player_neg_rate | kevin-park | 0.333333 | 0.166667 | 0 | 0.333333 | 0.5 | 6 |
| pyramidal | player_neg_rate | liam-starnes | 0.333333 | 0.291667 | 0.254167 | 0.329167 | 0.5 | 2 |
| pyramidal | player_neg_rate | malachi-ledford | 0 | 0.32381 | 0 | 0.7 | 1 | 13 |
| pyramidal | player_neg_rate | michal-gerasimiuk | 0.666667 | 0.15625 | 0 | 0.55 | 0.125 | 8 |
| pyramidal | player_neg_rate | omer-keskin | 0 | 0.17 | 0 | 0.425 | 1 | 10 |
| pyramidal | player_neg_rate | orion-keller | 0 | 0.252778 | 0 | 0.666667 | 1 | 12 |
| pyramidal | player_neg_rate | owen-ashbrook | 0 | 0.4 | 0.4 | 0.4 | 1 | 1 |
| pyramidal | player_neg_rate | patrick-torre | 0 | 0.416667 | 0.05 | 0.666667 | 1 | 4 |
| pyramidal | player_neg_rate | rohan-dalal | 0.25 | 0.22619 | 0 | 0.691667 | 0.466667 | 15 |
| pyramidal | player_neg_rate | rosie-zhang | 0.333333 | 0.333333 | 0.333333 | 0.333333 | 1 | 1 |
| pyramidal | player_neg_rate | sam-macchi | 0 | 0.45 | 0.266667 | 0.666667 | 1 | 5 |
| pyramidal | player_neg_rate | shardul-rao | 0.6 | 0.125 | 0.0125 | 0.2375 | 0 | 2 |
| pyramidal | player_neg_rate | sinecio-morales | 0 | 0 | 0 | 0 | 1 | 3 |
| pyramidal | player_neg_rate | stella-brown | 0.333333 | 0 | 0 | 0 | 0 | 1 |
| pyramidal | player_neg_rate | teigue-kelly | 0.333333 | 0 | 0 | 0 | 0 | 2 |
| pyramidal | player_neg_rate | william-orr | 0 | 0.190476 | 0 | 0.566667 | 1 | 7 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.936141 | 0.936291 | 0.000149888 | synergy |
| log_loss | 0.331058 | 0.330929 | -0.000128668 | synergy |
| ece | 0.0382418 | 0.037406 | -0.000835819 | synergy |
| brier | 0.10349 | 0.102833 | -0.000657292 | synergy |
| accuracy_lift_over_all_correct | 0.333498 | 0.335237 | 0.00173834 | synergy |
| part_accuracy | 0.853987 | 0.855726 | 0.00173834 | synergy |
| part_accuracy_macro_team | 0.856057 | 0.858083 | 0.00202585 | synergy |
| part_accuracy_macro_game | 0.854284 | 0.856058 | 0.00177425 | synergy |
| part_accuracy_macro_bonus | 0.861529 | 0.860165 | -0.00136367 | no-synergy |
| exact_acc | 0.61591 | 0.620586 | 0.00467552 | synergy |
| ranked_probability_score | 0.0941761 | 0.0920475 | -0.00212862 | synergy |
| bonus_total_score_log_loss | 0.838958 | 0.828797 | -0.0101609 | synergy |
| ppb_mae | 1.52347 | 0.86116 | -0.66231 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 0.92243 | 0.68624 | -2.00637 | -0.236352 | 0.513703 | 0.89398 | 1.32605 | 2.05122 | 3.99296 |
| player | theta_1 | 1455 | -0.318297 | 0.620208 | -2.11265 | -1.36203 | -0.724307 | -0.285834 | 0.107053 | 0.683286 | 1.35884 |
| player | theta_2 | 1455 | -0.544197 | 0.660279 | -2.62173 | -1.63752 | -0.999509 | -0.546412 | -0.059649 | 0.536743 | 1.28957 |
| player | theta_3 | 1455 | -0.376151 | 0.670758 | -2.55483 | -1.4467 | -0.860124 | -0.368892 | 0.0863452 | 0.741453 | 1.66749 |
| player | theta_4 | 1455 | -0.365854 | 0.619832 | -2.97902 | -1.3722 | -0.791978 | -0.361685 | 0.0615182 | 0.651666 | 1.47326 |
| player | theta_5 | 1455 | -0.461707 | 0.611735 | -2.34887 | -1.46216 | -0.860956 | -0.480121 | -0.0490942 | 0.516115 | 1.46659 |
| player | theta_norm | 1455 | 1.62195 | 0.531979 | 0.20058 | 0.793185 | 1.23665 | 1.61493 | 2.00493 | 2.54005 | 3.48353 |
| tossup | beta_1 | 1260 | 0.861065 | 0.449273 | -0.318857 | 0.3104 | 0.558046 | 0.754328 | 1.0959 | 1.74695 | 3.6387 |
| tossup | beta_2 | 1260 | 0.958252 | 0.537212 | -0.337806 | 0.282582 | 0.547261 | 0.819133 | 1.33032 | 1.92499 | 3.16618 |
| tossup | beta_3 | 1260 | 0.890807 | 0.516699 | -0.221309 | 0.297358 | 0.532158 | 0.72841 | 1.15486 | 1.88667 | 3.68116 |
| tossup | beta_4 | 1260 | 0.950943 | 0.50881 | -0.389747 | 0.337072 | 0.563476 | 0.815805 | 1.28136 | 1.89618 | 3.06184 |
| tossup | beta_5 | 1260 | 0.887633 | 0.507007 | -0.228542 | 0.315943 | 0.542273 | 0.755075 | 1.13453 | 1.84072 | 3.92602 |
| tossup | gamma_1 | 1260 | 14.0648 | 63.3886 | 0.938455 | 2.55415 | 3.91273 | 4.87588 | 5.99562 | 20.2782 | 1040.05 |
| tossup | gamma_2 | 1260 | 19.3022 | 83.7804 | 0.488869 | 2.7849 | 4.1661 | 5.12073 | 6.77039 | 32.4124 | 1056.73 |
| tossup | gamma_3 | 1260 | 21.2664 | 99.6381 | 1.36696 | 2.95653 | 4.08711 | 5.00341 | 6.35078 | 33.9034 | 1509.72 |
| tossup | gamma_4 | 1260 | 19.229 | 93.6178 | 1.03945 | 2.8738 | 4.04224 | 5.07567 | 6.99453 | 28.9506 | 1658.59 |
| tossup | gamma_5 | 1260 | 17.2275 | 78.4381 | 0.929284 | 2.68183 | 3.91089 | 4.93505 | 6.4143 | 29.9432 | 1232.73 |
| tossup | mu_1 | 1260 | 0.546819 | 0.124294 | 0.209211 | 0.395988 | 0.472384 | 0.513265 | 0.602542 | 0.795511 | 0.991732 |
| tossup | mu_2 | 1260 | 0.565357 | 0.143312 | 0.184419 | 0.409392 | 0.463956 | 0.51996 | 0.643545 | 0.865374 | 0.993681 |
| tossup | mu_3 | 1260 | 0.556503 | 0.139592 | 0.238918 | 0.410884 | 0.464228 | 0.511282 | 0.617398 | 0.873776 | 0.989589 |
| tossup | mu_4 | 1260 | 0.573316 | 0.147744 | 0.142884 | 0.407901 | 0.46931 | 0.524163 | 0.656277 | 0.89104 | 0.99319 |
| tossup | mu_5 | 1260 | 0.551824 | 0.128476 | 0.224905 | 0.403817 | 0.468079 | 0.513806 | 0.614905 | 0.80051 | 0.992586 |
| tossup | r_1 | 1260 | 1.23978 | 0.745452 | 0.124448 | 0.316083 | 0.666529 | 1.10049 | 1.64009 | 2.67502 | 4.04237 |
| tossup | r_2 | 1260 | 1.36364 | 0.807752 | 0.106206 | 0.347007 | 0.759183 | 1.15229 | 1.84609 | 2.90243 | 3.87477 |
| tossup | r_3 | 1260 | 1.26294 | 0.836967 | 0.0739993 | 0.335806 | 0.655869 | 1.0072 | 1.5854 | 3.03323 | 4.4989 |
| tossup | r_4 | 1260 | 1.42758 | 0.921802 | 0.124671 | 0.376616 | 0.709946 | 1.12325 | 1.99377 | 3.21066 | 5.36964 |
| tossup | r_5 | 1260 | 1.21018 | 0.656682 | 0.0872471 | 0.30963 | 0.702616 | 1.11401 | 1.624 | 2.44052 | 3.57261 |
| tossup | r_norm | 1260 | 3.34581 | 0.697984 | 1.56506 | 2.23764 | 2.86166 | 3.31953 | 3.78981 | 4.53484 | 6.36193 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.00208973 | 1.3339 | -2.93271 | -1.96904 | -1.22044 | -0.0157359 | 1.13604 | 2.09405 | 3.13852 |
| bonus_part | alpha_1 | 3768 | 0.15345 | 0.535068 | -1.77174 | -0.714691 | -0.153727 | 0.117303 | 0.437033 | 1.07854 | 2.64281 |
| bonus_part | alpha_2 | 3768 | 0.0636651 | 0.69793 | -2.1012 | -1.19078 | -0.434233 | 0.210112 | 0.597974 | 0.993231 | 2.29657 |
| bonus_part | alpha_3 | 3768 | 0.0773205 | 0.589087 | -1.95272 | -0.897781 | -0.31464 | 0.124369 | 0.434717 | 1.01941 | 2.46027 |
| bonus_part | alpha_4 | 3768 | 0.139527 | 0.577805 | -1.85992 | -0.787592 | -0.224002 | 0.129938 | 0.482223 | 1.13403 | 2.25871 |
| bonus_part | alpha_5 | 3768 | 0.0964804 | 0.612637 | -2.01196 | -0.947023 | -0.351185 | 0.168016 | 0.546253 | 1.00273 | 1.97629 |
| bonus_part | alpha_norm | 3768 | 1.28806 | 0.482136 | 0.0667458 | 0.538329 | 0.945769 | 1.25516 | 1.61971 | 2.08433 | 3.17346 |
