import itertools as it
import sys
import os

"""
Satisfiability problems check whether solutions exist satisfying an interpretation of
a given Boolean formula. They have practical applications in planning and scheduling, hard and software verification,
and drug design and genetics.
"""

def circuitSAT(C):
    """
    Circuit satisfiability takes an electrical Boolean circuit with a large number of inputs nad one output.
    Returns the possiblity of there being an output 1. "Yes" if C circuit is satsifiable. "No" otherwise.
    """
