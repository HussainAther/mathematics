import numpy as np

"""
We use the second-order Euler-Heun method to approximate an integral through which we can
use in integrating an ordinary differential equation.

x(t_n+1) = x(t_n) + integral from t_n to t_n+1 of f(x(s), s)ds

such that x(t) is an exact solution of ẋ = f(x, t).

We use a trapezoild approximation (in contrast to Euler's method of using a Riemann sum).
"""
a = np.zeros

# Step forward
for n in range(Nt):
    a[n+1] = a[n] + dt*b[n]
