import numpy as np

"""
The sine-Gordon (sine gordon sinegordon) equation is a nonlinear
partial differential equation:

u_tt - ∆u = -sin(u)

There are then three cases of dimensional lattices given by:

u_tt - u_xx = -sin(u)
u_tt - u_xx - u_yy = -sin(u)
u_tt - u_xx - u_yy - u_zz = -sin(u)

They have 1-, 2-, and 3-soliton solutions:

1-soliton:
phi(x, t) = 4arctan(exp(mγ(x-vt)+δ)
where
γ^2 = 1/(1-v^2)

2-soliton:

3-soliton:
Standing breather collides with a moving kink so the shift
of the standing breather is
∆_B = 2arctan(sqrt((1-ω^2)(1-v_K^2)))/(sqrt(1-ω^2))

for v_K velocity of the kink and ω the breather's frequency.
"""

def sg1sol(x, v, t):
    """
    Sine-Gordon 1-soliton solutions
    """
    g = 1/(1-v**2)
    gs = np.sqrt(g)
    phi = 4*np.arctan(np.exp(mgs(x-v*t)))
    return phi
    
"""
We can use the partial differentials of phi in a more general
form of the sine-Gordon equation.
phi_tt - phi_xx + m^2sin(phi) = 0  
""" 

def aback(phi, dphi, beta):
    """
    Use the auto-Bäcklund transform to show that, if u is a solution of the
    sine-Gordon equation (u_xy = sin(u)), then the system of two equations
    v_x = u_x + 2asin((v+u)/2)
    v_y = -u_y + (2/a)(sin((v-u)/2))
    (for arbitrary parameter a) is solvable with function v that also
    satisfies the sine-Gordon equation.
  
    For the output solution phi for the 1-soliton, we can differentiate
    phi and use it (with arbitrary parameter beta). For this function, we
    need phi to be a tuple with coordinates (u, v) and dphi to be a single
    value. 
    """
    dphiuv = ["", ""]
    dphiuv[0] = phi[0] + 2*beta*np.sin((dphi+phi)/2) 
    dphiuv[1] = -phi[1] + (2/beta)*np.sin((dphi-phi)/2)
    return dphiuv

def deltaB(omega, v_K):
    """
    Breather shift for 3-soliton solution 
    """
    return 2*np.arctan(np.sqrt((1-omega**2)*(1-v_K**2)))/np.sqrt(1-omega**2)

