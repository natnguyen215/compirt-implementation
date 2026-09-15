# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/synergy-evaluation`
Result root: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2`

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
| tau | 1.51519 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.896414 |
| log_loss | 0.407479 |
| ece | 0.0166293 |
| brier | 0.129425 |
| part_accuracy | 0.814431 |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.295064 |
| part_accuracy_macro_team | 0.816324 |
| part_accuracy_macro_bonus | 0.813061 |
| probability_std | 0.352185 |
| probability_p10 | 0.0496652 |
| probability_p50 | 0.531951 |
| probability_p90 | 0.964646 |
| mean_predictive_variance | 0.125527 |
| exact_acc | 0.527277 |
| ranked_probability_score | 0.111169 |
| bonus_total_score_log_loss | 0.987443 |
| ppb_mae | 1.67884 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

## Stage 1 Tossup Metrics

No tossup metrics CSV was found.

## Tossup Game Replay

No tossup game replay metrics CSV was found.

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25791 | 0.896414 | 0.407479 | 0.0166293 | 0.129425 | 0.814431 | 0.519367 | 0.295064 | 0.352185 | 0.0496652 | 0.531951 | 0.964646 | 0.125527 |
| bonus_part_correctness | tier | fall | 7995 | 0.90039 | 0.392493 | 0.0222194 | 0.125934 | 0.814259 | 0.595122 | 0.219137 | 0.344004 | 0.0834882 | 0.689256 | 0.977398 | 0.121175 |
| bonus_part_correctness | tier | nationals | 4095 | 0.894513 | 0.405168 | 0.0159406 | 0.128125 | 0.819536 | 0.425153 | 0.394383 | 0.333907 | 0.049978 | 0.357272 | 0.912613 | 0.13433 |
| bonus_part_correctness | tier | regionals | 5580 | 0.896184 | 0.407131 | 0.0186198 | 0.129485 | 0.81828 | 0.495878 | 0.322401 | 0.344474 | 0.0419873 | 0.466049 | 0.946135 | 0.131225 |
| bonus_part_correctness | tier | winter | 8121 | 0.889427 | 0.423636 | 0.023337 | 0.133475 | 0.809383 | 0.508435 | 0.300948 | 0.358483 | 0.0372393 | 0.498419 | 0.965399 | 0.121459 |
| bonus_part_correctness | category | Current Events | 216 | 0.920362 | 0.357315 | 0.051059 | 0.112097 | 0.861111 | 0.467593 | 0.393519 | 0.367987 | 0.0321163 | 0.435442 | 0.957865 | 0.114512 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.883047 | 0.431993 | 0.0311537 | 0.139286 | 0.791919 | 0.512795 | 0.279125 | 0.349874 | 0.0501152 | 0.512609 | 0.961665 | 0.127462 |
| bonus_part_correctness | category | Geography | 501 | 0.896936 | 0.407947 | 0.0603999 | 0.129502 | 0.812375 | 0.572854 | 0.239521 | 0.337477 | 0.0753957 | 0.716479 | 0.966842 | 0.125099 |
| bonus_part_correctness | category | History | 4068 | 0.900153 | 0.399832 | 0.0233671 | 0.12699 | 0.813422 | 0.549164 | 0.264258 | 0.351308 | 0.0550374 | 0.603928 | 0.971045 | 0.123818 |
| bonus_part_correctness | category | Literature | 4065 | 0.902324 | 0.394393 | 0.0256998 | 0.124437 | 0.825338 | 0.510947 | 0.314391 | 0.35826 | 0.0491677 | 0.504986 | 0.96825 | 0.121441 |
| bonus_part_correctness | category | Mythology | 945 | 0.862467 | 0.453348 | 0.0342731 | 0.148939 | 0.779894 | 0.606349 | 0.173545 | 0.324319 | 0.130328 | 0.691512 | 0.97438 | 0.131482 |
| bonus_part_correctness | category | Other Academic | 219 | 0.884635 | 0.438818 | 0.0862611 | 0.141249 | 0.794521 | 0.493151 | 0.30137 | 0.364516 | 0.0412544 | 0.52212 | 0.955757 | 0.117115 |
| bonus_part_correctness | category | Philosophy | 963 | 0.886944 | 0.423742 | 0.0290374 | 0.133469 | 0.812046 | 0.483904 | 0.328141 | 0.344996 | 0.0578005 | 0.468462 | 0.962933 | 0.130958 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.862037 | 0.464835 | 0.083882 | 0.151831 | 0.756944 | 0.625 | 0.131944 | 0.338439 | 0.11015 | 0.716303 | 0.980951 | 0.119094 |
| bonus_part_correctness | category | Religion | 1008 | 0.899024 | 0.403457 | 0.0307491 | 0.127954 | 0.806548 | 0.503968 | 0.302579 | 0.359615 | 0.0425184 | 0.485686 | 0.959491 | 0.120676 |
| bonus_part_correctness | category | Science | 4059 | 0.897487 | 0.406864 | 0.0177748 | 0.127493 | 0.822863 | 0.530673 | 0.29219 | 0.353535 | 0.0518158 | 0.549532 | 0.96778 | 0.124208 |
| bonus_part_correctness | category | Social Science | 909 | 0.923222 | 0.350487 | 0.0354675 | 0.109845 | 0.842684 | 0.458746 | 0.383938 | 0.365166 | 0.0338809 | 0.432426 | 0.967695 | 0.116397 |
| bonus_part_correctness | category | Unknown | 5580 | 0.896184 | 0.407131 | 0.0186198 | 0.129485 | 0.81828 | 0.495878 | 0.322401 | 0.344474 | 0.0419873 | 0.466049 | 0.946135 | 0.131225 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

No bonus model comparison CSV was found.

## Pyramidal Player And Tossup Parameters

No pyramidal parameter distribution summary CSV was found.

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum | parameter_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.183059 | 1.21973 | -2.72148 | -2.19858 | -1.23018 | -0.108006 | 0.855293 | 1.61645 | 2.29529 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/synergy |
| bonus_part | alpha_1 | 3768 | 0.839474 | 0.458829 | 0.214263 | 0.320503 | 0.444791 | 0.73287 | 1.14775 | 1.67567 | 3.60649 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/synergy |
| bonus_part | alpha_2 | 3768 | 0.813538 | 0.417956 | 0.242568 | 0.349736 | 0.469208 | 0.708129 | 1.07612 | 1.59808 | 3.33248 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/synergy |
| bonus_part | alpha_3 | 3768 | 0.800258 | 0.404524 | 0.196426 | 0.327579 | 0.465073 | 0.711764 | 1.06819 | 1.4927 | 3.14189 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/synergy |
| bonus_part | alpha_norm | 3768 | 1.47301 | 0.621313 | 0.513695 | 0.611943 | 0.904061 | 1.45074 | 1.9591 | 2.47534 | 3.73691 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/synergy |
| synergy_player | psi_1 | 1455 | 0.0135703 | 0.428385 | -2.27987 | -0.635242 | -0.272298 | 0.00977175 | 0.284591 | 0.753494 | 1.58045 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/synergy |
| synergy_player | psi_norm | 1455 | 0.323983 | 0.280466 | 0.000120788 | 0.0128868 | 0.0881869 | 0.27886 | 0.473509 | 0.867162 | 2.27987 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/synergy |
| synergy | synergy_score | 2515 | 0.0359966 | 0.23295 | -1.47543 | -0.356441 | -0.00581885 | 0.0203666 | 0.122755 | 0.364982 | 2.49361 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/synergy |
| synergy | synergy_contribution | 35890 | 0.285837 | 0.644089 | -1.60125 | -0.675319 | -0.05929 | 0.147762 | 0.672879 | 1.45706 | 2.52239 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_2/train/synergy |
