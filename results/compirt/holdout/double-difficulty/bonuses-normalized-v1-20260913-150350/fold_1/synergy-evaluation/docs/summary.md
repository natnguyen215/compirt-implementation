# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/synergy-evaluation`
Result root: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 3 |
| synergy | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.54431 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.899831 |
| log_loss | 0.401246 |
| ece | 0.0172029 |
| brier | 0.127255 |
| part_accuracy | 0.818606 |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.299604 |
| part_accuracy_macro_team | 0.821936 |
| part_accuracy_macro_bonus | 0.81682 |
| probability_std | 0.350947 |
| probability_p10 | 0.0525036 |
| probability_p50 | 0.543052 |
| probability_p90 | 0.964078 |
| mean_predictive_variance | 0.126142 |
| exact_acc | 0.534679 |
| ranked_probability_score | 0.10907 |
| bonus_total_score_log_loss | 0.968068 |
| ppb_mae | 1.76101 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

## Stage 1 Tossup Metrics

No tossup metrics CSV was found.

## Tossup Game Replay

No tossup game replay metrics CSV was found.

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25260 | 0.899831 | 0.401246 | 0.0172029 | 0.127255 | 0.818606 | 0.519002 | 0.299604 | 0.350947 | 0.0525036 | 0.543052 | 0.964078 | 0.126142 |
| bonus_part_correctness | tier | fall | 8160 | 0.894265 | 0.401984 | 0.015114 | 0.127851 | 0.816667 | 0.608701 | 0.207966 | 0.34116 | 0.0867097 | 0.692764 | 0.977561 | 0.122103 |
| bonus_part_correctness | tier | nationals | 4107 | 0.902587 | 0.392414 | 0.0346544 | 0.122966 | 0.826881 | 0.411493 | 0.415388 | 0.33286 | 0.0462542 | 0.371306 | 0.910794 | 0.135267 |
| bonus_part_correctness | tier | regionals | 5280 | 0.893531 | 0.411894 | 0.0226261 | 0.13138 | 0.81572 | 0.48125 | 0.33447 | 0.345928 | 0.0414219 | 0.477653 | 0.948773 | 0.130255 |
| bonus_part_correctness | tier | winter | 7713 | 0.901206 | 0.39788 | 0.02383 | 0.126084 | 0.818229 | 0.507196 | 0.311033 | 0.356521 | 0.0424667 | 0.505965 | 0.964738 | 0.12274 |
| bonus_part_correctness | category | Current Events | 249 | 0.903732 | 0.396085 | 0.0451625 | 0.123349 | 0.831325 | 0.514056 | 0.317269 | 0.366032 | 0.0583529 | 0.562373 | 0.965676 | 0.115009 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.88247 | 0.432226 | 0.0222558 | 0.139049 | 0.795501 | 0.507157 | 0.288344 | 0.343107 | 0.0580661 | 0.518624 | 0.960913 | 0.13206 |
| bonus_part_correctness | category | Geography | 459 | 0.881388 | 0.418266 | 0.0182585 | 0.135083 | 0.803922 | 0.618736 | 0.185185 | 0.335046 | 0.0847876 | 0.719655 | 0.96554 | 0.12648 |
| bonus_part_correctness | category | History | 4017 | 0.905099 | 0.389486 | 0.0222262 | 0.123697 | 0.825492 | 0.552153 | 0.273338 | 0.349862 | 0.0611554 | 0.617101 | 0.970111 | 0.123928 |
| bonus_part_correctness | category | Literature | 4047 | 0.908217 | 0.385154 | 0.0182228 | 0.120212 | 0.830986 | 0.50556 | 0.325426 | 0.357803 | 0.0498061 | 0.517086 | 0.967352 | 0.121701 |
| bonus_part_correctness | category | Mythology | 924 | 0.869974 | 0.441613 | 0.0343074 | 0.143515 | 0.792208 | 0.619048 | 0.17316 | 0.331061 | 0.103739 | 0.686779 | 0.973431 | 0.127358 |
| bonus_part_correctness | category | Other Academic | 237 | 0.913707 | 0.388672 | 0.0613119 | 0.120847 | 0.835443 | 0.481013 | 0.35443 | 0.36044 | 0.056901 | 0.617798 | 0.968483 | 0.118292 |
| bonus_part_correctness | category | Philosophy | 948 | 0.896235 | 0.408115 | 0.0383651 | 0.12853 | 0.811181 | 0.494726 | 0.316456 | 0.342308 | 0.0538402 | 0.495448 | 0.956296 | 0.132825 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.88568 | 0.401495 | 0.046092 | 0.130003 | 0.819728 | 0.673469 | 0.146259 | 0.325473 | 0.111795 | 0.719119 | 0.978084 | 0.126443 |
| bonus_part_correctness | category | Religion | 984 | 0.904252 | 0.39498 | 0.0193114 | 0.123738 | 0.822154 | 0.513211 | 0.308943 | 0.357616 | 0.0446726 | 0.533139 | 0.963394 | 0.121711 |
| bonus_part_correctness | category | Science | 3990 | 0.903547 | 0.394477 | 0.0195673 | 0.124617 | 0.820301 | 0.52807 | 0.292231 | 0.35003 | 0.0570431 | 0.549322 | 0.966399 | 0.126209 |
| bonus_part_correctness | category | Social Science | 897 | 0.924861 | 0.346612 | 0.0371585 | 0.107474 | 0.847269 | 0.490524 | 0.356745 | 0.368861 | 0.0294115 | 0.436375 | 0.967078 | 0.113659 |
| bonus_part_correctness | category | Unknown | 5280 | 0.893531 | 0.411894 | 0.0226261 | 0.13138 | 0.81572 | 0.48125 | 0.33447 | 0.345928 | 0.0414219 | 0.477653 | 0.948773 | 0.130255 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

No bonus model comparison CSV was found.

## Pyramidal Player And Tossup Parameters

No pyramidal parameter distribution summary CSV was found.

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum | parameter_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.205758 | 1.20891 | -2.7136 | -2.20724 | -1.25059 | -0.123793 | 0.822744 | 1.55167 | 2.32414 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/synergy |
| bonus_part | alpha_1 | 3768 | 0.838363 | 0.464406 | 0.220565 | 0.312026 | 0.442301 | 0.722218 | 1.15169 | 1.6997 | 3.46614 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/synergy |
| bonus_part | alpha_2 | 3768 | 0.814116 | 0.43319 | 0.222847 | 0.344824 | 0.45329 | 0.6893 | 1.09261 | 1.64642 | 2.87883 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/synergy |
| bonus_part | alpha_3 | 3768 | 0.794035 | 0.399465 | 0.180107 | 0.324995 | 0.470203 | 0.708959 | 1.03905 | 1.55013 | 2.89263 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/synergy |
| bonus_part | alpha_norm | 3768 | 1.47397 | 0.621607 | 0.506547 | 0.608083 | 0.897152 | 1.4557 | 1.95996 | 2.48773 | 3.61856 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/synergy |
| synergy_player | psi_1 | 1455 | 0.000568923 | 0.421365 | -1.393 | -0.673561 | -0.273098 | -0.00356284 | 0.266138 | 0.662165 | 1.60762 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/synergy |
| synergy_player | psi_norm | 1455 | 0.315643 | 0.279015 | 0.000271813 | 0.0107486 | 0.0766814 | 0.270082 | 0.456279 | 0.851477 | 1.60762 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/synergy |
| synergy | synergy_score | 2512 | 0.0281027 | 0.227338 | -1.43618 | -0.348946 | -0.0101564 | 0.011298 | 0.114536 | 0.327686 | 2.45758 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/synergy |
| synergy | synergy_contribution | 36067 | 0.242022 | 0.623719 | -1.59145 | -0.835498 | -0.0563311 | 0.0712747 | 0.62235 | 1.40378 | 2.49165 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_1/train/synergy |
