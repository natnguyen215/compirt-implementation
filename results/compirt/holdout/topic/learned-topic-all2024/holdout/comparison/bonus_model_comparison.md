# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.911356 | 0.91787 | 0.00651385 | synergy |
| log_loss | 0.391726 | 0.376906 | -0.0148195 | synergy |
| ece | 0.0588322 | 0.0526634 | -0.00616874 | synergy |
| part_accuracy | 0.825327 | 0.838494 | 0.013167 | synergy |
| part_accuracy_macro_team | 0.82751 | 0.840145 | 0.0126353 | synergy |
| part_accuracy_macro_game | 0.825644 | 0.838911 | 0.0132673 | synergy |
| part_accuracy_macro_bonus | 0.803847 | 0.830824 | 0.0269773 | synergy |
| exact_acc | 0.546217 | 0.576157 | 0.0299401 | synergy |
| ppb_mae | 1.78588 | 0.607208 | -1.17868 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
