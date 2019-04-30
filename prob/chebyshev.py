import sympy
import simpy.stats as ss

"""
Chebyshev’s Inequality (inequality) drops out directly from the Markov Inequality. Let μ = E( X ) 
and σ2 = V(X). Then, we have

P(|X − μ| ≥ t) ≤ σ^2 / t^2

ote that if we normalize so that Z = (X − μ)/σ, we have P(|Z| ≥ k) ≤ 1/k2. In particular, P(| Z | ≥ 2) ≤ 1/4.
We can illustrate this inequality using Sympy statistics module,
"""

t = sympy.symbols("t", real=True)
x = ss.ChiSquared("x", 1)

""" 
To get the left side of the Chebyshev inequality, we have to write this out 
as the following conditional probability,
"""

r = ss.P((x-1) > t,x>1)+ss.P(-(x-1) > t,x<1)

"""
Note that we cannot use vectorized inputs for the lambdify function because it contains embedded functions that are only
available in Sympy. Otherwise, we could have used lambdify(t,fw,numpy) to specify the corresponding functions in Numpy
to use for the expression.

This is because of certain limitations in the statistics module at this point in its devel- opment regarding the
absolute value function. We could take the above expression, which is a function of t and attempt to compute the
integral, but that would take a very long time (the expression is very long and complicated, which is why we did
not print it out above). This is because Sympy is a pure-python module that does not utilize any C-level optimizations
under the hood. In this situation, it’s better to use the built-in cumulative density function as in the following
(after some rearrangement of the terms),
"""

w = (1 - ss.cdf(x)(t+1)) + ss.cdf(x)(1-t)
fw = sympy.lambdify(t,w)

"""
To plot this, we can evaluate it at a variety of t values by using the .subs substitution method, but it is more
convenient to use the lambdify method to convert the expression to a function.
"""

map(fw,[0,1,2,3,4])
