import numpy as np

from gekko import GEKKO

"""
Partial differential equation example using GEKKO
"""

# Initialize model
m = GEKKO()

# Discretizations ( time and space )
m.time = np.linspace(0,1,100)
npx = 100
xpos = np.linspace(0,2*np.pi,npx)
dx = xpos[1]−xpos[0]

# Define Variables
c = m.Const(value = 10)
u = [m.Var(value = np.cos(xpos[i])) for i in range(npx)]
v = [m.Var(value = np.sin(2*xpos[i])) for i in range(npx)]

m.Equations([u[i].dt()==v[i] for i in range(npx) ])

# Manual discretization in space ( central difference )
m.Equation(v[0].dt()==c**2 * (u[1] − 2.0*u[0] + u[npx−1])/dx**2 )
m.Equations([v[i+1].dt()== c**2*(u[i+2]−2.0*u[i+1]+u[i])/dx**2 for i in range(npx−2)])
m.Equation(v[npx−1].dt()== c**2 * (u[npx−2] − 2.0*u[npx−1] + u[0])/dx**2 )

# set options
m.options.imode = 4
m.options.solver = 1
m.options.nodes = 3

# solve
m.solve()
