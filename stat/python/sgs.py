import numpy as np

from sklearn.tree import DecisionTreeClassifier
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

def prune_index(inner_tree, decisions, index=0):
    # Start pruning from the bottom - if we start from the top, we might miss
    # nodes that become leaves during pruning.
    # Do not use this directly - use prune_duplicate_leaves instead.
    if not is_leaf(inner_tree, inner_tree.children_left[index]):
        prune_index(inner_tree, decisions, inner_tree.children_left[index])
    if not is_leaf(inner_tree, inner_tree.children_right[index]):
        prune_index(inner_tree, decisions, inner_tree.children_right[index])
    # Prune children if both children are leaves now and make the same decision:     
    if (is_leaf(inner_tree, inner_tree.children_left[index]) and
        is_leaf(inner_tree, inner_tree.children_right[index]) and
        (decisions[index] == decisions[inner_tree.children_left[index]]) and 
        (decisions[index] == decisions[inner_tree.children_right[index]])):
        # turn node into a leaf by "unlinking" its children
        inner_tree.children_left[index] = TREE_LEAF
        inner_tree.children_right[index] = TREE_LEAF
        ##print("Pruned {}".format(index))

def prune(G, v):
    """
    Prune a graph G with variables v.
    """
     

def sgs(v):
    """
    For a set of variables v, perform the SGS algorithm 
    for discovering causal structure.
    """
    g = colliders(prune_index(DecisionTreeClassifier(len(v)))) # construct the graph
	gp  
