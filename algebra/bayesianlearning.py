
"""
Sequential Sparse Bayesian Learning Algorithm
If solving a regression problem, initialize beta using a basis function phi1 with hyperparameter
alpha1 set using

alphai = si^2 / (qi^2 - si)

and evaluate summation and m along with qi and si for all basis functions. Then we select a candidate
basis function phi. If qi^2 > si and alphai < infinity such that the basis vector phi is already included
in the model, update alphai using its equation. If qi^2 > si and alpha = infinity
"""

