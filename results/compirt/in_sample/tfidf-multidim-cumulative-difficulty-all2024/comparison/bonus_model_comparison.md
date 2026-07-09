# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.920612 | 0.925131 | 0.00451986 | synergy |
| log_loss | 0.367469 | 0.357551 | -0.00991714 | synergy |
| ece | 0.039716 | 0.0386346 | -0.00108141 | synergy |
| accuracy | 0.839137 | 0.84331 | 0.0041735 | synergy |
| part_accuracy | 0.839137 | 0.84331 | 0.0041735 | synergy |
| exact_acc | 0.579945 | 0.591229 | 0.0112842 | synergy |
| per_bonus_points_mae | 5.10066 | 4.86628 | -0.234378 | synergy |
| ppb_mae | 2.2433 | 1.90717 | -0.336129 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
