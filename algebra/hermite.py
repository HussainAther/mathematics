"""

"""


def recursiveHermite(x,n):
    """
    Recursive functino to calculate hermite polynomials.
    """
    if n==0:
        return 1
    elif n==1:
        return 2*x
    else:
        return 2*x*recursiveHermite(x,n-1)-2*(n-1)*recursiveHermite(x,n-2)
