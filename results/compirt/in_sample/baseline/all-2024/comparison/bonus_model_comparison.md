# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.932678 | 0.939241 | 0.00656315 | synergy |
| log_loss | 0.342423 | 0.327827 | -0.0145957 | synergy |
| ece | 0.0411874 | 0.0435584 | 0.00237102 | no-synergy |
| part_accuracy | 0.852594 | 0.859008 | 0.00641386 | synergy |
| part_accuracy_macro_team | 0.855296 | 0.861651 | 0.00635508 | synergy |
| part_accuracy_macro_game | 0.852995 | 0.859364 | 0.00636888 | synergy |
| part_accuracy_macro_bonus | 0.860211 | 0.862927 | 0.00271542 | synergy |
| exact_acc | 0.612404 | 0.627015 | 0.014611 | synergy |
| ppb_mae | 1.57744 | 0.878661 | -0.698775 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
