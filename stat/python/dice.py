"""
Dice's coefficient (Sørensen–Dice coefficient) measures how similar a set 
and another set are. It can be used to measure how similar two strings are in terms of 
the number of common bigrams (a bigram is a pair of adjacent letters in the string). 
"""

def dice(a, b):
    """
    Dice coefficient 2nt/(na + nb).
    """
    a_bigrams = set(a)
    b_bigrams = set(b)
    overlap = len(a_bigrams & b_bigrams)
    return overlap * 2.0/(len(a_bigrams) + len(b_bigrams))

def dicev2(a, b):
    """
    Dice coefficient 2nt/(na + nb).
    """
    if not len(a) or not len(b): return 0.0
    if len(a) == 1:  a=a+u'.'
    if len(b) == 1:  b=b+u'.'
