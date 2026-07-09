# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.922341 | 0.926801 | 0.00446066 | synergy |
| log_loss | 0.361265 | 0.351346 | -0.00991933 | synergy |
| ece | 0.0354595 | 0.0335056 | -0.00195392 | synergy |
| accuracy | 0.839873 | 0.846043 | 0.00616998 | synergy |
| part_accuracy | 0.839873 | 0.846043 | 0.00616998 | synergy |
| exact_acc | 0.580259 | 0.595395 | 0.0151355 | synergy |
| per_bonus_points_mae | 5.08034 | 4.8454 | -0.234936 | synergy |
| ppb_mae | 2.13149 | 1.83168 | -0.299805 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
