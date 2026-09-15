# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_6/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_6/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 336814 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.567186 |
| log_loss | 0.580373 |
| ece | 0.0838063 |
| brier | 0.187521 |
| accuracy | 0.760145 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00197954 |
| probability_std | 0.11583 |
| probability_p10 | 0.641898 |
| probability_p50 | 0.860649 |
| probability_p90 | 0.933745 |
| mean_predictive_variance | 0.133502 |
| integrated_brier_score | 0.173177 |
| joint_tossup_event_log_loss | 7.70704 |
| buzz_position_mae | 0.334126 |
| buzz_position_median_absolute_error | 0.338685 |
| buzz_position_bias | -0.320191 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.319586 |
| first_buzzer_mean_reciprocal_rank | 0.538646 |
| first_buzzer_log_loss | 1.71729 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.619488 |
| tossup_scorer_player_top1_accuracy | 0.269481 |
| tossup_scorer_team_top1_accuracy | 0.385065 |
| tossup_game_winner_accuracy | 0.720721 |
| tossup_game_margin_mae | 43.3735 |
| tournament_player_ppg_spearman | 0.560972 |
| tournament_player_ppg_mae | 10.5725 |
| tournament_player_ppg_top10_overlap | 0.565517 |
| neg_auroc | 0.567186 |
| neg_average_precision | 0.294803 |
| neg_precision | 0.425 |
| neg_recall | 0.0235784 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0333597 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.219975 |
| no_buzz_calibration_error | 0.204066 |
| no_buzz_brier | 0.0646807 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.567186 | 0.580373 | 0.0838063 | 0.187521 | 0.760145 | 0.762125 | -0.00197954 | 0.11583 | 0.641898 | 0.860649 | 0.933745 | 0.133502 |
| tossup_correctness | tier | fall | 2842 | 0.568743 | 0.542134 | 0.074207 | 0.172984 | 0.784659 | 0.785362 | -0.00070373 | 0.0922628 | 0.721065 | 0.873059 | 0.931909 | 0.122083 |
| tossup_correctness | tier | nationals | 1564 | 0.561387 | 0.615486 | 0.0827602 | 0.208588 | 0.712276 | 0.718031 | -0.00575448 | 0.134343 | 0.541377 | 0.708457 | 0.908289 | 0.184608 |
| tossup_correctness | tier | regionals | 1937 | 0.549035 | 0.586776 | 0.0813704 | 0.189396 | 0.754775 | 0.758389 | -0.00361384 | 0.116176 | 0.636263 | 0.836879 | 0.930407 | 0.142611 |
| tossup_correctness | tier | winter | 2750 | 0.561047 | 0.595413 | 0.106538 | 0.189241 | 0.765818 | 0.765818 | 0 | 0.0837265 | 0.745367 | 0.890305 | 0.94201 | 0.109821 |
| tossup_correctness | category | Current Events | 126 | 0.509421 | 0.588315 | 0.0957285 | 0.193334 | 0.738095 | 0.769841 | -0.031746 | 0.125926 | 0.591127 | 0.832962 | 0.912238 | 0.14879 |
| tossup_correctness | category | Fine Arts | 1071 | 0.587747 | 0.574523 | 0.0962558 | 0.184788 | 0.764706 | 0.766573 | -0.00186741 | 0.113174 | 0.654976 | 0.878145 | 0.938899 | 0.124632 |
| tossup_correctness | category | Geography | 185 | 0.543605 | 0.704987 | 0.167387 | 0.236056 | 0.691892 | 0.697297 | -0.00540541 | 0.123909 | 0.631521 | 0.870817 | 0.929181 | 0.131271 |
| tossup_correctness | category | History | 1440 | 0.556502 | 0.594317 | 0.0938826 | 0.193791 | 0.75625 | 0.754167 | 0.00208333 | 0.113395 | 0.64146 | 0.856375 | 0.928341 | 0.136387 |
| tossup_correctness | category | Literature | 1422 | 0.552608 | 0.507106 | 0.0686625 | 0.156327 | 0.808017 | 0.814346 | -0.00632911 | 0.107495 | 0.670835 | 0.882871 | 0.944481 | 0.120223 |
| tossup_correctness | category | Mythology | 318 | 0.584765 | 0.535691 | 0.087638 | 0.170741 | 0.795597 | 0.789308 | 0.00628931 | 0.106178 | 0.669187 | 0.879002 | 0.932073 | 0.122989 |
| tossup_correctness | category | Other Academic | 66 | 0.486002 | 0.723376 | 0.230006 | 0.244119 | 0.712121 | 0.712121 | 0 | 0.138175 | 0.58699 | 0.852479 | 0.924582 | 0.149899 |
| tossup_correctness | category | Philosophy | 311 | 0.58457 | 0.608018 | 0.121199 | 0.195781 | 0.745981 | 0.745981 | 0 | 0.116317 | 0.639292 | 0.87685 | 0.94151 | 0.124108 |
| tossup_correctness | category | Popular Culture | 102 | 0.581481 | 0.382747 | 0.0413126 | 0.112827 | 0.862745 | 0.882353 | -0.0196078 | 0.0893658 | 0.753834 | 0.856624 | 0.923204 | 0.125705 |
| tossup_correctness | category | Religion | 358 | 0.568894 | 0.671073 | 0.147477 | 0.224013 | 0.706704 | 0.712291 | -0.00558659 | 0.123361 | 0.625496 | 0.870542 | 0.930395 | 0.132857 |
| tossup_correctness | category | Science | 1433 | 0.581674 | 0.5979 | 0.0816064 | 0.196834 | 0.7418 | 0.738311 | 0.00348918 | 0.120506 | 0.622874 | 0.839281 | 0.926003 | 0.141743 |
| tossup_correctness | category | Social Science | 324 | 0.579951 | 0.619456 | 0.0971964 | 0.203418 | 0.728395 | 0.731481 | -0.00308642 | 0.112394 | 0.645587 | 0.873077 | 0.927344 | 0.131849 |
| tossup_correctness | category | Unknown | 1937 | 0.549035 | 0.586776 | 0.0813704 | 0.189396 | 0.754775 | 0.758389 | -0.00361384 | 0.116176 | 0.636263 | 0.836879 | 0.930407 | 0.142611 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.56215 | 0.630893 | 0.0912304 | 0.211505 | 0.700599 | 0.712575 | -0.011976 | 0.116665 | 0.632002 | 0.807488 | 0.90533 | 0.156973 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.569706 | 0.608207 | 0.078604 | 0.203192 | 0.72807 | 0.729167 | -0.00109649 | 0.115148 | 0.623665 | 0.83012 | 0.907077 | 0.150201 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.532834 | 0.595229 | 0.0974731 | 0.194524 | 0.752719 | 0.755083 | -0.00236407 | 0.109733 | 0.645227 | 0.846884 | 0.920964 | 0.139373 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.573515 | 0.547258 | 0.0737125 | 0.175496 | 0.779536 | 0.780942 | -0.00140647 | 0.112185 | 0.649106 | 0.869397 | 0.930671 | 0.131271 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.573903 | 0.589846 | 0.0892482 | 0.187877 | 0.760065 | 0.762029 | -0.00196399 | 0.121281 | 0.640275 | 0.881532 | 0.944655 | 0.125245 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1167 | -1.04788 | 1.01699 | -3.45564 | -2.44938 | -1.69369 | -1.23787 | -0.623665 | 1.17476 | 2.13758 |
| player | beta | 1167 | -4.12009 | 1.30471 | -7.22117 | -6.68267 | -4.95586 | -3.85989 | -3.10502 | -2.43697 | -2.04771 |
| player | theta_1 | 1167 | 0.635147 | 0.733007 | -2.11236 | -0.767454 | 0.208825 | 0.785951 | 1.15475 | 1.60805 | 2.68036 |
| player | theta_2 | 1167 | 0.675557 | 0.87742 | -2.20843 | -0.951743 | 0.0861287 | 0.863973 | 1.34916 | 1.85205 | 2.45018 |
| player | theta_3 | 1167 | 0.672626 | 0.834345 | -2.07985 | -0.880648 | 0.175009 | 0.828495 | 1.25958 | 1.83892 | 2.73762 |
| player | theta_4 | 1167 | 0.661133 | 0.82236 | -1.94271 | -0.873731 | 0.172843 | 0.76964 | 1.26066 | 1.80821 | 2.61326 |
| player | theta_5 | 1167 | 0.58651 | 0.631855 | -1.73846 | -0.656851 | 0.289111 | 0.695758 | 0.977393 | 1.41236 | 2.79282 |
| player | theta_6 | 1167 | 0.596153 | 0.627813 | -1.61022 | -0.65864 | 0.304832 | 0.712238 | 1.00561 | 1.40145 | 2.57689 |
| player | theta_norm | 1167 | 2.29414 | 0.810049 | 0.17349 | 0.809095 | 1.78331 | 2.3741 | 2.82835 | 3.53401 | 4.99224 |
| tossup | start_difficulty_d1 | 1220 | -0.70325 | 0.373735 | -1.7795 | -1.33298 | -0.96362 | -0.713463 | -0.411022 | -0.116417 | 0.319907 |
| tossup | start_difficulty_d2 | 1220 | -0.712405 | 0.398119 | -1.88768 | -1.40029 | -0.978131 | -0.705727 | -0.38417 | -0.127537 | 0.348539 |
| tossup | start_difficulty_d3 | 1220 | -0.722135 | 0.466622 | -2.19437 | -1.63075 | -1.024 | -0.643072 | -0.38603 | -0.0604669 | 0.31567 |
| tossup | start_difficulty_d4 | 1220 | -0.700763 | 0.412301 | -1.89386 | -1.3987 | -1.00518 | -0.692773 | -0.374245 | -0.0725289 | 0.248126 |
| tossup | start_difficulty_d5 | 1220 | -0.653269 | 0.358747 | -1.64295 | -1.23789 | -0.91733 | -0.664678 | -0.375062 | -0.0496247 | 0.325335 |
| tossup | start_difficulty_d6 | 1220 | -0.661485 | 0.377324 | -1.883 | -1.2899 | -0.927383 | -0.650245 | -0.379662 | -0.057629 | 0.32132 |
| tossup | end_difficulty_d1 | 1220 | -1.59265 | 0.331515 | -2.60282 | -2.1342 | -1.82152 | -1.58464 | -1.38507 | -1.02866 | -0.410853 |
| tossup | end_difficulty_d2 | 1220 | -1.58668 | 0.326304 | -2.48504 | -2.0957 | -1.8238 | -1.59031 | -1.37067 | -1.05027 | -0.246333 |
| tossup | end_difficulty_d3 | 1220 | -1.61063 | 0.403478 | -2.80942 | -2.31091 | -1.87099 | -1.56689 | -1.33241 | -0.983581 | -0.469835 |
| tossup | end_difficulty_d4 | 1220 | -1.59249 | 0.356405 | -2.72937 | -2.16368 | -1.85892 | -1.59558 | -1.34433 | -0.995109 | -0.524544 |
| tossup | end_difficulty_d5 | 1220 | -1.56383 | 0.332729 | -2.36979 | -2.09277 | -1.80123 | -1.5633 | -1.35031 | -0.981626 | -0.425596 |
| tossup | end_difficulty_d6 | 1220 | -1.56962 | 0.348151 | -2.52761 | -2.14451 | -1.81283 | -1.54455 | -1.34429 | -0.986934 | -0.46832 |
| tossup | total_drop_d1 | 1220 | 0.889398 | 0.183103 | 0.396439 | 0.611571 | 0.758807 | 0.871466 | 1.02362 | 1.18113 | 1.46673 |
| tossup | total_drop_d2 | 1220 | 0.874278 | 0.199048 | 0.301285 | 0.500219 | 0.751887 | 0.875049 | 1.02464 | 1.16915 | 1.33326 |
| tossup | total_drop_d3 | 1220 | 0.888495 | 0.202701 | 0.335144 | 0.538476 | 0.757001 | 0.882421 | 1.03206 | 1.22017 | 1.51372 |
| tossup | total_drop_d4 | 1220 | 0.891726 | 0.196215 | 0.35503 | 0.539455 | 0.772313 | 0.889581 | 1.02871 | 1.20624 | 1.44317 |
| tossup | total_drop_d5 | 1220 | 0.910556 | 0.164135 | 0.431097 | 0.681961 | 0.786516 | 0.882869 | 1.03062 | 1.19669 | 1.46834 |
| tossup | total_drop_d6 | 1220 | 0.908136 | 0.164444 | 0.475916 | 0.681019 | 0.781172 | 0.882836 | 1.02997 | 1.20145 | 1.44115 |
| tossup | drop_share_1_d1 | 1220 | 0.312379 | 0.0169387 | 0.24918 | 0.286728 | 0.301186 | 0.311044 | 0.323595 | 0.341401 | 0.378782 |
| tossup | drop_share_2_d1 | 1220 | 0.336746 | 0.0137917 | 0.287628 | 0.313004 | 0.328167 | 0.337111 | 0.345889 | 0.358702 | 0.380116 |
| tossup | drop_share_3_d1 | 1220 | 0.350875 | 0.0177554 | 0.296941 | 0.323741 | 0.339106 | 0.349775 | 0.361332 | 0.381478 | 0.428589 |
| tossup | drop_share_1_d2 | 1220 | 0.312687 | 0.0176403 | 0.254049 | 0.285401 | 0.300576 | 0.31177 | 0.324171 | 0.342004 | 0.377702 |
| tossup | drop_share_2_d2 | 1220 | 0.335637 | 0.0158909 | 0.264145 | 0.307179 | 0.326897 | 0.337295 | 0.346707 | 0.358806 | 0.377559 |
| tossup | drop_share_3_d2 | 1220 | 0.351676 | 0.0204365 | 0.295425 | 0.323346 | 0.338572 | 0.34901 | 0.361852 | 0.389576 | 0.432606 |
| tossup | drop_share_1_d3 | 1220 | 0.312989 | 0.0210835 | 0.23378 | 0.283294 | 0.300007 | 0.310092 | 0.323018 | 0.351702 | 0.410147 |
| tossup | drop_share_2_d3 | 1220 | 0.336488 | 0.0149255 | 0.275554 | 0.310844 | 0.327394 | 0.337643 | 0.346955 | 0.359338 | 0.377724 |
| tossup | drop_share_3_d3 | 1220 | 0.350523 | 0.0201916 | 0.268608 | 0.319148 | 0.338507 | 0.350503 | 0.361069 | 0.384784 | 0.441977 |
| tossup | drop_share_1_d4 | 1220 | 0.312057 | 0.0188941 | 0.219757 | 0.282881 | 0.300056 | 0.311662 | 0.322542 | 0.343059 | 0.393108 |
| tossup | drop_share_2_d4 | 1220 | 0.336075 | 0.0151057 | 0.268555 | 0.307929 | 0.327646 | 0.337714 | 0.346326 | 0.35778 | 0.37549 |
| tossup | drop_share_3_d4 | 1220 | 0.351868 | 0.0207945 | 0.295924 | 0.324309 | 0.339389 | 0.349985 | 0.36059 | 0.386375 | 0.472486 |
| tossup | drop_share_1_d5 | 1220 | 0.311656 | 0.0167504 | 0.255073 | 0.28393 | 0.300605 | 0.311518 | 0.322726 | 0.339555 | 0.373469 |
| tossup | drop_share_2_d5 | 1220 | 0.337819 | 0.013019 | 0.30151 | 0.315583 | 0.329261 | 0.337989 | 0.34689 | 0.358133 | 0.374714 |
| tossup | drop_share_3_d5 | 1220 | 0.350525 | 0.0168867 | 0.29673 | 0.323027 | 0.338904 | 0.350749 | 0.361271 | 0.377541 | 0.412416 |
| tossup | drop_share_1_d6 | 1220 | 0.31226 | 0.0172992 | 0.261746 | 0.285329 | 0.3008 | 0.311413 | 0.323313 | 0.340679 | 0.387785 |
| tossup | drop_share_2_d6 | 1220 | 0.337808 | 0.013002 | 0.290083 | 0.316327 | 0.329471 | 0.337706 | 0.34676 | 0.358153 | 0.385595 |
| tossup | drop_share_3_d6 | 1220 | 0.349931 | 0.0169248 | 0.297771 | 0.322232 | 0.339152 | 0.349494 | 0.359981 | 0.378468 | 0.414055 |
| tossup | r_1 | 1220 | 0.150361 | 0.0719853 | 0.0399255 | 0.0690761 | 0.110757 | 0.136743 | 0.166402 | 0.289045 | 0.567405 |
| tossup | r_2 | 1220 | 0.173868 | 0.122726 | 0.0400925 | 0.0725827 | 0.107429 | 0.131145 | 0.182183 | 0.473056 | 0.77074 |
| tossup | r_3 | 1220 | 0.176804 | 0.104658 | 0.0363978 | 0.0578944 | 0.120298 | 0.161209 | 0.189089 | 0.421559 | 0.687538 |
| tossup | r_4 | 1220 | 0.178898 | 0.106216 | 0.036511 | 0.0628089 | 0.124812 | 0.163955 | 0.19232 | 0.399141 | 0.761559 |
| tossup | r_5 | 1220 | 0.159644 | 0.0482777 | 0.04791 | 0.0722001 | 0.124775 | 0.170446 | 0.194679 | 0.223056 | 0.432544 |
| tossup | r_6 | 1220 | 0.160427 | 0.0453522 | 0.0456568 | 0.0713851 | 0.131907 | 0.175013 | 0.193839 | 0.210669 | 0.366388 |
| tossup | r_norm | 1220 | 0.457383 | 0.0704121 | 0.40853 | 0.41032 | 0.414617 | 0.422761 | 0.470422 | 0.620414 | 0.777694 |
