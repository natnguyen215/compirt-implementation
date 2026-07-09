# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.919946 | 0.93257 | 0.0126244 | synergy |
| log_loss | 0.364257 | 0.339477 | -0.0247804 | synergy |
| ece | 0.0284211 | 0.0355157 | 0.00709462 | no-synergy |
| accuracy | 0.837466 | 0.852047 | 0.014581 | synergy |
| part_accuracy | 0.837466 | 0.852047 | 0.014581 | synergy |
| exact_acc | 0.578821 | 0.609459 | 0.0306382 | synergy |
| per_bonus_points_mae | 5.07876 | 4.70285 | -0.375912 | synergy |
| ppb_mae | 2.43547 | 1.68894 | -0.746525 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
