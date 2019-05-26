import numpy as np

"""
The Bush-Mosteller (bush mosteller) stochastic model can analyze data with changing
probabilities.
"""

def event(t):
    """
    For t events, we may present a column vector with each operator Tj in an r x r matrix.
    However, since we're only concerned with a single probability that can represent two 
    alternative events A1 and A2, we don't need to use matrixes. Instead, we'll use a trans-
    formed probability vector. 
    """
