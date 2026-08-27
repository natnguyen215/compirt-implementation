# Double-Bernstein grid-search summary

Evaluation regime: 5-fold frozen whole-game matrix infill, tossups only.
Primary selection metric: pooled `joint_tossup_event_log_loss` (lower is better).

Complete configurations: 1 / 1.

| rank | degree | curves | Dirichlet | joint log loss | correctness log loss | neg AUROC | integrated Brier | no-buzz Brier |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 3 | 3 | 2 | 6.43762 | 0.505831 | 0.71659 | 0.0941821 | 0.0125952 |

## Selected configuration

- Degree: 3
- Curves/dimensions: 3
- Dirichlet concentration: 2
- Pooled joint event log loss: 6.43762

This is the CV winner, not an unbiased final-test estimate. Refit and assess it on an untouched test set, or use nested CV, before reporting a final generalization number.
