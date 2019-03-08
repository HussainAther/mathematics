import numpy as np

from fourier import *

"""
We can use the Fast Fourier transform to compute integrals of the form

integral from a to be of exp(i*omega*t) * h(t) * dt

which can be split up into real and imaginary parts

integral from a to be of cos(omega*t) * h(t) * dt and integral from a to be of sin(omega*t) * h(t) * dt
Taking advantage of hte oscillatory nature of the integral, if h(t) is at all smooth and omega is large
enough to imply several cycles in the interval [a, b], then the value of I is typically very small that it's sswamped
by the first-order error.

We use interpolation to approximate a function by a sum of kernel functions (which depend only on the intrepolation
scheme) times sample values (which depend only on the function). We write:

h(t) ~ summation of h_j from j=0 to M * psi(t-t_j)/delta + summation of j = endpoints * h_j * phi_j (t-t_j)/delta

Given sampled points h_j, we approximate h(t) everywhere in the interval [a, b] by interpolation on nearby h_j's.
We introduce a kernel function psi(s) of an interior point: it's zero for s sufficiently negative or sufficiently positive
and becomes nonezro only when s is in the range where h_j multiplying it is actually used in the interpolation.

There are two methods of interpolation: cubic and trapzeoidal. We can write a function with the terms for each of them.
"""

def DFTcor(w, delta, a, b):
    """
    For an integral approximated by a discrete Fourier transform, compute the correction factor
    that multiplies the DFT and the endpoint correction to be added. Input is angular frequency w, stepsize delta,
    lower and upper limits of integral a and b, and array endpoints contain the first 4 and last 4 functiona values.
    The correction factor is returned as crofac while the real and imaginary parts of the endpoint
    correction are returned as corre and corim.
    """
    endpoints = []
    for i in range(a, a+4):
        endpoints.append(np.exp(np.imag(j)*w * i))
    for i in range(b, b-4, -1):
        endpoints.append(np.exp(np.imag(j)*w * i))
    th = w*delta
    if a >= b or th < 0 or th > np.pi:
        print("bad arguments")
        return
    if abs(th) < 5e-2: # Use series method
        t = th # for convenience
        t2 = t*t
        t4 = t2*t2
        t6 = t4*t2
        corfact = 1-(11/720)*t4(23/15120)*t6
        a0r = (-2/3) + t2/45 + (103/15120) * t4 - (169/226800) * t6
        a1r = (7/24) - (7/180) * t2 + (t/3456) * t4 - (7/259200) * t6
        a2r = (-1/6) + t2/45 - (5/6048) * t4 + t6/64800
        a3r = (1/24) - t2/180 + (5/24192) * t4 - t6/259200
        a0i = t*(2/45 + (2/105) * t2 - (8/2835) * t4 + (86/467775) * t6)
        a1i = t*(7/72 - t2/168 + (11/72576) * t4 - (13/5987520) *t6)
        a2i = t*(-7.0/90.0+t2/210.0-(11.0/90720.0)*t4+(13.0/7484400.0)*t6)
        a3i=t*(7.0/360.0-t2/840.0+(11.0/362880.0)*t4-(13.0/29937600.0)*t6);
    else: # use trigonometric formulas
        cth = cos(th)
        sth = sin(th)
        ctth = cth*cth-sth*sth
        stth = 2.0e0*sth*cth
        th2 = th*th
        th4 = th2*th2
        tmth2 = 3.0e0-th;
        spth2 = 6.0e0+th2
        sth4i = 1.0/(6.0e0*th4)
        tth4i = 2.0e0*sth4i
        corfac = tth4i*spth2*(3.0e0-4.0e0*cth+ctth)
        a0r = sth4i*(-42.0e0+5.0e0*th2+spth2*(8.0e0*cth-ctth))
        a0i = sth4i*(th*(-12.0e0+6.0e0*th2)+spth2*stth)
        a1r = sth4i*(14.0e0*tmth2-7.0e0*spth2*cth)
        a1i = sth4i*(30.0e0*th-5.0e0*spth2*sth)
        a2r = tth4i*(-4.0e0*tmth2+2.0e0*spth2*cth)
        a2i = tth4i*(-12.0e0*th+2.0e0*spth2*sth)
        a3r = sth4i*(2.0e0*tmth2-spth2*cth)
        a3i = sth4i*(6.0e0*th-spth2*sth)
    cl = a0r*endpts[0]+a1r*endpts[1]+a2r*endpts[2]+a3r*endpts[3]
    sl = a0i*endpts[0]+a1i*endpts[1]+a2i*endpts[2]+a3i*endpts[3]
    cr = a0r*endpts[7]+a1r*endpts[6]+a2r*endpts[5]+a3r*endpts[4]
    sr = -a0i*endpts[7]-a1i*endpts[6]-a2i*endpts[5]-a3i*endpts[4]
