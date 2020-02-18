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
"""

def sg1sol(x, v, t):
    """
    Sine-Gordon 1-soliton solutions
    """
    g = 1/(1-v**2)
    gs = np.sqrt(g)
    return 4*np.arctan(np.exp(mgs(x-v*t)))
     
