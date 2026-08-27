# Analysis

Descriptive studies of the quizbowl dataset. Nothing here fits an IRT model, trains, or writes under `results/` — each folder is self-contained, reads the built HuggingFace tables under `data/hf/quizbowl-irt/`, and writes only its own `data/` and `figures/`.

For model fitting and evaluation see the family directories and `compirt_eval/` instead; for the dataset itself see [`../docs/dataset-schema.md`](../docs/dataset-schema.md).

| Folder | Scope | What it answers |
|---|---|---|
| [full_dataset_eda/](full_dataset_eda/) | Whole corpus: 68 sites, 9 question-set events, 2024–2025 | Corpus structure, season boundaries, tier gradient measured twice, cross-year player continuity, MDS at three grains |
| [season_2024_25_eda/](season_2024_25_eda/) | The one complete season: 33 sites, 4 events, Oct 2024 – Apr 2025 | Difficulty as a timing gradient, within-season player progression, selection measured on a fixed question set; complete category metadata |
| [acf_2024_eda/](acf_2024_eda/) | Calendar year 2024 only: 29 sites, 4 question-set events | Detailed single-year treatment of the 2024 sets |
| [buzz_accuracy_timing/](buzz_accuracy_timing/) | Focused study | Relationship between buzz accuracy and buzz timing, with robustness to the minimum-attempt threshold |
| [terminal_cell/](terminal_cell/) | Focused study | Empirical team first-buzz hazard cell by cell; why the final token position needs its own intercept |

The three EDA folders slice the same tables differently and are computed independently:

- **`full_dataset_eda/`** for anything about the corpus as a whole, or about the 2024-versus-2025 contrast.
- **`season_2024_25_eda/`** when the question is about a coherent competitive season. This is the cleanest slice — the only complete season, and the only one with no missing category metadata. Note that calendar-year splits cut this season in half, which `full_dataset_eda/` documents.
- **`acf_2024_eda/`** when the question is specifically about the four 2024 question sets.

They overlap on shared events and should agree there.

Each folder documents its own reproduction command in its `README.md`.
