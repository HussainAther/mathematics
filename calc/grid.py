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
        Carry out Newton-Raphson/Gauss-Seidel red-black
        iteration u->u, nu times. (red black red-black)
        Newton Raphson Gauss Seidel
        """
        print("Relax in %s for %d times" % (self.name,nu) v=self.u.copy())
        for i in range(nu):
            v=gs_rb_step(v,self.f,self.h2) 
        self.u=v

    def fas_v_cycle(self,nu1,nu2):
        """ 
        Recursive implementation of (nu1, nu2) FAS V-Cycle.
        """ 
        print("FAS-V-cycle called for grid at %s\n" % self.name)
        # Initial smoothing
        self.smooth(nu1)
        if self.co:
            # There is a coarser grid 
            self.co.u=restrict_hw(self.u)
            # Get residual 
            res=self.f-get_lhs(self.u,self.h2)
            # get coarser f 
            self.co.f=restrict_hw(res)+get_lhs(self.co.u, self.co.h2)
            oldc=self.co.u
            # Get new coarse solution 
            newc=self.co.fas_v_cycle(nu1,nu2)
            # Correct current u
            self.u+=prolong_lin(newc-oldc)
        self.smooth(nu2)
        return self.u 

    def fmg_fas_v_cycle(self,nu0,nu1,nu2):
        """ 
        Recursive implementation of FMG-FAS-V-Cycle.
        """
        print("FMG-FAS-V-cycle called for grid at %s\n" % self.name)
        if not self.co:
            # Coarsest grid
            self.u=solve(self.f)
        else:
            # Restrict f
            self.co.f=restrict_hw(self.f)
            # Use recursion to get coarser u
            self.co.u=self.co.fmg_fas_v_cycle(nu0,nu1,nu2)
            # Prolong to current u
            self.u=prolong_lin(self.co.u)
        for it in range(nu0):
            self.u=self.fas_v_cycle(nu1, nu2)
        return self.u
