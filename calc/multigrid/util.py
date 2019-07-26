import numpy as np

def l2_norm(a,h):
    return h*np.sqrt(np.sum(a**2))

def prolong_lin(a): 
    pshape = (2*np.shape(a)[0]-1,2*np.shape(a)[1]-1) 
    p = np.empty(pshape,float)
    p[0: :2,0: :2] = a[0: ,0: ]
    p[1:-1:2,0: :2] = 0.5*(a[0:-1,0: ]+a[1: ,0: ]) 
    p[0: :2,1:-1:2] = 0.5*(a[0: ,0:-1]+a[0: ,1: ]) 
    p[1:-1:2,1:-1:2] = 0.25*(a[0:-1,0:-1]+a[1: ,0:-1] + a[0:-1,1: ]+a[1: ,1: ]) 
    return p

def restrict_hw(a): 
    rshape = (np.shape(a)[0]/2+1,np.shape(a)[1]/2+1) 
    r = np.empty(rshape,float) 
    r[1:-1,1:-1]=0.5*a[2:-1:2,2:-1:2] + 0.125*(a[2:-1:2,1:-2:2]+a[2:-1:2,3: :2] + a[1:-2:2,2:-1:2]+a[3: :2,2:-1:2])
    r[0,0: ] = a[0,0: :2] 
    r[-1,0: ] = a[-1,0: :2] 
    r[0: ,0] = a[0: :2,0] 
    r[0: ,-1] = a[0: :2,-1] 
    return r

if __name__ == "__main__":
    a = np.linspace(1,81,81)
    b = a.reshape(9,9)
    c = restrict_hw(b)
    d = prolong_lin(c)
    print("original grid\n", b)
    print("with spacing 1 its norm is ",l2_norm(b,1))
    print("\n restricted grid\n", c)
    print("\n prolonged restricted grid\n", d)
