# DD-Bernstein 10,000-step convergence experiment

Fresh training on all five year_2024 folds. Degree 3, dimensions 3, drop concentration 2, simplex relevance, learned locations and terminal intercepts; lr 0.005, split and optimization seeds 42, normalized likelihood, no posterior draws. Only training duration changes versus the 3,000-step normalized run.

Reuses repository command builders and GPU queue. Both GPUs; up to three processes per GPU so all five independent folds can run concurrently. Four CPU report workers. Training, frozen replay, evaluation, aggregation, and matched normalized event scoring are queued.

Fit root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-10000steps`.

Resume with `nohup /bin/bash /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/common/execution/dd-normalized-first-buzz-10000steps/resume.sh > /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/common/execution/dd-normalized-first-buzz-10000steps/nohup.log 2>&1 < /dev/null &` after confirming the old scheduler has exited. Successful stages are retained; interrupted training stages restart.
