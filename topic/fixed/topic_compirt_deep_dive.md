# Topic CompIRT — End-to-End Deep Dive

This document explains how the `topic_compirt` pipeline works from raw question
text all the way to evaluation reports, with a focus on **the functions
involved and the core logic inside each one**. It is the implementation-level
companion to [`README.md`](README.md) (operational), [`equation_flow.md`](equation_flow.md)
(the math in paper-equation order), and [`equation_changes.md`](equation_changes.md)
(the prototype→current diff).

---

## 0. The one idea behind everything

Root CompIRT learns, for each question, a **free discrimination vector**
$\alpha$ that says how much each latent skill dimension matters. Topic CompIRT
throws that away and instead **fixes** a normalized **topic mixture** $r$ per
question — built from PLDA, LDA, or category one-hots — and learns a *per-topic
difficulty* where root learned a scalar.

So everywhere root writes $\theta \cdot \alpha$, the topic model writes
$\sum_k r_k \, \theta_k$, and $r$ is a constant input, not a sampled parameter.
That single substitution ripples through both modeling stages. Keep this in mind
and the rest follows:

$$\text{root correctness:} \quad \theta_i \cdot \alpha_j - b_j(t)$$

$$\text{topic correctness:} \quad \sum_k r_{jk}\bigl(\theta_{ik} - d_{jk}(t)\bigr)$$

where $r$ replaces $\alpha$ and difficulty becomes per-topic, pushed *inside* the
weighted sum.

---

## 1. Pipeline at a glance

Each stage writes files the next one reads — run them in this order.
`run_topic_compirt.sh` chains the whole thing.

| # | Stage | Script(s) | Reads | Writes |
| --- | --- | --- | --- | --- |
| 1 | Build topic vectors | `run_plda.py` / `run_lda.py` / `build_category_vectors.py` | `database.db` | `document_latent_vectors.csv` (the fixed $r$) |
| 2 | Stage 1 — pyramidal (tossups) | `train_topic_pyramidal.py` + `topic_compirt/pyramidal.py` | $r$ CSV + linked dataset | `players.csv` ($\theta$), `tossups.csv`, `tossup_predictions.csv` |
| 3 | Stage 2 — compositional (bonuses) | `train_topic_compositional.py` + `topic_compirt/compositional.py` | $\theta$ (`players.csv`) + $r$ CSV + dataset | `bonus_parts.csv`, `*_predictions.csv` |
| 4 | Evaluate | `evaluate_topic_compirt.py` + `topic_compirt/evaluation.py` | Stage 1 + Stage 2 outputs | metrics + plots + `experiment_report.md` |

The handoff chain in one line: `database.db` → $r$ CSV → (Stage 1) → $\theta$ →
(Stage 2) → predictions → (evaluate) → report. The next table breaks the same
components down by responsibility rather than run order.

| Layer | Files | Role |
| --- | --- | --- |
| Topic vectors | `run_plda.py`, `run_lda.py`, `build_category_vectors.py`, `topic/utils/` | Produce `document_latent_vectors.csv` = the fixed $r$ |
| Vector plumbing | `topic_compirt/topics.py` | Load / normalize / align $r$ onto model tensors |
| Shared infra | `topic_compirt/common.py`, root `compirt_data.py` | SVI loop; observation/tensor builders (reused from root) |
| Stage 1 | `train_topic_pyramidal.py` + `topic_compirt/pyramidal.py` | Tossup competing-risks buzz model → player skill $\theta$ |
| Stage 2 | `train_topic_compositional.py` + `topic_compirt/compositional.py` | Bonus-part model on fixed $\theta$ |
| Evaluation | `evaluate_topic_compirt.py` + `topic_compirt/evaluation.py` | Metrics, reliability/timing/parameter plots, report |
| Orchestration | `run_topic_compirt.sh` | One-pass driver reading env vars |

The package `topic_compirt/` itself is only five modules:
`topics.py` (data plumbing), `pyramidal.py` (Stage 1 model), `compositional.py`
(Stage 2 model), `evaluation.py` (plots/metrics), `common.py` (SVI + helpers).

---

## 2. Stage 0 — Building the fixed topic vector $r$

The goal of this stage is a single CSV, `document_latent_vectors.csv`, with
columns `document_id`, `question_type`, and one or more `latent_topic_NN`
columns. Each row is the $r$ vector for one tossup or bonus.

### 2a. Corpus loading — `topic/utils/corpus.py`

- **`load_documents(database, question_type)`** opens `data/database.db`
  read-only and runs two SQL queries (one for tossups, one for bonuses). The
  important part is how it builds `document_id`: it concatenates
  `question_set::edition::p<packet_id>::q<question_number>` (tossups) or
  `...::b<question_number>` (bonuses). **This is the join key** that must match
  the IDs CompIRT uses for tossups/bonuses, which is why the README warns you to
  regenerate vectors with CompIRT-compatible IDs. For bonuses, the text is
  `leadin + GROUP_CONCAT(parts)` — the whole bonus is one document, so all three
  parts share one $r$.
- **`tokenize(value)`** → `clean_text` (strips HTML via `TextExtractor`,
  unescapes entities, collapses whitespace) → lowercase → `TOKEN_RE` content
  words of length > 2 → drops `STOPWORDS` (quizbowl boilerplate like "points",
  "name", "question"). The point is to make topics key on *subject* content
  ("Napoleon", "mitochondria") not phrasing.
- **`labels_from_row(row)`** builds hierarchical labels
  (`category:…`, `subcategory:…/…`, `subsubcategory:…/…/…`) used to *supervise*
  PLDA. They structure training but are **not** exported as topic gates.

### 2b. PLDA — `run_plda.py` (the main source)

Uses `tomotopy.PLDAModel` (partially labeled LDA). Key functions:

- **`train_model(...)`** creates the model with `latent_topics=dimensions`,
  `topics_per_label=1`, adds each document with its labels, and trains in
  `train_interval`-sized chunks, logging `ll_per_word`. It tracks
  `added_documents` because tomotopy may drop a doc whose words all fall below
  `min_df`; the kept list stays aligned one-to-one with `model.docs`.
- **`topic_name(model, topic_id)`** disentangles the layout: tomotopy lays out
  label-guided topics first ($\lvert\text{topic\_label\_dict}\rvert \times
  \text{topics\_per\_label}$ of them), then the shared latent topics. Anything
  past the label block is the `latent_id`-th shared latent topic.
- **`write_document_vectors(...)`** is where $r$ is born. For each doc it calls
  `doc.get_topic_dist()` and **slices out only the shared latent block**
  (`topic_dist[label_topic_count : label_topic_count + dimensions]`). The label
  topics are dropped. `latent_mass` records how much of the distribution that
  slice held. Rows are written via `topic.utils.outputs.document_vector_row`.

So the exported $r$ is the document's mixture over the *shared latent* topics
only — label topics merely shaped training.

### 2c. The CSV schema — `topic/utils/outputs.py`

- **`latent_topic_columns(d)`** → `latent_topic_00, latent_topic_01, …`
- **`document_vector_fieldnames(d)`** and **`document_vector_row(source, dist)`**
  fix the schema so PLDA, LDA, and category builders all emit identical CSVs.
- **`load_dimension_labels(path)`** reads an optional `dimension,column,category`
  CSV into 1-based dimension→name labels, used only for plot legends downstream.
- Also defines the canonical paths (`REPO_ROOT`, `DEFAULT_TOPIC_VECTORS`, etc.)
  that the rest of the pipeline imports.

### 2d. Alternatives

- **`run_lda.py`** — same corpus and schema, no label supervision (plain LDA).
- **`build_category_vectors.py`** — replaces learned topics with one-hot
  top-level category flags; emits `category_index.csv` naming each dimension.
  Prints the dimension count (currently 13) you must pass as `DIMENSIONS`.

All three are interchangeable downstream because they emit the same CSV
contract. The model never knows or cares which source produced $r$.

---

## 3. The heart of the package — `topic_compirt/topics.py`

This module is the bridge between "a CSV of topic vectors" and "a tensor aligned
to the model's rows." Everything in it exists to guarantee that row $i$ of
`data["topic_weight"]` is the correct $r$ for entity $i$, in the right order, on
the right device.

| Function | Core logic |
| --- | --- |
| `topic_columns(frame)` | Regex-match `latent_topic_(\d+)`, **sort by numeric suffix** so dimension order is stable regardless of CSV column order. |
| `load_topic_dataframe(path, question_type, expected_dimensions)` | Read CSV (`document_id` as str), optionally filter to `tossup`/`bonus`, validate columns/dimension count, reject duplicate IDs, reject NaN/inf and **zero-mass rows**, then **$L_1$-normalize each row so $\sum_k r_k = 1$**, index by `document_id`. |
| `align_topic_vectors(frame, columns, ids)` | Reorder rows to exactly match a requested id list; **raises with a preview if any id is missing** a vector (fail-loud, never silently zero-fill). |
| `bonus_id_from_part_id(part_id)` | Strip the `::part-N` suffix to recover the base bonus id (all parts share one $r$). |
| `align_tossup_topic_weights(data, path, dims)` | Filter to `tossup`, align to `data["tossup_ids"]`, return a `float32` tensor on `data["y"].device`. |
| `align_bonus_topic_weights(data, path, dims)` | Filter to `bonus`, map each `part_id` → base `bonus_id`, align to `data["part_ids"]`, return tensor on device. |

Two subtleties worth internalizing:

1. **Re-normalization happens here, not in the builder.** The builders emit
   positive finite mass; `load_topic_dataframe` does the $L_1$ normalization so
   $r$ is a proper distribution at train time. (This is why the README says rows
   "just need positive finite mass.")
2. **Bonus parts share a vector.** Because the topic vector is per *bonus*, the
   alignment maps every `bonus_id::part-N` back to its base bonus and looks up
   the single shared $r_b$. So parts 1, 2, 3 of a bonus get identical topic
   weights but different learned difficulties $\beta_{bk}$.

The output tensor is stored as `data["topic_weight"]` and indexed *by tossup* or
*by part* (not by observation row) — the model modules re-index it per row.

---

## 4. Shared infrastructure

### 4a. `topic_compirt/common.py`

- **`add_repo_root_to_path()`** inserts the repo root on `sys.path` so the
  topic-side scripts can `import compirt_data`, `compositional_model`, etc. from
  the root project. (This is why the training scripts call it before their
  root imports.)
- **`fit_svi(model, model_args, n_steps, lr)`** is the standard training loop
  used by both stages: clears the Pyro param store, builds an **`AutoNormal`**
  mean-field guide, runs **`SVI`** with **`ClippedAdam`** against **`Trace_ELBO`**,
  logs ELBO every 100 steps, and returns **`guide.median(*model_args)`** (the
  posterior point estimates) plus the loss trace. Both stages get their
  "posterior" from this single function.
- **`tensor_values`** / **`add_numbered_tensor_columns`** — detach→CPU→NumPy and
  expand a $(\text{rows}, \text{dims})$ tensor into columns like
  `theta_1, theta_2, …` for CSV output.

### 4b. Reused root data builders — `compirt_data.py`

The topic scripts do **not** reimplement data prep; they reuse root functions:

- **`load_hf_tables` / `filter_tournament`** — load the linked dataset and
  optionally restrict to one tournament (or use the whole split when
  `TOURNAMENT=""`).
- **`build_tossup_observations(tables)`** — produces **one row per rostered
  player per game-tossup event**. For the actual first buzzer the row is
  `z="BUZZ"` with $y$ = correctness; teammates who didn't get to buzz are
  `z="CENSORED"` with $y=\text{NaN}$; a no-buzz event yields `z="NO-BUZZ"` rows.
  It sets $t^*$ (first-buzz token, clamped to $[1, T_j]$) and $T_j$ (total
  tokens). Critically, **NO-BUZZ rows set $t^* = T_j$** — the "dead tossup"
  convention.
- **`tossup_tensors(observations, device)`** — builds contiguous index spaces for
  players, tossups, and events, plus $t^*$, $T_j$, `is_buzz`, $y$, and the id
  lists. This `data` dict is what `align_tossup_topic_weights` then augments with
  `topic_weight`.
- **`build_bonus_part_observations` / `bonus_tensors`** — one row per team per
  bonus part, with a **padded roster** matrix and a `roster_mask` marking real
  vs. padded slots.

---

## 5. Stage 1 — Pyramidal tossups (`topic_compirt/pyramidal.py`)

A tossup reveals clues token by token; difficulty falls as more is read. For
each player–tossup row the model factors the outcome into **correctness**,
**hazard** (buzz-now-given-not-yet), and **survival** (hasn't buzzed yet), then
combines all rostered players as **competing risks** for the event's first buzz.

### 5.1 The building-block functions (forward logic)

**`difficulty_curve(beta, gamma, mu, t, T_j)` — Eq. 3, made per-topic**

$$d_{jk}(t) = \beta_{jk} \cdot \sigma\!\left( \gamma_{jk}\!\left( \mu_{jk} - \frac{t}{T_j} \right) \right)$$

$\beta$ = amplitude/sign, $\gamma$ = transition sharpness, $\mu$ = inflection
point — one of each **per topic $k$**. The relative position $t/T_j$ gets a
trailing axis (`unsqueeze(-1)`) so it broadcasts across the topic dimension.

**`topic_weighted_skill(theta, topic_weight)`** $= \sum_k r_{jk}\,\theta_{ik}$ (a
dot product over topics).

**`correctness_logit(theta, topic_weight, beta, gamma, mu, t, T_j)` — Eq. 4**

$$\sum_k r_{jk}\bigl(\theta_{ik} - d_{jk}(t)\bigr)$$

This is the CAIMIRA-style **relevance-gap**: difficulty is subtracted *inside*
the weighted sum, so a player only pays a topic's difficulty to the extent the
tossup weights that topic.

**`hazard_logit(..., c, ...)` — Eq. 5:** $\text{correctness\_logit} - c_i$.
Confidence $c_i$ shifts a player's whole buzz curve (higher $c$ = more reluctant).

**`log_survival(..., t_star, T_j)` — Eq. 6:** probability of *not* having buzzed
before $t^*$:

$$\log S_{ij}(t^*) = \sum_{s \,<\, t^*} \log\!\bigl(1 - h_{ij}(s)\bigr)$$

Computed in log space via `F.logsigmoid(-logits)` for stability. It builds a
`positions` grid $1 \ldots \max(t^*)$, masks with $\text{positions} < t^*$, and
broadcasts row parameters against every position by `unsqueeze(1)`. NO-BUZZ rows
(with $t^* = T_j$) therefore contribute pure survival over the whole question —
this is how **Eq. 13 (dead tossups)** enters implicitly.

### 5.2 Priors — `sample_parameters(data, n_dimensions)` (Eq. 14)

Inside two Pyro plates:

| Param | Prior | Shape | vs. root |
| --- | --- | --- | --- |
| $\theta$ | $\mathcal{N}(0, I)$ | $(n_\text{players}, n_\text{dim})$ | unchanged |
| $c$ | $\mathcal{N}(0, 1)$ | $(n_\text{players},)$ | unchanged |
| $\beta$ | $\mathcal{N}(0, I)$ | $(n_\text{tossups}, n_\text{dim})$ | **per-topic** (root: scalar) |
| $\gamma$ | $\text{Half-Cauchy}(5)$ | $(n_\text{tossups}, n_\text{dim})$ | **per-topic** |
| $\mu$ | $\text{Beta}(2, 2)$ | $(n_\text{tossups}, n_\text{dim})$ | **per-topic** |

There is **no $\alpha$** — the fixed $r$ (in `data["topic_weight"]`) plays its
role and is never sampled. `.to_event(1)` makes each row's vector one joint event.

### 5.3 Row indexing — `row_parameters(data, ...)`

Entity-level parameters are gathered to observation rows:
`theta[player]`, `c[player]`, **`data["topic_weight"][tossup]`**, `beta[tossup]`,
`gamma[tossup]`, `mu[tossup]`. Note `topic_weight` is stored by tossup and
indexed with the same `tossup` vector, keeping each row's fixed $r$ aligned with
that row's learned per-topic difficulty.

### 5.4 The likelihood — `competing_risks_model(data, n_dimensions, calibrate_correctness)` (Eq. 7/12)

The competing-risks likelihood is not a built-in distribution, so it's
**hand-summed in log space and attached with `pyro.factor`**:

$$\log L = \sum_{\text{all rows}} \log S_{ij}(t^*) \;+\; \sum_{\text{buzz}} \log \sigma\!\bigl(h_{i^*j}(t^*)\bigr) \;+\; \sum_{\text{buzz}} \log \mathrm{Bernoulli}\!\bigl(y_{i^*j} \mid \sigma(\text{corr}_{i^*j})\bigr)$$

- The **survival** term runs over *every* row (BUZZ + CENSORED + NO-BUZZ).
- The **hazard** and **correctness** terms apply only to the actual first buzzer
  $i^*$ (sliced by `buzz = data["is_buzz"]`).

In code: `survival.sum() + F.logsigmoid(buzz_logits).sum() +
dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()`.

**Calibration:** if `calibrate_correctness=True`, `sample_correctness_calibration`
draws a global $\text{scale} \sim \text{LogNormal}(0, 0.5)$ and
$\text{bias} \sim \mathcal{N}(0, 3)$, and only the **correctness** logit is
Platt-scaled, $\text{scale}\cdot\text{logit} + \text{bias}$. The hazard/timing
path — which also calls `correctness_logit` — is deliberately left untouched, so
calibration fixes correctness probabilities without distorting buzz timing.

### 5.5 Replay & simulation

- **`posterior_row_predictions(data, posterior, calibrate_correctness)`** replays
  Eq. 4/5/6 at the posterior medians to produce per-row `predicted_correct`,
  `predicted_hazard`, `predicted_survival` — guaranteeing the saved CSV matches
  the training likelihood. Applies the same Platt scaling to correctness if set.
- **`expected_first_buzz_positions(data, posterior)`** simulates the **team**
  first-buzz distribution. It regroups player-event rows into a padded
  per-event roster, then walks token by token computing

  $$P(\text{first buzz at } t) = P(\text{no earlier team buzz}) \cdot P(\geq 1 \text{ buzzes now}).$$

  Players are treated as **independent hazards**, so
  $P(\text{nobody buzzes}) = \prod_m (1 - h_m)$ and
  $\text{total\_hazard} = 1 - \prod_m (1 - h_m)$. Leftover survival mass at the
  end goes to the question end ($\text{expected} \mathrel{+}= T_j \cdot
  \text{event\_survival}$). Returns expected relative position per event.

### 5.6 Driver — `train_topic_pyramidal.py`

`run_experiment(args)` is the orchestration spine:

```text
load tables → build_tossup_observations → tossup_tensors
   → align_tossup_topic_weights (attach data["topic_weight"])
   → train_model = fit_svi(competing_risks_model, …)
   → save_topic_parameters (players.csv, tossups.csv)
   → posterior_row_predictions → tossup_predictions.csv + save_player_rankings
   → [optional] expected_first_buzz_positions → buzz_event_predictions.csv
   → summary.json
```

`save_topic_parameters` writes `players.csv` ($c$, `theta_*`, `theta_norm`) and
`tossups.csv` (`beta_*`, `gamma_*`, `mu_*`, **and the fixed `topic_weight_*`** so
evaluation can reconstruct curves). `players.csv` — specifically the learned
$\theta$ — is the **handoff to Stage 2**.

---

## 6. Stage 2 — Compositional bonuses (`topic_compirt/compositional.py`)

Stage 2 holds $\theta$ **fixed** (loaded from Stage 1) and learns how bonus parts
convert team skill into points. One observation = one team attempting one part.

### 6.1 Building-block functions

**`topic_weighted_member_abilities(member_theta, topic_weight)` — Eq. 8 member score**

$$a_{bm} = \sum_k r_{bk} \cdot \theta_{pk} \quad (\text{per roster member } m)$$

`member_theta` is $(n_\text{obs}, \text{max\_roster}, n_\text{dim})$;
`topic_weight` is $(n_\text{obs}, n_\text{dim})$ and gets `unsqueeze(1)` to line
up with every roster slot.

**`lse_aggregation(member_abilities, roster_mask, tau)`** (reused unchanged from
root `compositional_model.py`) — the **unnormalized smooth max** over the roster:

$$A_b(R) = \tau \cdot \log \sum_{m \in R} \exp\!\left( \frac{a_{bm}}{\tau} \right)$$

Padded slots are `masked_fill`-ed to $-\infty$ so they drop out of the logsumexp.
$\tau$ controls how sharply the team score approaches its strongest member.

**`topic_weighted_part_difficulty(part_beta, topic_weight)`**
$= \sum_k r_{bk} \cdot \beta_{bk}$, the scalar part difficulty collapsed against
the same fixed $r_b$.

### 6.2 The model — `compositional_model(data, theta, use_synergy, synergy_dimensions, calibrate_correctness)` (Eq. 8/10/11)

$$\eta_{rb} = A_b(R_r) - \sum_k r_{bk} \cdot \beta_{bk} \quad (+\; \text{synergy})$$

$$y_{rb} \sim \mathrm{Bernoulli}\!\bigl(\sigma(\eta_{rb})\bigr)$$

Logic flow:

1. Sample per-topic part difficulty $\beta \sim \mathcal{N}(0, I)$, shape
   $(n_\text{parts}, n_\text{dim})$ (no $\alpha$), and
   $\tau \sim \text{Half-Cauchy}(1)$.
2. Index $\beta$, `topic_weight`, and $\theta$ to rows; compute member abilities,
   aggregate with `lse_aggregation`, subtract weighted difficulty → `logits`.
3. **Optional synergy** (`use_synergy`): sample
   $\psi \sim \mathcal{N}(0, 0.5\,I)$ of width `synergy_dimensions`, add
   **`synergy_contribution(psi, roster, roster_mask)`** — Eq. 10's pairwise term

   $$\text{synergy}(R) = \sum_{\substack{i < k \\ i,k \in R}} \psi_i \cdot \psi_k$$

   over the upper triangle of roster slot pairs (active pairs only). Synergy is
   **independent of $r$ and $\theta$**; it's the root pairwise term and its sign
   is not interpretable without held-out recombined-roster validation.
4. **Optional calibration:** Platt-scale the whole logit
   ($\text{scale}\cdot\text{logit} + \text{bias}$), the bonus parallel of the
   Stage 1 fix.
5. Observe directly: `pyro.sample("obs", Bernoulli(logits=logits), obs=data["y"])`.
   Unlike Stage 1, this is a single built-in distribution, no `pyro.factor`.

> **Why subtracting difficulty outside the smooth max is valid:** log-sum-exp is
> shift-equivariant, so subtracting a per-part constant outside the aggregation
> equals subtracting it inside each member score. See `equation_changes.md`.

**`posterior_predictions(...)`** replays Eq. 8/10/11 at the medians to produce
per-row `predicted_correct`, `aggregate`, and `synergy`.

### 6.3 Driver — `train_topic_compositional.py`

```text
load_player_skills (theta from Stage 1 players.csv)
   → build_bonus_part_observations → keep only rows whose FULL roster has fitted θ
   → bonus_tensors → align_bonus_topic_weights (attach data["topic_weight"])
   → train_model = fit_svi(compositional_model, … theta fixed)
   → posterior_predictions
   → save bonus_parts.csv (beta_*, topic_weight_*), tau.txt
   → bonus_part_predictions.csv
   → team_predictions.csv  (expected_bonus_points = 10 · Σ part probabilities)
   → [optional] save_synergy_outputs
   → summary.json (incl. synergy stats: mean/median/negative fraction)
```

The roster filter is important: a bonus row is dropped unless **every** roster
member has a $\theta$ from Stage 1 (`known_roster`), since Stage 2 can't score an
unknown player. `expected_bonus_points` turns three part-correct probabilities
into expected points, $10 \cdot \sum_{\text{parts}} p$.

---

## 7. Evaluation (`topic_compirt/evaluation.py` + `evaluate_topic_compirt.py`)

`evaluate_topic_compirt.py` is a thin CLI: it parses result paths, optionally
loads dimension labels (`--topic-names`), and calls
**`evaluation.evaluate_topic_compirt`**, which:

1. **`evaluate_topic_tossups(pyramidal_results, …)`** — scores correctness on
   `z=="BUZZ"` rows (`classification_metrics`), draws `reliability_plot` and
   `stratified_tossup_reliability_plot`, and produces the topic-specific plots:
   - **`topic_difficulty_plot`** / **`_weighted_topic_difficulty`** — reconstructs
     the *effective* weighted difficulty curve
     $\sum_k r_k\,\beta_k\,\sigma\!\bigl(\gamma_k(\mu_k - \text{pos})\bigr)$ from
     saved params and overlays empirical buzz histograms.
   - **`topic_buzz_density_fit_plot`** / **`topic_first_buzz_distribution`** /
     **`_aggregate_topic_buzz_timing`** — a pure-NumPy replay of the team
     first-buzz simulation (mirrors `expected_first_buzz_positions`), comparing
     predicted vs. empirical first-buzz mass and reporting total-variation
     distance and dead-event rates.
   - **`topic_pyramidal_parameter_distribution_plots`** — dashboards of $\theta$,
     $c$, $\lVert\theta\rVert$, and per-topic $\beta/\gamma/\mu/r$ distributions,
     plus a difficulty-curve percentile-band plot and a summary CSV.
   - If `buzz_event_predictions.csv` exists, adds buzz-position MAE/median error
     and an observed-vs-predicted scatter.
2. **`evaluate_bonuses(compositional_results, …)`** — reused root bonus eval.
3. Optionally **`player_skill_stability_plot`** against a comparison run.
4. Writes `tossup_metrics.csv`, `bonus_metrics.csv`, and the Markdown
   `experiment_report.md`.

`dimension_labels` (from `--topic-names`) only relabels plot legends — it has no
effect on any number. `_sigmoid` here clips to $[-60, 60]$ for NumPy stability.

---

## 8. In-sample vs. held-out (train/test) evaluation

Everything above, run through `run_topic_compirt.sh`, trains and evaluates on the
**same** `--split`. So the metrics in §7 are an **in-sample fit**: each tossup's
$\beta/\gamma/\mu$ and each player's $\theta$ were estimated on the very rows being
scored. That is the right diagnostic for model inspection, but it is *not* a
generalization estimate (the evaluator's own header says so).

The repo also supports the paper's **primary temporal split** (paper §4.2): train
player skills on a historical split (`year_2024`) and report Scenario A/B on a
held-out future split (`year_2025`).

### What "transductive" means here

Because the 2025 questions are new packets, their **per-topic difficulty**
$\beta/\gamma/\mu$ is **co-estimated on the 2025 responses** alongside prediction —
the paper's "co-estimating items and persons." The fixed topic mixture $r$ is
*already* available for any question (it comes from text/category, §2), so the
topic side needs nothing new. What has to carry across the split is the **player
prior**:

- **Returning players** (seen in 2024): the prior on $\theta$ (and $c$) is their
  **2024 training posterior** — loc *and* scale, saved to `player_posterior.csv`.
- **New players** (~66% of 2025): a **tier-conditioned** population prior
  $\theta \sim \mathcal{N}(\mu_\text{tier}, \Sigma_\text{tier})$, with the moments
  estimated from 2024 players grouped by tournament tier
  (fall/winter/regionals/nationals). `--new-player-prior flat` selects the paper's
  $\mathcal{N}(0, I)$ ablation.

### How it works in code (shared across all three variants)

- **Models read optional priors.** `sample_parameters` (§5.2) now reads four
  optional keys from `data` — `theta_prior_loc/scale`, `c_prior_loc/scale` —
  defaulting to $\mathcal{N}(0,I)/\mathcal{N}(0,1)$ when absent, so an ordinary
  in-sample run is unchanged.
- **`holdout/player_priors.py`** (repo root) builds those tensors:
  `player_tier_map` (player→tier from `teams`×`tournaments`), `estimate_tier_priors`
  (per-tier $\mu/\Sigma$ from the training posterior), and
  `attach_player_priors` (returning→training posterior, new→tier prior).
- **`utils/saving.save_player_posterior`** extracts the `AutoNormal` loc/scale plus
  each player's tier and writes `player_posterior.csv` on every Stage-1 run (this is
  why `fit_svi` now has a `return_guide` option, §4a — the guide carries the
  posterior scale, not just the median).
- **`train_topic_pyramidal.py`** exposes `--train-posterior <player_posterior.csv>`
  and `--new-player-prior {tier,flat}` to switch a run into the held-out pass.

The fixed topic vectors $r$ are unaffected — the held-out machinery only changes the
player prior. Stage 2 and the evaluator need **no changes**: Stage 2 already freezes
$\theta$ by `player_id` and drops unknown-roster rows (few drops now, since new
players received a co-estimated $\theta$), and the evaluator only consumes
prediction CSVs.

### Running it

Use the repo-root driver `run_scripts/run_compirt_holdout.py` with `MODEL=topic`
(it chains the four steps; `TOPIC_VECTORS` selects the $r$ CSV):

```text
1. Stage-1 train on TRAIN_SPLIT (year_2024)      → <ROOT>/train/pyramidal  (+ player_posterior.csv)
2. Stage-1 HELD-OUT pass on TEST_SPLIT (year_2025, --train-posterior …)   → <ROOT>/holdout/pyramidal
3. Stage-2 on TEST_SPLIT using the held-out θ    → <ROOT>/holdout/compositional
4. evaluate_topic_compirt.py on the held-out predictions → <ROOT>/holdout/evaluation
```

The metrics in `<ROOT>/holdout/evaluation/` are then genuine held-out Scenario A/B
estimates rather than in-sample fit.

---

## 9. Orchestration — `run_topic_compirt.sh`

A single Bash driver that reads environment variables and chains everything,
teeing all output to `<ROOT>/run.log`:

```text
[optional] run_plda.py  (RUN_PLDA=1, default)         → document_latent_vectors.csv
train_topic_pyramidal.py  → <ROOT>/pyramidal/
train_topic_compositional.py (compositional)          → <ROOT>/compositional/
[optional] train_topic_compositional.py --use-synergy → <ROOT>/synergy/
[optional] evaluate_topic_compirt.py × {compositional, synergy}
```

Key environment variables (see README for the full table):

| Var | Effect |
| --- | --- |
| `ROOT` | Output directory for the whole run |
| `SPLIT`, `TOURNAMENT` | Data selection (`TOURNAMENT=""` = whole split) |
| `DIMENSIONS` | **Must equal** the number of `latent_topic_NN` columns |
| `TOPIC_VECTORS` | Vector CSV to use when `RUN_PLDA=0` |
| `RUN_PLDA` | `1` rebuilds PLDA first; `0` reuses `TOPIC_VECTORS` |
| `RUN_SYNERGY` | Also train + evaluate the synergy bonus model |
| `CALIBRATE_CORRECTNESS` | Add Platt scale+bias (a **retrain**, not post-processing) |
| `TOPIC_NAMES` | Optional dimension names for plot legends only |
| `DEVICE`, `GPU` | Torch device selection |

The script also validates CUDA availability up front and refuses to proceed if
`RUN_PLDA=0` but `TOPIC_VECTORS` doesn't exist.

---

## 10. Output layout

```text
<ROOT>/pyramidal/            players.csv, tossups.csv, tossup_predictions.csv,
                             buzz_event_predictions.csv, summary.json, loss plot
<ROOT>/compositional/        bonus_parts.csv, bonus_part_predictions.csv,
                             team_predictions.csv, tau.txt, summary.json
<ROOT>/synergy/              same as compositional + synergy details (if RUN_SYNERGY=1)
<ROOT>/evaluation/           metrics CSVs, plots, experiment_report.md (for compositional/)
<ROOT>/synergy-evaluation/   same, for synergy/
<ROOT>/run.log               full transcript
```

The two headline reports are `<ROOT>/evaluation/experiment_report.md` and
`<ROOT>/synergy-evaluation/experiment_report.md`.

---

## 11. Mental-model summary (and the gotchas)

- **$r$ is fixed input, never a Pyro sample.** It lives in
  `data["topic_weight"]`, indexed by tossup (Stage 1) or part (Stage 2).
- **Per-topic difficulty replaces a scalar.** $\beta/\gamma/\mu$ (Stage 1) and
  $\beta$ (Stage 2) carry a topic axis; difficulty is collapsed against the same
  $r$.
- **`document_id` is the contract.** PLDA/LDA/category builders must emit IDs
  that match CompIRT's tossup/bonus IDs, or alignment fails loudly.
- **Bonus parts share one $r_b$** but learn independent $\beta_{bk}$.
- **Stage 1 → Stage 2 handoff is $\theta$** via `players.csv`; bonus rows with any
  unfitted roster member are dropped.
- **Stage 1 likelihood is hand-built (`pyro.factor`)**; Stage 2 is a plain
  observed `Bernoulli`.
- **Calibration is a retrain**, and in Stage 1 touches *only* the correctness
  factor, not buzz timing.
- **`TOPIC_NAMES` is cosmetic** — legends only, no effect on results.
- **Default runs are in-sample**; the held-out train/test evaluation (§8) is a
  separate mode via `run_compirt_holdout.py` that only changes the **player
  prior** (training posterior for returning, tier-conditioned for new) — the topic
  vectors $r$ and the rest of the pipeline are untouched.

| Paper eq. | Function | Topic change |
| --- | --- | --- |
| Eq. 14 priors | `sample_parameters` / `compositional_model` | drop $\alpha$, per-topic $\beta/\gamma/\mu$ |
| Eq. 3 difficulty | `difficulty_curve` | per-topic |
| Eq. 4 correctness | `correctness_logit` | $r$ replaces $\alpha$, gap inside sum |
| Eq. 5 hazard | `hazard_logit` | — |
| Eq. 6 survival | `log_survival` | — |
| Eq. 7/12 tossup likelihood | `competing_risks_model` | — |
| Eq. 8 aggregate | `topic_weighted_member_abilities` + `lse_aggregation` | $r$ replaces $\alpha$ |
| Eq. 10 synergy | `synergy_contribution` | independent of $r$/$\theta$ |
| Eq. 11 bonus outcome | `compositional_model` | per-topic $\beta_{bk}$ |
| Eq. 13 dead tossup | implicit ($t^* = T_j$ on NO-BUZZ rows) | — |
