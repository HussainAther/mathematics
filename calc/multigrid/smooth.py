import numpy as np

"""
Problem-dependent 2-D utilities.
"""

def get_lhs(u,h2):
    w=np.zeros_like(u) w[1:-1,1:-1]=(u[0:-2,1:-1]+u[2: ,1:-1]+
               u[1:-1,0:-2]+u[1:-1,2: ]-
               4*u[1:-1,1:-1])/h2+u[1:-1,1:-1]*u[1:-1,1:-1]
    return w

def gs_rb_step(v,f,h2): u=v.copy()
   res=np.empty_like(v)
   res[1:-1:2,1:-1:2]=(u[0:-2:2,1:-1:2]+u[2: :2,1:-1:2]+
                     u[1:-1:2,0:-2:2]+u[1:-1:2,2: :2]-
                     4*u[1:-1:2,1:-1:2])/h2 +\
                     u[1:-1:2,1:-1:2]**2-f[1:-1:2,1:-1:2]
   u[1:-1:2, 1:-1:2]-=res[1:-1:2,1:-1:2]/(
                             -4.0/h2+2*u[1:-1:2,1:-1:2])
   res[2:-2:2,2:-2:2]=(u[1:-3:2,2:-2:2]+u[3:-1:2,2:-2:2]+
                     u[2:-2:2,1:-3:2]+u[2:-2:2,3:-1:2]-
                     4*u[2:-2:2,2:-2:2])/h2+\
                     u[2:-2:2,2:-2:2]**2-f[2:-2:2,2:-2:2]
   u[2:-2:2,2:-2:2]-=res[2:-2:2,2:-2:2]/(
                            -4.0/h2+2*u[2:-2:2,2:-2:2])
   res[2:-2:2,1:-1:2]=(u[1:-3:2,1:-1:2]+u[3:-1:2,1:-1:2]+
                     u[2:-2:2,0:-2:2]+u[2:-2:2,2: :2]-
                     4*u[2:-2:2,1:-1:2])/h2 +\
                     u[2:-2:2,1:-1:2]**2-f[2:-2:2,1:-1:2]
   u[2:-2:2,1:-1:2]-=res[2:-2:2,1:-1:2]/(
                            -4.0/h2+2*u[2:-2:2,1:-1:2])
   res[1:-1:2,2:-2:2]=(u[0:-2:2,2:-2:2]+u[2: :2,2:-2:2]+
                     u[1:-1:2,1:-3:2]+u[1:-1:2,3:-1:2]-
                     4*u[1:-1:2,2:-2:2])/h2+\
                     u[1:-1:2,2:-2:2]**2-f[1:-1:2,2:-2:2]
   u[1:-1:2,2:-2:2]-=res[1:-1:2,2:-2:2]/(
                            -4.0/h2+2*u[1:-1:2,2:-2:2])
                                                                                   
