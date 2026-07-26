# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.912196 | 0.923776 | 0.0115803 | synergy |
| log_loss | 0.373348 | 0.350467 | -0.0228807 | synergy |
| ece | 0.00569639 | 0.0115879 | 0.00589156 | no-synergy |
| part_accuracy | 0.82831 | 0.84296 | 0.0146503 | synergy |
| part_accuracy_macro_team | 0.828221 | 0.844418 | 0.0161974 | synergy |
| part_accuracy_macro_game | 0.82846 | 0.843426 | 0.014966 | synergy |
| part_accuracy_macro_bonus | 0.84023 | 0.852139 | 0.0119091 | synergy |
| exact_acc | 0.552321 | 0.586297 | 0.0339762 | synergy |
| ppb_mae | 1.88838 | 0.417365 | -1.47102 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
