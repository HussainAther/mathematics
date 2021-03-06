import numpy as np
import matplotlib.pyplot as plt

from scipy import signal
from sklearn.decomposition import FastICA, PCA

"""
Independent component analysis on sample simulated data.
"""

# Generate data.
np.random.seed(1234)
n_samples = 2000
time = np.linspace(0, 8, n_samples)
s1 = np.sin(2 * time)  # Signal 1 : sinusoidal signal
s2 = np.sign(np.sin(3 * time))  # Signal 2 : square signal
s3 = signal.sawtooth(2 * np.pi * time)  # Signal 3: sawtooth signal
S = np.c_[s1, s2, s3]
S += 0.2 * np.random.normal(size=S.shape)  # Add noise.
S /= S.std(axis=0)  # Standardize data.
# Mix data.
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # Mixing matrix
X = np.dot(S, A.T)  # Generate observations.
# Compute ICA.
ica = FastICA(n_components=3)
S_ = ica.fit_transform(X) # Get the estimated sources.
A_ = ica.mixing_ # Get estimated mixing matrix.

# Compute PCA (principal component analysis).
pca = PCA(n_components=3)
H = pca.fit_transform(X) # Estimate PCA sources.

plt.figure(figsize=(9, 6))

models = [X, S, S_, H]
names = ["Observations (mixed signal)",
         "True Sources",
         "ICA estimated sources",
         "PCA estimated sources"]
colors = ["red", "steelblue", "orange"]

for ii, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(4, 1, ii)
    plt.title(name)
    for sig, color in zip(model.T, colors):
        plt.plot(sig, color=color)

plt.tight_layout()
plt.show()
