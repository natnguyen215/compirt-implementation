"""A resumable dependency queue with shared GPU slots and separate CPU workers."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shlex
import signal
import subprocess
import time


@dataclass(frozen=True)
class Task:
    name: str
    command: list[str]
    needs: tuple[str, ...] = ()
    gpu: bool = True
    outputs: tuple[str, ...] = ()
    priority: int = 0


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def validate_tasks(tasks):
    by_name = {task.name: task for task in tasks}
    if len(by_name) != len(tasks):
        raise ValueError("Duplicate task names")
    for task in tasks:
        if not task.name or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-_" for c in task.name):
            raise ValueError(f"Invalid task name: {task.name}")
        if not task.command or set(task.needs) - by_name.keys():
            raise ValueError(f"Empty command or unknown dependencies: {task.name}")
    visited = set()
    while len(visited) < len(tasks):
        ready = {t.name for t in tasks if t.name not in visited and set(t.needs) <= visited}
        if not ready:
            raise ValueError("Task dependency cycle")
        visited.update(ready)


def run_queue(tasks, root, *, cwd, environment, gpus=(0, 1), jobs_per_gpu=1,
              cpu_jobs=2, contract=None, poll_seconds=1):
    """Run ready tasks, refilling the least occupied GPU after each completion.

    A task resumes only from a successful subprocess exit plus its expected
    artifacts. Independent tasks continue after failures; dependents stay
    blocked. SIGTERM/interrupt stops entire child process groups before the
    run lock is released, so a resume cannot overlap surviving workers.
    """
    validate_tasks(tasks)
    if not gpus or len(set(gpus)) != len(gpus) or min(gpus) < 0:
        raise ValueError("GPU indexes must be distinct and nonnegative")
    if jobs_per_gpu < 1 or cpu_jobs < 1:
        raise ValueError("Worker counts must be positive")
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    with (root / "queue.lock").open("w") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeError(f"Another scheduler owns {root}") from error
        manifest = {"tasks": [asdict(task) for task in tasks],
                    "environment": environment, "contract": contract}
        # Normalize tuples the same way they will be loaded from JSON.
        manifest = json.loads(json.dumps(manifest))
        configuration = root / "queue.json"
        if configuration.exists() and json.loads(configuration.read_text()) != manifest:
            raise ValueError(f"Queue configuration changed; use a fresh root: {root}")
        write_json(configuration, manifest)
        signature = hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()
        done, failed, running, records = set(), {}, {}, {}
        by_name = {task.name: task for task in tasks}
        for task in tasks:
            marker = root / "complete" / f"{task.name}.json"
            if marker.exists():
                saved = json.loads(marker.read_text())
                if saved.get("signature") == signature and all(Path(p).exists() for p in task.outputs):
                    done.add(task.name)
        # A missing prerequisite artifact also invalidates its dependents.
        while True:
            invalid = {name for name in done if not set(by_name[name].needs) <= done}
            if not invalid:
                break
            done.difference_update(invalid)
        pending = {task.name for task in tasks} - done
        for name in pending:
            (root / "complete" / f"{name}.json").unlink(missing_ok=True)

        def log(message):
            print(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {message}", flush=True)

        def status(state):
            write_json(root / "status.json", {
                "state": state, "pid": os.getpid(), "total": len(tasks),
                "completed": sorted(done), "failed": failed,
                "pending": sorted(pending), "running": records,
                "gpus": list(gpus), "jobs_per_gpu": jobs_per_gpu,
                "updated_at": datetime.now(timezone.utc).isoformat(),
            })

        def interrupt(signum, frame):
            raise KeyboardInterrupt

        old_term = signal.signal(signal.SIGTERM, interrupt)
        try:
            log(f"Queue: {len(tasks)} tasks; {len(done)} resumed; GPUs {list(gpus)}, "
                f"{jobs_per_gpu} slots/GPU, {cpu_jobs} CPU workers")
            status("running")
            while pending or running:
                changed = False
                for name, (process, handle, gpu) in list(running.items()):
                    code = process.poll()
                    if code is None:
                        continue
                    handle.close()
                    del running[name]
                    record = records.pop(name)
                    task = by_name[name]
                    missing = [p for p in task.outputs if not Path(p).exists()]
                    if code == 0 and not missing:
                        write_json(root / "complete" / f"{name}.json",
                                   {**record, "signature": signature, "exit_code": code})
                        done.add(name)
                        log(f"DONE {name} on {'CPU' if gpu is None else f'GPU {gpu}'}")
                    else:
                        failed[name] = {"exit_code": code, "missing_outputs": missing,
                                        "log": record["log"]}
                        log(f"FAILED {name}: exit={code}, missing={missing}; log={record['log']}")
                    changed = True

                ready = sorted((t for t in tasks if t.name in pending and set(t.needs) <= done),
                               key=lambda t: -t.priority)
                for task in ready:
                    loads = {g: sum(r[2] == g for r in running.values()) for g in gpus}
                    if task.gpu:
                        gpu = min(gpus, key=lambda g: loads[g])
                        if loads[gpu] >= jobs_per_gpu:
                            continue
                    else:
                        gpu = None
                        if sum(r[2] is None for r in running.values()) >= cpu_jobs:
                            continue
                    env = {**os.environ, **environment,
                           "CUDA_VISIBLE_DEVICES": "" if gpu is None else str(gpu),
                           "GPU": "cpu" if gpu is None else str(gpu)}
                    env.pop("COMPIRT_LOG_ACTIVE", None)
                    log_path = root / "logs" / f"{task.name}.log"
                    log_path.parent.mkdir(parents=True, exist_ok=True)
                    handle = log_path.open("a")
                    handle.write(f"\nSTART {datetime.now(timezone.utc).isoformat()} GPU={gpu}\n"
                                 f"{shlex.join(task.command)}\n")
                    handle.flush()
                    try:
                        process = subprocess.Popen(task.command, cwd=cwd, env=env,
                                                   stdin=subprocess.DEVNULL, stdout=handle,
                                                   stderr=subprocess.STDOUT, start_new_session=True)
                    except OSError as error:
                        handle.close()
                        failed[task.name] = {"exit_code": None, "error": str(error), "log": str(log_path)}
                        pending.remove(task.name)
                        log(f"FAILED to start {task.name}: {error}")
                        changed = True
                        continue
                    running[task.name] = process, handle, gpu
                    records[task.name] = {"pid": process.pid, "gpu": gpu, "log": str(log_path),
                                          "started_at": datetime.now(timezone.utc).isoformat()}
                    pending.remove(task.name)
                    log(f"START {task.name} on {'CPU' if gpu is None else f'GPU {gpu}'} pid={process.pid}")
                    changed = True
                if changed:
                    status("running")
                if not running:
                    if pending:
                        log(f"Blocked by failed prerequisites: {sorted(pending)}")
                    break
                time.sleep(poll_seconds)
            state = "failed" if failed or pending else "complete"
            status(state)
            log(f"Queue {state}: {len(done)}/{len(tasks)} tasks completed")
            if state != "complete":
                raise RuntimeError(f"Queue has failed or blocked tasks; inspect {root / 'status.json'}")
        except BaseException as error:
            # Suppress repeated termination while reaping each complete process tree.
            signal.signal(signal.SIGTERM, signal.SIG_IGN)
            for process, _, _ in running.values():
                try:
                    os.killpg(process.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
            deadline = time.monotonic() + 10
            for process, handle, _ in running.values():
                try:
                    process.wait(timeout=max(0, deadline - time.monotonic()))
                except subprocess.TimeoutExpired:
                    pass
                # Also stop descendants whose parent already exited.
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                process.wait()
                handle.close()
            pending.update(running)
            records.clear()
            status("interrupted" if isinstance(error, KeyboardInterrupt) else "failed")
            raise
        finally:
            signal.signal(signal.SIGTERM, old_term)
