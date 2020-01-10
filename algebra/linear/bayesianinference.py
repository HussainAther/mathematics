import numpy as np
import matplotlib.pyplot as plt
import torch

from scipy.special import gamma as gf
from torch import tensor
from torch.distributions.normal import Normal
from torch.distributions.gamma import Gamma
from torch.distributions.multivariate_normal import MultivariateNormal as MN
from torch.distributions.uniform import Uniform

"""
Bayesian inference in generative models

In this tutorial, we write several different inference methods for a simple Bayesian linear regression model. 

1. Defining the generative model
2. Exact posterior inference
3. Markov Chain Monte Carlo using Metropolis Hastings
4. Classic variational inference using a mean-field approximation
5. Stochastic variational inference
    
"""
