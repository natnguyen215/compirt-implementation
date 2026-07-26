# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.886726 | 0.893518 | 0.00679198 | synergy |
| log_loss | 0.424619 | 0.413527 | -0.0110921 | synergy |
| ece | 0.0172196 | 0.0236442 | 0.00642459 | no-synergy |
| brier | 0.135103 | 0.131992 | -0.00311115 | synergy |
| accuracy_lift_over_all_correct | 0.291347 | 0.292432 | 0.00108451 | synergy |
| part_accuracy | 0.809784 | 0.810868 | 0.00108451 | synergy |
| part_accuracy_macro_team | 0.812382 | 0.812641 | 0.000259131 | synergy |
| part_accuracy_macro_bonus | 0.805734 | 0.807966 | 0.00223257 | synergy |
| exact_acc | 0.513479 | 0.514292 | 0.000813386 | synergy |
| ranked_probability_score | 0.11738 | 0.113116 | -0.0042646 | synergy |
| bonus_total_score_log_loss | 1.02644 | 0.996424 | -0.030016 | synergy |
| ppb_mae | 2.3728 | 1.81822 | -0.554581 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
