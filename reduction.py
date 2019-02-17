
"""
F reduces to G means, informally, that if you can olve G, you can solve F. Turing reduction can informally
be stated as F polyreduces to G means if oyu can solve G in polynomial time, you can solve F in polynomial time.

A decision problem F has a polynomial time mappign reduction to problem G if there exists a polytime program C that converts instances
of F into isntances of G such taht C maps positive instances of F to positive instances of G, and negative instances of F to negative
instances of G.
"""

def convertPartitionToPacking(inString):
    """
    Polyreduction
    """
    weights = [int(x) for x in inString.split()]
    if totalWeight % 2 == 1:
        # if the total weight is odd, no partition is possible,
        # so return any negative instance of Packing
        return "0;1;1"
    else:
        # use thresholds that are half the total weight
        targetWeight = str(int(totalWeight / 2))
        return instring+";"targetWeight+";"targetWeight
