import cv2
import numpy as np
import sys
import scipy

from scipy.sparse.linalg import LinearOperator

"""
Ambrosio Tortorelli Minimizer of the Mumford-Shah functional.
Implementation of edge preserving smoothing by minimizing with 
the Ambrosio-Tortorelli appoach.
"""
