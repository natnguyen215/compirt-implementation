# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.929564 | 0.932626 | 0.00306151 | synergy |
| log_loss | 0.34149 | 0.335881 | -0.00560899 | synergy |
| ece | 0.0268148 | 0.0286101 | 0.00179532 | no-synergy |
| accuracy | 0.847631 | 0.852852 | 0.0052216 | synergy |
| part_accuracy | 0.847631 | 0.852852 | 0.0052216 | synergy |
| exact_acc | 0.598091 | 0.611291 | 0.0132001 | synergy |
| per_bonus_points_mae | 4.91799 | 4.69172 | -0.22627 | synergy |
| ppb_mae | 2.18781 | 1.70298 | -0.484829 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
