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
    u = len(set(s)) # Unique elements in s
    K = np.random.choice(range(1, u)) # Choose a non-zero random number K from the number of unique
                                      # elements in s.
    sp = [] # splits
    for i in range(K):
        at = np.random.choice(range(1, u)) # attribute
        sp.append(randomsplit(at))
    maxscore = 0
    maxsplit = "" 
    if score(p) > maxscore:
        maxscore = score(p)
        maxsplit = p
    return p, maxscore

def randomsplit(a):
    """
    For attribute y, return a split. 
    """
    asmax = 0 # max and min of the target values of the attribute
    asmin = 0
    for i in y:
        if targetvariable(i) > asmax:
            asmax = targetvariable(i)
        if targetvariable(i) < asmin:
            asmin = targetvariable(i)
    ac = np.random.choice(range(asmin, asmax)) # random cut-point
    return range(a, ac) # Return the split.

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
    if all(i == targetvariable(i) for i in s): # If all target variables are the same.
        return True
    if all(a == a for a in s): # If all attributes are the same.
        return True 
    return False

def score(p):
    """
    For some split p, return a score.
    """ 
    return p
