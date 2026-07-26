# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.91558 | 0.924547 | 0.0089666 | synergy |
| log_loss | 0.367053 | 0.349022 | -0.0180312 | synergy |
| ece | 0.00921776 | 0.0138288 | 0.00461103 | no-synergy |
| part_accuracy | 0.833184 | 0.844003 | 0.0108181 | synergy |
| part_accuracy_macro_team | 0.83408 | 0.84533 | 0.0112493 | synergy |
| part_accuracy_macro_game | 0.833439 | 0.844463 | 0.0110248 | synergy |
| part_accuracy_macro_bonus | 0.842891 | 0.847898 | 0.00500649 | synergy |
| exact_acc | 0.563767 | 0.588084 | 0.024316 | synergy |
| ppb_mae | 1.69835 | 0.445241 | -1.25311 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
