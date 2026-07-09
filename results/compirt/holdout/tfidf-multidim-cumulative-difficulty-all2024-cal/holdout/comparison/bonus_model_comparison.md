# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.928178 | 0.932839 | 0.00466122 | synergy |
| log_loss | 0.342408 | 0.333042 | -0.00936658 | synergy |
| ece | 0.0212791 | 0.0211868 | -9.22858e-05 | synergy |
| accuracy | 0.845795 | 0.852847 | 0.00705219 | synergy |
| part_accuracy | 0.845795 | 0.852847 | 0.00705219 | synergy |
| exact_acc | 0.594237 | 0.609521 | 0.0152843 | synergy |
| per_bonus_points_mae | 4.84414 | 4.66822 | -0.175917 | synergy |
| ppb_mae | 2.07174 | 1.65466 | -0.417077 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
