# DD-Bernstein: five-fold normalized-likelihood retraining comparison

Configuration: degree 3, dimensions 3, drop concentration 2; simplex relevance, learned locations, terminal intercepts. Split year_2024, folds 0–4, seeds 42. All 46,640 matched held-out race events, including 45,995 observed first buzzes and 645 no-buzz events. Pooled metrics; these are reused development folds.

Historical fitted parameters and new fitted parameters use the same normalized full-grid scoring function from analysis/correctness/tossup_accuracy_study/evaluate_timing.py. Historical event scores come from its saved timing_comparison outputs; 10 events per fold were independently reconstructed to verify agreement. Observation IDs, outcomes and times match exactly in each fold. Historical pooled metrics were checked against frozen-skills/pyro-cut-vi/comparison.csv.

Correctness conditions on the observed buzzer and position, with decision threshold 0.5. Position errors use expected relative position conditional on a buzz and are measured in fractions of question length. No-buzz rate is the mean probability of no first buzz, not the no-buzz fraction from token-threshold outcome replay. Joint log loss combines timing, identity and correctness, and includes no-buzz events. Lower losses/errors are better.

| Metric | Historical | Retrained | Change |
| --- | ---: | ---: | ---: |
| events | 46640.000000000 | 46640.000000000 | +0.000000000 |
| buzz_events | 45995.000000000 | 45995.000000000 | +0.000000000 |
| timing_mae | 0.151863557 | 0.154427597 | +0.002564040 |
| timing_rmse | 0.185772108 | 0.188576915 | +0.002804807 |
| timing_bias | -0.045302358 | -0.050115043 | -0.004812685 |
| integrated_brier | 0.101699928 | 0.101840507 | +0.000140579 |
| timing_nll | 4.481926071 | 4.474174868 | -0.007751203 |
| race_nll | 6.134499225 | 6.123231366 | -0.011267860 |
| joint_nll | 6.615526136 | 6.604271910 | -0.011254226 |
| first_buzzer_accuracy | 0.351646918 | 0.353321013 | +0.001674095 |
| first_buzzer_nll | 1.675747623 | 1.672181651 | -0.003565972 |
| dead_brier | 0.013233992 | 0.015242580 | +0.002008588 |
| predicted_dead_rate | 0.014769788 | 0.031211293 | +0.016441506 |
| observed_dead_rate | 0.013829331 | 0.013829331 | +0.000000000 |
| correctness_auc | 0.715438727 | 0.715367047 | -0.000071680 |
| correctness_log_loss | 0.487772478 | 0.487786303 | +0.000013825 |
| correctness_ece | 0.009848039 | 0.009654716 | -0.000193323 |
| correctness_brier | 0.158237954 | 0.158239929 | +0.000001975 |
| correctness_accuracy | 0.779497771 | 0.779345581 | -0.000152190 |
| correctness_all_correct_accuracy | 0.766996413 | 0.766996413 | +0.000000000 |
| correctness_accuracy_lift_over_all_correct | 0.012501359 | 0.012349168 | -0.000152190 |
| correctness_probability_std | 0.140395731 | 0.140521897 | +0.000126166 |
| correctness_probability_p10 | 0.582245800 | 0.581205000 | -0.001040800 |
| correctness_probability_p50 | 0.812397660 | 0.812487360 | +0.000089700 |
| correctness_probability_p90 | 0.917986720 | 0.918026556 | +0.000039836 |
| correctness_mean_predictive_variance | 0.154019655 | 0.153980053 | -0.000039602 |
| neg_auroc | 0.715438727 | 0.715367047 | -0.000071680 |
| neg_average_precision | 0.449319530 | 0.449446497 | +0.000126967 |
| neg_precision | 0.615508236 | 0.613964687 | -0.001543549 |
| neg_recall | 0.142950453 | 0.142763833 | -0.000186619 |
| neg_f1 | 0.232015750 | 0.231660232 | -0.000355519 |

Saved roots:

- historical: `results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal`
- retrained: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-20260913-150350`

This report covers Stage-1 tossup metrics. Bonus stages and downstream token-threshold game replay are separate; the research logs and frozen-skills comparison tables have not been rewritten.
