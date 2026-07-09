# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.927824 | 0.936097 | 0.00827259 | synergy |
| log_loss | 0.353406 | 0.33512 | -0.0182854 | synergy |
| ece | 0.0422139 | 0.0433857 | 0.00117174 | no-synergy |
| accuracy | 0.846367 | 0.854617 | 0.0082496 | synergy |
| part_accuracy | 0.846367 | 0.854617 | 0.0082496 | synergy |
| exact_acc | 0.597366 | 0.615393 | 0.0180277 | synergy |
| per_bonus_points_mae | 5.00527 | 4.64776 | -0.357513 | synergy |
| ppb_mae | 2.36638 | 1.7864 | -0.579984 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
