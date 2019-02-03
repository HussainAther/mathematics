import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO

"""
Solving non-linear equations
"""

m = GEKKO()             # create GEKKO model
x = m.Var(value=0)      # define new variable, initial value=0
y = m.Var(value=1)      # define new variable, initial value=1
m.Equations([x + 2*y==0, x**2+y**2==1]) # equations
m.solve(disp=False)     # solve
print([x.value[0],y.value[0]]) # print solution
