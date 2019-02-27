from vpython import *
import random

"""
Simulate the growth of ferns (fractial) in 3-dimensions. Simply beautiful.
"""

imax = 200000 # points
x = .5
y = 0
z = -2
xn = 0
yn = 0

graph1 = display(width=500, height=500, forward=(-1,1),\
                title="3D Fractal Fern (rotate via right mosue button)", range=10)
graph1.show_rendertime = True
