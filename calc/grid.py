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

    def __str__(self):
        """ 
        Generate an information string about this level. 
        """ 
        sme = "Grid at %s with steplength = %0.4g\n" % (
            self.name, self.h)
        if self.co:
            sco = "Coarser grid with name %s\n" % self.co.name
        else:
            sco = "No coarser grid\n"
        return sme+sco
 
   def smooth(self,nu): 
        """
        Carry out Newton--Raphson/Gauss--Seidel red--black
        iteration u-->u, nu times.
        """
        print("Relax in %s for %d times" % (self.name,nu) v=self.u.copy())
        for i in range(nu):
            v=gs_rb_step(v,self.f,self.h2) 
        self.u=v

