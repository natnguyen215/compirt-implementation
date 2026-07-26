# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.889463 | 0.897762 | 0.00829973 | synergy |
| log_loss | 0.420432 | 0.406814 | -0.0136172 | synergy |
| ece | 0.0226479 | 0.0283349 | 0.00568698 | no-synergy |
| brier | 0.134143 | 0.12947 | -0.00467244 | synergy |
| accuracy_lift_over_all_correct | 0.282594 | 0.291149 | 0.0085551 | synergy |
| part_accuracy | 0.808279 | 0.816834 | 0.0085551 | synergy |
| part_accuracy_macro_team | 0.811087 | 0.816055 | 0.00496746 | synergy |
| part_accuracy_macro_bonus | 0.806987 | 0.815844 | 0.0088576 | synergy |
| exact_acc | 0.509639 | 0.52738 | 0.017741 | synergy |
| ranked_probability_score | 0.117621 | 0.112153 | -0.00546823 | synergy |
| bonus_total_score_log_loss | 1.0228 | 0.988394 | -0.0344098 | synergy |
| ppb_mae | 2.34918 | 1.80858 | -0.540596 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
