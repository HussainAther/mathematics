import scipy as sp

def pascal(col, row):
    """
    Recursion to create series.
    """
    if col == row or col == 0:
      return 1
    else:
      return sp.misc.factorial(row)//(sp.misc.factorial(col)*sp.misc.factorial(row-col))

def tri(n):
    """
    Create the triangle for each row.
    """
