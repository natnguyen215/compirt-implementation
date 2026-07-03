"""Held-out (temporal) evaluation helpers for CompIRT.

These utilities build the informative player priors the paper prescribes for the
2024->2025 temporal split (Section 4.2, Appendix B): returning players keep their
training posterior as a prior, while new players draw a tier-conditioned
population prior estimated from training-set players in the same difficulty tier.
"""
