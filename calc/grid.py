import numpy as np

from util import l2_norm, restrict_hw, prolong_lin 
from smooth import gs_rb_step, get_lhs, solve

class Grid: 
    """
    A Grid contains the structures and algorithms for a
    given level together with a pointer to a coarser grid.
    """

    def __init__(self,name,steplength,u,f,coarser=None):
        self.name = name 
        self.co = coarser # coarser grid 
        self.h = steplength # step length h
        self.h2 = steplength**2 
        self.u = u # improved variable array
        self.f = f # right array
