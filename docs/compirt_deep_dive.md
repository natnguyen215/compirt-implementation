# Root CompIRT — End-to-End Deep Dive

This document explains how the **root (baseline) CompIRT** pipeline works from the
linked dataset all the way to evaluation reports, with a focus on **the functions
involved and the core logic inside each one**. It is the implementation-level
companion to [`README.md`](../README.md) (operational) and
[`compirt-experiments.md`](compirt-experiments.md) (setup, commands, assumptions).

The two topic variants are documented separately and described as *diffs* against
this baseline:
[`topic/fixed/topic_compirt_deep_dive.md`](../topic/fixed/topic_compirt_deep_dive.md)
(fixed topic mixture) and
[`topic/learned/joint_compirt_deep_dive.md`](../topic/learned/joint_compirt_deep_dive.md)
(jointly-learned topics). Read this one first.

---

## 0. The one idea behind everything

CompIRT is a **two-stage quizbowl item-response model**:

1. **Stage 1 (pyramidal / tossups)** learns, per player, a skill vector $\theta$
   and a confidence threshold $c$; per tossup, a discrimination vector $\alpha$
   and a difficulty curve $(\beta,\gamma,\mu)$. A tossup is read token by token and
   gets easier as clues accrue; the first player to buzz is modeled as a
   **competing risk** among the game's inferred lineup members.
2. **Stage 2 (compositional / bonuses)** holds $\theta$ **fixed** and learns how
   three-part bonus questions reward team skill, optionally with a pairwise
   **synergy** term.

The single correctness primitive is the **skill-minus-difficulty gap**:

$$\text{correctness logit} = \theta_i \cdot \alpha_j - b_j(t)$$

Everything else — hazard, survival, the competing-risks likelihood, the bonus
aggregation — is built on top of that gap. The topic variants replace
$\theta_i\cdot\alpha_j$ with a fixed/learned topic-weighted sum
$\sum_k r_{jk}\theta_{ik}$; the baseline keeps $\alpha$ a **free learned vector**.

---

## 1. Pipeline at a glance

Each stage writes files the next one reads — run them in this order.
`run_scripts/common/run_compirt.sh` (or `run_compirt.py`) chains the whole thing.

| # | Stage | Script(s) | Reads | Writes |
| --- | --- | --- | --- | --- |
| 1 | Stage 1 — pyramidal (tossups) | `train_pyramidal.py` + `pyramidal_model.py` | linked dataset | `players.csv` ($\theta$, $c$), `tossups.csv`, `tossup_predictions.csv`, `player_posterior.csv` |
| 2 | Stage 2 — compositional (bonuses) | `train_compositional.py` + `compositional_model.py` | $\theta$ (`players.csv`) + dataset | `bonus_parts.csv`, `*_predictions.csv`, `tau.txt` |
| 3 | Evaluate | `evaluate_compirt.py` + `compirt_eval/` | Stage 1 + Stage 2 outputs | metrics CSVs + plots + `experiment_report.md` |

One-line handoff chain: dataset → (Stage 1) → $\theta$ → (Stage 2) → predictions →
(evaluate) → report.

| Layer | Files | Role |
| --- | --- | --- |
| Data builders | `compirt_data.py` | Observations + padded tensors from the linked tables |
| Stage 1 | `train_pyramidal.py` + `pyramidal_model.py` | Tossup competing-risks buzz model → player skill $\theta$ |
| Stage 2 | `train_compositional.py` + `compositional_model.py` | Bonus-part model on fixed $\theta$ |
| Evaluation | `evaluate_compirt.py` + `compirt_eval/{tossups/,bonuses,metrics,figures}.py` | Scenario A/B metrics, plots, report |
| Held-out priors | `holdout/player_priors.py`, `utils/saving.py` | Train/test temporal split (§7) |
| Orchestration | `run_scripts/run_compirt.{sh,py}`, `run_compirt_holdout.py` | One-pass drivers reading env vars |

---

## 2. Data builders — `compirt_data.py`

The model never touches raw tables; these functions turn them into model-ready
tensors. (The topic scripts reuse these verbatim.)

- **`load_hf_tables(data_dir, split)` / `filter_tournament(tables, tournament)`** —
  load the linked dataset for a split (`"all"`, `"year_2024"`, `"year_2025"`) and
  optionally restrict to one tournament prefix (`TOURNAMENT=""` = whole split).
- **`build_tossup_observations(tables, lineups=None)`** — produces **one row per
  lineup member per game-tossup event**. The active players are the per-game
  **inferred lineups** from `lineup.py` (`LineupIndex.load_or_build`, cached under
  `data/lineups/`) — roughly the ~4 players who plausibly played each game, *not*
  the full registered roster. The actual first buzzer is `z="BUZZ"` with $y$ =
  correctness; lineup-mates who never got to buzz are `z="CENSORED"` with $y=$ NaN;
  a no-buzz event yields `z="NO-BUZZ"` rows. First buzzes are selected after
  sorting by token position with deterministic `buzz_id` tie-breaking, which
  excludes post-neg bounce-backs. It sets $t^*$ (first-buzz token, clamped
  to $[1, T_j]$) and $T_j$ (total tokens). **NO-BUZZ rows set $t^* = T_j$** — the
  "dead tossup" convention that makes Eq. 13 fall out implicitly.
- **`tossup_tensors(observations, device)`** — builds contiguous index spaces for
  players, tossups, and events, plus $t^*$, $T_j$, `is_buzz`, $y$, and the id
  lists. Row order of `data["player_ids"]` matches the $\theta$ rows the model
  samples — the contract Stage 2 and the held-out priors rely on.
- **`build_bonus_part_observations(tables, lineups=None)` / `bonus_tensors(observations, player_ids, device)`** —
  one row per team per bonus part, with a **padded roster** matrix and a
  `roster_mask` marking real vs. padded slots. Each bonus row reuses the
  **inferred lineup** of the tossup in the same cycle (same
  game/team/question-number → segment mapping), so aggregation and synergy also
  run over who plausibly played, not the registered roster.

---

## 3. Stage 1 — Pyramidal tossups (`pyramidal_model.py`)

For each player–tossup row the model factors the outcome into **correctness**,
**hazard** (buzz-now given not-yet), and **survival** (hasn't buzzed yet), then
combines all lineup members as **competing risks** for the event's first buzz.

### 3.1 Building-block functions (forward logic)

**`difficulty_curve(beta, gamma, mu, t, T_j)` — Eq. 3**

$$b_j(t) = \beta_j \cdot \sigma\!\left(\gamma_j\!\left(\mu_j - \tfrac{t}{T_j}\right)\right)$$

$\beta$ = amplitude/sign, $\gamma$ = transition sharpness, $\mu$ = inflection point
— all **scalars per tossup** (this is exactly what the topic variant makes
per-topic).

**`correctness_logit(theta, alpha, beta, gamma, mu, t, T_j)` — Eq. 4**

$$\theta_i \cdot \alpha_j - b_j(t)$$

The dot product $\theta_i\cdot\alpha_j$ is the discrimination-weighted skill; the
free $\alpha_j$ says how much each skill dimension matters for this tossup.

**`hazard_logit(..., c, ...)` — Eq. 5:** $\text{correctness\_logit} - c_i$. The
confidence $c_i$ shifts a player's whole buzz curve (higher $c$ = more reluctant).

**`log_survival(..., t_star, T_j)` — Eq. 6:** log-probability of *not* having buzzed
before $t^*$,

$$\log S_{ij}(t^*) = \sum_{s < t^*} \log\!\bigl(1 - h_{ij}(s)\bigr),$$

computed in log space via `F.logsigmoid(-logits)`. It builds a `positions` grid
$1\ldots\max(t^*)$, masks with $\text{positions} < t^*$, and broadcasts row
parameters with `unsqueeze(1)`. NO-BUZZ rows ($t^*=T_j$) contribute pure survival
over the whole question — **Eq. 13 enters here implicitly**.

### 3.2 Priors — `sample_parameters(data, n_dimensions)` (Eq. 14)

Inside two Pyro plates:

| Param | Prior | Shape |
| --- | --- | --- |
| $\theta$ | $\mathcal{N}(0, I)$ | $(n_\text{players}, n_\text{dim})$ |
| $c$ | $\mathcal{N}(0, 1)$ | $(n_\text{players},)$ |
| $\alpha$ | $\mathcal{N}(0, I)$ | $(n_\text{tossups}, n_\text{dim})$ |
| $\beta$ | $\mathcal{N}(0, 1)$ | $(n_\text{tossups},)$ |
| $\gamma$ | $\text{Half-Cauchy}(5)$ | $(n_\text{tossups},)$ |
| $\mu$ | $\text{Beta}(2, 2)$ | $(n_\text{tossups},)$ |

The $\theta$/$c$ priors are **the hook the held-out evaluation uses** (§7): the
function reads optional `theta_prior_loc/scale` and `c_prior_loc/scale` from
`data`, defaulting to the $\mathcal{N}(0,I)/\mathcal{N}(0,1)$ above, so a normal run
is unchanged.

### 3.3 Row indexing — `row_parameters(data, …)`

Gathers entity-level parameters down to observation rows:
`theta[player]`, `c[player]`, `alpha[tossup]`, `beta/gamma/mu[tossup]`.

### 3.4 The likelihood — `competing_risks_model(data, n_dimensions)` (Eq. 7/12)

Competing risks are not a built-in distribution, so the joint log-likelihood is
**hand-summed in log space and attached with `pyro.factor`**:

$$\log L = \sum_{\text{all rows}} \log S_{ij}(t^*) + \sum_{\text{buzz}} \log\sigma\!\bigl(h_{i^*j}(t^*)\bigr) + \sum_{\text{buzz}} \log\mathrm{Bernoulli}\!\bigl(y_{i^*j}\mid\sigma(\text{corr}_{i^*j})\bigr)$$

- **Survival** runs over *every* row (BUZZ + CENSORED + NO-BUZZ).
- **Hazard** and **correctness** apply only to the actual first buzzer $i^*$
  (sliced by `buzz = data["is_buzz"]`).
- **Optional recalibration** (`calibrate_correctness=True`, CLI
  `--calibrate-correctness`): samples a global scale
  $\sim\text{LogNormal}(0,0.5)$ and bias $\sim\mathcal{N}(0,3)$
  (`sample_correctness_calibration`) and applies them to the **correctness logit
  only** — hazard/timing keeps its base logit.

### 3.5 Replay & simulation

- **`posterior_row_predictions(data, posterior)`** replays Eq. 4/5/6 at the
  posterior medians → per-row `predicted_correct/hazard/survival`, so the saved CSV
  matches the training likelihood.
- **`expected_first_buzz_positions(data, posterior)`** regroups player-event rows
  into padded per-event rosters and walks token by token, treating players as
  independent hazards: $P(\text{first buzz at }t) = P(\text{no earlier buzz})\cdot
  \bigl(1 - \prod_m (1-h_m)\bigr)$. The returned position is **conditioned on a
  buzz occurring** — $E[t\mid\text{buzz}] = \sum_t t\,P(\text{first buzz at }t)
  \,/\,(1 - S_\text{event})$ — matching the observed-buzz events it is scored
  against; the question end is used only when the fitted buzz mass is
  numerically zero.

### 3.6 Driver — `train_pyramidal.py`

`run_experiment(args)`:

```text
load tables → build_tossup_observations → tossup_tensors
   → [held-out only] attach_player_priors (informative θ/c priors)
   → fit_svi(competing_risks_model, AutoNormal, ClippedAdam, Trace_ELBO)
   → save_parameters (players.csv, tossups.csv)
   → save_player_posterior (player_posterior.csv: θ/c loc+scale + tier)
   → posterior_row_predictions → tossup_predictions.csv + player_buzz_summary.csv
   → expected_first_buzz_positions → buzz_event_predictions.csv
   → summary.json
```

`fit_svi` returns `guide.median(...)` **and the guide itself** so
`save_player_posterior` can read the variational loc/scale, not just the median.
`players.csv` — specifically $\theta$ — is the **handoff to Stage 2**.

---

## 4. Stage 2 — Compositional bonuses (`compositional_model.py`)

Stage 2 holds $\theta$ **fixed** (loaded from Stage 1) and learns how bonus parts
turn team skill into points. One observation = one team attempting one part.

### 4.1 Building-block functions

**`lse_aggregation(member_abilities, roster_mask, tau)` — Eq. 8:** an unnormalized
smooth max over the roster,

$$A_b(R) = \tau \cdot \log \sum_{m\in R} \exp\!\left(\tfrac{a_{bm}}{\tau}\right),$$

where padded slots are `masked_fill`-ed to $-\infty$ so they drop out. $\tau$
controls how sharply the team score approaches its strongest member.

**`synergy_contribution(psi, roster, roster_mask)` — Eq. 10:** the summed pairwise
dot product over the upper triangle of active roster slots,
$\sum_{i<k\in R}\psi_i\cdot\psi_k$. Its sign is **not** interpretable as "teamwork
quality" without held-out recombined-roster validation.

### 4.2 The model — `compositional_model(data, theta, use_synergy, synergy_dimensions, calibrate_correctness, alpha_prior)` (Eq. 8/10/11)

1. Sample part discrimination $\alpha$ of shape $(n_\text{parts}, n_\text{dim})$
   from the prior named by `alpha_prior` (`alpha_distribution`): `"normal"`
   (default) is $\mathcal{N}(0,I)$ — signed loadings for a rotation-arbitrary
   Stage-1 basis; `"gamma"` is $\text{Gamma}(2,2)$ — nonnegative mean-1 loadings,
   only for a Stage-1 basis already pinned positive (the multidim `r`). Also
   sample part difficulty $\beta\sim\mathcal{N}(0,1)$ and aggregation temperature
   $\tau\sim\text{Half-Cauchy}(1)$ (outside the part plate — one shared scalar).
2. Member ability $a_{bm} = \alpha_b\cdot\theta_{p_m}$; aggregate with
   `lse_aggregation`; subtract $\beta_b$ → `logits`.
3. **Optional synergy:** sample $\psi\sim\mathcal{N}(0, 0.5\,I)$ and add the
   pairwise term.
4. **Optional recalibration** (`--calibrate-correctness`): Platt-scale the full
   part logit with the same LogNormal/Normal scale-and-bias priors as Stage 1.
5. Observe directly: `pyro.sample("obs", Bernoulli(logits=logits), obs=data["y"])`
   — a single built-in distribution, **no `pyro.factor`** (unlike Stage 1).

**`posterior_predictions(...)`** replays Eq. 8/10/11 at the medians →
`predicted_correct`, `aggregate`, `synergy`.

### 4.3 Driver — `train_compositional.py`

```text
load_player_skills (theta from Stage 1 players.csv, by player_id)
   → build_bonus_part_observations → keep only rows whose FULL roster has fitted θ
   → bonus_tensors → fit_svi(compositional_model, … theta fixed)
   → posterior_predictions
   → save bonus_parts.csv (beta, alpha_*), tau.txt
   → bonus_part_predictions.csv
   → team_predictions.csv  (expected_bonus_points = 10 · Σ part probabilities)
   → save_bonus_ppc  (posterior-predictive draws; off by default, --ppc-draws N)
   → [optional] save_synergy_outputs
   → summary.json (incl. synergy stats)
```

Key flags beyond the shared ones: `--use-synergy` / `--synergy-dimensions` /
`--save-synergy-details`, `--calibrate-correctness`, `--alpha-prior
{normal,gamma}`, and `--ppc-draws` / `--ppc-max-responses`.

**`load_player_skills(path, device)`** is the load-bearing handoff: it reads
`theta_1..K` by `player_id` and the `known_roster` filter drops any bonus row whose
roster contains a player without a fitted $\theta$. This same "freeze θ by
player_id, drop unknowns" mechanism is what the held-out path reuses across the
temporal split (§7).

---

## 5. Evaluation (`evaluate_compirt.py` + `compirt_eval/`)

`evaluate_compirt.py main()` is a thin rerunnable CLI. The Scenario A/B and
posterior-predictive diagnostics consume saved CSVs and never re-run training.
The optional match-winner simulation additionally loads the generated game
table; pass `--skip-game-simulation` when evaluating portable saved artifacts
without the local dataset.

- **`compirt_eval/tossups/` `evaluate_tossups` — Scenario A.** Reads
  `tossup_predictions.csv`, `players.csv`, `tossups.csv`; scores correctness on
  `z=="BUZZ"` rows (AUC, log-loss, **ECE**), draws aggregate and buzz-position
  stratified reliability, difficulty curves over empirical buzz locations, and
  $\theta/c/\alpha/\beta/\gamma/\mu$ parameter dashboards. It uses
  `buzz_event_predictions.csv` for buzz-position MAE/median error.
- **`compirt_eval/bonuses.py` `evaluate_bonuses` — Scenario B.** Part-level AUC /
  log-loss / part accuracy, strict all-three-parts exact accuracy, game-level
  PPB MAE, and part-level calibration.
- **`compirt_eval/metrics.py` / `figures.py`** hold the shared metric math and
  plotting primitives.

- **`compirt_eval/games.py` `simulate_match_winners`** — the optional
  match-winner diagnostic (`--game-simulations`, `--game-seed`); writes
  `game_metrics.csv`. **`compirt_eval/posterior_predictive.py`
  `evaluate_saved_ppc`** scores any saved bonus PPC draws.

Outputs land in `csvs/` and `graphs/` subdirectories of the evaluation root
(`compirt_eval/outputs.py`): `tossup_metrics.csv`, `bonus_metrics.csv`,
`game_metrics.csv`, a merged `prediction_diagnostics_by_stratum.csv`, plus
`experiment_report.md` and a generated eval-docs summary at the root.
Because these read only prediction CSVs, **the same evaluator scores single-split
or temporal-test predictions with no code change**. The temporal path is
transductive rather than fully inductive: the future split supplies the responses
used to co-estimate its player and item parameters (§7).

---

## 6. Orchestration — `run_scripts/run_compirt.{sh,py}`

A single env-var-driven driver that chains Stage 1 → Stage 2 → evaluate (and an
optional synergy bonus model + comparison). Key variables:

| Var | Effect |
| --- | --- |
| `SPLIT`, `TOURNAMENT` | Data selection (`TOURNAMENT=""` = whole split) |
| `ROOT` | Output directory for the whole run |
| `DIMENSIONS` | Latent skill dimensions $K$ |
| `PYRAMIDAL_STEPS`, `BONUS_STEPS`, `LR`, `SEED` | SVI budget + RNG seed |
| `RUN_SYNERGY`, `SYNERGY_DIMENSIONS`, `SAVE_SYNERGY_DETAILS` | Also fit + evaluate the synergy bonus model |
| `CALIBRATE_CORRECTNESS` | Pass `--calibrate-correctness` to both stages |
| `GPU` | CUDA card index — this runner is CUDA-only (`--device cuda` is hard-coded) |

`ROOT` passes through `resolve_result_root`, which redirects a bare
`results/compirt/<name>` into the `in_sample/` tier; all stage output is teed
into `<ROOT>/run.log` with a resolved-config header.

`run_compirt_2024.{sh,py}` is a reproducibility wrapper that validates the dataset
then calls the runner with all-2024 defaults.

Every pyramidal run simulates expected first-buzz positions.

---

## 7. In-sample vs. held-out (train/test) evaluation

Everything above trains and evaluates on the **same** `--split`, so the §5 metrics
are an **in-sample fit**: question and player parameters were estimated on the very
rows being scored — a model-inspection diagnostic, *not* a generalization estimate.

The repo also supports the paper's **primary temporal split** (paper §4.2): train
player skills on a historical split (`year_2024`) and report Scenario A/B on a
held-out future split (`year_2025`).

### What "transductive" means here

The 2025 questions are new packets, so their parameters
($\alpha, \beta, \gamma, \mu$) are **co-estimated on the 2025 responses** alongside
prediction — "co-estimating items and persons." What carries across the split is
the **player prior** (paper §4.2 / Appendix B):

- **Returning players** (seen in 2024): the prior on $\theta$ (and $c$) is their
  **2024 training posterior** — loc *and* scale, saved to `player_posterior.csv`.
- **New players** (~66% of 2025): a **tier-conditioned** population prior
  $\theta\sim\mathcal{N}(\mu_\text{tier},\Sigma_\text{tier})$, with moments
  estimated from 2024 players grouped by tournament tier
  (fall/winter/regionals/nationals). `--new-player-prior flat` selects the paper's
  $\mathcal{N}(0,I)$ ablation.

### How it works in code

- **Models read optional priors.** `sample_parameters` (§3.2) reads
  `theta_prior_loc/scale`, `c_prior_loc/scale` from `data`, defaulting to
  $\mathcal{N}(0,I)/\mathcal{N}(0,1)$ when absent — backward-compatible.
- **`holdout/player_priors.py`** builds those tensors: `player_tier_map`
  (player→tier from `teams`×`tournaments`), `estimate_tier_priors` (per-tier
  $\mu/\Sigma$ from the training posterior), `attach_player_priors`
  (returning→training posterior, new→tier prior, with an `n_dimensions` guard).
- **`utils/saving.save_player_posterior`** extracts the `AutoNormal` loc/scale plus
  each player's tier and writes `player_posterior.csv` on every Stage-1 run.
- **`train_pyramidal.py`** exposes `--train-posterior <player_posterior.csv>` and
  `--new-player-prior {tier,flat}` to switch a run into the held-out pass.

Stage 2 and the evaluator are **unchanged**: Stage 2 already freezes $\theta$ by
`player_id` and drops unknown-roster rows (few drops now, since new players got a
co-estimated $\theta$), and the evaluator only consumes prediction CSVs.

### Running it

`run_scripts/common/run_compirt_holdout.py` with `MODEL=baseline` chains the four steps:

```text
1. Stage-1 train on TRAIN_SPLIT (year_2024)   → <ROOT>/train/pyramidal  (+ player_posterior.csv)
2. Stage-1 HELD-OUT pass on TEST_SPLIT (year_2025, --train-posterior …)  → <ROOT>/holdout/pyramidal
3. Stage-2 on TEST_SPLIT using the held-out θ → <ROOT>/holdout/compositional
4. evaluate_compirt.py on the held-out predictions → <ROOT>/holdout/evaluation
```

The same script runs `MODEL=topic` and `MODEL=learned`; only the player-prior
machinery is shared — see those variants' deep dives for what each adds (the
learned variant additionally freezes its trained topic-word matrix).

---

## 8. Output layout

```text
results/compirt/in_sample/<run>/
                       full-data/in-sample experiment roots
results/compirt/holdout/<run>/
                       temporal train/test experiment roots
<ROOT>/pyramidal/      players.csv, player_posterior.csv, tossups.csv,
                       tossup_predictions.csv, buzz_event_predictions.csv,
                       player_buzz_summary.csv, summary.json, loss_curve.png
<ROOT>/compositional/  bonus_parts.csv, bonus_part_predictions.csv,
                       team_predictions.csv, tau.txt, summary.json
<ROOT>/synergy/        same as compositional + synergy details (if RUN_SYNERGY=1)
<ROOT>/evaluation/     csvs/ (tossup/bonus/game metrics, stratum diagnostics),
                       graphs/, experiment_report.md
```

A held-out run (`run_compirt_holdout.py`) nests these under `<ROOT>/train/` and
`<ROOT>/holdout/`.

---

## 9. Mental-model summary (and the gotchas)

- **One primitive, $\theta_i\cdot\alpha_j - b_j(t)$**, drives correctness, hazard,
  and survival; the bonus stage swaps the dot product for an LSE over the roster.
- **The competing-risks population is the inferred lineup** (`lineup.py`, cached
  under `data/lineups/`), not the registered roster — both stages' observation
  builders resolve players through it.
- **Stage 1 likelihood is hand-built (`pyro.factor`)**; Stage 2 is a plain observed
  `Bernoulli`.
- **NO-BUZZ rows set $t^*=T_j$** — that single convention is how dead tossups
  (Eq. 13) enter the survival sum.
- **Stage 1 → Stage 2 handoff is $\theta$** via `players.csv`; bonus rows with any
  unfitted roster member are dropped.
- **Synergy sign is not interpretable** without held-out recombined-roster
  validation.
- **Default runs are in-sample.** The held-out train/test evaluation (§7) is a
  separate mode (`run_compirt_holdout.py`) that only changes the **player prior**;
  question parameters are still co-estimated transductively on the test split.
- **The evaluator is model-agnostic** — it consumes prediction CSVs, so baseline,
  topic, and learned variants all reuse it (the learned variant even reuses this
  exact `evaluate_compirt.py`).

| Paper eq. | Function |
| --- | --- |
| Eq. 3 difficulty | `difficulty_curve` |
| Eq. 4 correctness | `correctness_logit` |
| Eq. 5 hazard | `hazard_logit` |
| Eq. 6 survival | `log_survival` |
| Eq. 7/12 tossup likelihood | `competing_risks_model` |
| Eq. 8 aggregate | `lse_aggregation` |
| Eq. 10 synergy | `synergy_contribution` |
| Eq. 11 bonus outcome | `compositional_model` |
| Eq. 13 dead tossup | implicit ($t^*=T_j$ on NO-BUZZ rows) |
| Eq. 14 priors | `sample_parameters` / `compositional_model` |
