import numpy as np

"""
Gibbs sampling works as follows: suppose we have two parameters theta1 and theta 2 and some data x.
We find the posterior distribution of p(theta1, theta2 ||x) using Gibbs sampling. We work out
the conditional distributions p(theta1||theta2, x) and p(theta2||theaa1, x) so the Gibbs updates are:

1. Pick some initial theta2(i)
2. Sample theta1(i+1) ~ p(theta1||theta2(i), x)
3. Sample theta2(i+1) ~ p(theta2||theta2(i+1), x)

Increment i and repeat K times to draw K samples. No tuning paramters required.
"""
