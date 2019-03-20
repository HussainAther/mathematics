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

def lyapunov(V):
    """
    Return Lyapunov stability.
    """
