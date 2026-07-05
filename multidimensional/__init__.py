"""Multidimensional CompIRT experiments and shared helpers.

Groups the multidimensional-difficulty CompIRT variants that share the same
per-dimension pyramidal math:

* 'multidim_mirt': the base variant with a freely learned tossup discrimination
  'alpha ~ Gamma(2, 2)' per latent dimension.
* 'embedding_mirt': the content-aware sibling that replaces 'alpha' with a
  relevance vector 'r' projected from a frozen text embedding.

Output helpers shared with the other CompIRT variants live in 'utils.saving'.
"""
