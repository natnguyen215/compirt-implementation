"""Multidimensional CompIRT experiments and shared helpers.

Groups the multidimensional-difficulty CompIRT variants that share the same
per-dimension pyramidal math:

* 'multidim_mirt': the base variant with a freely learned tossup relevance
  'r ~ Gamma(2, 2)' per latent dimension.
* 'embedding_mirt': the content-aware sibling whose 'r' is instead projected
  from a frozen text embedding.

Both name the weight vector 'r', not the baseline's 'alpha': per-dimension
difficulty puts the weight outside the skill gap, which is the CAIMIRA relevance
role rather than the paper's scalar-difficulty discrimination.

Output helpers shared with the other CompIRT variants live in 'utils.saving'.
"""
