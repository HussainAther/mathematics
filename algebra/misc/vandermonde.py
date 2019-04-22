import numpy as np

from sympy import Symbol

"""
Interpolation using the Vandermode function algorithm (vandermonde).

The Vandermonde matrix is an n × n matrix where the first row is the first point evaluated at
each of the n monomials, the second row is the second point x2 evaluated at each of the n monomials,
and so on. These are the terms of the geometric progression for each row.

The easiest way to create this matrix is to write the functions above the matrix and the points
to the left of the matrix as is shown below. Then evaluate the functions at the corresponding points.
"""

def symbol_gen(sym_str):
    """
    Symbol generator
    Generate sym_str_n where n is the number of times the generator
    has been called. Used for evaluating the symbolic objects as
    True, False, or None.
    """
    n = 0
    while True:
        yield Symbol("%s_%d" % (sym_str, n))
        n += 1

def comb_w_rep(n, k):
    """
    Combinations with repetition
    Return the list of k combinations with repetition from n objects.
    """
    if k == 0:
        return [[]]
    combs = [[i] for i in range(n)]
    for i in range(k - 1):
        curr = []
        for p in combs:
            for m in range(p[-1], n):
                curr.append(p + [m])
        combs = curr
    return combs

def vandermonde(order, dim=1, syms="a b c d"):
    """
    Compute a Vandermonde matrix of given order and dimension.
    Define syms to give beginning strings for temporary variables.
    Return the Matrix, the temporary variables, and the terms for the
    polynomials.
    """
    syms = syms.split() # extract the symbols
    n = len(syms) # get the length of them
    if n < dim: # make sure we have enough symbols
        new_syms = []
        for i in range(dim - n):
            j, rem = divmod(i, n)
            new_syms.append(syms[rem] + str(j))
        syms.extend(new_syms)
    terms = [] # create this so we can iterate over each term
    for i in range(order + 1):
        terms.extend(comb_w_rep(dim, i)) # use extend instead of append because we hve multiple combinations
    rank = len(terms)
    V = np.zeros(rank) # final Vandermonde matrix
    generators = [symbol_gen(syms[i]) for i in range(dim)]
    all_syms = []
    for i in range(rank):
        row_syms = [next(g) for g in generators]
        all_syms.append(row_syms)
        for j, term in enumerate(terms):
            v_entry = 1
            for k in term:
                v_entry *= row_syms[k]
            V[i*rank + j] = v_entry
    return V, all_syms, terms
