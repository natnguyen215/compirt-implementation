# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.886586 | 0.893986 | 0.00739965 | synergy |
| log_loss | 0.425413 | 0.414747 | -0.0106656 | synergy |
| ece | 0.0192293 | 0.0331832 | 0.0139539 | no-synergy |
| brier | 0.13543 | 0.132227 | -0.00320306 | synergy |
| accuracy_lift_over_all_correct | 0.286728 | 0.292777 | 0.00604862 | synergy |
| part_accuracy | 0.806095 | 0.812144 | 0.00604862 | synergy |
| part_accuracy_macro_team | 0.810061 | 0.81594 | 0.00587905 | synergy |
| part_accuracy_macro_bonus | 0.805663 | 0.808567 | 0.0029038 | synergy |
| exact_acc | 0.509131 | 0.523904 | 0.0147726 | synergy |
| ranked_probability_score | 0.116545 | 0.112309 | -0.0042358 | synergy |
| bonus_total_score_log_loss | 1.02119 | 0.993031 | -0.0281562 | synergy |
| ppb_mae | 2.34809 | 1.88191 | -0.466179 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
