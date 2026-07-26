"""Command-matrix combinators for the 2024 Nationals batch runner.

Family-specific command builders remain beside the public CLI because their
arguments encode model-specific contracts. This module owns the cross-product
of selected model families and calibration settings so matrix construction is
independently testable without importing execution or report code.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import TypeVar


ModelSpecT = TypeVar("ModelSpecT")
ModelRunT = TypeVar("ModelRunT")


def calibration_values(selection: str) -> tuple[bool, ...]:
    """Translate the public calibration option into stable matrix order."""
    if selection == "both":
        return (False, True)
    if selection == "cal":
        return (True,)
    return (False,)


def build_run_matrix(
    specs: Iterable[ModelSpecT],
    calibrations: Iterable[bool],
    build_run: Callable[[ModelSpecT, bool], ModelRunT],
) -> list[ModelRunT]:
    """Build model-major, calibration-minor runs in their public order."""
    return [
        build_run(spec, calibrate)
        for spec in specs
        for calibrate in calibrations
    ]
