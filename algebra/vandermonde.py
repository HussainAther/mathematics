from vpython import *
import math

"""
Interpolation using the Vandermode function.

The Vandermonde matrix is an n × n matrix where the first row is the first point evaluated at
each of the n monomials, the second row is the second point x2 evaluated at each of the n monomials,
and so on. These are the terms of the geometric progression for each row.

The easiest way to create this matrix is to write the functions above the matrix and the points
to the left of the matrix as is shown below. Then evaluate the functions at the corresponding points.
"""

def vandermonde(order, dim=1, syms='a b c d'):
    """Computes a Vandermonde matrix of given order and dimension.
    Define syms to give beginning strings for temporary variables.
    Returns the Matrix, the temporary variables, and the terms for the
    polynomials.
    """
    syms = syms.split()
    n = len(syms)
    if n < dim:
        new_syms = []
        for i in range(dim - n):
            j, rem = divmod(i, n)
            new_syms.append(syms[rem] + str(j))
        syms.extend(new_syms)
    terms = []
    for i in range(order + 1):
        terms.extend(comb_w_rep(dim, i))
    rank = len(terms)
    V = zeros(rank)
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
