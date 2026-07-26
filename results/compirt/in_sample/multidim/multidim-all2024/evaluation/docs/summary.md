# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/multidim/multidim-all2024/evaluation`
Result root: `results/compirt/in_sample/multidim/multidim-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 360025 |
| pyramidal | calibrate_correctness | False |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 2000 |
| compositional | final_loss | 66566.7 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.153747 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.927123 |
| log_loss | 0.355133 |
| ece | 0.0417817 |
| brier | 0.110096 |
| part_accuracy | 0.845678 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.325189 |
| part_accuracy_macro_team | 0.848976 |
| part_accuracy_macro_bonus | 0.853912 |
| probability_std | 0.336235 |
| probability_p10 | 0.0777476 |
| probability_p50 | 0.471455 |
| probability_p90 | 0.945791 |
| mean_predictive_variance | 0.136928 |
| exact_acc | 0.596534 |
| ranked_probability_score | 0.100243 |
| bonus_total_score_log_loss | 0.889913 |
| ppb_mae | 1.83683 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.700325 |
| log_loss | 0.57645 |
| ece | 0.128749 |
| brier | 0.192849 |
| accuracy | 0.715302 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | -0.0519681 |
| probability_std | 0.256321 |
| probability_p10 | 0.237035 |
| probability_p50 | 0.709465 |
| probability_p90 | 0.92861 |
| mean_predictive_variance | 0.163477 |
| integrated_brier_score | 0.085288 |
| joint_tossup_event_log_loss | 6.10421 |
| buzz_position_mae | 0.134659 |
| buzz_position_median_absolute_error | 0.115784 |
| buzz_position_bias | -0.0398828 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |
| first_buzzer_top1_accuracy | 0.47938 |
| first_buzzer_mean_reciprocal_rank | 0.670549 |
| first_buzzer_log_loss | 1.34399 |
| first_buzzer_events | 47914 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.803238 |
| match_winner_brier | 0.130041 |
| match_games | 2409 |
| match_simulations_per_game | 500 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.700325 | 0.57645 | 0.128749 | 0.192849 | 0.715302 | 0.767271 | -0.0519681 | 0.256321 | 0.237035 | 0.709465 | 0.92861 | 0.163477 |
| tossup_correctness | tier | fall | 14760 | 0.70572 | 0.561576 | 0.143458 | 0.186969 | 0.72439 | 0.787466 | -0.0630759 | 0.253991 | 0.243996 | 0.711148 | 0.925278 | 0.164317 |
| tossup_correctness | tier | nationals | 7940 | 0.691216 | 0.58643 | 0.0904968 | 0.197388 | 0.706675 | 0.72733 | -0.0206549 | 0.249351 | 0.273071 | 0.736643 | 0.9388 | 0.159609 |
| tossup_correctness | tier | regionals | 10202 | 0.701128 | 0.583724 | 0.123581 | 0.194809 | 0.711429 | 0.758969 | -0.0475397 | 0.260262 | 0.229176 | 0.711791 | 0.932555 | 0.161282 |
| tossup_correctness | tier | winter | 15012 | 0.706701 | 0.580852 | 0.145523 | 0.194897 | 0.713562 | 0.774181 | -0.0606182 | 0.258562 | 0.222686 | 0.690158 | 0.922421 | 0.166189 |
| tossup_correctness | category | Current Events | 640 | 0.668661 | 0.621403 | 0.135781 | 0.213773 | 0.673438 | 0.734375 | -0.0609375 | 0.257388 | 0.18271 | 0.654167 | 0.901982 | 0.172606 |
| tossup_correctness | category | Fine Arts | 5640 | 0.703603 | 0.578562 | 0.136787 | 0.194849 | 0.709574 | 0.766489 | -0.0569149 | 0.258828 | 0.221364 | 0.695694 | 0.926731 | 0.165172 |
| tossup_correctness | category | Geography | 972 | 0.659361 | 0.660724 | 0.125307 | 0.232341 | 0.632716 | 0.675926 | -0.0432099 | 0.246039 | 0.2038 | 0.6001 | 0.870712 | 0.185861 |
| tossup_correctness | category | History | 7599 | 0.715954 | 0.553338 | 0.114515 | 0.183856 | 0.729438 | 0.764969 | -0.035531 | 0.25248 | 0.254849 | 0.723082 | 0.927855 | 0.162467 |
| tossup_correctness | category | Literature | 7469 | 0.677603 | 0.568442 | 0.145958 | 0.187592 | 0.728879 | 0.812157 | -0.0832775 | 0.256317 | 0.261858 | 0.752678 | 0.941625 | 0.154274 |
| tossup_correctness | category | Mythology | 1692 | 0.652222 | 0.631835 | 0.209866 | 0.213939 | 0.683215 | 0.80792 | -0.124704 | 0.248221 | 0.226421 | 0.654424 | 0.894169 | 0.177687 |
| tossup_correctness | category | Other Academic | 357 | 0.703448 | 0.586898 | 0.154439 | 0.197862 | 0.722689 | 0.756303 | -0.0336134 | 0.240471 | 0.226468 | 0.661095 | 0.868729 | 0.181798 |
| tossup_correctness | category | Philosophy | 1649 | 0.726333 | 0.547089 | 0.13629 | 0.183984 | 0.722256 | 0.77926 | -0.0570042 | 0.256484 | 0.235423 | 0.704448 | 0.926305 | 0.163775 |
| tossup_correctness | category | Popular Culture | 538 | 0.60545 | 0.737916 | 0.308739 | 0.252309 | 0.64684 | 0.864312 | -0.217472 | 0.24505 | 0.172937 | 0.592442 | 0.846479 | 0.186862 |
| tossup_correctness | category | Religion | 1889 | 0.715781 | 0.58688 | 0.117903 | 0.197633 | 0.700371 | 0.724722 | -0.0243515 | 0.261326 | 0.201283 | 0.673592 | 0.910189 | 0.16862 |
| tossup_correctness | category | Science | 7556 | 0.705795 | 0.560853 | 0.105061 | 0.187062 | 0.728295 | 0.754235 | -0.0259397 | 0.248699 | 0.267856 | 0.72136 | 0.933012 | 0.162849 |
| tossup_correctness | category | Social Science | 1711 | 0.723514 | 0.576966 | 0.108324 | 0.19541 | 0.701929 | 0.722385 | -0.0204559 | 0.256552 | 0.20773 | 0.677703 | 0.90919 | 0.171091 |
| tossup_correctness | category | Unknown | 10202 | 0.701128 | 0.583724 | 0.123581 | 0.194809 | 0.711429 | 0.758969 | -0.0475397 | 0.260262 | 0.229176 | 0.711791 | 0.932555 | 0.161282 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.744768 | 0.949603 | 0.383773 | 0.327888 | 0.502651 | 0.727466 | -0.224814 | 0.244478 | 0.049232 | 0.312351 | 0.703948 | 0.166215 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.728459 | 0.783167 | 0.296392 | 0.271254 | 0.579791 | 0.736496 | -0.156706 | 0.264035 | 0.0898744 | 0.434194 | 0.813244 | 0.176755 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.717273 | 0.617892 | 0.185283 | 0.210047 | 0.680126 | 0.761053 | -0.0809279 | 0.260011 | 0.184768 | 0.616373 | 0.893394 | 0.176653 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.711255 | 0.520188 | 0.107127 | 0.172145 | 0.749052 | 0.786033 | -0.0369804 | 0.229639 | 0.331946 | 0.734975 | 0.931853 | 0.164798 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.705167 | 0.513135 | 0.0529966 | 0.167527 | 0.763782 | 0.765769 | -0.00198718 | 0.208197 | 0.433402 | 0.803974 | 0.949268 | 0.148209 |
| bonus_part_correctness | aggregate | all | 133461 | 0.927123 | 0.355133 | 0.0417817 | 0.110096 | 0.845678 | 0.520489 | 0.325189 | 0.336235 | 0.0777476 | 0.471455 | 0.945791 | 0.136928 |
| bonus_part_correctness | tier | fall | 42336 | 0.918816 | 0.365041 | 0.0365563 | 0.114663 | 0.835695 | 0.598828 | 0.236867 | 0.324373 | 0.116099 | 0.61454 | 0.952512 | 0.138837 |
| bonus_part_correctness | tier | nationals | 21051 | 0.935883 | 0.340517 | 0.0535738 | 0.103536 | 0.857346 | 0.428911 | 0.428436 | 0.325029 | 0.0616803 | 0.310766 | 0.903062 | 0.136976 |
| bonus_part_correctness | tier | regionals | 27762 | 0.931857 | 0.345915 | 0.0480624 | 0.10603 | 0.854297 | 0.483611 | 0.370687 | 0.33547 | 0.0732169 | 0.399849 | 0.938356 | 0.136602 |
| bonus_part_correctness | tier | winter | 42312 | 0.924052 | 0.358539 | 0.0381357 | 0.111457 | 0.844205 | 0.511864 | 0.332341 | 0.338808 | 0.073238 | 0.45412 | 0.949607 | 0.135206 |
| bonus_part_correctness | category | Current Events | 1281 | 0.936379 | 0.338875 | 0.0495865 | 0.103294 | 0.85402 | 0.501952 | 0.352069 | 0.347712 | 0.060504 | 0.467061 | 0.934119 | 0.128624 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.916734 | 0.375407 | 0.0386058 | 0.117456 | 0.836973 | 0.507697 | 0.329275 | 0.329204 | 0.0765785 | 0.452284 | 0.940099 | 0.141524 |
| bonus_part_correctness | category | Geography | 2427 | 0.922829 | 0.360213 | 0.0439074 | 0.112283 | 0.839308 | 0.60033 | 0.238978 | 0.324324 | 0.0852726 | 0.642521 | 0.943733 | 0.13936 |
| bonus_part_correctness | category | History | 21273 | 0.926954 | 0.354596 | 0.0408308 | 0.11031 | 0.841536 | 0.555446 | 0.28609 | 0.33505 | 0.0790364 | 0.545148 | 0.947906 | 0.136503 |
| bonus_part_correctness | category | Literature | 21312 | 0.929622 | 0.348629 | 0.0444277 | 0.107454 | 0.852994 | 0.515813 | 0.337181 | 0.33819 | 0.082442 | 0.457572 | 0.949718 | 0.135619 |
| bonus_part_correctness | category | Mythology | 4923 | 0.905508 | 0.386825 | 0.0393234 | 0.123247 | 0.817388 | 0.617713 | 0.199675 | 0.30691 | 0.157876 | 0.626671 | 0.952201 | 0.147185 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.947495 | 0.308297 | 0.0498589 | 0.0923895 | 0.874214 | 0.522799 | 0.351415 | 0.356648 | 0.0564724 | 0.517915 | 0.952061 | 0.122692 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.914495 | 0.381583 | 0.0435745 | 0.119582 | 0.834436 | 0.491481 | 0.342954 | 0.3226 | 0.0868253 | 0.42247 | 0.93163 | 0.145456 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.907387 | 0.381363 | 0.0411077 | 0.122089 | 0.822917 | 0.622396 | 0.200521 | 0.316797 | 0.114793 | 0.600701 | 0.957627 | 0.141209 |
| bonus_part_correctness | category | Religion | 5280 | 0.92939 | 0.348663 | 0.041302 | 0.108263 | 0.845833 | 0.505871 | 0.339962 | 0.34493 | 0.0606067 | 0.450477 | 0.941932 | 0.130935 |
| bonus_part_correctness | category | Science | 21183 | 0.927244 | 0.35436 | 0.0402561 | 0.109884 | 0.844167 | 0.529812 | 0.314356 | 0.337185 | 0.0818478 | 0.491148 | 0.948658 | 0.1361 |
| bonus_part_correctness | category | Social Science | 4698 | 0.936352 | 0.329912 | 0.0431219 | 0.101567 | 0.858025 | 0.476799 | 0.381226 | 0.350641 | 0.0568441 | 0.344883 | 0.947946 | 0.125642 |
| bonus_part_correctness | category | Unknown | 27762 | 0.931857 | 0.345915 | 0.0480624 | 0.10603 | 0.854297 | 0.483611 | 0.370687 | 0.33547 | 0.0732169 | 0.399849 | 0.938356 | 0.136602 |

## Posterior Predictive Checks

| stage | discrepancy | stratum | observed | replicated_mean | replicated_p05 | replicated_p95 | posterior_predictive_p_value | draws |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| compositional | bonus_score_mass | 0 | 0.074 | 0.0505 | 0.0398 | 0.062 | 0 | 20 |
| compositional | bonus_score_mass | 10 | 0.442 | 0.3891 | 0.3592 | 0.4242 | 0 | 20 |
| compositional | bonus_score_mass | 20 | 0.378 | 0.4445 | 0.4217 | 0.4747 | 1 | 20 |
| compositional | bonus_score_mass | 30 | 0.106 | 0.1159 | 0.0997 | 0.1281 | 0.9 | 20 |
| pyramidal | buzz_position_mass | Q1 | 0.0162602 | 0.0708647 | 0.0552414 | 0.0966422 | 1 | 20 |
| pyramidal | buzz_position_mass | Q2 | 0.0934959 | 0.111717 | 0.089903 | 0.130928 | 0.85 | 20 |
| pyramidal | buzz_position_mass | Q3 | 0.25813 | 0.247374 | 0.203754 | 0.277032 | 0.3 | 20 |
| pyramidal | buzz_position_mass | Q4 | 0.329268 | 0.337336 | 0.310958 | 0.362684 | 0.7 | 20 |
| pyramidal | buzz_position_mass | Q5 | 0.302846 | 0.232708 | 0.216898 | 0.251187 | 0 | 20 |
| pyramidal | dead_tossup_rate | all | 0.016 | 0.0598 | 0.0476 | 0.0702 | 1 | 20 |
| pyramidal | neg_rate | all | 0.254065 | 0.417197 | 0.386124 | 0.444681 | 1 | 20 |
| pyramidal | player_neg_rate | alec-riso | 0 | 0.133333 | 0 | 0.333333 | 1 | 5 |
| pyramidal | player_neg_rate | arhith-dharanendra | 0.666667 | 0.333333 | 0.333333 | 0.333333 | 0 | 1 |
| pyramidal | player_neg_rate | arunn-sankar | 0.25 | 0.283333 | 0.05 | 0.466667 | 0.8 | 5 |
| pyramidal | player_neg_rate | biniam-alaro | 0 | 0.666667 | 0.666667 | 0.666667 | 1 | 1 |
| pyramidal | player_neg_rate | caleb-kendrick | 0 | 0.329932 | 0.0428571 | 0.616667 | 1 | 7 |
| pyramidal | player_neg_rate | cormac-beirne | 0 | 0.413725 | 0 | 0.666667 | 1 | 17 |
| pyramidal | player_neg_rate | daniel-chen | 0.666667 | 0.555556 | 0.0666667 | 0.966667 | 0.666667 | 3 |
| pyramidal | player_neg_rate | henry-bylinowski | 0.4 | 0.159524 | 0 | 0.333333 | 0 | 7 |
| pyramidal | player_neg_rate | jack-rado | 0 | 0.180556 | 0 | 0.458333 | 1 | 6 |
| pyramidal | player_neg_rate | jason-zhang | 0 | 0.444444 | 0.333333 | 0.633333 | 1 | 3 |
| pyramidal | player_neg_rate | jonathan-shauf | 0.333333 | 0.166667 | 0 | 0.333333 | 0.5 | 4 |
| pyramidal | player_neg_rate | kevin-park | 0.333333 | 0.283333 | 0.05 | 0.466667 | 0.6 | 5 |
| pyramidal | player_neg_rate | liam-starnes | 0.333333 | 0.270833 | 0 | 0.6875 | 0.5 | 4 |
| pyramidal | player_neg_rate | malachi-ledford | 0 | 0.3 | 0 | 0.75 | 1 | 17 |
| pyramidal | player_neg_rate | michal-gerasimiuk | 0.666667 | 0.266667 | 0.206667 | 0.326667 | 0 | 2 |
| pyramidal | player_neg_rate | omer-keskin | 0 | 0.144444 | 0 | 0.333333 | 1 | 6 |
| pyramidal | player_neg_rate | orion-keller | 0 | 0.316667 | 0 | 0.866667 | 1 | 5 |
| pyramidal | player_neg_rate | owen-ashbrook | 0 | 0.611111 | 0.516667 | 0.666667 | 1 | 3 |
| pyramidal | player_neg_rate | patrick-torre | 0 | 0.666667 | 0.666667 | 0.666667 | 1 | 1 |
| pyramidal | player_neg_rate | rohan-dalal | 0.25 | 0.216667 | 0.05 | 0.316667 | 0.8 | 5 |
| pyramidal | player_neg_rate | sam-macchi | 0 | 0.283333 | 0 | 0.666667 | 1 | 10 |
| pyramidal | player_neg_rate | shardul-rao | 0.6 | 0.533333 | 0.0666667 | 0.933333 | 0.6 | 5 |
| pyramidal | player_neg_rate | sinecio-morales | 0 | 0.291667 | 0 | 0.775 | 1 | 10 |
| pyramidal | player_neg_rate | teigue-kelly | 0.333333 | 0.166667 | 0.0166667 | 0.316667 | 0.5 | 2 |
| pyramidal | player_neg_rate | william-orr | 0 | 0.222222 | 0 | 0.583333 | 1 | 6 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.927123 | 0.935559 | 0.00843554 | synergy |
| log_loss | 0.355133 | 0.336424 | -0.0187089 | synergy |
| ece | 0.0417817 | 0.0437654 | 0.00198365 | no-synergy |
| brier | 0.110096 | 0.104196 | -0.00589924 | synergy |
| accuracy_lift_over_all_correct | 0.325189 | 0.333528 | 0.00833951 | synergy |
| part_accuracy | 0.845678 | 0.854017 | 0.00833951 | synergy |
| part_accuracy_macro_team | 0.848976 | 0.857456 | 0.00847967 | synergy |
| part_accuracy_macro_game | 0.846101 | 0.854597 | 0.00849552 | synergy |
| part_accuracy_macro_bonus | 0.853912 | 0.857878 | 0.0039661 | synergy |
| exact_acc | 0.596534 | 0.614764 | 0.01823 | synergy |
| ranked_probability_score | 0.100243 | 0.0931524 | -0.00709033 | synergy |
| bonus_total_score_log_loss | 0.889913 | 0.840351 | -0.0495621 | synergy |
| ppb_mae | 1.83683 | 0.905 | -0.931831 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.51098 | 1.35343 | 0.723138 | 1.61455 | 3.9081 | 4.8549 | 5.45127 | 6.14437 | 7.0507 |
| player | theta_1 | 1455 | 0.0105468 | 0.729681 | -2.29718 | -1.3337 | -0.467246 | 0.120122 | 0.551619 | 1.05555 | 2.328 |
| player | theta_2 | 1455 | -0.0675416 | 0.730803 | -2.81725 | -1.42729 | -0.516298 | 0.0383081 | 0.443084 | 1.01004 | 1.69692 |
| player | theta_3 | 1455 | 0.109091 | 0.73321 | -2.09547 | -1.24056 | -0.350461 | 0.23776 | 0.610819 | 1.18357 | 2.26385 |
| player | theta_4 | 1455 | 0.0619244 | 0.74244 | -2.16384 | -1.33199 | -0.402477 | 0.197639 | 0.594157 | 1.14547 | 2.04531 |
| player | theta_5 | 1455 | -0.0166705 | 0.747911 | -2.6008 | -1.4037 | -0.462318 | 0.120182 | 0.527514 | 1.04083 | 1.64749 |
| player | theta_norm | 1455 | 1.54835 | 0.579974 | 0.292146 | 0.754318 | 1.12206 | 1.45277 | 1.92279 | 2.65475 | 3.70676 |
| tossup | beta_1 | 1260 | 0.730598 | 0.501776 | -2.41418 | 0.213117 | 0.395197 | 0.572758 | 0.945376 | 1.75774 | 2.75765 |
| tossup | beta_2 | 1260 | 0.822327 | 0.580847 | -1.01539 | 0.197013 | 0.39633 | 0.604864 | 1.23712 | 1.9625 | 2.65647 |
| tossup | beta_3 | 1260 | 0.725846 | 0.512934 | -1.6722 | 0.210046 | 0.392162 | 0.562407 | 0.908339 | 1.81302 | 2.89195 |
| tossup | beta_4 | 1260 | 0.768572 | 0.549474 | -0.802486 | 0.210858 | 0.401261 | 0.574868 | 0.998464 | 2.00726 | 3.38218 |
| tossup | beta_5 | 1260 | 0.808082 | 0.576291 | -1.32519 | 0.20626 | 0.389406 | 0.597827 | 1.14069 | 1.99113 | 2.88054 |
| tossup | gamma_1 | 1260 | 13.1646 | 73.7075 | 0.663624 | 3.14656 | 4.42507 | 5.11935 | 6.02534 | 26.5331 | 2046.72 |
| tossup | gamma_2 | 1260 | 13.8264 | 80.8711 | 0.881303 | 3.3239 | 4.52733 | 5.16583 | 6.46508 | 24.3964 | 2031.4 |
| tossup | gamma_3 | 1260 | 11.341 | 47.4914 | 0.153922 | 2.89244 | 4.42057 | 5.05636 | 5.85229 | 20.8066 | 805.69 |
| tossup | gamma_4 | 1260 | 17.0952 | 119.47 | 1.29639 | 3.1945 | 4.4522 | 5.09351 | 6.00226 | 23.5765 | 2156.82 |
| tossup | gamma_5 | 1260 | 15.1222 | 78.0386 | 0.77931 | 2.95593 | 4.47727 | 5.15946 | 6.50493 | 28.9149 | 1632.4 |
| tossup | mu_1 | 1260 | 0.498907 | 0.103286 | 0.156009 | 0.383461 | 0.443312 | 0.474716 | 0.524684 | 0.719273 | 0.956272 |
| tossup | mu_2 | 1260 | 0.51482 | 0.123002 | 0.233629 | 0.379105 | 0.439186 | 0.474986 | 0.556062 | 0.788815 | 0.976916 |
| tossup | mu_3 | 1260 | 0.50587 | 0.110171 | 0.173911 | 0.384152 | 0.449581 | 0.478697 | 0.52784 | 0.742186 | 0.988322 |
| tossup | mu_4 | 1260 | 0.503973 | 0.112898 | 0.104119 | 0.372506 | 0.446767 | 0.477923 | 0.521811 | 0.74891 | 0.986156 |
| tossup | mu_5 | 1260 | 0.511348 | 0.115064 | 0.126147 | 0.374966 | 0.445138 | 0.482212 | 0.550756 | 0.753014 | 0.992188 |
| tossup | r_1 | 1260 | 0.973098 | 0.736791 | 0.0865554 | 0.220677 | 0.425502 | 0.744118 | 1.31146 | 2.55225 | 4.948 |
| tossup | r_2 | 1260 | 1.30327 | 1.07824 | 0.0983441 | 0.218858 | 0.493551 | 0.914733 | 1.81759 | 3.54456 | 5.75502 |
| tossup | r_3 | 1260 | 1.09275 | 0.937037 | 0.0630926 | 0.196739 | 0.43657 | 0.750178 | 1.46365 | 3.02639 | 5.5279 |
| tossup | r_4 | 1260 | 1.0894 | 0.921586 | 0.0650252 | 0.227398 | 0.450391 | 0.762929 | 1.40119 | 3.17055 | 5.63893 |
| tossup | r_5 | 1260 | 1.18041 | 0.833939 | 0.0718148 | 0.21812 | 0.500455 | 0.94339 | 1.72389 | 2.76025 | 4.65232 |
| tossup | r_norm | 1260 | 3.13563 | 0.844448 | 1.047 | 1.90537 | 2.52854 | 3.04788 | 3.63211 | 4.62946 | 6.58415 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.821385 | 1.49108 | -2.32339 | -1.74162 | -0.420336 | 1.09252 | 2.07775 | 2.866 | 3.7932 |
| bonus_part | alpha_1 | 3768 | 0.153319 | 0.429926 | -1.35344 | -0.512974 | -0.127894 | 0.136428 | 0.411861 | 0.873064 | 2.17156 |
| bonus_part | alpha_2 | 3768 | 0.235707 | 0.507871 | -1.54897 | -0.508423 | -0.0882484 | 0.191517 | 0.517061 | 1.17643 | 2.44597 |
| bonus_part | alpha_3 | 3768 | 0.144466 | 0.517392 | -1.67795 | -0.639914 | -0.208345 | 0.105323 | 0.483828 | 1.00456 | 2.33205 |
| bonus_part | alpha_4 | 3768 | 0.169596 | 0.530381 | -1.79065 | -0.639176 | -0.191789 | 0.142593 | 0.514312 | 1.06272 | 2.49751 |
| bonus_part | alpha_5 | 3768 | 0.1825 | 0.419812 | -1.40464 | -0.466559 | -0.0688287 | 0.158701 | 0.417392 | 0.885062 | 2.06571 |
| bonus_part | alpha_norm | 3768 | 1.03785 | 0.502629 | 0.0591555 | 0.322144 | 0.646389 | 0.996136 | 1.34657 | 1.97654 | 2.85597 |
