# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/evaluation`
Result root: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| compositional | tournament | all tournaments |
| compositional | dimensions | 3 |
| compositional | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.57755 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.891023 |
| log_loss | 0.417147 |
| ece | 0.0233032 |
| brier | 0.13338 |
| part_accuracy | 0.809026 |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.290024 |
| part_accuracy_macro_team | 0.812057 |
| part_accuracy_macro_bonus | 0.805723 |
| probability_std | 0.343838 |
| probability_p10 | 0.0587158 |
| probability_p50 | 0.542228 |
| probability_p90 | 0.957796 |
| mean_predictive_variance | 0.131007 |
| exact_acc | 0.515202 |
| ranked_probability_score | 0.115706 |
| bonus_total_score_log_loss | 1.01345 |
| ppb_mae | 2.41632 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

## Stage 1 Tossup Metrics

No tossup metrics CSV was found.

## Tossup Game Replay

No tossup game replay metrics CSV was found.

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25260 | 0.891023 | 0.417147 | 0.0233032 | 0.13338 | 0.809026 | 0.519002 | 0.290024 | 0.343838 | 0.0587158 | 0.542228 | 0.957796 | 0.131007 |
| bonus_part_correctness | tier | fall | 8160 | 0.886842 | 0.413321 | 0.0193744 | 0.132944 | 0.808211 | 0.608701 | 0.19951 | 0.32988 | 0.103287 | 0.669037 | 0.968711 | 0.130731 |
| bonus_part_correctness | tier | nationals | 4107 | 0.891366 | 0.414498 | 0.0382807 | 0.131175 | 0.812028 | 0.411493 | 0.400536 | 0.333854 | 0.0424239 | 0.404634 | 0.913411 | 0.13588 |
| bonus_part_correctness | tier | regionals | 5280 | 0.879643 | 0.437088 | 0.0366536 | 0.141381 | 0.796402 | 0.48125 | 0.315152 | 0.343704 | 0.0474423 | 0.484698 | 0.948814 | 0.131864 |
| bonus_part_correctness | tier | winter | 7713 | 0.894982 | 0.408955 | 0.0290083 | 0.129537 | 0.816932 | 0.507196 | 0.309737 | 0.348925 | 0.0498127 | 0.504436 | 0.95785 | 0.128118 |
| bonus_part_correctness | category | Current Events | 249 | 0.902893 | 0.395959 | 0.078478 | 0.122212 | 0.835341 | 0.514056 | 0.321285 | 0.360078 | 0.0597496 | 0.594132 | 0.94563 | 0.119971 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.877044 | 0.440824 | 0.0163961 | 0.141632 | 0.798909 | 0.507157 | 0.291752 | 0.335591 | 0.0641686 | 0.504362 | 0.951869 | 0.137246 |
| bonus_part_correctness | category | Geography | 459 | 0.88328 | 0.416087 | 0.0632518 | 0.132961 | 0.803922 | 0.618736 | 0.185185 | 0.329803 | 0.0914296 | 0.692096 | 0.952867 | 0.131793 |
| bonus_part_correctness | category | History | 4017 | 0.898324 | 0.402537 | 0.0272422 | 0.128774 | 0.812049 | 0.552153 | 0.259895 | 0.341826 | 0.0681018 | 0.618021 | 0.963029 | 0.129441 |
| bonus_part_correctness | category | Literature | 4047 | 0.898568 | 0.402674 | 0.029497 | 0.12711 | 0.825303 | 0.50556 | 0.319743 | 0.348904 | 0.0561049 | 0.517546 | 0.961568 | 0.127931 |
| bonus_part_correctness | category | Mythology | 924 | 0.872785 | 0.434644 | 0.0323469 | 0.141037 | 0.794372 | 0.619048 | 0.175325 | 0.320622 | 0.120597 | 0.664105 | 0.964455 | 0.134855 |
| bonus_part_correctness | category | Other Academic | 237 | 0.920767 | 0.382916 | 0.0712301 | 0.119662 | 0.843882 | 0.481013 | 0.362869 | 0.349987 | 0.0686686 | 0.608045 | 0.965804 | 0.12478 |
| bonus_part_correctness | category | Philosophy | 948 | 0.885542 | 0.429332 | 0.0442088 | 0.136013 | 0.806962 | 0.494726 | 0.312236 | 0.333873 | 0.0549823 | 0.512268 | 0.946523 | 0.13848 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.890941 | 0.39487 | 0.0659048 | 0.128562 | 0.823129 | 0.673469 | 0.14966 | 0.31345 | 0.12777 | 0.661512 | 0.96942 | 0.137751 |
| bonus_part_correctness | category | Religion | 984 | 0.901904 | 0.39906 | 0.0285906 | 0.124977 | 0.829268 | 0.513211 | 0.316057 | 0.351631 | 0.0468272 | 0.5226 | 0.957241 | 0.126002 |
| bonus_part_correctness | category | Science | 3990 | 0.892535 | 0.414899 | 0.0276538 | 0.132832 | 0.806767 | 0.52807 | 0.278697 | 0.342697 | 0.0696447 | 0.545885 | 0.958865 | 0.131245 |
| bonus_part_correctness | category | Social Science | 897 | 0.911224 | 0.374766 | 0.0368335 | 0.117709 | 0.816054 | 0.490524 | 0.32553 | 0.358816 | 0.0306099 | 0.441875 | 0.961937 | 0.121116 |
| bonus_part_correctness | category | Unknown | 5280 | 0.879643 | 0.437088 | 0.0366536 | 0.141381 | 0.796402 | 0.48125 | 0.315152 | 0.343704 | 0.0474423 | 0.484698 | 0.948814 | 0.131864 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

No bonus model comparison CSV was found.

## Pyramidal Player And Tossup Parameters

No pyramidal parameter distribution summary CSV was found.

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum | parameter_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.220304 | 1.23028 | -2.73395 | -2.26564 | -1.25691 | -0.146349 | 0.821451 | 1.5754 | 2.2357 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/compositional |
| bonus_part | alpha_1 | 3768 | 0.806867 | 0.448062 | 0.201086 | 0.301683 | 0.432307 | 0.694023 | 1.10147 | 1.65747 | 3.35968 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/compositional |
| bonus_part | alpha_2 | 3768 | 0.753215 | 0.405879 | 0.194275 | 0.327727 | 0.425484 | 0.619715 | 1.00118 | 1.57288 | 2.58196 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/compositional |
| bonus_part | alpha_3 | 3768 | 0.756537 | 0.392309 | 0.177838 | 0.312645 | 0.448606 | 0.664336 | 0.979338 | 1.5041 | 2.98012 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/compositional |
| bonus_part | alpha_norm | 3768 | 1.40128 | 0.588622 | 0.476482 | 0.593581 | 0.852181 | 1.36748 | 1.86085 | 2.37235 | 3.44708 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/compositional |
