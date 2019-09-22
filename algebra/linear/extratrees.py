import numpy as np

"""
Extra-trees (extra trees extratrees) splitting algorithm (extremely randomized trees).
"""

def nodesplit(s):
    """
    For local learning subset s corresponding to the node to split,
    return a split [a<a_c] if there is one. Otherwise, return False. 
    """
    if stopsplit(s):
        return False
    K = np.random.choice(range(len(set(s))) # Choose a random number K from the number of unique
                                            # elements in s.

def targetvariable(a):
    """
    Return the target variable for the input.
    """
    return a

def stopsplit(s):
    """
    For subset s, return a boolean if the split should stop. 
    """
    if abs(s) < nmin: # reached the minimum
        return True
    if all(input == targetvariable(input) for input in s): # If all target variables are the same.
        return True
    if all(attribute == attribute for attribute in s): # If all attributes are the same.
        return True 
    return False 
