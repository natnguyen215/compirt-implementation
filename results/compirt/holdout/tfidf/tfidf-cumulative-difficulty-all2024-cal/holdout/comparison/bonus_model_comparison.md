# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.912494 | 0.927395 | 0.0149013 | synergy |
| log_loss | 0.376319 | 0.345773 | -0.0305459 | synergy |
| ece | 0.0210548 | 0.0244892 | 0.00343436 | no-synergy |
| part_accuracy | 0.82847 | 0.847168 | 0.0186974 | synergy |
| part_accuracy_macro_team | 0.829393 | 0.848547 | 0.0191534 | synergy |
| part_accuracy_macro_game | 0.82871 | 0.847548 | 0.018838 | synergy |
| part_accuracy_macro_bonus | 0.836547 | 0.857646 | 0.021099 | synergy |
| exact_acc | 0.554422 | 0.597181 | 0.0427598 | synergy |
| ppb_mae | 2.10351 | 0.534199 | -1.56931 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
