from numpy import zeros, linspace

"""
How can we verify that the programming of an ODE model is correct? The best method is to find a problem where
there are no unknown numerical approximation errors, because we can then compare the exact solution of the
problem with the result produced by our implementation and expect the difference to be within a very small tolerance.

We shall base a unit test on this idea and implement a corresponding test function (see the section Constructing unit
tests and writing test functions) for automatic verification of our implementation.
"""

def ode_FE(f, U_0, dt, T):
    """
    Verify our ODE model.
    """
    N_t = int(round(float(T)/dt))
    u = zeros(N_t+1)
    t = linspace(0, N_t*dt, len(u))
    u[0] = U_0
    for n in range(N_t):
        u[n+1] = u[n] + dt*f(u[n], t[n])
    return u, t

def test_ode_FE():
    """
    Test that a linear u(t)=a*t+b is exactly reproduced.
    """

    def exact_solution(t):
        """
        Gauge this as a measure of performance.
        """
        return a*t + b

    def f(u, t):  # ODE
        """
        Use the ODE to test.
        """
        return a + (u - exact_solution(t))**m

    a = 4
    b = -1
    m = 6

    dt = 0.5
    T = 20.0

    u, t = ode_FE(f, exact_solution(0), dt, T)
    diff = abs(exact_solution(t) - u).max()
    tol = 1E-15 # Tolerance for float comparison
    success = diff < tol
    assert success
