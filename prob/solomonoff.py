"""
The algorithmic Solomonoff (solomonoff) probability addresses the philosphical probelm of induction formally.
It's based upon Occam's razor, Epicurus' principle of multiple explanations, Bayes' Rule, Universal Turing
machines, and algorithmic complexity. We use Occam's razor with respect to Epicurus' principle of indifference 
to give a high or low a priori plausibility to simple or complex strings x, respectively. We use a complexity
score K to show the a prior probability of x is 2^(-K(x)) by the Kraft-McMillan (Kraft McMillan kraft mcmillan) 
inequality:

For each source symbol of the alphabet (S = {s1, s2,...sn}) encoding into a uniquely decodable code over an 
alphabet of size r with codeword lengths (l1, l2,...ln).

The sum of r^(-li) for all i=1,...n <= 1. 
"""

def M(x):
    """
    Measure of probability M concentrated on the set of all binary sequences in list x. 
    """
    summ = 0
    for i in x:
         summ += 2**(-len(i))
    return summ
