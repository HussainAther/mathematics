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
    Apply operator Q to our event probabilities n times. We may use the Monte Carlo
    method of making approximate calculations using a random number table for making
    decisions about which operator Q1 or Q2 to apply to the probability.
    """
    lamd = [] # asymptotic values of the operator Q as n gets very large 
    for i in a:
        lamd.append(i /(1-i))
    Qout = []
    p = 2 # Number of alternatives 
    for l in range(len(lamd)):
        Qout.append(lamd[i] - (lamd[i] - p)*a[i]**n)
    return Qout

def moment(theta, pi, n):
    """
    A moment-generating function for theta. These moments are the specific values
    of the distribution for the events given their probabilities and values. theta
    is the parameter we use to define the function and quantify the distribution. pi are
    the list of probabilities that when an event occurs, it will be event E. n is the 
    number of events.
    """
    summ = 0
    for i in range(len(pi)):
        summ += pi[i]*np.exp(theta*a[i]) 
    return summ 
