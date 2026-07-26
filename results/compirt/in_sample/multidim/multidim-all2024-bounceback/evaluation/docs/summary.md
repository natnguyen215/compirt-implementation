# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/multidim/multidim-all2024-bounceback/evaluation`
Result root: `results/compirt/in_sample/multidim/multidim-all2024-bounceback`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 412362 |
| pyramidal | calibrate_correctness | False |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 2000 |
| compositional | final_loss | 66879.3 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.11934 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.924131 |
| log_loss | 0.358455 |
| ece | 0.0366069 |
| brier | 0.111821 |
| part_accuracy | 0.843295 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.322806 |
| part_accuracy_macro_team | 0.845959 |
| part_accuracy_macro_game | 0.843711 |
| part_accuracy_macro_bonus | 0.851473 |
| probability_std | 0.338338 |
| probability_p10 | 0.0757429 |
| probability_p50 | 0.474651 |
| probability_p90 | 0.95255 |
| mean_predictive_variance | 0.135477 |
| exact_acc | 0.590217 |
| ranked_probability_score | 0.102047 |
| bonus_total_score_log_loss | 0.900859 |
| ppb_mae | 1.97857 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.700393 |
| log_loss | 0.573395 |
| ece | 0.130664 |
| brier | 0.191409 |
| accuracy | 0.716847 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | -0.0504237 |
| probability_std | 0.252523 |
| probability_p10 | 0.245086 |
| probability_p50 | 0.704809 |
| probability_p90 | 0.926538 |
| mean_predictive_variance | 0.165552 |
| integrated_brier_score | 0.0867061 |
| joint_tossup_event_log_loss | 6.11618 |
| buzz_position_mae | 0.134574 |
| buzz_position_median_absolute_error | 0.11554 |
| buzz_position_bias | -0.0302251 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |
| first_buzzer_top1_accuracy | 0.477647 |
| first_buzzer_mean_reciprocal_rank | 0.667782 |
| first_buzzer_log_loss | 1.36117 |
| first_buzzer_events | 47914 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.806144 |
| match_winner_brier | 0.130001 |
| match_games | 2409 |
| match_simulations_per_game | 500 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.700393 | 0.573395 | 0.130664 | 0.191409 | 0.716847 | 0.767271 | -0.0504237 | 0.252523 | 0.245086 | 0.704809 | 0.926538 | 0.165552 |
| tossup_correctness | tier | fall | 14760 | 0.709766 | 0.550494 | 0.138184 | 0.183068 | 0.732995 | 0.787466 | -0.0544715 | 0.247876 | 0.254479 | 0.713427 | 0.923894 | 0.165882 |
| tossup_correctness | tier | nationals | 7940 | 0.681576 | 0.59896 | 0.103321 | 0.200601 | 0.701511 | 0.72733 | -0.0258186 | 0.251761 | 0.26519 | 0.725838 | 0.939986 | 0.160408 |
| tossup_correctness | tier | regionals | 10202 | 0.696916 | 0.587214 | 0.130243 | 0.195191 | 0.708587 | 0.758969 | -0.0503823 | 0.257029 | 0.236893 | 0.701518 | 0.931541 | 0.163859 |
| tossup_correctness | tier | winter | 15012 | 0.710562 | 0.573 | 0.146072 | 0.192178 | 0.714695 | 0.774181 | -0.0594857 | 0.253491 | 0.23298 | 0.684011 | 0.91862 | 0.169098 |
| tossup_correctness | category | Current Events | 640 | 0.667885 | 0.632752 | 0.149833 | 0.216164 | 0.660937 | 0.734375 | -0.0734375 | 0.248506 | 0.20356 | 0.644141 | 0.890277 | 0.17934 |
| tossup_correctness | category | Fine Arts | 5640 | 0.706464 | 0.570029 | 0.130906 | 0.191796 | 0.715071 | 0.766489 | -0.0514184 | 0.257388 | 0.232681 | 0.700928 | 0.93002 | 0.164535 |
| tossup_correctness | category | Geography | 972 | 0.695818 | 0.636075 | 0.126616 | 0.221443 | 0.658436 | 0.675926 | -0.0174897 | 0.244667 | 0.197767 | 0.576586 | 0.857496 | 0.187707 |
| tossup_correctness | category | History | 7599 | 0.723043 | 0.546216 | 0.120783 | 0.180789 | 0.734834 | 0.764969 | -0.0301355 | 0.248258 | 0.254662 | 0.713381 | 0.924258 | 0.165781 |
| tossup_correctness | category | Literature | 7469 | 0.673561 | 0.563151 | 0.140158 | 0.18603 | 0.729817 | 0.812157 | -0.0823403 | 0.252628 | 0.277235 | 0.753995 | 0.941528 | 0.154013 |
| tossup_correctness | category | Mythology | 1692 | 0.667496 | 0.594701 | 0.191896 | 0.198416 | 0.71513 | 0.80792 | -0.0927896 | 0.238574 | 0.254904 | 0.673144 | 0.899464 | 0.177798 |
| tossup_correctness | category | Other Academic | 357 | 0.689315 | 0.605896 | 0.169638 | 0.206225 | 0.691877 | 0.756303 | -0.0644258 | 0.237417 | 0.216769 | 0.635378 | 0.863508 | 0.185312 |
| tossup_correctness | category | Philosophy | 1649 | 0.716186 | 0.554077 | 0.138835 | 0.186425 | 0.710734 | 0.77926 | -0.0685264 | 0.255113 | 0.242687 | 0.700197 | 0.925651 | 0.165198 |
| tossup_correctness | category | Popular Culture | 538 | 0.591044 | 0.682558 | 0.283555 | 0.235957 | 0.663569 | 0.864312 | -0.200743 | 0.236327 | 0.197091 | 0.624449 | 0.85507 | 0.187628 |
| tossup_correctness | category | Religion | 1889 | 0.71006 | 0.58871 | 0.120802 | 0.198482 | 0.704606 | 0.724722 | -0.0201165 | 0.254735 | 0.217291 | 0.669595 | 0.904989 | 0.172261 |
| tossup_correctness | category | Science | 7556 | 0.704125 | 0.564972 | 0.110863 | 0.188518 | 0.722737 | 0.754235 | -0.0314981 | 0.244624 | 0.270675 | 0.708385 | 0.926958 | 0.167261 |
| tossup_correctness | category | Social Science | 1711 | 0.707738 | 0.586451 | 0.120958 | 0.19764 | 0.706604 | 0.722385 | -0.0157802 | 0.252371 | 0.211396 | 0.668581 | 0.908034 | 0.172818 |
| tossup_correctness | category | Unknown | 10202 | 0.696916 | 0.587214 | 0.130243 | 0.195191 | 0.708587 | 0.758969 | -0.0503823 | 0.257029 | 0.236893 | 0.701518 | 0.931541 | 0.163859 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.731444 | 0.924429 | 0.371424 | 0.322584 | 0.496288 | 0.727466 | -0.231177 | 0.243388 | 0.0561827 | 0.313109 | 0.719046 | 0.170038 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.735459 | 0.753998 | 0.286839 | 0.262255 | 0.594578 | 0.736496 | -0.141918 | 0.260717 | 0.0978 | 0.443962 | 0.808958 | 0.179492 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.723392 | 0.617188 | 0.195524 | 0.210457 | 0.676376 | 0.761053 | -0.0846778 | 0.252861 | 0.192431 | 0.599317 | 0.880755 | 0.181767 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.722738 | 0.516647 | 0.119634 | 0.171053 | 0.748055 | 0.786033 | -0.0379781 | 0.225982 | 0.324877 | 0.716391 | 0.91936 | 0.171244 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.695734 | 0.518309 | 0.0504597 | 0.166985 | 0.768013 | 0.765769 | 0.00224359 | 0.200343 | 0.463056 | 0.816762 | 0.955171 | 0.143524 |
| bonus_part_correctness | aggregate | all | 133461 | 0.924131 | 0.358455 | 0.0366069 | 0.111821 | 0.843295 | 0.520489 | 0.322806 | 0.338338 | 0.0757429 | 0.474651 | 0.95255 | 0.135477 |
| bonus_part_correctness | tier | fall | 42336 | 0.915573 | 0.368531 | 0.0311541 | 0.116451 | 0.833286 | 0.598828 | 0.234458 | 0.325522 | 0.116391 | 0.616785 | 0.959349 | 0.137568 |
| bonus_part_correctness | tier | nationals | 21051 | 0.934951 | 0.338462 | 0.0495933 | 0.10326 | 0.856634 | 0.428911 | 0.427723 | 0.330279 | 0.0560755 | 0.315197 | 0.910446 | 0.133847 |
| bonus_part_correctness | tier | regionals | 27762 | 0.927954 | 0.351064 | 0.041087 | 0.108465 | 0.850767 | 0.483611 | 0.367157 | 0.33735 | 0.0709683 | 0.40106 | 0.943941 | 0.135451 |
| bonus_part_correctness | tier | winter | 42312 | 0.920502 | 0.36317 | 0.0337189 | 0.113648 | 0.841771 | 0.511864 | 0.329906 | 0.340273 | 0.0734446 | 0.457975 | 0.956476 | 0.134211 |
| bonus_part_correctness | category | Current Events | 1281 | 0.935333 | 0.336004 | 0.0462475 | 0.101987 | 0.858704 | 0.501952 | 0.356753 | 0.351838 | 0.055955 | 0.487059 | 0.93644 | 0.125982 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.913117 | 0.38018 | 0.034454 | 0.119582 | 0.832271 | 0.507697 | 0.324573 | 0.330411 | 0.0762969 | 0.453533 | 0.946061 | 0.140768 |
| bonus_part_correctness | category | Geography | 2427 | 0.921213 | 0.360222 | 0.0456503 | 0.113131 | 0.832303 | 0.60033 | 0.231974 | 0.328196 | 0.0835031 | 0.640222 | 0.953888 | 0.136038 |
| bonus_part_correctness | category | History | 21273 | 0.923957 | 0.357818 | 0.035141 | 0.112033 | 0.840784 | 0.555446 | 0.285338 | 0.337229 | 0.0765348 | 0.55035 | 0.955257 | 0.134822 |
| bonus_part_correctness | category | Literature | 21312 | 0.927422 | 0.35099 | 0.0417541 | 0.108892 | 0.850741 | 0.515813 | 0.334929 | 0.339566 | 0.0809916 | 0.459765 | 0.956835 | 0.134658 |
| bonus_part_correctness | category | Mythology | 4923 | 0.903117 | 0.387528 | 0.0344285 | 0.124042 | 0.817388 | 0.617713 | 0.199675 | 0.309551 | 0.159294 | 0.636026 | 0.960185 | 0.144434 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.947289 | 0.307169 | 0.0493893 | 0.0931521 | 0.875 | 0.522799 | 0.352201 | 0.358244 | 0.0535786 | 0.52887 | 0.963249 | 0.121466 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.912372 | 0.382422 | 0.0419946 | 0.120071 | 0.832832 | 0.491481 | 0.341351 | 0.326483 | 0.0852965 | 0.42607 | 0.93938 | 0.143054 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.912098 | 0.370849 | 0.0354932 | 0.117988 | 0.832682 | 0.622396 | 0.210286 | 0.32194 | 0.117344 | 0.636288 | 0.964818 | 0.136164 |
| bonus_part_correctness | category | Religion | 5280 | 0.927186 | 0.352081 | 0.0334325 | 0.109983 | 0.843561 | 0.505871 | 0.337689 | 0.345668 | 0.0595421 | 0.43874 | 0.947559 | 0.13044 |
| bonus_part_correctness | category | Science | 21183 | 0.923494 | 0.358848 | 0.0343895 | 0.11201 | 0.842326 | 0.529812 | 0.312515 | 0.339483 | 0.0806017 | 0.492381 | 0.95584 | 0.134469 |
| bonus_part_correctness | category | Social Science | 4698 | 0.933918 | 0.331609 | 0.0339186 | 0.103008 | 0.851852 | 0.476799 | 0.375053 | 0.354021 | 0.0541665 | 0.345927 | 0.956993 | 0.123462 |
| bonus_part_correctness | category | Unknown | 27762 | 0.927954 | 0.351064 | 0.041087 | 0.108465 | 0.850767 | 0.483611 | 0.367157 | 0.33735 | 0.0709683 | 0.40106 | 0.943941 | 0.135451 |

## Posterior Predictive Checks

| stage | discrepancy | stratum | observed | replicated_mean | replicated_p05 | replicated_p95 | posterior_predictive_p_value | draws |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| compositional | bonus_score_mass | 0 | 0.074 | 0.0484 | 0.038 | 0.0581 | 0 | 20 |
| compositional | bonus_score_mass | 10 | 0.442 | 0.3971 | 0.375 | 0.4401 | 0.05 | 20 |
| compositional | bonus_score_mass | 20 | 0.378 | 0.4436 | 0.4189 | 0.473 | 1 | 20 |
| compositional | bonus_score_mass | 30 | 0.106 | 0.1109 | 0.0938 | 0.124 | 0.75 | 20 |
| pyramidal | buzz_position_mass | Q1 | 0.0162602 | 0.0728884 | 0.0616726 | 0.0877378 | 1 | 20 |
| pyramidal | buzz_position_mass | Q2 | 0.0934959 | 0.113662 | 0.0944134 | 0.126993 | 0.95 | 20 |
| pyramidal | buzz_position_mass | Q3 | 0.25813 | 0.230326 | 0.207536 | 0.250243 | 0 | 20 |
| pyramidal | buzz_position_mass | Q4 | 0.329268 | 0.317336 | 0.296006 | 0.335053 | 0.35 | 20 |
| pyramidal | buzz_position_mass | Q5 | 0.302846 | 0.265788 | 0.234025 | 0.285476 | 0 | 20 |
| pyramidal | dead_tossup_rate | all | 0.016 | 0.0517 | 0.038 | 0.0664 | 1 | 20 |
| pyramidal | neg_rate | all | 0.254065 | 0.404218 | 0.371008 | 0.433331 | 1 | 20 |
| pyramidal | player_neg_rate | alec-riso | 0 | 0.166667 | 0 | 0.583333 | 1 | 6 |
| pyramidal | player_neg_rate | andrew-kelley | 0 | 0.666667 | 0.666667 | 0.666667 | 1 | 1 |
| pyramidal | player_neg_rate | arhith-dharanendra | 0.666667 | 0.166667 | 0.0166667 | 0.316667 | 0 | 2 |
| pyramidal | player_neg_rate | arunn-sankar | 0.25 | 0.0833333 | 0 | 0.333333 | 0.25 | 8 |
| pyramidal | player_neg_rate | biniam-alaro | 0 | 0.5 | 0.333333 | 0.666667 | 1 | 4 |
| pyramidal | player_neg_rate | caleb-kendrick | 0 | 0.216071 | 0 | 0.483333 | 1 | 12 |
| pyramidal | player_neg_rate | cormac-beirne | 0 | 0.397778 | 0.14 | 0.766667 | 1 | 15 |
| pyramidal | player_neg_rate | daniel-chen | 0.666667 | 0.433333 | 0.333333 | 0.633333 | 0.2 | 5 |
| pyramidal | player_neg_rate | henry-bylinowski | 0.4 | 0.238095 | 0 | 0.333333 | 0 | 7 |
| pyramidal | player_neg_rate | jack-rado | 0 | 0.466667 | 0.25 | 0.9 | 1 | 5 |
| pyramidal | player_neg_rate | jason-zhang | 0 | 0.166667 | 0.0166667 | 0.316667 | 1 | 2 |
| pyramidal | player_neg_rate | jonathan-shauf | 0.333333 | 0.333333 | 0.333333 | 0.333333 | 1 | 1 |
| pyramidal | player_neg_rate | kevin-park | 0.333333 | 0.25 | 0.25 | 0.25 | 0 | 1 |
| pyramidal | player_neg_rate | liam-starnes | 0.333333 | 0.333333 | 0.0333333 | 0.633333 | 0.5 | 2 |
| pyramidal | player_neg_rate | malachi-ledford | 0 | 0.343137 | 0 | 0.683333 | 1 | 17 |
| pyramidal | player_neg_rate | michal-gerasimiuk | 0.666667 | 0.354167 | 0.0375 | 0.641667 | 0.25 | 4 |
| pyramidal | player_neg_rate | omer-keskin | 0 | 0.133333 | 0 | 0.313333 | 1 | 4 |
| pyramidal | player_neg_rate | orion-keller | 0 | 0.197917 | 0 | 0.55 | 1 | 8 |
| pyramidal | player_neg_rate | owen-ashbrook | 0 | 0.333333 | 0.333333 | 0.333333 | 1 | 1 |
| pyramidal | player_neg_rate | patrick-torre | 0 | 0.458333 | 0.333333 | 0.641667 | 1 | 4 |
| pyramidal | player_neg_rate | rohan-dalal | 0.25 | 0.45625 | 0.116667 | 0.720833 | 0.875 | 8 |
| pyramidal | player_neg_rate | rosie-zhang | 0.333333 | 0.333333 | 0.333333 | 0.333333 | 1 | 1 |
| pyramidal | player_neg_rate | sam-macchi | 0 | 0.387037 | 0.1 | 0.666667 | 1 | 9 |
| pyramidal | player_neg_rate | shardul-rao | 0.6 | 0.444444 | 0.333333 | 0.633333 | 0.333333 | 3 |
| pyramidal | player_neg_rate | sinecio-morales | 0 | 0.222222 | 0.0333333 | 0.333333 | 1 | 3 |
| pyramidal | player_neg_rate | teigue-kelly | 0.333333 | 0.333333 | 0.0333333 | 0.633333 | 0.5 | 2 |
| pyramidal | player_neg_rate | vedang-singhal | 0.333333 | 0.472222 | 0.0666667 | 0.741667 | 0.666667 | 3 |
| pyramidal | player_neg_rate | william-orr | 0 | 1 | 1 | 1 | 1 | 1 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.924131 | 0.934156 | 0.0100249 | synergy |
| log_loss | 0.358455 | 0.337141 | -0.0213141 | synergy |
| ece | 0.0366069 | 0.0389809 | 0.00237403 | no-synergy |
| brier | 0.111821 | 0.104816 | -0.00700466 | synergy |
| accuracy_lift_over_all_correct | 0.322806 | 0.332299 | 0.00949341 | synergy |
| part_accuracy | 0.843295 | 0.852788 | 0.00949341 | synergy |
| part_accuracy_macro_team | 0.845959 | 0.855759 | 0.00979968 | synergy |
| part_accuracy_macro_game | 0.843711 | 0.853329 | 0.00961888 | synergy |
| part_accuracy_macro_bonus | 0.851473 | 0.856721 | 0.00524836 | synergy |
| exact_acc | 0.590217 | 0.612471 | 0.0222537 | synergy |
| ranked_probability_score | 0.102047 | 0.0936624 | -0.00838462 | synergy |
| bonus_total_score_log_loss | 0.900859 | 0.843012 | -0.0578469 | synergy |
| ppb_mae | 1.97857 | 0.8459 | -1.13267 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.68045 | 1.30394 | 0.731054 | 1.73596 | 4.19295 | 5.02174 | 5.56052 | 6.24609 | 7.15366 |
| player | theta_1 | 1455 | 0.115039 | 0.695665 | -2.41226 | -1.22037 | -0.270111 | 0.243 | 0.603122 | 1.06939 | 2.23256 |
| player | theta_2 | 1455 | -0.0203654 | 0.692714 | -2.58165 | -1.32875 | -0.416677 | 0.0792803 | 0.454624 | 0.972191 | 1.65878 |
| player | theta_3 | 1455 | 0.223425 | 0.69601 | -2.37217 | -1.14487 | -0.144056 | 0.32958 | 0.682549 | 1.20679 | 2.01335 |
| player | theta_4 | 1455 | 0.197192 | 0.701928 | -2.34462 | -1.17706 | -0.171596 | 0.317264 | 0.682393 | 1.17815 | 2.05869 |
| player | theta_5 | 1455 | 0.102863 | 0.688775 | -2.48074 | -1.31463 | -0.223512 | 0.232589 | 0.570104 | 1.04999 | 1.49642 |
| player | theta_norm | 1455 | 1.49685 | 0.53513 | 0.313103 | 0.770904 | 1.11578 | 1.41445 | 1.78805 | 2.56688 | 3.73944 |
| tossup | beta_1 | 1260 | 0.75386 | 0.50755 | -0.269916 | 0.217192 | 0.402819 | 0.576452 | 0.996499 | 1.80215 | 3.15657 |
| tossup | beta_2 | 1260 | 0.823139 | 0.572711 | -0.771172 | 0.197318 | 0.406767 | 0.598564 | 1.23365 | 1.94104 | 2.84763 |
| tossup | beta_3 | 1260 | 0.746597 | 0.47966 | -2.02262 | 0.251657 | 0.416529 | 0.588712 | 0.999945 | 1.6894 | 3.16208 |
| tossup | beta_4 | 1260 | 0.773552 | 0.544487 | -0.171085 | 0.230685 | 0.403602 | 0.571358 | 1.01716 | 1.91385 | 2.96158 |
| tossup | beta_5 | 1260 | 0.8402 | 0.570014 | -0.277407 | 0.206236 | 0.420496 | 0.624319 | 1.22556 | 1.97669 | 2.75435 |
| tossup | gamma_1 | 1260 | 15.5697 | 80.0846 | 0.623047 | 2.8082 | 4.32795 | 5.01416 | 6.03307 | 23.3239 | 1942.2 |
| tossup | gamma_2 | 1260 | 15.3595 | 82.5995 | 0.494544 | 2.99061 | 4.44341 | 5.15771 | 6.45629 | 22.97 | 1974.56 |
| tossup | gamma_3 | 1260 | 15.1482 | 77.8332 | 0.171224 | 2.64148 | 4.25612 | 4.99416 | 5.85407 | 26.3665 | 1460.55 |
| tossup | gamma_4 | 1260 | 17.6657 | 98.759 | 1.4976 | 3.19 | 4.37174 | 5.04646 | 5.94868 | 25.5393 | 1908 |
| tossup | gamma_5 | 1260 | 19.9829 | 103.62 | 0.802431 | 2.88629 | 4.37677 | 5.11238 | 6.37212 | 33.4759 | 1689.8 |
| tossup | mu_1 | 1260 | 0.513077 | 0.121231 | 0.106669 | 0.381981 | 0.448275 | 0.478352 | 0.542595 | 0.778243 | 0.990437 |
| tossup | mu_2 | 1260 | 0.526976 | 0.136936 | 0.200462 | 0.384058 | 0.441437 | 0.479151 | 0.580221 | 0.829326 | 0.992815 |
| tossup | mu_3 | 1260 | 0.517563 | 0.12219 | 0.198635 | 0.38056 | 0.452283 | 0.48327 | 0.549728 | 0.776276 | 0.993123 |
| tossup | mu_4 | 1260 | 0.525609 | 0.133037 | 0.212308 | 0.397665 | 0.4519 | 0.482223 | 0.542655 | 0.842054 | 0.9922 |
| tossup | mu_5 | 1260 | 0.530009 | 0.132192 | 0.246926 | 0.380927 | 0.45004 | 0.487462 | 0.5839 | 0.824791 | 0.992469 |
| tossup | r_1 | 1260 | 1.018 | 0.759211 | 0.094088 | 0.207175 | 0.426623 | 0.771701 | 1.45027 | 2.49611 | 4.54458 |
| tossup | r_2 | 1260 | 1.26093 | 1.04043 | 0.0757528 | 0.224094 | 0.484236 | 0.90689 | 1.75152 | 3.51225 | 5.72897 |
| tossup | r_3 | 1260 | 1.22168 | 1.0695 | 0.108067 | 0.225141 | 0.461369 | 0.880079 | 1.59127 | 3.57006 | 7.05776 |
| tossup | r_4 | 1260 | 1.11999 | 1.02767 | 0.0663415 | 0.218774 | 0.422799 | 0.721337 | 1.35488 | 3.42905 | 5.85462 |
| tossup | r_5 | 1260 | 1.27163 | 0.971807 | 0.0831754 | 0.245104 | 0.495484 | 0.937523 | 1.87677 | 3.12963 | 6.09509 |
| tossup | r_norm | 1260 | 3.3037 | 0.935877 | 1.06694 | 1.98874 | 2.65468 | 3.17155 | 3.80947 | 5.08156 | 8.14425 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.786552 | 1.41718 | -2.15393 | -1.62089 | -0.400261 | 1.03804 | 1.96932 | 2.7658 | 3.73263 |
| bonus_part | alpha_1 | 3768 | 0.129995 | 0.435336 | -1.58779 | -0.560477 | -0.157913 | 0.117995 | 0.41844 | 0.831837 | 2.09678 |
| bonus_part | alpha_2 | 3768 | 0.21824 | 0.46892 | -1.5509 | -0.498144 | -0.0651887 | 0.195419 | 0.48604 | 1.01654 | 2.52383 |
| bonus_part | alpha_3 | 3768 | 0.169692 | 0.585729 | -1.39568 | -0.711351 | -0.243701 | 0.121025 | 0.56753 | 1.14481 | 2.40833 |
| bonus_part | alpha_4 | 3768 | 0.104027 | 0.551238 | -1.7764 | -0.751863 | -0.294759 | 0.0768203 | 0.521712 | 0.992426 | 2.21526 |
| bonus_part | alpha_5 | 3768 | 0.150018 | 0.443712 | -1.43991 | -0.53531 | -0.144573 | 0.12593 | 0.434922 | 0.896414 | 2.0394 |
| bonus_part | alpha_norm | 3768 | 1.07322 | 0.477285 | 0.0967737 | 0.362639 | 0.692971 | 1.05415 | 1.39602 | 1.90857 | 2.81868 |
