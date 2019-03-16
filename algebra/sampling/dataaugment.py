import numpy as np
import random
import skimage as sk

from scipy import ndarray
from skimage import transform
from skimage import util


"""
With the data augmentation algorithm, we alternate between the I-step (imputation step, analogous to
the E step of the EM algorithm) and the P-step (posterior step, analogous to M).
"""
