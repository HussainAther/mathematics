from PyDSTool import *
from matplotlib import pyplot as plt
from numpy.linalg import eig

"""
In the mathematical theory of bifurcations, a Hopf bifurcation is a critical point where a system's stability
switches and a periodic solution arises. More accurately, it is a local bifurcation in which a fixed point of
a dynamical system loses stability, as a pair of complex conjugate eigenvalues - of the linearization around
the fixed point - crosses the complex plane imaginary axis. Under reasonably generic assumptions about the
dynamical system, a small-amplitude limit cycle branches from the fixed point. It's also called a Poincaré-Andronov-Hopf bifurcation.
"""

def make_A(tau):
    """
    Jacobian matrix of the differentiated forms of our system of equations.
    """
    return array([[-1./20, 0, 0, -1./20],
               [1./tau, -1./tau, 0, 0],
               [0, 6./50, -1./50, 0],
               [0, 0, 1./tau, -1./tau]])


cols = ["r", "g", "k", "b"]

plt.plot([-0.3, 0.01], [0, 0], 'k')
plt.plot([0, 0], [-0.15, 0.15], 'k')
plt.xlabel("real")
plt.ylabel("imag")
plt.show()

# Boolean flag initialization
Hopf_found = False

taus = linspace(0.05, 15, 100)

# keep the "handle" of the text object so that we can update it later
t = plt.text(-0.2, 0.12, 'tau = %.3f' % 0.05, fontsize=20)

plt.title("Eigenvalues of f.p.")

for i, tau in enumerate(taus):
    # [0] is eigenvalues, [1] is eigenvectors
    evals = eig(make_A(tau))[0]
    for j, e in enumerate(evals):
        re = real(e)
        im = imag(e)
        if re > 0 and not Hopf_found:
            # assumes that we know the eigenvalues started negative real part
            print("Hopf found near tau = %.4f (index %i)" % (tau, i))
            Hopf_found = True
        plt.plot(re, im, cols[j]+".")
        plt.xlim([-0.3, 0.01])
        plt.ylim([-0.15, 0.15])
        t.set_text("tau = %.3f" % tau)
        plt.draw()
