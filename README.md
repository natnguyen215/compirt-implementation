# Quizbowl IRT

This project builds linked quizbowl datasets and uses Pyro to model player and
team performance.


## Repository Layout

The root CompIRT files are separated by responsibility through their names:

- `pyramidal_model.py` and `compositional_model.py`: paper equation implementations.
- `compirt_data.py`: observation and tensor construction.
- `train_pyramidal.py` and `train_compositional.py`: experiment training.
- `evaluate_compirt.py` and the `compirt_eval/` package: the executed evaluation code
   plus its metrics, figures, and per-scenario (tossup/bonus) modules.
- `data_pipeline/`: source-database to Hugging Face dataset builder and validator.
- `run_scripts/run_compirt.sh` / `run_scripts/run_compirt.py`: end to end configurable
  experiment (train, evaluate, and compare in one pass). Both python and bash versions.
- `run_scripts/run_compirt_2024.sh` / `run_scripts/run_compirt_2024.py`:
  full-2024 reproducibility wrapper. It runs dataset validation, then calls the
  configurable runner with all-2024 defaults.
- `topic/`: topic-model experiments — `topic/fixed/` (topics fit upstream via
  LDA/PLDA/categories and fed in as fixed weights), `topic/learned/` (topics
  learned jointly with the IRT model), and shared topic helpers in `topic/utils/`.
- `tfidf/`: isolated cumulative IDF-aware pyramidal model for clue timing.
- `multidimensional/`: multidimensional-difficulty experiments —
  `multidimensional/multidim_mirt/` (the multidimensional-skill pyramidal
  variant, with a free learned relevance vector `r`),
  `multidimensional/embedding_mirt/` (sibling whose `r` is instead a
  CAIMIRA-style relevance vector computed from a frozen Qwen3-Embedding-8B
  vector of the question text through a learned linear projection). The
  embedding variant reuses `multidim_mirt`'s tossup math and the root
  `compositional_model.py` rather than duplicating them. Both name the weight
  `r` rather than the baseline's `alpha` because their difficulty is
  per-dimension; see the naming convention in `CLAUDE.md`.

Variant scripts run as modules from the repo root, e.g.
`.venv/bin/python -m topic.fixed.train_topic_pyramidal --help`.

See `docs/compirt-experiments.md` for setup, commands, assumptions, and
limitations, including the opt-in temporal C1--C4 roster-generalization
evaluation (`RUN_C1_C4=1`).

# CompIRT Paper Implementation

Each file has a module docstring and per-function paper-equation references; the smaller
helper functions sit above the `run_experiment`/`main` entry point that ties
them together.

1. `compirt_data.py`: turns the linked tables into model-ready observations and
   padded tensors (paper Section 3.1 tossups, Section 3.2 bonus parts).
2. `pyramidal_model.py`: the Stage 1 tossup competing-risks model
   (Eq. 3-7 and the dead-tossup survival term in Eq. 13).
3. `train_pyramidal.py`: fits Stage 1 and saves player/tossup parameters; start
   at `run_experiment`.
4. `compositional_model.py`: the Stage 2 bonus model that holds player skill
   `theta` fixed and learns how parts reward it (Eq. 8 aggregation, Eq. 10
   synergy, Eq. 11 outcome).
5. `train_compositional.py`: fits Stage 2 from the saved `theta`; start at
   `run_experiment`.
6. `evaluate_compirt.py`: turns saved predictions into metrics and figures; start
   at `main`, which calls the two scenario modules in `compirt_eval/`
   (`tossups/` is paper Scenario A, `bonuses.py` is Scenario B; `metrics.py`
   and `figures.py` hold the shared math and plotting helpers).


## Dataset Pipeline

`data_pipeline.dataset` builds the linked HuggingFace tables from
`data/database.db`. Player rows that share the same raw player slug are grouped
under that slug; the builder does not attempt cross-slug identity resolution.

Rebuild and validate the generated data:

```bash
.venv/bin/python -m data_pipeline.build --overwrite
.venv/bin/python -m data_pipeline.validate
```

The full table schema is documented in `docs/dataset-schema.md`.

## Tests

```bash
.venv/bin/python -m unittest discover -s tests -v
```

## Important Implementation Details

- Eq. 9 (Noisy-OR) not implemented
- Neg handling/bounce back not implemented
- Game-specific lineups are inferred from buzz evidence (`lineup.py`, cached under
  `data/lineups/`) rather than taken from the full registered roster, so the tossup
  competing-risks population and the bonus aggregation/synergy run over the ~4 players
  who plausibly played each game. Games with no buzz evidence fall back to the full
  roster. Each bonus reuses the inferred lineup of the tossup in the same cycle.
- SVI used instead of MCMC
- Current local data covers 2024-2025 and links players by exact raw slug, not the paper's proposed 2023-2025 fuzzy/manual linking procedure.
