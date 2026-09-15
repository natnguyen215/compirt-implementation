#!/usr/bin/env python3
"""Targeted worst-case drops: how few dropped events flip a top pair? (Tier 2)

The headline check of arXiv 2508.11847, with a heuristic influence proxy in
place of their AMIP selector: drop the target player's strongest evidence
(direction "demote": their correct buzzes, earliest first; "promote": their
negs) in increasing prefix sizes, refit each Stage-1 family at the fixed
seed, and record when the target-vs-rival predicted-PPG ordering flips. Every
flip is refit-confirmed. The raw actual-PPG gap is evaluated at every prefix
length without a refit, giving that method's exact minimal flip count.

The recommended workflow reuses a Tier-1 root's full and noise-floor fits:

    .venv/bin/python run_scripts/common/run_targeted_drop.py \
        --reuse-full results/compirt/in_sample/common/drop-robustness

Without '--reuse-full', pass '--target-player' and '--rival' explicitly and
the runner fits its own full references. A pair flip only counts as a finding
when the induced gap change clearly exceeds the pair's seed-noise gap std.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_data import DEFAULT_DATA_DIR
from compirt_eval.common import player_scoring
from compirt_eval.drop_robustness.figures import save_targeted_outputs
from compirt_eval.drop_robustness.layout import (
    count_list_path,
    full_dir,
    targeted_cell_dir,
    targeted_droplist_dir,
)
from compirt_eval.drop_robustness.perturbations import (
    rank_events_for_target,
    write_drop_list,
)
from compirt_eval.drop_robustness.tier1 import ranking_for
from compirt_eval.drop_robustness.tier2 import (
    collect_results,
    reference_dirs,
    report_flip_brackets,
    resolve_pair,
)
from run_scripts.common.lib.ablation import (
    Stage,
    configure_environment,
    path_for_command,
    repo_path,
    run_stage,
    save_ablation_config,
    start_run_log,
    validate_ablation_resume,
)
from run_scripts.common.lib.drop_training import FAMILY_DEFAULTS, train_command
from utils.run_logging import format_run_log_header, resolve_result_root

DEFAULT_ROOT = Path("results/compirt/in_sample/common/drop-robustness-targeted")
DEFAULT_COUNTS = (5, 10, 25, 50, 100, 200)


def generate_droplists(args: argparse.Namespace, observations, target: str):
    """Save the full ranked-event table once and every count-prefix list.

    Existing files are kept (completed fits were trained against them)."""
    ranked = rank_events_for_target(observations, target, args.direction)
    if ranked.empty:
        raise ValueError(f"{target} has no {args.direction} candidate events")
    directory = targeted_droplist_dir(args.root, args.direction, target)
    ranked_path = directory / "ranked_events.csv"
    if not ranked_path.exists():
        directory.mkdir(parents=True, exist_ok=True)
        ranked.to_csv(ranked_path, index=False)
    usable_counts = [count for count in args.counts if count <= len(ranked)]
    skipped = [count for count in args.counts if count > len(ranked)]
    if skipped:
        print(
            f"skip counts {skipped}: {target} has only {len(ranked)} "
            f"{args.direction} candidates",
            flush=True,
        )
    for count in usable_counts:
        path = count_list_path(args.root, args.direction, target, count)
        if not path.exists():
            write_drop_list(path, ranked["event_id"].head(count).tolist())
    return ranked, usable_counts


def build_stages(args: argparse.Namespace, target: str, counts) -> list[Stage]:
    """Local full fits (only when not reusing Tier 1) plus one refit per
    (model, count)."""
    stages = []
    for model in args.models:
        if args.reuse_full is None:
            full = full_dir(args.root, model)
            stages.append(
                Stage(
                    f"{model}-full",
                    full / "summary.json",
                    train_command(args, model, full, args.seed),
                )
            )
        for count in counts:
            cell = targeted_cell_dir(args.root, model, args.direction, target, count)
            stages.append(
                Stage(
                    f"{model}-{args.direction}-n{count}",
                    cell / "summary.json",
                    train_command(
                        args,
                        model,
                        cell,
                        args.seed,
                        drop_file=count_list_path(
                            args.root, args.direction, target, count
                        ),
                    ),
                )
            )
    return stages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument(
        "--models",
        nargs="+",
        choices=tuple(FAMILY_DEFAULTS),
        default=list(FAMILY_DEFAULTS),
    )
    parser.add_argument(
        "--reuse-full",
        type=Path,
        help="Tier-1 root whose full and noise-floor fits are reused as the "
        "references (recommended); otherwise pass --target-player/--rival",
    )
    parser.add_argument(
        "--reference-model",
        choices=tuple(FAMILY_DEFAULTS),
        default="multidim",
        help="whose full ranking picks the default target pair",
    )
    parser.add_argument("--target-player")
    parser.add_argument("--target-rank", type=int)
    parser.add_argument("--rival")
    parser.add_argument("--direction", choices=("demote", "promote"), default="demote")
    parser.add_argument("--counts", nargs="+", type=int, default=list(DEFAULT_COUNTS))
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--split", default="year_2024")
    parser.add_argument("--tournament")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument(
        "--difficulty-link", choices=("sigmoid", "tanh"), default="sigmoid"
    )
    parser.add_argument("--dimensions", type=int)
    parser.add_argument("--steps", type=int)
    parser.add_argument("--lr", type=float)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument(
        "--python",
        type=Path,
        default=Path(os.environ.get("PYTHON", REPO_ROOT / ".venv" / "bin" / "python")),
    )
    parser.add_argument("--rerun", action="store_true")
    parser.add_argument("--collect-only", action="store_true")
    args = parser.parse_args()
    args.root = Path(resolve_result_root(repo_path(args.root), "in_sample"))
    args.reuse_full = repo_path(args.reuse_full)
    args.data_dir = repo_path(args.data_dir)
    if args.reuse_full is None and not (args.target_player and args.rival):
        raise ValueError(
            "Auto pair selection needs an existing full fit: pass "
            "--reuse-full <tier1-root>, or name --target-player and --rival"
        )
    if args.reference_model not in args.models:
        raise ValueError("--reference-model must be one of --models")
    return args


def main() -> None:
    args = parse_args()
    configure_environment()
    start_run_log(args.root)
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/common/run_targeted_drop.py",
                "ROOT": path_for_command(args.root),
                "MODELS": args.models,
                "REUSE_FULL": path_for_command(args.reuse_full)
                if args.reuse_full is not None
                else "",
                "REFERENCE_MODEL": args.reference_model,
                "DIRECTION": args.direction,
                "COUNTS": args.counts,
                "SPLIT": args.split,
                "TOURNAMENT": args.tournament or "<all>",
                "DIFFICULTY_LINK": args.difficulty_link,
                "SEED": args.seed,
                "DEVICE": args.device,
                "COLLECT_ONLY": args.collect_only,
                "RERUN": args.rerun,
            }
        ),
        flush=True,
    )

    observations = player_scoring.build_observations(
        args.split, args.tournament, args.data_dir or DEFAULT_DATA_DIR
    )
    _, full_data, full_games = player_scoring.tensors_and_games(observations)

    if args.target_player and args.rival:
        target, rival = args.target_player, args.rival
    else:
        reference_full, _ = reference_dirs(args, args.reference_model)
        if not (reference_full / "summary.json").exists():
            raise RuntimeError(
                f"No full {args.reference_model} fit at "
                f"{path_for_command(reference_full)}; run Tier 1 first"
            )
        reference_ppg = ranking_for(
            args,
            args.reference_model,
            reference_full,
            observations,
            full_data,
            full_games,
        )
        target, rival = resolve_pair(args, reference_ppg)
    print(f"\nTarget pair: {target} (target) vs {rival} (rival), "
          f"direction={args.direction}\n", flush=True)

    ranked, counts = generate_droplists(args, observations, target)

    if not args.collect_only:
        stages = build_stages(args, target, counts)
        validate_ablation_resume(args.root, stages, args.rerun)
        config_path = save_ablation_config(args.root, args, stages)
        print(f"Wrote run configuration to {path_for_command(config_path)}\n", flush=True)
        for stage in stages:
            run_stage(stage, args.rerun)

    frame, actual = collect_results(args, observations, target, rival, ranked, counts)
    save_targeted_outputs(args.root, frame, actual)
    report_flip_brackets(frame, actual)
    print(f"\nWrote metrics to {path_for_command(args.root / 'csvs')}")


if __name__ == "__main__":
    main()
