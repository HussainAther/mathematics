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

The program dftcor, below, implements the endpoint corrections for the cubic case. Given input values of omega, delta, a, b, and an array of endpoint corrections in equation for I(omega_n).

it returns the real and imaginary parts of the endpoint corrections in equation (13.9.13), and the factor W.􏰌/. The code is turgid, but only because the formulas above are complicated. The formulas have cancellations to high powers of 􏰌. It is therefore necessary to compute the right-hand sides in double precision, even when the corrections are desired only to single precision. It is also necessary to use the series expansion for small values of 􏰌. The opti- mal cross-over value of 􏰌 depends on your machine’s wordlength, but you can always find it experimentally as the largest value where the two methods give identical results to machine precision.
"""

def DFTcor(w, delta, a, b, endpts):
    """
    For an integral approximated by a discrete Fourier transform, compute the correction factor
    that multiplies the DFT and the endpoint correction to be added. Input is angular frequency w, stepsize delta,
    lower and upper limits of integral a and b, and array endpoints contain the first 4 and last 4 functiona values.
    The correction factor is returned as crofac while the real and imaginary parts of the endpoint
    correction are returned as corre and corim.
    """
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
    cl = a0r * endpts[0] + a1r*endpts[1]+a2r*endpts[2]+a3r*endpts[3]
    sl = a0i * endpts[0] +a 1i*endpts[1]+a2i*endpts[2]+a3i*endpts[3]
    cr = a0r * endpts[7] + a1r*endpts[6]+a2r*endpts[5]+a3r*endpts[4]
    sr = -a0i * endpts[7] - a1i*endpts[6]-a2i*endpts[5]-a3i*endpts[4]
    arg=w * (b - a)
    c = cos(arg)
    s = sin(arg)
    corre = cl + c * cr - s * sr
    corim = sl + s * cr + c * sr
    return corfac, corre, corim

def Poly_interp(xx, yy, x, *mm):
    """
    Given a value x and data xx and yy, return an interpolated value y and store
    and error estimate dy. It uses mm-point polynomial interpolation.
    """
    i = 0
    m = 0
    ns = 0
    dift = 0
    if not mm:
        mm = 5
    j1 = len(xx) - (mm + 1)
    xa = xx[j1]
    ya = yy[j1]
    c = [0]*mm
    d = [0]*mm
    diff = abs(x - xa[0])
    for i in range(0, mm): # find index ns of closest table entry
        if (dift = abs(x-xa[i])) < dif):
            ns = i
            dif = dift
        c[i] = ya[i] # initialize tableu of c's and d's
        d[i] = ya[i]
    y = ya[ns - 1]
    for m in range(1, mm):
        for i in range(0, mm-m): # loop over c's and d's and update them.
            ho = xa[i] - x
            hp = xa[i+m] - x
            w = c[i+1] - d[i]
            if ((den=ho-hp) ==0):
                print("return polyinterpolation error") # if two input xa's are identical
            den = w/den
            d[i] = hp * den
            c[i] = ho * den
        if (ns+1) < (mm-m)):
            dy = (2* c[ns+1])
            y += dy
        else:
            dy = (2* d[ns-1])
            y += dy
    return y, dy


def DFTint(func, a, b):
    """
    User supplies an external function func that returns the quantity h(t).
    Return integral of a to be of cos(omega*t)*h(t)*dt as cosint and
    integral of a to be of sin(omega*t)*h(t)*dt as sinint.
    """
    init = 0
    aold = -1e30
    bold = -1e30

    # illustrative values that should be optimized for a particular application. #
    M = 64 # number of subintervals
    NDFT = 1024 # length of the Fast Fourier transform (power of 2)
    MPOL = 6 # degree of polynomial interpolation used to obtain the desired frequency from the Fast Fourier transform

    data = [""]*NDFT
    endpoints = [""]*8
    funcold = ""
    if init != 1 or a != aold or b != bold or func != funcold:
        init = 1
        aold = a
        bold = b
        funcold = func
        delta = (b-a)/M
        for j in range(0, M):
            data[j] = func(a+j*delta)
        for j in range(M+1, NDFT):
            data[j] = 0
        for j in range(0, 4):
            endpoints[j] = data[j]
            endpoints[j+4] = data[M-3+j]
        FFT(data)
        data[1] = 0
        en = w*delta*NDFT/(2*np.pi + 1)
        nn = min(max(int(en - .5*MPOL + 1),1), NDFT/2-MPOL+1) # leftmost point for interpolation
        for j in range(0, MPOL):
            cpol[j] = data[2*nn-2]
            spol[j] = data[2*nn-1]
            xpol[j] = nn
        cdft, cdftdy = Poly_interp(xpol, cpol, MPOL).interp(en)
        sdft, sdftdy = Poly_interp(xpol, spol, MPOL).interp(en)
        (corfac, corre, corim) = DFTcor(w, delta, a, b, endpoints)
        cdft *= corfac
        sdft *= corfac
        cdft += corre
        sdft += corim
        c = delta * np.cos(w * a)
        s = delta * np.sin(w * a)
        cosint = c * cdft - s * sdft
        sinint = s * cdft + c * sdft
        return cosint, sinint

