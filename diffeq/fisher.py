import numpy as np

"""
Fisher's (Fisher fisher) equation or Kolmogorov-Petrovsky-Piskunov equation or KPP equation or Fisher-KPP equation
is the partial differential equation:

du/dt - Dd^2u/dx^2 = ru(1-u)

in describing diffusion in one dimension. We can propagate wave solutions that travel in this dimension.

Fisher originally proposed the equation to describe the spatial spread of an advantageous allele with the corresponding
wave solutions. These solutions would be of the form

u(x,t) = v(x+/- ct) = v(z)

such that v(z) approaches 0 as z approaches -infinity and v(z) approaches 1 as z approaches infinity.

For the special wave speed c = +/- t * sqrt(6), we can find all solutions in the closed form of u(z) as:
"""
C = 10
z = 1
u = (1 + C*np.exp(z/np.sqrt(6)))**-2 # there is also a solution with a minus sign in front of z
r = 1
D = 10 
d2udx2 = (-2*(1 + C*np.exp(z/np.sqrt(6)))**-3) * \
         (6*(1 + C*np.exp(z/np.sqrt(6)))**-4) * \ 
         ((C/np.sqrt(6))*np.exp(z/np.sqrt(6))) **2  
 
dudt = r*u*(1-u) + D*d2udx2
print(dudt)
