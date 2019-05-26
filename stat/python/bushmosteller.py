import numpy as np

"""
The Bush-Mosteller (bush mosteller) stochastic model can analyze data with changing
probabilities.

For t events, we may present a column vector with each operator Tj in an r x r matrix.
However, since we're only concerned with a single probability that can represent two 
alternative events A1 and A2, we don't need to use matrixes. Instead, we'll use a trans-
formed probability vector.  
"""

# Event probabilities
a = np.linspace(0, 100, 10)

def Q(n):
    """
    Apply operator Q to our event probabilities n times. 
    """
     
