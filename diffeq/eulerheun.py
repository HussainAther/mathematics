import numpy as np

"""
We use the second-order Euler-Heun method to approximate an integral through which we can
use in integrating an ordinary differential equation.

x(t_n+1) = x(t_n) + integral from t_n to t_n+1 of f(x(s), s)ds

such that x(t) is an exact solution of ẋ = f(x, t).

We use a trapezoild approximation (in contrast to Euler's method of using a Riemann sum).
It's a second-order (2nd) Runge-Kutta method. 
"""

def heun(f, y0, x_vals, h):
    """
    Perform the Euler-Heun method for a function f in which y0 is the initial condition
    of the function at y = 0, x_vals is the range of x values we use, h is the 
    y-directional height of the step size we take as we proceed through the function. 
    """
    m = len(y0) # length for range
    n = int(x_vals[-1] - x_vals[0])/ h # size of range over x values
    x = x_vals[0] 
    y = y0
    xreturn = np.empty(0)
    xreturn = np.append(xreturn, x)
         





"""
An example a simple harmonic oscillator model we solve using
the Forward Euler method.
"""

omega = 4 # angular frequency
P = 2*np.pi*omega # calculate period
dt = P/50 # step size
T = 4*P # time interval
N = int(round(T/dt)) # number of steps
t = np.linspace(0, N*dt, N+1) # initialize time range

# Initialize arrays and initial condition
a = np.zeros(N) # this will be our first function
b = np.zeros(N) # this will be our second function
x0 = 2
a[0] = x0 # start at some 
b[0] = 0 

# Step forward
for n in range(N):
    a[n+1] = a[n] + dt*b[n] # step size in the forward direction
    b[n+1] = b[n] - (dt*omega**2)*b[n] # taken from the differential of our oscillator 
