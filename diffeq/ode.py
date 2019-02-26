"""
How can we verify that the programming of an ODE model is correct? The best method is to find a problem where
there are no unknown numerical approximation errors, because we can then compare the exact solution of the
problem with the result produced by our implementation and expect the difference to be within a very small tolerance.

We shall base a unit test on this idea and implement a corresponding test function (see the section Constructing unit
tests and writing test functions) for automatic verification of our implementation.
"""

def test_ode_FE():
    """Test that a linear u(t)=a*t+b is exactly reproduced."""

    def exact_solution(t):
        return a*t + b

    def f(u, t):  # ODE
        return a + (u - exact_solution(t))**m

    a = 4
    b = -1
    m = 6

    dt = 0.5
    T = 20.0

    u, t = ode_FE(f, exact_solution(0), dt, T)
    diff = abs(exact_solution(t) - u).max()
    tol = 1E-15           # Tolerance for float comparison
    success = diff < tol
    assert success
