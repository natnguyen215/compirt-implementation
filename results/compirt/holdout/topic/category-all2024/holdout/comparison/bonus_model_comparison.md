# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.915462 | 0.921776 | 0.00631381 | synergy |
| log_loss | 0.377652 | 0.362624 | -0.0150287 | synergy |
| ece | 0.0437456 | 0.0384641 | -0.00528148 | synergy |
| part_accuracy | 0.831398 | 0.841196 | 0.00979808 | synergy |
| part_accuracy_macro_team | 0.832336 | 0.84298 | 0.0106443 | synergy |
| part_accuracy_macro_game | 0.831555 | 0.841632 | 0.010077 | synergy |
| part_accuracy_macro_bonus | 0.821037 | 0.839418 | 0.0183814 | synergy |
| exact_acc | 0.5595 | 0.581649 | 0.0221491 | synergy |
| ppb_mae | 1.67053 | 0.543396 | -1.12714 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
