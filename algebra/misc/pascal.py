import scipy as sp

"""
Pascal's (Pascal pascal) triangle through iteration.
Faster, more effective methods may be employed through dynamic programming.
"""

def pascal(col, row):
    """
    Recursion to create series for an input row and column of the triangle.
    """
    if col == row or col == 0:
      return 1
    else: # iterate through the factorial's rows and columns
      return sp.misc.factorial(row)//(sp.misc.factorial(col)*sp.misc.factorial(row-col))

def tri(n):
    """
    Create the triangle for each row up to a number n.
    """
    for i in range(n):
        for j in range(i+1):
           print(pascal(j, i)))
        print("\n") 

