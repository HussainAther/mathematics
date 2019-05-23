import numpy as np

from scipy import stats

"""
Wald test as an asymptotic test. We decide whether to reject the 
Wald statistics. 
"""

theta0 = .5 # Null hypothesis
k = np.random.binomial(1000, .3)
