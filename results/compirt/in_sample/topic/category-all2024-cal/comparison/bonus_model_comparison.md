# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.909656 | 0.919556 | 0.00990025 | synergy |
| log_loss | 0.379766 | 0.360456 | -0.0193097 | synergy |
| ece | 0.00556298 | 0.011178 | 0.005615 | no-synergy |
| part_accuracy | 0.827036 | 0.838575 | 0.011539 | synergy |
| part_accuracy_macro_team | 0.828369 | 0.840975 | 0.0126053 | synergy |
| part_accuracy_macro_game | 0.827087 | 0.838776 | 0.0116886 | synergy |
| part_accuracy_macro_bonus | 0.833123 | 0.841408 | 0.00828505 | synergy |
| exact_acc | 0.552903 | 0.579518 | 0.0266145 | synergy |
| ppb_mae | 1.78164 | 0.583224 | -1.19842 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
