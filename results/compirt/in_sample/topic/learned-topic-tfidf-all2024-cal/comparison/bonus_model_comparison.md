# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.915021 | 0.921569 | 0.00654779 | synergy |
| log_loss | 0.368886 | 0.356425 | -0.0124616 | synergy |
| ece | 0.0097505 | 0.0138302 | 0.00407967 | no-synergy |
| part_accuracy | 0.831973 | 0.841152 | 0.00917871 | synergy |
| part_accuracy_macro_team | 0.833107 | 0.843252 | 0.0101455 | synergy |
| part_accuracy_macro_game | 0.831964 | 0.841329 | 0.00936485 | synergy |
| part_accuracy_macro_bonus | 0.83733 | 0.842415 | 0.0050849 | synergy |
| exact_acc | 0.562591 | 0.582934 | 0.020343 | synergy |
| ppb_mae | 1.53525 | 0.540131 | -0.995124 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
