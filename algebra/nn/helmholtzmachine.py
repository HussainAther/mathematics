import numpy as np

"""
The Helmholtz machine was designed to accommodate hierarchical architectures that construct complex
multilayer representations. The model in- volves two interacting networks, one with parameters G
that is driven in the top-down direction to implement the generative model, and the other, with
parameters W , driven bottom-up to implement the recogni- tion model.

The parameters are determined by a modified EM algorithm that results in roughly symmetric updates for the two networks.
"""
