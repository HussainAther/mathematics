import numpy as np

"""
Lyapunov's "second method" or "direct method" for ordinary differential
equations of the form:

dx/dt = ẋ = f(x)

in which the first equals sign denotes the definition of dx/dt. Suppose
the equation above has an isolated fixed point at x = 0. If there's a differential function V(x)
that is positive definite and for which dV/dt = ∇V · f is negative definite on some domain D ∋ 0,
then 0 is asymptotically stable. if dV/dt is negative semidefinite (e.g., dV/dt = 0 is allowed),
then 0 is Lypunov stable.
"""

def lyapunov(V, x):
    """
    Return Lyapunov stability for some function V and some list of numbers x.
    You must also know dotV(x) = dV/dt = summation of i=1 to n of the partial differential 
    of V with respect to x_i times f_i(x) <= 0 for all values of x != 0.
    """
    if V(0) == 0:
        for i in x:
            if V(x) != 0 and x != 0:
                pass
            else:
                return False
            if V(x) > 0:
                if x != 0:
                    pass
                else:
                    return False
    return True
           
 
