# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.891193 | 0.897276 | 0.00608297 | synergy |
| log_loss | 0.418663 | 0.409278 | -0.0093858 | synergy |
| ece | 0.02631 | 0.0346524 | 0.00834242 | no-synergy |
| brier | 0.133331 | 0.130243 | -0.0030877 | synergy |
| accuracy_lift_over_all_correct | 0.284814 | 0.290497 | 0.00568314 | synergy |
| part_accuracy | 0.810369 | 0.816052 | 0.00568314 | synergy |
| part_accuracy_macro_team | 0.814372 | 0.82204 | 0.00766887 | synergy |
| part_accuracy_macro_bonus | 0.801633 | 0.808883 | 0.00724938 | synergy |
| exact_acc | 0.515658 | 0.529344 | 0.0136859 | synergy |
| ranked_probability_score | 0.117406 | 0.113508 | -0.00389834 | synergy |
| bonus_total_score_log_loss | 1.02344 | 1.00018 | -0.023266 | synergy |
| ppb_mae | 2.31844 | 1.86663 | -0.451812 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
