# CompIRT Experiment Report

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Tossup Metrics

| auc | log_loss | ece | accuracy | buzz_position_mae | buzz_position_median_absolute_error |
| --- | --- | --- | --- | --- | --- |
| 0.653424 | 0.618791 | 0.161958 | 0.680031 | 0.155791 | 0.138595 |

## Bonus Metrics

| auc | log_loss | ece | part_accuracy | part_accuracy_macro_team | part_accuracy_macro_game | part_accuracy_macro_bonus | exact_acc | ppb_mae |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.913158 | 0.380812 | 0.0356412 | 0.830452 | 0.832946 | 0.830577 | 0.83049 | 0.560838 | 0.757519 |

Generated figures include aggregate and buzz-position-stratified reliability, tossup difficulty over empirical buzz locations, per-dimension difficulty overlays for multidim fits, predicted-versus-empirical buzz timing, bonus-score predictions, and player, tossup, bonus-part, and optional synergy parameter distributions.
