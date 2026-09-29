# Team IRT 3D: identifiability and what the axes track

Model: `P = sigmoid(sum_k r_bk * (theta_tk - beta_bk))`, with `r_b ~ Dirichlet(1)`
and `theta, beta ~ Normal(0, 1)`. The analysis reads the saved fits plus three
fold-0 refits on identical data: seeds 43 and 44, and seed 42 with the `beta`
prior mean moved to `(1, 0, -1)`. Nothing else is trained. Full numbers are in
[output.txt](output.txt). All results are for fold 0 unless noted.

```bash
CUDA_VISIBLE_DEVICES=1 .venv/bin/python -B <this dir>/code/refit.py
.venv/bin/python -B <this dir>/code/analyze.py
```

## What the data determine

| Quantity | Identified? | Evidence |
| --- | --- | --- |
| Per-axis difficulty `beta_bk` | **No.** Only `r_b · beta_b` is identified | Moving `beta_b` 3 units orthogonal to `r_b` changes no logit (max 2e-15). Fitted `beta_b` is the prior's minimum-norm split `(r_b·beta_b) r_b / \|r_b\|²` (R² 0.947). With the shifted prior, the per-axis means move from (−0.12, 0.07, 0.08) to (1.14, −0.01, −1.14). Effective difficulty (Spearman 0.983) and training probabilities (corr 0.992) stay within seed-to-seed variation (0.982–0.989 and 0.991–0.995). |
| Effective difficulty `r_b · beta_b` | Within a question set | Across seeds, Spearman 0.98–0.99; across folds, 0.973. Within each set it tracks declared easy < medium < hard at 0.860 (DD multidim: 0.877). |
| Difficulty across question sets | **No** | Teams are tournament-specific, so the four 2024 sets are disconnected blocks of the team–part graph. Shifting one set's `theta` and `beta` together leaves the likelihood unchanged. The fitted mean difficulty of every set is about 0 (−0.11 to 0.01), even though conversion ranges from 43% to 60%. The gap goes into mean team skill instead: +0.25 for Fall, −0.62 for Nationals. DD multidim, whose players link the sets, orders them Fall −0.94, Regionals −0.56, Winter −0.51, Nationals +0.41. |
| Relevance `r_b` and team skills `theta_t` | Up to relabelling the axes separately in each set | The data narrow `r` from the prior's 95% width of 0.83 to 0.20. Relabelling one set's axes leaves the likelihood unchanged. Across seeds, per-axis `r` Spearman is 0.27–0.51 under one global permutation but 0.82–0.93 under per-set permutations. Across folds, the axes kept the same labels in only 1 of 10 pairs. |

## What the axes track: part difficulty, not subject

- **Declared difficulty dominates.** Within a set, declared difficulty explains
  54.0% of the variance in `r` (chance 0.2%). Category explains 4.7% (chance 1.1%),
  subcategory 3.1%, and part position 1.7%.
- **Each set has an easy axis, a hard axis, and a mixed axis.** One axis carries
  the easy parts (mean `r` 0.69–0.75), another the hard parts (0.52–0.69). Medium
  parts spread roughly evenly (largest mean share 0.34–0.43).
- **The roles recur; the labels don't.** All five folds and all three refits show
  the same structure (η² 0.52–0.56). Which axis number is easy or hard changes
  between sets, folds, and seeds. The Regionals set, for example, uses axis 2 for
  easy and axis 1 for hard.
- **Top-loaded parts confirm it.** The top decile of the easy axis is 96–100% easy
  parts, and of the hard axis 87–100% hard parts. Their distinctive words and
  answers are generic and mix subjects. Literature leans on Winter's mixed axis
  (56%) and Fall's hard axis (42%), but on no Nationals axis (26% at most).
- **Team skills follow the same roles.** After aligning axes to roles, `theta_easy`
  tracks a team's easy-part conversion (Spearman 0.70) and `theta_hard` its
  hard-part conversion (0.67). The hard-minus-easy contrast tracks the
  corresponding conversion gap (0.49). Within-set correlations between the easy
  and hard skills range from −0.15 to 0.35. Role contrasts against subject
  conversion gaps give |ρ| ≤ 0.24 for every category.
- **Comparison with other 3D models:**
  - Old Team IRT 3D (Gamma loadings; η² of loading shares): 0.171 by declared difficulty, 0.069 by category.
  - DD multidim difficulty (η² of `r`): 0.046 by declared difficulty, 0.113 by category.

## Reading per-axis difficulty

`beta_bk` has no meaning of its own. It is the prior's split of the part's one
identified difficulty, in proportion to `r_b`. An easy part puts almost all its
weight on the easy axis, so its `beta` on that axis approximates its effective
difficulty. Its other coordinates stay near the prior mean. Two changes are
needed to make separate per-axis difficulties identifiable:

- `beta_bk` has to enter the likelihood nonlinearly, for example a noncompensatory
  `P = prod_k sigmoid(theta_tk - beta_bk)^r_bk`.
- Question sets have to be linked, for example through player-level skills or
  shared anchor questions.

## Caveats

- Most tests use fold 0; the folds share about 80% of their training games.
- Parameters are mean-field AutoNormal medians.
- Refits differ from the saved fit by up to 0.37–0.46 in individual training
  probabilities, so the 3D optimum is seed-dependent. The held-out comparison uses
  seed 42 only.
- The Regionals set has no category labels.
