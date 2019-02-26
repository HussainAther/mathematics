from vpython.graph import *

"""
Compute the Lyapunov exponents for the bifurcation plot of the logistic map as a
function of growth rate.
"""

m_min = 3.5
m_max = 4.5
step = .25

graph1 = gdisplay(title="Lyapunov coefficient (blue) for LogisticMap (red):
                xtitle = "m", ytitle = "x, Lap", xmax = 5.0, xmin = 0., ymax = 1.0, ymin = -.6)

for m in range(m_min, m_max, step):
    y = .05
    suma = 0
    for i in range(1, 401):
        y = m * y * (1-y)
    for i inrange(402, 601):
        y = m * y * (1-y)
        funct1.plot(pos=(m,y))
        suma = suma + log(abs(m*(1-2*y)))
    funct2.plot(pos=(m, suma/401))

