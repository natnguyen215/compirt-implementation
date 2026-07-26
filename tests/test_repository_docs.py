"""Repository-level checks for the public Markdown reading path."""

from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
INLINE_MARKDOWN_LINK = re.compile(
    r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)"
)
REFERENCE_MARKDOWN_LINK = re.compile(
    r"^ {0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)", re.MULTILINE
)
PRIVATE_CONTEXT_NAMES = ("CLAUDE.md", "CONTEXT.md", "NATHAN_READ.md")


def public_markdown_files() -> list[Path]:
    """Return documentation intended to work in a clean public clone."""
    files = {
        ROOT / "README.md",
        ROOT / "data" / "README.md",
        ROOT / "results" / "README.md",
        ROOT / "simple_mirt" / "README.md",
        ROOT / "tests" / "README.md",
        ROOT / "compirt_eval" / "METRICS.md",
        ROOT / "compirt_eval" / "README.md",
        ROOT / "compirt_eval" / "EVALUATION_TLDR.md",
        ROOT / "compirt_eval" / "SCENARIO_C.md",
        ROOT / "compirt_eval" / "drop_robustness" / "README.md",
        ROOT / "compirt_eval" / "imaginary_tournament" / "README.md",
        ROOT / "compirt_eval" / "noise_floor" / "README.md",
        ROOT / "compirt_eval" / "parameter_recovery" / "README.md",
        ROOT / "compirt_eval" / "player_rankings" / "README.md",
        ROOT / "compirt_eval" / "synergy_comparison" / "README.md",
    }
    for directory in ("docs", "tfidf", "topic", "multidimensional"):
        files.update(
            path
            for path in (ROOT / directory).rglob("*.md")
            if path.name != "CLAUDE.md"
            and not path.name.startswith(".")
            and "hf_cache" not in path.parts
        )
    return sorted(path for path in files if path.exists())


def local_link_target(source: Path, raw_target: str) -> Path | None:
    """Resolve a Markdown link target, or return None for non-file links."""
    target = raw_target.strip().strip("<>")
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    path_text = unquote(target.split("#", 1)[0])
    if not path_text:
        return None
    return (source.parent / path_text).resolve()


def markdown_link_targets(text: str) -> list[str]:
    """Return inline and reference-style Markdown link destinations."""
    return INLINE_MARKDOWN_LINK.findall(text) + REFERENCE_MARKDOWN_LINK.findall(text)


class PublicDocumentationTests(unittest.TestCase):
    def test_standalone_studies_use_the_runner_convention(self) -> None:
        runners = [
            ROOT / "run_scripts" / "common" / "run_imaginary_tournament.py",
            ROOT / "run_scripts" / "common" / "run_player_rankings.py",
            ROOT / "run_scripts" / "common" / "run_synergy_comparison.py",
            ROOT
            / "run_scripts"
            / "multidimensional"
            / "multidim"
            / "run_multidim_noise_floor.py",
            ROOT
            / "run_scripts"
            / "multidimensional"
            / "multidim"
            / "run_parameter_recovery.py",
        ]
        self.assertTrue(all(path.exists() for path in runners))
        self.assertEqual([], list((ROOT / "compirt_eval" / "cli").glob("*.py")))
        self.assertEqual([], list((ROOT / "compirt_eval").rglob("__main__.py")))
        parser_modules = [
            path.relative_to(ROOT)
            for path in (ROOT / "compirt_eval").rglob("*.py")
            if "ArgumentParser" in path.read_text(encoding="utf-8")
        ]
        self.assertEqual([], parser_modules)

        stale_commands = (
            "compirt_eval.cli.",
            "python -m compirt_eval.parameter_recovery",
            "python -m compirt_eval.imaginary_tournament",
        )
        stale_references = []
        for source in public_markdown_files():
            text = source.read_text(encoding="utf-8")
            for command in stale_commands:
                if command in text:
                    stale_references.append(
                        f"{source.relative_to(ROOT)} -> {command}"
                    )
        self.assertEqual([], stale_references)

    def test_relative_markdown_links_resolve(self) -> None:
        missing: list[str] = []
        for source in public_markdown_files():
            text = source.read_text(encoding="utf-8")
            for raw_target in markdown_link_targets(text):
                target = local_link_target(source, raw_target)
                if target is not None and not target.exists():
                    missing.append(
                        f"{source.relative_to(ROOT)} -> {raw_target}"
                    )
        self.assertEqual([], missing, "Broken public documentation links:\n" + "\n".join(missing))

    def test_public_docs_do_not_depend_on_private_context(self) -> None:
        references: list[str] = []
        for source in public_markdown_files():
            text = source.read_text(encoding="utf-8")
            for private_name in PRIVATE_CONTEXT_NAMES:
                if private_name in text:
                    references.append(f"{source.relative_to(ROOT)} -> {private_name}")
        self.assertEqual([], references, "Private-context references:\n" + "\n".join(references))

    def test_public_docs_are_not_gitignored(self) -> None:
        ignored: list[str] = []
        for source in public_markdown_files():
            result = subprocess.run(
                ["git", "check-ignore", "--quiet", str(source)],
                cwd=ROOT,
                check=False,
            )
            if result.returncode == 0:
                ignored.append(str(source.relative_to(ROOT)))
        self.assertEqual([], ignored, "Public documentation is ignored:\n" + "\n".join(ignored))


if __name__ == "__main__":
    unittest.main()
