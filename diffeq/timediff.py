import numpy as np
import matplotlib.pyplot as plt

from gekko import GEKKO

"""
Simple GEKKO usage with an equation differentiated by time.
"""

m = GEKKO() # create GEKKO model
k = 0.3 # constant
y = m.Var(5.0) # create GEKKO variable
m.Equation(y.dt()==-k*y) # create GEKKO equation
m.time = np.linspace(0, 20) # time points

# solve ODE
m.options.IMODE = 4
m.solve()

# plot results
plt.plot(m.time, y)
plt.xlabel("time")
plt.ylabel("y(t)")
plt.show()
