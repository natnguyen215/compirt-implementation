#!/usr/bin/env bash
set -uo pipefail

# Retrain the existing in-sample and temporal-holdout CompIRT result roots.
#
# Default behavior is nohup-first: the parent process detaches a child, prints
# the PID/log paths, and exits. Set FOREGROUND=1 to run in the current shell.
# Existing result roots are reused in place; no result directory is deleted.

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

if [[ "${FOREGROUND:-0}" != "1" && "${COMPIRT_RETRAIN_NOHUP_CHILD:-0}" != "1" ]]; then
  log_dir="${LOG_DIR:-logs/retrain_existing_compirt_results}"
  mkdir -p "$log_dir"
  timestamp="$(date +%Y%m%d-%H%M%S)"
  log_path="$log_dir/$timestamp.log"
  pid_path="$log_dir/$timestamp.pid"

  nohup env COMPIRT_RETRAIN_NOHUP_CHILD=1 "$BASH" "$0" "$@" >"$log_path" 2>&1 &
  child_pid="$!"
  printf '%s\n' "$child_pid" >"$pid_path"

  echo "Started CompIRT retrain batch with nohup."
  echo "PID: $child_pid"
  echo "PID file: $pid_path"
  echo "Log: $log_path"
  if [[ "${DRY_RUN:-0}" == "1" ]]; then
    echo "DRY_RUN=1 is active; inspect the log for the command matrix."
    wait "$child_pid"
    child_status="$?"
    echo "Dry-run child exited with status $child_status."
    exit "$child_status"
  fi
  exit 0
fi

PYTHON="${PYTHON:-.venv/bin/python}"
GPU="${GPU:-0}"
DEVICE="${DEVICE:-cuda}"
SPLIT="${SPLIT:-year_2024}"
TRAIN_SPLIT="${TRAIN_SPLIT:-year_2024}"
TEST_SPLIT="${TEST_SPLIT:-year_2025}"
TOURNAMENT="${TOURNAMENT-}"
NEW_PLAYER_PRIOR="${NEW_PLAYER_PRIOR:-tier}"
SEED="${SEED:-42}"

BASELINE_DIMENSIONS="${BASELINE_DIMENSIONS:-5}"
BASELINE_PYRAMIDAL_STEPS="${BASELINE_PYRAMIDAL_STEPS:-5000}"
BASELINE_BONUS_STEPS="${BASELINE_BONUS_STEPS:-3000}"
BASELINE_LR="${BASELINE_LR:-${LR:-0.005}}"

TOPIC_DIMENSIONS="${TOPIC_DIMENSIONS:-5}"
CATEGORY_DIMENSIONS="${CATEGORY_DIMENSIONS:-13}"
TOPIC_PYRAMIDAL_STEPS="${TOPIC_PYRAMIDAL_STEPS:-5000}"
TOPIC_BONUS_STEPS="${TOPIC_BONUS_STEPS:-3000}"
TOPIC_LR="${TOPIC_LR:-${LR:-0.005}}"
TOPIC_PYRAMIDAL_DEVICE="${TOPIC_PYRAMIDAL_DEVICE:-$DEVICE}"
CATEGORY_PYRAMIDAL_DEVICE="${CATEGORY_PYRAMIDAL_DEVICE:-$TOPIC_PYRAMIDAL_DEVICE}"

LEARNED_DIMENSIONS="${LEARNED_DIMENSIONS:-5}"
LEARNED_PYRAMIDAL_STEPS="${LEARNED_PYRAMIDAL_STEPS:-5000}"
LEARNED_BONUS_STEPS="${LEARNED_BONUS_STEPS:-3000}"
LEARNED_LR="${LEARNED_LR:-${LR:-0.005}}"

MULTIDIM_DIMENSIONS="${MULTIDIM_DIMENSIONS:-5}"
MULTIDIM_PYRAMIDAL_STEPS="${MULTIDIM_PYRAMIDAL_STEPS:-3000}"
MULTIDIM_BONUS_STEPS="${MULTIDIM_BONUS_STEPS:-2000}"
MULTIDIM_LR="${MULTIDIM_LR:-${LR:-0.01}}"

SYNERGY_DIMENSIONS="${SYNERGY_DIMENSIONS:-3}"
DRY_RUN="${DRY_RUN:-0}"
CONTINUE_ON_ERROR="${CONTINUE_ON_ERROR:-0}"

PLDA_TOPIC_VECTORS="${PLDA_TOPIC_VECTORS:-topic/fixed/outputs/plda/document_latent_vectors.csv}"
LDA_TOPIC_VECTORS="${LDA_TOPIC_VECTORS:-topic/fixed/outputs/lda/document_latent_vectors.csv}"
CATEGORY_TOPIC_VECTORS="${CATEGORY_TOPIC_VECTORS:-topic/fixed/outputs/category/document_latent_vectors.csv}"
CATEGORY_TOPIC_NAMES="${CATEGORY_TOPIC_NAMES:-topic/fixed/outputs/category/category_index.csv}"

export CUDA_VISIBLE_DEVICES="$GPU"
export PYTHONUNBUFFERED=1
export MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/matplotlib-compirt}"
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

FAILED_JOBS=()

print_cmd() {
  printf '+'
  printf ' %q' "$@"
  printf '\n'
}

run_cmd() {
  print_cmd "$@"
  if [[ "$DRY_RUN" == "1" ]]; then
    return 0
  fi
  "$@"
}

tournament_args() {
  if [[ -n "$TOURNAMENT" ]]; then
    printf '%s\n' --tournament "$TOURNAMENT"
  fi
}

run_baseline_insample() {
  local root="$1"
  local calibrate="$2"

  run_cmd env \
    PYTHON="$PYTHON" \
    GPU="$GPU" \
    SPLIT="$SPLIT" \
    TOURNAMENT="$TOURNAMENT" \
    ROOT="$root" \
    PYRAMIDAL_STEPS="$BASELINE_PYRAMIDAL_STEPS" \
    BONUS_STEPS="$BASELINE_BONUS_STEPS" \
    DIMENSIONS="$BASELINE_DIMENSIONS" \
    LR="$BASELINE_LR" \
    SEED="$SEED" \
    RUN_SYNERGY=1 \
    SYNERGY_DIMENSIONS="$SYNERGY_DIMENSIONS" \
    SAVE_SYNERGY_DETAILS=1 \
    CALIBRATE_CORRECTNESS="$calibrate" \
    "$PYTHON" run_scripts/common/run_compirt.py
}

run_baseline_holdout() {
  local root="$1"
  local calibrate="$2"

  run_cmd env \
    PYTHON="$PYTHON" \
    GPU="$GPU" \
    MODEL=baseline \
    TRAIN_SPLIT="$TRAIN_SPLIT" \
    TEST_SPLIT="$TEST_SPLIT" \
    TOURNAMENT="$TOURNAMENT" \
    ROOT="$root" \
    PYRAMIDAL_STEPS="$BASELINE_PYRAMIDAL_STEPS" \
    BONUS_STEPS="$BASELINE_BONUS_STEPS" \
    DIMENSIONS="$BASELINE_DIMENSIONS" \
    LR="$BASELINE_LR" \
    SEED="$SEED" \
    DEVICE="$DEVICE" \
    NEW_PLAYER_PRIOR="$NEW_PLAYER_PRIOR" \
    RUN_SYNERGY=1 \
    SYNERGY_DIMENSIONS="$SYNERGY_DIMENSIONS" \
    SAVE_SYNERGY_DETAILS=1 \
    CALIBRATE_CORRECTNESS="$calibrate" \
    "$PYTHON" run_scripts/common/run_compirt_holdout.py
}

run_multidim_insample() {
  local root="$1"
  local calibrate="$2"

  run_cmd env \
    PYTHON="$PYTHON" \
    GPU="$GPU" \
    SPLIT="$SPLIT" \
    TOURNAMENT="$TOURNAMENT" \
    ROOT="$root" \
    PYRAMIDAL_STEPS="$MULTIDIM_PYRAMIDAL_STEPS" \
    BONUS_STEPS="$MULTIDIM_BONUS_STEPS" \
    DIMENSIONS="$MULTIDIM_DIMENSIONS" \
    LR="$MULTIDIM_LR" \
    SEED="$SEED" \
    DEVICE="$DEVICE" \
    SYNERGY_DIMENSIONS="$SYNERGY_DIMENSIONS" \
    SAVE_SYNERGY_DETAILS=1 \
    CALIBRATE_CORRECTNESS="$calibrate" \
    "$PYTHON" run_scripts/multidimensional/multidim/run_multidim_compirt.py
}

run_multidim_holdout() {
  local root="$1"
  local calibrate="$2"

  run_cmd env \
    PYTHON="$PYTHON" \
    GPU="$GPU" \
    MODEL=multidim \
    TRAIN_SPLIT="$TRAIN_SPLIT" \
    TEST_SPLIT="$TEST_SPLIT" \
    TOURNAMENT="$TOURNAMENT" \
    ROOT="$root" \
    PYRAMIDAL_STEPS="$MULTIDIM_PYRAMIDAL_STEPS" \
    BONUS_STEPS="$MULTIDIM_BONUS_STEPS" \
    DIMENSIONS="$MULTIDIM_DIMENSIONS" \
    LR="$MULTIDIM_LR" \
    SEED="$SEED" \
    DEVICE="$DEVICE" \
    NEW_PLAYER_PRIOR="$NEW_PLAYER_PRIOR" \
    RUN_SYNERGY=1 \
    SYNERGY_DIMENSIONS="$SYNERGY_DIMENSIONS" \
    SAVE_SYNERGY_DETAILS=1 \
    CALIBRATE_CORRECTNESS="$calibrate" \
    "$PYTHON" run_scripts/common/run_compirt_holdout.py
}

run_topic_insample() {
  local root="$1"
  local vectors="$2"
  local dimensions="$3"
  local topic_names="$4"
  local calibrate="$5"

  run_cmd env \
    PYTHON="$PYTHON" \
    GPU="$GPU" \
    DEVICE="$DEVICE" \
    SPLIT="$SPLIT" \
    TOURNAMENT="$TOURNAMENT" \
    ROOT="$root" \
    RUN_PLDA=0 \
    TOPIC_VECTORS="$vectors" \
    TOPIC_NAMES="$topic_names" \
    DIMENSIONS="$dimensions" \
    PYRAMIDAL_STEPS="$TOPIC_PYRAMIDAL_STEPS" \
    BONUS_STEPS="$TOPIC_BONUS_STEPS" \
    LR="$TOPIC_LR" \
    SEED="$SEED" \
    RUN_SYNERGY=1 \
    SYNERGY_DIMENSIONS="$SYNERGY_DIMENSIONS" \
    SAVE_SYNERGY_DETAILS=1 \
    CALIBRATE_CORRECTNESS="$calibrate" \
    EVALUATE=1 \
    bash topic/fixed/run_topic_compirt.sh
}

run_topic_holdout() {
  local root="$1"
  local vectors="$2"
  local dimensions="$3"
  local topic_names="$4"
  local calibrate="$5"
  local pyramidal_device="$6"
  local cal_args=()
  local names_args=()
  local t_args=()

  if [[ "$calibrate" == "1" ]]; then
    cal_args=(--calibrate-correctness)
  fi
  if [[ -n "$topic_names" ]]; then
    names_args=(--topic-names "$topic_names")
  fi
  if [[ -n "$TOURNAMENT" ]]; then
    t_args=(--tournament "$TOURNAMENT")
  fi

  run_cmd "$PYTHON" -m topic.fixed.train_topic_pyramidal \
    --split "$TRAIN_SPLIT" \
    "${t_args[@]}" \
    --topic-vectors "$vectors" \
    --dimensions "$dimensions" \
    --steps "$TOPIC_PYRAMIDAL_STEPS" \
    --lr "$TOPIC_LR" \
    --seed "$SEED" \
    --device "$pyramidal_device" \
    "${cal_args[@]}" \
    --output-dir "$root/train/pyramidal" || return

  run_cmd "$PYTHON" -m topic.fixed.train_topic_pyramidal \
    --split "$TEST_SPLIT" \
    "${t_args[@]}" \
    --topic-vectors "$vectors" \
    --dimensions "$dimensions" \
    --steps "$TOPIC_PYRAMIDAL_STEPS" \
    --lr "$TOPIC_LR" \
    --seed "$SEED" \
    --device "$pyramidal_device" \
    --train-posterior "$root/train/pyramidal/player_posterior.csv" \
    --new-player-prior "$NEW_PLAYER_PRIOR" \
    "${cal_args[@]}" \
    --output-dir "$root/holdout/pyramidal" || return

  run_cmd "$PYTHON" -m topic.fixed.train_topic_compositional \
    --split "$TEST_SPLIT" \
    "${t_args[@]}" \
    --topic-vectors "$vectors" \
    --player-skills "$root/holdout/pyramidal/players.csv" \
    --steps "$TOPIC_BONUS_STEPS" \
    --lr "$TOPIC_LR" \
    --seed "$SEED" \
    --device "$DEVICE" \
    "${cal_args[@]}" \
    --output-dir "$root/holdout/compositional" || return

  run_cmd "$PYTHON" -m topic.fixed.train_topic_compositional \
    --split "$TEST_SPLIT" \
    "${t_args[@]}" \
    --topic-vectors "$vectors" \
    --player-skills "$root/holdout/pyramidal/players.csv" \
    --use-synergy \
    --synergy-dimensions "$SYNERGY_DIMENSIONS" \
    --save-synergy-details \
    --steps "$TOPIC_BONUS_STEPS" \
    --lr "$TOPIC_LR" \
    --seed "$SEED" \
    --device "$DEVICE" \
    "${cal_args[@]}" \
    --output-dir "$root/holdout/synergy" || return

  run_cmd "$PYTHON" -m topic.fixed.evaluate_topic_compirt \
    --pyramidal-results "$root/holdout/pyramidal" \
    --compositional-results "$root/holdout/compositional" \
    "${names_args[@]}" \
    --output-dir "$root/holdout/evaluation" || return

  run_cmd "$PYTHON" -m topic.fixed.evaluate_topic_compirt \
    --pyramidal-results "$root/holdout/pyramidal" \
    --compositional-results "$root/holdout/synergy" \
    "${names_args[@]}" \
    --output-dir "$root/holdout/synergy-evaluation"
}

run_learned_insample() {
  local root="$1"
  local calibrate="$2"
  local cal_args=()
  local t_args=()

  if [[ "$calibrate" == "1" ]]; then
    cal_args=(--calibrate-correctness)
  fi
  if [[ -n "$TOURNAMENT" ]]; then
    t_args=(--tournament "$TOURNAMENT")
  fi

  run_cmd "$PYTHON" -m topic.learned.train_joint_pyramidal \
    --split "$SPLIT" \
    "${t_args[@]}" \
    --dimensions "$LEARNED_DIMENSIONS" \
    --steps "$LEARNED_PYRAMIDAL_STEPS" \
    --lr "$LEARNED_LR" \
    --device "$DEVICE" \
    "${cal_args[@]}" \
    --output-dir "$root/pyramidal" || return

  run_cmd "$PYTHON" -m topic.learned.train_joint_compositional \
    --split "$SPLIT" \
    "${t_args[@]}" \
    --player-skills "$root/pyramidal/players.csv" \
    --topic-model-dir "$root/pyramidal" \
    --steps "$LEARNED_BONUS_STEPS" \
    --lr "$LEARNED_LR" \
    --device "$DEVICE" \
    "${cal_args[@]}" \
    --output-dir "$root/compositional" || return

  run_cmd "$PYTHON" -m topic.learned.train_joint_compositional \
    --split "$SPLIT" \
    "${t_args[@]}" \
    --player-skills "$root/pyramidal/players.csv" \
    --topic-model-dir "$root/pyramidal" \
    --use-synergy \
    --synergy-dimensions "$SYNERGY_DIMENSIONS" \
    --save-synergy-details \
    --steps "$LEARNED_BONUS_STEPS" \
    --lr "$LEARNED_LR" \
    --device "$DEVICE" \
    "${cal_args[@]}" \
    --output-dir "$root/synergy" || return

  run_cmd "$PYTHON" -m topic.fixed.evaluate_topic_compirt \
    --pyramidal-results "$root/pyramidal" \
    --compositional-results "$root/compositional" \
    --output-dir "$root/evaluation" || return

  run_cmd "$PYTHON" -m topic.fixed.evaluate_topic_compirt \
    --pyramidal-results "$root/pyramidal" \
    --compositional-results "$root/synergy" \
    --output-dir "$root/synergy-evaluation" || return

  run_cmd "$PYTHON" run_scripts/common/run_synergy_comparison.py \
    --compositional-metrics "$root/evaluation/csvs/bonus_metrics.csv" \
    --synergy-metrics "$root/synergy-evaluation/csvs/bonus_metrics.csv" \
    --output-dir "$root/comparison"
}

run_learned_holdout() {
  local root="$1"
  local calibrate="$2"
  local cal_args=()
  local t_args=()

  if [[ "$calibrate" == "1" ]]; then
    cal_args=(--calibrate-correctness)
  fi
  if [[ -n "$TOURNAMENT" ]]; then
    t_args=(--tournament "$TOURNAMENT")
  fi

  run_cmd "$PYTHON" -m topic.learned.train_joint_pyramidal \
    --split "$TRAIN_SPLIT" \
    "${t_args[@]}" \
    --dimensions "$LEARNED_DIMENSIONS" \
    --steps "$LEARNED_PYRAMIDAL_STEPS" \
    --lr "$LEARNED_LR" \
    --device "$DEVICE" \
    "${cal_args[@]}" \
    --output-dir "$root/train/pyramidal" || return

  run_cmd "$PYTHON" -m topic.learned.train_joint_pyramidal \
    --split "$TEST_SPLIT" \
    "${t_args[@]}" \
    --dimensions "$LEARNED_DIMENSIONS" \
    --steps "$LEARNED_PYRAMIDAL_STEPS" \
    --lr "$LEARNED_LR" \
    --device "$DEVICE" \
    --train-posterior "$root/train/pyramidal/player_posterior.csv" \
    --train-topic-model "$root/train/pyramidal" \
    --new-player-prior "$NEW_PLAYER_PRIOR" \
    "${cal_args[@]}" \
    --output-dir "$root/holdout/pyramidal" || return

  run_cmd "$PYTHON" -m topic.learned.train_joint_compositional \
    --split "$TEST_SPLIT" \
    "${t_args[@]}" \
    --player-skills "$root/holdout/pyramidal/players.csv" \
    --topic-model-dir "$root/train/pyramidal" \
    --steps "$LEARNED_BONUS_STEPS" \
    --lr "$LEARNED_LR" \
    --device "$DEVICE" \
    "${cal_args[@]}" \
    --output-dir "$root/holdout/compositional" || return

  run_cmd "$PYTHON" -m topic.learned.train_joint_compositional \
    --split "$TEST_SPLIT" \
    "${t_args[@]}" \
    --player-skills "$root/holdout/pyramidal/players.csv" \
    --topic-model-dir "$root/train/pyramidal" \
    --use-synergy \
    --synergy-dimensions "$SYNERGY_DIMENSIONS" \
    --save-synergy-details \
    --steps "$LEARNED_BONUS_STEPS" \
    --lr "$LEARNED_LR" \
    --device "$DEVICE" \
    "${cal_args[@]}" \
    --output-dir "$root/holdout/synergy" || return

  run_cmd "$PYTHON" -m topic.fixed.evaluate_topic_compirt \
    --pyramidal-results "$root/holdout/pyramidal" \
    --compositional-results "$root/holdout/compositional" \
    --output-dir "$root/holdout/evaluation" || return

  run_cmd "$PYTHON" -m topic.fixed.evaluate_topic_compirt \
    --pyramidal-results "$root/holdout/pyramidal" \
    --compositional-results "$root/holdout/synergy" \
    --output-dir "$root/holdout/synergy-evaluation"
}

run_job() {
  local label="$1"
  shift

  echo
  echo "## $label"
  if "$@"; then
    echo "ok: $label"
    return 0
  fi

  local status="$?"
  echo "failed ($status): $label" >&2
  if [[ "$CONTINUE_ON_ERROR" == "1" ]]; then
    FAILED_JOBS+=("$label")
    return 0
  fi
  exit "$status"
}

# Ordered batch specification. Each command is stored as a real Bash array so
# environment-supplied paths retain whitespace and delimiter characters.
RETRAIN_JOB_LABELS=()
RETRAIN_JOB_COMMAND_NAMES=()

register_job() {
  local label="$1"
  shift
  local command_name="RETRAIN_JOB_COMMAND_${#RETRAIN_JOB_LABELS[@]}"
  RETRAIN_JOB_LABELS+=("$label")
  RETRAIN_JOB_COMMAND_NAMES+=("$command_name")
  declare -g -a "$command_name"
  local -n command_ref="$command_name"
  command_ref=("$@")
}

register_job "in-sample baseline all-2024" run_baseline_insample results/compirt/in_sample/baseline/all-2024 0
register_job "holdout baseline all-2024" run_baseline_holdout results/compirt/holdout/baseline/all-2024 0
register_job "in-sample baseline baseline-all2024-cal" run_baseline_insample results/compirt/in_sample/baseline/baseline-all2024-cal 1
register_job "holdout baseline all2024-cal using 5d/5000/3000/3d synergy" run_baseline_holdout results/compirt/holdout/baseline/all2024-cal 1
register_job "in-sample PLDA all2024" run_topic_insample results/compirt/in_sample/topic/plda-all2024 "$PLDA_TOPIC_VECTORS" "$TOPIC_DIMENSIONS" "" 0
register_job "holdout PLDA all2024" run_topic_holdout results/compirt/holdout/topic/plda-all2024 "$PLDA_TOPIC_VECTORS" "$TOPIC_DIMENSIONS" "" 0 "$TOPIC_PYRAMIDAL_DEVICE"
register_job "in-sample PLDA all2024 cal" run_topic_insample results/compirt/in_sample/topic/plda-all2024-cal "$PLDA_TOPIC_VECTORS" "$TOPIC_DIMENSIONS" "" 1
register_job "holdout PLDA all2024 cal" run_topic_holdout results/compirt/holdout/topic/plda-all2024-cal "$PLDA_TOPIC_VECTORS" "$TOPIC_DIMENSIONS" "" 1 "$TOPIC_PYRAMIDAL_DEVICE"
register_job "in-sample LDA all2024" run_topic_insample results/compirt/in_sample/topic/lda-all2024 "$LDA_TOPIC_VECTORS" "$TOPIC_DIMENSIONS" "" 0
register_job "holdout LDA all2024" run_topic_holdout results/compirt/holdout/topic/lda-all2024 "$LDA_TOPIC_VECTORS" "$TOPIC_DIMENSIONS" "" 0 "$TOPIC_PYRAMIDAL_DEVICE"
register_job "in-sample LDA all2024 cal" run_topic_insample results/compirt/in_sample/topic/lda-all2024-cal "$LDA_TOPIC_VECTORS" "$TOPIC_DIMENSIONS" "" 1
register_job "holdout LDA all2024 cal" run_topic_holdout results/compirt/holdout/topic/lda-all2024-cal "$LDA_TOPIC_VECTORS" "$TOPIC_DIMENSIONS" "" 1 "$TOPIC_PYRAMIDAL_DEVICE"
register_job "in-sample category all2024" run_topic_insample results/compirt/in_sample/topic/category-all2024 "$CATEGORY_TOPIC_VECTORS" "$CATEGORY_DIMENSIONS" "$CATEGORY_TOPIC_NAMES" 0
register_job "holdout category all2024" run_topic_holdout results/compirt/holdout/topic/category-all2024 "$CATEGORY_TOPIC_VECTORS" "$CATEGORY_DIMENSIONS" "$CATEGORY_TOPIC_NAMES" 0 "$CATEGORY_PYRAMIDAL_DEVICE"
register_job "in-sample category all2024 cal" run_topic_insample results/compirt/in_sample/topic/category-all2024-cal "$CATEGORY_TOPIC_VECTORS" "$CATEGORY_DIMENSIONS" "$CATEGORY_TOPIC_NAMES" 1
register_job "holdout category all2024 cal" run_topic_holdout results/compirt/holdout/topic/category-all2024-cal "$CATEGORY_TOPIC_VECTORS" "$CATEGORY_DIMENSIONS" "$CATEGORY_TOPIC_NAMES" 1 "$CATEGORY_PYRAMIDAL_DEVICE"
register_job "in-sample learned-topic all2024" run_learned_insample results/compirt/in_sample/topic/learned-topic-all2024 0
register_job "holdout learned-topic all2024" run_learned_holdout results/compirt/holdout/topic/learned-topic-all2024 0
register_job "in-sample learned-topic all2024 cal" run_learned_insample results/compirt/in_sample/topic/learned-topic-all2024-cal 1
register_job "holdout learned-topic all2024 cal" run_learned_holdout results/compirt/holdout/topic/learned-topic-all2024-cal 1
register_job "in-sample multidim all2024" run_multidim_insample results/compirt/in_sample/multidim/multidim-all2024 0
register_job "holdout multidim all2024" run_multidim_holdout results/compirt/holdout/multidim/multidim-all2024 0
register_job "in-sample multidim all2024 cal" run_multidim_insample results/compirt/in_sample/multidim/multidim-all2024-cal 1
register_job "holdout multidim all2024 cal" run_multidim_holdout results/compirt/holdout/multidim/multidim-all2024-cal 1

run_job_matrix() {
  local index
  for index in "${!RETRAIN_JOB_LABELS[@]}"; do
    local -n command_ref="${RETRAIN_JOB_COMMAND_NAMES[$index]}"
    run_job "${RETRAIN_JOB_LABELS[$index]}" "${command_ref[@]}"
  done
}

main() {
  echo "# Retrain Existing CompIRT Results"
  echo "Started: $(date -Is)"
  echo "Repo: $REPO_ROOT"
  echo "Overwrite policy: reuse existing result roots; do not delete roots first."
  echo "DRY_RUN: $DRY_RUN"
  echo "CONTINUE_ON_ERROR: $CONTINUE_ON_ERROR"
  echo "Python: $PYTHON"
  echo "GPU: $GPU"
  echo "Device: $DEVICE"
  echo "Splits: in-sample=$SPLIT train=$TRAIN_SPLIT test=$TEST_SPLIT"
  echo "Tournament: ${TOURNAMENT:-<all>}"
  echo "Synergy details: forced on"

  run_job_matrix

  echo
  echo "Finished: $(date -Is)"
  if [[ "${#FAILED_JOBS[@]}" -gt 0 ]]; then
    echo "Failed jobs:"
    printf '  - %s\n' "${FAILED_JOBS[@]}"
    exit 1
  fi
}

main "$@"
