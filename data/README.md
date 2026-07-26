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
All three locations are ignored because they are reproducible local artifacts.

See [`../docs/dataset-schema.md`](../docs/dataset-schema.md) for table schemas
and [`../docs/lineup-inference.md`](../docs/lineup-inference.md) for lineup rules.
