from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

# Generate "data" with process simulation
nt = 51
# input steps
u_meas = np.zeros(nt)
u_meas[3:10] = 1.0
u_meas[10:20] = 2.0
u_meas[20:40] = 0.5
u_meas[40:] = 3.0
# simulation model
p = GEKKO()
p.time = np.linspace(0,10,nt)
n = 1 #process model order
# Parameters
steps = np.zeros(n)
p.u = p.MV(value=u_meas)
p.u.FSTATUS=1
p.K = p.Param(value=1) #gain
p.tau = p.Param(value=5) #time constant
# Intermediate
p.x = [p.Intermediate(p.u)]
# Variables
p.x.extend([p.Var() for _ in range(n)])  #state variables
p.y = p.SV() #measurement
# Equations
p.Equations([p.tau/n * p.x[i+1].dt() == -p.x[i+1] + p.x[i] for i in range(n)])
p.Equation(p.y == p.K * p.x[n])
# Simulate
p.options.IMODE = 4
p.solve(disp=False)
# add measurement noise
y_meas = (np.random.rand(nt)-0.5)*0.2
for i in range(nt):
    y_meas[i] += p.y.value[i]
plt.plot(p.time,u_meas,'b:',label='Input (u) meas')
plt.plot(p.time,y_meas,'ro',label='Output (y) meas')
plt.plot(p.time,p.y.value,'k-',label='Output (y) actual')
plt.legend()
plt.show()

