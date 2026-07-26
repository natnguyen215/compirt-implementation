# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.934334 | 0.93609 | 0.00175579 | synergy |
| log_loss | 0.331262 | 0.329038 | -0.00222385 | synergy |
| ece | 0.0286843 | 0.0314931 | 0.00280883 | no-synergy |
| part_accuracy | 0.853034 | 0.857352 | 0.00431733 | synergy |
| part_accuracy_macro_team | 0.854377 | 0.858783 | 0.00440579 | synergy |
| part_accuracy_macro_game | 0.853472 | 0.857805 | 0.00433343 | synergy |
| part_accuracy_macro_bonus | 0.866045 | 0.867152 | 0.00110676 | synergy |
| exact_acc | 0.612052 | 0.621812 | 0.00975949 | synergy |
| ppb_mae | 1.4743 | 0.72152 | -0.752781 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
