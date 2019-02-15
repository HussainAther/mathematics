import pandas as pd
import numpy as np
import scipy.stats

"""
Inverse cumulative distribution function

Suppose we want to generate samples from a fair six-sided die. Our workhouse uniform random variable is defined continuously
over the unit interval and the fair six-sided die is discrete. We must first create a mapping between the continuous random
variable u and the discrete outcomes of the die. Each individual segment is assigned to one of the die outcomes. For example,
if u ∈ [1/6, 2/6), then the outcome for the die is 2. Because the die is fair, all segments on the unit interval are the same
length. Thus, our new random variable v is derived from u.

The method is called the inverse CDF3 method because the CDF (namely,[0,1/12,2/12,3/12,2/4,3/4,1])
 has been inverted (using the pd.cut method) to generate the samples. The inversion is easier to
 see for continuous variables, which we consider next.
"""

u = np.random.rand(100)
df = pd.DataFrame(data=u,columns=["u"])

labels = [1,2,3,4,5,6]
df["v"]=pd.cut(df.u,np.linspace(0,1,7), include_lowest=True,labels=labels)

df.head()

df.groupby("v").count()


"""
The method above applies to continuous random variables, but now we have to use squeeze the intervals down to individual points.
In the example above, our inverse function was a piecewise function that operated on uniform random samples. In this case, the
piecewise function collapses to a continuous inverse function. We want to generate random samples for a CDF that is invertible.
As before, the criterion for generating an appropriate sample v is the following,

P(F(x) < v < F(x+Δx)) = F(x+Δx) − F(x) = integral from x to x + Δx: f(u)du ~ f(x)Δx
"""

from numpy import array, log

alpha = 1.   # distribution parameter
nsamp = 1000 # num of samples
# define uniform random variable
u = scipy.stats.uniform(0,1)
# define inverse function
Finv = lambda u: 1/alpha*log(1/(1-u))
# apply inverse function to samples
v = np.array(map(Finv,u.rvs(nsamp)))

"""
In some cases, inverting the CDF may be impossible. The rejection method can handle this situation.
The idea is to pick two uniform random variables u1, u2 ∼ U[a, b] so that

P( u_1 ∈ NΔ(x) ^ u_2 < f(u_1) / M) ≈ Δx / (b−a) * f(u_1)/ M

where we take x = u1 and f (x) < M. This is a two-step process. First, draw u1 uniformly from the interval
[a, b]. Second, feed it into f (x) and if u2 < f (u1)/M, then you have a valid sample for f (x). Thus,
u1 is the proposed sample from f that may or may not be rejected depending on u2. The only job of the M constant
is to scale down the f (x) so that the u2 variable can span the range. The efficiency of this method is the
probability of accepting u1 which comes from integrating out the above approximation,

integral: (f(x) / M(b−a))dx = 1 / (M(b−a)) * integral: f(x)dx = 1 / (M(b−a))

This means that we don’t want an unecessarily large M because that makes it more likely that samples will be discarded.
"""

# Rejection method for continuous function f(x) = exp(− (x-1)^2 / 2x) * (x + 1)/12

x = np.linspace(0.001,15,100)
f = lambda x: np.exp(-(x-1)**2/2./x)*(x+1)/12.
fx = f(x)
M=0.3                          # scale factor
u1 = np.random.rand(10000)*15  # uniform random samples scaled out
u2 = np.random.rand(10000)     # uniform random samples
idx,= np.where(u2<=f(u1)/M)    # rejection criterion
v = u1[idx]
