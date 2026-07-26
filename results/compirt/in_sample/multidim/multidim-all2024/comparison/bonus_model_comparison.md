# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.927123 | 0.935559 | 0.00843554 | synergy |
| log_loss | 0.355133 | 0.336424 | -0.0187089 | synergy |
| ece | 0.0417817 | 0.0437654 | 0.00198365 | no-synergy |
| brier | 0.110096 | 0.104196 | -0.00589924 | synergy |
| accuracy_lift_over_all_correct | 0.325189 | 0.333528 | 0.00833951 | synergy |
| part_accuracy | 0.845678 | 0.854017 | 0.00833951 | synergy |
| part_accuracy_macro_team | 0.848976 | 0.857456 | 0.00847967 | synergy |
| part_accuracy_macro_game | 0.846101 | 0.854597 | 0.00849552 | synergy |
| part_accuracy_macro_bonus | 0.853912 | 0.857878 | 0.0039661 | synergy |
| exact_acc | 0.596534 | 0.614764 | 0.01823 | synergy |
| ranked_probability_score | 0.100243 | 0.0931524 | -0.00709033 | synergy |
| bonus_total_score_log_loss | 0.889913 | 0.840351 | -0.0495621 | synergy |
| ppb_mae | 1.83683 | 0.905 | -0.931831 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
