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


