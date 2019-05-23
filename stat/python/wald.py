import numpy as np

from scipy import stats

"""
Wald test as an asymptotic test. We decide whether to reject the 
Wald statistics. 
"""

theta0 = .5 # Null hypothesis H0
k = np.random.binomial(1000, .3)
thetahat = k/1000 # Maximum likelihood estimation (MLE)
W = (thetahat-theta0)/np.sqrt(thetahat*(q-thetahat)/1000)
c = stats.norm().isf(0.04/2) # z_alpha/2
print(abs(W)>c) # If true, reject null hypothesis
