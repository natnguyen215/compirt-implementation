# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.913187 | 0.919302 | 0.00611497 | synergy |
| log_loss | 0.390435 | 0.37741 | -0.0130251 | synergy |
| ece | 0.0592938 | 0.0565526 | -0.00274114 | synergy |
| part_accuracy | 0.831689 | 0.839684 | 0.00799484 | synergy |
| part_accuracy_macro_team | 0.834192 | 0.84189 | 0.00769809 | synergy |
| part_accuracy_macro_game | 0.831739 | 0.839989 | 0.00824966 | synergy |
| part_accuracy_macro_bonus | 0.824351 | 0.836234 | 0.0118833 | synergy |
| exact_acc | 0.562344 | 0.580754 | 0.0184099 | synergy |
| ppb_mae | 1.48994 | 0.643422 | -0.846517 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
