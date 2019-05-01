import numpy as np

"""
We use the second-order Euler-Heun (euler Euler Heun heun) method to approximate an integral 
through which we can use in integrating an ordinary differential equation.

x(t_n+1) = x(t_n) + integral from t_n to t_n+1 of f(x(s), s)ds

such that x(t) is an exact solution of ẋ = f(x, t).

We use a trapezoid approximation (in contrast to Euler's method of using a Riemann sum).
It's a second-order (2nd) Runge-Kutta method. 
"""

def feval(funcName, *args):
    """
    Evaluate a function with its corresponding arguments. 
    """
    return eval(funcName)(*args)

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
    # solutions we return at the end
    xreturn = np.empty(0)
    xreturn = np.append(xreturn, x)
    yreturn = np.empty(0)
    yreturn = np.append(yreturn, y) # I think this is faster than Python's built-in list append
    # evaluate using our method
    for i in range(n):
         y0prime = feval(f, x, y) # y0', the differental at our starting position
         k1 = y0prime * h # evaluate the step using the differential
         ypred = y + k1 # prediction
         y1prime = feval(f, x+h, ypred) # evaluate based on that prediction
         for j in range(m): # continue to evaluate in accordance with our method
             y[j] = y[j] + (h/2)*y0prime[j] + (h/2)*y1prime[j] 
         x += h # steparoo 
         xreturn = np.append(xreturn, x) # using numpy's method to append again
         for r in range(len(y)):
             yreturn = np.append(yreturn, y[r]) 
    return [xreturn, yreturn]

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
