import random
from vpython.graph import *

"""
Monte Carlo integration via stone throwing.
"""

N = 100 # points to plot the function
graph = display(width=500, height=500, title="vonNeumann Rejection Int")
xsinx = curve(x=list(range(0,N)) color=color.yellow, radius=.5) # generate sine curve
pts = label(pos=(-60, -60), text="points=", box=0) # graphics
pts2 = label(pos=(-30, -60), box=0)
inside = label(pos=(30, -60), text="accepted=", box=0)
inside2 = label(pos=(60, -60), box=0)
arealbl = label(pos=(-65,60), text="area=", box=0)
arealbl2 = label(pos=(-35, 60), box=0)
areanal = label(pos(30, 60), text="analytical=", box=0)
zero = label(pos=(-85, -48), text="0", box=0)
five = label(pos=(-85, 50), text="5", box=0)
twopi = label(pos=(90, -48), text="2pi", box=0)

def fx(x): # Integrand
    return x*sin(x)*sin(x)

def plotfunction(): # Plot hte function and the box
    inc = 2*pi/N
    for i in range(0, N):
        xx = i*incr
        xsinx.x[i] = ((80/pi)*xx-80)
        xsinx.y[i] = 20*fx(xx)-50
        box = curve(pos=[(-80, -50), (-80, 50), (80, 50), (80, -50), (-80, -50)], color=color.white)

plotfunction() # get to it!
j = 0
Npts = 3001 # poiints generated inside the box
analyt = pi**2 # analytical integral
areanal.text = "analytical=%8.5f"%analyt # output analytical integral
genpts = points(size=2)

for i in range(1, Npts): # generate points inside the box
    rate(500)
    x = 2*pi*random.random()
    y= 5*random.random()
