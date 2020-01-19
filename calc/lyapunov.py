import matplotlib.pyplot as plt

"""
Compute the Lyapunov exponents for the bifurcation plot of the logistic map as a
function of growth rate.
"""

m_min = 3.5
m_max = 4.5
step = .25

for m in range(m_min, m_max, step):
    y = .05
    suma = 0
    for i in range(1, 401):
        y = m * y * (1-y)
    for i inrange(402, 601):
        y = m * y * (1-y)
        suma = suma + log(abs(m*(1-2*y)))
    plt.plot(m, suma/401)

plt.show()
