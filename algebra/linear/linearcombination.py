def factors_set():
    """
    Implemented method to calculate scalars. Otherwise just use numpy.
    """
    factors_set = ( (i,j,k,l) for i in [-1,0,1]
                          for j in [-1,0,1]
                          for k in [-1,0,1]
                          for l in [-1,0,1])
    for factor in factors_set:
        yield factor

def memoize(f):
    """
    Memoize calculation results of an input.
    """
    results = {}
    def helper(n):
        if n not in results:
            results[n] = f(n)
        return results[n]
    return helper

def linear_combination(n):
    """
    Returns the tuple (i,j,k,l) satisfying
        n = i*1 + j*3 + k*9 + l*27      
    """
    weighs = (1,3,9,27)
    
    for factors in factors_set():
       sum = 0
       for i in range(len(factors)):
          sum += factors[i] * weighs[i]
       if sum == n:
          return factors

# calculate the linear combinations of the first 10 positive integers:
for i in range(1,11):
    print(linear_combination(i))
