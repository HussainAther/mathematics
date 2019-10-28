"""
Differentiation as one of the primary methods of calculus for error analysis,
approximation, and many other mathematical and statistical techniques.

Not sure if this will be useful for anything but at the very least it's 
documented.
"""

# forward differentiation
def fd(y, t, h): # function f at point t at interval h
    return( y(t+h) - y(t)) /h

# central differentiation
def cd(y, t, h):
    """
    Differentiate around both sides of a point t of interval h.
    """
    return (y(t+h/2) - y(t-h/2))/h

# extrapolation
def ed(y, t, h):
    """
    Extrapolate by splitting the derivative equation into four parts
    that we sum toghether.
    """
    return (8*(y(t+h/4)-y(t-h/4)) - (y(t+h/2)-y(t-h/2)))/3/h
