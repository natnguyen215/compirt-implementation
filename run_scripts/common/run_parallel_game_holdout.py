"""Schedule DD-Bernstein and multidimensional frozen folds across shared GPUs.

Reuses the existing runners' command builders, bonus audits, and aggregators.
Training and CUDA replay share a dynamic queue; reports use separate CPU slots.
Run under nohup for terminal-independent execution. Repeat the same arguments
and roots to resume successfully completed stages.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
import math
from pathlib import Path

from holdout.game_splits import game_holdout_split_name
from run_scripts.double_difficulty import run_dd_bernstein_332 as dd
from run_scripts.common.lib.gpu_queue import Task, run_queue, validate_tasks
from run_scripts.common.run_compirt_holdout import (
    HoldoutConfig, build_frozen_holdout_stages, output_paths,
)
from utils.run_logging import resolve_result_root

REPO_ROOT = Path(__file__).resolve().parents[2]
PYTHON = str(REPO_ROOT / ".venv/bin/python")
FOLDS = list(range(5))


def python_call(source, *arguments):
    return [PYTHON, "-B", "-u", "-c", source, *map(str, arguments)]


def configurations(args):
    config = dd.Configuration(
        root=str(args.dd_root), base_split=args.base_split, folds=FOLDS,
        split_seed=args.split_seed, optimization_seed=args.seed,
        degree=args.degree, dimensions=args.dd_dimensions,
        drop_concentration=args.drop_concentration, relevance_prior="simplex",
        learned_curve_locations=True, terminal_intercepts=True,
        steps=args.steps, lr=args.dd_lr, device="cuda", posterior_draws=0,
        incorrect_weight=1.0, player_neg_propensity=False, data_dir=None,
    )
    bonus = [PYTHON, "-B", "-u", "-m", "run_scripts.common.run_compositional_from_folds",
             "--stage1-root", str(args.dd_root), "--root", str(args.bonus_root),
             "--folds", *map(str, FOLDS), "--arms", "compositional", "synergy",
             "--alpha-prior", "gamma", "--steps", str(args.bonus_steps),
             "--lr", str(args.bonus_lr), "--seed", str(args.seed), "--device", "cuda"]
    return config, bonus


def multidim_config(args, fold):
    return HoldoutConfig(
        model="multidim", frozen_predict="1",
        train_split=game_holdout_split_name(args.base_split, "train", 5, fold, args.split_seed),
        test_split=game_holdout_split_name(args.base_split, "test", 5, fold, args.split_seed),
        new_player_prior="tier", tournament="", root=str(args.multidim_root / f"fold_{fold}"),
        pyramidal_steps=str(args.steps), bonus_steps=str(args.bonus_steps),
        dimensions=str(args.multidim_dimensions), difficulty_link="sigmoid",
        lr=str(args.multidim_lr), seed=str(args.seed), device="cuda",
        calibrate_correctness="0", run_synergy="1", synergy_dimensions=str(args.synergy_dimensions),
        save_synergy_details="1", mplconfigdir="/tmp/matplotlib-compirt",
    )


def build_tasks(args):
    config, bonus_command = configurations(args)
    tasks = [Task("dd-prepare", python_call(
        "import json, sys; from run_scripts.double_difficulty.run_dd_bernstein_332 import "
        "Configuration, snapshot_configuration; "
        "snapshot_configuration(Configuration(**json.loads(sys.argv[1])))",
        json.dumps(asdict(config))), gpu=False,
        outputs=(str(args.dd_root / "configuration.json"),))]
    dd_evaluations, multidim_comparisons, bonus_evaluations = [], [], []
    dd_training = []
    for fold in FOLDS:
        previous = "dd-prepare"
        _, stages = dd.experiment_commands(config, fold)
        for name, expected, command in stages:
            task_name = f"dd-{fold}-{name}"
            tasks.append(Task(task_name, list(map(str, command)), (previous,),
                              gpu=name != "evaluation", outputs=(str(expected),),
                              priority=100 if name == "train" else 10))
            previous = task_name
        dd_training.append(f"dd-{fold}-train")
        dd_evaluations.append(previous)

        mirt = multidim_config(args, fold)
        dependencies = {
            "train-pyramidal": (),
            "train-compositional": ("train-pyramidal",),
            "train-synergy": ("train-pyramidal",),
            "frozen-pyramidal": ("train-pyramidal",),
            "frozen-compositional": ("train-compositional",),
            "frozen-synergy": ("train-synergy",),
            "holdout-evaluation": ("frozen-pyramidal", "frozen-compositional"),
            "holdout-synergy-evaluation": ("frozen-pyramidal", "frozen-synergy"),
            "compare-bonus-models": ("holdout-evaluation", "holdout-synergy-evaluation"),
        }
        for stage in build_frozen_holdout_stages(mirt, output_paths(mirt.root)):
            command = list(map(str, stage.command))
            output = Path(command[command.index("--output-dir") + 1])
            gpu = stage.name.startswith(("train-", "frozen-"))
            expected = (str(output / "summary.json"),) if gpu else ()
            if stage.name in ("holdout-evaluation", "holdout-synergy-evaluation"):
                expected = tuple(str(output / "csvs" / f"{kind}_metrics.csv") for kind in ("tossup", "bonus"))
            task_name = f"multidim-{fold}-{stage.name}"
            tasks.append(Task(task_name, command,
                              tuple(f"multidim-{fold}-{name}" for name in dependencies[stage.name])
                              or ("dd-prepare",),
                              gpu=gpu, outputs=expected,
                              priority=100 if stage.name == "train-pyramidal" else
                              50 if stage.name.startswith("train-") else 10))
        multidim_comparisons.append(f"multidim-{fold}-compare-bonus-models")

    tasks.append(Task("bonus-prepare", [*bonus_command, "--prepare-only"], tuple(dd_training),
                      gpu=False, outputs=(str(args.bonus_root / "configuration.json"),)))
    for fold in FOLDS:
        for arm in ("compositional", "synergy"):
            previous = "bonus-prepare"
            for stage in ("train", "replay", "evaluate"):
                task_name = f"bonus-{fold}-{arm}-{stage}"
                run = args.bonus_root / f"fold_{fold}"
                output = (run / ("train" if stage == "train" else "holdout") / arm / "summary.json"
                          if stage != "evaluate" else run / f"{arm}_checks.json")
                tasks.append(Task(task_name, [*bonus_command, "--worker-fold", str(fold),
                                              "--worker-arm", arm, "--worker-stage", stage],
                                  (previous,), gpu=stage != "evaluate", outputs=(str(output),),
                                  priority=50 if stage == "train" else 10))
                previous = task_name
            bonus_evaluations.append(previous)
    tasks.append(Task("dd-aggregate", python_call(
        "import json, sys; from run_scripts.double_difficulty.run_dd_bernstein_332 import "
        "Configuration, run_fold, aggregate; c = Configuration(**json.loads(sys.argv[1])); "
        "[run_fold(c, f) for f in c.folds]; aggregate(c)", json.dumps(asdict(config))),
        tuple(dd_evaluations), gpu=False,
        outputs=(str(args.dd_root / "aggregate/pooled.csv"),)))
    tasks.append(Task("bonus-aggregate", [*bonus_command, "--collect-only"],
                      tuple(bonus_evaluations), gpu=False,
                      outputs=(str(args.bonus_root / "aggregate/report.md"),)))
    tasks.append(Task("multidim-aggregate", python_call(
        "import sys; from run_scripts.common.run_compirt_game_holdout import aggregate_folds; "
        "aggregate_folds(sys.argv[1], int(sys.argv[2]))", args.multidim_root, 5),
        tuple(multidim_comparisons), gpu=False,
        outputs=(str(args.multidim_root / "aggregate/summary.md"),)))
    validate_tasks(tasks)
    return tasks


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("root", "dd-root", "bonus-root", "multidim-root"):
        parser.add_argument(f"--{name}", type=Path, required=True)
    parser.add_argument("--gpus", nargs="+", type=int, default=[0, 1])
    parser.add_argument("--jobs-per-gpu", type=int, default=2)
    parser.add_argument("--cpu-jobs", type=int, default=2)
    parser.add_argument("--base-split", default="year_2024")
    parser.add_argument("--split-seed", type=int, default=42)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--degree", type=int, default=3)
    parser.add_argument("--dd-dimensions", type=int, default=3)
    parser.add_argument("--drop-concentration", type=float, default=2.0)
    parser.add_argument("--multidim-dimensions", type=int, default=5)
    parser.add_argument("--synergy-dimensions", type=int, default=3)
    parser.add_argument("--steps", type=int, default=3000)
    parser.add_argument("--bonus-steps", type=int, default=2000)
    parser.add_argument("--dd-lr", type=float, default=0.005)
    parser.add_argument("--bonus-lr", type=float, default=0.01)
    parser.add_argument("--multidim-lr", type=float, default=0.01)
    parser.add_argument("--survival-chunk", type=int, default=2048)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if not args.gpus or min(args.gpus) < 0 or len(set(args.gpus)) != len(args.gpus):
        parser.error("--gpus must contain distinct nonnegative indexes")
    for name in ("jobs_per_gpu", "cpu_jobs", "degree", "dd_dimensions", "multidim_dimensions",
                 "synergy_dimensions", "steps", "bonus_steps", "survival_chunk", "dd_lr",
                 "bonus_lr", "multidim_lr", "drop_concentration"):
        if not math.isfinite(getattr(args, name)) or getattr(args, name) <= 0:
            parser.error(f"--{name.replace('_', '-')} must be positive and finite")
    roots = []
    for name in ("root", "dd_root", "bonus_root", "multidim_root"):
        value = Path(resolve_result_root(getattr(args, name), "holdout")).resolve()
        setattr(args, name, value)
        roots.append(value)
    if any(a == b or a in b.parents or b in a.parents
           for i, a in enumerate(roots) for b in roots[i + 1:]):
        parser.error("Use four distinct, non-nested output roots")
    return args


def main(argv=None):
    args = parse_args(argv)
    tasks = build_tasks(args)
    if args.dry_run:
        print(json.dumps([asdict(task) for task in tasks], indent=2))
        return
    if not (args.root / "queue.json").exists():
        for path in (args.dd_root, args.bonus_root, args.multidim_root):
            if path.exists() and any(path.iterdir()):
                raise ValueError(f"A new queue requires fresh output roots: {path}")
    environment = {"OMP_NUM_THREADS": "1", "MKL_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
                   "PYTHONUNBUFFERED": "1", "PYTHONDONTWRITEBYTECODE": "1",
                   "MPLBACKEND": "Agg", "MPLCONFIGDIR": "/tmp/matplotlib-compirt",
                   "COMPIRT_SURVIVAL_CHUNK": str(args.survival_chunk)}
    sources = ["run_scripts/common/run_parallel_game_holdout.py", "run_scripts/common/lib/gpu_queue.py",
               "run_scripts/common/run_compositional_from_folds.py", "run_scripts/common/run_compirt_holdout.py",
               "run_scripts/double_difficulty/run_dd_bernstein_332.py", "compirt_race.py",
               "hazard_double_difficulty/bernstein/pyramidal_model.py",
               "hazard_double_difficulty/bernstein/train_pyramidal.py",
               "multidimensional/multidim_mirt/pyramidal_model.py",
               "multidimensional/multidim_mirt/train_pyramidal.py",
               "compositional_model.py", "train_compositional.py", "holdout/frozen_predict.py"]
    contract = {path: hashlib.sha256((REPO_ROOT / path).read_bytes()).hexdigest() for path in sources}
    run_queue(tasks, args.root, cwd=REPO_ROOT, environment=environment, gpus=args.gpus,
              jobs_per_gpu=args.jobs_per_gpu, cpu_jobs=args.cpu_jobs, contract=contract)


if __name__ == "__main__":
    main()
