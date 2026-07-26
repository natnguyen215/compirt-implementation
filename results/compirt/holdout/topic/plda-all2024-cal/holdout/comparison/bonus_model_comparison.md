# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.907102 | 0.918793 | 0.0116911 | synergy |
| log_loss | 0.384478 | 0.362169 | -0.0223091 | synergy |
| ece | 0.0100158 | 0.0157777 | 0.00576191 | no-synergy |
| part_accuracy | 0.823596 | 0.837849 | 0.0142533 | synergy |
| part_accuracy_macro_team | 0.824384 | 0.839467 | 0.015083 | synergy |
| part_accuracy_macro_game | 0.823847 | 0.838348 | 0.0145006 | synergy |
| part_accuracy_macro_bonus | 0.8353 | 0.84575 | 0.0104496 | synergy |
| exact_acc | 0.543173 | 0.574106 | 0.0309326 | synergy |
| ppb_mae | 1.89131 | 0.43123 | -1.46008 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
