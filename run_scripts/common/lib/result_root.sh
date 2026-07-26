#!/usr/bin/env bash
# Shared guard that keeps CompIRT run outputs under
# results/compirt/{in_sample,holdout}/. Source this and pass every run root
# through resolve_result_root before creating directories or spawning trainers.
#
#   source "$REPO_ROOT/run_scripts/common/lib/result_root.sh"
#   OUTPUT_ROOT="$(resolve_result_root "${ROOT:-results/compirt/in_sample/foo}" in_sample)"
#
# Behavior (idempotent, safe to apply more than once):
#   * already under results/compirt/{in_sample,holdout}/  -> returned unchanged
#   * bare results/compirt/<name> (missing the tier)      -> results/compirt/<tier>/<name> (+ warning)
#   * any path not under results/compirt/                  -> returned unchanged (tests / custom dirs)
resolve_result_root() {
  local candidate="${1%/}"
  local tier="$2"
  case "$tier" in
    in_sample | holdout) ;;
    *)
      printf 'resolve_result_root: tier must be in_sample|holdout, got %s\n' "$tier" >&2
      return 2
      ;;
  esac

  # Leave paths that are not CompIRT results untouched.
  case "$candidate" in
    *results/compirt/*) ;;
    *)
      printf '%s\n' "$candidate"
      return 0
      ;;
  esac

  local prefix="${candidate%%results/compirt/*}"
  local rest="${candidate#*results/compirt/}"
  if [[ -z "$rest" ]]; then
    printf '%s\n' "$candidate"
    return 0
  fi

  local first="${rest%%/*}"
  if [[ "$first" == "in_sample" || "$first" == "holdout" ]]; then
    printf '%s\n' "$candidate"
    return 0
  fi

  local fixed="${prefix}results/compirt/${tier}/${rest}"
  printf 'note: run ROOT %s is missing the %s/ tier; redirecting outputs to %s\n' \
    "$candidate" "$tier" "$fixed" >&2
  printf '%s\n' "$fixed"
}
