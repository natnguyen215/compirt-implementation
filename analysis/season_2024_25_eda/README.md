# 2024–25 season exploratory data analysis

This folder analyses the **2024–25 ACF season** — the one complete competitive season in the local dataset. It runs Fall (2024-10-19) → Winter (2024-11-16) → Regionals (2025-02-01) → Nationals (2025-04-19) across 33 mirror sites.

Because this is a single season, calendar year is perfectly collinear with tier (Fall and Winter are 2024, Regionals and Nationals are 2025), so **year is dropped as an axis entirely**. Tier is the chronological axis here, and it happens to be the difficulty axis too. That is the structural difference from [`../full_dataset_eda/`](../full_dataset_eda/), which analyses both calendar years and treats year as a comparison axis.

## Season at a glance

| Tier | Date | Sites | Teams | Games | Player IDs | Attempts |
|---|---|---:|---:|---:|---:|---:|
| ACF Fall | Oct 2024 | 8 | 141 | 744 | 542 | 17,682 |
| ACF Winter | Nov 2024 | 10 | 166 | 758 | 674 | 18,136 |
| ACF Regionals | Feb 2025 | 14 | 137 | 747 | 504 | 18,050 |
| ACF Nationals | Apr 2025 | 1 | 48 | 412 | 182 | 10,169 |
| **Season** | | **33** | **492** | **2,661** | **1,339** | **64,037** |

Plus 1,360 tossups, 1,359 bonuses, 49,042 bonuses heard, and 147,126 bonus-part observations.

## Why this scope is worth its own folder

Two things are true here that are not true of any year-based slice:

1. **Category metadata is complete.** The only unlabelled question set in the corpus is 2024 Regionals, which belongs to season 2023–24. Every one of the 1,360 tossups and 1,359 bonuses here carries a category, so no category analysis has to carve out an exception.
2. **Players can be followed through the season**, and selection can be measured on a *fixed* question set — comparing players by how far they later go, while holding the questions constant. That removes the difficulty confound that makes naive cross-tier player comparisons meaningless.

## Main findings

- **The tier "difficulty gradient" is mostly a timing and dead-tossup gradient, not a conditional-accuracy gradient.** All-attempt accuracy falls 6.5 points across the season (79.9% → 74.7%), but **scored accuracy barely moves — 82.9% → 81.1%, a range of 1.9 points**. What actually changes is when people buzz (median position 66.7% → 80.4% revealed), how often tossups die unanswered (zero rate 3.7% → 10.3%), and bonus conversion (PPB 17.96 → 14.18). Conditional on taking a scored buzz, players are right about 82% of the time regardless of set difficulty.
- **What separates players who advance is timing, not conditional accuracy.** Holding the question set fixed, players who reach Nationals buzz 8–13 percentage points of the question earlier than players who stop after that tier, while their scored accuracy is only 4–6 points higher. On the Winter set: 62.4% mean position for Nationals-bound players against 75.1% for those who stop at Winter, with scored accuracy 0.852 against 0.813.
- **The season funnels sharply, but the field is not a cohort.** 898 of 1,339 players appear at exactly one tier and only **7** play all four. Yet carry-over accumulates: Winter is 18.1% attempts from players seen earlier, Regionals 56.0%, Nationals 72.1%. Only 3% of Fall players reach Nationals, while 64% of Nationals players had played Regionals.
- **Scored accuracy rises monotonically with buzz position** (0.736 in the first decile to 0.910 in the last) and neg rate falls alongside it. All-attempt accuracy appears to reverse in the final decile only because the zero rate jumps to 13.7% there.
- **Bonus-part labels are well calibrated**, with easy > medium > hard holding at every tier (0.89–0.95 / 0.41–0.61 / 0.09–0.24). Nationals is the exception at the top: its easy parts convert at 0.942, on par with Fall.
- **Both MDS maps are clean.** Team stress-1 0.132 over 480 stable team entries, mirror-site 0.150 over 33 sites. At both grains dimension 1 is general strength/difficulty and dimension 2 separates neg-taking from the rest.
- **Buzzing has strong clue-local structure.** 17.05% of scored phase-0 first buzzes land exactly on a sentence/clue boundary versus 4.67% of token opportunities in the same questions, a 3.65× enrichment. This supports clue-aware hazard curves rather than position-only smoothness.
- **Player timing carries across events, and category timing specialization carries across season halves.** Question-centered timing correlations are 0.54–0.74 for adjacent-tier returners. Category-specific timing residuals repeat at r = 0.387 (10-attempt threshold), while category-specific correctness residuals do not (r = 0.009). This suggests informative player drift priors and richer multidimensional structure in the hazard branch than in correctness.

## Where to start

- [EDA_REPORT.md](EDA_REPORT.md): findings and interpretation.
- [FIGURE_INDEX.md](FIGURE_INDEX.md): guide to all 29 graphs.
- [MDS.md](MDS.md): MDS features, algorithm, axis interpretation, and limitations.
- [METHODOLOGY.md](METHODOLOGY.md): scope definition, transformations, denominators, reproducibility.
- [DATA_DICTIONARY.md](DATA_DICTIONARY.md): generated table definitions.
- [DATA_QUALITY.md](DATA_QUALITY.md): what is and is not a problem in this slice.
- [data/dataset_summary.csv](data/dataset_summary.csv): headline machine-readable counts.
- [data/validation.json](data/validation.json): automated integrity checks.

## Reproduce

From the repository root:

```bash
MPLCONFIGDIR=/tmp/season_eda_mpl \
  .venv/bin/python -B analysis/season_2024_25_eda/analyze.py
```

The script reads the `all` split of `data/hf/quizbowl-irt/*`, filters to the 2024–25 season by tournament start date, writes every aggregate CSV to `data/`, and regenerates all figures in `figures/`. Add `--skip-figures` for CSVs only. It writes nothing outside this folder.
