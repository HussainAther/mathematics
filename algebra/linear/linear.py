import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO

"""
Solving Linear equations
"""

m = GEKKO()            # create GEKKO model
x = m.Var()            # define new variable, default=0
y = m.Var()            # define new variable, default=0
m.Equations([3*x+2*y==1, x+2*y==0])  # equations
m.solve(disp=False)    # solve
print(x.value,y.value) # print solution
