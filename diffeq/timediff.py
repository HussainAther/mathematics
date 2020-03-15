import matplotlib.pyplot as plt
import numpy as np

from gekko import GEKKO

"""
Simple GEKKO usage with an equation differentiated by time.
"""

m = GEKKO() # Create GEKKO model.
k = 0.3 # constant
y = m.Var(5.0) # Create GEKKO variable.
m.Equation(y.dt()==-k*y) # Create GEKKO equation.
m.time = np.linspace(0, 20) # time points

# Solve ODE.
m.options.IMODE = 4
m.solve()

# Plot results.
plt.plot(m.time, y)
plt.xlabel("time")
plt.ylabel("y(t)")
plt.show()
