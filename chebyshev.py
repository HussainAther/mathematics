import sympy
import simpy.stats as ss

"""
Chebyshev’s Inequality drops out directly from the Markov Inequality. Let μ = E( X ) and σ2 = V(X). Then, we have

P(|X − μ| ≥ t) ≤ σ^2 / t^2

ote that if we normalize so that Z = (X − μ)/σ, we have P(|Z| ≥ k) ≤ 1/k2. In particular, P(| Z | ≥ 2) ≤ 1/4.
We can illustrate this inequality using Sympy statistics module,
"""

t = sympy.symbols("t", real=True)
x = ss.ChiSquared("x", 1)

# To get the left side of the Chebyshev inequality, we have to write this out as the following conditional probability,

r = ss.P((x-1) > t,x>1)+ss.P(-(x-1) > t,x<1)
