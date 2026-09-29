# DD model interpretation

Start with the [bonus interpretation report](bonus/README.md). It follows the
requested questions with four figures and one ordering table:

1. **Difficulty:** easy/medium/hard density curves overall and within each question set.
2. **Ordering:** how often each bonus satisfies easy < medium < hard, with links to uncertainty and ten complete question examples.
3. **Skill overlap:** part difficulty and pooled team skill on the same scale.
4. **Clustering:** the subject patterns in relevance and the limits of those groups.

Use **D = r·d** for difficulty rankings and **location = D / sum(r)** when
comparing difficulty with team skill. The bonus report explains the distinction
and why individual difficulty coordinates cannot be read as subject difficulty.

## Supporting context: the shared skill axes

The [tossup report](tossup/README.md) has one figure comparing hazard and
correctness relevance. Axes 1–3 are learned skill coordinates; the bonus model
uses these frozen player skills. Recorded subjects help describe associations
after fitting: Science questions tend to weight axis 1 more, for example.
The axes retain neutral numeric labels because these associations overlap.
The [bonus grouping explanation](bonus/README.md#4-how-to-read-the-relevance-groups)
distinguishes axis weights, cluster membership, and recorded categories.

Across subcategory means, bonus direction agrees more closely with tossup
hazard relevance (Spearman 0.93 / 0.91 / 0.88) than correctness relevance
(0.86 / 0.54 / 0.66). The [comparison values](shared/data/subcategory_axes.csv)
and [summary](shared/data/output.txt) retain this check.

Both reports use the full-season 2024–25 in-sample fits at
`results/compirt/in_sample/common/bonus-difficulty-season-2024-25/dd/`.
They describe one fit's parameters; predictive results are in the
[bonus research log](../RESEARCH_LOG_2.md).

## Reproduce the five retained figures

From the repository root:

```bash
.venv/bin/python -B -m dd_model_interpretation.bonus.figures
.venv/bin/python -B -m dd_model_interpretation.tossup.figures
```

These commands use the saved analysis tables and, for team-skill density,
the saved bonus predictions. The `bonus.analyze`,
`tossup.analyze`, and `shared.compare` modules refresh supporting tables from
saved fits. No model training is needed.
