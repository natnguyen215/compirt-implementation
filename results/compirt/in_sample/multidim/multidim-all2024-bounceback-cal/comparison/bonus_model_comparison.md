# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.936141 | 0.936291 | 0.000149888 | synergy |
| log_loss | 0.331058 | 0.330929 | -0.000128668 | synergy |
| ece | 0.0382418 | 0.037406 | -0.000835819 | synergy |
| brier | 0.10349 | 0.102833 | -0.000657292 | synergy |
| accuracy_lift_over_all_correct | 0.333498 | 0.335237 | 0.00173834 | synergy |
| part_accuracy | 0.853987 | 0.855726 | 0.00173834 | synergy |
| part_accuracy_macro_team | 0.856057 | 0.858083 | 0.00202585 | synergy |
| part_accuracy_macro_game | 0.854284 | 0.856058 | 0.00177425 | synergy |
| part_accuracy_macro_bonus | 0.861529 | 0.860165 | -0.00136367 | no-synergy |
| exact_acc | 0.61591 | 0.620586 | 0.00467552 | synergy |
| ranked_probability_score | 0.0941761 | 0.0920475 | -0.00212862 | synergy |
| bonus_total_score_log_loss | 0.838958 | 0.828797 | -0.0101609 | synergy |
| ppb_mae | 1.52347 | 0.86116 | -0.66231 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
