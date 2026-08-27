#!/usr/bin/env python3
"""Run the default double-Bernstein ablation across independent CUDA workers.

This launcher keeps one grid runner per selected GPU, writes a log per worker,
and runs the final aggregate collection only after every shard succeeds.  The
underlying runner remains resumable, so relaunching after interruption skips
completed train, replay, and evaluation stages.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from utils.run_logging import resolve_result_root

PYTHON = REPO_ROOT / ".venv" / "bin" / "python"
RUNNER = "run_scripts.bernstein.run_dd_bernstein_ablation"
DEFAULT_ROOT = Path("results/compirt/holdout/double-difficulty/ablations/hyperparameter-grid")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--gpus", nargs="+", type=int, default=[0, 1])
    parser.add_argument("--base-split", default="year_2024")
    parser.add_argument("--split-seed", type=int, default=42)
    parser.add_argument("--optimization-seed", type=int, default=42)
    parser.add_argument("--steps", type=int, default=3000)
    parser.add_argument("--lr", type=float, default=0.005)
    parser.add_argument("--posterior-draws", type=int, default=0)
    args = parser.parse_args(argv)
    if not args.gpus or len(set(args.gpus)) != len(args.gpus):
        parser.error("--gpus must contain distinct GPU indexes")
    if any(gpu < 0 for gpu in args.gpus):
        parser.error("--gpus values must be non-negative")
    return args


def common_command(args, root: Path) -> list[str]:
    return [
        str(PYTHON),
        "-m",
        RUNNER,
        "--root",
        str(root),
        "--base-split",
        args.base_split,
        "--split-seed",
        str(args.split_seed),
        "--optimization-seed",
        str(args.optimization_seed),
        "--steps",
        str(args.steps),
        "--lr",
        str(args.lr),
        "--device",
        "cuda",
        "--posterior-draws",
        str(args.posterior_draws),
    ]


def main(argv=None) -> None:
    args = parse_args(argv)
    args.root = Path(resolve_result_root(args.root, "holdout"))
    root = args.root if args.root.is_absolute() else REPO_ROOT / args.root
    root.mkdir(parents=True, exist_ok=True)
    base = common_command(args, root)
    # Establish the immutable configuration before workers start so they never
    # race while creating configuration.json.
    setup_log = root / "setup.log"
    with setup_log.open("a", encoding="utf-8") as handle:
        subprocess.run(
            [*base, "--collect-only"],
            cwd=REPO_ROOT,
            stdout=handle,
            stderr=subprocess.STDOUT,
            check=True,
            text=True,
        )
    workers = []
    manifest = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "gpus": args.gpus,
        "workers": [],
    }
    for shard_index, gpu in enumerate(args.gpus):
        command = [
            *base,
            "--shard-count",
            str(len(args.gpus)),
            "--shard-index",
            str(shard_index),
            "--skip-aggregate",
        ]
        log_path = root / f"worker_gpu_{gpu}.log"
        handle = log_path.open("a", encoding="utf-8")
        handle.write(
            f"\n=== launcher start {datetime.now(timezone.utc).isoformat()} ===\n"
        )
        handle.flush()
        env = dict(os.environ)
        env["CUDA_VISIBLE_DEVICES"] = str(gpu)
        process = subprocess.Popen(
            command,
            cwd=REPO_ROOT,
            env=env,
            stdout=handle,
            stderr=subprocess.STDOUT,
            text=True,
        )
        workers.append((gpu, process, handle, log_path))
        manifest["workers"].append(
            {
                "gpu": gpu,
                "pid": process.pid,
                "log": str(log_path),
                "command": command,
            }
        )
        print(f"GPU {gpu}: pid={process.pid} log={log_path}", flush=True)
    status_path = root / "parallel_run.json"
    status_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    failure = None
    try:
        while any(process.poll() is None for _, process, _, _ in workers):
            for gpu, process, _, _ in workers:
                code = process.poll()
                if code not in (None, 0):
                    failure = (gpu, code)
                    break
            if failure is not None:
                break
            time.sleep(10)
        if failure is not None:
            for _, process, _, _ in workers:
                if process.poll() is None:
                    process.terminate()
        return_codes = {
            str(gpu): process.wait() for gpu, process, _, _ in workers
        }
    finally:
        for _, _, handle, _ in workers:
            handle.close()

    manifest["finished_at"] = datetime.now(timezone.utc).isoformat()
    manifest["return_codes"] = return_codes
    if any(code != 0 for code in return_codes.values()):
        manifest["status"] = "failed"
        status_path.write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
        )
        raise SystemExit(f"One or more workers failed: {return_codes}")

    print("All GPU workers complete; collecting pooled rankings.", flush=True)
    aggregate_log = root / "aggregate.log"
    with aggregate_log.open("a", encoding="utf-8") as handle:
        subprocess.run(
            [*base, "--collect-only"],
            cwd=REPO_ROOT,
            stdout=handle,
            stderr=subprocess.STDOUT,
            check=True,
            text=True,
        )
    manifest["status"] = "complete"
    manifest["aggregate_log"] = str(aggregate_log)
    status_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Complete: {root / 'aggregate' / 'summary.md'}", flush=True)


if __name__ == "__main__":
    main()
