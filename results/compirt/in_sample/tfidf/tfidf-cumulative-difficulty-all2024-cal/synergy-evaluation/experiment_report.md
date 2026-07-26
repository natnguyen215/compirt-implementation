# CompIRT Experiment Report

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.64844 | 0.516876 | 0.00921367 | 0.769671 | 0.130063 | 0.111996 |

## Bonus Metrics

| auc | log_loss | ece | part_accuracy | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.927831 | 0.347097 | 0.0297489 | 0.848323 | 0.850983 | 0.848868 | 0.848751 | 0.602198 | 0.613089 |

Generated figures include aggregate and buzz-position-stratified reliability, tossup difficulty over empirical buzz locations, per-dimension difficulty overlays for multidim fits, predicted-versus-empirical buzz timing, bonus-score predictions, and player, tossup, bonus-part, and optional synergy parameter distributions.
