from sklearn.linear_model import Perceptron
from sklearn.ensemble import AdaBoostClassifier, BaggingClassifier
from sklearn.ensemble import BaggingClassifier

"""
The perceptron uses bagging. Bagging is bootstrap aggregating that uses
sampling and resampling to reduce collective variance in high-variance
models. With a two-dimensional plane that 
partitions into two regions at a boundary, we can identify points
above the boundary as one and the ones below as zero. We take
samples from each of these regions as a linear classifier that
finds the line to separate the two categories.
"""

p = Perceptron()

bp = BaggingClassifier(Perceptron(), max_samples=.5, n_estimators=3)


"""
Boosting classifier Adaptive boosting (adaboost). 
"""

clf = AdaBoostClassifier(Perceptron(), n_estimators=3, algorithm="SAMME", learning_rate=0.5)
