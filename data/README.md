# Local and Generated Data

The repository does not commit the source SQLite database or generated
HuggingFace tables. Place the source export at `data/database.db`, then build and
validate the linked tables from the repository root:

```bash
.venv/bin/python -B -m data_pipeline.build --overwrite
.venv/bin/python -B -m data_pipeline.validate
```

Generated outputs are written to `data/hf/quizbowl-irt/` and
`data/response_matrix.csv`. Inferred lineups are cached under `data/lineups/`.
All three locations are ignored by git.

The builder emits `all`, `year_2024`, and `year_2025` splits from the 2024–25
export. The current local `data/hf/quizbowl-irt/` is a one-off union that also
adds tossup-only records from nine 2023 tournaments to the `all` split;
`build_report.json` there records both sources and the resulting counts.
Rebuilding from `data/database.db` alone does not reproduce that extension.

See the [model data contract](../docs/dataset-schema.md) for table schemas,
derived training rows, and conversion requirements. Active-lineup inference is
specified in [`../lineup.py`](../lineup.py).
