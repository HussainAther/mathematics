import numpy as np

from sklearn.tree._tree import TREE_LEAF

"""
Spirtes-Glymour-Scheines algorithm (SGS)
"""

def sgs(v):
    """
    For a set of variables v, perform the SGS algorithm 
    for discovering causal structure.
    """
    g = colliders(
