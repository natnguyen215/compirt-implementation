"""Run-log helpers for CompIRT experiment orchestrators."""

from __future__ import annotations

import atexit
import codecs
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Mapping


_ACTIVE_LOG_HANDLES = []

_RESULT_MARKER = "results/compirt/"
_RESULT_TIERS = ("in_sample", "holdout")


def resolve_result_root(candidate, tier: str) -> str:
    """Keep experiment outputs under ``results/compirt/{in_sample,holdout}/``.

    Run roots are supplied by hand through the ``ROOT`` env var, and dropping the
    ``in_sample/``/``holdout/`` segment used to scatter full runs directly under
    ``results/compirt/``. This normalizes them:

    * a root already under a tier is returned unchanged;
    * a bare ``results/compirt/<name>`` is redirected into ``<tier>/<name>`` with
      a warning;
    * a path that is not under ``results/compirt/`` (tests, custom dirs) is left
      untouched.

    Keys on the ``results/compirt/`` marker so it works for both repo-relative
    and absolute paths, and is idempotent (safe to apply more than once).
    """
    if tier not in _RESULT_TIERS:
        raise ValueError(f"tier must be one of {_RESULT_TIERS}, got {tier!r}")
    text = str(candidate).rstrip("/")
    index = text.find(_RESULT_MARKER)
    if index == -1:
        return text
    prefix = text[:index]
    rest = text[index + len(_RESULT_MARKER) :]
    if not rest:
        return text
    if rest.split("/", 1)[0] in _RESULT_TIERS:
        return text
    fixed = f"{prefix}{_RESULT_MARKER}{tier}/{rest}"
    print(
        f"note: run ROOT {text!r} is missing the {tier!r} tier; "
        f"redirecting outputs to {fixed!r}",
        file=sys.stderr,
    )
    return fixed


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
        bufsize=0,
    )
    assert process.stdout is not None
    # Read raw bytes rather than iterating "lines": text-mode iteration applies
    # universal-newline translation, which treats a bare '\r' (how tqdm redraws
    # a progress bar in place) as a line terminator. That turns every tqdm
    # refresh into its own logged line instead of one line that updates in
    # place, so read a fixed chunk size and decode incrementally (chunk
    # boundaries can split a multi-byte UTF-8 character), writing through
    # 'sys.stdout.write' -- not '.buffer.write' -- so a 'TeeStream' installed by
    # 'tee_run_output' still mirrors the bytes to the log file.
    decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
    while True:
        chunk = process.stdout.read(4096)
        if not chunk:
            break
        sys.stdout.write(decoder.decode(chunk))
        sys.stdout.flush()
    sys.stdout.write(decoder.decode(b"", final=True))
    return_code = process.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, printable)
