"""Multidimensional CompIRT experiments.

* 'multidim_mirt': the per-dimension difficulty variant with a freely learned
  tossup relevance 'r ~ Gamma(2, 2)' per latent dimension.

It names the weight vector 'r' because per-dimension difficulty puts the weight
outside the skill gap. The embedding-relevance sibling was archived under
'archive/multidimensional/embedding_mirt'.

Output helpers shared with the other CompIRT variants live in 'utils.saving'.
"""
