"""Validation-selected point fits for conditional first-buzz correctness.

This package was moved from ``analysis/tossup_accuracy_study`` to
``analysis/correctness/tossup_accuracy_study`` when the three correctness
studies were grouped. The saved fold predictors under
``results/compirt/holdout/common/tossup-accuracy-study/`` were pickled before
that move, so they name the old module path. Registering the aliases here — at
package import, ahead of any ``joblib.load`` by a caller that imports this
package — keeps those artifacts loadable without refitting them.

Remove the aliases only if the saved predictors are regenerated.
"""

import sys

_LEGACY_PACKAGE = "analysis.tossup_accuracy_study"
_LEGACY_SUBMODULES = ("models", "predictor", "run")


def _install_legacy_aliases() -> None:
    if _LEGACY_PACKAGE in sys.modules:
        return
    sys.modules[_LEGACY_PACKAGE] = sys.modules[__name__]
    for name in _LEGACY_SUBMODULES:
        try:
            module = __import__(f"{__name__}.{name}", fromlist=[name])
        except ImportError:
            continue
        sys.modules[f"{_LEGACY_PACKAGE}.{name}"] = module


_install_legacy_aliases()
