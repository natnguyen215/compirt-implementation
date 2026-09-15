# Detached two-GPU retraining

Started 2026-09-13T15:03:50.594162-07:00; initial scheduler PID 1393882.
The old single-GPU process was stopped with authorization; its existing root was preserved.

Two simultaneous CUDA jobs per GPU, plus two independent CPU report workers.
The queue covers all five folds and both bonus arms for DD and multidimensional fits.
Each trainer keeps the original steps, learning rates, split/optimization seeds, and model settings.

## Output roots

- root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/common/parallel-normalized-v1-20260913-150350`
- dd-root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-20260913-150350`
- bonus-root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350`
- multidim-root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/multidim-normalized-v1-20260913-150350`

## Monitor

```bash
RUN=/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/common/parallel-normalized-v1-20260913-150350
tail -f "$RUN/nohup.log"
# Current task assignments and failures:
cat "$RUN/status.json"
# Per-task training progress:
tail -n 10 "$RUN"/logs/*train*.log
# Live GPU usage:
watch -n 2 nvidia-smi
```

The scheduler log records stage transitions; logs/ contains the actual training output.
At the initial verification, both GPUs were training (83% and 96% utilization).
GPU percentages vary with loading, individual jobs, and CPU-only reporting.

## Stop and resume

```bash
RUN=/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/common/parallel-normalized-v1-20260913-150350
kill -TERM "$(cat "$RUN/scheduler.pid")"
```

Wait for the scheduler to stop its workers. After interruption, resume using:

```bash
RUN=/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/common/parallel-normalized-v1-20260913-150350
nohup /bin/bash "$RUN/resume.sh" >> "$RUN/nohup.log" 2>&1 < /dev/null &
echo $! > "$RUN/scheduler.pid"
```

Keep all four output paths. Completed stages resume from the queue's success markers;
unfinished training restarts. A concurrent scheduler is rejected by the run lock.
Changed source hashes or configurations require a fresh run root.

All repository checks passed before launch. Research logs and frozen-skills
comparison tables are not automatically rewritten by this run.
