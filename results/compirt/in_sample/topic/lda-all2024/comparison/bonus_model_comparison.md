# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.90667 | 0.915409 | 0.00873892 | synergy |
| log_loss | 0.408108 | 0.386472 | -0.0216358 | synergy |
| ece | 0.0729473 | 0.0588741 | -0.0140732 | synergy |
| part_accuracy | 0.81767 | 0.836102 | 0.0184324 | synergy |
| part_accuracy_macro_team | 0.821964 | 0.838083 | 0.0161187 | synergy |
| part_accuracy_macro_game | 0.817494 | 0.836351 | 0.0188565 | synergy |
| part_accuracy_macro_bonus | 0.800352 | 0.832314 | 0.0319621 | synergy |
| exact_acc | 0.535415 | 0.573853 | 0.0384382 | synergy |
| ppb_mae | 2.09587 | 0.718756 | -1.37711 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
