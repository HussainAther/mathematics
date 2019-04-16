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

def random_rotation(image_array: ndarray):
    """
    Random degree of rotation.
    """
    random_degree = random.uniform(-25, 25)
    return sk.transform.rotate(image_array, random_degree)

def random_noise(image_array: ndarray):
    """
    Make some noise.
    """
    return sk.util.random_noise(image_array)

def horizontal_flip(image_array: ndarray):
    """
    As easy as 1, 2, 3.
    """
    return image_array[:, ::-1]

