# Bonus difficulty across the 2024–25 season

Fresh in-sample parameter fits for all 17 models in
[`RESEARCH_LOG_2.md`](../../../../../RESEARCH_LOG_2.md#full-season-bonus-difficulty-ordering).
The research log contains the findings; this directory stores the fits and
their audit tables. The metric definitions are in
[`compirt_eval/METRICS.md`](../../../../../compirt_eval/METRICS.md#research-log-bonus-classification-and-difficulty-ordering).

## Population and configuration

`season_2024_25` selects tournament dates from July 2024 through June 2025:
Fall and Winter 2024, Regionals and Nationals 2025. The local population is
33 mirror sites, 2,661 games, and 49,042 bonus responses. The source contains
1,359 bonus question records; 1,296 were heard and can receive fitted bonus
parameters. The 63 unheard questions do not enter difficulty-order scores.

Both tossup skill sources are fitted jointly across the season, with no
calendar-year transfer or test fitting. DD uses the degree-3 Bernstein model,
3D skills, drop concentration 2, simplex relevance, learned curve locations,
terminal intercepts, and the normalized first-buzz likelihood. The
multidimensional reference uses 5D skills and sigmoid difficulty curves.
Both use 3,000 SVI steps, with learning rates 0.005 and 0.01, respectively.

The 13 DD bonus variants use the same frozen DD skills, Gamma loading priors,
and 3,000 steps at learning rate 0.01. The two multidimensional bonus variants
use the same frozen 5D skills, Normal loading priors, 2,000 steps at 0.01,
and either no synergy or additive dot synergy in 3D. Team IRT 1D/3D use
3,000 steps at 0.01 and their existing Gamma-loading/simplex-relevance priors.
All optimization seeds are 42. No correctness calibration or bounceback
phases are enabled. Each configuration is fitted once to the whole season;
these are parameter diagnostics, not five-fold generalization estimates.

`configuration.json` maps model labels to fit directories and records source
and data hashes. `execution/queue.json` records every exact training command,
dependency, and environment setting. `execution/status.json` records progress,
`execution/complete/` stores successful task markers, and `execution/logs/`
contains the training output. Stage-1 outputs are in `{dd,multidim}/pyramidal/`;
the other model directories contain the bonus fits.

## Difficulty artifacts

Effective part difficulty is `beta` for scalar models and
`sum_k r_k * beta_k` for vector-difficulty models, using saved posterior
medians. One bonus scores 1 exactly when easy < medium < hard, and 0 otherwise.
Source difficulty labels identify the three parts. Ties fail strict ordering.

| Artifact | Grain and calculation |
| --- | --- |
| `bonus_difficulty_order.csv` | One model/bonus row; effective easy, medium, hard difficulties and `order_score` |
| `difficulty_means_by_tournament.csv` | One model/site/declared-difficulty row; mean over distinct fitted parts heard at that site, plus count |
| `difficulty_means_by_set.csv` | One model/question-set/declared-difficulty row; mean over distinct fitted parts across all mirrors, plus count |
| `difficulty_summary.csv` | Per-model bonus-order rate, site and set ordering counts, equal-site season means, and tier ordering/pair agreement |
| `season_observed_conversion.csv` | Per-tier observed conversion and PPB; response, question, and site aggregation checks |
| `validation.json` | Fitted parameter coverage, input hashes, losses, and unknown-roster exclusions |

The [ordering uncertainty follow-up](../../../../../RESEARCH_LOG_2.md#how-certain-are-the-individual-bonus-orderings)
uses only `dd/multidim-difficulty-synergy`, reading its saved fit without
retraining. The original 17-model ordering table remains the point-estimate
comparison.

| Uncertainty artifact | Grain and calculation |
| --- | --- |
| `bonus_difficulty_uncertainty.csv` | One row per fitted bonus in the selected model; original score, attempt count, both adjacent difficulty gaps, sampled gap quantiles, and probability of the full expected order |
| `bonus_difficulty_uncertainty_by_attempts.csv` | Counts, ordering rates, median point gaps, and posterior support summaries for all sets and each set, overall and in 1–9 / 10–19 / 20–29 / 30+ attempt groups |
| `bonus_difficulty_uncertainty_method.json` | Input hashes, quantile-to-distribution calculation, 20,000 draws per bonus, seed 42, array order, package versions, and validation record |

An attempt is one distinct bonus `response_id`, not one part row. Grouping by
attempts reuses the full-season fit; it does not remove training observations.
The uncertainty calculation reconstructs independent Normal `beta` and Normal
`log(r)` distributions from their saved AutoNormal quantiles, then recomputes
`r dot beta` in each draw. Its intervals are conditional on frozen player skills
and the saved fit. The calculation record describes the one-off extraction;
findings are edited directly in the research log.

The expected tier order is Fall < Winter < Regionals < Nationals. Each of the
six strict pairwise inequalities earns one agreement; ties earn zero. Check
each declared difficulty separately. The research log cites ACF's event
descriptions and reports full-season observed conversion as context.

The Team IRT helper writes both `bonus_part_predictions.csv` and
`train_bonus_part_predictions.csv`. Here they contain the same full-season
fitted responses: neither is a held-out prediction table.

## Resume the recorded commands

Run from the repository root with the same code and data. This uses the
existing GPU queue and its completion markers:

```bash
.venv/bin/python -B - <<'PY'
import json
from pathlib import Path
from run_scripts.common.lib.gpu_queue import Task, run_queue

root = Path('results/compirt/in_sample/common/bonus-difficulty-season-2024-25')
saved = json.loads((root / 'execution/queue.json').read_text())
run_queue(
    [Task(**task) for task in saved['tasks']], root / 'execution',
    cwd=Path.cwd(), environment=saved['environment'],
    contract=saved['contract'], gpus=(0, 1), jobs_per_gpu=1, cpu_jobs=1,
)
PY
```

Changed model settings, code, or data require a fresh result root. Findings
are edited directly in the research log; no report generator is used.
