# CompIRT Experiment Report

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.659738 | 0.514427 | 0.0145269 | 0.770526 | 0.123381 | 0.10022 |

## Bonus Metrics

| auc | log_loss | ece | part_accuracy | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.927551 | 0.349442 | 0.0352078 | 0.844404 | 0.845488 | 0.844588 | 0.850389 | 0.592937 | 1.82848 |

Generated figures include aggregate and buzz-position-stratified reliability, tossup difficulty over empirical buzz locations, per-dimension difficulty overlays for multidim fits, predicted-versus-empirical buzz timing, bonus-score predictions, and player, tossup, bonus-part, and optional synergy parameter distributions.
