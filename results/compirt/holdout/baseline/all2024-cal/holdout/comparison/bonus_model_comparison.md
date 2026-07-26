# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.929564 | 0.932626 | 0.00306151 | synergy |
| log_loss | 0.34149 | 0.335881 | -0.00560899 | synergy |
| ece | 0.0268148 | 0.0286101 | 0.00179532 | no-synergy |
| part_accuracy | 0.847631 | 0.852852 | 0.0052216 | synergy |
| part_accuracy_macro_team | 0.848914 | 0.854272 | 0.0053586 | synergy |
| part_accuracy_macro_game | 0.848022 | 0.853226 | 0.00520495 | synergy |
| part_accuracy_macro_bonus | 0.858451 | 0.862939 | 0.0044879 | synergy |
| exact_acc | 0.598091 | 0.611291 | 0.0132001 | synergy |
| ppb_mae | 1.51927 | 0.697841 | -0.82143 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
