"""Run-log helpers for CompIRT experiment orchestrators."""

from __future__ import annotations

import atexit
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Mapping


_ACTIVE_LOG_HANDLES = []


class TeeStream:
    """Write every message to the original stream and a log file."""

    def __init__(self, stream, log_handle):
        self.stream = stream
        self.log_handle = log_handle

    def write(self, message):
        self.stream.write(message)
        # The log handle is closed at process exit; guard against the
        # interpreter's final flush landing on an already-closed file.
        if not self.log_handle.closed:
            self.log_handle.write(message)
        return len(message)

    def flush(self):
        self.stream.flush()
        if not self.log_handle.closed:
            self.log_handle.flush()

    def isatty(self):
        return self.stream.isatty()

    def __getattr__(self, name):
        return getattr(self.stream, name)


def _format_value(value):
    """Render scalars and small containers consistently for logs."""
    if value is None or value == "":
        return "unknown"
    if isinstance(value, (list, tuple)):
        return ", ".join(_format_value(item) for item in value) or "unknown"
    if isinstance(value, dict):
        return json.dumps(value, sort_keys=True)
    return str(value)


def format_run_log_header(
    config: Mapping[str, object],
    *,
    placeholder: bool = False,
    summaries: Mapping[str, object] | None = None,
) -> str:
    """Return a standardized Markdown-ish run-log header."""
    title = "# CompIRT Run Log"
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    lines = [
        title,
        "",
        f"Generated: {timestamp}",
        f"Placeholder: {'yes' if placeholder else 'no'}",
    ]
    if placeholder:
        lines.extend(
            [
                "Captured stdout/stderr: unavailable",
                (
                    "Note: this log was reconstructed from saved result artifacts; "
                    "historical command output was not captured."
                ),
            ]
        )
    else:
        lines.append("Captured stdout/stderr: yes")

    lines.extend(["", "## Run Variables", ""])
    for key in sorted(config):
        value = _format_value(config[key])
        lines.append(f"- {key}: {value}")

    if summaries:
        lines.extend(["", "## Recovered Stage Summaries", ""])
        for name, summary in summaries.items():
            lines.append(f"### {name}")
            lines.append("")
            lines.append("```json")
            lines.append(json.dumps(summary, indent=2, sort_keys=True))
            lines.append("```")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def tee_run_output(log_path: Path, *, append: bool = False):
    """Duplicate stdout/stderr to ``log_path`` for the rest of the process."""
    log_path = Path(log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    handle = log_path.open("a" if append else "w", encoding="utf-8")
    _ACTIVE_LOG_HANDLES.append(handle)
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = TeeStream(sys.stdout, handle)
    sys.stderr = TeeStream(sys.stderr, handle)

    def _restore_and_close():
        # Restore the real streams before closing the log so the interpreter's
        # final flush at shutdown does not touch a closed file (which would make
        # Python exit 120 and look like a failed run).
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        if not handle.closed:
            handle.flush()
            handle.close()

    atexit.register(_restore_and_close)
    return handle


def run_logged(args: list[str], *, cwd: Path | None = None) -> None:
    """Run a child command while streaming combined stdout/stderr through Python."""
    printable = [str(arg) for arg in args]
    process = subprocess.Popen(
        printable,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )
    assert process.stdout is not None
    for line in process.stdout:
        sys.stdout.write(line)
        sys.stdout.flush()
    return_code = process.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, printable)
