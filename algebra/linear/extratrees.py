import numpy as np

"""
Extra-trees (extra trees extratrees) splitting algorithm (extremely randomized trees).
"""

def nodesplit(s):
    """
    For local learning subset s corresponding to the node to split,
    return a split [a<a_c] if there is one. Otherwise, return False. 
    """
