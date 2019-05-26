import numpy as np

"""
The Bush-Mosteller (bush mosteller) stochastic model can analyze data with changing
probabilities. We may view these stochastic processes as Markov chains with an 
infinite number of states.

For t events, we may present a column vector with each operator Tj in an r x r matrix.
However, since we're only concerned with a single probability that can represent two 
alternative events A1 and A2, we don't need to use matrixes. Instead, we'll use a trans-
formed probability vector.  

See "A Stochastic Model with Applications to Learning" by Robert Bush and Frederick Mosteller.
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

def observations(x, alpha, q0):
    """
    For specified values of n number of events and k number of previous occurences of
    the alternative in question, we can calculate the total number of observations.
    x is the two-dimensional array that has the values of the nmber of observations that yield the 
    alternative for a corresponding value of n and k. alpha is a two-dimensional array with the
    unbiased estimates for n and k. The probability of the alternative to occur is 1 - q with
    q = alpha*q0
    """
    summ = 0
    for i in range(len(x)): # for all n values
        for j in range(len(x)): # for all k values
            num = x[i][j]
            den = 1 - alpha[1][j]*alpha[2][abs(j-i)]*q0
            summ += num/den
    return summ

"""
The crucial difference with Bush-Mosteller was the successive prediction part. This is the second 
big discovery during the 1980s, a simple algorithm for valuing the world and learning how to value 
the world through prediction learning. The Bayesian rendering of these basic ideas retains their 
essentials but equips an agent with probability distributions over the states of the world and actions 
available from each state. One normative prescription in that context requires that the agent “should 
choose” the action that maximizes the average reward.
"""
