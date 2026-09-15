# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/evaluation`
Result root: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0`

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
| tau | 1.54877 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.891441 |
| log_loss | 0.416593 |
| ece | 0.0195634 |
| brier | 0.133171 |
| part_accuracy | 0.809164 |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.290727 |
| part_accuracy_macro_team | 0.809183 |
| part_accuracy_macro_bonus | 0.80652 |
| probability_std | 0.34446 |
| probability_p10 | 0.0556049 |
| probability_p50 | 0.53525 |
| probability_p90 | 0.956073 |
| mean_predictive_variance | 0.130762 |
| exact_acc | 0.512201 |
| ranked_probability_score | 0.11697 |
| bonus_total_score_log_loss | 1.0224 |
| ppb_mae | 2.35188 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

## Stage 1 Tossup Metrics

No tossup metrics CSV was found.

## Tossup Game Replay

No tossup game replay metrics CSV was found.

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25818 | 0.891441 | 0.416593 | 0.0195634 | 0.133171 | 0.809164 | 0.518437 | 0.290727 | 0.34446 | 0.0556049 | 0.53525 | 0.956073 | 0.130762 |
| bonus_part_correctness | tier | fall | 8415 | 0.885355 | 0.417159 | 0.0222046 | 0.135177 | 0.80202 | 0.600475 | 0.201545 | 0.328636 | 0.104345 | 0.677596 | 0.966323 | 0.131934 |
| bonus_part_correctness | tier | nationals | 4179 | 0.889733 | 0.418639 | 0.0483447 | 0.132577 | 0.81766 | 0.413975 | 0.403685 | 0.332584 | 0.0392525 | 0.411595 | 0.913905 | 0.137241 |
| bonus_part_correctness | tier | regionals | 5070 | 0.890793 | 0.417262 | 0.0219192 | 0.133201 | 0.806114 | 0.477318 | 0.328797 | 0.347177 | 0.0329765 | 0.422795 | 0.93949 | 0.128339 |
| bonus_part_correctness | tier | winter | 8154 | 0.892735 | 0.414546 | 0.0187211 | 0.131386 | 0.814079 | 0.512877 | 0.301202 | 0.34921 | 0.052883 | 0.516363 | 0.958353 | 0.127738 |
| bonus_part_correctness | category | Current Events | 258 | 0.931671 | 0.341814 | 0.0578499 | 0.100022 | 0.879845 | 0.496124 | 0.383721 | 0.355471 | 0.0389938 | 0.564212 | 0.938469 | 0.123476 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.877131 | 0.44147 | 0.0218588 | 0.142047 | 0.793171 | 0.506667 | 0.286504 | 0.333858 | 0.0706405 | 0.52434 | 0.952313 | 0.13824 |
| bonus_part_correctness | category | Geography | 453 | 0.888873 | 0.416819 | 0.0423496 | 0.132601 | 0.8234 | 0.600442 | 0.222958 | 0.327305 | 0.0692354 | 0.701845 | 0.959824 | 0.129554 |
| bonus_part_correctness | category | History | 4176 | 0.889207 | 0.417894 | 0.0269624 | 0.134912 | 0.800048 | 0.55364 | 0.246408 | 0.339492 | 0.0675965 | 0.611053 | 0.962085 | 0.130709 |
| bonus_part_correctness | category | Literature | 4197 | 0.90564 | 0.390233 | 0.0272381 | 0.123226 | 0.828449 | 0.508458 | 0.31999 | 0.346788 | 0.0580948 | 0.509498 | 0.958764 | 0.129378 |
| bonus_part_correctness | category | Mythology | 951 | 0.869858 | 0.439493 | 0.0349584 | 0.143797 | 0.783386 | 0.608833 | 0.174553 | 0.31073 | 0.154937 | 0.688008 | 0.966638 | 0.137232 |
| bonus_part_correctness | category | Other Academic | 258 | 0.911915 | 0.380033 | 0.0407881 | 0.117736 | 0.829457 | 0.55814 | 0.271318 | 0.354213 | 0.0435587 | 0.605346 | 0.96074 | 0.123398 |
| bonus_part_correctness | category | Philosophy | 969 | 0.876247 | 0.441661 | 0.0294812 | 0.143013 | 0.791538 | 0.493292 | 0.298246 | 0.332285 | 0.0669913 | 0.505557 | 0.946046 | 0.139514 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.860037 | 0.447551 | 0.0846577 | 0.153365 | 0.768977 | 0.620462 | 0.148515 | 0.312521 | 0.148078 | 0.734747 | 0.970725 | 0.133542 |
| bonus_part_correctness | category | Religion | 1041 | 0.894028 | 0.416998 | 0.042639 | 0.131735 | 0.819404 | 0.509126 | 0.310279 | 0.35036 | 0.0386138 | 0.53739 | 0.951581 | 0.126994 |
| bonus_part_correctness | category | Science | 4152 | 0.891778 | 0.415102 | 0.021443 | 0.131977 | 0.816474 | 0.529383 | 0.287091 | 0.344522 | 0.0649498 | 0.557284 | 0.957504 | 0.129825 |
| bonus_part_correctness | category | Social Science | 915 | 0.88854 | 0.421258 | 0.0381724 | 0.133716 | 0.814208 | 0.485246 | 0.328962 | 0.357437 | 0.0297751 | 0.430007 | 0.95898 | 0.12199 |
| bonus_part_correctness | category | Unknown | 5070 | 0.890793 | 0.417262 | 0.0219192 | 0.133201 | 0.806114 | 0.477318 | 0.328797 | 0.347177 | 0.0329765 | 0.422795 | 0.93949 | 0.128339 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

No bonus model comparison CSV was found.

## Pyramidal Player And Tossup Parameters

No pyramidal parameter distribution summary CSV was found.

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum | parameter_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.215417 | 1.2349 | -2.74897 | -2.25018 | -1.25419 | -0.160375 | 0.826598 | 1.62163 | 2.17147 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/compositional |
| bonus_part | alpha_1 | 3768 | 0.792452 | 0.440736 | 0.198466 | 0.30427 | 0.430561 | 0.683658 | 1.0636 | 1.61791 | 3.31306 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/compositional |
| bonus_part | alpha_2 | 3768 | 0.755785 | 0.406089 | 0.192176 | 0.32886 | 0.426208 | 0.627177 | 0.990406 | 1.56751 | 2.84682 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/compositional |
| bonus_part | alpha_3 | 3768 | 0.753061 | 0.385893 | 0.207786 | 0.314158 | 0.44849 | 0.656705 | 0.977369 | 1.44874 | 2.97016 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/compositional |
| bonus_part | alpha_norm | 3768 | 1.38706 | 0.591926 | 0.491301 | 0.588622 | 0.843642 | 1.32253 | 1.84365 | 2.38061 | 3.48008 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/compositional |
