"""
Linear combinations. 
"""
def memoize(f):
    """
    Memoize previous results.
    """
    results = {}
    def helper(n):
        if n not in results:
            results[n] = f(n)
        return results[n]
    return helper

def factors_set():
    """
    Find the set of factors satisfying the linear combination.
    """
    factors_set = ( (i,j,k,l) for i in [-1,0,1] 
                          for j in [-1,0,1]
                          for k in [-1,0,1]
                          for l in [-1,0,1])
    for factor in factors_set:
        yield factor

@memoize
def linearcomb(n):
    """
    Return a tuple (i, j, k, l) satisfying the 
    linear combination n = i*1 + j*3 + k*9 + l*27
    """
    weighs = (1, 3, 9, 27)
    for factors in factors_set()
