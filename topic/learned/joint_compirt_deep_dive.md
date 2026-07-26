# Joint sLDA + CompIRT — End-to-End Deep Dive

This document explains how the **learned-topic** (joint supervised-LDA + CompIRT)
pipeline works from question text and buzz data to evaluation, with a focus on
**the functions involved and the core logic inside each one**. It is the
implementation-level companion to:

- [`HOW_IT_WORKS.md`](HOW_IT_WORKS.md) — the *conceptual* derivation (what sLDA is,
  why the discrete topic assignments integrate out, why $K$ equals the skill
  dimension). Read that for the "why."
- [`README.md`](README.md) — operational commands.
- [`../../docs/compirt_deep_dive.md`](../../docs/compirt_deep_dive.md) (root baseline) and
  [`../fixed/topic_compirt_deep_dive.md`](../fixed/topic_compirt_deep_dive.md)
  (fixed topics) — this variant reuses most of their machinery.

---

## 0. The one idea behind everything

The fixed-topic variant loads a topic vector $r_j$ per question from a CSV that an
**unsupervised** LDA produced. This variant makes $r_j$ a **latent of the model**,
learned **jointly** with the IRT skills, so buzz/answer outcomes shape the topics:

- Each question (tossup **and** bonus) gets $\theta_{\text{doc}} \sim
  \text{Dirichlet}$ on the $K$-simplex. It generates the question's **bag of words**
  via the LDA mixture $\text{Multinomial}(N, \theta_{\text{doc}}\cdot\phi)$ (the
  per-word topic assignments integrate out — see HOW_IT_WORKS §3a).
- For tossups, that **same** $\theta_{\text{doc}}$ *is* the IRT topic-weight $r_j$
  that gates $\sum_k r_{jk}(\theta_{ik} - d_{jk}(t))$.

Because both likelihoods share $\theta_{\text{doc}}$, fitting them together makes
"who got it right" flow back into the topics. That is supervised LDA, fused with
CompIRT.

Where the fixed-topic model reads $r$ from `data["topic_weight"]`, this model
**samples** `theta_doc` and slices `theta_doc[:n_tossups]` as $r$. The
competing-risks likelihood, difficulty curves, and bonus aggregation are
**reused** from `topic_compirt`.

---

## 1. Pipeline at a glance

There is no separate "build vectors" stage — the vectors are an *output* of the
joint fit. Two stages, run in order:

| # | Stage | Script(s) | Reads | Writes |
| --- | --- | --- | --- | --- |
| 1 | Stage 1 — joint pyramidal | `train_joint_pyramidal.py` + `joint_pyramidal.py` | `database.db` text + linked dataset | `players.csv` ($\theta$), `tossups.csv`, `tossup_predictions.csv`, **`topic_word_matrix.npy` + `vocabulary.json`**, `topics.csv`, `document_latent_vectors.csv`, `player_posterior.csv` |
| 2 | Stage 2 — joint compositional | `train_joint_compositional.py` + `joint_compositional.py` | $\theta$ + **frozen** topic-word matrix + dataset | `bonus_parts.csv`, `*_predictions.csv`, `tau.txt` |
| — | Evaluate | root `evaluate_compirt.py` + `compirt_eval/` | Stage 1 + Stage 2 outputs | Scenario A/B metrics + report |
| — | Diagnostic | `topic_response_profiles.py` | `document_latent_vectors.csv` | per-topic correctness/buzz separation |

The learned variant **reuses the root `evaluate_compirt.py`** (its outputs match the
root schema), unlike the fixed-topic variant which has its own evaluator.

| Layer | Files | Role |
| --- | --- | --- |
| BoW | `bow.py` | Vocabulary + `(n_docs, V)` count matrix aligned to an id order |
| Stage 1 model | `joint_pyramidal.py` | LDA word model + topic-weighted competing-risks, one shared `theta_doc` |
| Stage 2 model | `joint_compositional.py` | LDA word model + topic-weighted bonus likelihood, frozen $\theta$ & `topic_word` |
| Diagnostics | `slda_responses.py`, `topic_response_profiles.py` | Did supervision separate difficulty across topics? |
| Reused | `topic_compirt.{pyramidal,compositional,common}`, root `compirt_data.py` | Difficulty/aggregation math, SVI loop, data builders |

### 1.1 Critical invariants

These are the implementation details most likely to cause silent model bugs:

| Invariant | Why it matters | Where enforced / created |
|---|---|---|
| `K` equals both topic count and player skill dimension | `r_jk` multiplies `theta_player_ik`; the axes must mean the same thing | CLI `--dimensions`; Stage 2 validates `topic_word.shape[0] == theta.shape[1]` |
| Tossup documents come first in `theta_doc` | `theta_doc[:n_tossups]` is sliced as tossup topic weights | `build_corpus` in `train_joint_pyramidal.py` |
| `topic_word` rows define the axes | player skills and document topic weights are only meaningful relative to those rows | `topic_word_matrix.npy` + `vocabulary.json` from Stage 1 |
| Held-out and Stage 2 reuse the training vocabulary | changing vocabulary order changes every column of `topic_word` | `load_topic_model` and `--train-topic-model` |
| Saved `beta_*` is CompIRT difficulty, not LDA beta | prevents confusing `tossups.csv` with the topic-word prior | local variable `difficulty_beta`; saved prefix kept for compatibility |
| The word model observes counts, not tokens | per-word `z` assignments are integrated out | `bow_tensor`; `Multinomial(..., obs=bow)` |

If one of these invariants breaks, the model can still run but the dot products
will mean the wrong thing. The most important one is axis alignment: dimension
`k` must mean the same topic in `topic_word[k]`, `theta_doc[..., k]`, and
`theta_player[..., k]`.

---

## 2. Bag-of-words — `bow.py`

The LDA word likelihood needs a fixed-width count vector per document, not a token
list.

- **`build_vocabulary(documents, vocab_size, min_df, rm_top)`** — keeps words in
  $\geq$ `min_df` documents, drops the `rm_top` most frequent (stopword-like), keeps
  the top `vocab_size`; returns a **sorted** vocabulary and a `word → index` map.
- **`build_bow_matrix` / `bow_tensor(documents, vocabulary_index, ordered_ids)`** —
  a `(n_documents, V)` float count matrix aligned to a caller-supplied id order.

The **id order is load-bearing**: the corpus is built **tossups-first**
(`build_corpus` in `train_joint_pyramidal.py` puts every `data["tossup_ids"]`
document first, then bonuses), so `theta_doc[:n_tossups]` lines up row-for-row with
the IRT observations.

Implementation notes worth remembering:

- The BoW tensor is float-valued because PyTorch distributions and the rest of
  the tensors run in floating point, but semantically each row is word counts.
- `rm_top` removes corpus-wide frequent words before selecting the vocabulary.
  This is not a modeling prior; it is preprocessing to keep `topic_word` from
  spending capacity on stopword-like tokens.
- In `joint_pyramidal.py`, `total_count` is set to the maximum row sum only
  because `torch.distributions.Multinomial` requires a scalar total count. With
  `validate_args=False`, the log-probability uses each observed row's count sum
  in the multinomial coefficient. The likelihood still corresponds to each
  document's own bag-of-words count vector.
- The collapsed likelihood is dense in vocabulary space:
  `log_prob(bow_row)` uses `log(theta_doc @ topic_word)`, not hard assignment of
  each word to a single topic.

---

## 3. Stage 1 — Joint pyramidal (`joint_pyramidal.py`)

### 3.1 The model — `joint_model(data, n_dimensions, vocab_size, bow_weight, topic_concentration, calibrate_correctness)`

Notation guardrail:

| Paper symbol | Code name | Meaning here |
|---|---|---|
| $\alpha$ in $\text{Dirichlet}(\alpha\mathbf 1)$ | `topic_concentration` | Fixed hyperparameter; default `1.0`. |
| $\theta_{\text{doc}}$ | `theta_doc` | Per-document topic mixture; also used as CompIRT topic weight $r$. |
| $z_{dn}$ | none | Per-word topic assignment; integrated out, never sampled. |
| $\bar z_d$ | `theta_doc` / `topic_weight` conceptually | Canonical sLDA's average topic usage; represented directly by `theta_doc` here. |
| $\phi$ / topic-word matrix | `topic_word` | Topic-word matrix, point-estimated from `topic_word_logits`. |
| LDA $\beta$ prior | none | Classic `phi_k ~ Dirichlet(beta)` prior; not implemented here. |
| CompIRT $\beta$ | `difficulty_beta` in locals; `posterior["beta"]` on disk | Difficulty-curve size parameter; not the topic-word matrix. |
| $\eta$ | none | Canonical sLDA response coefficient; replaced by the CompIRT likelihood. |

Logic flow:

1. **Topic-word matrix $\phi$ / `topic_word`** — a point-estimated `pyro.param`
   (`topic_word_logits`, softmaxed per topic): the variational-EM "M-step" view of
   topics. This is not sampled from a classic LDA `Dirichlet(beta)` prior.
   *(Held-out exception below.)*
2. **Player priors** — $\theta_{\text{player}}\sim\mathcal{N}(0,I)$,
   $c\sim\mathcal{N}(0,1)$, reading the optional held-out prior keys from `data`
   (§6), same hook as the root model.
3. **Per-document topics + words** — in a `documents` plate,
   $\theta_{\text{doc}}\sim\text{Dirichlet}(\alpha\mathbf 1)$, then
   `word_probs = theta_doc @ topic_word` observed as
   $\text{Multinomial}(N, \theta_{\text{doc}}\phi)$ under `poutine.scale(bow_weight)`
   — the LDA mixture with discrete assignments integrated out. In code,
   $\alpha$ is the scalar `topic_concentration`.
4. **Per-topic tossup difficulty** — `difficulty_beta`, $\gamma$, and $\mu$
   sampled per tossup (no learned $\alpha$; the topic weight replaces it). The
   Pyro site and CSV prefix remain `beta` for compatibility.
5. **IRT likelihood** — slice `tossup_topic = theta_doc[:n_tossups]` as $r$, then
   call the **reused** topic-weighted competing-risks likelihood from
   `topic_compirt.pyramidal` (survival over all rows, hazard + correctness on
   buzzers, attached with `pyro.factor`). Optional `calibrate_correctness` Platt-
   scales only the correctness logit.

`bow_weight` (a `poutine.scale`) balances the thousands of word tokens per document
against the far fewer IRT observations — the one hyperparameter worth sweeping
(HOW_IT_WORKS §6).

### 3.1.1 Tensor shapes inside `joint_model`

| Tensor / site | Shape | Meaning |
|---|---:|---|
| `data["bow"]` | `(n_documents, V)` | count vector for every tossup and bonus document |
| `topic_word_logits` | `(K, V)` | unconstrained topic-word scores |
| `topic_word` | `(K, V)` | row-softmax topic-word distributions |
| `theta_doc` | `(n_documents, K)` | document topic proportions on the simplex |
| `theta` | `(n_players, K)` | player skill vectors |
| `c` | `(n_players,)` | player buzz thresholds |
| `difficulty_beta`, `gamma`, `mu` | `(n_tossups, K)` | per-tossup, per-topic curve parameters |
| `topic_weight = theta_doc[:n_tossups][data["tossup"]]` | `(n_rows, K)` | topic vector aligned to each player-question observation row |
| `row_theta = theta[data["player"]]` | `(n_rows, K)` | player skill aligned to each observation row |

The IRT likelihood is row-aligned: `data["player"]` and `data["tossup"]` are
integer index vectors built by `tossup_tensors`, so every player-question row
receives the correct player skill and tossup topic vector.

### 3.1.2 Probability-to-code map

| Math | Code |
|---|---|
| $\phi_k = \text{softmax}(\ell_k)$ | `topic_word = F.softmax(topic_word_logits, dim=-1)` |
| $\theta_{\text{doc},d}\sim\text{Dirichlet}(\alpha\mathbf 1)$ | `pyro.sample("theta_doc", dist.Dirichlet(concentration))` |
| $p(x_d|\theta_d,\phi)=\text{Multinomial}(N_d,\theta_d\phi)$ | `word_probs = theta_doc @ topic_word`; `pyro.sample("bow_obs", dist.Multinomial(...), obs=bow)` |
| $\theta_i\sim\mathcal N(0,I)$ | `pyro.sample("theta", dist.Normal(...).to_event(1))` |
| $c_i\sim\mathcal N(0,1)$ | `pyro.sample("c", dist.Normal(...))` |
| $d_{jk}(t)=\beta_{jk}\sigma(\gamma_{jk}(\mu_{jk}-t/T_j))$ | `difficulty_curve` in `topic_compirt.pyramidal` |
| correctness, hazard, survival | `correctness_logit`, `hazard_logit`, `log_survival` |
| tossup response likelihood | summed manually, then added by `pyro.factor(...)` |

`pyro.factor` is used because the competing-risks likelihood is not one simple
built-in distribution over a rectangular tensor. It combines censored survival
terms, first-buzz hazard terms, and correctness Bernoulli terms with masks.

### 3.2 `topic_word_distributions()`

Returns `softmax(pyro.param("topic_word_logits"))` — the fitted $(K, V)$ topic-word
distributions, used to write `topics.csv` (top words per topic) and
`topic_word_matrix.npy` (the frozen matrix Stage 2 and the held-out pass reuse).

### 3.3 Driver — `train_joint_pyramidal.py`

```text
build_corpus (tossups-first) → build_vocabulary → bow_tensor
   → tossup_tensors (data) ; data["bow"] = BoW
   → [held-out only] freeze topic_word from training; attach_player_priors
   → fit_svi(joint_model, … , return_guide=True)
   → data["topic_weight"] = theta_doc[:n_tossups]
   → save_parameters (players.csv, tossups.csv)
   → save_player_posterior (player_posterior.csv)
   → write_topics (topics.csv) + write_topic_model (topic_word_matrix.npy, vocabulary.json)   # skipped on held-out
   → write_document_vectors (document_latent_vectors.csv: tossup + bonus r_j)
   → posterior_row_predictions → tossup_predictions.csv ; summary.json
```

Bonuses ride along in the joint fit as **word-only documents** (they share
`topic_word` so their vectors live in the same space) but do **not** enter the
IRT line — that is the compositional stage's job.

### 3.4 Variational posterior and saved point estimates

`fit_svi(..., return_guide=True)` returns the fitted `AutoNormal` guide and the
loss history. The training script then calls `guide.median(data, ...)` to get
one representative value for each sampled latent:

- `posterior["theta_doc"]` → document topic vectors.
- `posterior["theta"]` and `posterior["c"]` → player outputs.
- `posterior["beta"]`, `posterior["gamma"]`, `posterior["mu"]` → tossup curve
  parameters.

`topic_word` is different: it is a `pyro.param`, so it is not inside
`guide.median`. `topic_word_distributions()` reads the optimized
`topic_word_logits` from Pyro's parameter store and softmaxes them. This is why
the pipeline saves both posterior-derived CSVs and the separate
`topic_word_matrix.npy`.

The exported outputs therefore mix:

| Output | Source |
|---|---|
| `players.csv`, `tossups.csv`, `document_latent_vectors.csv` | guide medians of sampled latents |
| `topics.csv`, `topic_word_matrix.npy` | optimized `pyro.param("topic_word_logits")` |
| `tossup_predictions.csv` | deterministic posterior-row predictions from the median latents |
| `player_posterior.csv` | posterior loc/scale summary used as held-out priors |

---

## 4. Stage 2 — Joint compositional (`joint_compositional.py`)

The bonus analogue of sLDA. It **freezes** the pyramidal stage's player skills
$\theta$ **and** the topic-word matrix `topic_word`, then re-samples each bonus's
$\theta_{\text{doc}}$ so the bonus's own part-correctness — not just its words —
shapes its place in topic space.

### 4.1 The model — `joint_compositional_model(data, theta, topic_word, bow_weight, …)`

1. **Per-bonus topics + words** — in a `bonus_documents` plate,
   $\theta_{\text{doc}}\sim\text{Dirichlet}$ generates the bonus BoW via the
   **fixed** `topic_word` (`word_probs = theta_doc @ topic_word`, scaled by `bow_weight`).
2. **Per-topic part difficulty** `difficulty_beta_b ~ Normal(0, I)` and
   $\tau\sim\text{Half-Cauchy}(1)$.
3. Each part inherits its bonus's learned weight $r_b = \theta_{\text{doc}}$ via
   `part_doc_index`; member abilities, `lse_aggregation`, and
   `topic_weighted_part_difficulty` are **reused from `topic_compirt.compositional`**.
   Logit $= A_b(R) - \sum_k r_{bk}\,\text{difficulty\_beta}_{bk}$ ($+$
   optional synergy, $+$ optional Platt calibration), observed as a plain
   `Bernoulli`.

**Why freeze `topic_word` (and $\theta$)?** The member score $\sum_k r_{bk}\theta_{pk}$
only makes sense if dimension $k$ means the same topic for the bonus weight and the
player skill — and that meaning is anchored by row $k$ of `topic_word`.
Refitting `topic_word` would rotate the axes and break the dot product; freezing
also keeps faith with CompIRT's two-stage design (bonus data never moves player
skills). See HOW_IT_WORKS §5.

### 4.1.1 What can move in Stage 2

| Quantity | Frozen or learned? | Reason |
|---|---|---|
| player `theta` | frozen | preserves Stage 1 player skills |
| `topic_word` | frozen | preserves topic/skill axis meanings |
| bonus `theta_doc` | learned | lets bonus words and part outcomes place each bonus in the fixed topic space |
| bonus part `difficulty_beta` | learned | part-specific difficulty under the same topic axes |
| `tau` | learned | controls smooth max aggregation over team members |
| optional synergy parameters | learned if `--use-synergy` | captures team composition effects beyond independent member ability |

So Stage 2 is not "retraining the topic model on bonuses." It is **folding bonus
documents into the fixed Stage 1 topic space while using bonus correctness as
supervision**.

### 4.2 Driver — `train_joint_compositional.py`

```text
load_player_skills (theta from Stage 1 players.csv)
   → load_topic_model (frozen topic_word_matrix.npy + vocabulary.json)   # --topic-model-dir
   → build_bonus_part_observations → keep only fully-fitted rosters
   → build_part_doc_index (map each part → its bonus document row)
   → bonus_tensors ; data["bonus_bow"] = bow over the FROZEN vocabulary
   → fit_svi(joint_compositional_model, … theta & topic_word fixed)
   → joint_posterior_predictions → bonus_part_predictions.csv, team_predictions.csv
   → save_bonus_part_parameters, tau.txt, summary.json
```

`load_topic_model` validates that `topic_word`'s column count equals the vocabulary size
and that its row count equals $\theta$'s skill dimension — the topics, skills, and
`topic_word` rows cannot silently disagree.

---

## 5. Diagnostics — `slda_responses.py` + `topic_response_profiles.py`

Did supervision actually push difficulty into the topics?

- **`slda_responses.py`** turns the observation DataFrames into
  `{question_id: value}` maps: correctness rate and mean buzz position per question.
  (Pure aggregates; the model is supervised by the IRT likelihood, not these.)
- **`topic_response_profiles.py`** assigns each question its **primary topic**
  (argmax of its $r$ vector) and reports mean correctness / buzz position per topic.
  If supervision worked, those should **separate** across topics and the
  `topics.csv` word lists should look subject-coherent.

### 5.1 Diagnosing sparse topics and repeated-looking curves

The learned-topic runs can produce coherent word topics while the response curves
look visually repetitive. That usually means the word/topic side is working, but
the response-side curve parameters are not richly differentiated.

Check these from `pyramidal/tossups.csv`:

| Diagnostic | How to read it |
|---|---|
| `max_k topic_weight_k` | near `1.0` means the tossup is effectively assigned to one topic |
| entropy / effective number of topics | lower values mean sparse topic mixtures |
| whether `argmax(topic_weight)` equals `argmax(beta)` | if almost always true, the model puts the real difficulty scale on the dominant topic |
| `gamma_*`, `mu_*` spread among active topics | similar values imply mostly vertical rescaling |
| inactive-topic `beta_*` values | tiny values imply weakly identified side curves |

Interpretation:

- **Good / expected:** many tossups are single-subject, so sparse weights are not
  automatically wrong.
- **Warning sign:** if nearly every tossup is one-hot and curves differ mostly by
  vertical magnitude, the model may be using topics as subject labels plus scalar
  difficulty, not as meaningfully different response dimensions.
- **Ablation to propose:** constrain curve shapes, such as shared or
  topic-global `gamma`/`mu`, and test whether metrics change. If not, the current
  per-tossup-per-topic curve family is more flexible than the data needs.

Hyperparameter response:

- Increase `--topic-concentration` to push `theta_doc` away from one-hot mixtures.
- Lower `--bow-weight` if word reconstruction dominates and forces hard
  subject-like assignments.
- Keep an eye on `topics.csv`; forcing distributed weights can make topics less
  clean if pushed too far.

---

## 6. In-sample vs. held-out (train/test) evaluation

By default Stage 1 trains and evaluates on the **same** `--split` — an **in-sample
fit**. The repo also supports the paper's **temporal split** (paper §4.2): train on
`year_2024`, report Scenario A/B on held-out `year_2025`. As in the other variants
this is **transductive** (2025 question difficulty co-estimated on 2025 responses)
and the **player prior** carries across the split:

- **Returning players** → their 2024 training posterior (loc + scale), from
  `player_posterior.csv`.
- **New players** → a **tier-conditioned** prior
  $\mathcal{N}(\mu_\text{tier},\Sigma_\text{tier})$ (or $\mathcal{N}(0,I)$ with
  `--new-player-prior flat`).

The shared machinery is identical to the root model — optional `theta_prior_*`/
`c_prior_*` keys on the model, `holdout/player_priors.py`, and
`save_player_posterior`. See [`../../docs/compirt_deep_dive.md`](../../docs/compirt_deep_dive.md) §7.

### What this variant adds

A learned-topic held-out pass must **not** re-learn topics on the 2025 text — that
would put 2025 documents in different axes than the trained players. So:

- `train_joint_pyramidal.py --train-topic-model <training dir>` **freezes** the
  trained `topic_word_matrix.npy` and reuses `vocabulary.json` (same column order),
  so 2025 `theta_doc` is inferred against trained topics. In code, `joint_model`
  reads `data["fixed_topic_word"]` instead of creating the `topic_word_logits`
  param, and `write_topics`/`write_topic_model` are skipped (nothing new to save).
- `--train-posterior` is required to come **with** `--train-topic-model` (enforced in
  `parse_args`).

### Running it

`run_scripts/common/run_compirt_holdout.py` with `MODEL=learned` chains:

```text
1. Stage-1 train on TRAIN_SPLIT → <ROOT>/train/pyramidal  (+ player_posterior.csv, topic_word_matrix.npy, vocabulary.json)
2. Stage-1 HELD-OUT pass on TEST_SPLIT (--train-posterior … --train-topic-model <train dir>) → <ROOT>/holdout/pyramidal
3. Stage-2 on TEST_SPLIT (--player-skills holdout/… --topic-model-dir <train dir>) → <ROOT>/holdout/compositional
4. evaluate_compirt.py on the held-out predictions → <ROOT>/holdout/evaluation
```

Note steps 2 and 3 both point their topic-model dir at the **training** pyramidal
output — that is where the frozen topics live.

---

## 7. Mental-model summary (and the gotchas)

- **$r_j = \theta_{\text{doc}, j}$** — a tossup's topic proportions *are* its IRT
  topic-weight; one Dirichlet latent explains both its words and its buzz outcomes.
- **No discrete topic assignments** — they integrate out into
  $\text{Multinomial}(\theta_{\text{doc}}\phi)$ (`theta_doc @ topic_word`).
- **Tossups-first ordering** lets `theta_doc[:n_tossups]` align with the IRT rows.
- **`topic_word` / $\phi$ is point-estimated** (a `pyro.param`, EM M-step), not sampled from a classic LDA `Dirichlet(beta)` prior.
- **Stage 2 freezes $\theta$ and `topic_word`**; only bonus `theta_doc` + part difficulty
  are learned, so supervision moves *where a bonus sits*, not the axes.
- **`bow_weight`** trades word-fit vs. outcome-fit — the knob to sweep.
- **`K` = topics = skill dimensions** — not a free topic hyperparameter.
- **Held-out mode freezes the trained topic-word matrix** (`--train-topic-model`) and
  only changes the player prior; reuse the **training** vocabulary, never a fresh
  one. The evaluator is the root `evaluate_compirt.py`.
- **No encoder / no amortization** — a brand-new question has no $\theta_{\text{doc}}$
  until a fold-in (a few SVI steps holding `topic_word` fixed); that is exactly what the
  held-out pass does for the whole 2025 set at once.

---

## 8. Technical defense crib sheet

| If asked... | Answer | Code / artifact to cite |
|---|---|---|
| "Does this actually maximize `p(words, labels)`?" | It maximizes an ELBO for the joint model containing word likelihood, IRT outcome likelihood, priors, and guide entropy. `topic_word` is point-estimated. | `joint_pyramidal.py` `bow_obs` + `pyro.factor`; `fit_svi` |
| "Where are the LDA `z` variables?" | Integrated out analytically: `p(w|theta,phi)=theta @ phi`. No per-token discrete latent is sampled. | `word_probs = theta_doc @ topic_word` |
| "What is beta?" | Saved `beta_*` is CompIRT `difficulty_beta`, not LDA's topic-word prior. LDA topic-word distributions are `topic_word`/`phi`. | `tossups.csv`; `topic_word_matrix.npy`; notation table |
| "Why not let Pyro enumerate `z`?" | Enumeration is unnecessary because the collapsed likelihood is exact and differentiable. Enumeration would add work without changing the marginal word likelihood. | collapsed `Multinomial` in `joint_model` |
| "Why are topics and skill dimensions the same?" | `r_jk` gates `theta_player_ik`; therefore topic axis `k` must be the skill axis `k`. | `correctness_logit` in `topic_compirt/pyramidal.py` |
| "Why freeze `topic_word` in Stage 2 or held-out?" | Refitting it would rotate/relabel axes, making existing player skills incompatible with new document weights. | `load_topic_model`; `fixed_topic_word`; `--train-topic-model` |
| "Is buzz timing regression?" | No. Buzzing is a discrete-time Bernoulli hazard with survival; correctness is a Bernoulli on the winning buzz. | `hazard_logit`, `log_survival`, `dist.Bernoulli(logits=correctness)` |
| "What if topic weights are too one-hot?" | Increase `topic_concentration`, possibly lower `bow_weight`, and compare against constrained difficulty-curve ablations. | `summary.json`; `tossups.csv`; curve diagnostics |
| "What is the most fragile implementation assumption?" | Document order and axis alignment: tossups first, fixed vocabulary order, and matching `K` across `topic_word`, `theta_doc`, and player `theta`. | `build_corpus`; `load_topic_model` validation |

The best concise defense of the implementation is:

> We changed only the source of the topic weights. Fixed-topic CompIRT reads
> `r_j` from a CSV; learned-topic CompIRT samples `theta_doc`, uses it in a
> collapsed LDA word likelihood, and slices the tossup rows as `r_j` for the same
> competing-risks likelihood. That is why the math remains recognizable CompIRT
> while the topics become supervised by outcomes.
