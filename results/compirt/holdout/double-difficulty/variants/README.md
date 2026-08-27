# Variants

Structural changes to the model, not settings on the reference. Each is measured
against [`../reference-model/`](../reference-model/).

| Folder | Change | Verdict |
| --- | --- | --- |
| [`player-neg-propensity/`](player-neg-propensity/) | Adds a hierarchical per-player neg propensity term. | Essentially ties the reference on every headline metric (joint LL 6.5831 vs 6.6124) — the extra parameter buys little. §3.10 |
| [`perceived-difficulty/`](perceived-difficulty/) | Players respond to a *perceived* difficulty rather than the true curve. 6 arms: `unconstrained`, `positive-alpha`, `three-slice`, `three-slice-10000-steps`, `three-slice-alternating`, `three-slice-alternating-10000-steps`. | All arms lose badly to the reference on correctness LL and ECE; several fall below the 0.7670 all-correct accuracy baseline. §3.8 |
| [`perceived-logit/`](perceived-logit/) | Perception applied on the logit scale. `unconstrained` and `positive-alpha`. | Worse still — `positive-alpha` reaches 0.3458 ECE and 0.3758 accuracy. §3.9 |

The perceived-difficulty and perceived-logit families are **negative results**
kept for the record. Do not present them as candidate models.
