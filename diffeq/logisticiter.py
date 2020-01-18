"""
Iterate through a logistic map.
"""

def iterate(x0, r, iter):
    for i in range(iter):
        prod = r*x0*(1-x0)
        x0 = prod
    return prod

print(iterate(.2, 2.6, 10))
