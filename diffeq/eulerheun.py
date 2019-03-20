import numpy as np

"""
We use the second-order Euler-Heun method to approximate an integral through which we can
use in integrating an ordinary differential equation.

x(t_n+1) = x(t_n) + integral from t_n to t_n+1 of f(x(s), s)ds

such that x(t) is an exact solution of ẋ = f(x, t).

We use a trapezoild approximation (in contrast to Euler's method of using a Riemann sum).
It's a second-order (2nd) Runge-Kutta method. 
In this example, we look at a one-dimensional oscillating model.
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
