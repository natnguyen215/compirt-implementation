# Drop robustness Tier 1: random-drop curves (2024 in-sample)

This directory holds one completed Tier-1 run of the data-dropping robustness
study: for each drop fraction and replicate, a random set of buzz events is
deleted, each Stage-1 ranking method is refit at the fixed model seed, and the
refit ranking is scored against the same method's full-data ranking. The
mathematical contract (functionals, agreement metrics, AMIP relation) is
`compirt_eval/drop_robustness/README.md`; commands and general interpretation are in
`docs/compirt-experiments.md`. This README records what *this* run found.

Tier 2 (targeted worst-case drops, `run_scripts/common/run_targeted_drop.py`) has not
been run yet; see "Status" at the end.

## Setup

| Setting | Value |
| --- | --- |
| Data split | `year_2024`, in sample (48,612 buzz events; 1,455 players) |
| Methods | raw actual PPG (no refit), plain IRT, baseline CompIRT, multidim CompIRT |
| Drop fractions | 0.001, 0.005, 0.01, 0.05 → 48 / 243 / 486 / 2,430 events |
| Replicates | 3 per fraction, drop-list seed 2025, lists shared by all methods |
| Model seed | 42 for every full and dropped fit |
| Noise seeds | 7, 123 (full-data refits, recorded as fraction-0 rows) |
| Family configs | plain: K=1, 1,000 steps, lr 0.02; baseline: m=5, 5,000 steps, lr 0.005; multidim: m=5, 3,000 steps, lr 0.01, sigmoid link |
| Device | cuda |

Every agreement row was computed on the full common player set
(`n_common = 1455`): even at the 5% fraction no player lost all of their
events, so no ranking shrank.

## Seed-noise floors (fraction 0)

Alternate-seed full-data fits scored against the fixed-seed full fit. These
bands are the resolution limit: a drop-induced change smaller than the same
family's band is not a finding.

| Family | Seed | Kendall tau | Top-10 Jaccard | Top-25 Jaccard | Max top-25 displacement | Top-1 changed |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| plain | 7 | 0.808 | 0.667 | 0.667 | 186 | no |
| plain | 123 | 0.952 | 0.667 | 0.852 | 7 | no |
| baseline | 7 | 0.929 | 1.000 | 0.852 | 18 | **yes** |
| baseline | 123 | 0.926 | 1.000 | 0.923 | 18 | **yes** |
| multidim | 7 | 0.906 | 0.818 | 0.852 | 11 | no |
| multidim | 123 | 0.912 | 0.667 | 0.786 | 13 | no |

Two floor observations matter more than any drop curve:

- **Plain IRT has a bad-basin seed.** Seed 7 lands in a visibly different
  optimum (tau 0.808 against seed 42; a reference top-25 player displaced 186
  ranks). Its two-seed band is so wide that essentially no drop effect on the
  plain ranking is resolvable in this run.
- **Baseline CompIRT's #1 player is not seed-stable.** Both alternate seeds
  change the top-1, while its top-10 *membership* is seed-invariant
  (Jaccard 1.0 at both seeds) — the top set is stable, the order inside it is
  not. Any later top-1 or "narrow gap at the top" claim about the baseline
  must be read against this.

## Agreement vs. drop fraction

Mean Kendall tau over the 3 replicates (each method vs. its own full-data
ranking; per-replicate scatter is in the CSV and graphs):

| Method | 0.001 | 0.005 | 0.01 | 0.05 | own floor band |
| --- | ---: | ---: | ---: | ---: | --- |
| actual | 0.998 | 0.992 | 0.986 | 0.951 | none (deterministic) |
| plain | 0.997 | 0.989 | 0.984 | 0.954 | 0.808–0.952 |
| baseline | 0.975 | 0.955 | 0.954 | 0.924 | 0.926–0.929 |
| multidim | 0.994 | 0.967 | 0.973 | 0.934 | 0.906–0.912 |

Maximum displacement of a reference top-25 player, worst replicate per cell:

| Method | 0.001 | 0.005 | 0.01 | 0.05 | own floor |
| --- | ---: | ---: | ---: | ---: | ---: |
| actual | 2 | 3 | 3 | **58** | — |
| plain | 1 | 2 | 6 | 29 | 186 / 7 |
| baseline | 5 | 14 | 12 | 15 | 18 |
| multidim | 1 | 9 | 8 | **8** | 11–13 |

## Reading

**Applying the significance rule, the global-order data effect on the CompIRT
rankings is unresolved everywhere on this grid.** Multidim's tau stays above
its own seed band (0.906–0.912) at every fraction including 5%; baseline first
*reaches* its band (0.926–0.929) at the 5% fraction and never clearly exceeds
it. In other words: deleting up to 5% of buzz events moves the CompIRT global
rankings by at most about as much as re-randomizing SVI initialization does.
That is a statement about the resolution of the design, not proof of
robustness — a two-seed floor is a coarse band.

**The raw and plain curves sitting above the CompIRT curves is not evidence
against the graceful-degradation hypothesis.** Actual PPG is deterministic, so
its curve is pure data effect; the model curves bundle data effect and refit
jitter, which the floors show is the dominant term. The curves are comparable
across methods only after subtracting each family's own floor, and after that
subtraction the model curves are consistent with ≈ zero drop effect below 5%.

**The one clean cross-method signal is top-of-ranking fragility at 5%, and it
favors the models.** Raw actual PPG's global order is trivially stable, but an
individual top-25 player can crash 58 places when a random 5% deletion happens
to take several of their scoring events (the +10/−5 arithmetic has no way to
re-estimate a player whose observed events vanish). Multidim never moved a
top-25 player more than 8 places under any 5% replicate — *below* its own
seed jitter (11–13) — and baseline stayed ≤ 15 against a floor of 18. The
model-based rankings pool evidence across all remaining events and so
regularize exactly the players people actually look at. This asymmetry —
raw PPG robust in the aggregate, fragile per player; CompIRT the reverse — is
the finding to carry forward into Tier 2.

**Baseline top-1 flips under drops are uninformative.** `top1_changed` fires
in 3 of 12 baseline drop cells, but it also fires at both fraction-0 noise
seeds, so it carries no drop signal for that family.

`mean_abs_ppg_change` is score-scale and only comparable within a method
(plain PPG has no neg penalty; see the contract doc). For reference, the pure
data effect on actual PPG at 5% is ≈ 0.95 PPG mean absolute change.

## Status and next steps

- Tier 2 has not been run. The recommended invocation reuses this directory's
  full and noise-floor fits:

  ```bash
  .venv/bin/python run_scripts/common/run_targeted_drop.py \
      --reuse-full results/compirt/in_sample/common/drop-robustness
  ```

  Given the floors above, a Tier-2 result will only be meaningful for pairs
  whose gap change clearly exceeds `noise_gap_std`, and the baseline's
  seed-unstable top-1 makes the default smallest-gap-in-top-10 target worth
  checking against the multidim reference (`--reference-model multidim` is
  already the default).
- The plain-IRT seed-7 basin is worth one follow-up fit at another seed or
  two before quoting any plain-IRT floor: with two seeds we cannot tell an
  outlier basin from a genuinely wide floor.
- These are descriptive stability measurements on an in-sample, transductive
  fit — not confidence intervals, and not out-of-sample generalization.

## Artifacts

- `csvs/drop_robustness_metrics.csv` — every row behind the tables above
  (one per method × fraction × replicate, plus fraction-0 noise rows).
- `graphs/kendall_tau_vs_fraction.png`, `graphs/topk_jaccard_vs_fraction.png`
  — the curves with each family's floor band shaded.
- `droplists/frac_<α>/rep_<r>.txt` — the perturbations of record (shared by
  all methods; never regenerated once written).
- `<family>/{full,noisefloor/seed_<s>,frac_<α>/rep_<r>}/pyramidal/` — every
  fit's posterior tables and `summary.json`.
- `ablation_config.json`, `run.log` — resolved settings and the full log.
