# How the joint supervised-LDA + CompIRT model works (end to end)

A complete, self-contained explanation — assumes you know basic probability and
gradient-based optimization, but **not** topic models, IRT, or sLDA. By the end
you should be able to defend every design choice to a skeptical ML person.

---

## 0. The 30-second / 2-minute / deep versions

**30 seconds.** We fit a topic model and an item-response (skill) model *at the
same time*, sharing one set of per-question "topic" vectors. Normally a topic
model learns topics only from words. Here the same topic vectors also have to
explain *who buzzed and who got the question right*, so the topics bend toward
capturing **difficulty and subject matter that actually predict performance** —
not just word co-occurrence.

**2 minutes.** Each quizbowl question gets a latent vector `θ` on the probability
simplex (it sums to 1) — its mix over `K` topics. Two things are generated from
that vector: (1) the question's **bag of words** (a topic model), and (2) the
**buzz/answer outcomes** of the players who saw it (an item-response model where
`θ` says which skill dimensions the question rewards). Because both likelihoods
share `θ`, fitting them jointly makes "correct/incorrect" flow back into the
topics. We fit everything by stochastic variational inference (SVI) in Pyro. The
classic-LDA trick that makes this tractable is that the per-word topic
assignments **integrate out analytically**, leaving a plain `Multinomial`
word-likelihood with no discrete latent variables.

**Deep version.** The rest of this document.

---

## 1. The two ingredients

### 1a. Topic models and LDA (if you've never seen them)

A **topic model** explains a corpus of documents as mixtures of *topics*, where a
topic is a distribution over the vocabulary. **Latent Dirichlet Allocation (LDA)**
is the canonical one. Its generative story for one document `d`:

1. Draw topic proportions `θ_d ~ Dirichlet(α)` — a point on the `K`-simplex
   (non-negative, sums to 1). E.g. `θ_d = [0.7 history, 0.2 art, 0.1 ...]`.
2. For each word position `n`: draw a topic `z_{d,n} ~ Categorical(θ_d)`, then a
   word `w_{d,n} ~ Categorical(φ_{z_{d,n}})`, where `φ_k` is topic `k`'s
   distribution over the vocabulary.

So `θ_d` is "what this document is about" and `φ` is "what each topic says."
LDA is **unsupervised**: topics are whatever best reconstructs the words.

Classic Bayesian LDA often also has a word-prior hyperparameter, commonly
written `β` or `η`, with `φ_k ~ Dirichlet(β)`. This implementation does **not**
sample `φ` from that prior; it point-estimates `φ` as `topic_word =
softmax(topic_word_logits)`. That avoids colliding with CompIRT's own `β`
notation for difficulty.

### 1b. Supervised LDA (sLDA) — the key idea

**sLDA** (Blei & McAuliffe, 2007) attaches a **response variable** `y_d` to each
document, generated *from the document's topic proportions* through a regression:
`y_d ~ GLM(η · θ_d)`. Now the topics must do double duty — reconstruct the words
**and** predict the response. The supervision "propagates into the topics": the
fitted topics are the ones that are both coherent *and* predictive of `y`.

> The one-line mental model: **LDA = topics that explain words; sLDA = topics that
> explain words *and* an outcome.**

Our system is sLDA where the "response" is not a single scalar regression but the
**entire item-response model** of how players performed on the question. That's
the fusion.

### 1c. CompIRT: the item-response (skill) model

**Item Response Theory (IRT)** models `P(person answers item correctly)` as a
function of a latent **person ability** and latent **item difficulty**. CompIRT
is a quizbowl-specific IRT with two stages:

- **Pyramidal stage (tossups).** A tossup is read one clue/token at a time and
  gets *easier* as more clues appear; the first player to "buzz" wins the chance
  to answer. This is a **survival / competing-risks** model over reading
  position. It learns each player's skill vector `θ_player ∈ ℝ^K` and each
  tossup's per-topic difficulty curve.
- **Compositional stage (bonuses).** Holds player skills fixed and learns how
  three-part bonus questions reward those skills.

This repo's `topic/fixed/` already had a *topic-weighted* CompIRT where each
question carried a **fixed** topic vector `r_j` (loaded from a CSV produced by an
unsupervised LDA). The novelty here: **`r_j` is no longer fixed — it's a latent
of the model, learned jointly, so the IRT outcomes shape it.** That makes the
whole thing an sLDA.

---

## 2. Notation

| Symbol | Shape | Meaning |
|---|---|---|
| `K` | scalar | number of topics **=** number of IRT skill dimensions (they're the same axes) |
| `V` | scalar | vocabulary size |
| `θ_doc_j` (`r_j`) | `K` | question `j`'s topic proportions; on the simplex. **Doubles as the IRT topic-weight.** |
| `φ` / `topic_word` | `K × V` | each row is a topic's distribution over words; point-estimated from `topic_word_logits` |
| LDA `β` prior | scalar or `V` | classic Dirichlet prior for `φ`; **not present in this code** |
| `θ_player_i` | `K` | player `i`'s skill vector (one coordinate per topic/skill) |
| `c_i` | scalar | player `i`'s buzz "confidence threshold" (how sure they need to be) |
| `difficulty_beta_j, γ_j, μ_j` | `K` each | tossup `j`'s per-topic difficulty curve: size, sharpness, inflection point. Saved as `beta_*` for compatibility. |
| `d_jk(t)` | scalar | difficulty of tossup `j` on topic `k` at reading position `t` |
| `t*`, `T_j` | scalars | first-buzz position; total tokens in tossup `j` |

Two names, one object: a tossup's `θ_doc` *is* its IRT topic-weight `r_j`. That
identity is the entire bridge between the topic model and the IRT model.

### 2a. What is latent, learned, fixed, and saved

This distinction prevents most notation confusion:

| Quantity | Role in inference | Where it lives |
|---|---|---|
| `θ_doc` | latent random variable; one variational posterior per document | sampled in `joint_model`, exported as `document_latent_vectors.csv`; tossup rows also become `topic_weight_*` in `tossups.csv` |
| `θ_player`, `c` | latent random variables; player skill and buzz threshold | sampled in `joint_model`, exported as `players.csv` and `player_posterior.csv` |
| `difficulty_beta`, `γ`, `μ` | latent random variables; per-tossup, per-topic difficulty-curve parameters | sampled in `joint_model`, exported in `tossups.csv`; `difficulty_beta` is saved as `beta_*` for compatibility |
| `topic_word` (`φ`) | learned parameter, not a sampled latent | `softmax(topic_word_logits)`; exported as `topic_word_matrix.npy` and summarized in `topics.csv` |
| `topic_concentration` (`α`) | fixed hyperparameter | CLI flag `--topic-concentration`; controls the Dirichlet prior on `θ_doc` |
| `bow_weight` | fixed objective weight | CLI flag `--bow-weight`; multiplies only the word likelihood |

In particular, the saved `beta_*` columns are **not** the LDA topic-word matrix.
They are CompIRT difficulty sizes. The topic-word matrix is `topic_word`/`φ`,
saved separately as `topic_word_matrix.npy`.

---

## 3. The generative model (what we claim produced the data)

For every **document** (tossup **or** bonus):

```
θ_doc ~ Dirichlet(α · 1_K)          # topic proportions, on the K-simplex
topic_word = softmax(topic_word_logits)  # point-estimated φ, not sampled
words  ~ Multinomial(N, θ_doc · topic_word)  # the bag of words (see §3a)
```

For every **player** and every **tossup** (the IRT half, tossups only):

```
θ_player ~ Normal(0, I_K),  c ~ Normal(0,1)         # player skill + threshold
difficulty_beta_j, γ_j, μ_j ~ priors                # per-topic difficulty curve
buzz & answer outcomes ~ competing-risks(θ_player, r_j = θ_doc_j, difficulty)
```

The crucial line is the last one: the tossup's topic vector `r_j = θ_doc_j`
enters the IRT likelihood. So a single `θ_doc` for a tossup is responsible for
**both** its words **and** its buzz/answer outcomes.

For a tossup document, the joint density has this schematic form:

```
p(θ_doc_j | α)
· p(words_j | θ_doc_j, topic_word)
· p(buzz/answer rows for j | θ_doc_j, θ_player, c, difficulty_j)
```

For a bonus document in the pyramidal stage, the last term is absent:

```
p(θ_doc_b | α) · p(words_b | θ_doc_b, topic_word)
```

That asymmetry is intentional. Tossup outcomes supervise tossup topic vectors in
Stage 1. Bonus outcomes supervise bonus topic vectors later in Stage 2, after
the tossup-trained player skills and topic axes are fixed.

### 3a. Why there are no discrete latent variables (the LDA "collapse")

Classic LDA draws a discrete topic `z_n` for every word — thousands of discrete
latents per document. Discrete latents are painful for gradient-based variational
inference. The escape hatch: **marginalize them out**. Summing over `z_n`:

```
p(word = w | θ, φ) = Σ_k P(z=k) P(w | z=k) = Σ_k θ_k φ_{k,w} = (θ · φ)_w
```

For a bag of words with counts `x_w`, this becomes:

```
p(x | θ, φ) = Multinomial(x; N, θφ)
log p(x | θ, φ) = const(x) + Σ_w x_w log((θφ)_w)
```

So a document's word counts are just `Multinomial(N, θ · φ)` — a **mixture** of
the topic-word distributions, with no `z` to sample. This is what the code does:
`word_probs = theta_doc @ topic_word`. It is mathematically identical to LDA's
observed word likelihood after summing out the assignments, and it turns an
awkward discrete model into a smooth, differentiable one.

> This is the single most important technical point. If someone says "you can't
> do LDA with SVI because of the discrete topic assignments," the answer is: we
> don't sample them — they integrate out into the `Multinomial(θφ)` mixture.

This is also why there is no code variable for `z` or `z_bar`. In canonical sLDA,
the response model often uses

```
z_bar_d = (1/N_d) Σ_n one_hot(z_dn)
```

the empirical average topic assignment in a document. After marginalization, the
smooth analogue is the document topic vector `θ_doc`: its expectation is exactly
the per-token topic probability. This implementation therefore uses `θ_doc` as
the differentiable stand-in for `z_bar_d`.

### 3b. The IRT half: competing-risks survival over reading position

A tossup is read token by token. Model each rostered player as having a per-token
**hazard** of buzzing. Define the per-topic **difficulty curve**

```
d_jk(t) = difficulty_beta_jk · sigmoid( γ_jk · (μ_jk − t/T_j) )
```

— high early (few clues), decaying as `t` grows (more clues → easier). The
**correctness logit** if player `i` buzzed on tossup `j` at position `t` is the
topic-weighted skill-minus-difficulty gap:

```
correctness_logit = Σ_k  r_jk · ( θ_player[i,k] − d_jk(t) )
                         └──────┬──────┘
                    r_j weights which skills matter for THIS question
```

This is exactly where the topic vector does its job: `r_jk` says how much skill
dimension `k` matters for question `j`. (In plain IRT this slot holds a learned
"discrimination" `α`; here the topic weight replaces it.) From the correctness
logit:

```
hazard_logit(t) = correctness_logit(t) − c_i          # buzz now? (minus threshold)
S_i(t*)         = Π_{s < t*} (1 − sigmoid(hazard_logit(s)))   # survived to t* without buzzing
```

The **competing risk** is "who buzzes first." The log-likelihood for one tossup
event factorizes into:

- every rostered player's **survival** up to the stop position (they didn't buzz
  earlier), plus
- the **winner's hazard** at `t*` (they did buzz then), plus
- a **Bernoulli** on whether the winner's answer was correct.

Dead tossups (nobody buzzed) contribute survival all the way to `T_j`. In code
this is the hand-built `pyro.factor("...competing_risks_likelihood", ...)`,
reused unchanged from `topic_compirt/pyramidal.py`.

This is **not** a Normal regression on buzz time. Buzz timing is modeled through
a discrete-time survival process:

```
is_buzz_at_t ~ Bernoulli(sigmoid(hazard_logit(t)))
correct_if_buzzed ~ Bernoulli(sigmoid(correctness_logit(t*)))
```

The Normal distributions in this part of the model are priors on latent
parameters (`θ_player`, `c`, `difficulty_beta`), not the observation model for
buzz time.

Code map:

| Equation concept | Function / code object |
|---|---|
| `d_jk(t)` | `difficulty_curve` in `topic_compirt/pyramidal.py` |
| `Σ_k r_jk θ_ik` | `topic_weighted_skill` |
| correctness logit | `correctness_logit` |
| buzz hazard logit | `hazard_logit` |
| survival before first buzz | `log_survival` |
| full tossup likelihood | `pyro.factor("topic_weighted_competing_risks_likelihood", log_likelihood)` in `joint_pyramidal.py` |

### 3c. The combined objective

We fit one objective — the joint log-likelihood under the priors:

```
log p(words | θ_doc, topic_word)  · bow_weight          ← topic model (all docs)
+ log p(buzz/answer outcomes | θ_player, r_j, difficulty)  ← IRT (tossups only)
+ log priors on θ_doc, θ_player, c, difficulty
```

`bow_weight` is a scalar knob (`pyro.poutine.scale`) that balances the two
likelihoods. It matters because a document contributes thousands of word tokens
but a question contributes far fewer IRT observations — left unscaled, one term
can drown the other. Tune so both move.

**Bonuses** appear only in the first line (they share `topic_word`, so their topic vectors
live in the same space), but not in the IRT line — the pyramidal stage is
tossups only. Their difficulty is supervised later by the compositional stage.

Technically, the optimizer maximizes an **ELBO**, not the exact marginal
likelihood. The ELBO contains:

```
E_q[ bow_weight · log p(words | θ_doc, topic_word)
   + log p(IRT outcomes | θ_doc, θ_player, c, difficulty)
   + log p(latents | priors)
   - log q(latents) ]
```

`topic_word` is optimized as a parameter inside that objective. The other
unknowns have variational posteriors under `q`. So it is fair to say the code
fits `p(words, outcomes)` jointly, but the exact technical statement is:
**we optimize a variational lower bound on the joint model's evidence, with a
point estimate for `topic_word`.**

---

## 4. Inference: how we actually fit it

We use **stochastic variational inference (SVI)** in Pyro: approximate the true
posterior `p(latents | data)` with a tractable family `q`, and maximize the ELBO
by gradient ascent.

- **Guide (the `q`).** A single `AutoNormal` mean-field guide covers **every**
  latent: `θ_player`, `c`, the difficulty params, and crucially `θ_doc`.
  AutoNormal places an independent Gaussian in each latent's *unconstrained*
  space and pushes it through the constraint transform — for `θ_doc ~ Dirichlet`
  that transform maps the simplex to/from `ℝ^{K-1}` (stick-breaking). So we never
  optimize on the simplex directly.
- **Why one guide suffices.** There is **no amortizing encoder** (no neural net
  mapping a document to its `θ`). Each document simply has its own variational
  parameters. That's what lets us reuse the project's existing
  `topic_compirt.common.fit_svi` verbatim. (Dropping the encoder is the
  deliberate "supervised-LDA, not a neural topic model" choice; the cost is in
  §6.)
- **The topic-word matrix `topic_word` (`φ`).** A point-estimated `pyro.param`
  (`topic_word_logits`, softmax-normalized per topic) rather than a sampled
  latent — this is the variational-EM "M-step" treatment of topics, optimized
  directly by the same `ClippedAdam` step. There is no LDA `β`/`η` Dirichlet
  word-prior hyperparameter in this code. Initialized with small random noise so
  the `K` topics break symmetry instead of collapsing to identical rows.
- **Optimizer.** `ClippedAdam` over the ELBO; full-batch (no minibatching),
  because the competing-risks likelihood couples all players/rows.
- **Outputs are posterior medians.** After fitting, `guide.median(...)` gives a
  point estimate for each latent; `θ_doc` medians are the exported topic vectors.

Practical consequences:

- The exported CSVs are **summaries of the variational posterior**, not raw
  samples. If someone asks "where is the uncertainty?", it is in the guide's
  learned scales, but most downstream code consumes medians for compatibility
  with the existing CompIRT pipeline.
- `θ_doc` sparsity is controlled partly by the Dirichlet prior
  `topic_concentration` and partly by the likelihood. A document can still become
  nearly one-topic even with `α=1` if its words and outcomes strongly prefer one
  axis.
- Pyro does support enumeration for some discrete latent variables, but here
  enumeration is unnecessary because summing out the LDA word assignments is
  closed-form. We give SVI the already-marginalized likelihood.

---

## 5. End-to-end data flow

```
SQLite question text                 HuggingFace observation tables
        │                                       │
   load_documents()                    build_tossup_observations()
        │  (tokens per question)                │  (one row per player×tossup event)
        ▼                                       ▼
   build_vocabulary()                     tossup_tensors()  → data{player,tossup,
        │  (top words, min_df, rm_top)               t_star, T_j, y, is_buzz, ...}
        ▼                                       │
   bow_tensor(combined_ids)  ───────────────────┘
   (BoW matrix, TOSSUPS FIRST in data["tossup_ids"] order, then bonuses)
        │
        ▼
   joint_model  +  AutoNormal guide   ──fit_svi──▶  posterior medians + losses
        │                                               │
        │  θ_doc[:n_tossups] = tossup topic weights     │  θ_player, c, difficulty_beta, γ, μ
        ▼                                               ▼
   document_latent_vectors.csv          players.csv, tossups.csv,
   (tossup + bonus r_j vectors)         tossup_predictions.csv, topics.csv,
        │                               summary.json, loss_curve.png
        ▼
   downstream: train_joint_compositional.py  →  evaluate_compirt.py
```

The **tossups-first ordering** is load-bearing: the first `n_tossups` rows of the
document set are exactly `data["tossup_ids"]`, so `θ_doc[:n_tossups]` lines up
row-for-row with the IRT observations (`θ_doc[:n_tossups][data["tossup"]]`).

### Why bonuses are in the topic model at all

The downstream bonus (compositional) stage needs bonus topic vectors *in the same
topic space* as the tossups. Since there's no encoder to apply to new text, we
include bonuses as **word-only documents** in the joint fit: they get their own
`θ_doc` and reconstruct their own words through the **shared** `topic_word`. So their
vectors are consistent with the supervised tossup topics, even though bonus
outcomes don't enter the pyramidal IRT likelihood.

### Supervising the bonus topics too (learned compositional stage)

The pyramidal run leaves bonus topics word-only. The **learned compositional**
stage (`joint_compositional.py` / `train_joint_compositional.py`) closes that gap
— it's the bonus analogue of sLDA. It loads the pyramidal stage's player skills
`θ` and topic-word matrix `topic_word` and **freezes both**, then re-samples each bonus's
`θ_doc ~ Dirichlet` and fits it to two terms at once:

1. the LDA word likelihood `Multinomial(θ_doc · topic_word)` (with `topic_word` fixed), and
2. the compositional bonus-part likelihood, where `r_b = θ_doc` is the topic
   weight gating `A_b(R) = LSE_m(Σ_k r_bk θ_pmk; τ)` minus
   `Σ_k r_bk difficulty_beta_bk`.

So a bonus's **part-correctness** now pulls its topic proportions, exactly the way
tossup outcomes pull tossup topics. All three parts of a bonus share one `θ_doc`
(one document), so the supervision is per-bonus.

Why freeze `topic_word` (not refit it on bonus words)? The member score `Σ_k r_bk θ_pk`
only makes sense if dimension `k` of `r_b` means the same topic as dimension `k`
of the player skill `θ_p` — and that meaning is anchored by row `k` of
`topic_word`. Refitting `topic_word` would rotate the axes away from `θ` and
break the dot product. Freezing `topic_word` (and `θ`)
also keeps us faithful to CompIRT's two-stage design: bonus data never moves
player skills. The supervision therefore reshapes *where each bonus sits* in the
fixed topic space, not the axes themselves.

---

## 6. Design decisions & the FAQ technical people will ask

**"Why not just train LDA, then regress outcomes on the topics?"** That's the
two-stage baseline sLDA was invented to beat. Training jointly lets the outcomes
*reshape* the topics; the two-stage version freezes topics chosen for word-fit
only.

**"Why marginalize the discrete topic assignments instead of enumerating them?"**
Enumeration is possible in Pyro but expensive and unnecessary — the sum is
analytic and gives the clean `Multinomial(θφ)` mixture (§3a). Smooth objective,
standard SVI.

**"Why Dirichlet `θ` and a plain mixture decoder, instead of a neural
(logistic-normal / product-of-experts / encoder) topic model?"** Because we
specifically wanted classic **sLDA**, which is the Dirichlet + mixture model.
A neural amortized variant (an encoder producing `θ = softmax(MLP(bow))`) is a
*different* model; we deliberately don't use it. Trade-off in the next answer.

**"What do you lose by not having an encoder (no amortization)?"** Generalization
to unseen questions. With per-document latents, a brand-new question has no
`θ` until you do a **fold-in** (a few SVI steps on that document holding `topic_word`
fixed). An encoder would map any bag-of-words straight to a `θ`. We accepted this.

**"Why is `K` (topics) equal to the IRT skill dimension?"** Because `r_jk` gates
`θ_player[i,k]` — the topic axes *are* the skill axes. A question's topic mixture
literally says which skill coordinates it rewards. So `K` is not a free
topic-model hyperparameter; it's pinned to the IRT dimensionality.

**"How does `bow_weight` actually matter?"** It's the knob that decides how much
the topics must respect words vs. outcomes. Too low → topics ignore words and
become arbitrary skill directions (you lose interpretability). Too high → topics
ignore outcomes and you're back to unsupervised LDA. It's the one hyperparameter
worth sweeping.

**"How does `topic_concentration` differ from `bow_weight`?"**
`topic_concentration` is the Dirichlet prior strength on each document's
`θ_doc`. With `K=5`, `α<1` encourages sparse one-topic mixtures, `α=1` is uniform
over the simplex, and `α>1` pushes documents toward using multiple topics.
`bow_weight` does not change the prior; it changes how loudly the word likelihood
argues relative to the IRT likelihood. To make topic weights more distributed,
sweep `topic_concentration` upward first (`2`, `5`, maybe `10`), then try a lower
`bow_weight` if the word model is still making documents too one-hot.

**"If topic weights become almost one-hot, is that a bug?"** Not necessarily.
Many quizbowl questions really are mostly one subject. It becomes a problem if
the topics are supposed to represent mixed skill usage and instead the model is
just assigning each question to one subject plus a scalar difficulty. Diagnose it
by checking median max topic weight, topic entropy, `topics.csv`, and whether
response profiles separate across topics.

**"Why do the per-topic difficulty curves sometimes look like the same curve at
different heights?"** In this model `difficulty_beta_jk`, `γ_jk`, and `μ_jk` are
per tossup and per topic. If a tossup has weight `0.95` on topic 3, the
likelihood strongly identifies topic 3's difficulty curve and barely identifies
the other four. Those inactive curves often sit near small, generic shapes. That
is an interpretability warning, not a numerical error.

**"Would a simpler response model be more defensible?"** Maybe. A useful
ablation is to share some curve parameters, for example global or topic-global
`γ`/`μ`, and let only the difficulty scale vary by tossup. If performance barely
changes, the fully per-tossup-per-topic curves are overparameterized.

**"Where is canonical sLDA's `ηᵀ z_bar`?"** Replaced by the CompIRT likelihood.
Canonical binary sLDA might use
`y_d ~ Bernoulli(sigmoid(ηᵀ z_bar_d))`. Here the response is much richer:
survival over buzz position plus correctness, with player skill and threshold.
The shared topic vector is still the same sLDA bridge; only the response GLM is
specialized to quizbowl.

**"Identifiability — aren't topics only defined up to permutation/rotation?"**
Yes, as in any topic/factor model. The Dirichlet prior, the IRT structure, and
the random-but-seeded init pin a particular solution; absolute axis labels aren't
meaningful, but the *partition* of questions and the per-axis word lists are.
Compare runs by held-out metrics and topic content, not by raw coordinate values.

**"Is the per-document Dirichlet posterior really Gaussian (AutoNormal)?"** The
guide is a Gaussian in the unconstrained (stick-breaking) space, i.e. a
logistic-normal approximation to the Dirichlet posterior. That's a standard,
well-behaved choice; it's an approximation, not the exact posterior, like all VI.

**"Why point-estimate `topic_word` instead of sampling it from an LDA `β`
prior?"** Speed and simplicity — it's the EM M-step view of topics, and it keeps
a single AutoNormal over the remaining latents. Making `topic_word` fully
Bayesian (`φ_k ~ Dirichlet(β)`) is a possible change if you want posterior
uncertainty on the topics.

**"What exactly does `--calibrate-correctness` do?"** It applies a learned scale
and bias to the correctness logit before the Bernoulli correctness likelihood.
It does **not** change the word model, the buzz survival structure, or the
definition of topics. It can improve probability calibration while lowering AUC,
so report both discrimination and calibration metrics.

**"Is this in-sample unless we run the holdout pipeline?"** Yes. A normal
`--split year_2024` run fits and evaluates on 2024. The temporal holdout path
freezes the trained topic-word matrix and uses training player posteriors as
priors, then folds in held-out documents/responses under those fixed axes.

---

## 7. What comes out, and how to read it

| File | Contents |
|---|---|
| `document_latent_vectors.csv` | the learned topic vector `r_j` for every tossup **and** bonus (standard schema; consumed by the downstream stages) |
| `players.csv` | each player's skill vector `θ_player`, threshold `c`, and skill magnitude |
| `tossups.csv` | each tossup's per-topic difficulty params and its learned topic weight |
| `topics.csv` | the top words of each topic (from `topic_word`) — your interpretability handle |
| `tossup_predictions.csv` | per-row fitted correctness / hazard / survival |
| `summary.json` | run config + final loss |
| `loss_curve.png` | ELBO trajectory; should descend and flatten |

To sanity-check supervision worked, run `topic_response_profiles.py`: it groups
questions by their dominant topic and reports mean correctness / buzz position
per topic. If the topics captured difficulty, those should *separate* across
topics (and the `topics.csv` word lists should look subject-coherent).

### 7a. Diagnostic checklist before defending a run

| Question | What to inspect | Good sign | Warning sign |
|---|---|---|---|
| Are the topics word-coherent? | `topics.csv` | top words form recognizable subjects/styles | same generic words in every topic |
| Are topic weights too sparse? | `tossups.csv` `topic_weight_*` entropy / max weight | median max weight not always near 1 unless questions are genuinely single-subject | most tossups have max weight `>0.9` |
| Do topics affect responses? | `topic_response_profiles.py` | correctness or buzz timing differs by dominant topic | profiles nearly identical |
| Are difficulty curves identifiable? | `tossups.csv` `beta_*`, `gamma_*`, `mu_*`; curve plots | active topics carry meaningful curves; inactive curves are recognized as weakly identified | every topic looks like only a vertical rescale |
| Is calibration acceptable? | `tossup_metrics.csv` `ece`, `log_loss`, AUC | calibration and discrimination both reasonable | calibrated model improves ECE but destroys AUC |
| Is this a real generalization result? | output root / split names | temporal holdout path used | only in-sample split used |

If challenged on a visually repetitive curve plot, the precise answer is:
"The word topics may still be coherent, but the response-side difficulty curves
are weakly differentiated. That suggests the current per-tossup-per-topic curve
parameterization may be richer than the data can identify. We should compare
against a constrained curve ablation."

---

## 8. The thirty-word summary to memorize

> Every question gets a topic vector. That vector both generates the question's
> words (a Dirichlet topic model with the per-word topics integrated out) and
> tells an item-response model which skills the question rewards. Fitting both
> jointly by variational inference makes correctness reshape the topics. That's
> supervised LDA, fused with CompIRT.
