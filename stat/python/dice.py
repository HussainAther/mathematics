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
    if len(a) == 1:  a=a+u"."
    if len(b) == 1:  b=b+u"."
    a_bigram_list=[]
    for i in range(len(a)-1):
      a_bigram_list.append(a[i:i+2])
    b_bigram_list=[]
    for i in range(len(b)-1):
      b_bigram_list.append(b[i:i+2])
      
    a_bigrams = set(a_bigram_list)
    b_bigrams = set(b_bigram_list)
    overlap = len(a_bigrams & b_bigrams)
    dice_coeff = overlap * 2.0/(len(a_bigrams) + len(b_bigrams))
    return dice_coeff
