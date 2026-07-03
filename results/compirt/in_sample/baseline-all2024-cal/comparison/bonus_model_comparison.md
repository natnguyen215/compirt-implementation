# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.929964 | 0.932743 | 0.00277858 | synergy |
| log_loss | 0.342806 | 0.338007 | -0.00479888 | synergy |
| ece | 0.0330169 | 0.0341318 | 0.00111496 | no-synergy |
| accuracy | 0.84624 | 0.851312 | 0.00507264 | synergy |
| part_accuracy | 0.84624 | 0.851312 | 0.00507264 | synergy |
| exact_acc | 0.597613 | 0.608875 | 0.0112617 | synergy |
| rounded_score_accuracy | 0.597298 | 0.61146 | 0.0141614 | synergy |
| per_bonus_points_mae | 4.89124 | 4.6849 | -0.206348 | synergy |
| ppb_mae | 2.29036 | 1.75832 | -0.532043 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
