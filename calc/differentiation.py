
"""
Differentiation as one of the primary methods of calculus for error analysis,
approximation, and many other mathematical and statistical techniques.
"""

# forward differentiation
def fd(y, t, h): # function f at point t at interval h
    return( y(t+h) - y(t)) /h

# central differentiation
def cd(y, t, h):
    return ( y(t+h/2) -y(t-h/2))/h

# extrapolation
def ed(y, t, h):
    return (8*(y(t+h/4)-y(t-h/4)) - (y(t+h/2)-y(t-h/2)))/3/h
