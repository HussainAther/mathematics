import numpy as np

from vpython.graph import color, gcurve, gdisplay, rate

"""
When we add two sine functions with nearly identical frequences, we obtain beats. Sick!

y(t) = A sin(30t) + A sin(33t)
"""

graph = gdisplay(x=0, y=0, width=500, height=300, title="Beats: f(x)=np.sin(30x)+np.sin(33x)"
    xtitle="x", title="f(x)", xmax=5.0, xmin=0.0, ymax=2, ymin=-2, foreground=color.black,
    background=color.white)

function = gcurve(color=color.red)
for x in range(0, 5, .01):
    rate(40)
    y = np.sin(30*x) + np.sin(33*x)
    function.plot(pos=(x,y))
