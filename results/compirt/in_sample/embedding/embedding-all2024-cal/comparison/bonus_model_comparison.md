# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.911376 | 0.919715 | 0.0083394 | synergy |
| log_loss | 0.375706 | 0.360107 | -0.015599 | synergy |
| ece | 0.00621708 | 0.0133781 | 0.00716099 | no-synergy |
| part_accuracy | 0.82771 | 0.838267 | 0.0105574 | synergy |
| part_accuracy_macro_team | 0.828909 | 0.840659 | 0.0117496 | synergy |
| part_accuracy_macro_game | 0.827812 | 0.838546 | 0.0107341 | synergy |
| part_accuracy_macro_bonus | 0.834802 | 0.842337 | 0.00753512 | synergy |
| exact_acc | 0.554027 | 0.576416 | 0.0223886 | synergy |
| ppb_mae | 1.59555 | 0.527134 | -1.06842 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
