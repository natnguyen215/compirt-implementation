#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

LOG_DIR="${LOG_DIR:-logs}"
mkdir -p "$LOG_DIR"

timestamp="$(date +%Y%m%d_%H%M%S)"
log_file="$LOG_DIR/multidim_everything_$timestamp.log"
pid_file="$LOG_DIR/multidim_everything_$timestamp.pid"
latest_log="$LOG_DIR/multidim_everything_latest.log"
latest_pid="$LOG_DIR/multidim_everything_latest.pid"

nohup ./run_scripts/run_multidim_everything.sh >"$log_file" 2>&1 &
pid="$!"

printf "%s\n" "$pid" >"$pid_file"
ln -sfn "$(basename "$log_file")" "$latest_log"
ln -sfn "$(basename "$pid_file")" "$latest_pid"

echo "Started multidim rerun with PID $pid"
echo "Log: $log_file"
echo "PID file: $pid_file"
echo
echo "Watch it with:"
echo "  tail -f $latest_log"
echo
echo "Check whether it is still running with:"
echo "  ps -p $pid"
