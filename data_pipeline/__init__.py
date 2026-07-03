"""Build and validate the linked quizbowl datasets used by experiments.

* 'schema' -- the output HuggingFace table schema (features, primary keys).
* 'text_cleaning' -- HTML/question-text cleanup helpers.
* 'identity' -- readable ID assignment and dedup for teams/players/scores.
* 'dataset' -- reads the raw SQLite export and writes the linked tables
  ('build_dataset_directory' is the main entry point; see its docstring).
* 'validate' -- independently checks a built dataset for internal
  consistency and agreement with its source database.
* 'build' -- CLI wrapper around 'dataset.build_dataset_directory'.
"""
