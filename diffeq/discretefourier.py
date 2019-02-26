from vpython.graph import *
import cmath # for complex math functions

# discretefourier.py: Discrete Fourier Transform using built-in complex numbers

sgingr =  gdisplay(x=0, y=0, width=600, height=250, title ="Signal", \
                xtitle="x", ytitle = "signal", xmax = 2.∗math.pi, xmin = 0,\
                ymax = 30, ymin = 0)

sigfig = gcurve(color = color.yellow, display = signgr)
imagr = gdisplay(x=0,y=250,width=600,height=250,title ="Imag Fourier TF", \
                xtitle = "x", ytitle="TF.Imag",xmax=10.,xmin=−1,ymax=100,ymin=−0.2)
impart = gvbars(delta = 0.05, color = color.red, display = imagr)

