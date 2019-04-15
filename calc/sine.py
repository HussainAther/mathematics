import math

"""
Calcluate sin(x) as a finite sum.
"""

def sine(x, N):
    """
    Discrete method of calculating the sine function.
    Helpful for certain Fourier transforms of noisy data.
    """
    result = 0
    for i in range(1, N+1):
        num = ((-1)**i-1) * (x**(2*i-1)) # numerator
        den = math.factorial(2*i-1) # denominator
        result += num/den
    return result
