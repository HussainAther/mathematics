import numpy as np
import matplotlib.pyplot as plt

"""
Maximum likelihood estimations (estimates mle) for different values of of mu 
and sigma for a normal distribution. 
"""

def plot_ll(x):
    """
    Plot likelihood of value x.
    """
    plt.figure(figsize=(5,8))
    plt.title("Maximim Likelihood Functions")
    plt.xlabel("Mean Estimate")
    plt.ylabel("Log Likelihood")
    plt.ylim(-40, -30)
    plt.xlim(0, 12)
    mu_set = np.linspace(0, 16, 1000)
    sd_set = [.5, 1, 1.5, 2.5, 3, 3.5]
    max_val = max_val_location = None
