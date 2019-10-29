import numpy as np

from sklearn.tree._tree import TREE_LEAF

"""
Spirtes-Glymour-Scheines algorithm (SGS)
"""

def is_leaf(inner_tree, index):
    """
    Check whether node is leaf node.
    """
    return (inner_tree.children_left[index] == TREE_LEAF and 
            inner_tree.children_right[index] == TREE_LEAF)

def sgs(v):
    """
    For a set of variables v, perform the SGS algorithm 
    for discovering causal structure.
    """
    g = colliders(
