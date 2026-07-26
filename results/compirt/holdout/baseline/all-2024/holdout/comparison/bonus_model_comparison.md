# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.932352 | 0.938384 | 0.00603197 | synergy |
| log_loss | 0.340014 | 0.325596 | -0.0144186 | synergy |
| ece | 0.0370095 | 0.0358433 | -0.00116626 | synergy |
| part_accuracy | 0.852323 | 0.858691 | 0.00636848 | synergy |
| part_accuracy_macro_team | 0.854254 | 0.860685 | 0.00643097 | synergy |
| part_accuracy_macro_game | 0.852802 | 0.859155 | 0.00635361 | synergy |
| part_accuracy_macro_bonus | 0.86529 | 0.868147 | 0.00285783 | synergy |
| exact_acc | 0.609306 | 0.624094 | 0.0147881 | synergy |
| ppb_mae | 1.44329 | 0.65602 | -0.787269 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
