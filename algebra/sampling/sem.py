import numpy as np
import random
import skimage as sk

from scipy import ndarray
from skimage import transform
from skimage import util

"""
With the supplemental expectation maximization algorithm, we get the covariance matrix by
using only the code for computing the complete-data covariance matrix, the code for the expectation
maximization itself, and the code for standard matrix operations.
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
