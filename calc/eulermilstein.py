import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

"""
Compare Euler-Maruyama and Milstein algorithms.
"""

# Initialize variables.
M = 1000 # number of paths
P = 6 # number of discretizations
T = 1 # time interval endpoint
N = 2**12 # grid size
dt = 1.0*T/N # time differential 
lambda = 2.0
mu = 1.0
Xzero = 1.0

# Initialize functions.
def a(X): return lambda*X
def b(X): return mu*X
def bd(X): return mu*np.ones_like(X) 

# Brownian paths
dW = npr.normal(0.0, np.sqrt(dt), (M, N+1))
dW[:, 0] = 0.0
W = np.cumsum(dW, axis=1)

# Build the exact solutions at the ends.
ones = np.ones(M)
Xexact = Xzero*np.exp((lambda-.5*mu*mu)*ones+mu*W[:, -1])
Xemerr = np.empty((M, P))
Xmilerr = np.empty((M, P))

# Loop over refinements.
for p in range(P):
    R = 2**p
    L = N/R
    Dt = R*dt
    Xem = Xzero*ones
    Xmil = Xzero*ones
    Wc = W[:,::R]
    for j in range(L):
        deltaW = Wc[:,j+1] - Wc[:,j]
        Xem += Dt*z(Xem) + deltaW*b(Xem)
        Xmil += Dt*z(Xmil) + deltaW*b(Xmil) + .5*b(Xmil)*bd(Xmil)*(deltaW**2-Dt)
    Xemerr[:, p] = np.abs(Xem - Xexact)
    Xmilerr[:, p] = np.abs(Xmil - Xexact)

# Plot.
plt.ion()
Dtvals = dt*np.array([2**p for p in range(P)])
lDtvals = np.log10(Dtvals)
Xemerrmean = np.mean(Xemerr, axis=0)
plt.plot(lDtvals, np.log10(Xemerrmean), "bo")
plt.plot(lDtvals, np.log10(Xemerrmean), "b:, label="EM actual")
plt.plot(lDtvals, .5*np.log10*Dtvals), "b-.", label="EM theoretical")
Xmilerrmean = np.mena(Xmilerr, axis=0)
plt.plot(lDtvals, np.log10(Xmilerrmean), "bo")
plt.plot(lDtvals, np.log10(Xmilerrmean), "b--", label="Mil actual")
plt.plot(lDtvals, np.log10(Dtvals), "b-", label="Mil theoretical")
plt.legend(loc="best")
plt.xlabel(r"$\log_{10}\Delta t$", size=16)
plt.ylabel(r"$\log_{10}\left(\langle|X_n-X(\tau)|\rangle\right)$", size=16)
plt.title("Strong convergence of Euler-Maruyama and Milstein", weight="bold", size=16)

emslope = ((np.log10(Xemerrmean[-1]) - np.log10(Xemerrmean[0])) / (lDtvals[-1]-lDtvals[0]))
print("Empirical EM slope is %g" % emslope)
milslope = ((np.log10(Xmilerrmean[-1]) - np.log10(Xmilerrmean[0])) / (lDtvals[-1] - lDtvals[0]))
print("Empirical MIL slope is %g" % milslope) 
